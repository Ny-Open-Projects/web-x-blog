import socket
import threading
import time
from q668_resp_parser import RespParser
from q669_resp_client import encode_command, dispatch  # 复用编解码与语义


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        parser = RespParser()
        try:
            conn.settimeout(2)
            while True:
                data = conn.recv(65536)
                if not data:
                    break
                replies = b"".join(dispatch(cmd) for cmd in parser.feed(data))
                conn.sendall(replies)
        except OSError:
            pass
        finally:
            conn.close()
    srv.close()


def bench(port: int, n: int = 200) -> tuple:
    c = socket.create_connection(("127.0.0.1", port), timeout=3)
    c.settimeout(3)
    parser = RespParser()
    pending: list = []  # 未消费的回复队列 (feed 的返回值汇入, 消费时弹出)

    # 串行: 一发一收
    t0 = time.perf_counter()
    for i in range(n):
        c.sendall(encode_command("SET", f"k{i}", "v"))
        while not pending:
            pending.extend(parser.feed(c.recv(65536)))
        pending.pop(0)
    t_seq = time.perf_counter() - t0

    # 管线化: 全部命令一次写出, 再统一读回复
    parser2 = RespParser()
    pending2: list = []
    batch = b"".join(encode_command("SET", f"k{i}", "v") for i in range(n))
    t0 = time.perf_counter()
    c.sendall(batch)  # 1 次 RTT
    got = 0
    while got < n:
        if pending2:
            pending2.pop(0)
            got += 1
            continue
        pending2.extend(parser2.feed(c.recv(65536)))
    t_pipe = time.perf_counter() - t0
    c.close()
    return t_seq, t_pipe


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)
    t_seq, t_pipe = bench(box[0])
    print(f"串行 200 条: {t_seq * 1000:.1f}ms ({t_seq / 200 * 1000:.3f}ms/条)")
    print(f"管线 200 条: {t_pipe * 1000:.1f}ms ({t_pipe / 200 * 1000:.3f}ms/条)")
    print(f"提速约 {t_seq / max(t_pipe, 1e-9):.0f}x — 省掉的是 N-1 次 RTT")
    stop.set()
