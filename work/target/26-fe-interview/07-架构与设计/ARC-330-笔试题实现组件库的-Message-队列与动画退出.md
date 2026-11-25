---
title: [ARC-330] 笔试题：实现组件库的 Message 队列与动画退出？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-330：笔试题：实现组件库的 Message 队列与动画退出？
**答**：实现 `message.success(text)` 全局提示：1) 命令式 API + React 集成（无 Provider 也可用）；2) 自动关闭（3s）+ hover 暂停；3) 退出动画播放完才移除 DOM（leaving 状态）；4) 同屏上限（超限移除最旧的）。
**评分点**：
- 命令式调用与 React 渲染桥接正确（单例容器挂载 + 事件/store 驱动）。
- 定时器与 hover 暂停正确（mouseleave 重置计时）。
- 退出动画状态机（visible → leaving → removed），用 transitionend 或超时兜底。
- 上限裁剪正确（FIFO 移除），列表 key 稳定。
```tsx
type Msg = { id: number; text: string; state: 'visible' | 'leaving' };
const store = { list: [] as Msg[], emit: () => {} };
export const message = {
  success(text: string) {
    const id = Date.now() + Math.random();
    store.list = [...store.list, { id, text, state: 'visible' }].slice(-5);  // 4) 上限 5 条
    store.emit();
    setTimeout(() => close(id), 3000);
    return () => close(id);
  },
};
function close(id: number) {
  store.list = store.list.map(m => m.id === id ? { ...m, state: 'leaving' } : m);  // 3) 先退出态
  store.emit();
  setTimeout(() => { store.list = store.list.filter(m => m.id !== id); store.emit(); }, 200); // 动画时长兜底
}
function MessageHost() {
  const [, force] = useReducer(x => x + 1, 0);
  useEffect(() => { store.emit = force; }, []);
  return <div className="msg-host">{store.list.map(m =>
    <div key={m.id} className={`msg msg-${m.state}`}                       // leaving 触发 CSS 退出动画
      onMouseEnter={e => (e.currentTarget as HTMLElement).dataset.pause = '1'}
      onMouseLeave={() => setTimeout(() => close(m.id), 3000)}>{m.text}</div>)}</div>;
}
// 挂载：root.render(<><App/><MessageHost/></>) —— message.success('已保存') 无需 Provider
```
