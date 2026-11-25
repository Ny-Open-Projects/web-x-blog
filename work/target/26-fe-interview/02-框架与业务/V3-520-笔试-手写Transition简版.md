---
title: [V3-520] 笔试：手写 Transition 简版（CSS 模式）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-520：笔试：手写 Transition 简版

**答**：实现 `MyTransition`（CSS 模式）：① 进入：添加 `-enter-from` → 下一帧 `-enter-active -enter-to`，transitionend 后清理；② 离开：`-leave-from` → `-leave-active -leave-to`，动画结束才真正移除 DOM（延迟卸载）；③ 自动检测过渡时长（getComputedStyle 取最长 transition-duration）；④打断处理：leave 期间重新进入要取消 leave 流程；⑤ appear 支持。写出实现。

```javascript
const MyTransition = {
  name: 'MyTransition',
  props: { name: { type: String, default: 'v' }, appear: Boolean },
  setup(props, { slots }) {
    return () => {
      const child = slots.default()[0];
      child.props = child.props ?? {};
      child.props.appearHook = props.appear;   // patch 层消费
      child.transition = {
        enter(el, done) {
          const base = props.name;
          el.classList.add(`${base}-enter-from`, `${base}-enter-active`);
          requestAnimationFrame(() => {
            el.classList.remove(`${base}-enter-from`);
            el.classList.add(`${base}-enter-to`);
            whenTransitionEnds(el, done);
          });
        },
        leave(el, done) { /* 同构 leave 流程 + 延迟卸载 */ },
      };
      return child;
    };
  },
};
function whenTransitionEnds(el, done) {
  const { transitionDuration: dur, transitionDelay: del } = getComputedStyle(el);
  const total = (parseTime(dur) + parseTime(del)) * 1000;
  const onEnd = (e) => { if (e.target === el) { cleanup(); done(); } };
  const cleanup = () => { el.removeEventListener('transitionend', onEnd); clearTimeout(t); };
  const t = setTimeout(done, total + 20);      // 兜底
  el.addEventListener('transitionend', onEnd);
}
```

**评分点**：
- 三段类名时序（from → active+to → 清理）且下一帧切换（强制过渡）
- 过渡时长自动检测 + setTimeout 兜底（transitionend 不触发防御）
- 延迟卸载（done 回调才 remove）
- 打断与 appear 的处理认知
