---
title: [PER-618] 点击劫持的新变种有哪些？除了 X-Frame-Options，现代防御组合是什么？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-618：点击劫持的新变种有哪些？除了 X-Frame-Options，现代防御组合是什么？

**答**：
- 变种一族：**likejacking**（诱导点赞）、**拖放劫持**（drag-drop 把敏感内容拖到攻击者 iframe）、**跨域 iframe 嵌套劫持**（多层嵌套绕 Frame 检测）、**不透明层+透明度渐变**（鼠标跟随动画让用户以为点的是可见层）、**利用 tabindex 的键盘劫持**（不嵌 iframe，靠焦点顺序让盲打密码落到攻击者输入框）。
- 现代防御组合：`X-Frame-Options: DENY/SAMEORIGIN`（老标准，只管 frame 嵌套）+ **CSP `frame-ancestors 'none'`**（CSP2+，粒度更细可按 origin 放行）+ **`frame-src`/`object-src` 控制自己嵌别人** + 敏感操作二次确认（验证码/重输密码）+ JS 断帧脚本兜底（`self !== top` 时报警）。
- 交互类防御：拖放劫持要 `event.dataTransfer` 敏感数据限制 + drop 目标校验；键盘劫持要敏感输入框 blur 时清空或用系统级输入（如支付密码控件）。
- 检测：上线前用嵌入测试页验证 frame-ancestors 是否真的拦截（配置写错不报错，只是不生效）。

```javascript

// 多层防御配置与断帧兜底
const clickjackingDefense = {
  headers: {
    'X-Frame-Options': 'DENY',
    'Content-Security-Policy': "frame-ancestors 'none'; frame-src 'self'",
  },
  js: `if (self !== top) { top.location = self.location; }`,  // 断帧兜底（CSP 失效时）
  ux: {
    sensitiveAction: '二次确认（重输密码/验证码）',
    drag: 'dataTransfer 敏感字段过滤 + drop 目标白名单',
    focus: '密码框 blur 清空，敏感输入用系统安全控件',
  },
};
// 嵌入测试（必须真实验证，配置写错不报错）：
// <iframe src="https://target.example.com"></iframe> -> 应被拒绝加载
```
