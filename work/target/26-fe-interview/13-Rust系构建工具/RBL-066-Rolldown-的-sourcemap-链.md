---
title: [RBL-066] Rolldown 如何处理多级 sourcemap 合并？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-066：Rolldown 如何处理多级 sourcemap 合并？
**答**：
- 管线上的 map 链：ts 源码 → oxc_transformer 转换（生成 map1）→ 插件 transform 修改（map2）→ 打包拼接（生成最终 chunk map）——三级映射必须级联合并成一条指向源文件的链。
- rolldown 做法：oxc_sourcemap 在 Rust 内完成合并，插件返回的 sourcemap 字段会被消费进链；每级 transform 提供 inputMap 时才可精确级联，缺 map 的插件会导致该段映射丢失（跳到插件产物而非源码）。
- 常见坑：rollup 时代插件用 magic-string 手工生成 map，rolldown 兼容此路径；但插件直接拼字符串不返回 map，调试定位会漂移。
- 输出控制：sourcemap: true/inline/hidden 语义同 rollup；库打包推荐 hidden（外部发布 map 可选）。
- 验证方法：断点在 ts 源码行（devtools 里确认映射落点）或用 sourcemap-visualization 工具检查链完整性。
- 追问钩子：rolldown 的 map 合并在 Rust 完成，比 rollup 的 JS remapping 快且不占 Node 内存。

```javascript
// 插件正确返回 sourcemap 的姿势（保证链不断）
import MagicString from 'magic-string';
export const stripType = {
  name: 'strip-type',
  transform(code, id) {
    if (!id.endsWith('.ts')) return null;
    const s = new MagicString(code);
    s.replaceAll('// @ts-nocheck\n', '');
    return { code: s.toString(), map: s.generateMap({ hires: true }) };
  },
};
```
