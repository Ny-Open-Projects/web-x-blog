---
title: [MFW-365→MFW-365] Strict Mode 双调用在服务端数据函数的语义
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→365：Strict 双调用服务端语义

**答**:
- 现象：dev 下组件函数/lifecycle 双调用（暴露非幂等假设）——SSR 数据函数同样会被框架去重/重试机制多次进入，dev 双调是最早的预警器
- 判读规则：双调用结果不同 = 藏着非幂等（时间戳/随机/自增副作用）→ 生产重试场景必炸——dev 报警是礼物不是噪音
- 服务端配套：数据函数内聚合去重（cache()/per-request Map——MFW-263/219）让「多次进入」收敛为「多次读取同一 Promise」——幂等由结构保证而非自觉
- 测试增强：单测里显式双调用断言（deep-equal 两次结果——非幂等函数在 CI 就红，不等线上）

```javascript
// 结构性幂等：同请求收敛为同一 Promise
export const getCart = cache(async (id) => db.cart.read(id))    // cache() 同参同 Promise
// CI 断言：const [a, b] = await Promise.all([fn(), fn()]); expect(a).toEqual(b)
```
