---
title: [RBL-314] 构建产物的 License 合规检查
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-314：构建产物的 License 合规检查

**答**:
- 检查内容：依赖 license 类型审计（GPL 类传染性风险评估——前端产物一般允许但公司策略各异）、license 文本保留（MIT 要求版权声明保留在产物或分发物中）
- 构建/发布集成：license-checker 生成清单 → 白名单策略校验 → 产物附 THIRD-PARTY-NOTICES 文件（构建自动生成）
- 边界场景：字体 license（商业字体授权按页面/流量计费，要记录使用范围）、内嵌二进制（wasm/binding 的 license）、devDependency 不进产物（分母要对）
- CI 门禁：新增依赖触发 license 检查（PR 级），非白名单 license 需合规审批

```text
流程：license 清单生成 → 白名单校验 → NOTICES 产物生成 → PR 级门禁
注意：字体/二进制/代码外的资源也有 license
```
