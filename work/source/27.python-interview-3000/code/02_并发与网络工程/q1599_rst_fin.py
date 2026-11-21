"""RST 与 FIN 的语义差: SO_LINGER 实验。

- FIN(四次挥手的关闭): "我说完了", 缓冲区数据仍会送达, 对端 recv 得 b"";
- RST(重置): "这条连接死了", 未读数据直接丢弃, 对端 recv 抛
  ConnectionResetError; SO_LINGER(l_onoff=1, l_linger=0) 让 close 改发 RST。
对端感知不同: 前者是干净的下线, 后者是"要么对端崩溃, 要么被防火墙重置"。
"""
import socket
import struct
import threading
import time


def serve(port_slot, behavior):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    port_slot.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    time.sleep(0.1)                         # 等客户端 connect 返回, 再谈断开
    if behavior == "fin":
        conn.recv(1024)                     # 读一条, 表示业务收到
        conn.close()                        # 正常 close -> FIN
    else:                                   # rst
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.pack("ii", 1, 0))
        conn.close()                        # 立即 RST, 未读数据一并丢弃
    srv.close()


def client_check(port):
    s = None
    for attempt in range(3):                # 连接竞态防护: 服务端刚起时重试
        try:
            s = socket.create_connection(("127.0.0.1", port), timeout=1.0)
            break
        except OSError:
            if attempt == 2:
                raise
            time.sleep(0.1)
    s.settimeout(1.0)
    s.sendall(b"hello")                     # RST 场景下服务端根本不读
    try:
        data = s.recv(1024)
        return ("recv-eof", data)
    except ConnectionResetError:
        return ("reset", None)
    except socket.timeout:
        return ("timeout", None)
    finally:
        s.close()


def main():
    fin_slot, rst_slot = [], []
    t1 = threading.Thread(target=serve, args=(fin_slot, "fin"), daemon=True)
    t2 = threading.Thread(target=serve, args=(rst_slot, "rst"), daemon=True)
    t1.start()
    t2.start()
    while not (fin_slot and rst_slot):      # bind 完成即端口可用
        threading.Event().wait(0.01)

    out_fin = client_check(fin_slot[0])
    print("FIN 场景客户端感知:", out_fin)
    assert out_fin == ("recv-eof", b""), "正常关闭应读到干净 EOF"

    out_rst = client_check(rst_slot[0])
    print("RST 场景客户端感知:", out_rst)
    assert out_rst == ("reset", None), "SO_LINGER 0 关闭应触发 ConnectionResetError"

    print("结论: FIN 是'说完了', RST 是'死了'; 排障时先分清是哪种断开")


if __name__ == "__main__":
    main()
