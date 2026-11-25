---
title: [MFW-693] 笔试：手写 SW 缓存策略协调器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-693：笔试：手写 SW 缓存策略协调器

**答**：实现 `swStrategyFor(url)`。规则（RBL-692）：1) hash 文件名（`[\w]-[a-f0-9]{8,}.ext`）→ 'cacheFirst'（immutable——内容寻址）；2) `_next/data/`（Pages Router 数据 payload——getServerSideProps/getStaticProps 的 JSON；App Router 的 RSC payload 不走这里）→ 'networkFirst'（可变——SW 不屏蔽新数据）；3) `/api/` → 'networkOnly'（API 不缓存）；4) html（.html 或路径无扩展名）→ 'networkFirst'；5) 其余静态（图片/字体无 hash）→ 'cacheFirst' + maxEntries 限容。返回 `{ strategy, maxAge?, maxEntries? }`。校验函数 `isSafeCache(url)`：SW 缓存「可变内容」→ false（payload/API——反模式检测 RBL-692）。边界：未知扩展名（默认 networkFirst——保守）；空 URL。

```javascript
function swStrategyFor(url = '') {
  const isHashed = /[\w]-[a-f0-9]{8,}\.\w+$/.test(url);
  if (isHashed) return { strategy: 'cacheFirst', maxAge: 31536000 };   // immutable
  if (url.includes('/_next/data/')) return { strategy: 'networkFirst' };   // payload
  if (url.startsWith('/api/') || url.includes('/api/')) return { strategy: 'networkOnly' };
  if (url.endsWith('.html') || !/\.\w+$/.test(url)) return { strategy: 'networkFirst' };
  if (/\.(png|jpg|webp|woff)$/.test(url))
    return { strategy: 'cacheFirst', maxEntries: 60 };   // 无 hash 静态：限容
  return { strategy: 'networkFirst' };                   // 未知：保守
}
function isSafeCache(url) {
  const s = swStrategyFor(url);
  if (s.strategy === 'cacheFirst' && !/[\w]-[a-f0-9]{8,}/.test(url) &&
      !/\.(png|jpg|webp|woff)$/.test(url))
    return false;                                        // cacheFirst 无 hash 文件名 = 反模式
  return s.strategy !== 'networkOnly';                   // networkOnly 不缓存 = 安全
}

// 自测
// hash 文件名：immutable
console.log(swStrategyFor('/_next/static/main.a1b2c3d4.js').strategy === 'cacheFirst');
// payload：networkFirst
console.log(swStrategyFor('/_next/data/build1/products.json').strategy === 'networkFirst');
console.log(isSafeCache('/_next/data/build1/products.json') === true);   // networkFirst 安全
// API：networkOnly
console.log(swStrategyFor('/api/products').strategy === 'networkOnly');
console.log(isSafeCache('/api/products') === true);     // networkOnly 不缓存
// HTML
console.log(swStrategyFor('/products').strategy === 'networkFirst');
// 无 hash 图片：限容
r = swStrategyFor('/images/logo.png');
console.log(r.strategy === 'cacheFirst' && r.maxEntries === 60);
// 反模式检测：cacheFirst 无 hash
console.log(isSafeCache('/legacy/app.js') === false);   // 无 hash 无图片类型 = 反模式
// 空保守
console.log(swStrategyFor('').strategy === 'networkFirst');
```

**评分点**：
- 四类策略（hash cacheFirst/payload networkFirst/API networkOnly/无 hash 限容——可变性分层）
- isSafeCache 反模式检测（cacheFirst 无 hash = 可变内容被永久缓存——RBL-692）
- 未知保守 networkFirst（fail-safe——不确定时不缓存）；边界
- 能说清「SW 缓存边界 = 可变性判断：hash 文件名 immutable 安全，payload/API 必须 network-first」属于加分
