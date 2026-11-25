---
title: [BLD-301] 笔试题——实现构建锁与原子 emit？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-301：手写构建锁与原子 emit

**需求与边界**：
- 需求：防并发构建——① 目录锁（锁文件 + 持有者信息 + 过期检测——崩溃残留锁自动释放）；② 原子 emit（临时目录构建完 rename 替换——SCN-BLD-286 正确性）；③ emit 失败清理临时目录（现场恢复）。
- 边界：① 锁的过期时间（构建最大时长——超时锁自动失效防死锁）；② rename 跨设备失败回退（copy + 校验）；③ 强制解锁通道（--force 带审计）。

**答**：
```javascript
import fs from 'fs', path from 'path';
async function withBuildLock(dir, fn, { maxAge = 30 * 60_000 } = {}) {
  const lockFile = path.join(dir, '.build-lock');
  if (fs.existsSync(lockFile)) {
    const lock = JSON.parse(fs.readFileSync(lockFile));
    if (Date.now() - lock.ts < maxAge)                 // 未过期：真并发
      throw new Error(`构建被 ${lock.holder} 持有（${new Date(lock.ts)}）——确认后用 --force 解锁`);
    warn(`过期锁自动释放（持有者 ${lock.holder}，疑似崩溃残留）`);   // 崩溃残留
  }
  fs.writeFileSync(lockFile, JSON.stringify({ holder: process.pid + ':' + user(), ts: Date.now() }));
  try { return await fn(); }
  finally { fs.rmSync(lockFile); }
}
async function atomicEmit(dir, emitFn) {
  const tmp = dir + '.tmp-' + Date.now();
  try {
    await emitFn(tmp);                                 // 先写临时目录
    fs.renameSync(tmp, dir);                           // 原子替换（SCN-BLD-286）
  } catch (e) {
    fs.rmSync(tmp, { recursive: true, force: true });  // 失败清现场
    throw e;
  }
}
```

**评分点**:
- 锁三态（持有中拒绝/过期自动释放/强制解锁）。
- 持有者信息（谁在构建——排障可定位）。
- 原子 emit（临时目录 + rename——SCN-BLD-286 正确性保证）。
- 失败现场清理（tmp 不残留）。
