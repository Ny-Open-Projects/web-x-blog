---
title: [DP-225] 源码识别：date-fns/Lodash 源码中的函数组合与选项对象？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-225：源码识别：date-fns/Lodash 源码中的函数组合与选项对象？
**答**：
- 策略+参数化：date-fns 每个 format/token 是独立策略（xx 解析月、xxxx 解析年），locale 是注入的适配器（各语言 token 表）。
- 选项对象模式：options { weekStartsOn, locale, ... } 统一入口——可变部分收敛成一个对象参数（对比位置参数的扩展性灾难）。
- 函数组合：date-fns/fp 版自动柯里化（compose(isWeekend, addDays(1))），Lodash 的 chain 是组合的流式封装。
- 识别要点：date-fns 的树摇依赖"一函数一文件一纯函数"——无副作用设计让策略单元可被独立消费（对比 moment 全局单例的体积灾难）。

```javascript
// date-fns 源码级简化：format = token 策略分发 + locale 适配
function format(date, fmtStr, { locale = enUS, weekStartsOn = 0 } = {}) {
  return fmtStr.replace(/(yyyy|MM|dd|HH|mm|ss|E+)/g, (token) => {
    const formatter = locale.formatters[token] ?? defaultFormatters[token];  // locale 适配器
    return formatter(date, { weekStartsOn });
  });
}
// fp 组合：
const { compose, addDays, isWeekend } = dateFnsFp;
const nextWorkday = compose(findNextWorkday, addDays(1));
// 树摇：import format from 'date-fns/format' —— 纯函数单文件，无全局副作用，构建器可精准裁剪
```
