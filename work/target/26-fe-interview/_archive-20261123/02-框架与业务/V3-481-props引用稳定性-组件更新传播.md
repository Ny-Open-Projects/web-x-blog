---
title: [V3-481] props 引用稳定性：更新传播链的治理
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-481：props 引用稳定性：更新传播链的治理

**答**：
- 传播链模型：父组件任一响应式变更 → 父 render 重跑 → 子组件 props 变化才触发子组件更新——「props 引用稳定」决定传播是否继续深入
- 不稳定 props 的来源：模板内联对象/数组（:list="[a, b]"）、计算结果未 memo、函数内联（:onClick="() => x"——V3 事件缓存默认救大部分）、store 的 getter 每次新对象
- 治理手段：props 拆分为基础类型（string/number 天然稳定）、稳定集合用 computed + 引用不变（依赖不变时 computed 返回同引用）、大子树用 v-memo 显式跳过
- v-memo 的取舍：显式声明「这些输入不变就不重渲」——收益大但维护成本高（依赖清单要人肉维护），适合确认瓶颈的局部
- 向下传导监控：DevTools 高亮「每次更新的组件集合」——传播到不该到的组件就是治理对象

```vue
<!-- 反模式 -->
<Table :columns="[{...每次新建}]" />
<!-- 正解 -->
<script setup>
const columns = computed(() => buildColumns(props.schema)); // 依赖不变引用不变
</script>
<Table :columns="columns" />
<!-- 极端: v-memo -->
<Row v-for="r in rows" :key="r.id" v-memo="[r.updatedAt]" :row="r" />
```
