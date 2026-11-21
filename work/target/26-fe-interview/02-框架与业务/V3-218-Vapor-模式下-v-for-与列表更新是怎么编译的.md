---
title: [V3-218] Vapor 模式下 v-for 与列表更新是怎么编译的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-218：Vapor 模式下 v-for 与列表更新是怎么编译的？
**答**：
- 编译为 `createFor(source, renderItem, key)`，内部维护**基于 key 的位置映射**（非完整 vnode diff）。
- renderItem 每次**新建块**（子组件实例/子节点组），删除时直接卸载对应块并断开订阅。
- 排序优化：同 key 复用块实例，按新顺序执行 `insertBefore` 移动，不做逐节点同层比较。
- 与 VDOM 模式差异：没有"新旧 children 数组 diff"阶段，响应式驱动 `createFor` 内部的增量同步（增/删/移）。
- 追问钩子：无 key 时性能如何？——退化为按索引复用，仅更新内容，等价 VDOM 模式的无 key diff。

```javascript
// <li v-for="item of items" :key="item.id">{{ item.name }}</li>
import { createFor } from 'vue/vapor';
function setup() {
  const items = ref([{ id: 1, name: 'a' }, { id: 2, name: 'b' }]);
  return createFor(
    () => items.value,
    (item, i) => {               // 每项一个独立块
      const li = template('<li></li>')();
      setText(li, () => item.name); // 细粒度绑定
      return li;
    },
    (item) => item.id,           // keyGetter：驱动复用与移动
  );
}
// items.value.sort(...) 时：块不重建，仅 insertBefore 移动 DOM
```
