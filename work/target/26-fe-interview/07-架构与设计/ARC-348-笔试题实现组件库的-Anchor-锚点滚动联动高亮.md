---
title: [ARC-348] 笔试题：实现组件库的 Anchor 锚点滚动联动高亮？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-348：笔试题：实现组件库的 Anchor 锚点滚动联动高亮？
**题目**：实现 Anchor 目录组件：1) 滚动监听高亮当前区块（取"最后一个 top ≤ 阈值"的锚点）；2) scroll 监听 rAF 节流 + Passive；3) 点击平滑滚动（考虑 sticky header 偏移 offsetTop 配置）；4) 目标元素动态增删时重新收集锚点。
**评分点**：
- 高亮算法正确（当前激活 = 最后一个满足 getBoundingClientRect().top - offset ≤ 0 的锚点）。
- rAF 节流 + passive 监听，性能意识。
- 平滑滚动 offset 处理正确（scrollTo top = el.offsetTop - offset，scroll-margin-top 亦可）。
- MutationObserver/依赖数组重收集锚点。
```tsx
function Anchor({ links, offset = 80 }) {
  const [active, setActive] = useState(links[0]?.id);
  useEffect(() => {
    let raf = 0;
    const onScroll = () => {                                        // 2) rAF 节流
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        let cur = links[0]?.id;
        for (const l of links) {
          const el = document.getElementById(l.id);
          if (el && el.getBoundingClientRect().top - offset <= 0) cur = l.id;  // 1) 最后一个过线者
        }
        setActive(cur);
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true }); // passive
    onScroll();
    return () => { window.removeEventListener('scroll', onScroll); cancelAnimationFrame(raf); };
  }, [links, offset]);
  const jump = (id: string) => {
    const el = document.getElementById(id);
    el?.scrollTo ? window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - offset,
      behavior: 'smooth' }) : null;                                 // 3) header 偏移
  };
  return <nav className="anchor">
    {links.map(l => <a key={l.id} className={l.id === active ? 'on' : ''}
      onClick={e => { e.preventDefault(); jump(l.id); }} href={`#${l.id}`}>{l.title}</a>)}
  </nav>;
}
// 4) 动态锚点：调用方 links 来自状态（如 docs 章节异步加载完成更新 links → effect 重收集）
```
