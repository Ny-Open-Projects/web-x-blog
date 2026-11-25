---
title: [DP-104] 重构实战：上帝对象 userManager 如何用组合 + 外观拆分？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-104：重构实战：上帝对象 userManager 如何用组合 + 外观拆分？（高频）
**答**：
- 上帝对象识别信号：一个类/文件承担鉴权、资料、消息、日志等 3 个以上互不相关的职责，属性 30+，任何需求都要改它（DP-002）。
- 拆分手法：按职责切成独立模块（组合），旧 API 用外观保留——老调用方零改动，新代码走新模块，风险可控。
- 迁移策略：外观内部先委托给新模块（绞杀者模式思路），逐个方法迁移 + 单测护航，最后删除上帝对象。

```javascript
// 重构前：userManager 上帝对象 —— 登录、资料、消息、日志全在一个对象里
const userManager = {
  users: [], logs: [], messages: [],
  login(name, pwd) { /* 校验 + 写日志 + 发通知，60 行 */ },
  getProfile(id) { /* 查资料 + 写日志，40 行 */ },
  sendMessage(id, text) { /* 发消息 + 写日志，40 行 */ },
  log(msg) { this.logs.push(msg); },   // 每个方法都要手动写日志，重复且易漏
};
```

```javascript
// 重构后：按职责拆成组合关系的小模块，外观只做转发
class AuthService   { constructor(db, logger) { Object.assign(this, { db, logger }); } login(u, p) { this.logger.info('login ' + u); return this.db.verify(u, p); } }
class ProfileService{ constructor(db, logger) { Object.assign(this, { db, logger }); } get(id) { this.logger.info('profile ' + id); return this.db.findUser(id); } }
class MessageService{ constructor(db, logger) { Object.assign(this, { db, logger }); } send(id, text) { this.logger.info('msg to ' + id); return this.db.insertMsg(id, text); } }
// 外观：老代码继续调 userManager.xxx，内部已委托新模块（绞杀者迁移）
class UserManagerFacade {
  constructor(db, logger) {
    this.auth = new AuthService(db, logger);        // 组合：has-a 而非 is-a
    this.profile = new ProfileService(db, logger);
    this.message = new MessageService(db, logger);
  }
  login(u, p) { return this.auth.login(u, p); }
  getProfile(id) { return this.profile.get(id); }
  sendMessage(id, t) { return this.message.send(id, t); }
}
const userApi = new UserManagerFacade(db, logger);   // 对外出口保持稳定
userApi.login('tom', '***');
```
