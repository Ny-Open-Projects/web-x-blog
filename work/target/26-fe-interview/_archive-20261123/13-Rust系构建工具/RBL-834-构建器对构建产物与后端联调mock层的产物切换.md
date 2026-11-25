---
title: [RBL-834] 场景题：mock 数据层的产物切换——开发/测试/生产环境的网络层构建差异
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-834：场景题：mock 数据层的产物切换——三环境网络层的构建差异

**答**:
- 网络层的三环境形态：dev 用 mock 层（MSW/本地 stub）、测试用录制回放、生产用真实 API——构建差异的正确实现是「模块级条件」：`import '#api'` 的 resolve 按 mode 指向不同实现（api.real.ts / api.mock.ts）——解析期分支（RBL-745 平台分支的 mode 版），产物只含本环境的实现。
- 反模式：运行时 if（mock 代码进生产产物——体积 + 泄漏 mock 数据风险）；「生产产物含 mock 路由表」是审计必查项。
- mock 与类型的同构：mock 层必须与真实 API 共享类型（同构契约）——构建器校验 mock 实现的返回类型 = 真实实现的返回类型（TypeScript 层），mock 漂移（接口变了 mock 没更新）在类型检查暴露。
- 测试环境的录制回放产物：录制的 fixture 入仓（确定性），构建器把 fixture 作为资源处理（hash + 按需加载）；「录制数据含真实用户数据」是合规风险（RBL-804 泄漏检测的 mock 版）。
- 追问钩子：为什么 mock 切换用「resolve 条件」而不是「环境变量 if」？——resolve 条件在打包期完成 tree shaking（mock 代码物理不在产物里，零体积零泄漏）；env if 依赖死代码消除识别（define 替换 + DCE 可靠但脆弱——复杂表达式绕过 DCE）；「解析期分支」是确定性最强的环境隔离。

```javascript
// 条件 resolve 配置
const alias = (mode) => ({
  '#api': mode === 'dev' ? './src/api/api.mock.ts'
        : mode === 'test' ? './src/api/api.replay.ts'
        : './src/api/api.real.ts',
});
// 同构类型契约
// src/api/types.ts —— 真实与 mock 共享
export interface ApiClient { getUser(id: string): Promise<User>; }
// api.mock.ts 实现同样接口（类型层校验 mock 漂移）
export const api: ApiClient = { getUser: async (id) => fixtures.users[id] };
// 产物审计：生产产物不含 mock
function auditNoMock(products, { prodMode }) {
  if (!prodMode) return [];
  return products.filter(f => /__mocks__|msw|fixture/.test(f.code))
    .map(f => `${f.name} 含 mock 残留——生产产物禁止`);
}
```
