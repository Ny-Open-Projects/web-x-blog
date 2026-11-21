---
title: [DP-132] 什么是 Repository 仓库模式？前端为什么需要它？（高频压轴）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-132：什么是 Repository 仓库模式？前端为什么需要它？（高频压轴）
**答**：
- Repository 把"数据访问"从组件中抽走：对上暴露领域方法（getUserById / saveCart），对下封装 HTTP 细节、缓存、错误归一；组件依赖抽象接口而非 fetch 细节（DIP 落地）。
- 前端价值：换请求库/数据源只动 Repository；组件测试时注入内存版假仓库；缓存、重试、去重有统一落点（与 DP-133 Service 分层：Repository 管存取，Service 管业务编排）。
- 识别反例：组件里到处 `fetch('/api/...')` + 手拼 query + 裸吞错误，就是缺 Repository。

```javascript
// 抽象接口：依赖倒置的分界线
// interface UserRepository { getById(id): Promise<User>; save(user): Promise<void>; }
class HttpUserRepository {
  #http; #cache = new Map();                                  // 缓存收口在仓库内
  constructor(http) { this.#http = http; }
  async getById(id) {
    if (this.#cache.has(id)) return this.#cache.get(id);
    const dto = await this.#http.get(`/users/${id}`);
    const user = User.fromDTO(dto);                           // DTO → 领域模型（见 DP-133）
    this.#cache.set(id, user);
    return user;
  }
  async save(user) {
    const saved = await this.#http.put(`/users/${user.id}`, user.toDTO());
    this.#cache.set(user.id, User.fromDTO(saved));            // 写后更新缓存
    return saved;
  }
}
class InMemoryUserRepository {                                // 测试替身：同接口
  #db = new Map();
  async getById(id) { return this.#db.get(id) ?? Promise.reject(new Error('not found')); }
  async save(user) { this.#db.set(user.id, user); }
}
// 组件只认接口，实现来自注入（组合根决定用哪个）
function useUser(repo, id) {
  const user = ref(null);
  repo.getById(id).then((u) => (user.value = u));
  return user;
}
const repo = import.meta.env.TEST ? new InMemoryUserRepository() : new HttpUserRepository(http);
```
