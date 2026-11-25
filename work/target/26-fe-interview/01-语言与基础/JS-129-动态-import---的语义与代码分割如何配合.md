---
title: [JS-129] 动态 import() 的语义与代码分割如何配合？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-129：动态 import() 的语义与代码分割如何配合？

**答**：
- `import()` 返回 Promise（模块命名空间对象），可在任意位置调用：条件、循环、事件回调。
- 打包器以 import() 的目标为切分点生成独立 chunk，实现按需加载与路由级分割。
- 与静态 import 的区别：静态 import 在模块求值前完成加载且不可取消；import() 是运行时决策。
- 弱网下 chunk 加载会失败，要做重试兜底；配合 prefetch/preload 提示可优化体验。

```javascript
// 1. 事件触发按需加载
button.addEventListener('click', async () => {
  const { default: Chart } = await import('./chart.js'); // 点击才拉取
  new Chart(el);
});

// 2. 路由级代码分割
const routes = {
  '/home':  () => import('./pages/home.js'),
  '/admin': () => import('./pages/admin.js'), // 权限页独立分包
};

// 3. 失败重试：弱网 chunk 加载失败是线上常见问题
async function loadPage(name, retries = 2) {
  try {
    return await routes[name]();
  } catch (e) {
    if (retries > 0) return loadPage(name, retries - 1);
    throw new Error(`页面资源加载失败: ${name}`);
  }
}

// 4. 与预加载提示配合（不执行，只提前下载）
// <link rel="modulepreload" href="/chunks/admin.js">
// webpack: import(/* webpackPrefetch: true */ './next-page.js')

// 5. 模块命名空间对象的形态
import('./math.js').then((mod) => {
  console.log(Object.keys(mod));   // 所有具名导出 + default
  console.log(mod.default);
});
```

**追问**：

1. 同一个模块 `import()` 两次，会发两次请求吗？ → 不会，模块只求值一次，第二次拿到同一个命名空间对象；但求值结果（含失败）会被模块映射缓存。
2. 为什么「失败重试 import」经常无效？ → 浏览器把失败的 fetch 也记进模块映射，同一 URL 再 import 仍直接 reject；重试必须换 URL（加版本或时间戳参数）才能重新请求。
3. 路由分包后再做 prefetch，会不会把弱网用户流量打爆？ → 会；prefetch 应在空闲且网络良好时触发，用 `requestIdleCallback` 加 `connection.effectiveType` 判断，弱网直接跳过。
