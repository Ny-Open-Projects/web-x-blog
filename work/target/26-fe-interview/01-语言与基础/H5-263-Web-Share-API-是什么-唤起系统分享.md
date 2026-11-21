---
title: [H5-263] Web Share API 是什么：唤起系统分享
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-263：Web Share API 是什么：唤起系统分享

**答**：
- `navigator.share({ title, text, url, files })`：唤起系统级分享面板，可分享到任意已装 App（微信/微博/系统剪贴板等）
- 与复制链接方案的区别：原生分享面板包含用户设备上的所有分享目标，转化率高于「复制链接去粘贴」
- 条件：必须 https、必须用户手势触发；files 分享需要 `navigator.canShare({ files })` 检测
- Web Share Target（反向）：已安装 PWA 可注册为分享接收方（manifest 里声明 share_target），被其他 App 分享进来
- 降级链：不支持时退回「复制链接 + toast」，行为逻辑分支要写全

```javascript
shareBtn.onclick = async () => {
  const data = { title: '好文推荐', text: '分享给你', url: location.href };
  if (navigator.share) {
    try { await navigator.share(data); report({ share: 'ok' }); }
    catch (e) { /* 用户取消不算错误 */ }
  } else {
    await navigator.clipboard.writeText(data.url);
    toast('链接已复制，去粘贴给朋友吧');
  }
};
```
