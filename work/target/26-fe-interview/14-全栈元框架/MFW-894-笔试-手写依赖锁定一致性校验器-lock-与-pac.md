---
title: [MFW-894] 笔试：手写依赖锁定一致性校验器（lock 与 package.json 对账）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-894：笔试：手写依赖锁定一致性校验器（lock 与 package.json 对账）

**答**：
- 结论：校验 package.json 声明的依赖范围与 lock 文件实际锁定的版本是否一致；不一致（lock 未更新）就拒绝构建，避免「声称兼容实际漂移」。
- 关键：比对直接依赖的 semver 范围是否包含 lock 中的解析版本；检测 lock 中缺失/多余的顶层依赖。
- 追问钩子：为什么 semver 范围满足还不够？——lock 必须精确对应一次可复现的安装，范围满足但 lock 过期仍是非确定性来源。

```javascript
function satisfies(version, range) {                  // 简化：^1.2.0
  const m = /\^(\d+)\.(\d+)/.exec(range);
  if (!m) return version === range;
  const [maj, min] = version.split('.').map(Number);
  return maj === +m[1] && min >= +m[2];
}
function checkLock(pkg, lock) {
  const errors = [];
  for (const [name, range] of Object.entries(pkg.dependencies || {})) {
    const locked = lock.packages?.['node_modules/' + name]?.version;
    if (!locked) { errors.push(name + ': lock 中缺失'); continue; }
    if (!satisfies(locked, range)) errors.push(name + ': ' + locked + ' 不满足 ' + range);
  }
  return { ok: errors.length === 0, errors };
}
// 自测
const pkg = { dependencies: { react: '^18.0.0' } };
const lock = { packages: { 'node_modules/react': { version: '18.2.0' } } };
console.log(checkLock(pkg, lock).ok);                 // true
```

**评分点**：
- 比对 package.json 范围与 lock 解析版本（semver 满足性）
- 检测 lock 中缺失/多余的顶层依赖
- 不一致即拒绝构建（frozen 语义），保障可复现
- 边界：无 lock、嵌套依赖、peer 依赖处理（加分）
