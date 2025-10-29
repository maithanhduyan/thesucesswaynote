#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download subtitle cho video YouTube cụ thể và chuyển đổi thành markdown
URL target: https://www.youtube.com/watch?v=i2yYw9s1SlM
"""

import sys
import os
from pathlib import Path

# Add parent directory to path to import subtitle_downloader
sys.path.append(str(Path(__file__).parent))

from subtitle_downloader import (
    download_single_video_subtitle_and_convert,
    log_message,
    clear_log,
    YTDLP_EXE,
    BASE_DIR,
)


def main():
    """Main function để download video cụ thể"""
    clear_log()

    # Target URL
    target_url = "https://www.youtube.com/watch?v=i2yYw9s1SlM"

    log_message("🎯 DOWNLOAD SPECIFIC VIDEO SUBTITLE")
    log_message("=" * 50)
    log_message(f"🔗 Target URL: {target_url}")
    log_message(f"🛠️ yt-dlp path: {YTDLP_EXE}")
    log_message(f"📂 Base directory: {BASE_DIR}")

    # Check if yt-dlp exists
    if not YTDLP_EXE.exists():
        log_message(f"❌ yt-dlp.exe not found at: {YTDLP_EXE}", "ERROR")
        log_message("💡 Please ensure yt-dlp.exe is in the .tools directory", "INFO")
        return False

    log_message("✅ yt-dlp.exe found, proceeding with download...")

    # Download and convert
    success = download_single_video_subtitle_and_convert(target_url)

    if success:
        log_message("🎉 SUCCESS: Video subtitle downloaded and converted to markdown!")

        # List generated files
        log_message("\n📁 Generated files:")
        srt_files = list(BASE_DIR.glob("*i2yYw9s1SlM*.srt"))
        md_files = list(BASE_DIR.glob("*i2yYw9s1SlM*.md"))

        for srt_file in srt_files:
            log_message(f"   📝 SRT: {srt_file.name}")

        for md_file in md_files:
            log_message(f"   📄 Markdown: {md_file.name}")

    else:
        log_message("❌ FAILED: Could not download or convert video subtitle", "ERROR")

    return success


if __name__ == "__main__":
    try:
        main()
        input("\nPress Enter to exit...")
    except KeyboardInterrupt:
        log_message("⏹️ Interrupted by user")
    except Exception as e:
        log_message(f"💥 Unexpected error: {e}", "ERROR")
