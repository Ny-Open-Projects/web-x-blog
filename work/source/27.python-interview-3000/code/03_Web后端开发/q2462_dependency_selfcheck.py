"""服务依赖自检脚本与就绪判定(纯标准库)。"""
import json
import shutil
import socket
import threading
import time


def check_disk(min_free_bytes):
    usage = shutil.disk_usage("/")
    return usage.free >= min_free_bytes, "剩余 {:.1f} MB / 需要 {:.1f} MB".format(
        usage.free / 1048576, min_free_bytes / 1048576)


def check_env(required):
    missing = [name for name in required if not __import__("os").environ.get(name)]
    return not missing, ("全部就绪" if not missing
                         else "缺失: " + ",".join(missing))


def check_tcp(host, port, timeout=1.0):
    t0 = time.perf_counter()
    sock = socket.socket()
    sock.settimeout(timeout)
    try:
        rc = sock.connect_ex((host, port))
    finally:
        sock.close()
    ms = (time.perf_counter() - t0) * 1000
    return rc == 0, "connect {}:{} {} ({:.0f}ms)".format(
        host, port, "成功" if rc == 0 else "失败 rc={}".format(rc), ms)


def run_checks(cfg):
    results = []
    for name, fn in cfg["checks"]:
        t0 = time.perf_counter()
        try:
            ok, detail = fn()
        except Exception as exc:                  # 自检自身异常按失败处理
            ok, detail = False, "检查异常: {}".format(exc)
        results.append({"name": name, "ok": ok, "detail": detail,
                        "ms": round((time.perf_counter() - t0) * 1000, 1)})
    report = {"ready": all(r["ok"] for r in results), "checks": results}
    return report


# 准备一个可连通的回环依赖与一个必挂的端口
gate = socket.socket()
gate.bind(("127.0.0.1", 0))
gate.listen(5)
good_port = gate.getsockname()[1]
bad_port = 1                                        # 回环上通常无监听
stop = {"flag": False}


def acceptor():
    """替身依赖: 接受连接后立即关闭, 模拟一个健康的 TCP 服务。"""
    gate.settimeout(0.2)
    while not stop["flag"]:
        try:
            conn, _ = gate.accept()
            conn.close()
        except socket.timeout:
            pass
        except OSError:
            break


worker = threading.Thread(target=acceptor, daemon=True)
worker.start()

cfg = {
    "checks": [
        ("disk", lambda: check_disk(10 * 1024 * 1024)),
        ("env", lambda: check_env(["PATH"])),
        ("db", lambda: check_tcp("127.0.0.1", good_port)),
        ("cache", lambda: check_tcp("127.0.0.1", bad_port, 0.3)),
    ]
}

report = run_checks(cfg)
print(json.dumps(report, ensure_ascii=False, indent=2))
assert report["ready"] is False                     # cache 挂了整体不就绪
by_name = {c["name"]: c for c in report["checks"]}
assert by_name["db"]["ok"] and not by_name["cache"]["ok"]

cfg2 = {"checks": [c for c in cfg["checks"] if c[0] != "cache"]}
report2 = run_checks(cfg2)
print("去掉 cache 后 ready =", report2["ready"])
assert report2["ready"] is True
stop["flag"] = True
gate.close()
worker.join(1)
print("要点: 自检脚本把 就绪 判定收敛成一条 all, 每项带耗时与失败原因, "
      "输出 JSON 既能给探针用也能贴进工单; 任一依赖失败都不该对外宣称 ready")
