#!/usr/bin/env python3
"""
对失败的文章重新抓取。
策略：每个 URL 间隔 5 秒；每次失败再 sleep 10 秒重试；最多 3 轮；
使用完整的浏览器头（含 Accept, Accept-Language, Referer）。
"""
import subprocess
import time
import sys
from pathlib import Path

META_DIR = Path("/Users/Wang/Code/webfault-ai/dsa/_meta")
ART_DIR = META_DIR / "articles"
FAILED = META_DIR / "failed.txt"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
HEADERS = [
    "-H", f"User-Agent: {UA}",
    "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "-H", "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8",
    "-H", "Accept-Encoding: identity",
    "-H", "Connection: keep-alive",
    "-H", "Upgrade-Insecure-Requests: 1",
]

ANTI_BOT_MARKERS = ("Security Verification", "安全验证")


def is_valid(html: str) -> bool:
    if len(html) < 5000:
        return False
    for m in ANTI_BOT_MARKERS:
        if m in html:
            return False
    if 'class="title-article"' not in html:
        return False
    return True


def fetch(url: str) -> str:
    result = subprocess.run(
        ["curl", "-s", "-L", *HEADERS, url, "--max-time", "60"],
        capture_output=True, text=True, timeout=70,
    )
    return result.stdout


def main():
    if not FAILED.exists():
        print("No failed.txt")
        return

    items = []
    for line in FAILED.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            items.append(parts)

    print(f"Refetching {len(items)} failed articles...")

    still_failed = []
    for i, (aid, fetch_url) in enumerate(items, 1):
        out = ART_DIR / f"{aid}.html"
        success = False
        for attempt in range(3):
            html = fetch(fetch_url)
            if is_valid(html):
                out.write_text(html, encoding="utf-8")
                success = True
                print(f"[{i}/{len(items)}] OK {aid}")
                break
            else:
                time.sleep(8 + attempt * 4)
        if not success:
            still_failed.append((aid, fetch_url))
            print(f"[{i}/{len(items)}] FAIL {aid}")
        time.sleep(2)

    if still_failed:
        with (META_DIR / "failed.txt").open("w", encoding="utf-8") as f:
            for aid, url in still_failed:
                f.write(f"{aid}\t{url}\n")
        print(f"\nStill failed: {len(still_failed)}")
    else:
        FAILED.unlink()
        print("\nAll recovered!")


if __name__ == "__main__":
    main()