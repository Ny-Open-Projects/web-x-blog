import socket
import threading
import time


def udp_echo(stop: threading.Event, port_box: list) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 0))
    port_box.append(s.getsockname()[1])
    s.settimeout(0.2)
    while not stop.is_set():
        try:
            data, addr = s.recvfrom(65535)
            s.sendto(data, addr)  # 原样回显
        except socket.timeout:
            continue
        except OSError:
            continue
    s.close()


def probe_mtu(host: str, port: int, lo: int = 1200, hi: int = 65000) -> int:
    """二分探测 UDP 回环可达的最大数据报 (含应用载荷)。"""
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        try:
            s.sendto(b"x" * mid, (host, port))
            s.recvfrom(mid + 64)
            best = mid
            lo = mid + 1
        except socket.timeout:
            hi = mid - 1  # 超过上限: 丢弃或 EMSGSIZE 后的超限
        except OSError as e:
            if e.errno == 90:  # EMSGSIZE: 超过本地 socket 上限
                hi = mid - 1
            else:
                hi = mid - 1
        finally:
            s.close()
    return best


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=udp_echo, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    max_payload = probe_mtu("127.0.0.1", port)
    print(f"回环 UDP 单报文最大载荷: {max_payload} 字节")
    print(f"  (上限 65507 = 65535 - IP头20 - UDP头8, 实际受 SO_SNDBUF 影响可能更小)")

    print("\nTCP 场景的对应概念: MSS = MTU - 40 (IP+TCP头)")
    print("  MTU 1500 → MSS 1460; VPN 封装 MTU 1400 → MSS 1360")
    print("  MSS 协商不当时: 握手成功但大包反复重传 = PMTUD 黑洞")

    # 演示本地 EMSGSIZE 边界
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.sendto(b"x" * 70000, ("127.0.0.1", port))
    except OSError as e:
        print(f"\n超限报文: {e} (errno={e.errno})")
    s.close()
    stop.set()
