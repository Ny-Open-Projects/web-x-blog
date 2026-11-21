---
title: [DP-023] 组件的"默认配置合并"（options 模式）怎么设计？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-023：组件的"默认配置合并"（options 模式）怎么设计？
**答**：
- options 模式：对外只暴露一个大配置对象（而非一长串参数），内部与默认值合并——组件库 API 的标配。
- 关键实现：一层浅合并不够（嵌套对象被整体覆盖），需要 deepMerge 或分组合并。
- 加分点：默认值函数化（依赖其他配置）、`undefined` 不覆盖默认值、合并结果冻结防污染。
- 与建造者的关系：options 是"声明式一次给出"，builder 是"过程式分步构建"，复杂场景可 options 起步、builder 演进。

```javascript
// 组件库风格的 options 合并
const MODAL_DEFAULTS = {
  title: '提示',
  visible: false,
  maskClosable: true,
  style: { width: 420, top: 100 },
  onOk: null,
};

class Modal {
  constructor(options = {}) {
    // 分组深合并：浅合并会丢掉 style.fontSize 这类嵌套字段
    const o = {
      ...MODAL_DEFAULTS,
      ...options,
      style: { ...MODAL_DEFAULTS.style, ...(options.style || {}) }, // 嵌套层单独合并
    };
    // 默认值派生：可依赖其他配置
    if (o.width) o.style.width = o.width;
    Object.freeze(o); // 冻结，防止运行时篡改共享默认值
    this.opts = o;
  }
}
const m1 = new Modal({ title: '登录', style: { top: 200 } });
const m2 = new Modal();
console.log(m1.opts.style.top, m1.opts.style.width); // 200 420 —— 合并正确
console.log(m2.opts.title, m2.opts.style.top);       // 提示 100 —— 默认值未被污染
console.log(Object.isFrozen(m1.opts));               // true

// 默认值函数化：值依赖其他配置时用工厂
function createChartOptions(user = {}) {
  const isDark = user.theme === 'dark';
  return {
    theme: user.theme ?? 'light',
    colors: user.colors ?? (isDark ? ['#4ec9b0'] : ['#5470c6']), // 派生默认值
    legend: { show: user.legend?.show ?? true },
  };
}
console.log(createChartOptions({ theme: 'dark' }).colors); // ['#4ec9b0']
```
