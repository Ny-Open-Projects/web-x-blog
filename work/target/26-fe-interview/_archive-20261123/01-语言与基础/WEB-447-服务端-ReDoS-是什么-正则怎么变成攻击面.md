---
title: [WEB-447] 服务端 ReDoS 是什么，正则怎么变成攻击面
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-447：服务端 ReDoS 是什么，正则怎么变成攻击面

**答**：
- ReDoS：构造特定输入让正则回溯爆炸，一条请求耗尽 CPU，服务近乎瘫痪
- 高危模式：嵌套量词 `(a+)+`、`(a|a)*`、含可选分组的连环量词 `(.*a){20}`
- 攻击入口：任何「用户输入进正则」的地方——搜索关键词、URL 路由匹配、日志过滤、表单校验
- 防御：输入长度上限（如 200 字符内必胜）、审查正则回溯风险、用线性时间引擎（RE2、REXML、safe-regex 审查工具）
- 前端也存在 ReDoS（主线程卡死），但影响面通常是小；服务端那条才是事故级

```javascript
// 危险正则示例与安全改写
const bad  = /^(\w+\s?)*$/;                  // 嵌套量词，输入 "a a a a a a ! " 会爆炸
const good = /^\w+(\s?\w+)*$/;               // 线性，且先做长度校验
function check(input) {
  if (input.length > 100) return false;      // 长度闸门优先
  return good.test(input);
}
```
