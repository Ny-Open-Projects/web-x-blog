"""最小 UDP 服务端与客户端。"""
import socket
import threading


def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    threading.Thread(target=_serve, args=(srv,), daemon=True).start()

    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cli.settimeout(2)
    cli.sendto(b"ping", ("127.0.0.1", port))  # 无连接,直接发
    data, addr = cli.recvfrom(1024)  # 返回数据和来源地址
    print("udp reply:", data, "from", addr)


def _serve(srv):
    while True:
        data, addr = srv.recvfrom(1024)
        srv.sendto(b"pong:" + data, addr)  # 回给来源地址


if __name__ == "__main__":
    main()
