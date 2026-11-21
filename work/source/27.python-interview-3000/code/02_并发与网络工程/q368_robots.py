"""robots.txt 合规检查,离线演示 robotparser 用法。"""
import urllib.robotparser


def make_parser(robots_text: str) -> urllib.robotparser.RobotFileParser:
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots_text.splitlines())  # 也可 rp.set_url + rp.read 在线拉取
    return rp


ROBOTS = """
User-agent: *
Disallow: /private/
Crawl-delay: 2

User-agent: edu-crawler
Allow: /
Disallow: /admin
"""

if __name__ == "__main__":
    rp = make_parser(ROBOTS)
    ua = "edu-crawler"
    print("can /posts :", rp.can_fetch(ua, "https://x.com/posts"))
    print("can /admin :", rp.can_fetch(ua, "https://x.com/admin"))
    print("can /private (其他UA):", rp.can_fetch("Baiduspider", "https://x.com/private/a"))
    print("crawl_delay:", rp.crawl_delay(ua))
