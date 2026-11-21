import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_one(url: str) -> str:
    time.sleep(random.uniform(0.05, 0.2))  # 模拟网络 IO
    if random.random() < 0.2:
        raise ConnectionError(url)
    return f"saved {url}"


def download_all(urls: list, max_workers: int = 4) -> dict:
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(download_one, u): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                results[url] = fut.result()
            except ConnectionError:
                results[url] = "failed"  # 收集后可统一重试
    return results


if __name__ == "__main__":
    random.seed(42)
    res = download_all([f"https://cdn.example.com/f{i}" for i in range(10)])
    print(len([v for v in res.values() if v != "failed"]), "ok")
