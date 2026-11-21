---
title: [Q2008] 配置漂移检测:多实例配置 diff
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2008 · 配置漂移检测:多实例配置 diff

> 难度:★★★☆ | 标签:配置管理, 漂移检测

**问**:线上十几台实例,怎么保证它们的配置和基准一致?"有人上机改过"这种事怎么发现?

**答**:实例多了配置必然漂:有人 SSH 上去改参数忘了同步、发布部分失败、灰度实例参数不同。漂移检测三步:基准配置入库版本化;定时拉取各实例实际配置;逐键 diff 分三类(缺失/多余/不同),敏感键(db_host、auth_url)单独分级,漂移立即告警。实测 node-2 有三项漂移且 db_host 指向 staging,是"实例连错环境"的典型事故,普通 diff 只会说三个键不一样,敏感键分级才能定级响应。修复方向是回归基准而不是把漂移固化成新基准——"大家都这么配"式改基准会掩埋变更语义。检测要覆盖配置加载后的最终值,环境变量注入的漂移只有运行时才暴露。

```python
# file: code/05_数据分析与工程化/q2008_config_drift.py
"""配置漂移检测:各实例配置对基准逐键 diff,敏感键单独分级"""

BASELINE = {
    "log_level": "INFO", "timeout": 30, "max_conn": 100,
    "feature_dark_mode": "on", "db_host": "db.internal",
}
SENSITIVE = {"db_host", "auth_url"}   # 这些键漂移必须立即告警
INSTANCES = {
    "node-1": {"log_level": "INFO", "timeout": 30, "max_conn": 100,
               "feature_dark_mode": "on", "db_host": "db.internal"},
    "node-2": {"log_level": "DEBUG", "timeout": 30, "max_conn": 80,
               "feature_dark_mode": "on", "db_host": "db-staging.internal",
               "legacy_flag": "on"},
    "node-3": {"log_level": "INFO", "timeout": 60, "max_conn": 100,
               "feature_dark_mode": "off", "db_host": "db.internal"},
}


def diff(baseline, actual):
    keys = set(baseline) | set(actual)
    out = {}
    for k in sorted(keys):
        if k not in actual:
            out[k] = ("缺失", baseline[k])
        elif k not in baseline:
            out[k] = ("多余", actual[k])
        elif baseline[k] != actual[k]:
            out[k] = ("不同", f"{baseline[k]} -> {actual[k]}")
    return out


if __name__ == "__main__":
    for node, cfg in INSTANCES.items():
        d = diff(BASELINE, cfg)
        if not d:
            print(f"{node}: 一致")
            continue
        critical = [k for k in d if k in SENSITIVE]
        suffix = f"  <敏感键漂移 {critical},立即处理>" if critical else ""
        print(f"{node}: 漂移 {len(d)} 项 {d}{suffix}")
    print("要点:基准配置入库版本化,实例配置定时拉回 diff;缺失/多余/不同三类分开报;漂移修复是回归基准,而不是把漂移固化成新基准")
```

**追问**:
- 追问 1:合法的实例差异(如分片数不同)怎么办?—— 基准支持按实例组的覆盖层,diff 对着"该实例应有的基准"做,而不是全局单一基准。
- 追问 2:多久检测一次?—— 配置变更后即时检测加每日全量兜底,漂移的破坏力随时间放大。
