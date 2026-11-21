import time
from concurrent.futures import ThreadPoolExecutor, as_completed

visited: set[str] = set()
lock = __import__("threading").Lock()


def crawl(url: str) -> str:
    with lock:  # 去重集合加锁
        if url in visited:
            return f"{url} 已爬过"
        visited.add(url)
    time.sleep(0.2)  # 模拟网络请求
    if "bad" in url:
        raise ConnectionError(f"{url} 无法连接")
    return f"{url} 抓取成功, 长度 1024"


def run(urls: list[str]) -> None:
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(crawl, u): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                print(fut.result())
            except ConnectionError as e:
                print("失败:", e)
    print("共爬取:", len(visited))


if __name__ == "__main__":
    start = time.perf_counter()
    run([f"https://example.com/page{i}" for i in range(10)]
        + ["https://example.com/bad1", "https://example.com/bad2"])
    print(f"总耗时 {time.perf_counter() - start:.2f}s")
