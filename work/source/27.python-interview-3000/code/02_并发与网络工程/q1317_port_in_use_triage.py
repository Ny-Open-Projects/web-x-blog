import errno
import os
import socket
import subprocess


def probe_bind(port: int) -> str:
    s = socket.socket()
    try:
        s.bind(("127.0.0.1", port))
        return "FREE 端口可用"
    except OSError as exc:
        if exc.errno == errno.EADDRINUSE:
            return "EADDRINUSE 已被占用"
        if exc.errno == errno.EADDRNOTAVAIL:
            return "EADDRNOTAVAIL 本机没有该地址, 检查网卡与配置"
        return f"其他错误 {errno.errorcode.get(exc.errno, exc.errno)}"
    finally:
        s.close()


def find_listener(port: int):
    """lsof 找监听进程, 返回 (pid, 进程名), 失败返回 None。"""
    try:
        out = subprocess.run(
            ["lsof", "-nP", "-iTCP:%d" % port, "-sTCP:LISTEN"],
            capture_output=True, text=True, timeout=5).stdout
        for line in out.splitlines()[1:]:     # 跳过表头
            parts = line.split()
            if len(parts) >= 2:
                return int(parts[1]), parts[0]
    except (OSError, ValueError):
        return None
    return None


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.listen(1)

    print(f"步骤一 bind 探测: {probe_bind(port)}")

    found = find_listener(port)
    if found:
        pid, name = found
        who = "就是我自己(旧实例嫌疑)" if pid == os.getpid() else name
        print(f"步骤二 lsof 定位: PID={pid} 进程={name} -> {who}")
        assert pid == os.getpid()
    else:
        print("步骤二 lsof 定位: 本机无 lsof 或无结果, 跳过(替代: ss -ltnp / netstat)")

    srv.close()
    print(f"关闭后 bind 探测: {probe_bind(port)}")
    print("SO_REUSEADDR 只救 TIME_WAIT 残留, 不等于允许双进程同端口(SO_REUSEPORT 才是)")


if __name__ == "__main__":
    main()
