import multiprocessing


def child(conn) -> None:
    conn.send({"pid_cmd": "hello from child"})
    reply = conn.recv()
    print("child 收到:", reply)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=child, args=(child_conn,))
    p.start()
    msg = parent_conn.recv()
    print("parent 收到:", msg)
    parent_conn.send("hello from parent")
    p.join()
