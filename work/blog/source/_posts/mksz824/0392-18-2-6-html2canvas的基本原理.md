---
disableNunjucks: true
title: 18-2-6 html2canvas的基本原理
date: 2026-11-17 10:32:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

html2canvas 的源代码有几千行，结构虽整齐（用 TS 写的），整体逻辑却非常复杂，所以不用源码讲解，而是用一个简单的例子浅显易懂地讲一下原理。

## 目标与 Canvas 的能力

先明确目的：希望有一个 Canvas 元素，上面绘制了一系列 HTML 节点。要把 DOM 节点绘制到 Canvas 上，就得把 DOM 节点中的信息原封不动地拷贝过去。而 Canvas 只是一张画布，没法在上面添加具体的 HTML 节点，只能在上面填充形状或绘制已有的图形。

先了解一下 Canvas：通过 `canvas.getContext('2d')` 拿到 2D 渲染上下文（CanvasRenderingContext2D），就可以在上面绘制图形了。它有非常多 API，绘制矩形、文本、线型等等，但其中最关键的是 **drawImage**：把一张图像绘制到 canvas 画布上。

于是问题变成：怎样把一个 DOM 节点变成一张可以被绘制的图像？

## 关键角色：SVG 与 foreignObject

DOM 本身是 HTML 代码，由特殊标签组成的元素。此时想到另一种和 HTML 结构非常类似的格式：**SVG**，可缩放矢量图形，一种描述二维矢量图形的格式，特别注意它是基于 XML 的标记语言，结构上和 HTML 很像。那能否把 HTML 代码写进 SVG？答案是肯定的，靠一个神奇的元素：**foreignObject**。

看它的文档：foreignObject 元素允许包含来自不同 XML 命空间的元素，在浏览器的上下文中，很可能就是 HTML 代码。文档示例先创建一个 SVG 元素，用一系列坐标生成一个黑色多边形，然后 foreignObject 设定坐标和长宽，里面放了一段非常熟悉的 HTML（一长串文字），最终效果就是黑色矩形上面显示了一系列 HTML 元素。这就是解决问题的关键。注意它是新版浏览器才支持的特性，IE 理所当然不支持。

## 解题思路

两个前提齐备，思路就明确了：

1. 创建一个 canvas 元素；
2. 创建 SVG 文件，用我们已经用过多次的 Blob 构造函数；SVG 中先填充一个 foreignObject，再把我们想复制的 DOM 的 innerHTML 原封不动放进去，这样就能画出类似上面的图形；
3. 创建一个 image 标签，drawImage 需要一张图像才能绘制。image 的 src 使用静态方法 `URL.createObjectURL`，它可以生成一个内存中存储文件的 URL；
4. image 加载完毕后（load 事件），调用 canvas 的 drawImage，把图片绘制到画布上。

解题关键就是 foreignObject 这个特性。有了这个大体思路，下节就可以编码验证，看看能否完成这个看起来很复杂的任务。
