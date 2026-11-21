---
title: [ARC-251] 国际化中的动态内容与 UGC 翻译策略？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-251：国际化中的动态内容与 UGC 翻译策略？
**答**：
- 静态文案走语言包，动态内容（商品标题、UGC 评论）走**运行时翻译**：机翻服务 + 缓存层，与静态文案两套链路不混用。
- 架构：内容服务按"内容 ID+目标语言"维护翻译缓存（TTL 或按内容版本失效），首请求实时机翻并回填，命中缓存零延迟；高风险场景（商品详情）预生成常用语言。
- 展示策略：机翻内容明确标注（"译文"标识），可一键切回原文；法律/价格类内容不机翻或走人工。
- 输入侧国际化：UGC 输入的多语言敏感词（ARC-ESM 里敏感词 Trie 思路）按语言维护词库；富文本里用户语言自动检测辅助分类。

```typescript
// 动态内容翻译读取链
async function getContent(id: string, lang: string) {
  const cacheKey = `i18n:${id}:${lang}`;
  const cached = await kv.get(cacheKey);
  if (cached) return cached;
  const src = await contentRepo.get(id);
  const meta = await translate(src.title, src.lang, lang);     // 机翻
  const out = { ...src, title: meta.text, machine: true };     // 标记机翻
  await kv.set(cacheKey, out, { ttl: contentVersionTtl(src) });// 内容更新即失效
  return out;
}
// 前端：<p>{item.title}{item.machine && <Tag>译文</Tag>}<button onClick={showOriginal}>原文</button></p>
```
