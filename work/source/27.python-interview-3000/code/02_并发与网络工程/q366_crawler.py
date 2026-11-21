"""并发爬虫调度器:线程池 + 失败隔离 + 去重 + 汇总。"""
import concurrent.futures as cf
import urllib.error
import urllib.request

HEADERS = {"User-Agent": "edu-crawler/1.0 (+contact@example.com)"}


def fetch(url, timeout=5):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(64 * 1024)  # 只取前 64KB,防超大页面


def run(urls, max_workers=4):
    seen, ok, failed = set(), [], []
    todo = [u for u in urls if not (u in seen or seen.add(u))]  # 去重
    with cf.ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fetch, u): u for u in todo}
        for fut in cf.as_completed(futures):
            url = futures[fut]
            try:
                ok.append((url, len(fut.result())))
            except Exception as e:  # 单个失败不拖垮整体
                failed.append((url, repr(e)))
    return ok, failed


if __name__ == "__main__":
    urls = ["https://httpbin.org/get", "https://no-such-host.invalid/",
            "https://httpbin.org/get?x=1"]  # 第三条与第一条同 host 但不同 URL
    ok, failed = run(urls)
    print("成功:", ok)
    print("失败:", failed)
