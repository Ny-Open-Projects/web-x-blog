---
title: [MFW-831] ISR 生成时旧请求把刚生成的新页回填覆盖成旧内容的竞态怎么解
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-831：ISR 生成时旧请求把刚生成的新页回填覆盖成旧内容的竞态怎么解

**答**：
- 结论：按需重验证时慢请求拿旧数据生成、快请求拿新数据生成；若慢请求后完成并写缓存，会把新页覆盖回旧页（陈旧回填）。
- 解法：缓存条目带生成版本号，写入用 CAS——仅当新版本 >= 当前版本才写入，旧版本回填直接丢弃。
- 追问钩子：版本号从哪来？——用触发重验证时的数据版本（DB updatedAt / 全局单调计数器），不用请求到达时间。

```javascript
const cache = new Map();   // key -> { version, html }
function writeIfNewer(key, version, html) {
  const cur = cache.get(key);
  if (cur && cur.version > version) return false;   // 旧回填 → 丢弃
  cache.set(key, { version, html });
  return true;
}

// 快请求：数据版本 10，先完成
writeIfNewer('/product/1', 10, '<new>');            // true
// 慢请求：数据版本 9（触发时更旧），后完成
writeIfNewer('/product/1', 9, '<stale>');           // false —— 不覆盖新页
console.log(cache.get('/product/1').html);          // <new>

// 版本号取自数据本身，而非 Date.now()（请求时间会误判）
async function regenerate(key) {
  const { html, dataVersion } = await renderWithVersion(key);
  return writeIfNewer(key, dataVersion, html);
}
```
