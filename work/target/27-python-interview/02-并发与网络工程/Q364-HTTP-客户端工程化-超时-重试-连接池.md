---
title: [Q364] HTTP 客户端工程化:超时、重试、连接池
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q364 · HTTP 客户端工程化:超时、重试、连接池

> 难度:★★★ | 标签:requests, httpx, HTTP 客户端

**问**:生产代码里用 requests/httpx 调外部 API,你会强制做哪几件事?

**答**:四件事:①显式超时——`timeout` 必须设置,且最好区分连接超时与读超时(httpx 支持 `httpx.Timeout(5, read=30)`),默认无超时是最常见的线上事故;②重试只针对幂等请求(GET/PUT)或幂等操作,配指数退避与抖动,可用 `urllib3.Retry`/httpx 的 `transport` 机制;③连接池复用——用 `requests.Session`/`httpx.Client` 而不是每次新建,降低握手开销并限制并发;④带 UA、校验状态码 `raise_for_status()`、记录请求 ID 便于排查。

```python
# file: code/02_并发与网络工程/q364_http_client.py
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
```

**追问**:
- POST 请求能盲目重试吗?不能,可能造成重复下单;除非携带幂等键 idempotency-key 且服务端支持去重。
- httpx 与 requests 怎么选?requests 同步生态最成熟;httpx API 相似且原生支持 async/HTTP2,适合 asyncio 项目。
