---
title: [Q1925] 指标基数治理: label 设计与爆炸预防
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1925 · 指标基数治理: label 设计与爆炸预防

> 难度:★★★★ | 标签:监控, Prometheus

**问**:加一个 label 的代价是什么?为什么 user_id 不能进指标?

**答**:指标基数是各 label 取值数的笛卡尔积,每加一个维度都是乘法:method 7 乘 route 40 乘 status_class 5 等于 1400 个系列看着安全,再乘 user_id 的 5000 就是 700 万,采集、存储、查询全链路爆炸,单条高基数指标拖垮监控集群是典型事故。治理三招:注册守卫——指标上线时预估基数,超过容量上限直接拒绝;有界桶——高基数维度映射到有限桶(用户分层、状态枚举、路径模板),个案细节去日志与 trace 查;声明审计——label 白名单进指标注册表,出现未声明维度即告警。判断维度去留的问句:这个维度会用于告警与看板聚合吗?会才进 label,只用于个案排查的维度一律走日志。存量爆炸的指标不能直接删,先停新维度、保留旧系列自然过期,迁移到新指标。

```python
# file: code/03_Web后端开发/q1925_label_cardinality.py
"""指标基数治理: label 设计与爆炸预防(纯标准库)。"""


def estimate_series(base_labels, extra_label_values):
    """基数是各 label 取值数的笛卡尔积; 返回 (总系列数, 各 label 值数)。"""
    total = 1
    detail = {}
    for name, values in list(base_labels.items()) + list(extra_label_values.items()):
        n = values if isinstance(values, int) else len(values)
        detail[name] = n
        total *= n
    return total, detail


def guard(name, total, cap=20000):
    """注册指标时做基数守卫: 超过容量上限直接拒绝上线。"""
    if total > cap:
        raise ValueError("指标 {} 的预估基数 {} 超过上限 {}".format(name, total, cap))
    return "ok"


base = {"method": 7, "route_template": 40, "status_class": 5}
total, detail = estimate_series(base, {})
print("请求计数器基数: {} = {} 的乘积".format(total, detail))
assert guard("http_requests_total", total) == "ok"

# 反例: 把 user_id 塞进 label, 千用户乘上去瞬间爆炸
try:
    total_bad, _ = estimate_series(base, {"user_id": 5000})
    print("带 user_id 的基数:", total_bad)
    guard("http_requests_by_user", total_bad)
    raise AssertionError("守卫未生效")
except ValueError as e:
    print("守卫拦截:", e)

# 正确姿势: 高基数维度进日志与追踪, 指标只留有界桶
def user_bucket(user_id):
    if user_id.startswith("enterprise-"):
        return "tier:enterprise"
    return "tier:self-serve"


total_ok, _ = estimate_series(base, {"user_tier": 2})
print("用有界桶替代 user_id 后基数:", total_ok, "样例映射:",
      user_bucket("enterprise-a"), user_bucket("u9999"))
assert guard("http_requests_by_tier", total_ok) == "ok"
print("要点: label 每加一个维度都是乘法, 指标只留可枚举维度, 用户级细节去日志和 trace 里查")
```

**追问**:
- histogram 的 bucket 算基数吗?——算,bucket 数乘 label 组合,延迟指标要控制 bucket 数量与 label 精简。
- 基数上限定多少?——按监控集群容量算单指标配额,常规服务单指标几千系列,超一万必须有充分理由。
