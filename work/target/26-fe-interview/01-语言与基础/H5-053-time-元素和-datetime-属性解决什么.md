---
title: [H5-053] time 元素和 datetime 属性解决什么问题？什么时候必须写 datetime？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-053：time 元素和 datetime 属性解决什么问题？什么时候必须写 datetime？
**答**：
- `<time>` 把人类可读的时间文本和机器可读的 ISO 8601 值绑定，方便爬虫、日历、搜索引擎提取结构化时间。
- 元素内文本格式随意（"昨天""3 天前"），但必须是**有效的时间/日期语义**；机器值交给 `datetime` 属性。
- 当元素内容不是合法的机器格式（如"3 天前"）时，`datetime` **必填**；内容本身是合法格式时可省略。
- 支持日期、时间、时长（时长加 `PT2H30M` 前缀）；无效值如 `<time>2026-13-01</time>` 不是合法 time 元素。
- 常见坑：发布时间建议同时给 `<time datetime="2026-11-07T09:00+08:00">` 带时区，避免解析歧义。

```html
<!-- 内容即机器格式，datetime 可省略 -->
<time>2026-11-07</time>
<time>09:30</time>

<!-- 相对时间：文本随意，datetime 必填 -->
<time datetime="2026-11-04">3 天前</time>
<time datetime="2026-11-07T09:00+08:00">今天上午</time>

<!-- 时长写法：PT 前缀，2 小时 30 分 -->
<time datetime="PT2H30M">两个半小时</time>

<script>
  // 爬虫/脚本视角：一条语句拿走页面全部机器可读时间
  const times = [...document.querySelectorAll('time[datetime]')]
    .map(el => ({ raw: el.textContent, iso: el.dateTime }));
  console.log(times); // [{raw: '3 天前', iso: '2026-11-04'}, ...]
</script>
```
