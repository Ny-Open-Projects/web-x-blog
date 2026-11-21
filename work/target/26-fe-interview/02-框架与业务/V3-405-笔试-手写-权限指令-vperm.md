---
title: [V3-405] 笔试：手写按钮级权限指令 v-perm
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-405：笔试：手写按钮级权限指令 v-perm
**题**：实现 v-perm 指令：用法 `v-perm="'order:delete'"` 或 `v-perm="['a','b']"`（满足其一）；无权限时移除元素（并解绑其事件）；支持全局注册权限来源（响应式 userPermissions）；权限变化（登录/切换租户）后已渲染指令不自动复活（要求重新渲染场景说明）。

```javascript
const permissions = ref<string[]>([])
let permGetter = () => permissions.value
export function setupPerm(getter) { permGetter = getter }

function hasPerm(required) {
  const list = permGetter()
  const need = Array.isArray(required) ? required : [required]
  return need.some(p => list.includes(p))
}
export const vPerm = {
  mounted(el, binding) {
    if (!hasPerm(binding.value)) el.remove() // 直接移除，事件一并消失
  }
}
// 全局：app.directive('perm', vPerm)
// <button v-perm="'order:delete'">删除</button>
// 组件更新时权限动态变化需要 v-if 或 key 重渲染——指令 mounted 只判一次
```
**评分点**：
- 数组传参 anyOf 语义正确。
- 移除而非隐藏（安全：DOM 上不该存在），并说明事件随之消失。
- 权限来源做成可注入 getter（解耦 store）。
- 能指出 mounted 只执行一次的局限与 v-if/key 方案。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-6edfb38f-eb48-4426-9af3-ad60e40ee2d3-cwd'; fi
exit "$__zcode_status"
