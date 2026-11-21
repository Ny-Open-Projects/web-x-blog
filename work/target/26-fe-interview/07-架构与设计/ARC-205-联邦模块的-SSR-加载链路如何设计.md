---
title: [ARC-205] 联邦模块的 SSR 加载链路如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-205：联邦模块的 SSR 加载链路如何设计？
**答**：
- SSR 联邦的核心矛盾：浏览器端联邦靠运行时动态 fetch，Node 端没有浏览器环境且要求"同步可用"。2.0 提供 node 运行时 + chrome（进程内单例运行时）解决。
- 服务端链路：init 时预拉各子应用 manifest → 运行时把 remote 模块解析为 Node 可加载的产物（CDN 下载到内存/本地缓存）→ renderToString 时像本地模块一样 import。
- 关键工程点：产物缓存与失效（按 buildVersion 缓存，发布后失效）；一个进程一个 share-scope（避免多请求互相污染单例 React）；水位与超时（子应用 CDN 慢时走本地降级产物）。
- 水合一致性：服务端用了哪个版本的共享依赖必须随 HTML 传给客户端（如注入版本指纹），客户端协商结果必须一致，否则水合 mismatch。

```javascript
// Node 端联邦初始化（Next/Nitro 中间件层）
import { init, loadRemote } from '@module-federation/enhanced/runtime';

let inited = false;
export async function mfInit() {
  if (inited) return;                              // 进程级单例：一个 Node 进程一个 share-scope
  await init({ name: 'ssr-host', remotes: {
    shop: { entry: 'https://cdn.example.com/shop/mf-manifest.json' },
  }});
  inited = true;
}

export async function renderPage() {
  await mfInit();
  const Header = await loadRemote('shop/Header');  // 服务端直接拿到组件，无需浏览器 fetch
  return renderToString(createElement(Header, { lang: 'zh' }));
}
// 兜底：loadRemote 包一层 timeout+cache，CDN 抖动时回退到本地预构建的 fallback chunk
```
