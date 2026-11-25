---
title: [WCN-767] 笔试：手写编译产物版本戳与运行时校验器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-767：笔试：手写编译产物版本戳与运行时校验器

**答**：
- 需求：实现 `stamp(code, version)` 在代码首部插入 `/* @compiler X */` 注释；`verify(code, runtimeVersion)` 解析版本戳并用 semver 简化比较（主版本相同、次版本产物<=运行时即兼容），返回 `{ ok, version, reason }`。要求重复 stamp 时替换旧戳而非叠加；边界：无戳、格式非法。
- 要点：正则匹配并替换首部旧戳；semver 取 major/minor 比较；非法格式返回 ok:false。

```javascript
const RE = /^\/\* @compiler ([\d.]+) \*\/\n?/;
function stamp(code, version) {
  return `/* @compiler ${version} */\n` + code.replace(RE, ''); // 去旧戳再加新戳
}
function verify(code, runtimeVersion) {
  const m = code.match(RE);
  if (!m) return { ok: false, reason: '缺少版本戳' };
  const pv = m[1].split('.').map(Number);
  const rv = runtimeVersion.split('.').map(Number);
  if (pv.length < 2 || rv.length < 2 || pv.some(isNaN) || rv.some(isNaN))
    return { ok: false, version: m[1], reason: '版本格式非法' };
  const ok = pv[0] === rv[0] && pv[1] <= rv[1];
  return { ok, version: m[1], reason: ok ? '' : '版本不兼容' };
}
let code = stamp('const a=1;', '2.3.0');
code = stamp(code, '2.4.0');                      // 替换，不叠加
console.log(code, verify(code, '2.4.0'));
```

**评分点**：
- stamp 重复调用替换旧戳（正则去旧），不叠加污染。
- verify 正确解析并做 major/minor 兼容比较。
- 无戳与非法格式返回明确失败原因。
- 返回结构化结果，便于运行时决策。
