"""应急演练的评分引擎: 预期对照与退步检测"""

from collections import namedtuple

Step = namedtuple("Step", "name expect actual budget_s used_s")
CURRENT = [
    Step("摘除流量", "成功", "成功", 60, 40),
    Step("切换备用", "成功", "成功", 120, 150),
    Step("数据校验", "通过", "通过", 60, 90),
    Step("恢复流量", "成功", "超时", 60, 120),
]
LAST = {"摘除流量": 45, "切换备用": 120, "数据校验": 70, "恢复流量": 90}


def score(steps, last):
    passed = 0
    regress = []
    for s in steps:
        if s.expect == s.actual:
            passed += 1
        if s.used_s > last.get(s.name, s.used_s) * 1.2:
            regress.append(f"{s.name} {s.used_s}s 对上次 {last[s.name]}s")
    return passed / len(steps), regress


if __name__ == "__main__":
    rate, regress = score(CURRENT, LAST)
    for s in CURRENT:
        mark = "PASS" if s.expect == s.actual else "FAIL"
        print(f"  [{mark}] {s.name}: 预期 {s.expect} 实际 {s.actual} 用时 {s.used_s}s 预算 {s.budget_s}s")
    print(f"步骤通过率 {rate:.0%}; 耗时退步项: {regress if regress else '无'}")
    print("要点: 通过但变慢也是退步; FAIL 直接生成整改单; 分数入台账看季度趋势")
