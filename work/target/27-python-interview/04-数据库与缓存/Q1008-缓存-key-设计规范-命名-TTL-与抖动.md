---
title: [Q1008] 缓存 key 设计规范: 命名、TTL 与抖动
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1008 · 缓存 key 设计规范: 命名、TTL 与抖动

> 难度:★★☆☆ | 标签:key 设计, 规范

**问**:缓存 key 怎么命名才不乱?TTL 为什么要加随机抖动?

**答**:命名三段式:`业务:对象:标识`,如 `mall:stock:sku123`、`mall:user:profile:{uid}`,用冒号分隔(guish 常见约定),全小写、禁空格;好处是可读、可按前缀统计(scan mall:stock:*)、可按前缀清理。TTL 纪律:所有 key 必须带 TTL(防止忘记删除的僵尸键);同一批次的 key 加随机抖动(TTL ± 10%~20%),避免"同一秒批量加载的缓存同时过期"造成集体回源的惊群;数据版本变化用 key 带版本(v2)整体切换。长度控制:key 本身也是内存与网络成本,长 uuid 全量拼进 key 要斟酌。大促场景的 key 生命周期要单独评审(临时 key 用完即删)。

```python
# file: code/04_数据库与缓存/q1008_key_design.py
"""key 构造器 + TTL 抖动"""
import random

class KeyBuilder:
    def __init__(self, app="mall"):
        self.app = app

    def make(self, *parts) -> str:
        return ":".join([self.app] + [str(p).lower() for p in parts])

def ttl_with_jitter(base_sec, jitter_ratio=0.15):
    delta = base_sec * jitter_ratio
    return int(base_sec + random.uniform(-delta, delta))

if __name__ == "__main__":
    kb = KeyBuilder()
    print(kb.make("stock", "sku123"))
    print(kb.make("user", "profile", 10086))
    print("同批缓存 TTL 抖动:", [ttl_with_jitter(300) for _ in range(6)])
    print("无抖动 1000 个 key 同秒过期 -> 集体回源 = 惊群; 有抖动则错峰")
```

**追问**:
- 用户维度 key 里放手机号安全吗?——不安全,key 可见性高(慢日志/监控/误读),用 uid 或哈希;敏感字段永不进 key 与日志。
- 版本化 key(v2)怎么清理旧版本?——切换后旧前缀批量 SCAN+UNLINK,或旧版本 TTL 自然过期,避免双份内存长期共存。

---
