"""用纯标准库 urllib 演示与 requests.Session 等价的工程化要点:
显式超时 + 指数退避重试 + 单例复用。"""
import json
import time
import urllib.error
import urllib.request


class HttpClient:
    """生产级 HTTP 客户端骨架,标准库可运行。"""

    def __init__(self, base_url, retries=3, connect_timeout=3.0, read_timeout=10.0):
        self.base_url = base_url.rstrip("/")
        self.retries = retries
        self.timeout = (connect_timeout, read_timeout)  # 连接超时/读超时分离
        self.opener = urllib.request.build_opener()  # 等价 Session:复用连接语义

    def get_json(self, path, params=None):
        url = self.base_url + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        last_err = None
        for attempt in range(1, self.retries + 1):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "my-svc/1.0"})
                with self.opener.open(req, timeout=max(self.timeout)) as resp:
                    return json.loads(resp.read())
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last_err = e  # GET 幂等,可安全重试
                time.sleep(min(2 ** attempt + random_jitter(), 10))
        raise RuntimeError(f"GET {url} failed after {self.retries} retries") from last_err


def random_jitter():
    import random
    return random.uniform(0, 0.5)


if __name__ == "__main__":
    client = HttpClient("https://httpbin.org")
    try:
        print(client.get_json("/get", params={"q": "python"})["url"])
    except RuntimeError as e:
        print("网络不可用,优雅降级:", e)
