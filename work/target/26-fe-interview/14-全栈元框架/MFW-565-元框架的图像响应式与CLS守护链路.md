---
title: [MFW-565] 图像响应式与 CLS 守护链路：尺寸占位的全链路
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-565：CLS 守护链路：图像尺寸占位的全链路

**答**:
- CLS 的守护链路：1) **Image 组件强制宽高**（width/height 属性 → aspect-ratio 占位 RBL-523——无尺寸图片 = 编译警告）；2) **SSR 时的占位计算**（构建期已知尺寸 → SSR HTML 直接带 aspect-ratio——首屏无偏移）；3) **动态图片**（用户上传任意尺寸——构建期未知 → 运行时 onLoad 后才能算——骨架占位策略：已知平均比例或 blur 占位 LQIP）；4) **字体 metrics**（RBL-564 size-adjust）。
- CLS 的 RSC 语义：SSR HTML 的占位在「流式注入」时保持（Suspense 边界的 skeleton 尺寸预占——内容到达替换后布局不跳——骨架尺寸 = 内容尺寸的预估精度决定 CLS）。
- CLS 监控：RUM 的 CLS 归因（layout-shift 的 source 元素——哪个元素偏移：图片/字体/动态内容——归因到组件）。
- 追问钩子：为什么「骨架屏」常常引入 CLS 而不是消除？——骨架的尺寸 ≠ 真实内容的尺寸（骨架高度 80px、内容 140px——内容到达时偏移 60px）；「骨架尺寸的精度」= CLS 的决定项：基于数据预估（商品图 4:3 固定）、CSS aspect-ratio 锁定、动态内容留余量——骨架屏的工程不是 UI 装饰而是「尺寸预测系统」：预测越准 CLS 越低。

```tsx
// 构建期已知尺寸：aspect-ratio 锁定
<Image src={product.image} width={800} height={600}
  style={{ aspectRatio: '4/3' }} />                      // 占位比例 = 真实比例
// SSR HTML：<img ... style="aspect-ratio: 800/600">     // 首屏零偏移
// 动态尺寸（用户上传）：LQIP 占位
function UserAvatar({ userId }: { userId: string }) {
  const [dim, setDim] = useState<{ w: number; h: number } | null>(null);
  return (
    <div style={dim ? undefined : { aspectRatio: '1/1' }}>   {/* 未知时方占位 */}
      <img src={...} onLoad={(e) => {
        setDim({ w: e.currentTarget.naturalWidth, h: e.currentTarget.naturalHeight });
      }} style={dim ? undefined : { visibility: 'hidden' }} />
    </div>
  );
}
// RUM CLS 归因
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    const sources = e.sources?.map(s => s.node?.nodeName);   // 偏移源元素
    report({ cls: e.value, sources, buildId: window.__BUILD_ID });
  }
}).observe({ type: 'layout-shift', buffered: true });
```
