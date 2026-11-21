---
title: [H5-322] 笔试：手写 visualViewport 键盘避让
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, 移动端]
type: 笔试题
---

## H5-322：笔试：手写 visualViewport 键盘避让

**题目**：实现聊天页输入框键盘避让：键盘弹出时输入框贴在键盘上方；键盘收起恢复原位；同时内容区高度 = 可视高度（不被键盘遮挡）。兼容无 visualViewport 的环境（降级 focus/blur + setTimeout）。

**答**：
```javascript
function keyboardAvoid(composer, contentArea) {
  const vv = window.visualViewport;
  if (vv) {
    const onResize = () => {
      const kb = window.innerHeight - vv.height - vv.offsetTop; // 键盘高度
      const height = vv.height;
      contentArea.style.height = height + 'px';
      composer.style.transform = `translateY(-${Math.max(0, kb)}px)`;
    };
    vv.addEventListener('resize', onResize);
    vv.addEventListener('scroll', onResize); // iOS 页面被顶起时 offsetTop 变化
    return { destroy: () => { vv.removeEventListener('resize', onResize); vv.removeEventListener('scroll', onResize); } };
  }
  // 降级：focus/blur 估计
  const input = composer.querySelector('input');
  input.addEventListener('focus', () => setTimeout(() => {
    composer.style.transform = `translateY(-${(window.innerHeight * 0.4)}px)`; // 估键盘高度
  }, 300));
  input.addEventListener('blur', () => (composer.style.transform = ''));
}
```

**评分点**：
- 键盘高度 = innerHeight - vv.height - vv.offsetTop（完整公式，漏 offsetTop 在 iOS 会错）
- resize 与 scroll 双事件监听（iOS 顶起方式不同）
- 无 vv 环境的降级路径
- destroy 清理监听
