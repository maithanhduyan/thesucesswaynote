#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BBooks Subtitle Downloader - Chuyên download subtitle dạng SRT
Tool chuyên dụng để download phụ đề .srt cho video BBooks
"""

import subprocess
import os
import re
import json
import csv
from pathlib import Path
from datetime import datetime

# =====================================================
# CONFIGURATION
# =====================================================
BASE_DIR = Path(__file__).parent.parent
YTDLP_EXE = BASE_DIR / ".tools" / "yt-dlp.exe"  # Updated path to .tools/yt-dlp.exe
CSV_FILE = BASE_DIR / "listbook.csv"
LOG_FILE = BASE_DIR / "subtitle_download.log"

# Subtitle settings - Tối ưu cho SRT
SUBTITLE_LANGS = (
    "vi,en,auto"  # Vietnamese ưu tiên, English fallback, auto-generated cuối
)
SUBTITLE_FORMAT = "srt"  # Chỉ format SRT
SUB_FILE_FORMAT = (
    "%(title)s [id=%(id)s].%(lang)s.%(ext)s"  # Format: Title [id=VideoID].vi.srt
)

# Control settings
DRY_RUN = False  # Set True để test
VERBOSE = False
MAX_RETRIES = 2
OVERWRITE_EXISTING = False  # Set True để overwrite subs đã có

# =====================================================
# UTILITY FUNCTIONS
# =====================================================


def log_message(message, level="INFO"):
    """Logging với timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_line = f"[{timestamp}] {level}: {message}"
    print(log_line)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")
    except:
        pass


def clear_log():
    """Xóa log file cũ"""
    try:
        if LOG_FILE.exists():
            LOG_FILE.unlink()
        log_message("🧹 Cleared old log file")
    except:
        pass


def srt_to_markdown(srt_file_path, markdown_file_path, video_title):
    """Chuyển đổi file SRT thành Markdown, chỉ giữ lại nội dung text"""
    try:
        with open(srt_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse SRT content
        # SRT format:
        # 1
        # 00:00:01,000 --> 00:00:04,000
        # Text content here
        # (blank line)

        # Split by blank lines to get subtitle blocks
        blocks = re.split(r"\n\s*\n", content.strip())

        # Extract text from each block
        subtitle_texts = []
        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) >= 3:
                # Skip sequence number (line 0) and timestamp (line 1)
                # Get text from line 2 onwards
                text_lines = lines[2:]
                text = " ".join(text_lines).strip()
                if text:
                    subtitle_texts.append(text)

        # Create markdown content
        markdown_content = f"""# {video_title}

## Nội dung phụ đề

{' '.join(subtitle_texts)}

---
*Được tạo từ phụ đề video bằng BBooks Subtitle Downloader*
*Ngày tạo: {datetime.now().strftime('%d/%m/%Y %H:%M')}*
"""

        # Write to markdown file
        with open(markdown_file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        log_message(f"   📄 Created markdown: {os.path.basename(markdown_file_path)}")
        return True

    except Exception as e:
        log_message(f"   ❌ Failed to convert SRT to markdown: {e}", "ERROR")
        return False


def process_subtitle_to_markdown(video_id, title):
    """Tìm subtitle file và chuyển đổi thành markdown"""
    # Tìm file SRT cho video này
    srt_patterns = [f"*[id={video_id}]*.srt", f"*{video_id}*.srt"]

    srt_files = []
    for pattern in srt_patterns:
        found = list(BASE_DIR.glob(pattern))
        srt_files.extend(found)

    # Remove duplicates
    srt_files = list(set(srt_files))

    if not srt_files:
        log_message(f"   ⚠️ No SRT files found for: {video_id}")
        return False

    # Process each SRT file found
    converted_count = 0
    for srt_file in srt_files:
        # Generate markdown filename
        srt_name = srt_file.stem  # filename without extension
        markdown_name = f"{srt_name}.md"
        markdown_path = BASE_DIR / markdown_name

        # Check if markdown already exists
        if markdown_path.exists():
            log_message(f"   📄 Markdown exists: {markdown_name}")
            continue

        # Convert SRT to Markdown
        if srt_to_markdown(srt_file, markdown_path, title):
            converted_count += 1

    return converted_count > 0


def extract_video_id(url):
    """Extract YouTube video ID"""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
        r"(?:watch\?v=)([0-9A-Za-z_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def check_existing_subtitles(video_id, title):
    """Kiểm tra xem đã có subtitle chưa"""
    existing_subs = []

    # Tìm các pattern subtitle có thể có
    patterns = [
        f"*[id={video_id}]*.srt",  # Standard format
        f"*{video_id}*.srt",  # ID anywhere in filename
    ]

    for pattern in patterns:
        found = list(BASE_DIR.glob(pattern))
        existing_subs.extend(found)

    # Remove duplicates
    existing_subs = list(set(existing_subs))

    if existing_subs:
        log_message(
            f"   📝 Found {len(existing_subs)} existing subtitles for {video_id}"
        )
        for sub in existing_subs:
            log_message(f"      - {sub.name}")

    return existing_subs


def download_subtitle_only(video_info, retry_count=0):
    """Download chỉ subtitle cho 1 video"""
    title = video_info["title"]
    url = video_info["url"]
    video_id = video_info["video_id"]

    log_message(f"📥 Downloading subtitles: {title[:50]}... (ID: {video_id})")

    # Kiểm tra existing subtitles trước
    existing_subs = check_existing_subtitles(video_id, title)

    if existing_subs and not OVERWRITE_EXISTING:
        log_message(f"   ⏭️ Skip - đã có {len(existing_subs)} subtitles")
        return True

    # yt-dlp command - CHỈ DOWNLOAD SUBTITLES
    cmd = [
        str(YTDLP_EXE),
        "--write-subs",  # Download available subtitles
        "--write-auto-subs",  # Download auto-generated subtitles
        "--sub-langs",
        SUBTITLE_LANGS,
        "--sub-format",
        SUBTITLE_FORMAT,
        "--convert-subs",
        SUBTITLE_FORMAT,
        "--skip-download",  # QUAN TRỌNG: Không download video
        "--output",
        str(BASE_DIR / SUB_FILE_FORMAT),
        "--no-overwrites" if not OVERWRITE_EXISTING else "--force-overwrites",
        "--ignore-errors",
        url,
    ]

    if VERBOSE:
        cmd.append("--verbose")

    try:
        if DRY_RUN:
            log_message(f"   🔄 DRY RUN - Would download subtitles: {video_id}")
            return True
        else:
            log_message(f"   🔄 Executing subtitle download: {video_id}")
            result = subprocess.run(
                cmd, capture_output=True, text=True, encoding="utf-8", timeout=180
            )

            if result.returncode == 0:
                # Kiểm tra xem có subtitle nào được download không
                new_subs = check_existing_subtitles(video_id, title)
                if len(new_subs) > len(existing_subs):
                    log_message(f"   ✅ Subtitle download success: {video_id}")
                    return True
                else:
                    log_message(f"   ⚠️ No new subtitles downloaded: {video_id}")
                    return True  # Không coi là lỗi
            else:
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                log_message(
                    f"   ❌ Subtitle download failed: {video_id} - {error_msg}", "ERROR"
                )

                # Retry logic
                if retry_count < MAX_RETRIES:
                    log_message(
                        f"   🔄 Retrying {retry_count + 1}/{MAX_RETRIES}...", "WARNING"
                    )
                    return download_subtitle_only(video_info, retry_count + 1)
                else:
                    log_message(f"   ❌ Max retries reached: {video_id}", "ERROR")
                    return False

    except subprocess.TimeoutExpired:
        log_message(f"   ⏱️ Timeout downloading subtitles: {video_id}", "ERROR")
        return False
    except Exception as e:
        log_message(f"   💥 Exception: {video_id}: {e}", "ERROR")
        return False


# =====================================================
# CSV MANAGEMENT
# =====================================================


def load_csv_data():
    """Load CSV data"""
    log_message("📄 Loading video list from CSV...")

    if not CSV_FILE.exists():
        log_message(f"❌ CSV file not found: {CSV_FILE.name}", "ERROR")
        return None

    try:
        with open(CSV_FILE, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            videos = []

            for row in reader:
                if "Tên Video" in row and "Link" in row:
                    title = row["Tên Video"]
                    url = row["Link"]
                    video_id = extract_video_id(url)

                    if video_id:
                        videos.append(
                            {"title": title, "url": url, "video_id": video_id}
                        )

            log_message(f"✅ Loaded {len(videos)} videos from CSV")
            return videos

    except Exception as e:
        log_message(f"❌ Error reading CSV: {e}", "ERROR")
        return None


# =====================================================
# MAIN FUNCTIONS
# =====================================================


def scan_subtitle_status():
    """Scan tình trạng subtitle hiện tại"""
    log_message("🔍 Scanning current subtitle status...")

    # Get all subtitle files
    subtitle_files = list(BASE_DIR.glob("*.srt"))
    log_message(f"📝 Found {len(subtitle_files)} .srt files")

    # Analyze subtitle files
    vietnamese_subs = []
    english_subs = []
    auto_subs = []
    other_subs = []

    for sub_file in subtitle_files:
        filename_lower = sub_file.name.lower()

        if ".vi." in filename_lower or "vietnamese" in filename_lower:
            vietnamese_subs.append(sub_file)
        elif ".en." in filename_lower or "english" in filename_lower:
            english_subs.append(sub_file)
        elif "auto" in filename_lower or "generated" in filename_lower:
            auto_subs.append(sub_file)
        else:
            other_subs.append(sub_file)

    # Report
    log_message("📊 SUBTITLE STATUS:")
    log_message(f"   📝 Total .srt files: {len(subtitle_files)}")
    log_message(f"   🇻🇳 Vietnamese: {len(vietnamese_subs)}")
    log_message(f"   🇬🇧 English: {len(english_subs)}")
    log_message(f"   🤖 Auto-generated: {len(auto_subs)}")
    log_message(f"   ❓ Other: {len(other_subs)}")

    return {
        "total_subs": len(subtitle_files),
        "vietnamese_subs": vietnamese_subs,
        "english_subs": english_subs,
        "auto_subs": auto_subs,
        "other_subs": other_subs,
    }


def download_all_subtitles():
    """Download subtitles cho tất cả videos trong CSV"""
    log_message("🚀 Starting subtitle download process...")

    # Check prerequisites
    if not YTDLP_EXE.exists():
        log_message(f"❌ yt-dlp.exe not found: {YTDLP_EXE}", "ERROR")
        return False

    # Load video data
    videos = load_csv_data()
    if not videos:
        return False

    # Scan current status
    current_status = scan_subtitle_status()

    log_message(f"\n🎯 Will process {len(videos)} videos for subtitles")

    if DRY_RUN:
        log_message("🧪 DRY RUN MODE - No actual downloads")

    if not OVERWRITE_EXISTING:
        log_message("⏭️ SKIP MODE - Will skip existing subtitles")

    # Process each video
    success_count = 0
    skip_count = 0
    error_count = 0
    start_time = datetime.now()

    for i, video_info in enumerate(videos, 1):
        log_message(f"\n[{i}/{len(videos)}] Processing: {video_info['video_id']}")

        # Check if already has subtitles
        existing = check_existing_subtitles(video_info["video_id"], video_info["title"])
        if existing and not OVERWRITE_EXISTING:
            log_message(f"   ⏭️ Skipping - already has {len(existing)} subtitles")
            skip_count += 1
            continue

        # Download subtitles
        if download_subtitle_only(video_info):
            success_count += 1
        else:
            error_count += 1

        # Progress report every 10 videos
        if i % 10 == 0:
            elapsed = (datetime.now() - start_time).total_seconds() / 60
            log_message(
                f"📊 Progress: {i}/{len(videos)} | Success: {success_count} | Skip: {skip_count} | Error: {error_count} | Time: {elapsed:.1f}min"
            )

    # Final report
    elapsed_total = (datetime.now() - start_time).total_seconds() / 60
    processed = success_count + error_count
    success_rate = (success_count / processed * 100) if processed > 0 else 0

    log_message("\n" + "=" * 60)
    log_message("📊 SUBTITLE DOWNLOAD SUMMARY:")
    log_message(f"   ✅ Successfully downloaded: {success_count}")
    log_message(f"   ⏭️ Skipped (already have): {skip_count}")
    log_message(f"   ❌ Failed: {error_count}")
    log_message(f"   📈 Success rate: {success_rate:.1f}%")
    log_message(f"   ⏱️ Total time: {elapsed_total:.1f} minutes")

    # Re-scan to show final status
    log_message(f"\n🔄 Final subtitle status:")
    scan_subtitle_status()

    return success_count > 0


def download_all_subtitles_missing_only():
    """Download subtitles chỉ cho videos chưa có subtitles"""
    global OVERWRITE_EXISTING
    original_overwrite = OVERWRITE_EXISTING

    # Temporarily set to not overwrite
    OVERWRITE_EXISTING = False

    try:
        result = download_all_subtitles()
    finally:
        # Restore original setting
        OVERWRITE_EXISTING = original_overwrite

    return result


def convert_all_srt_to_markdown():
    """Chuyển đổi tất cả file SRT thành markdown"""
    log_message("📄 Converting all SRT files to markdown...")

    videos = load_csv_data()
    if not videos:
        return False

    converted_count = 0
    total_count = 0

    for i, video in enumerate(videos, 1):
        video_id = video["video_id"]
        title = video["title"]

        log_message(
            f"📄 Processing {i}/{len(videos)}: {title[:50]}... (ID: {video_id})"
        )

        if process_subtitle_to_markdown(video_id, title):
            converted_count += 1
        total_count += 1

        # Progress update every 10 videos
        if i % 10 == 0:
            log_message(
                f"📊 Progress: {i}/{len(videos)} | Converted: {converted_count}"
            )

    log_message("\n" + "=" * 60)
    log_message("📄 MARKDOWN CONVERSION SUMMARY:")
    log_message(f"   ✅ Successfully converted: {converted_count}")
    log_message(f"   📂 Total processed: {total_count}")
    log_message(
        f"   📈 Conversion rate: {(converted_count/total_count*100) if total_count > 0 else 0:.1f}%"
    )

    return converted_count > 0


def download_single_video_subtitle_and_convert(video_url):
    """Download subtitle cho 1 video URL cụ thể và chuyển đổi thành markdown"""
    log_message(f"🎯 Processing single video: {video_url}")

    # Extract video ID
    video_id = extract_video_id(video_url)
    if not video_id:
        log_message("❌ Invalid YouTube URL")
        return False

    log_message(f"🆔 Video ID: {video_id}")

    # Get video title using yt-dlp
    try:
        cmd_info = [str(YTDLP_EXE), "--get-title", "--no-warnings", video_url]

        result = subprocess.run(
            cmd_info, capture_output=True, text=True, encoding="utf-8", timeout=60
        )
        if result.returncode == 0:
            title = result.stdout.strip()
            log_message(f"📺 Title: {title}")
        else:
            title = f"Video_{video_id}"
            log_message(f"⚠️ Could not get title, using: {title}")

    except Exception as e:
        title = f"Video_{video_id}"
        log_message(f"⚠️ Error getting title: {e}, using: {title}")

    # Create video info object
    video_info = {"title": title, "url": video_url, "video_id": video_id}

    # Step 1: Download subtitle
    log_message("📥 Step 1: Downloading subtitles...")
    if not download_subtitle_only(video_info):
        log_message("❌ Failed to download subtitle")
        return False

    # Step 2: Convert to markdown
    log_message("📄 Step 2: Converting to markdown...")
    if not process_subtitle_to_markdown(video_id, title):
        log_message("❌ Failed to convert to markdown")
        return False

    log_message("✅ Single video processing completed successfully!")
    return True


def download_and_convert_pipeline(video_url=None):
    """Pipeline: Download subtitle + Convert to markdown cho 1 video"""
    if not video_url:
        video_url = input("🔗 Enter YouTube URL: ").strip()
        if not video_url:
            log_message("❌ No URL provided")
            return False

    # Extract video ID
    video_id = extract_video_id(video_url)
    if not video_id:
        log_message("❌ Invalid YouTube URL")
        return False

    # Find video info from CSV
    videos = load_csv_data()
    video_info = None

    for video in videos:
        if video["video_id"] == video_id:
            video_info = video
            break

    if not video_info:
        log_message(f"❌ Video ID {video_id} not found in CSV")
        return False

    title = video_info["title"]
    log_message(f"🎯 Processing: {title}")
    log_message(f"🔗 URL: {video_url}")
    log_message(f"🆔 ID: {video_id}")

    # Step 1: Download subtitle
    log_message("\n📥 Step 1: Downloading subtitles...")
    if not download_subtitle_only(video_info):
        log_message("❌ Failed to download subtitle")
        return False

    # Step 2: Convert to markdown
    log_message("\n📄 Step 2: Converting to markdown...")
    if not process_subtitle_to_markdown(video_id, title):
        log_message("❌ Failed to convert to markdown")
        return False

    log_message("✅ Pipeline completed successfully!")
    return True


def main():
    """Main function"""
    clear_log()
    log_message("🎯 BBOOKS SUBTITLE DOWNLOADER STARTED")
    log_message("=" * 50)

    print("🏷️ BBOOKS SUBTITLE DOWNLOADER")
    print("=" * 50)
    print("📝 Chuyên download subtitle .srt cho BBooks videos")
    print(f"🎯 Target: Vietnamese (.vi.srt) subtitles")
    print(f"📂 CSV source: {CSV_FILE.name}")
    print(f"🛠️ yt-dlp: {YTDLP_EXE}")
    print("=" * 50)

    # Show current settings
    print("⚙️ SETTINGS:")
    print(f"   Languages: {SUBTITLE_LANGS}")
    print(f"   Format: {SUBTITLE_FORMAT}")
    print(f"   Dry run: {'Yes' if DRY_RUN else 'No'}")
    print(f"   Overwrite existing: {'Yes' if OVERWRITE_EXISTING else 'No'}")
    print("=" * 50)

    # Menu
    print("\n📋 OPTIONS:")
    print("1. 📊 Scan current subtitle status")
    print("2. 📥 Download subtitles for all videos")
    print("3. 🔍 Download subtitles for missing only")
    print("4. 📄 Convert all SRT files to Markdown")
    print("5. 🔄 Download subtitle + Convert to Markdown (single video)")
    print("6. 🎯 Download and convert specific YouTube URL")
    print("0. ❌ Exit")

    while True:
        try:
            choice = input("\nSelect option (0-6): ").strip()

            if choice == "0":
                log_message("👋 Exiting subtitle downloader")
                break

            elif choice == "1":
                scan_subtitle_status()

            elif choice == "2":
                confirm = (
                    input("⚠️ Download subtitles for ALL videos? (y/N): ")
                    .strip()
                    .lower()
                )
                if confirm == "y":
                    download_all_subtitles()
                else:
                    log_message("❌ Download cancelled")

            elif choice == "3":
                # Download for missing subtitles only (skip existing)
                log_message("🔍 Download for missing subtitles only...")
                download_all_subtitles_missing_only()

            elif choice == "4":
                # Convert all SRT files to markdown
                log_message("📄 Converting all SRT files to markdown...")
                convert_all_srt_to_markdown()

            elif choice == "5":
                # Download + Convert pipeline for single video
                download_and_convert_pipeline()

            elif choice == "6":
                # Download and convert specific YouTube URL
                target_url = "https://www.youtube.com/watch?v=i2yYw9s1SlM"
                log_message(f"🎯 Processing target URL: {target_url}")
                download_single_video_subtitle_and_convert(target_url)

            else:
                print("❌ Invalid option")

            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            log_message("⏹️ Interrupted by user")
            break
        except Exception as e:
            log_message(f"💥 Unexpected error: {e}", "ERROR")


if __name__ == "__main__":
    main()
