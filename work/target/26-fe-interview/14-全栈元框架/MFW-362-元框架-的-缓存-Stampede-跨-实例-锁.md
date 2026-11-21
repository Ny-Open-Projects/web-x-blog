---
title: [MFW-362] 跨实例缓存重建锁（fencing token 版）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→362：跨实例重建锁

**答**:
- 升级版需求：热点 key 失效瞬间 N 个实例同时重建（DB 被 ×N 打）——MFW-266 单实例单飞不够，需跨实例仲裁
- fencing token 方案：Redis SET NX 抢锁获得单调递增 fence 号 → 重建者携带 fence 写入（写时校验自己的 fence 仍是最新——持锁过期的旧写入被拒）——防「锁过期后旧实例延迟写覆盖新值」的经典锁缺陷
- 等待者策略：抢锁失败者不空转——订阅完成通知（Pub/Sub key）或短退避读旧值（旧值可用性优先）+ 最长等待上限（超限自己重建——锁持有者崩溃自愈）
- 正确性边界：fencing 需要存储层支持条件写（Redis WATCH 或版本 CAS）——不支持时退化为「最后写胜 + 版本时间戳丢弃旧写」

```javascript
const { token: fence } = await acquireBuildLock(key, 10_000)      // NX + 单调号
const fresh = await rebuildSlowly(key)
await casWrite(key, fresh, { expectFence: fence })                // 旧 fence 写入被拒
// 等待者：sub(`done:${key}`) 或 300ms 退避读旧值；等待 >15s 自行重建（自愈）
```
