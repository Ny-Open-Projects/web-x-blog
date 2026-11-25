---
title: [WCN-855] 编译产物的「确定性构建」（reproducible build）如何保障？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-855：编译产物的「确定性构建」（reproducible build）如何保障？

**答**：
- 结论先行：确定性构建指「相同源码 + 相同环境 → 字节级完全相同的产物」——这是供应链安全与可复现发布的基础，要在编译流程里消除一切非确定性来源。
- 非确定性来源：时间戳、随机数、绝对路径、文件系统遍历顺序、并发编译顺序、依赖版本漂移、locale/时区。
- 对策：固定时间戳（或用 `SOURCE_DATE_EPOCH`）、禁用随机、产物中路径改用相对路径、按字典序稳定排序文件与 chunk id、锁定依赖版本（lockfile）、固定 Node/编译器版本、设固定 locale/时区。
- 验证：同一提交在两台机器构建，对产物做哈希比对（如 sha256）；CI 加入「重复构建一致性」检查；用内容哈希命名产物文件名。
- 价值：能证明发布的产物确实来自对应源码（防止供应链投毒）、便于增量缓存（内容哈希可靠）、问题可精确复现。
- 追问钩子：面试官会问「chunk id 怎么稳定」——答：用基于模块路径/内容的确定性 hash 而非自增计数或编译顺序，避免并发顺序影响 id。

```javascript
// 确定性构建：用内容哈希命名 + 稳定排序 + 固定时间戳
import { createHash } from 'crypto';
function deterministicBuild(modules, { epoch = 0 } = {}) {
  const sorted = [...modules].sort((a, b) => a.path.localeCompare(b.path)); // 稳定顺序
  return sorted.map(m => {
    const hash = createHash('sha256').update(m.code).digest('hex').slice(0, 8); // 内容哈希
    return {
      name: `${m.path.replace(/\W/g, '_')}.${hash}.js`,  // 确定性文件名，非自增id
      code: `/* build:${epoch} */\n${m.code}`,            // 固定时间戳
    };
  });
}
const out = deterministicBuild([{ path: 'src/b.js', code: 'export const b=2' }, { path: 'src/a.js', code: 'export const a=1' }]);
console.log(out.map(o => o.name)); // 每次构建顺序、命名完全一致
```
