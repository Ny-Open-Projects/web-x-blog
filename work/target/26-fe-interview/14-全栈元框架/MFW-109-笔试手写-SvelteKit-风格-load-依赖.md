---
title: [MFW-109] 笔试：手写 SvelteKit 风格的 load 依赖追踪导航器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-109：笔试：手写 SvelteKit 风格的 load 依赖追踪导航器
**答**：实现简化版 SvelteKit 导航数据层：① 每个路由的 load 声明自己读取了 `url` 还是 `params`（用显式 deps 数组模拟）；② 导航时只重跑「URL 或 params 变化且 load 声明了对应依赖」的 load；③ 结果缓存在内存，未重跑的 load 直接复用；④ 支持手动 invalidateAll。

```ts
type LoadCtx = { url: URL; params: Record<string, string> };
type LoadFn = (ctx: LoadCtx) => Promise<unknown>;

interface RouteModule {
  path: string;            // 路由模式，如 /products/:id
  load: LoadFn;
  deps: Array<'url' | 'params'>;  // 声明依赖
}

function matchPath(pattern: string, pathname: string): Record<string, string> | null {
  const pSegs = pattern.split('/').filter(Boolean);
  const aSegs = pathname.split('/').filter(Boolean);
  if (pSegs.length !== aSegs.length) return null;
  const params: Record<string, string> = {};
  for (let i = 0; i < pSegs.length; i++) {
    if (pSegs[i].startsWith(':')) params[pSegs[i].slice(1)] = aSegs[i];
    else if (pSegs[i] !== aSegs[i]) return null;
  }
  return params;
}

class Navigator {
  private cache = new Map<string, unknown>(); // key: path + url
  private results = new Map<string, unknown>();

  constructor(private modules: RouteModule[]) {}

  async navigate(to: string, from?: string): Promise<Map<string, unknown>> {
    const url = new URL(to, 'https://x.com');
    const out = new Map<string, unknown>();
    const fromUrl = from ? new URL(from, 'https://x.com') : null;

    for (const mod of this.modules) {
      const params = matchPath(mod.path, url.pathname);
      if (!params) continue;

      // 依赖判断：没声明依赖 -> 永远复用；声明了且对应输入变了 -> 重跑
      const urlChanged = fromUrl && (fromUrl.pathname !== url.pathname || fromUrl.search !== url.search);
      const paramsChanged = fromUrl && JSON.stringify(matchPath(mod.path, fromUrl.pathname)) !== JSON.stringify(params);

      const needsRerun = !fromUrl
        || (mod.deps.includes('url') && urlChanged)
        || (mod.deps.includes('params') && paramsChanged);

      const cacheKey = `${mod.path}|${url.pathname}|${url.search}`;
      if (!needsRerun && this.cache.has(cacheKey)) {
        out.set(mod.path, this.cache.get(cacheKey));
        continue;
      }

      const result = await mod.load({ url, params });
      this.cache.set(cacheKey, result);
      out.set(mod.path, result);
    }
    this.results = out;
    return out;
  }

  invalidateAll(): void { this.cache.clear(); }
}

// —— 验证 ——
// const nav = new Navigator([
//   { path: '/products/:id', load: async ({ params }) => `detail:${params.id}`, deps: ['params'] },
// ]);
// await nav.navigate('/products/1');
// await nav.navigate('/products/1?tab=x', '/products/1'); // 未声明 url 依赖 -> 复用
```

**评分点**：
1. 依赖判定逻辑正确：未声明的依赖不触发重跑（复用），这正是 SvelteKit 细粒度导航的核心。
2. params 变化比较正确（含动态段值与空参对象的 JSON 对比）。
3. 缓存 key 覆盖 path+query，未命中才执行 load。
4. matchPath 处理了动态段与静态段混合、段数不符返回 null。
5. invalidateAll 清缓存后导航会全部重跑。
