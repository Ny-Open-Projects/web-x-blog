import socket
import time


def show(label: str, infos: list) -> None:
    print(f"--- {label}: {len(infos)} 条结果")
    for family, stype, proto, canon, sockaddr in infos[:4]:
        ip = sockaddr[0]
        kind = "IPv4" if family == socket.AF_INET else "IPv6"
        print(f"  {kind} {ip} type={stype}")


if __name__ == "__main__":
    # 1. IP 字面量: 快速路径, 不查 DNS
    t0 = time.perf_counter()
    infos = socket.getaddrinfo("127.0.0.1", 80)
    t1 = time.perf_counter()
    show(f"IP 字面量 耗时 {(t1 - t0) * 1000:.2f}ms", infos)

    # 2. 服务名映射: http → 80
    infos = socket.getaddrinfo("127.0.0.1", "http", type=socket.SOCK_STREAM)
    print("服务名 http 解析为端口:", infos[0][4][1])

    # 3. 主机名解析: 双栈可能返回多族结果
    infos = socket.getaddrinfo("localhost", None)
    show("localhost", infos)
    for info in infos:
        print("   sockaddr:", info[4])

    # 4. 失败分类: 域名不存在 vs 参数错误
    for bad in ("no-such-host.invalid", "256.256.256.256"):
        try:
            socket.getaddrinfo(bad, 80)
        except socket.gaierror as e:
            print(f"gaierror for {bad}: errno={e.errno} {e}")

    # 5. 重复解析耗时: 观察 libc 是否缓存 (通常没有)
    t0 = time.perf_counter()
    for _ in range(20):
        socket.getaddrinfo("localhost", 80)
    t1 = time.perf_counter()
    print(f"重复解析 20 次总耗时 {(t1 - t0) * 1000:.1f}ms → 平均 {(t1 - t0) * 20:.3f}ms 级别")
