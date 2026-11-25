---
title: [V3-503] Vue3 的 SSR 水合错误与降级
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## V3-503：Vue3 的 SSR 水合错误与降级

**答**：
- 水合错误来源：服务端与客户端渲染结果不一致（随机数/时间/window 判断/用户态差异）、DOM 结构被浏览器改写（嵌套错误被浏览器自动修正）——「标签嵌套非法」是最隐蔽的水合错
- Vue3 行为：水合不匹配 dev 严格告警并丢弃服务端 DOM 重建（客户端渲染兜底）；生产默认静默重建——「白屏闪一下」就是水合失败的重建
- 预防清单：时间/随机内容用客户端挂载后再填（onMounted 填充）、条件渲染依赖「水合稳定」的状态（用户态在服务端已知）、避免在 setup 里读浏览器 API
- 降级策略：水合失败页级降级（整页 CSR）vs 局部降级——局部用「客户端专属组件包 ClientOnly」隔离不稳定部分
- 诊断：vue 的 hydrationMismatch dev 警告带节点 diff；用「服务端 HTML 快照 vs 客户端 render 快照」对比工具定位

```vue
<ClientOnly>
  <LiveClock />        <!-- 时间类内容隔离, 避免 SSR/CSR 不一致 -->
</ClientOnly>
<!-- ClientOnly 实现: mounted 置 true, 服务端渲染占位 -->
```
