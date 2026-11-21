---
title: [MFW-195] 笔试：手写带 sticky cookie 的 A/B 分流器
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-195：笔试：手写带 sticky cookie 的 A/B 分流器
**题目**：实现实验分流中间件：① 按 `experiments: [{ name, ratio }]`（如 0.2 = 20% 进 B 组）分桶；② 用户首次分配写入 cookie，之后**永远命中同一组**（sticky，防止实验期间来回切换污染数据）；③ 分桶对用户 ID 稳定：同一用户在任何实例/重启后仍得到相同分组（不能依赖内存随机数）；④ 全部实验关闭或 ratio 为 0 时直接跳过；⑤ 边界：ratio 校验（0~1）、非法配置不 crash；⑥ 分组结果注入响应头/上下文供业务读取。

```ts
// 稳定哈希：同 userId → 同 bucket，跨实例/重启一致
function hash(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
  return (h >>> 0) / 2 ** 32; // 归一化到 [0,1)
}

type Exp = { name: string; ratio: number; cookieMaxAge?: number };

export function abMiddleware(exps: Exp[]) {
  return (ctx: any, next: () => Promise<void>) => {
    const userId = ctx.cookies.get('uid') ?? ctx.ip;
    for (const exp of exps) {
      if (exp.ratio <= 0 || exp.ratio > 1) continue; // ④⑤ 非法/关闭直接跳过
      const key = `${exp.name}:${userId}`;
      const cookieName = `ab_${exp.name}`;
      // ② 先读 cookie：sticky 优先于重算
      let group = ctx.cookies.get(cookieName);
      if (group !== 'A' && group !== 'B') {
        group = hash(key) < exp.ratio ? 'B' : 'A'; // ③ 确定性分桶
        ctx.cookies.set(cookieName, group, {
          maxAge: exp.cookieMaxAge ?? 30 * 86400, httpOnly: true, sameSite: 'lax',
        });
      }
      ctx.state.experiments = { ...ctx.state.experiments, [exp.name]: group }; // ⑥
      ctx.set(`x-exp-${exp.name}`, group);
    }
    return next();
  };
}
```

**评分点**：
1. 稳定哈希分桶（FNV 等确定性哈希）而非 `Math.random()`——随机数每次重算会改变分组，直接破坏实验数据。
2. cookie sticky 优先：重算结果与 cookie 冲突时以 cookie 为准，实验中途改 ratio 只影响新用户。
3. 边界处理：ratio 越界跳过、无 uid 回退到 ip（能指出 ip 回退不稳定、最好强制登录态，加分）。
4. 分组注入上下文/响应头，业务与数据分析都能拿到结果。
5. 能说出采样偏差：hash 分桶在流量小时两桶人数可能不均，重要实验要校验分桶均匀性。
