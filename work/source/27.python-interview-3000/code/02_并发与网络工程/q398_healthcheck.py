"""分层健康检查脚本:liveness 与 readiness 分离,标准库可运行。"""
import json
import shutil
import socket
import time


def check_port(host, port, timeout=2.0) -> tuple:
    start = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, time.perf_counter() - start
    except OSError:
        return False, time.perf_counter() - start


def disk_usage_ok(path="/", min_free_gb=1.0) -> bool:
    usage = shutil.disk_usage(path)
    return usage.free >= min_free_gb * 1024 ** 3


def liveness() -> dict:
    """只关心进程自身能否响应, 不检查外部依赖。"""
    return {"status": "ok", "ts": time.time()}


def readiness() -> dict:
    """检查依赖, 决定是否接流量。"""
    db_ok, db_latency = check_port("1.1.1.1", 53)  # 演示用公共 DNS, 实际换成 DB
    checks = {
        "db": {"ok": db_ok, "latency_ms": round(db_latency * 1000, 1)},
        "disk": {"ok": disk_usage_ok(min_free_gb=0.001)},
    }
    return {"status": "ok" if all(c["ok"] for c in checks.values()) else "degraded",
            "checks": checks, "ts": time.time()}


if __name__ == "__main__":
    print(json.dumps(liveness()))
    print(json.dumps(readiness(), ensure_ascii=False, indent=2))
