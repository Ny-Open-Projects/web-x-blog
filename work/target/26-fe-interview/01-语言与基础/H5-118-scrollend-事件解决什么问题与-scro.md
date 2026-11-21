---
title: [H5-118] scrollend 事件解决什么问题？与 scroll + debounce 的差别？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-118：scrollend 事件解决什么问题？与 scroll + debounce 的差别？
**答**：
- `scroll` 是高频过程事件，"滚动停止"只能靠 debounce 猜测；`scrollend` 是浏览器**官方定义的停止时机**，语义准确、无抖动误判（如惯性滚动、轨道板）。
- 支持前降级：`'onscrollend' in window` 检测，不支持时回退防抖方案；Chrome 114+、Firefox 109+ 已支持。
- 典型场景：轮播翻页后加载对应数据、滚动监听埋点停止上报、无限滚动防抖加载、滚动吸附后的高亮同步。
- 注意 scrollend 不区分"用户停止"与"代码 scrollTo 停止"（都会触发）；需要区分时打标 flag。
- 与 CSS scroll-snap 组合：snap 结束即 scrollend，做"对齐后记录索引"最省事。

```javascript
const scroller = document.getElementById('carousel');

function loadSlide(index) { console.log('加载幻灯片数据：', index); }

if ('onscrollend' in window) {
  // 原生停止事件：无需猜测
  scroller.addEventListener('scrollend', () => {
    const idx = Math.round(scroller.scrollLeft / scroller.clientWidth);
    loadSlide(idx);
  });
} else {
  // 降级：scroll + 防抖
  let timer;
  scroller.addEventListener('scroll', () => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      const idx = Math.round(scroller.scrollLeft / scroller.clientWidth);
      loadSlide(idx);
    }, 120);
  }, { passive: true });
}

// 程序滚动也会触发 scrollend：用 flag 区分人为触发
let programmatic = false;
function scrollToSlide(i) {
  programmatic = true;
  scroller.scrollTo({ left: i * scroller.clientWidth, behavior: 'smooth' });
}
scroller.addEventListener('scrollend', () => {
  if (programmatic) { programmatic = false; return; }
  track('user-scroll-stop');
});
```
