---
title: [ALG-175] 密码管理器插件要生成强随机密码。为什么不能用 `Math.random()`？如何实现无模偏差的安全生成？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-175：密码管理器插件要生成强随机密码。为什么不能用 `Math.random()`？如何实现无模偏差的安全生成？
**答**：`Math.random()` 是伪随机（xorshift128+），状态可被观测反推，安全场景必须用 CSPRNG——`crypto.getRandomValues`。生成还要解决"模偏差"：直接 `% 62` 时 256 不是 62 的倍数，前 8 个字符概率偏高；拒绝采样法：先算 `limit = floor(256/62)*62`，采样到 `>= limit` 就重抽，保证等概率。最后保证每类字符至少一个并 Fisher-Yates 打乱位置。

```javascript
function generatePassword(length = 16, { symbols = true } = {}) {
  const pools = ['abcdefghijkmnpqrstuvwxyz', 'ABCDEFGHJKLMNPQRSTUVWXYZ', '23456789'];
  if (symbols) pools.push('!@#$%^&*_-+=');
  const all = pools.join('');
  const rand = max => {                 // 拒绝采样：消除模偏差
    const limit = Math.floor(256 / max) * max;
    const buf = new Uint8Array(1);
    do { crypto.getRandomValues(buf); } while (buf[0] >= limit);
    return buf[0] % max;                // 每个值严格等概率
  };
  const pwd = pools.map(p => p[rand(p.length)]); // 每类至少一个
  while (pwd.length < length) pwd.push(all[rand(all.length)]);
  for (let i = pwd.length - 1; i > 0; i--) {     // Fisher-Yates 打乱位置
    const j = rand(i + 1);
    [pwd[i], pwd[j]] = [pwd[j], pwd[i]];
  }
  return pwd.join('');
}
// Math.random 的输出序列可被反推，密码生成严禁使用
```
