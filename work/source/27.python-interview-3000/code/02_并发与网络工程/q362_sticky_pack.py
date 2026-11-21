"""长度前缀协议:4 字节大端长度 + body,解决 TCP 粘包。"""
import socket
import struct
import threading

HEADER = struct.Struct("!I")  # 网络字节序(大端)uint32


def send_msg(sock, payload: bytes):
    sock.sendall(HEADER.pack(len(payload)) + payload)


def recv_exact(sock, n: int) -> bytes:
    """循环读满 n 字节,连接关闭则抛异常。"""
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("peer closed")
        buf.extend(chunk)
    return bytes(buf)


def recv_msg(sock) -> bytes:
    (length,) = HEADER.unpack(recv_exact(sock, 4))
    if length > 10 * 1024 * 1024:  # 防恶意超大包
        raise ValueError("payload too large")
    return recv_exact(sock, length)


def main():
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    threading.Thread(target=_serve, args=(srv,), daemon=True).start()

    cli = socket.create_connection(("127.0.0.1", port))
    # 连发三条模拟粘包,服务端按帧逐条还原
    for i in range(3):
        send_msg(cli, f"msg-{i}".encode())
    cli.close()
    srv.close()


def _serve(srv):
    conn, _ = srv.accept()
    with conn:
        for _ in range(3):
            print("recv frame:", recv_msg(conn))


if __name__ == "__main__":
    main()
