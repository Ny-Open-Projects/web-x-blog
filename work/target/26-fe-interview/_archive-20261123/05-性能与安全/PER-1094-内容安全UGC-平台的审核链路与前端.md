---
title: [PER-1094] 内容安全：UGC 平台的审核链路与前端配合
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1094：内容安全：UGC 平台的审核链路与前端配合

**答**：
- 链路：发布前机审（敏感词/图片模型）→ 疑似人审队列 → 发布后抽审与举报处理；前端负责"发布即拦截 + 展示层合规"。
- 前端配合：输入侧敏感词即时提示（本地词库 + 服务端校验）、图片上传前本地压缩与基础检测、被处置内容前端渲染降级（仅作者可见等）。
- 对抗：变体词（拼音/拆字/同音字）需要服务端 NLP，前端规则只拦明显违规降低误发成本。
- 证据链：举报/处置记录留存，前端处置操作要幂等可追溯。

```javascript
// 敏感词前端即时校验
const WORDS = loadWordlist();                        // 本地基础词库
function precheck(text) {
  const hits = WORDS.filter(w => text.includes(w));
  return { ok: hits.length === 0, hits, action:
    hits.length ? '阻断发布并提示修改' : '送服务端机审' };
}
// 服务端机审通过后前端才允许真正 submit，
// 处置状态内容渲染：status==='removed' 时仅作者可见并展示违规原因
```
