---
title: [V3-424] 笔试：手写 v-memo 效果的自定义指令（依赖变化才更新）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-424：笔试：手写 v-memo 效果的自定义指令（依赖变化才更新）
**题**：实现指令 `v-freeze="[dep1, dep2]"`：值未变化时阻止元素内容更新（利用自定义指令在组件更新阶段做对比），变化时更新并记录新快照；快照比较用浅比较数组序列化；卸载时清理。

```javascript
export const vFreeze = {
  beforeMount(el, binding) {
    el.__freezeKey = JSON.stringify(binding.value)
  },
  updated(el, binding) {
    const key = JSON.stringify(binding.value)
    if (key === el.__freezeKey) {
      // 冻结：恢复旧 DOM？实际 v-memo 是编译期跳过 patch，
      // 指令层面近似实现：把当前 DOM 克隆缓存，更新后替换回旧版
      const saved = el.__freezeSnapshot
      if (saved) el.replaceWith(saved.cloneNode(true))
    } else {
      el.__freezeKey = key
      el.__freezeSnapshot = el.cloneNode(true) // 更新后记录新快照
    }
  },
  mounted(el) { el.__freezeSnapshot = el.cloneNode(true) },
  unmounted(el) { delete el.__freezeSnapshot }
}
// 说明：真正 v-memo 在编译层（withMemo 跳过整个 subtree patch），指令版是运行时近似
```
**评分点**：
- 快照机制 + 依赖序列化比较。
- 能说清指令版与编译期 v-memo 的本质区别（编译期直接跳 patch，无 DOM 替换成本）。
- mounted/updated 生命周期配对。
- 能指出 JSON.stringify 比较的局限（大对象开销）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-ff15686e-55dd-460d-af67-5eb13c3990a5-cwd'; fi
exit "$__zcode_status"
