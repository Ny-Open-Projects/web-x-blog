---
title: [R19-035] 为什么列表要用稳定唯一的 key？index 作 key 有什么坑？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-035：为什么列表要用稳定唯一的 key？index 作 key 有什么坑？
**答**：
- key 是 Fiber 节点在同级间的身份标识，Diff 时靠 key 匹配新旧节点决定复用还是重建。
- 用数组 index 作 key：头部插入或删除时，后面所有元素的 index 都变了，React 会错位复用。
- 错位复用的典型 bug：带输入框的列表删除中间项后，输入内容串行；组件内部状态跟着"搬家"。
- 正确做法：使用数据自带的稳定 id；确实无 id 且列表纯静态展示时 index 才可接受。

```jsx
function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'a' },
    { id: 2, text: 'b' },
  ]);

  const insertTop = () => {
    setTodos([{ id: Date.now(), text: 'new' }, ...todos]);
  };

  return (
    <>
      <button onClick={insertTop}>头部插入</button>
      {/* 反例：index 作 key，头部插入后每项的 index 都变了 */}
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo.text}
            <input placeholder="index 作 key 会串行" />
          </li>
        ))}
      </ul>
      {/* 正例：稳定唯一 id，头部插入只新建第一项 */}
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.text}</li>
        ))}
      </ul>
    </>
  );
}
```
