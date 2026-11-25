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

**追问**：

1. 同层级出现重复 key 会发生什么？→ 开发环境会告警，diff 时靠 key 建索引，重复的后者覆盖前者，节点会丢失或渲染到错误位置，表现出来是"少了一行/内容串了"。
2. 想主动重置一个组件的内部状态，用 key 是对的吗？→ 对，key 变化等于卸载重挂，但代价是 DOM 重建、焦点与动画丢失，只适合"换数据源就重来"的场景，不要拿它当刷新按钮用。
3. 嵌套列表里 key 需要全局唯一吗？→ 不需要，只在同级兄弟间唯一即可；但两个不同列表若渲染到同一父级，要用 `${groupId}-${id}` 拼前缀，否则会互相复用。
