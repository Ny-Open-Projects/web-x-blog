import errno
import socket
import time


def diagnose_resolution(host: str, port: int = 443) -> str:
    try:
        infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        ips = [i[4][0] for i in infos]
        return f"OK {host} → {ips[:3]}"
    except socket.gaierror as e:
        code = e.errno
        if code in (socket.EAI_NONAME, -2):  # 平台差异: mac/linux errno 值不同
            return (f"NXDOMAIN {host}: 名称不存在 → 检查拼写/记录是否被删/"
                    f"是否本地 hosts 覆盖")
        if code in (socket.EAI_AGAIN,):
            return f"TEMPFAIL {host}: DNS 服务器超时 → 查 resolv.conf 上游与网络"
        if code in (socket.EAI_FAMILY,):
            return f"FAMILY {host}: 地址族不受支持 → 代码参数问题"
        return f"OTHER {host}: errno={code} ({e})"
    except OSError as e:
        return f"SYSERR {host}: {e!r}"


if __name__ == "__main__":
    cases = [
        ("localhost", "正常解析"),
        ("this-domain-does-not-exist.invalid", "NXDOMAIN 样本"),
        ("127.0.0.1", "IP 字面量快速路径"),
    ]
    for host, label in cases:
        print(f"[{label}]")
        print(" ", diagnose_resolution(host))

    # 参数类错误演示: 请求不存在的服务名
    try:
        socket.getaddrinfo("localhost", "not-a-service", type=socket.SOCK_STREAM)
    except socket.gaierror as e:
        print(f"[服务名错误] errno={e.errno} → {e}")

    # 解析耗时对比: 排障时先看耗时再下结论
    for host in ("localhost", "127.0.0.1"):
        t0 = time.monotonic()
        socket.getaddrinfo(host, 80)
        dt = (time.monotonic() - t0) * 1000
        print(f"解析 {host}: {dt:.2f}ms")
    print("若 localhost 也要几十毫秒, 说明 nsswitch/hosts 配置异常")
