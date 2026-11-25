---
title: [Q5106] fromisoformat 与 strptime 解析成本账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5106 · fromisoformat 与 strptime 解析成本账

> 难度:★★★☆☆ | 标签:datetime, 成本工程, 热路径

**问**:批量日志解析每秒几十万条时间戳，`datetime.strptime` 成了 CPU 热点，怎么办？

**答**:结论：`strptime` 每次调用都要做格式串解析与正则式匹配（内部 `_strptime` 模块带缓存但仍有 Python 层开销），比 `datetime.fromisoformat`（C 实现、纯格式直读）慢一个数量级（典型 10~30x）。取舍矩阵：ISO 8601 格式一律 `fromisoformat`（3.11+ 已支持 `Z` 后缀与任意分隔符，基线标注：3.10 及以下不含 Z 支持，降级用 `str.replace("Z", "+00:00")`）；非 ISO 固定格式用 `strptime` + 预编译思想（改用 `re` 自己编译一次再取组）；海量固定列场景最后才考虑手写切片解析。实战上，解析成本是批量 ETL 与日志管道（Q5047 同族成本账）里最常见的隐形税，先把格式归一到 ISO 才是治本。

```python
import timeit
from datetime import datetime, timezone

iso = "2026-11-21T09:30:15.123456+00:00"
legacy = "2026/11/21 09:30:15"

d1 = datetime.fromisoformat(iso)                      # C 实现
print("fromisoformat:", d1.isoformat() == iso)

# Python 3.10 及以下的 Z 降级
z = "2026-11-21T09:30:15Z"
d2 = datetime.fromisoformat(z.replace("Z", "+00:00")) if z.endswith("Z") else datetime.fromisoformat(z)
print("Z 降级 OK:", d2.tzinfo is not None)

t_iso = timeit.timeit(lambda: datetime.fromisoformat(iso), number=50_000)
t_strp = timeit.timeit(lambda: datetime.strptime(legacy, "%Y/%m/%d %H:%M:%S"), number=50_000)
print(f"fromisoformat {t_iso:.3f}s | strptime {t_strp:.3f}s | {t_strp/t_iso:.1f}x")

# 固定非 ISO 格式的次优解：一次性编译正则
import re
RX = re.compile(r"(\d{4})/(\d{2})/(\d{2}) (\d{2}):(\d{2}):(\d{2})")
def rx_parse(s):
    y, mo, d, h, mi, se = map(int, RX.match(s).groups())
    return datetime(y, mo, d, h, mi, se)
t_rx = timeit.timeit(lambda: rx_parse(legacy), number=50_000)
print(f"预编译正则 {t_rx:.3f}s")
```

**追问一层**:`strptime` 的缓存（`_strptime` 的 format 缓存）为什么救不了海量调用？
**追二层**:带时区缩写（`%Z`/`CST`）的解析为什么危险？和 zoneinfo 的关系？

**背诵要点**
- strptime 一次十几十 µs，fromisoformat C 直读快 10~30x。
- 3.11+ 的 fromisoformat 才支持 Z 后缀；老版本 replace 降级。
- 治本是格式归一 ISO，正则预编译只是次优解。

**复盘追问**
- 上游日志格式不可控时，管道的格式探测与降级链怎么设计？提示：首行 sniff + 指标计数。
- `fromisoformat` 对非标准（如 `2026-11-21 09:30:15,123`）的兼容边界在哪？提示：3.11 放宽到任意单字符分隔符但不含逗号毫秒。
