---
title: [WEB-116] IntersectionObserver 的参数怎么用？rootMargin 和 threshold 各控制什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-116：IntersectionObserver 的参数怎么用？rootMargin 和 threshold 各控制什么？
**答**：
- `root`：交叉判定的参照容器，null 即视口；`rootMargin` 在参照框外扩/内收缩判定区，"200px" 提前 200px 触发，实现预加载。
- `threshold` 是交叉比例数组（0~1）：`[0]` 一进入就回调，`[0.5]` 一半可见时再回调，`[0, 0.5, 1]` 可做曝光深度打点。
- 回调是异步批量派发，不阻塞滚动；`entry.isIntersecting` 与 `intersectionRatio` 是主判定，首次 observe 必回调一次初始状态。
- 注意与 scroll 监听的本质区别：IO 由引擎在合成管线里判定，不进主线程逐帧循环，性能高一个量级。

```javascript
// 懒加载 + 曝光打点的标准配置
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => {
    if (!en.isIntersecting) return;
    if (en.target.dataset.src) {
      en.target.src = en.target.dataset.src;  // 进入判定区才加载
      io.unobserve(en.target);                // 一次性需求记得解除
    } else {
      track(`曝光 ratio=${en.intersectionRatio.toFixed(2)}`);
    }
  });
}, {
  root: null,               // 视口为参照
  rootMargin: '200px 0px 200px 0px', // 上下外扩 200px，提前预加载
  threshold: [0, 0.5, 1],   // 进入、半屏、全屏三个档位各回调一次
});
document.querySelectorAll('img[data-src], .exposure').forEach((el) => io.observe(el));
```
