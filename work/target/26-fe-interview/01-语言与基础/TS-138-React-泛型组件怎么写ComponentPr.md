---
title: [TS-138] React 泛型组件怎么写？ComponentProps 如何提取 Props？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-138：React 泛型组件怎么写？ComponentProps 如何提取 Props？
**答**：
- 类型参数写在函数组件上，使用处由 props 自动实例化，实现数据驱动的组件类型。
- `ComponentProps<typeof X>` 提取组件 Props，用于 wrapper、HOC、测试工具。
- 泛型组件必须先"具象化"再提取：`ComponentProps<typeof List<User>>`（TS 4.7+ 实例化表达式）；或直接导出 Props 接口复用。

```tsx
// 泛型组件
function List<T extends { id: string }>(props: {
  items: T[];
  render: (item: T) => React.ReactNode;
  onSelect?: (item: T) => void;
}) {
  return (
    <ul>
      {props.items.map((it) => (
        <li key={it.id} onClick={() => props.onSelect?.(it)}>{props.render(it)}</li>
      ))}
    </ul>
  );
}

interface User { id: string; name: string }

// Props 提取：先具象化
type UserListProps = ComponentProps<typeof List<User>>;
const renderName: UserListProps["render"] = (u) => u.name; // u 自动是 User

// 坑：ComponentProps<typeof List> 不具象化时拿到未解析的泛型签名，T 悬空
// 实践：非泛型包装组件直接导出 Props 接口，泛型组件先固定 T 再提取
```
