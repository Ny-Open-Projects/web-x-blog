---
title: [MP-293] 笔试：手写 WXS 格式化工具集（时间/金额/状态）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-293：笔试：手写 WXS 工具集
**题**：编写 fmt.wxs：formatRelativeTime(ts, now)（1 分钟内「刚刚」、1h 内「N 分钟前」、24h 内「N 小时前」、7 天内「N 天前」、更久 MM-DD）；formatMoney(fen)（分转元，保留两位）；getStatusText(code)（枚举映射）。注意 WXS 是 ES5 子集（无模板字符串/箭头函数）。

```javascript
// fmt.wxs
function pad(n) { return n < 10 ? '0' + n : '' + n }
function formatRelativeTime(ts, now) {
  var diff = Math.floor((now - ts) / 1000)
  if (diff < 60) return '刚刚'
  if (diff < 3600) return Math.floor(diff / 60) + '分钟前'
  if (diff < 86400) return Math.floor(diff / 3600) + '小时前'
  if (diff < 604800) return Math.floor(diff / 86400) + '天前'
  var d = getDate(ts)
  return pad(d.getMonth() + 1) + '-' + pad(d.getDate())
}
function formatMoney(fen) {
  var yuan = Math.floor(fen / 100)
  var rest = Math.abs(fen % 100)
  return yuan + '.' + (rest < 10 ? '0' + rest : '' + rest)
}
var STATUS = { 0: '待支付', 1: '已支付', 2: '已发货', 3: '已完成' }
function getStatusText(code) { return STATUS[code] || '未知' }
module.exports = { formatRelativeTime: formatRelativeTime, formatMoney: formatMoney, getStatusText: getStatusText }
```
**评分点**：
- WXS ES5 语法合规（var/function，无模板字符串）。
- getDate 是 WXS 内建（不是 new Date）——高频考点。
- 分转元整数运算避免浮点误差。
- module.exports 导出、WXML 中 <wxs module="fmt"> 用法说明。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-43d10973-ee48-4d7a-acd2-392128e7b510-cwd'; fi
exit "$__zcode_status"
