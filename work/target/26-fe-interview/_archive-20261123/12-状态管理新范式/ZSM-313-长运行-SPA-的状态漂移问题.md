---
title: [ZSM-313] 页面开一整天后状态漂移（陈旧/膨胀）怎么治理
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-313：页面开一整天后状态漂移（陈旧/膨胀）怎么治理

**答**:
- 漂移三类：数据陈旧（早上拉的配置下午用）、内存膨胀（无限滚动的 query 缓存/动态 atom 累积）、会话语义漂移（权限/租户已变而前端未感知）
- 治理：gcTime/maxPages 限内存；关键低频数据定时重校验（refetchInterval 或版本号轮询）；会话类状态挂心跳（WS/轮询）失效即广播收敛
- 显式「会话重置点」：跨天/长时间 idle 检测（visibilitychange + 时间阈值）后全量 invalidate 或提示刷新——长开 SPA 必须有这个逃生舱
- 监控：store 大小/条目数周期采样上报，膨胀有曲线可看才能治理

```javascript
let lastActive = Date.now()
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && Date.now() - lastActive > 8 * 3600_000) {
    queryClient.invalidateQueries()      // 长时间后台回来：全量重校验
    refreshSession()                     // 会话语义重校验
  }
  lastActive = Date.now()
})
```
