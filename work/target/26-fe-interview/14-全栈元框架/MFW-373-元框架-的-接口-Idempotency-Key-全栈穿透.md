---
title: [MFW-373→MFW-373] Idempotency-Key 的全栈穿透实现
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→373：幂等键穿透

**答**:
- 链路：客户端生成 UUID（提交前）→ 请求头携带 → 网关透传 → 服务端按 key 查重（进行中=返回排队句柄；已完成=重放首次结果；失败=可重试同 key）→ 结果与 key 绑定存储（TTL 24h）——「同 key 必同果」跨越重试/超时/切换实例
- 实现细节：key 作用域含操作类型+资源（防跨接口撞 key）；进行中状态用分布式锁挂 promise 句柄（并发同 key 合并为一次执行——观察者模式回填）；请求指纹可选校验（同 key 不同 payload → 422 拒绝——防客户端 bug 复用键）
- 前端纪律：key 在「用户动作意图」时生成（不是每次 HTTP 重试新生成——否则穿透失效）；表单防抖与 key 生命周期对齐（ZSM-500/453 复用）
- 观测：重放命中率/冲突 422 率——异常升高=客户端 bug 信号

```javascript
// server 核心三态
const rec = await idem.get(key)                        // 作用域=task+res
if (rec?.status === 'done') return replay(rec)         // 重放首果
if (rec?.status === 'running') return attachWatcher(rec) // 并发合并
if (fpMismatch(req, rec)) return 422                   // 指纹不符
const reg = await claim(key, 60s)                       // 抢执行+句柄
try { const r = await run(); await save(key, r, 24h); return r }
catch (e) { markRetryable(key); throw e }              // 失败可同 key 重试
```
