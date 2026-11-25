---
title: [SCN-045] Vue2 老项目要升级到 Vue3，升级策略怎么制定？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-045：Vue2 老项目要升级到 Vue3，升级策略怎么制定？
**答**：
- 先列破坏性变更清单：移除 filters 与 $on/$off 事件总线、v-model 参数变化、异步组件 API 变化、Element UI → Element Plus、vuex → pinia。
- 工具链：gogocode / vue-codemod 做自动化语法转换，eslint-plugin-vue 的 vue3 规则扫描残余写法，全量回归核心链路。
- 策略：中小项目一次性升级；大项目先迁 Vue 2.7（内置 Composition API）过渡，再切 Vue3；升级窗口冻结需求。

```bash
# 1. 过渡：先升 Vue 2.7，团队提前熟悉 Composition API
npm i vue@2.7

# 2. 自动化转换：迁移 filters、事件总线、v-model 等破坏性写法
npx gogocode -s src -t gogocode-plugin-vue -o src-vue3

# 3. 依赖替换：UI 库与周边生态同步升级
npm i vue@3 vue-router@4 pinia element-plus
npm un vuex element-ui

# 4. 静态扫描残留写法 + 全量回归测试
npx eslint src --ext .vue --rule '{"vue/no-deprecated-dollar-listeners": "error"}'
npm run test
```
