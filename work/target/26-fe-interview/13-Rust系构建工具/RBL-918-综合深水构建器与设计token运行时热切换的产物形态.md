---
title: [RBL-918] 综合深水：设计 token 热切换的产物形态——多品牌运行的变量架构
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-918：综合深水：设计 token 热切换的产物形态——多品牌变量架构

**答**:
- 多品牌（A/B 两个品牌皮肤）的 token 架构光谱：1) **单产物 + CSS 变量切换**（品牌差异全在变量层：`:root[data-brand=a]` / `[data-brand=b]`——切品牌 = 改一个 attribute；适合差异 ≤ 变量集）；2) **多产物**（品牌差异是代码级的——不同组件实现；按品牌构建 N 份）；3) **混合**（变量层 + 品牌专属组件懒加载）。选型依据：diff 的「代码占比」——变量可表达 → 单产物（体积与切换延迟双赢 RBL-777）。
- 构建器的配套：1) token 编译产出「品牌变量矩阵」（RBL-697 扩展：每品牌的变量集 + 完整性校验——品牌缺项 = fallback 告警）；2) 品牌专属 chunk 的标记（懒加载边界）；3) 字体/图标按品牌分包（品牌资源不共享——每品牌独立子集 RBL-720）。
- 热切换的完整性约束：切换时「进行中的动画/主题相关的 canvas」要重绘——token 切换只管 CSS 层，JS 侧读 token 的地方（canvas 绘制/echarts 主题）需要订阅切换事件——「CSS 变量 vs JS 常量」的双轨一致性是热切换的坑（RBL-777 对比度审计的 JS 扩展）。
- 首帧无闪烁：品牌 attribute 在 html 服务端就写入（SSR 读 cookie/domain 判定品牌）——客户端脚本再切就晚了（品牌闪变）。
- 追问钩子：为什么「JS 侧读 token」是热切换的隐形破坏者？——CSS 变量切换是即时的，但 `const COLOR = tokens.primary` 这种 JS 常量在模块加载时固化——切品牌后 canvas/图表仍用旧色（双轨不一致）；正确姿势是「JS 读 token 也走变量」（getComputedStyle 实时读或订阅变更）——token 架构的完整性必须覆盖所有消费点，CSS 层完整 ≠ 全局完整。

```javascript
// 品牌变量矩阵编译
function compileBrandTokens(tokens, brands) {
  const matrix = {};
  for (const b of brands) {
    matrix[b] = {};
    const missing = [];
    for (const [k, def] of Object.entries(tokens)) {
      const val = def.brands?.[b] ?? def.value;
      if (def.brands?.[b] === undefined && !def.shared) missing.push(k);
      matrix[b][k] = val;
    }
    if (missing.length) warn(`品牌 ${b} 缺 ${missing.length} 个 token——回退默认值`);
  }
  // 产出 CSS：[data-brand=a] { --x: ... } 每品牌一层
  return { matrix, css: brands.map(b =>
    `[data-brand="${b}"] {\n${Object.entries(matrix[b]).map(([k, v]) => `  --${k}: ${v};`).join('\n')}\n}`) };
}
// JS 侧消费（实时读，不固化）
const readToken = (name) =>
  getComputedStyle(document.documentElement).getPropertyValue(`--${name}`).trim();
// canvas 重绘订阅
document.addEventListener('brand-change', () => redrawCanvas());   // 双轨一致性
```
