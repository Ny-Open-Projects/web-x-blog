# -*- coding: utf-8 -*-
"""线程身份三件套: name / ident / native_id 与 main_thread。

- name 是给人看的, 日志排障的第一线索, 启动前可改;
- ident 是解释器内线程 id, 线程死后可能被复用, 不能当永久键;
- native_id 是操作系统级 tid, 可与 ps/top 的观察对上;
- threading.main_thread() 识别主线程, 守护化逻辑常靠它分流。
"""
import threading
import time


def worker(store):
    cur = threading.current_thread()
    store["worker"] = {
        "name": cur.name,
        "ident": cur.ident,
        "native_id": cur.native_id,
        "is_main": cur is threading.main_thread(),
        "get_ident": threading.get_ident(),
        "get_native_id": threading.get_native_id(),
    }
    time.sleep(0.1)


def main():
    store = {}
    t = threading.Thread(target=worker, args=(store,), name="etl-worker-1")
    print("启动前 name:", t.name, "| ident:", t.ident, "(未启动为 None)")
    t.name = "etl-worker-1-b"      # 启动前改名合法
    t.start()
    t.join()
    w = store["worker"]
    print("worker 视角: name=%s ident=%s native_id=%s is_main=%s" %
          (w["name"], w["ident"], w["native_id"], w["is_main"]))
    print("get_ident 与 t.ident 一致:", w["get_ident"] == w["ident"])
    print("get_native_id 与 native_id 一致:", w["get_native_id"] == w["native_id"])

    m = threading.main_thread()
    print("主线程: name=%s ident=%s native_id=%s" %
          (m.name, m.ident, m.native_id))
    print("ident 全局唯一性: 主线程与 worker 不同:",
          m.ident != w["ident"])

    t2 = threading.Thread(target=lambda: None)
    t2.start()
    alive_ident = t2.ident
    t2.join()
    print("线程死后 ident 属性仍可读但已失效:", alive_ident, "-> is_alive:",
          t2.is_alive())


if __name__ == "__main__":
    main()
