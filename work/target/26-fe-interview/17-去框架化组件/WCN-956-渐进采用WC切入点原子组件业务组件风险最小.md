---
title: [WCN-956] 渐进式采用 WC 从哪类组件切入风险最小：原子组件还是业务组件
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-956：渐进式采用 WC 从哪类组件切入风险最小：原子组件还是业务组件

**答**：
- 结论先行：从「无状态、接口稳定、跨端复用价值高」的原子组件切入（Button/Input/Icon/Tag）——改动小、风险低、能快速验证协议与工具链。
- 避开两类：① 强业务耦合组件（下单按钮联动库存/优惠）——协议复杂、WC 表达成本高；② 深度依赖框架能力的组件（依赖 Context/Router/状态管理）——跨边界传递困难。
- 切入顺序：先原子展示组件 → 再表单类（验证 ElementInternals）→ 最后容器类；每步配套测试与文档，形成可复用范式。
- 验证指标：首个组件要跑通「构建→发布→多框架消费→监控」全链路，证明工程闭环后再扩大范围（试点成功但推广失败的常见反例）。
- 追问钩子：面试官问「能不能直接在核心交易页用 WC 重写」——答：不建议，核心页优先绞杀者模式按模块替换，WC 切入从周边原子开始，降低回归风险。

```javascript
// 切分示例：先原子，再表单，后容器
const adoptionOrder = [
  { type: '原子展示', examples: ['ds-button', 'ds-icon'], status: '先做' },
  { type: '表单输入', examples: ['ds-input', 'ds-select'], status: '次做（验证 ElementInternals）' },
  { type: '业务容器', examples: ['ds-order-card'], status: '最后（依赖 Context，谨慎）' },
];
// 判断一个组件是否适合做切入点
function isGoodStart(c) {
  return c.status === '先做' && c.examples.length >= 1;
}
adoptionOrder.forEach(x => console.log(x.type, '->', x.status));
console.log('适合先做:', adoptionOrder.filter(isGoodStart).map(x => x.type));
// 验证工程闭环：构建 -> 发布 -> 多框架消费 -> 监控
const loop = ['构建', '发布', '多框架消费', '监控'].every(s => typeof s === 'string');
console.log('全链路闭环具备:', loop);
// 原则：接口越稳定、状态越少的组件，越适合做 WC 切入点
```
