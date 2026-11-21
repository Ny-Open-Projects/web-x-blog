---
title: [JS-132] 模块联邦（Module Federation）在 JS 层面的原理是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-132：模块联邦（Module Federation）在 JS 层面的原理是什么？

**答**：
- 核心思想：运行时从另一个独立构建的"远程容器"加载模块，而不是构建期打进来。
- 实现：远程站点暴露一个入口脚本，向全局注册容器对象；宿主按需 `container.get('模块名')`。
- 依赖协商：宿主与远程声明共享依赖（如 react）及版本范围，运行时谈判后只加载一份，解决双实例问题。
- 与动态 import 的区别：import() 的 chunk 是构建期已知的；联邦加载的是运行期才决定的第三方构建产物。

```javascript
// 简化版联邦加载器
function loadScript(src) {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[src="${src}"]`)) return resolve();
    const s = document.createElement('script');
    s.src = src;
    s.onload = resolve;
    s.onerror = () => reject(new Error(`远程入口加载失败: ${src}`));
    document.head.appendChild(s);
  });
}

async function loadRemoteModule(entryUrl, moduleName) {
  await loadScript(entryUrl);                 // 1. 拉取远程入口脚本
  const container = window.__remoteContainer__; // 2. 远程脚本注册的全局容器
  if (!container) throw new Error('容器未注册');
  const factory = await container.get(moduleName); // 3. 按名取模块工厂（异步）
  return factory();                            // 4. 得到模块命名空间，用法同本地 import
}

// 宿主使用：远程团队独立构建、独立部署
loadRemoteModule('https://remote.app/remoteEntry.js', './ProductList')
  .then((mod) => mod.default(document.querySelector('#app')));

// 依赖协商示意（真实联邦内部机制）：
// 宿主声明 shared: { react: { singleton: true, requiredVersion: '^18' } }
// 远程声明同样依赖 → 运行时比较版本 → 复用宿主已加载的那一份
// 结果：两份代码共享一个 React 实例，hooks 不会因双实例报错
```
