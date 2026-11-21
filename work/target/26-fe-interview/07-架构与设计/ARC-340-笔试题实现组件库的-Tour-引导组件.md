---
title: [ARC-340] 笔试题：实现组件库的 Tour 引导组件？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-340：笔试题：实现组件库的 Tour 引导组件？
**题目**：实现新手引导 Tour：1) 按步骤高亮目标元素（遮罩挖洞效果）；2) 步骤切换滚动目标进入视口；3) 提示卡片自动选方位（目标下方空间不足则上方）；4) 目标元素不存在时跳过该步。
**评分点**：
- 挖洞实现正确（box-shadow 巨大扩散 或 4 块遮罩拼接，rect 动态获取）。
- scrollIntoView + 等待滚动完成再测量（否则位置错）。
- 卡片方位决策含翻转与边缘 clamp。
- 目标缺失容错（跳过并继续，不中断整个 Tour）。
```tsx
function Tour({ steps, open, onClose }) {
  const [cur, setCur] = useState(0);
  const [rect, setRect] = useState<DOMRect | null>(null);
  useEffect(() => {
    if (!open) return;
    const step = steps[cur];
    const el = document.querySelector(step.target);
    if (!el) { setCur(c => c + 1); return; }                    // 4) 跳过缺失目标
    el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    const t = setTimeout(() => setRect(el.getBoundingClientRect()), 350);  // 2) 等滚动完成再测
    return () => clearTimeout(t);
  }, [open, cur]);
  if (!open || !rect) return null;
  const pad = 8;
  const spot = { top: rect.top - pad, left: rect.left - pad,
                 width: rect.width + pad * 2, height: rect.height + pad * 2 };
  const flipUp = rect.bottom + 140 > window.innerHeight;        // 3) 下方空间不足 → 上方
  const cardTop = flipUp ? Math.max(8, rect.top - 150) : Math.min(window.innerHeight - 160, rect.bottom + 10);
  return createPortal(<>
    <div className="tour-mask" style={{ position: 'fixed', inset: 0 }}>
      <div style={{ position: 'fixed', ...spot, boxShadow: '0 0 0 9999px rgba(0,0,0,.5)', borderRadius: 6 }}/> {/* 1) 挖洞 */}
    </div>
    <div className="tour-card" style={{ position: 'fixed', top: cardTop, left: Math.max(8, rect.left) }}>
      {steps[cur].content}
      <button onClick={() => cur < steps.length - 1 ? setCur(cur + 1) : onClose()}>下一步</button>
      <button onClick={onClose}>跳过</button>
    </div>
  </>, document.body);
}
```
