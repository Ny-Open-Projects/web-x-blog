---
title: [R19-214] Action 里读 FormData 的边界值有哪些坑（file/多选/空值）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-214：Action 里读 FormData 有哪些边界值坑？
**答**：
- 所有值都是 string | File | null：数字要先转换（`Number(fd.get('price'))`，NaN 兜底）；勾选框未选时 get 返回 null（用 has/checkbox value 设计）。
- 多选（select multiple、同名 checkbox）：`fd.getAll('tags')` 返回数组，get 只拿第一个。
- File：大小/类型校验在服务端做（不能信任前端），大文件考虑流式处理（`formData` 的 File.stream()）或直传对象存储签名。
- 结构化数据：数组/对象要自己设计 key 约定（`items.0.name`）或 JSON 字符串字段 + 服务端解析。
- zod 兜底：`schema.parse(Object.fromEntries(fd))` 一次性完成类型收敛，配合 fieldErrors 回显。
