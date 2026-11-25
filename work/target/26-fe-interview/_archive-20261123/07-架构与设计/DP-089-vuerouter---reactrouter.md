---
title: [DP-089] vue-router / react-router 源码里有哪些模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-089：vue-router / react-router 源码里有哪些模式？（高频）
**答**：
- **观察者/发布订阅**：URL 变化（popstate/hashchange）→ 通知当前路由组件重渲染——Router 实例是被观察者。
- **策略 + 状态**：hash/history/abstract 三种模式是三套"URL 同步策略"；路由匹配结果（matched 记录）本质是应用的状态。
- **工厂**：`createRouter(createWebHistory())` 工厂注入 history 实现，`createRouterMatcher` 生成匹配器。
- **职责链**：`beforeEach/resolve` 导航守卫链，逐环校验可重定向/中断（next() 即 next()）。

```javascript
// vue-router 简化骨架：策略（模式）+ 观察者（响应）+ 职责链（守卫）
class HistoryBase {                       // 抽象：URL 同步的公共骨架
  constructor(router) { this.router = router; }
  listen() { throw new Error('abstract'); }
  transitionTo(location, onComplete) {    // 模板方法：统一导航流程
    const target = this.router.resolve(location);   // 1. 匹配
    this.router.beforeGuards.run(target, () => {    // 2. 守卫职责链
      this.updateRoute(target);                     // 3. 更新路由状态
      onComplete?.(target);
    });
  }
  updateRoute(target) { this.current = target; } // 观察者会因 current 变化触发重渲染
}
class HashHistory extends HistoryBase {   // 策略1：hash 模式
  listen() {
    window.addEventListener('hashchange', () => this.transitionTo(location.hash.slice(1)));
  }
  push(loc) { location.hash = loc; }
}
class HTML5History extends HistoryBase {  // 策略2：history 模式
  listen() {
    window.addEventListener('popstate', (e) => this.transitionTo(e.state?.path || '/'));
  }
  push(loc) { history.pushState({ path: loc }, '', loc); this.transitionTo(loc); }
}
class Router {                            // 工厂产物
  #guards = [];
  constructor(options) {
    this.routes = options.routes;
    this.mode = options.mode || 'hash';   // 运行时选择策略
    this.matcher = createMatcher(options.routes);
  }
  beforeEach(fn) { this.#guards.push(fn); } // 注册守卫（职责链节点）
  get beforeGuards() {
    const guards = this.#guards;
    return {
      run(to, done) {                      // 串行职责链：任一环返回 false 即中断
        (function next(i) {
          if (i >= guards.length) return done();
          guards[i](to, () => next(i + 1));
        })(0);
      },
    };
  }
  resolve(location) {
    const record = this.matcher.match(location);
    return { path: location, matched: record || [] };
  }
}
function createMatcher(routes) {
  const map = new Map(routes.map((r) => [r.path, r]));
  return { match: (loc) => map.get(loc) || [] };
}
// 使用
const router = new Router({ routes: [{ path: '/', component: 'Home' }, { path: '/about', component: 'About' }] });
router.beforeEach((to, next) => { console.log('守卫1 放行', to.path); next(); });
const hist = new (router.mode === 'hash' ? HashHistory : HTML5History)(router);
router.mode = 'hash';
hist.transitionTo('/about');
// 守卫1 放行 /about —— 匹配 -> 守卫链 -> 状态更新 -> 订阅组件重渲染
```
