---
title: [DP-002] 单一职责原则 SRP 在前端怎么落地？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-002：单一职责原则 SRP 在前端怎么落地？
**答**：
- SRP：一个模块/类/组件只应有一个引起它变化的原因。
- 前端典型违反：一个 `utils.js` 既做格式化又做本地存储又做埋点；一个组件既拉数据又渲染还弹 toast。
- 落地手法：按"变化方向"拆分——格式化归 `formatters`，存储归 `storage`，组件拆成容器组件 + 展示组件。
- 判断标准：能不能用一句话不带"和/与"地描述这个模块的职责。

```javascript
// 反例：一个函数承担三个变化原因（格式规则变、存储介质变、埋点协议变都会改它）
function saveUserInfo(user) {
  const text = `${user.name}(${user.vip ? '会员' : '普通'})`; // 职责1 展示格式
  localStorage.setItem('user', text);                          // 职责2 持久化
  tracker.send('save_user', user);                             // 职责3 埋点
}

// 正例：按变化方向拆成三个模块，各自独立演化
const formatters = {
  user: (u) => `${u.name}(${u.vip ? '会员' : '普通'})`,
};
const storage = {
  saveUser: (text) => localStorage.setItem('user', text),
};
const tracker = { send: (event, payload) => console.log(event, payload) };

function saveUserInfo(user) {
  storage.saveUser(formatters.user(user)); // 组装层只做编排，不含具体职责
  tracker.send('save_user', user);
}
saveUserInfo({ name: 'Tom', vip: true }); // Tom(会员)
```
