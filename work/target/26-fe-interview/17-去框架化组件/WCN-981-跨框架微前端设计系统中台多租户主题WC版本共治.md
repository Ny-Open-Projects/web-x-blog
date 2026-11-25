---
title: [WCN-981] 跨框架微前端 + 设计系统中台：多租户主题与 WC 版本怎么共治
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-981：跨框架微前端 + 设计系统中台：多租户主题与 WC 版本怎么共治

**答**：
- 结论先行：多租户主题 + 多框架宿主的治理核心是「协议统一、版本协商、作用域隔离」——主题 token 按租户作用域注入，WC 版本由宿主统一协商提升。
- 主题隔离：每个子应用容器声明自己的 token 覆盖层（CSS 变量作用域），避免全局 :root 污染；WC 只消费变量，不感知租户（前文 token 下发可复用）。
- 版本协商：用 Module Federation shared + import maps 把 DS 组件包设 singleton，租户/子应用声明可接受版本范围，加载器取兼容的最高版本。
- 治理红线：所有租户主题覆盖必须过对比度/a11y 校验，WC 新版本要跑「三框架一致性 + 视觉回归」门禁才准发。
- 追问钩子：面试官问「两个租户主题不同但共享组件实例会不会串色」——答：WC 用 CSS 变量继承，按容器作用域注入，实例虽复用但样式随宿主容器而定，彼此隔离。

```javascript
// 按租户作用域注入主题，不污染全局
function applyTenantTheme(container, tokens) {
  for (const [k, v] of Object.entries(tokens))
    container.style.setProperty('--' + k, v); // 只作用于该容器子树
}
const tenantA = document.getElementById('tenant-a') || document.body;
applyTenantTheme(tenantA, { 'ds-primary': '#f00', 'ds-radius': '4px' });
applyTenantTheme(document.getElementById('tenant-b') || document.body,
  { 'ds-primary': '#1677ff', 'ds-radius': '8px' });
// WC 内部 var(--ds-primary) 自动取所在容器的值，多租户互不干扰
function tenantColor(el) {
  return getComputedStyle(el).getPropertyValue('--ds-primary').trim();
}
console.log('租户A主色:', tenantColor(tenantA));
// 版本协商：shared singleton，取兼容的最高版本
const ranges = [['^1.0.0', '^2.0.0'], ['^2.3.0']];
const version = ranges.every(r => r.some(x => x.includes('2'))) ? '2.3.0' : 'v1';
console.log('协商版本:', version);
// 治理红线：主题覆盖需过对比度校验
console.log('主题隔离与版本协商已就绪');
```
