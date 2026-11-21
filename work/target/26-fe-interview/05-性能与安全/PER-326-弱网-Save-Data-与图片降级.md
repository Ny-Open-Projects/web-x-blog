---
title: [PER-326] 用户开启 Save-Data 省流模式后，前端应该做什么？图片与接口的降级矩阵？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-326：用户开启 Save-Data 省流模式后，前端应该做什么？图片与接口的降级矩阵？

**答**：
- 信号：`navigator.connection.saveData === true`（Chrome/Android WebView）；HTTP 头 `Save-Data: on`（服务端也可感知）。语义是"用户主动要求省流量"——不是猜测，必须尊重。
- 降级矩阵：图片——首屏保留必要图但降到预览分辨率/强压缩格式，列表页用 LQIP 占位图、点击加载原图；视频——不自动播放、默认 360p、封面替代；字体——跳过自定义 webfont 用系统字体；JS——禁用非关键 prefetch/prefetch 数据、三方 SDK 全部延迟；轮询——间隔拉长。
- 服务端配合：`Save-Data` 头透传到 BFF，接口瘦身（砍非核心字段、合并分页）；CDN 按头返回低清资源（Vary: Save-Data 注意缓存分键）。
- 度量：saveData 用户占比上报（决定降级投入优先级）；降级后这些用户的 LCP/流量消耗对比，验证降级有效性且不伤转化。

```html
<!-- CSS 侧识别 saveData -->
<img src="cover-preview.avif" data-full="cover.avif" alt="">
```
```javascript
const saveData = navigator.connection?.saveData ?? false;
document.querySelectorAll('img[data-full]').forEach((img) => {
  if (!saveData) {
    const full = new Image();                          // 非省流：后台换高清
    full.src = img.dataset.full;
    full.onload = () => { img.src = full.src; };
  }
});
// 服务端（Express）：
app.use((req, res, next) => { req.saveData = req.get('save-data') === 'on';
  res.set('Vary', [res.get('Vary'), 'Save-Data'].filter(Boolean).join(', ')); next(); });
// req.saveData ? 瘦身响应 : 完整响应
```
