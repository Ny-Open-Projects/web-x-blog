"""最小 TCP echo 服务端 + 客户端,单进程可自测。"""
import socket
import threading


def start_server(host="127.0.0.1", port=0):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 快速重启
    srv.bind((host, port))
    srv.listen(5)  # backlog:等待 accept 的连接队列长度
    srv.settimeout(2)
    return srv


def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)  # 返回 bytes,空表示对端关闭
            if not data:
                break
            conn.sendall(data)  # 循环发送直到全部写完


def main():
    srv = start_server()
    port = srv.getsockname()[1]
    threading.Thread(target=accept_loop, args=(srv,), daemon=True).start()

    # 客户端
    cli = socket.create_connection(("127.0.0.1", port), timeout=2)
    cli.sendall(b"hello")
    print("echo:", cli.recv(1024))
    cli.close()
    srv.close()


def accept_loop(srv):
    while True:
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    main()
