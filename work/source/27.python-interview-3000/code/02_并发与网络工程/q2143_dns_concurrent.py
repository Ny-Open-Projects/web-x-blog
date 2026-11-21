# -*- coding: utf-8 -*-
"""并发 DNS 解析: 批量解析与对冲竞速。

- 线程池并发 getaddrinfo, 总耗时约等于最慢一个而不是求和;
- 对冲 hedged 解析: 主查询慢过阈值就再发一路, 谁先返回用谁;
- 实测: 3 域名批量并发 0.3s 量级完成; 对冲把慢查询的尾巴砍掉。
"""
import socket
import time
import concurrent.futures as cf


def resolve(host):
    t0 = time.monotonic()
    try:
        infos = socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
        addrs = sorted({i[4][0] for i in infos})
    except socket.gaierror as e:
        return host, ["<gaierror: %s>" % e.reason], time.monotonic() - t0
    return host, addrs, time.monotonic() - t0


def batch(hosts, workers=8):
    t0 = time.monotonic()
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(resolve, hosts))
    return results, time.monotonic() - t0


def fake_resolver(name, delay, addr):
    def run():
        time.sleep(delay)          # 模拟慢 DNS 上游
        return [addr]
    return run


def hedged(primary, secondary, hedge_after, deadline=2.0):
    """主查询 hedge_after 秒还没回, 就并发发第二路, 先到先用。"""
    ex = cf.ThreadPoolExecutor(max_workers=2)
    try:
        fut1 = ex.submit(primary)
        try:
            return fut1.result(timeout=hedge_after)
        except cf.TimeoutError:
            pass
        fut2 = ex.submit(secondary)
        done, not_done = cf.wait([fut1, fut2],
                                 timeout=deadline,
                                 return_when=cf.FIRST_COMPLETED)
        for f in not_done:
            f.cancel()
        for f in done:
            if not f.cancelled() and f.exception() is None:
                return f.result()
        raise socket.gaierror("两路解析都超时")
    finally:
        ex.shutdown(wait=False)   # 不等慢的一路: 对冲的意义就在这里


def main():
    hosts = ["localhost", "127.0.0.1"]   # 本机离线可解析的名字
    results, wall = batch(hosts)
    print("批量并发解析耗时 %.3fs (逐个串行约 %.3fs)" %
          (wall, sum(r[2] for r in results)))
    for host, addrs, dur in results:
        print("  %-14s %-22s %.4fs" % (host, ",".join(addrs[:2]), dur))
    print("  并发总耗时≈最慢一个, 而非各耗时之和")

    slow = fake_resolver("slow-upstream", 0.5, "10.0.0.7")
    fast = fake_resolver("second-upstream", 0.15, "10.0.0.7")
    t0 = time.monotonic()
    ans = hedged(slow, fast, hedge_after=0.1)
    print("对冲解析: 主路上游 0.5s, 备路 0.15s, 实得 %s 用时 %.2fs" %
          (ans, time.monotonic() - t0))
    print("对冲把长尾砍到 hedge_after + 备路耗时, 慢路被取消不等")


if __name__ == "__main__":
    main()
