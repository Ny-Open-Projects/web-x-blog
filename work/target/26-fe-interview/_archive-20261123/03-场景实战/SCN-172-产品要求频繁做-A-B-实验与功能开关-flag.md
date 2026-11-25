---
title: [SCN-172] 产品要求频繁做 A/B 实验与功能开关，flag 如何全链路管理（创建、生效、清理）？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-172：产品要求频繁做 A/B 实验与功能开关，flag 如何全链路管理（创建、生效、清理）？
**答**：
- flag 有生命周期就必然要管"归还"：创建必须登记 owner、过期时间、影响面；到期的 flag 进CI 扫描清单，未清理就报警——遗忘的 flag 分支组合爆炸是事故源。
- 生效链路统一：服务端下发 flag 快照（登录时 + 关键操作时刷新），前端只消费快照，不做本地逻辑判断（用户分桶、百分比全在服务端），保证同用户全端一致。
- 前端接入用统一 SDK：`flag('new-checkout')`，未注册的 flag 读取时在 dev 环境报错，防手滑拼错。
- 清理自动化：CI 定期扫描代码中引用的 flag 与平台登记比对，"平台已删除但代码还在读"与"平台存活但代码无引用"都报。

```javascript
// feature flag SDK：快照消费 + 未注册校验 + 曝光埋点
export function createFlagClient(snapshot, { env }) {
  const registry = snapshot.flags;                     // { 'new-checkout': { value, variant, meta } }
  const exposed = new Set();
  return {
    get(key, defaultValue = false) {
      const f = registry[key];
      if (!f && env !== 'prod') console.error(`[flag] 未注册的 flag: ${key}`); // 拼错尽早暴露
      if (f && !exposed.has(key)) {                    // 曝光埋点：实验分析的数据基础
        exposed.add(key);
        report({ type: 'flag-exposed', key, variant: f.variant, bucket: snapshot.bucket });
      }
      return f?.value ?? defaultValue;
    },
    variant: key => registry[key]?.variant ?? 'control',
  };
}

// CI 清理扫描：代码引用 vs 平台登记 双向比对
// node scripts/flag-audit.js
export async function flagAudit() {
  const [used, registered] = await Promise.all([
    scanCodeUsage('src/**/*.{js,ts,tsx}', /flags?\.(get|variant)\(\s*['"]([\w.-]+)['"]/g),
    api.listFlags({ status: 'active' }),
  ]);
  const orphans = registered.filter(f => !used.has(f.key));   // 平台存活但代码不用：该清理
  const missing = [...used].filter(k => !registered.find(f => f.key === k)); // 代码在用但未登记
  const expired = registered.filter(f => f.expireAt < Date.now());           // 过期未清理
  if (orphans.length || missing.length || expired.length) {
    console.table([...orphans, ...missing, ...expired]);
    process.exit(1);                                   // 卡合入：新代码不允许引用未登记 flag
  }
}
```
