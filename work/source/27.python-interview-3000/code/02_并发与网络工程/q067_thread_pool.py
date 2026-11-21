import time
from concurrent.futures import ThreadPoolExecutor


def fetch(url: str) -> str:
    time.sleep(0.2)  # 模拟网络请求
    return f"内容 of {url}"


if __name__ == "__main__":
    urls = [f"https://example.com/page{i}" for i in range(5)]

    with ThreadPoolExecutor(max_workers=3) as pool:
        # map: 按顺序返回
        for result in pool.map(fetch, urls):
            print("map:", result)

        # submit: 返回 Future, 可乱序处理
        futures = [pool.submit(fetch, u) for u in urls]
        for fut in futures:
            print("submit:", fut.result(timeout=5))
