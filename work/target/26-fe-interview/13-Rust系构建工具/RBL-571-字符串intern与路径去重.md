---
title: [RBL-571] 构建器里的字符串 Intern：为什么路径与包名要全局去重
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-571：构建器里的字符串 Intern：为什么路径与包名要全局去重

**答**：
- 大型构建中同一字符串被海量重复持有：`node_modules/lodash/lodash.js` 这类路径会在模块元数据、依赖边、sourcemap sources、诊断信息里出现成百上千次——每份都是独立拷贝时内存翻倍。Intern（驻留）= 全局哈希表里只存一份，其余持有等价的轻量句柄（索引/id）。
- 收益 1：内存 O(种类数) 而非 O(引用数)；收益 2：**比较变 O(1)**——模块 id 相等性判断从逐字节 strcmp 变成整数比较，模块图去重/依赖匹配的热路径大幅提速；收益 3：哈希只需算一次，后续用 id 当 key。
- 实现要点：DashMap<String, u32> 或 per-thread 池 + 全局合并；id 反查表（Vec<String>）用于输出；生命周期上 intern 表全局驻存（泄漏可控——种类数有限），这也意味着「临时字符串」不要 intern（如用户传来的任意路径片段只 intern 规范化后的）。
- 构建器具体落点：ModuleId 用 intern 后的 u32；source 字段在 sourcemap 输出时才物化字符串；Atom 类型（SWC）本质就是 intern 的字符串句柄。
- 追问钩子：与 JS 引擎的 string table（V8 internalized string）同构——V8 里属性名比较快正是因为 intern；构建器做 intern 等于把引擎的优化手工搬到应用层。

```javascript
// JS 概念实现：全局 intern 表
class StringPool {
  #map = new Map(); #vec = [];
  intern(s) {
    let id = this.#map.get(s);
    if (id === undefined) { id = this.#vec.length; this.#map.set(s, id); this.#vec.push(s); }
    return id;                       // 相同字符串 -> 相同 u32
  }
  get(id) { return this.#vec[id]; }
}
const pool = new StringPool();
const m1 = pool.intern('/src/a/index.js'), m2 = pool.intern('/src/a/index.js');
console.log(m1 === m2);              // true：比较 O(1)

// 应用：依赖边存储从字符串对变成 id 对
// edges: Array<[u32, u32]>            // 8 字节/边 vs 两个字符串对象 ~100+ 字节
// 反查：
console.log(pool.get(m1));           // '/src/a/index.js'
```
