---
title: [ARC-141] Vue2 → Vue3 大型项目迁移架构如何设计（兼容层/gogocode/分模块灰度）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-141：Vue2 → Vue3 大型项目迁移架构如何设计（兼容层/gogocode/分模块灰度）？
**答**：
- 总路线：先全局升级依赖底座（Vue 3 + @vue/compat 兼容层跑通构建与启动）→ codemod 批量转换（gogocode/gogocode-plugin-vue 处理 API 改名、过滤器、事件总线等机械变更）→ 兼容层下逐模块清理告警 → 移除 compat 切换正式运行时 → 分应用/路由灰度发布。
- 禁区先行盘点：第三方依赖清单（UI 库、vue-router、vuex）必须先有 Vue3 兼容版，这是前置阻塞项；无法兼容的库（如老的富文本封装）列入替换方案。
- 状态管理迁移是独立工作流：vuex → pinia 可共存（两套 store 并行，新模块用 pinia，老模块按需迁移），不要求一步到位。
- 风险控制：compat 模式下逐步清零 warning（每个 warning 对应一条 codemod 或手改项），全清后才允许移除 compat——这是迁移完成的客观标准。

```javascript
// 迁移配置要点
// 1. 兼容层启动（迁移期）
import { createApp, configureCompat } from 'vue';
configureCompat({
  MODE: 2,                                   // 按 Vue2 语义兼容运行
  COMPONENT_V_MODEL: false,                  // 已完成 codemod 的特性可单独关闭，逐步收敛
});
// 2. vite 集成：vite-plugin-vue2 与 @vitejs/plugin-vue 无法共存 → 迁移期用 webpack5 构建更稳
// 3. codemod 批量转换
//   npx gogocode -s ./src -t gogocode-plugin-vue -o ./src-vue3
//   覆盖：new Vue → createApp、$listeners 移除、过滤器移除、异步组件 API 等
// 4. 兼容告警看板（迁移完成的客观标准）
//   window.addEventListener('vue-devtools-hook', ...)
//   收集 configureCompat warnings → 按特性分组统计 → 清零 → MODE: 3 移除 compat
const migrationChecklist = {
  step1_upgrade_deps:   ['vue@3', '@vue/compat', 'vue-router@4', 'pinia(并行引入)', 'ui 库 v3 版'],
  step2_codemod:        ['gogocode 批量转换', 'git 按模块分 PR 便于 review'],
  step3_clean_warnings: ['compat warnings 清零（每条对应修复项）'],
  step4_remove_compat:  ['configureCompat 移除', '全量回归'],
  step5_gray_release:   ['按应用/路由灰度', '性能与错误率对照监控'],
};
```
