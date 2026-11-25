---
title: [AIC-651] 大促前 AI 生成代码的性能回归怎么专项检查？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-651：大促前 AI 生成代码的性能回归怎么专项检查？

**答**：
- 结论先行：**AI 生成代码的性能问题常藏在「看起来合理」的写法里（列表里重复计算、大对象深拷贝、useEffect 依赖不当导致重渲染），专项检查要盯这些高频模式，而非泛泛跑分**（AIC-578 重渲染检测）。
- 高频性能反模式：1) **渲染循环里做重计算**：`items.map(item => heavyTransform(item))` 每次渲染重算，应 useMemo；2) **不必要的深拷贝**：`JSON.parse(JSON.stringify(data))` 在大促数据量下是灾难；3) **全局状态订阅过宽**：组件订阅了整个 store，任何变更都重渲染；4) **图片/资源无懒加载**：大促页面素材多，首屏爆炸。
- 专项检查手法：1) **静态扫描**：ESLint 插件 + 自定义规则扫上述反模式；2) **数据放大测试**：用 10 倍真实数据量跑 AI 生成的关键路径，看是否线性劣化（AIC-366 性能预算）；3) **火焰图对比**：改动前后录 profile，对比耗时热点；4) **包体积 diff**：AI 引入新依赖或大段代码使 bundle 膨胀要告警。
- 大促特殊性：平时 100 条数据没问题，大促 10 万条就崩——**必须用真实峰值数据量验证，不能用开发环境的玩具数据**。
- 追问钩子：为什么「数据放大测试」比「代码审查」更能发现性能问题？——因为性能是运行时特性，光看代码很难判断「这个 map 在 10 万条时会不会卡」；用放大数据实测，瓶颈自己暴露——把「推测」变成「测量」。

```typescript
function checkPerfAntipatterns(code: string): string[] {
  const patterns = [
    { re: /\.map\([^)]*\)\.filter\(/, msg: '链式map+filter可能产生中间数组，考虑单次reduce' },
    { re: /JSON\.parse\(JSON\.stringify\(/, msg: '深拷贝在大对象上是性能杀手' },
    { re: /useEffect\([^,]+,\s*\[\]\)/, msg: '空依赖useEffect确认是否漏依赖' },
    { re: /<img(?![^>]*loading)/, msg: '图片缺少loading="lazy"' },
  ];
  return patterns.filter(p => p.re.test(code)).map(p => p.msg);
}

const code = `
const data = JSON.parse(JSON.stringify(raw));
const result = items.map(f).filter(Boolean);
return <img src={url} />`;
console.log(checkPerfAntipatterns(code).length >= 3); // 深拷贝 + 链式 + 图片
```
