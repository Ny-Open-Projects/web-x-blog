---
title: [AIC-375] 评审一个新 API 的设计（REST 接口/组件 props），AI 检查清单包含什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-375：评审一个新 API 的设计（REST 接口/组件 props），AI 检查清单包含什么？
**答**：
- 一致性：命名/分页/错误码/返回结构是否与既有 API 模式一致（仓库惯例优先）。
- 演进性：版本化策略/向后兼容性/废弃路径——今天的设计明天能不能改。
- 错误设计：错误响应是否可行动（客户端拿到能做什么）/错误码是否枚举完整。
- 文档自足：仅凭 API 文档（不读实现）能否正确接入——AI 以「只读文档模拟接入」验证。

```javascript
const apiDesignCheck = {
  consistency: '与仓库既有 API 模式对齐',
  evolution: '版本化/兼容/废弃路径',
  errors: '错误可行动 + 码完整',
  docOnly: 'AI 只读文档模拟接入，卡壳即文档缺口',
};
r
```
