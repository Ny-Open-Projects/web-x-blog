---
title: [DP-235] 源码识别：CSS-in-JS 库源码中的备忘录与适配器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-235：源码识别：CSS-in-JS 库（emotion/styled-components）源码模式？
**答**：
- 备忘录（核心性能设计）：样式字符串 + props → 生成 className 有一张 hash 缓存（serializedMap），同输入同 class 复用已插入的 style 标签——不重复注入。
- 适配器：styled.div / css / createGlobalStyle 是同序列化引擎的多个入口适配；babel 宏做静态提取。
- 策略：运行时注入（动态主题便利）vs 构建期提取（零运行时，linaria/panda 风格）是两条策略路线。
- 识别要点：能说出"className 稳定性"问题——序列化 hash 受 props 影响，不稳定 props（函数/对象字面量）会导致 class 膨胀。

```javascript
// emotion 序列化缓存（源码级简化）
const cache = new Map();                     // serialized → className
function serialize(styles, props) {
  const parts = styles.map(s => typeof s === 'function' ? s(props) : s);   // 插值策略
  const key = parts.join('');
  let cls = cache.get(key);
  if (!cls) {                                // 备忘录：同输入只注入一次
    cls = `css-${hash(key)}`;
    insertRule(`.${cls}{${key}}`);
    cache.set(key, cls);
  }
  return cls;
}
function styled(Tag, styles) { return function Styled(props) {
  return <Tag {...props} className={[props.className, serialize(styles, props)].join(' ')}/>;
}; }
// 稳定性：styles 中 props.theme 变化 → 新 hash → 新 class（旧 class 残留在缓存 → 策略是 LRU 清理）
```
