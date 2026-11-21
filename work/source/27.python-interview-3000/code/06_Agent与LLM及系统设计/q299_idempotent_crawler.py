import hashlib
from dataclasses import dataclass


def normalize_url(url: str) -> str:
    """URL 归一化:去尾部斜杠与 tracking 参数,保证业务键稳定。"""
    base = url.split("?")[0].rstrip("/")
    return base


def content_key(url: str) -> str:
    return hashlib.sha256(normalize_url(url).encode()).hexdigest()[:16]


@dataclass
class Page:
    url: str
    etag: str
    body: str


class Crawler:
    def __init__(self):
        self.seen: dict[str, str] = {}   # key -> etag
        self.store: dict[str, str] = {}

    def visit(self, page: Page) -> str:
        key = content_key(page.url)
        if self.seen.get(key) == page.etag:
            return "skipped"           # 内容未变,幂等跳过
        self.store[key] = page.body
        self.seen[key] = page.etag
        return "updated"


if __name__ == "__main__":
    c = Crawler()
    p = Page("https://example.com/post/1/", "v1", "hello")
    print(c.visit(p))                                # updated
    print(c.visit(Page("https://example.com/post/1", "v1", "hello")))  # skipped
    print(c.visit(Page("https://example.com/post/1/", "v2", "hello2")))  # updated
