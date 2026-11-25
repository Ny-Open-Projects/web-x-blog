---
title: "[Q6094] 响应 gzip 压缩的成本与 CDN 卸载取舍"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6094 · 响应 gzip 压缩的成本与 CDN 卸载取舍

难度：P6 | 标签：成本工程 | gzip | 中间件

**问**：一个 JSON-heavy 的 API，P95 从 80ms 涨到 160ms，时间线上看是"加了 GZipMiddleware"。应用层响应压缩的成本账怎么算？压缩率、CPU、与 CDN/网关侧压缩的关系如何取舍？

**答**：
结论：应用层压缩的成本 = 每响应一次 gzip 压缩的 CPU（对 ~100KB JSON 是毫秒级，压垮 P95 完全可能）+ 双缓冲内存 + 压缩等级与响应大小的线性时间。收益 = 传输体积缩到 1/5-1/10，只在"带宽贵或客户端弱网"时值回 CPU。取舍矩阵：① 网关/CDN 压缩（Nginx gzip、CloudFront）把 CPU 从应用进程卸载到边缘，且可缓存压缩结果——应用侧通常应该关掉自己的压缩、只保证 `Vary: Accept-Encoding` 正确；② 应用压缩仅在无边缘层、内网大包、或响应不可被边缘缓存（带鉴权的动态响应）时考虑；③ level 选 1-4，绝不默认 9；④ 阈值化：小于 ~1KB 不压（压缩率差还加头部成本），大于 ~1MB 交给流式/分段。
实战：上压缩前后必须测三件事：P95 延迟、CPU 利用率、传输字节；`GZipMiddleware(minimum_size=1024)` 只对同进程动态响应兜底，静态大文件走 CDN。另外压缩与 SSE/流式响应冲突（缓冲破坏推送语义），要显式排除。

```python
import gzip, json, time

payload = json.dumps({
    "items": [{"id": i, "name": f"item-{i}", "tags": ["a", "b", "c"],
               "desc": "x" * 60} for i in range(1200)]
}).encode()
print(f"原始 {len(payload)/1024:.0f} KB")

print("level | 压缩后 KB | 压缩耗时 ms | 每响应 CPU 占比(@80ms预算)")
for lv in (1, 4, 6, 9):
    t0 = time.perf_counter()
    blob = gzip.compress(payload, lv)
    dt = (time.perf_counter() - t0) * 1000
    print(f"{lv:5d} | {len(blob)/1024:9.0f} | {dt:11.2f} | {dt/80*100:5.0f}%")

# 决策模型：何时应用层压缩划算
def decide(level, latency_budget_ms=80, edge_available=True,
           cacheable_by_edge=True, size_kb=len(payload)//1024):
    t0 = time.perf_counter(); gzip.compress(payload, level); ms = (time.perf_counter()-t0)*1000
    if edge_available and cacheable_by_edge:
        return "交给 CDN/网关压缩：应用只设置 Vary: Accept-Encoding"
    if ms > latency_budget_ms * 0.2:
        return f"应用压缩吃掉 {ms/latency_budget_ms*100:.0f}% 延迟预算 → 降 level 或不压"
    if size_kb < 1:
        return "小于 1KB：压缩率差且加头部成本 → 不压"
    return f"应用压缩可接受（{ms:.1f}ms，{size_kb}KB→{len(gzip.compress(payload, level))//1024}KB）"

print(decide(6))                       # 有 CDN → 卸载
print(decide(6, edge_available=False)) # 无边缘层 → 权衡
print(decide(9, edge_available=False)) # level 9 贵

# 流式/SSE 冲突：压缩需要缓冲完整块，破坏推送时序
def sse_note():
    return ("SSE/流式响应禁用 gzip 中间件：缓冲会攒帧，"
            "客户端看到的推送间隔变成压缩块间隔")
print(sse_note())

# 实测压缩率对数据形态的敏感性
repetitive = (json.dumps({"k": "v" * 40}) * 300).encode()
randomish = bytes((i * 7 % 256) for i in range(100_000))
print(f"重复 JSON 压缩率 {len(gzip.compress(repetitive))/len(repetitive):.2f}, "
      f"近随机数据 {len(gzip.compress(randomish))/len(randomish):.2f}")
```

**追问 1**：为什么压缩与 SSE/WebSocket 不兼容？
- 追问 2 层：gzip 需要积累足够数据产出压缩块，中间件缓冲把逐帧推送变成块间隔；WS 更是二进制帧协议，HTTP 压缩中间件根本不该碰。
- 追问 3 层：确实要压缩 SSE 时只能应用内逐事件 gzip 并以 `flush` 收尾，代价是压缩率崩掉——通常直接不做。

**追问 2**：`Vary: Accept-Encoding` 为什么要由应用保证？
- 追问 2 层：边缘层按该头区分缓存条目；应用自己压过（Content-Encoding: gzip）而边缘又缓存未压缩版本会出现双重压缩/错配。
- 追问 3 层：若应用压缩了而 CDN 又压缩，两层头冲突会直接让客户端解码失败——所以"谁压缩"必须全局唯一决策。

## 背诵要点
1. 应用层 gzip 每响应毫秒级 CPU，P95 直接翻倍；默认决策是卸载给 CDN/网关，应用只管 Vary 头。
2. 不得不压时 level 1-4 + minimum_size≈1KB 阈值 + 排除流式/SSE；level 9 是 CPU 税。
3. "谁压缩"全局唯一：双层压缩会导致 Content-Encoding 错配与解码失败。

## 复盘追问
1. 为什么加了中间件 CPU 没见涨但延迟翻倍？——压缩耗时在单请求关键路径上同步执行，CPU 总量涨但被多 worker 摊薄，单请求延迟先爆。
2. 弱网客户端占比高的场景怎么权衡？——用带宽成本×节省字节对比 CPU 成本×QPS，真实数据算账而非拍板。
