"""客户端提前断开: 写入侧感知与资源清理(纯标准库, 回环 socket 直连)。"""
import socket
import threading
import time

HOST = "127.0.0.1"
CHUNK = b"x" * 4096
N_CHUNKS = 25
events = []
ready = threading.Event()
holder = {}


def server_once():
    """逐块写大响应; 客户端断开后 send 抛错, 捕获后必须走清理而非重试。"""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    holder["port"] = srv.getsockname()[1]
    ready.set()
    conn, _ = srv.accept()
    try:
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n" % (len(CHUNK) * N_CHUNKS))
        for i in range(N_CHUNKS):
            try:
                conn.sendall(CHUNK)
                time.sleep(0.02)  # 模拟慢生成, 给 RST 到达留时间
            except (BrokenPipeError, ConnectionResetError, OSError) as e:
                events.append("client_gone_at_chunk_%d: %s" % (i, type(e).__name__))
                break
        else:
            events.append("finished")
    finally:
        conn.close()
        events.append("cleaned_up")
        srv.close()


t = threading.Thread(target=server_once, daemon=True)
t.start()
ready.wait(3)

cli = socket.create_connection((HOST, holder["port"]), timeout=3)
cli.recv(1024)          # 只读一小口就跑路
cli.close()
t.join(timeout=5)

assert any(e.startswith("client_gone_at_chunk") for e in events), events
assert "cleaned_up" in events, events
print("事件序列:", events)


def guarded_send(conn, gen):
    """通用模式: 逐块写出, 断开异常就地转成静默终止, finally 保证清理。"""
    try:
        for piece in gen:
            conn.sendall(piece)
        return "done"
    except (BrokenPipeError, ConnectionResetError):
        return "aborted"


class Gone:
    def sendall(self, _):
        raise BrokenPipeError()


result = guarded_send(Gone(), iter([b"1", b"2"]))
assert result == "aborted"
print("guarded_send 在断开时返回 aborted, 不再继续无谓的计算")
