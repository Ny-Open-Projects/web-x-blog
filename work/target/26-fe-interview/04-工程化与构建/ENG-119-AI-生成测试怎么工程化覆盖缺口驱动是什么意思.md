---
title: [ENG-119] AI 生成测试怎么工程化？覆盖缺口驱动是什么意思？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-119：AI 生成测试怎么工程化？覆盖缺口驱动是什么意思？
**答**：
- 核心思路：不让 AI"随便补测"，而是先从覆盖率报告定位缺口分支，把源码与缺口喂给 AI 定向生成。
- 流水线化：低覆盖清单 → AI 生成 Vitest 用例 → 自动跑通 → 不通过回炉重试 → 人工 review 合入。
- 生成物与人工代码同门禁：lint、覆盖率重算、review，防止"为覆盖率而覆盖率"的空转用例。
- 适用边界：工具函数、状态机、解析器效果好；含复杂交互的 UI 生成质量低，优先人写。

```bash
# 1. 从覆盖率报告提取低覆盖文件清单（缺口驱动）
jq -r 'to_entries[] | select(.value.lines.pct < 60) | .key' \
  coverage/coverage-summary.json > low-covered.txt

# 2. 逐文件让 AI 生成用例，提示词写明框架与断言风格
while read -r file; do
  prompt="为 src/${file} 补充 Vitest 单测，覆盖现有用例未覆盖的分支，使用工厂函数构造数据"
  llm-cli "$prompt" < "src/${file}" > "tests/${file%.ts}.spec.ts"
done < low-covered.txt

# 3. 生成用例过同一门禁，不过关的丢弃重试
pnpm vitest run --reporter=dot
```
