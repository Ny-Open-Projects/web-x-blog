import socket
import threading
import time
import uuid

BOUNDARY = "----pyboundary" + uuid.uuid4().hex[:16]


def build_multipart(fields: dict, file_field: tuple) -> bytes:
    """fields: 普通字段; file_field: (name, filename, content, ctype)。"""
    lines: list = []
    for name, value in fields.items():
        lines.append(f"--{BOUNDARY}\r\n".encode())
        lines.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        lines.append(value.encode() + b"\r\n")
    name, filename, content, ctype = file_field
    lines.append(f"--{BOUNDARY}\r\n".encode())
    lines.append(
        f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'.encode()
    )
    lines.append(f"Content-Type: {ctype}\r\n\r\n".encode())
    lines.append(content + b"\r\n")
    lines.append(f"--{BOUNDARY}--\r\n".encode())
    return b"".join(lines)


def parse_multipart(body: bytes, boundary: str) -> list:
    parts = []
    delim = b"--" + boundary.encode()
    for seg in body.split(delim):
        seg = seg.strip(b"\r\n-")
        if not seg or seg == b"--":
            continue
        head, _, content = seg.partition(b"\r\n\r\n")
        headers = {}
        for line in head.split(b"\r\n"):
            if b": " in line:
                k, v = line.split(b": ", 1)
                headers[k.decode().lower()] = v.decode()
        disp = headers.get("content-disposition", "")
        name = disp.split('name="')[1].split('"')[0] if 'name="' in disp else ""
        filename = disp.split('filename="')[1].split('"')[0] if 'filename="' in disp else None
        parts.append({"name": name, "filename": filename, "content": content})
    return parts


def server(stop: threading.Event, port_box: list, received: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            conn.settimeout(3)
            data = b""
            while b"\r\n\r\n" not in data:
                data += conn.recv(65536)
            head, body = data.split(b"\r\n\r\n", 1)
            ctype = next(l.split(b": ", 1)[1].decode() for l in head.split(b"\r\n")
                         if l.lower().startswith(b"content-type"))
            boundary = ctype.split("boundary=")[1]
            received.extend(parse_multipart(body, boundary))
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nok")
        except Exception as e:
            print("[server] 解析失败:", repr(e))
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    got: list = []
    threading.Thread(target=server, args=(stop, box, got), daemon=True).start()
    while not box:
        time.sleep(0.01)

    file_content = b"PNG-data\x00\x01\x02-with\r\nnewlines"  # 内容含 \r\n 验证解析正确
    body = build_multipart(
        fields={"note": "hello"},
        file_field=("file", "img.png", file_content, "image/png"),
    )
    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(
        b"POST /upload HTTP/1.1\r\n"
        + f"Content-Type: multipart/form-data; boundary={BOUNDARY}\r\n".encode()
        + f"Content-Length: {len(body)}\r\n\r\n".encode()
        + body
    )
    c.settimeout(2)
    print("上传响应:", c.recv(64).split(b"\r\n")[0].decode())
    c.close()

    for p in got:
        print(f"  part name={p['name']} filename={p['filename']} bytes={len(p['content'])}")
    f = next(p for p in got if p["name"] == "file")
    assert f["content"] == file_content, "二进制内容被破坏"
    print("二进制内容往返一致, multipart 编解码正确")
    stop.set()
