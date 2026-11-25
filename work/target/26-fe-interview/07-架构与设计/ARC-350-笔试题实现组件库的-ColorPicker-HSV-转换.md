---
title: [ARC-350] 笔试题：实现组件库的 ColorPicker HSV 转换？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-350：笔试题：实现组件库的 ColorPicker HSV 转换？
**答**：实现 ColorPicker 的核心颜色引擎：1) HSV ↔ Hex/RGB 互转（函数正确性）；2) 面板选色：点击/拖动映射到 s/v（0~1）；3) hue 条映射 0~360；4) 输出格式切换（hex/rgb/hsl 任一）。
**评分点**：
- 转换公式正确（重点 HSV→RGB 分段计算）。
- 拖动映射正确（clientX/width clamp 到 0~1，s=右为满、v=上为满）。
- hue 独立维度（面板底色随 hue 变化）。
- 输出格式化正确（hex 补零）。
```tsx
function hsv2rgb(h: number, s: number, v: number) {                  // 1) 核心转换
  const c = v * s, x = c * (1 - Math.abs(((h / 60) % 2) - 1)), m = v - c;
  const seg = Math.floor(h / 60) % 6;
  const rgb = [[c, x, 0], [x, c, 0], [0, c, x], [0, x, c], [x, 0, c], [c, 0, x]][seg];
  return rgb.map(n => Math.round((n + m) * 255));
}
function toHex(r: number, g: number, b: number) {
  return '#' + [r, g, b].map(n => n.toString(16).padStart(2, '0')).join('');   // 补零
}
function ColorPicker({ value, onChange }) {
  const [hsv, setHsv] = useState({ h: 210, s: 1, v: 1 });
  const areaRef = useRef<HTMLDivElement>(null);
  const onArea = (e: React.PointerEvent) => {                        // 2) 面板映射
    const rect = areaRef.current!.getBoundingClientRect();
    const s = Math.min(1, Math.max(0, (e.clientX - rect.left) / rect.width));
    const v = 1 - Math.min(1, Math.max(0, (e.clientY - rect.top) / rect.height));
    const next = { ...hsv, s, v };
    setHsv(next);
    const [r, g, b] = hsv2rgb(next.h, next.s, next.v);
    onChange(toHex(r, g, b));                                        // 4) hex 输出
  };
  const [r, g, b] = hsv2rgb(hsv.h, hsv.s, hsv.v);
  return <div>
    <div ref={areaRef} onPointerDown={onArea}
      style={{ background: `linear-gradient(to top, #000, transparent), linear-gradient(to right, #fff, hsl(${hsv.h} 100% 50%))`, height: 160 }}/> {/* 3) hue 决定底色 */}
    <input type="range" min={0} max={360} value={hsv.h}
      onChange={e => { const next = { ...hsv, h: +e.target.value }; setHsv(next);
        const [r2, g2, b2] = hsv2rgb(next.h, next.s, next.v); onChange(toHex(r2, g2, b2)); }}/>
  </div>;
}
```
