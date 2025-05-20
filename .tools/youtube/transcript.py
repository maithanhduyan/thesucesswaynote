#!/usr/bin/env python3
import sys
import urllib.request
import xml.etree.ElementTree as ET

def main():
    if len(sys.argv) < 2:
        print("Usage: transcript.py <video_id>")
        sys.exit(1)

    video_id = sys.argv[1]
    # URL lấy phụ đề tiếng Anh
    url = f"https://www.youtube.com/api/timedtext?lang=vi&v={video_id}"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            if not data:
                print("Không tìm thấy phụ đề cho video này.")
                sys.exit(0)

            root = ET.fromstring(data)
            for text in root.findall('text'):
                start = text.attrib.get('start')
                dur = text.attrib.get('dur')
                content = text.text if text.text else ""
                print(f"{start}s (duration: {dur}s): {content}")
    except Exception as e:
        print(f"Lỗi khi lấy phụ đề: {e}")

if __name__ == "__main__":
    main()
