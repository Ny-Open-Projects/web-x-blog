---
title: [MFW-490] 笔试：手写 Middleware 重写循环检测器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-490：Middleware 重写循环检测器
**需求**：实现 `createRewriteLoopGuard({ maxHops = 5 })`：1) middleware 每次重写调用 `hop(from, to)`：同请求内 hop 链超 maxHops → 拒绝并返回 500（重写循环会把请求打成死循环）；2) 环检测：hop 目标在本次链中已出现过 → 立即断（如 /a→/b→/a）；3) 带 x-mw-hops 头计数（跨函数实例也能看到 hop 数——请求头是唯一可靠载体）；4) 断环时返回建议：输出完整 hop 链供配置排查（rewrites 误配是常见事故）。

```javascript
export function createRewriteLoopGuard({ maxHops = 5 } = {}) {
  return {
    init(req, res) {
      const chain = (req.headers.get('x-mw-hops') || '').split('>').filter(Boolean)
      req.__chain = chain
    },
    hop(req, from, to) {
      const chain = [...req.__chain, from]
      if (chain.includes(to))   // 环：目标已在链中
        return { ok: false, status: 500, chain: [...chain, to], why: 'cycle' }
      if (chain.length >= maxHops)
        return { ok: false, status: 500, chain: [...chain, to], why: 'max-hops' }
      req.__chain = [...chain, to]
      req.headers.set('x-mw-hops', req.__chain.join('>'))
      return { ok: true, hops: req.__chain.length }
    },
  }
}
```

**评分点**：
- hop 计数走请求头（middleware 多实例执行，内存态不可靠——载体选对）
- 环检测先于次数上限（/a→/b→/a 两跳就该断，不必等 5 跳）
- 超限 500 + 完整链输出（断环要可诊断，不能静默白屏）
- init/hop 分离（每请求初始化状态，防跨请求串台）
