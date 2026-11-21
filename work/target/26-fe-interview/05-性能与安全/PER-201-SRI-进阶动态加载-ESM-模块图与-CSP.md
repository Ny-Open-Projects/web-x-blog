---
title: [PER-201] SRI 进阶：动态加载、ESM 模块图与 CSP 怎么组合？（静态标签基础见 PER-080）
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-201：SRI 进阶：动态加载、ESM 模块图与 CSP 怎么组合？（静态标签基础见 PER-080）

**答**：
- 动态加载同样受保护：`createElement('script')` 支持 `integrity` 属性（同样必须 `crossOrigin = 'anonymous'`）；`fetch(url, { integrity })` 在哈希不匹配时直接 reject，内容先校验后使用。
- ESM 的盲区：给入口 `<script type="module">` 加 integrity 只校验**入口文件本身**，`import` 的子模块不校验——要覆盖整个模块图，需在 import map 的顶层 `integrity` 字段按模块标识逐个声明（Chromium 与 Safari 已支持，Firefox 落地较晚，使用前查 caniuse 并准备降级为自托管）。
- 能力边界：SRI 只验证"传输内容未被篡改"，不防"源头就坏"（上游包本身恶意、构建机被投毒）——后者靠依赖审计与锁版本（PER-079）；它也不覆盖同源动态接口响应。
- 组合拳：CSP `script-src` 管**允许哪些来源**，SRI 管**该来源的内容是否被改过**，两者正交、缺一不可；注意 CSP3 曾提案的 `require-sri-for` 指令未被浏览器广泛实现，方案里不要依赖它。第三方 CDN 不可控更新与哈希失效的权衡：锁版本号 URL + 锁哈希，或干脆自托管 vendoring。

```javascript
// 1. 动态插入第三方脚本：与静态标签同等参与 SRI 校验
export function loadScript(src, integrity) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src;
    s.integrity = integrity;              // 哈希不符时 onerror，脚本不会执行
    s.crossOrigin = 'anonymous';          // SRI 要求 CORS 模式，同 PER-080
    s.onload = () => resolve(s);
    s.onerror = () => reject(new Error(`load/SRI failed: ${src}`));
    document.head.appendChild(s);
  });
}

// 2. fetch 校验内容哈希：配置类 JSON 先验证再消费
const res = await fetch('https://cdn.example.com/config.json', {
  integrity: 'sha384-<构建时计算的哈希>',
});                                       // 内容被篡改时 fetch 直接 reject（TypeError）
const config = await res.json();
```

```html
<!-- 3. import map：给模块图整体加 integrity，覆盖动态 import 的子模块 -->
<script type="importmap">
{
  "imports": {
    "lodash-es": "https://cdn.example.com/lodash-es@4.17.21/lodash.js",
    "vue": "https://cdn.example.com/vue@3.5.13/dist/vue.runtime.esm-browser.prod.js"
  },
  "integrity": {
    "lodash-es": "sha384-<hash>",
    "vue": "sha384-<hash>"
  }
}
</script>
<!-- 只给入口 <script type="module" integrity> 加哈希是常见误区：子模块不在校验范围 -->
```
