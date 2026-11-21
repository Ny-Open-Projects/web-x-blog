---
title: [ARC-466] 渲染层的分层架构：UI 组件与领域逻辑如何真正分离？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-466：UI 组件与领域逻辑分离的落地
**答**:
- 分离标准：UI 组件不知道业务名词（商品/订单），只接收 props 数据与回调；领域逻辑（校验规则/状态流转/接口调用）在 hooks/store/service 层。测试视角最清晰：UI 组件用通用数据测试，领域层不依赖 DOM 测试。
- 落地模式：容器组件（领域接线：数据获取 + 动作分发）+ 展示组件（纯 props）→ 演进到 hooks 接线（useOrder(id) 返回渲染所需 view-model）。
- View-Model 设计：领域数据 → 渲染数据的转换层（格式化/状态映射/权限显隐计算）放 view-model，组件保持"哑"；同一领域多个页面共享 view-model 片段。
- 边界守护：lint 禁止 views 直接 import services（ARC-409 脚本）；领域名词不出现在展示组件 props 命名（可以叫 items 不叫 orders——视组件通用程度权衡，过度通用化也要警惕）。
- 权衡说明：完全分离有转换样板成本——按组件复用潜力决定投入，一次性页面允许接线宽松，可复用区块严格分离。
```typescript
// view-model 接线（领域 → 渲染）
function useOrderView(orderId: string) {
  const { data, error, isLoading } = useOrder(orderId);       // 领域层
  const perms = usePermission();
  const vm = useMemo(() => data && ({
    header: { title: `订单 ${data.no}`, statusLabel: STATUS_LABEL[data.status] },
    items: data.items.map(i => ({ ...i, priceText: fmtPrice(i.price) })),
    canCancel: perms.has('order:cancel') && data.status === 'paid'
  }), [data, perms]);
  return { vm, error, isLoading };                            // 组件只消费 vm
}
```
