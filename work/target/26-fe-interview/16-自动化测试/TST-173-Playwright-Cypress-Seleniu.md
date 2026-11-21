---
title: [TST-173] Playwright / Cypress / Selenium 怎么选型？各自适用场景？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-173：Playwright / Cypress / Selenium 怎么选型？各自适用场景？
**答**：
- 一句话结论：2026 年新项目默认 Playwright；存量 Cypress 项目无强需求不必迁；遗留老系统/需要非浏览器语言（Java/Python 团队）或老旧浏览器兼容才考虑 Selenium。
- Playwright 优势：三引擎全支持、进程外控制（多页签/iframe/多域自由）、自动等待 + locator 现代化、trace 调试、组件测试、并行分片成熟、微软持续迭代。劣势：无商业支持时遇到浏览器协议 bug 只能等修复；团队从 Selenium 迁移有学习成本。
- Cypress 优势：运行在浏览器内、time-travel 调试体验好、错误提示对新手友好、生态插件多。劣势：同源限制（多域/iframe 受限）、并行要付费 Dashboard（或社区方案）、单 tab 能力弱、对 Shadow DOM 要开开关。
- Selenium 优势：W3C 标准、语言/浏览器/生态最广、企业遗留资产多、真机/网格体系（Grid、云厂商）成熟。劣势：协议层 HTTP 轮询慢、无自动等待（手写 wait）、维护成本高。
- 选型维度清单：浏览器矩阵需求、团队语言栈、测试并发规模、调试基础设施（trace/视频）、CI 资源、与现有平台的集成、社区与维护活跃度。

```javascript
// 选型决策速查（白板可画）
const decision = {
  '新项目 Web E2E': 'Playwright（默认）',
  '已有大型 Cypress 代码库': '继续 Cypress（迁移成本 > 收益）',
  '跨多团队多语言（Java QA 团队）': 'Selenium + Grid',
  '需要测 Electron': 'Playwright（_electron API）',
  '需要多域跨站链路（OAuth 跳转）': 'Playwright（Cypress 同源受限）',
  '测试组件级视觉回归': 'Playwright CT / Storybook + Playwright',
};
```
