---
title: [WCN-766] 编译平台多版本产物共存时，如何做 compiler 版本 lock 与兼容？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-766：编译平台多版本产物共存时，如何做 compiler 版本 lock 与兼容？

**答**：
- 结论：每个编译产物头部写入生成它的 compiler 版本戳（如 `/* @compiler 2.3.0 */`）；运行时/加载器读取版本戳，与当前运行时能力比对，不匹配则拒绝加载或走兼容适配层。
- 通过 lockfile 锁定 compiler 版本，团队统一升级；重大语法变更时产物带 feature flag，运行时按能力开启。
- 追问钩子：新旧产物混在一个页面里共享全局运行时怎么办？考察「版本隔离 + shim 兼容层」。

```javascript
const STAMP = /\/\* @compiler ([\d.]+) \*\//;
function checkCompat(code, runtimeVersion) {
  const m = code.match(STAMP);
  if (!m) return { ok: false, reason: '缺少版本戳' };
  const [a, b] = m[1].split('.').map(Number);
  const [ra, rb] = runtimeVersion.split('.').map(Number);
  const ok = a === ra && b <= rb;                  // 主版本一致且次版本不超前
  return { ok, version: m[1], reason: ok ? '' : '版本不兼容' };
}
const code = '/* @compiler 2.3.0 */ export const x = 1;';
console.log(checkCompat(code, '2.4.0'));
```
