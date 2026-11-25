---
title: [R19-369] 并发渲染边界：hydration mismatch 的场景库
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## R19-369：并发渲染边界：hydration mismatch 的场景库

**答**：
- mismatch 高发场景：时间/随机数（Date.now/Math.random）、locale 格式化（Intl 时区差异）、window 判断（typeof window）、localStorage 读取、浏览器插件改 DOM（翻译插件是最常见的「假性 mismatch」）
- React 18 行为：丢弃服务端 DOM 全树客户端重建（白屏闪）；React 19：保留服务端结果 + 补丁式修复（只重建不匹配节点）——修复粒度提升
- 规避模式：不稳定内容用 useId 生成稳定 id、动态内容包 ClientOnly 岛（mounted 后渲染）、SSR 一致的环境判断（用 request headers 而非 window）
- Suspense + streaming 的 mismatch：流式边界的服务端顺序与客户端补齐顺序不一致——React 用「隐藏 div + 替换」处理，业务无需干预但要理解
- 诊断：React 19 的 hydration error 带服务端/客户端差异 diff 输出——比 18 的报错信息可定位性强得多

```jsx
function Timestamp() {
  const [t, setT] = useState(null);
  useEffect(() => setT(Date.now()), []);       // 客户端挂载后才设 → SSR/CSR 一致
  return <time>{t ? format(t) : '--'}</time>;
}
```
