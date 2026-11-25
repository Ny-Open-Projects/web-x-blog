---
title: [TST-882] 笔试：手写一个「随机故障注入器」（fetch 随机失败/延迟/脏数据）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-882：笔试：手写一个「随机故障注入器」（fetch 随机失败/延迟/脏数据）
**答**：
- 需求：实现 injectChaos(fetchFn, config) —— 按概率对请求注入「失败」「延迟」「脏数据」三类故障，返回包装后的 fetch。
- 规则：故障按 weights 权重随机选择；fail 抛网络错误、delay 增加随机延迟、corrupt 返回被污染的数据。
- 边界：注入率/权重非法抛错；可通过 enabled 开关动态启停；保留原 fetch 语义。

```javascript
function injectChaos(fetchFn, {
  enabled = true, rate = 0.3, weights = { fail: 0.4, delay: 0.4, corrupt: 0.2 },
  maxDelayMs = 2000,
} = {}) {
  if (rate < 0 || rate > 1) throw new RangeError('非法注入率');
  const kinds = Object.keys(weights);
  const pick = () => {
    const r = Math.random();
    let acc = 0;
    for (const k of kinds) { acc += weights[k]; if (r <= acc) return k; }
    return kinds[kinds.length - 1];
  };
  return async (...args) => {
    if (enabled && Math.random() < rate) {
      const kind = pick();
      if (kind === 'fail') throw new Error('Chaos: 网络中断');
      if (kind === 'delay') await new Promise(r => setTimeout(r, Math.random() * maxDelayMs));
      if (kind === 'corrupt') {
        const res = await fetchFn(...args);
        return { ...res, corrupted: true, data: '<script>bad</script>' };
      }
    }
    return fetchFn(...args);
  };
}
const chaoticFetch = injectChaos(fetch, { rate: 0.5 });
```
**评分点**：
- 按权重随机选择故障类型，三类故障（失败/延迟/脏数据）实现完整。
- 注入率/权重校验，enabled 开关可动态启停，边界健壮。
- 保留原 fetch 语义（透传入参与返回值）。
- 能点出「故障注入用于验证前端降级与容错，而非破坏生产」这一安全前提。
