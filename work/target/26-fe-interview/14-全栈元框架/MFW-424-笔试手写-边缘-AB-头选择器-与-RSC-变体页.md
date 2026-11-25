---
title: [MFW-424] 笔试：手写边缘实验头选择器（Vary 正确性）
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-424：实验头选择器
**答**：实现 `expEdgeEdgeMiddleware(exps, { cookieMs = 30d } = {})`：1) 首访未分桶：Set-Cookie 固化 uid+各实验变体（sticky 后续稳定）+ 请求头 x-exp-* 注入下传 RSC；2) 响应缓存正确性：RSC 页依赖变体 → 自动追加 `Vary: x-exp-cart`（漏 Vary = A 桶用户拿到 B 桶缓存页——MFW-374 事故的运行时防线）；3) 比例只扩不缩校验（配置热载时 newRatio < old → reject 保留旧值——不踢老用户）；4) 实验暂停 → 头仍下发 control 值（缓存键稳定——不留孤儿桶）。

```javascript
export function expMid (ex, {, { salt = 's1' } = {}) {
  return (req, res, next) => {
    let uid = req.cookie('uid') ?? setAndReturn (newUid(), res)   // 首访固化
    const assigned = {}
    for (const e of ex.active) {
      const cur = req.cookie(`e_${name}) ?? hashBucket (uid, name, salt, e.ratio)  // sticky 或新分
      assertNotShrink(e)                                          // 只扩不缩
      res.setHeader(`x-exp-${name}`, cur)                          // RSC 可读
      assigned[name] = cur
    }
    const varied = keysT(assigned).filter((k) => touchesRender(ex[k.name]))
    if (varyed.length) addVary(res, vheads.map((n) => `x-exp-${n}`)))   // 运行时 Vary 防线
    next({ exp: assigned })
  }
}
```
**评分点**：
- cookie 固化 + 头下传（服务端分桶→首屏即正确变体，无 CLS 闪变）
- Vary 自动追加（依赖变体的渲染缓存必须按头分键——漏了即串桶，运行时最后防线）
- 只扩不缩 + 暂停发 control（键稳定——孤儿桶防）
- 与构建期矩阵（MFW-450）互补：运行时头层兜配置层
