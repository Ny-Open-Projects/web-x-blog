# 题目卡模板（work/target/ 用）

> 一张卡 = 一个考点。`{...}` 是待填位。
> **顶部 front-matter 是 hexo 用的** —— 这张卡直接丢进 `work/blog/source/_posts/` 就能进站，不用二次加工。
> `categories` / `tags` 就是博客的**分类依据**，填的时候想好站上挂哪儿。

```markdown
---
title: {考点或题目摘要}
date: {YYYY-MM-DD}
categories: [{科目，如 Elasticsearch / Kubernetes}]
tags: [{考点关键词}]
---

## {题目正文 —— 一句话，自足可读}

- **科目**：{go / py / sql / k8s / es}
- **来源**：source/{course-dir}/{file}.txt
- **课程编号**：{如 4.es-go}
- **类型**：概念 / 原理 / 实战
- **考点**：{一个，不超过 10 字}
- **难度**：★☆☆ ~ ★★★
- **答案**：
  {结论 + 关键过程。不能只写结论。}
- **追问**：
  1. {可延伸的一问}
- **质检**：PASS / 打回（挂 `ai/prompts/card-qc.md`）
- **创建时间**：{YYYY-MM-DD}
```

## 命名

```
work/target/{科目}/{编号}-{考点关键词}.md
```

例：`work/target/es/11-04-段合并触发条件.md`
