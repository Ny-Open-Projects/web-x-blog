---
title: [R19-359] useTransition 内部机制：isPending 与 lane 绑定
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-359：useTransition 内部机制：isPending 与 lane 绑定

**答**：
- startTransition(updateFn)：updateFn 内的 setState 被标记为 TransitionLane（低优先级）——渲染可被打断/丢弃，isPending 由「该 lane 是否仍在渲染中」驱动
- isPending 状态机：transition 开始 → pending true；渲染完成（或被更高优先级打断后重完成）→ false；「transition 内又触发新 transition」是新的 pending 周期
- 旧内容保持：Transition 期间旧 UI 一直显示（渲染没 commit）——这是「可中断不提交」的语义；但旧内容期间的用户交互（新点击）作为新优先级打断
- React 19 的 useActionState 关联：transition 与表单 action 的 pending 共享语义——isPending 统一了「提交中」的视图表达
- 常见误用：transition 包裹「输入受控值更新」——受控输入要即时（SyncLane），包裹后输入延迟；transition 只包「结果渲染」不包「输入状态」

```jsx
const [isPending, startTransition] = useTransition();
const [query, setQuery] = useState('');        // Sync: 输入即时
const [results, setResults] = useState([]);
function onChange(v) {
  setQuery(v);                                  // 即时
  startTransition(() => {                       // 低优: 可打断
    setResults(filter(hugeList, v));
  });
}
```
