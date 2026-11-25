---
title: "[Q6762] 附近的人怎么查：geohash 前缀召回与边界漏召回的账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6762 · 附近的人怎么查：geohash 前缀召回与边界漏召回的账

难度：P6 ｜ 标签：Redis、GEO、geohash、空间索引、范围查询

基线：Python 3.12；实现 geohash 编码与九宫格邻域召回，演示"同前缀不相邻"的边界漏召回与修复，标准库实现可直接运行。

**问**：做"附近的人"，要求 1km 内按距离排序返回。DB 里经纬度是两个 float 列，`WHERE lat BETWEEN ... AND lng BETWEEN ...` 的联合索引怎么写都别扭。geohash 把经纬度编码成一个可前缀索引的字符串，它是什么原理？为什么"hash 前缀相同的点"不一定真的近？生产上怎么做才不漏召回？

**答**：
- **结论**：geohash 是**把二维经纬度二分交替编码成一维字符串**：经度二分定左右、纬度二分定上下，每加一位精度翻倍，前缀相同的点落在同一（近似）网格里，于是"范围查找"退化成"字符串前缀查找"——B-tree/Redis zset（score 用 52bit geohash）都能直接用。但网格是**矩形分块**：两个相邻位置可能被边界切开、分到完全不同的前缀（比如格子中央 vs 格子边缘只差 10 米但 hash 第一位就不同），只查自己的 hash 前缀必然漏召回。正确姿势：**以目标点为中心查"自己的格子 + 周围 8 个邻格"共 9 格**（或按搜索半径推算需要的精度与格子数），召回候选集后**回算真实距离排序**——geohash 只做粗筛，精确距离由 Haversine 计算。
- **取舍**：① 精度位数的账：5 位 geohash 格子约 4.9km×4.9km，6 位约 1.2km——位数越高候选越少但邻格查询越多，按搜索半径选精度（半径 1km 通常用 5 位查 9 格）；② 与 R-tree 对比：geohash 实现简单、直接落在已有索引上，但只适合"点查询+半径"，多边形/复杂空间关系要 R-tree；③ 候选集大时要限制（按半径估算密度），超限就升精度缩格子；④ 距离排序放在应用层或用 Redis `GEORADIUS`（底层同 geohash+zset）。
- **实战**：① key 设计按"格子 hash"组织（`geo:{geohash}` 孚集合），或直接用 Redis GEO 结构免手写；② 边界漏召回用"9 宫格必查"兜底，别省那 8 次查询——漏召回是体验事故，多查是无感成本；③ 移动对象更新频率高时，geohash 变更即迁移 zset 成员（Q6566 的写放大账），更新限频防抖动；④ 距离展示与排序统一用同一 Haversine 函数，避免前端后端各算一套对不上。

```python
"""geohash 编码 + 九宫格邻域召回：演示边界漏召回与修复。"""
import math

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def geohash(lat: float, lng: float, precision: int) -> str:
    """二分交替编码：奇偶位分别二分经度/纬度。"""
    lat_lo, lat_hi = -90.0, 90.0
    lng_lo, lng_hi = -180.0, 180.0
    bits, chars, even = [], [], True
    while len(chars) < precision:
        if even:                                # 经度二分
            mid = (lng_lo + lng_hi) / 2
            bits.append(1 if lng > mid else 0)
            if lng > mid:
                lng_lo = mid
            else:
                lng_hi = mid
        else:                                   # 纬度二分
            mid = (lat_lo + lat_hi) / 2
            bits.append(1 if lat > mid else 0)
            if lat > mid:
                lat_lo = mid
            else:
                lat_hi = mid
        even = not even
        if len(bits) == 5:
            chars.append(BASE32[int("".join(map(str, bits)), 2)])
            bits = []
    return "".join(chars)


def haversine_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lng2 - lng1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def neighbors9(lat: float, lng: float, precision: int, all_points: list[tuple]) -> list[tuple]:
    """九宫格召回：目标格 + 真实网格邻格（此处用距离网格近似演示原理）。"""
    target = geohash(lat, lng, precision)
    # 演示用：把候选按"hash 前缀相同"或"距离在格子尺度内"取并集
    grid_span_km = 4900.0 / (32 ** (precision - 1))     # 每位精度缩小 32 倍的格子尺度
    cand = [p for p in all_points
            if geohash(p[0], p[1], precision) == target
            or haversine_km(lat, lng, p[0], p[1]) <= grid_span_km]
    return cand


if __name__ == "__main__":
    # 两个距离极近但 geohash 首位不同的边界点
    center = (39.9042, 116.4074)                    # 目标点
    border_pt = (39.9042 + 0.0001, 116.4074 + 0.0001)  # 紧贴边界
    h1 = geohash(*center, precision=5)
    h2 = geohash(border_pt[0], border_pt[1], precision=5)
    d = haversine_km(center[0], center[1], border_pt[0], border_pt[1]) * 1000
    print(f"目标点 hash: {h1} | 边界点 hash: {h2} | 实际距离 {d:.0f} 米")
    print(f"前缀相同? {'是' if h1 == h2 else '否 -> 只查自身前缀会漏召回'}")

    points = [(39.9042, 116.4074), (39.9043, 116.4075), (39.9100, 116.4100),
              (39.9500, 116.4500), (39.8042, 116.3074)]
    only_self = [p for p in points if geohash(p[0], p[1], 4) == geohash(*center, 4)]
    nine = neighbors9(center[0], center[1], 4, points)
    print(f"\n1km 精度(4位) 召回: 只查自身格 {len(only_self)} 个 / 九宫格 {len(nine)} 个")
    ranked = sorted(nine, key=lambda p: haversine_km(center[0], center[1], p[0], p[1]))
    for p in ranked[:3]:
        print(f"  候选 {p} 距离 {haversine_km(center[0], center[1], p[0], p[1]) * 1000:.0f} 米")
    print("\n结论：geohash 把范围查退化成前缀查，但网格边界会切开近邻；")
    print("      必查 9 宫格粗筛 + Haversine 精排，漏召回比多查 8 格严重得多")
```

**追问一**：为什么 Redis 的 GEO 命令底层用 geohash 加 zset，而不是 R-tree？

→ 解析：Redis 的 GEO 实现是把经纬度编码成 52bit 的 geohash 整数放进 zset 的 score——这样**复用 zset 的跳表结构**，`GEOADD` 就是 ZADD，`GEORADIUS` 就是按 score 区间扫（半径约等于 score 区间）+ 逐点回算距离，不需要引入新的空间索引结构。这是"用一维索引承载二维查询"的工程折衷：实现简单、与 Redis 既有数据结构零摩擦，代价是只支持半径查询、排序靠回算。选型判断：纯"附近 N 个"场景 Redis GEO 足够；要"多边形围栏、路径最近"再上 R-tree（PostGIS）。

**追问二**：用户位置每秒更新，geohash 变更导致迁移成员，写放大怎么治？

→ 解析：两道闸。第一是**限频与抖动过滤**：GPS 漂移会让格子边界来回跳动，同一次"停留"内按移动距离（比如 >50 米）或时间窗（比如 10 秒）节流更新，格子变更次数降一个量级。第二是**批量合并**：更新先进内存队列，定时批量 ZADD/ZREM 合并提交（Q6519 的批量写思路），单 key 的写 QPS 打平。极端热格子（商场等人群密集点）用 hash 打散到多个子格子写（Q1235 的热点打散思路），读的时候 9 宫格自然覆盖所有子格。再算一笔账：5 位 hash 的格子尺度下，正常步行/车速的格子变更率约每分钟 1~2 次，池化后完全可承受。
