---
title: [WCN-715] 跨团队共享 WC 时，如何用契约测试保障 API 向后兼容？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-715：跨团队共享 WC 时，如何用契约测试保障 API 向后兼容？

**答**：
- 结论：把组件的公开契约（tag、attributes、properties、events、slots、::part）写成机器可读的 schema，发布前用契约测试校验实际组件是否仍满足。
- 流程：组件方维护契约文件 → CI 跑「契约 vs 实现」一致性校验 → 消费方按契约生成 mock，不依赖真实组件即可测试；破坏契约必须 major 版本。
- 追问钩子：属性类型从 string 改成 number 算不算破坏契约？考察对「类型兼容」的细致判断。

```javascript
const contract = {
  tag: 'ds-input',
  attributes: { size: 'string', disabled: 'boolean' },
  events: { 'ds-change': { detail: 'string' } },
  parts: ['input', 'label'],
};
function verify(impl) {
  const errs = [];
  for (const [name] of Object.entries(contract.attributes)) {
    if (!(name in impl.attributes)) errs.push(`缺属性 ${name}`);
  }
  for (const ev of Object.keys(contract.events)) {
    if (!impl.events.includes(ev)) errs.push(`缺事件 ${ev}`);
  }
  return errs;
}
console.log(verify({ attributes: { size: '' }, events: ['ds-change'] }));
```
