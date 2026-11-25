---
title: [MFW-406] 笔试：手写 PPR 壳洞划分校验器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-406：壳洞校验器
**答**：实现 `validatePprSplit(pageAst)`（输入：构建器给出的段清单 `[{ id, usesRequestFx: bool, sizeEst, aboveFold} ]`）：1) 壳内禁止请求级 API——任一非 Suspense 段 usesRequestFx=true → 整页退化 SSR（报错并指认段）；2) 洞预算：aboveFold 动态段 ≤2（首屏等待面收敛）；3) 骨架尺寸声明齐全（每个洞有 fallback 尺寸≈内容——CLS 防护）；4) 输出 { ok, degradedTo?: 'ssr', violations: [{code, seg}] }，错误码：SHELL_LEAK / TOO_MANY_ABOVE_FOLD / NO_FALLBACK_SIZE。

```javascript
// segments: [{ id, inShell, inSusp, readsRequest, aboveFold, fallbackBytes? }]
export function validatePpr(segments) {
  const errs = []
  let degraded = false
  for (const s of segments) {
    if (s.inShell && !s.inSusp && s.readsRequest) {           // 壳内直接请求 → 整页退化 SSR
      errs.push({ code: 'SHELL_LEAK', seg: s.id })
      degraded = true
    }
    if (!s.inShell && s.aboveFold && s.fallbackBytes == null)
      errs.push({ code: 'NO_FALLBACK_SIZE', seg: s.id })      // 骨架尺寸缺失 = CLS 源
  }
  const aboveDyn = segments.filter((x) => !x.inShell && x.aboveFold).length
  if (aboveDyn > 2) errs.push({ code: 'TOO_MANY_ABOVE_FOLD', seg: aboveDyn })
  return { ok: errs.length === 0, degradedTo: degraded ? 'ssr' : undefined, violations: errs }
}
```
**评分点**：
- 壳泄漏即整页退化的判定（一个 cookies() 毁掉全静态收益——最贵错误最先报）
- 首屏洞数预算（用户等待面收敛——无限洞=伪 PPR）
- 骨架尺寸声明（流式 CLS 的构建期预防）
- 错误码结构化（修复建议可挂接文档）
