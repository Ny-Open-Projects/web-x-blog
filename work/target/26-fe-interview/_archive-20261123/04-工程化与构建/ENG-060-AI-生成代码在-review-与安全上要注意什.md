---
title: [ENG-060] AI 生成代码在 review 与安全上要注意什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-060：AI 生成代码在 review 与安全上要注意什么？
**答**：
- 幻觉包投毒：AI 建议安装的 npm 包可能不存在或名字相近的恶意包，装包前必须到 registry 核实。
- 凭证安全：对话中禁止粘贴真实密钥、内网地址与生产数据；发现生成代码里有硬编码凭证必须打回。
- 供应链与合规：新增依赖过 pnpm audit 与 license 审查；AI 生成代码同样不能引入不兼容协议的代码片段。
- 责任边界：AI 代码按"新人提交"对待，reviewer 逐行理解后才能 approve，不允许无 review 直接合入。

```bash
# 1. 核实 AI 建议的包真实存在，防幻觉包
npm view some-ai-suggested-pkg version

# 2. 扫描生成代码中是否泄漏敏感信息
grep -rnE "(api[_-]?key|secret|password)" src/ || echo "未发现明文凭证"

# 3. 与人工代码同一门禁
pnpm lint && pnpm test && pnpm build

# 4. 依赖安全审计
pnpm audit --prod
```

---

## 第十六章 包管理深水区（ENG-061 ~ ENG-066）

```mermaid
graph TD
  A["全局 store 内容寻址存储"] --> B["文件按内容 hash 分片 全局唯一一份"]
  B --> C["项目 node_modules .pnpm 目录"]
  C --> D["每个包版本一个目录"]
  D --> E["包内文件硬链接到 store 不复制数据"]
  C --> F["根 node_modules 直接依赖"]
  F --> G["符号链接指向 .pnpm 对应目录"]
  G --> H["传递依赖闭包在 .pnpm 内部"]
```
