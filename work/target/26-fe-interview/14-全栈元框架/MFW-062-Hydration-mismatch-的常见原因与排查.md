---
title: [MFW-062] Hydration mismatch 的常见原因与排查思路？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-062：Hydration mismatch 的常见原因与排查思路？
**答**：
- 四大高频原因：① 首帧渲染依赖了服务端/客户端不一致的数据（`Date.now()`、随机数、`window.innerWidth`）；② 浏览器插件往 body 里注入 DOM；③ 不合法 HTML 嵌套（`<p>` 里放 `<div>`、`<table>` 里塞组件）导致浏览器解析纠偏；④ 服务端与客户端的条件渲染分支不一致（isMobile 判断时点不同）。
- 排查顺序：看控制台绿色 mismatch 警告里 React 给出的服务端/客户端两棵树的 diff，通常第一个不一致节点就是元凶；再向上找第一次出现布尔/时间条件的地方。
- 修法三板斧：把不确定数据挪到 `useEffect`（首帧渲染占位值）、用 `<supressHydrationWarning>` 局部豁免（仅限文本节点级小差异）、时间类内容全部转成服务端生成好再传下来。
- React 19 的 mismatch 报错会把两边 HTML 直接打出来，比 18 的「443 行」友好得多，面试时能提版本差异是加分项。

```tsx
// 反例：服务端 10:00:00 渲染，客户端 10:00:01 水合 -> 文本必然不同
function Clock() {
  return <span>{new Date().toLocaleTimeString()}</span>; // mismatch!
}

// 正解 1：时间类内容服务端定稿，客户端只接收字符串
async function ClockServer() {
  const now = new Date().toLocaleTimeString('zh-CN', { timeZone: 'Asia/Shanghai' });
  return <span suppressHydrationWarning>{now}</span>;
}

// 正解 2：客户端专属逻辑放 useEffect，首帧渲染一致占位
function ClockClient() {
  const [time, setTime] = useState<string | null>(null);
  useEffect(() => {
    setTime(new Date().toLocaleTimeString()); // 水合之后才更新
    const t = setInterval(() => setTime(new Date().toLocaleTimeString()), 1000);
    return () => clearInterval(t);
  }, []);
  return <span>{time ?? '--:--:--'}</span>; // 服务端与首帧都是 '--:--:--'
}
```
