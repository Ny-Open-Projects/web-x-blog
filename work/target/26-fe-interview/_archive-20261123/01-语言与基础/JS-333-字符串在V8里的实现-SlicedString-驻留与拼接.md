---
title: [JS-333] 字符串在 V8 里的实现：驻留、切片与拼接
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, V8]
type: 面试题
---

## JS-333：字符串在 V8 里的实现：驻留、切片与拼接

**答**：
- 字符串驻留（internalization）：短字符串/属性名被内部化（同一实例）——对象属性查找依赖内部化字符串的比较，`===` 对内部化字符串是 O(1)
- Sliced String：substring 返回切片视图（引用原串 + 偏移），不复制内存——大日志文件做大量 substring 时内存不释放（原串被切片引用着），需要时 join('') 或 TextDecoder 显式扁平化
- Cons String：字符串拼接生成 cons 树（左右子串引用），延迟扁平化——大量 += 拼接先攒树再一次性 flatten，比想象中高效；但超长树深度会触发过早扁平化
- 外部字符串：C++ 扩展/Node native 可以提供外部字符串资源（不进堆）
- 实战含义：处理大文本（日志/源码）用 TypedArray + 解码器流式处理，避免「切片引用拖住原串」的隐性内存驻留

```javascript
const log = hugeText;                       // 100MB
const firstLine = log.substring(0, 100);    // Sliced String: 引用整个 100MB 原串
// 场景: 只保留 firstLine → 原 100MB 无法回收!
const flat = log.substring(0, 100).split('').join('');  // 扁平化, 断开引用
// 或: const flat = new TextDecoder().decode(new TextEncoder().encode(...))
```
