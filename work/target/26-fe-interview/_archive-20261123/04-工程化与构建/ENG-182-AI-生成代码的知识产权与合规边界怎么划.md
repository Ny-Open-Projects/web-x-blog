---
title: [ENG-182] AI 生成代码的知识产权与合规边界怎么划？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-182：AI 生成代码的知识产权与合规边界怎么划？
**答**：
- 风险三问：训练数据来源是否合规、生成代码是否与开源许可代码实质性相似、上传片段是否带商业机密。
- 边界约定：内部代码只在私有部署或企业版（不训练）模型使用；开源贡献仓库禁止接入内部代码上下文。
- 许可证检查：生成代码做相似度扫描对标知名开源库（尤其 GPL 片段），命中阈值转人审改写。
- 合规留痕：AI 参与 PR 必须标记，记录工具版本、模型 ID 与 prompt 模板引用，出争议可追溯生成环境。

```yaml
# ai-compliance.yaml —— AI 使用合规策略
model_policy:
  allowed: [corp-private-llm, vendor-enterprise-no-training]
  forbidden: [public-free-tier]           # 公共免费渠道 内部代码禁用
data_boundary:
  upload_allow: [src/, docs/, types/]
  upload_deny: [secrets/, .env, '**/credential*', customer-data/]
license_scan:
  similarity_check: true                  # 生成代码与许可代码相似度扫描
  threshold: 0.85
  on_hit: manual_review_and_rewrite
traceability:
  pr_label_required: ai-generated
  record: { tool_version: true, model_id: true, prompt_template_ref: true }
```

## 第三十五章 体系与前瞻（ENG-183 ~ ENG-200）
