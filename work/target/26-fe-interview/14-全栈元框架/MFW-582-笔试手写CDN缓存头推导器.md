---
title: [MFW-582] 笔试：手写 CDN 缓存头推导器（路由声明 → Cache-Control）
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-582：笔试：手写 CDN 缓存头推导器

**答**：实现 `deriveCacheControl(route, config)`。config: `{ type: 'static'|'isr'|'dynamic'|'handler', revalidate?, swr?, private? }`。规则：1) static → `public, s-maxage=31536000, immutable`（构建产物 hash 寻址）；2) isr → `public, s-maxage=revalidate, stale-while-revalidate=revalidate`；3) dynamic → `private, no-cache`（个性化不可共享缓存）；4) handler + GET + revalidate → `public, s-maxage=revalidate`；handler 无 revalidate → `no-store`；5) private=true 覆盖为 private。冲突校验：dynamic + revalidate 同时声明 → 抛错（语义矛盾——动态却要 CDN 缓存）。返回 `{ cacheControl, warnings? }`。边界：isr 无 revalidate（默认 60）；private handler。

```javascript
function deriveCacheControl(route, config = {}) {
  const { type, revalidate, swr, private: priv } = config;
  if (type === 'dynamic' && revalidate != null)
    throw new Error(`${route}: dynamic 与 revalidate 语义矛盾（每请求渲染却要 CDN 缓存）`);
  let cc;
  switch (type) {
    case 'static': cc = 'public, s-maxage=31536000, immutable'; break;
    case 'isr': {
      const ttl = revalidate ?? 60;
      cc = `public, s-maxage=${ttl}, stale-while-revalidate=${ttl}`;
      break;
    }
    case 'dynamic': cc = 'private, no-cache'; break;
    case 'handler':
      cc = revalidate != null
        ? `public, s-maxage=${revalidate}`
        : 'no-store';
      break;
    default: throw new Error(`未知类型: ${type}`);
  }
  const warnings = [];
  if (priv && cc.includes('public'))
    cc = cc.replace('public', 'private');
  if (priv && cc.includes('immutable'))
    warnings.push('private + immutable 组合存疑——个人数据不应长期缓存');
  return { cacheControl: cc, warnings };
}

// 自测
console.log(deriveCacheControl('/_next/static/x.js', { type: 'static' }).cacheControl)
  .includes('immutable'));
console.log(deriveCacheControl('/products', { type: 'isr', revalidate: 60 }).cacheControl)
  === 'public, s-maxage=60, stale-while-revalidate=60');
console.log(deriveCacheControl('/account', { type: 'dynamic' }).cacheControl === 'private, no-cache');
console.log(deriveCacheControl('/api/products', { type: 'handler', revalidate: 60 }).cacheControl)
  === 'public, s-maxage=60');
console.log(deriveCacheControl('/api/user', { type: 'handler' }).cacheControl === 'no-store');

// 语义矛盾
let e; try { deriveCacheControl('/x', { type: 'dynamic', revalidate: 60 }); } catch (x) { e = x; }
console.log(/语义矛盾/.test(e.message));

// private 覆盖
r = deriveCacheControl('/products', { type: 'isr', revalidate: 60, private: true });
console.log(r.cacheControl.startsWith('private') && r.warnings.length === 0);

r = deriveCacheControl('/x', { type: 'static', private: true });
console.log(r.warnings[0].includes('存疑'));

// isr 默认 revalidate
console.log(deriveCacheControl('/blog', { type: 'isr' }).cacheControl).includes('s-maxage=60'));
```

**评分点**：
- 四类型 → 四种头的映射完整（static immutable/isr swr/dynamic private/handler 显式）；默认值合理
- 语义矛盾前置校验（dynamic + revalidate 抛错——无效组合显式化 RBL-526）
- private 覆盖与存疑告警（immutable 个人数据的组合问题）；边界
- 能说清「构建期推导 CDN 头 = 配置即产物（RBL-618）——两层缓存 TTL 对齐防屏蔽」属于加分
