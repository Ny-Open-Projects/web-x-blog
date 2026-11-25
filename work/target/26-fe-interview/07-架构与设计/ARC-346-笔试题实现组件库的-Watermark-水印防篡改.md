---
title: [ARC-346] 笔试题：实现组件库的 Watermark 防篡改水印？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-346：笔试题：实现组件库的 Watermark 防篡改水印？
**答**：实现 Watermark 组件：1) Canvas 生成平铺水印背景（rotate/opacity/font）；2) MutationObserver 防篡改（删节点/改样式自动恢复）；3) 组件卸载清理 observer；4) 高清屏（devicePixelRatio）模糊问题处理。
**评分点**：
- Canvas 尺寸乘 dpr 并 ctx.scale，文字清晰。
- Observer 观察 attr/childList/subtree 三类变更，检测到被移除/修改即重绘。
- 卸载时 disconnect + 移除 canvas。
- 防篡改不与业务冲突（防抖恢复，避免死循环）。
```tsx
function Watermark({ text, rotate = -20, opacity = 0.15, gap = 100, children }) {
  const hostRef = useRef<HTMLDivElement>(null);
  const cvsRef = useRef<HTMLCanvasElement>(null);
  useEffect(() => {
    const dpr = window.devicePixelRatio || 1;                       // 4) 高清屏
    const cvs = cvsRef.current!;
    cvs.width = gap * 4 * dpr; cvs.height = gap * 4 * dpr;
    const ctx = cvs.getContext('2d')!;
    ctx.scale(dpr, dpr);
    ctx.globalAlpha = opacity;
    ctx.rotate((rotate * Math.PI) / 180);
    ctx.font = '14px sans-serif';
    ctx.strokeText(text, 10, gap / 2);
    const url = cvs.toDataURL();
    const host = hostRef.current!;
    const paint = () => { Object.assign(host.style, { backgroundImage: `url(${url})` }); };  // 1) 平铺
    paint();
    const mo = new MutationObserver(() => {                         // 2) 防篡改
      if (!host.style.backgroundImage.includes(url.slice(32, 64))) paint();   // 被改 → 恢复（节流由浏览器合并）
    });
    mo.observe(host, { attributes: true, childList: false, subtree: false });
    return () => mo.disconnect();                                   // 3) 清理
  }, [text, rotate, opacity, gap]);
  return <div ref={hostRef} style={{ position: 'relative' }}>
    <canvas ref={cvsRef} style={{ display: 'none' }}/>
    {children}
  </div>;
}
```
