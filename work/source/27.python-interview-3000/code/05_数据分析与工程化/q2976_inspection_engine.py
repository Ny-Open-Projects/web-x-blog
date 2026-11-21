"""巡检完整清单引擎: 检查项注册 -> 自动重试 -> 分级结论 -> 汇总报告与退出码"""
import json

TRANSIENT = {"heartbeat_calls": 0}   # 可注入的瞬时故障状态


def check_disk():
    """磁盘水位: 模拟根分区使用率 85%, 阈值 90"""
    used_pct = 85
    if used_pct >= 90:
        raise RuntimeError("根分区使用率 %d%%" % used_pct)
    return "根分区使用率 %d%%" % used_pct


def check_config():
    """配置可解析: 第二个配置文件是坏的"""
    texts = {"db.json": '{"port": 5432}', "es.json": '{"hosts": [}'}  # 后者 JSON 残缺
    bad = []
    for name, text in texts.items():
        try:
            json.loads(text)
        except ValueError:
            bad.append(name)
    if bad:
        raise RuntimeError("无法解析 " + ", ".join(bad))
    return "全部配置可解析"


def check_heartbeat():
    """服务心跳: 前一次探测超时, 重试后恢复 -> 验证重试机制"""
    TRANSIENT["heartbeat_calls"] += 1
    if TRANSIENT["heartbeat_calls"] == 1:
        raise RuntimeError("订单服务心跳超时 3s")
    return "订单服务心跳正常"


def check_cert():
    """证书有效期: 剩 21 天, 低于 30 天告警但不阻断"""
    days_left = 21
    if days_left < 30:
        raise RuntimeError("证书剩 %d 天" % days_left)
    return "证书剩 %d 天" % days_left


class InspectionEngine:
    def __init__(self):
        self.items = []

    def register(self, name, fn, severity="FAIL", retries=0):
        self.items.append({"name": name, "fn": fn, "severity": severity, "retries": retries})

    def run(self):
        """逐项执行: 重试耗尽后才落定 FAIL/WARN, 汇总出总体结论与退出码"""
        results = []
        for item in self.items:
            detail, ok, attempts = "", False, 0
            for i in range(item["retries"] + 1):
                attempts = i + 1
                try:
                    detail = item["fn"]()
                    ok = True
                    break
                except Exception as e:
                    detail = str(e)
            status = "PASS" if ok else item["severity"]
            results.append({"name": item["name"], "status": status,
                            "attempts": attempts, "detail": detail})
        has_fail = any(r["status"] == "FAIL" for r in results)
        has_warn = any(r["status"] == "WARN" for r in results)
        verdict = "FAIL" if has_fail else ("WARN" if has_warn else "PASS")
        exit_code = 1 if has_fail else 0
        return {"results": results, "verdict": verdict, "exit_code": exit_code}


if __name__ == "__main__":
    eng = InspectionEngine()
    eng.register("磁盘水位", check_disk)
    eng.register("配置可解析", check_config)
    eng.register("服务心跳", check_heartbeat, retries=2)   # 瞬时抖动给重试
    eng.register("证书有效期", check_cert, severity="WARN")

    rep = eng.run()
    for r in rep["results"]:
        mark = {"PASS": "PASS", "FAIL": "FAIL", "WARN": "WARN"}[r["status"]]
        print("[%s] %-8s 尝试 %d 次 | %s" % (mark, r["name"], r["attempts"], r["detail"]))
    print("总体结论: %s, 退出码 %d" % (rep["verdict"], rep["exit_code"]))
    print("要点: 瞬时故障靠重试消除而不是告警, 常年不修的靠 WARN 降级记录, FAIL 决定退出码从而接入 cron 与值班升级")
