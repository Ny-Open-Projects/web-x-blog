---
title: [R19-048] React.memo 在什么情况下会失效？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-048：React.memo 在什么情况下会失效？
**答**：
- memo 只做 props 浅比较：传入新对象、新数组、新函数都会击穿缓存。
- 内联函数 props 不包 useCallback、对象 props 不包 useMemo 时，memo 形同虚设。
- 组件内部自身的 state 或 useContext 变化仍会重渲染，memo 管不到。
- 数据结构复杂时可给 memo 第二个参数自定义比较函数，但要自己保证正确性。

```jsx
const UserCard = memo(function UserCard({ user, onSelect }) {
  console.log('render UserCard', user.name);
  return <div onClick={() => onSelect(user.id)}>{user.name}</div>;
});

function Parent({ users }) {
  // 用 useCallback 稳定函数，否则 memo 失效
  const handleSelect = useCallback((id) => console.log(id), []);

  // user 对象需保证引用稳定（列表数据不要每次现造）
  return users.map((u) => <UserCard key={u.id} user={u} onSelect={handleSelect} />);
}
```
