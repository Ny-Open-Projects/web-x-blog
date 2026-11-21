---
title: [MFW-276] 同构 Date/Time 与时区陷阱（SSR-CSR 渲染不一致）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-276：同构时区陷阱

**答**:
- 经典不一致：服务端 UTC 渲染「3:00」+ 客户端本地时区（UTC+8）渲染「11:00」——hydration mismatch 警告 + 闪变
- 治理三选一：①统一 UTC 显示 + 本地换算提示（「你的时区 11:00」客户端补充渲染——suppressHydration 包住该节点）②服务端按用户时区渲染（时区存 profile/cookie——首屏即正确，代价是服务端 Intl 计算与缓存 key 含 tz）③时间戳传输、客户端专责渲染（时间组件 client-only——最简单可靠）
- 细节：Date 序列化（ISO 字符串跨边界安全；Date 对象经 RSC 可传但时区语义仍按显示端决定）——「存储 UTC、显示端决定、渲染位置声明」三句话纪律

```javascript
// 方案三：时间戳传输 + client-only 渲染
// RSC: <Time ts={post.createdAtMs} />        // 只传数字
'use client'
function Time({ ts }) {
  const [t, setT] = useState(null)
  useEffect(() => setT(new Date(ts).toLocaleString()), [ts])   // 客户端决定时区
  return <time suppressHydrationWarning>{t ?? ''}</time>
}
```
