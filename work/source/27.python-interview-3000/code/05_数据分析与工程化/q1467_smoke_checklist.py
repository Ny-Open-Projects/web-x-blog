"""发布前冒烟清单自动化:关键路径逐项检查,全部通过才放行"""

SERVICE = {
    "health": {"status": "ok"},
    "db": {"connected": True, "version": "8.0.36"},
    "orders_api": {"sample_query_ms": 180, "rows": 42},
    "metrics": {"freshness_seconds": 120},
}

CHECKS = [
    ("健康检查 200", lambda s: s["health"]["status"] == "ok"),
    ("数据库连通", lambda s: s["db"]["connected"]),
    ("样例查询 < 500ms", lambda s: s["orders_api"]["sample_query_ms"] < 500),
    ("样例查询有数据", lambda s: s["orders_api"]["rows"] > 0),
    ("指标新鲜度 < 5 分钟", lambda s: s["metrics"]["freshness_seconds"] < 300),
]


def smoke(service):
    results, passed = [], 0
    for name, check in CHECKS:
        try:
            ok = bool(check(service))
        except Exception as exc:  # 冒烟检查自身不能被异常打断
            ok, reason = False, repr(exc)
        results.append((name, ok))
        passed += ok
    return passed, len(CHECKS), results


if __name__ == "__main__":
    passed, total, results = smoke(SERVICE)
    for name, ok in results:
        print(("PASS " if ok else "FAIL "), name)
    print(f"\n冒烟结果 {passed}/{total} ->", "放行,继续灰度" if passed == total else "阻断发布")
