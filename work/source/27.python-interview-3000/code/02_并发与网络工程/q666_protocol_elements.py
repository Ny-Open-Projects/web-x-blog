import socket
import threading

# 语法: 文本帧, 命令+参数, \n 分隔
# 语义: 每个命令的参数与响应
# 时序: 状态机 ALLOWED = 当前状态 → {命令: 下一状态}
TRANSITIONS = {
    "INIT": {"HELLO": "GREETED"},
    "GREETED": {"AUTH": "READY", "BYE": "CLOSED"},
    "READY": {"DATA": "READY", "BYE": "CLOSED"},
}


def serve(conn: socket.socket) -> None:
    state = "INIT"
    conn.settimeout(2)
    try:
        while state != "CLOSED":
            line = conn.recv(256).decode().strip()
            if not line:
                break
            cmd = line.split(" ")[0]
            nxt = TRANSITIONS.get(state, {}).get(cmd)
            if nxt is None:
                conn.sendall(f"ERR out-of-order {cmd} in {state}\n".encode())  # 时序违规
                continue
            if cmd == "AUTH" and len(line.split(" ")) < 2:
                conn.sendall(b"ERR missing token\n")  # 语义校验
                continue
            state = nxt
            conn.sendall(f"OK state={state}\n".encode())
    except (OSError, socket.timeout):
        pass
    finally:
        conn.close()


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
        threading.Thread(target=serve, args=(conn,), daemon=True).start()
    srv.close()


def run_client(port: int, script: list) -> None:
    c = socket.create_connection(("127.0.0.1", port), timeout=2)
    for line in script:
        c.sendall((line + "\n").encode())
        c.settimeout(2)
        print(f"  发 {line!r} → {c.recv(256).decode().strip()}")
    c.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)
    print("正常时序:")
    run_client(box[0], ["HELLO", "AUTH token-1", "DATA payload", "BYE"])
    print("违规时序 (未 HELLO 直接 DATA):")
    run_client(box[0], ["DATA payload", "HELLO"])
    stop.set()
