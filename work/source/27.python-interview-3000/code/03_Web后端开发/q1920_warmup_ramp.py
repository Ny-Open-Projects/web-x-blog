"""新实例流量爬坡: 预热期的权重阶梯与就绪判据(纯标准库)。"""
import random

STAGES = [          # (上线秒数, 权重百分比, 通过判据: 错误率上限, p95 上限秒)
    (0, 1, 1.00, 3.0),
    (10, 5, 0.05, 2.0),
    (30, 20, 0.02, 1.0),
    (60, 50, 0.01, 0.8),
    (120, 100, 0.01, 0.8),
]


def weight_for(age, error_rate, p95):
    """按实例年龄选阶段, 但指标不达标就原地踏步, 不达标不升级。"""
    current = STAGES[0]
    for stage in STAGES:
        if age >= stage[0] and error_rate <= stage[2] and p95 <= stage[3]:
            current = stage
    return current[1]


def split_traffic(new_weight):
    """新旧实例按权重分流; 返回 (新实例份额, 旧实例份额)。"""
    new_weight = max(1, new_weight)
    return new_weight, 100 - new_weight


random.seed(11)
health = {"error_rate": 0.0, "p95": 0.5}
plan = []
for tick in range(0, 150, 10):
    w = weight_for(tick, health["error_rate"], health["p95"])
    plan.append((tick, w))
print("健康时的爬坡计划:", plan)
assert plan[0][1] == 1 and plan[-1][1] == 100

# 预热期出现慢查询: 权重卡在低档不再上升
health_bad = {"error_rate": 0.03, "p95": 1.5}
stuck = [(t, weight_for(t, health_bad["error_rate"], health_bad["p95"]))
         for t, _ in plan]
print("指标不达标时的实际权重:", stuck)
assert all(w <= 20 for _, w in stuck)

for _, w in plan:
    new, old = split_traffic(w)
    assert 0 < new and old >= 0 and new + old == 100
print("要点: 爬坡解决的是缓存与 JIT 类运行时的冷启动, 判据是一票否决, 指标坏住就冻结放量")
