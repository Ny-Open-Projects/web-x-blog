---
title: [RBL-733] 笔试：手写 WASM 插件 ABI 版本协商器（兼容范围 + 升级建议）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-733：笔试：手写 WASM 插件 ABI 版本协商器（兼容范围 + 升级建议）

**答**：实现 `checkAbi(core, plugin, available)`。core: 核心 ABI `{ major, minor, patch }`；plugin: `{ major, minor }`。规则：1) major 不等 → 拒绝 `{ ok: false, reason: 'major-mismatch' }`，建议文案从 available（同 major 的可用版本列表）选「≥plugin.minor 的最新」；2) plugin.minor > core.minor → 拒绝 `{ reason: 'plugin-newer' }`（插件用了更新的 ABI）建议升级核心；3) plugin.minor ≤ core.minor → 通过 `{ ok: true }`。available 为空时建议只给「升级插件」。边界：available 中无同 major 版本建议文案降级。

```javascript
function checkAbi(core, plugin, available = []) {
  if (plugin.major !== core.major) {
    const candidates = available.filter(v => v.major === plugin.major && v.minor >= plugin.minor);
    const suggestion = candidates.length
      ? `请使用核心 ${plugin.major}.${candidates[0].minor}.x（或更高）`
      : `无兼容核心版本，请等待核心 ${plugin.major}.x 支持或降级插件`;
    return { ok: false, reason: 'major-mismatch', suggestion };
  }
  if (plugin.minor > core.minor)
    return { ok: false, reason: 'plugin-newer',
      suggestion: `插件要求 ABI ≥${plugin.major}.${plugin.minor}，请升级核心至 ${plugin.major}.${plugin.minor}.x` };
  return { ok: true };
}

// 自测
const core = { major: 1, minor: 4, patch: 0 };
let r = checkAbi(core, { major: 1, minor: 3 });
console.log(r.ok === true);

r = checkAbi(core, { major: 1, minor: 5 });              // 插件更新
console.log(r.reason === 'plugin-newer' && r.suggestion.includes('1.5'));

r = checkAbi(core, { major: 2, minor: 0 },
  [{ major: 2, minor: 1 }, { major: 2, minor: 3 }, { major: 1, minor: 9 }]);
console.log(r.reason === 'major-mismatch');
console.log(r.suggestion.includes('2.1'));               // 选 ≥0 的最新同 major

r = checkAbi(core, { major: 2, minor: 0 }, []);          // 无可用
console.log(r.suggestion.includes('无兼容'));

r = checkAbi(core, { major: 2, minor: 0 }, [{ major: 1, minor: 9 }]);
console.log(r.suggestion.includes('无兼容'));
```

**评分点**：
- 三分支判定正确：major 不等 / 插件更新 / 通过
- 升级建议逻辑完整：available 里同 major 且 minor ≥ 插件需求的最新版；空/无匹配降级文案
- minor 向后兼容语义正确（核心 minor ≥ 插件 minor 即可）
- 能说清「major 相等是 ABI 硬约束、minor 是兼容窗口」的版本语义属于加分
