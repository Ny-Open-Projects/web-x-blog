---
title: [Q5514] socket.sendfile 零拷贝路径与限制
date: 2026-11-19
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5514 · socket.sendfile 零拷贝

> 难度:★★☆ | 标签:零拷贝, I/O

**问**：「发一个 2GB 文件给客户端」有几种写法？`socket.sendfile` 的零拷贝路径具体省了哪几次拷贝、哪次系统调用？它什么时候会**静默退化**成普通写？

**答**：三层写法对比：① 普通 `sock.send(chunk)` 循环：用户态分配 buffer → `read()`（磁盘→页缓存→用户态 1 次拷贝）→ `send()`（用户态→内核 socket 缓冲 1 次拷贝），共 4 次拷贝 2 次系统调用/块；② `sendfile`（`socket.socket.sendfile`）：`os.sendfile` 让内核直接**页缓存 → socket 缓冲**（fd 到 fd），省掉 2 次用户态拷贝，且大文件配合 `sendfile(2)` 零 CPU 参与数据搬运；③ 零拷贝极致是 `splice`/`mmap+write`（Python 标准库不直接暴露）。静默退化：`socket.sendfile` 遇到**非普通文件**（socket/管道）、或 OS 不支持对应系统调用（macOS 用 sendfile(2) 但语义略异）、或 **SSL 包裹的 socket**——`ssl.SSLSocket.sendfile` 会退化为 `send` 循环（TLS 必须用户态加密，零拷贝天然不适用）。所以「TLS 终止在应用层的静态文件服务」吃不到 sendfile 红利，要零拷贝就得把 TLS 下沉到内核态（kTLS）或前置网关。

```python
# 全部标准库；demo 对比三种发法的耗时结构（本地回环）
import socket, os, tempfile, time, threading

def make_file(size_mb=50):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".bin")
    f.write(os.urandom(size_mb * 1024 * 1024)); f.close()
    return f.name

def serve(path, mode):
    srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0)); srv.listen(1)
    port = srv.getsockname()[1]
    def run():
        conn, _ = srv.accept()
        if mode == "sendfile":
            with open(path, "rb") as f:
                conn.sendfile(f)                  # 零拷贝路径（macOS sendfile(2)）
        else:
            with open(path, "rb") as f:
                while chunk := f.read(1024 * 1024):
                    conn.sendall(chunk)           # 用户态循环
        conn.close()
    threading.Thread(target=run, daemon=True).start()
    return port

def fetch(port):
    s = socket.create_connection(("127.0.0.1", port))
    got = 0
    while s.recv(1024 * 1024):
        got += 1
    s.close()
    return got

if __name__ == "__main__":
    path = make_file(50)
    for mode in ("send", "sendfile"):
        port = serve(path, mode)
        t0 = time.perf_counter()
        blocks = fetch(port)
        dt = time.perf_counter() - t0
        print(f"{mode:9s}: {blocks}MB {dt:.2f}s")
        # 回环上差距被协议栈摊薄；真实磁盘大文件 + 适中网络下 sendfile 的 CPU 降幅更显著
    os.unlink(path)
    # 退化清单：ssl.SSLSocket.sendfile 退化为 send 循环（TLS 要用户态加密）；
    # 非普通文件（管道/socket）退化；count/offset 参数限制内走零拷贝，超出部分走 send。
```

**追问**：1) 为什么 TLS 下零拷贝不成立？——TLS 要求每段数据经 MAC/加密（用户态密码套件），内核直接搬运跳过了加密；kTLS 把加密下沉内核后才恢复 sendfile 红利。2) `sendfile` 和 `mmap` + `send` 谁更好？——mmap 走页缓存映射省一次显式 read 拷贝但仍需用户态参与，且大文件映射表管理复杂；sendfile 在内核内完成，页缓存友好；小文件差异可忽略。3) Nginx 的 `sendfile on` + Python 应用层静态服务的取舍？——静态文件不该由 Python 应用发：前置 Nginx/CDN 开 sendfile，Python 只做动态；应用内做静态服务是部署事故源。

## 背诵要点
1. send 循环 4 次拷贝/块；sendfile 省 2 次用户态拷贝、数据搬运零 CPU 参与。
2. 退化三连：TLS socket（退 send 循环）、非普通文件、不支持的系统调用——「退化静默」要监控。
3. 静态文件服务归属：前置网关开 sendfile，Python 应用只做动态请求。

## 复盘追问
1. 大文件下载的限速怎么做才不占线程？（提示：sendfile 分段 + sleep/令牌桶控制 offset 推进）
2. 断点续传配合 sendfile 怎么实现？（提示：offset/count 参数天然支持 Range 请求映射）
