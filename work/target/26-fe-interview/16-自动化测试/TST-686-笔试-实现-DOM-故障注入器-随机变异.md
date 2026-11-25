---
title: [TST-686] 笔试：实现 DOM 故障注入器（随机变异 + 回滚 + 断言）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-686：笔试：实现 DOM 故障注入器（随机变异 + 回滚 + 断言）

**题目**：实现 injectDomChaos(root,{rate,types})。对 root 后代按 rate 概率做 hide/remove/text 变异；每个变异记录精确回滚（恢复 display/parent+nextSibling/textContent）；返回 {count,restore}。

**答**：
- 支持 hide/remove/text 三类变异，按概率随机选择节点。
- 回滚函数精确恢复节点位置与样式（记录 parent 与 nextSibling）。
- 返回变异清单供断言使用。

```javascript
function injectDomChaos(root, { rate = 0.2, types = ['hide'] } = {}) {
  const actions = [];
  [...root.querySelectorAll('*')].forEach(n => {
    if (Math.random() >= rate) return;
    const type = types[Math.floor(Math.random() * types.length)];
    if (type === 'hide') {
      const old = n.style.display;
      n.style.display = 'none';
      actions.push(() => { n.style.display = old; });
    } else if (type === 'remove') {
      const parent = n.parentNode, next = n.nextSibling;
      parent.removeChild(n);
      actions.push(() => parent.insertBefore(n, next));
    } else {
      const old = n.textContent;
      n.textContent = '[chaos]';
      actions.push(() => { n.textContent = old; });
    }
  });
  return { count: actions.length,
    restore: () => { while (actions.length) actions.pop()(); } };
}
```

**评分点**：
- 三类变异实现正确
- 回滚精确恢复节点位置
- 概率注入可复现（可注入随机源）
- 返回清单便于断言
