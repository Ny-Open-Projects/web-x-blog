---
disableNunjucks: true
title: 18-2-4 html2canvas 踩坑修正 bug
date: 2026-11-17 08:30:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节完成了截图的第一步，中间编辑的内容能显示在页面上。最后留下一个问题：html2canvas 设置的宽度是 375px，但截图后实际图片宽度是 750，正好两倍。这不是所有电脑都会出现的，有的同学截图实际就是 375。为什么会结果不同？

## 两类像素

先把像素分成两类：

1. **设备像素**（也叫物理像素）：一听"物理"就知道跟硬件有关，它是显示设备中最微小的物理部件，同一设备中物理像素总数固定。
2. **独立像素**（CSS 像素）：相对的概念，抽象单位，主要用在浏览器上精确度量 web 页面内容，也叫 device independent pixels，简称 DIPS。

在标准显示密度下，一个 CSS 像素对应一个设备像素，一比一。

## devicePixelRatio

有了这个前提，可以引出 window 上的变量 **devicePixelRatio**：它返回当前显示设备的物理像素分辨率与 CSS 像素分辨率之比。说白了，它告诉浏览器应该用多少屏幕实际像素来绘制单个 CSS 像素。标准密度下它为 1。

但有特例，视网膜显示屏（Retina，比如 MacBook），它用更多的屏幕像素绘制相同对象以获得更清晰的图像，devicePixelRatio 是 2。打开 console 直接输出 `window.devicePixelRatio`，可以看到是 2。

这就是答案：中间元素的 CSS 尺寸是 375px，但 Apple 是视网膜屏，用两倍于 CSS 尺寸的设备像素渲染它，所以图片宽 750px。非视网膜屏一比一，截图就是 375px。

html2canvas 允许改变这个对应关系，options 里的 **scale** 属性控制图片缩放，默认取 window.devicePixelRatio（也就是 2）。直接改成 1，点击发布，图片真实像素宽度变成 375px。

## 三个 bug 的修复

scale 改成 1 后冒出几个新问题，正好逐一踩掉。

**bug 一：黑色区域。** 所有框的地方出现了灰色黑色区域，这是 html2canvas 的经典大坑。原因：元素上有 box-shadow 属性，它不支持 box-shadow 的渲染，即使这个属性没有任何有意义的值，只要存在就会出问题。修复方式是截图时给画布添加一个类，暂时覆盖掉 box-shadow：创建临时状态 canvasFix，初始 false，截图开始时置 true。特别注意要**等 DOM 更新结束再截图**，效果才能上去，所以要加 async/await，从 vue 引入 nextTick，在截图前 `await nextTick()`。样式添加在最下面：有这个类时，edit-wrapper 下面所有元素的 box-shadow 都删除。画布区域用动态对象绑定 `{ canvasFix: canvasFix }`（记得把 canvasFix 返回出去）。刷新点击发布，黑色框消失。

**bug 二：蓝色选中框。** 截图时如果选中了元素，蓝色的框也会被截进去。修起来很简单：截图最开始 remove 选中元素，`store.commit('setActiveElement', '')` 置空即可。

**bug 三：截图不完整。** 图片很长时只能截取一部分。原因是元素上加了特殊样式：position: fixed 加 max-height: 80vh，超出高度的内容靠内部滚动，截图自然不完整。修复同样是截图时暂时消除规则：添加类似的样式覆盖，把 position 换成 absolute，max-height 设成 none。

测试：故意把区域只设置一半高度，点击发布，截图完整了，选中框消失，黑框问题也没了，三个 bug 全部解决，截图看起来很完美。

最后别忘了一个小收尾：截图结束后把 `canvasFix.value = false` 复原回来。这节就是 html2canvas 的踩坑之旅，这些坑是很多人使用时都会遇到的经典 bug，搞定它们就可以愉快地完成截图工作了。
