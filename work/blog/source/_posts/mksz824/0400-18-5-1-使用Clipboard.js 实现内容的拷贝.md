---
disableNunjucks: true
title: 18-5-1 使用Clipboard.js 实现内容的拷贝
date: 2026-11-17 08:40:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

之前我们已经完成了生成二维码的工作，并且支持在添加渠道的时候动态生成。这节课完成另一个功能：点击复制按钮，复制对应的 URL。复制功能听起来很简单，仿佛直接调用一个 API 就能实现，但其实它的实现充满了各种 hack 和技巧。这节课先用第三方库实现，之后简单学习一下它的原理。

我们使用的库是 clipboard.js，它是使用人数最多的把文字复制到剪贴板的工具，star 数达到了三万个，用法简单直接，很受开发者欢迎。安装很简单：`npm install clipboard --save`。特别注意，这个库自带类型文件，安装以后就可以支持 TypeScript。

它的用法可以在文档中看一下，很多指令是添加在 DOM 节点上的。第一步，对于想要复制的值，要给它一个独一无二的节点，也就是添加一个 ID。我们想复制的值是 input 的内容，所以给它加一个动态 ID，用模板字符串：`channel-url-${channel.id}`。

第二步，在触发复制的地方添加一个特殊的自定义 data 属性。触发点在复制按钮上，要添加的属性是 data-clipboard-target。data 开头加连字符是自定义 data 属性，里面可以存放任意的属性。把属性粘贴到按钮位置，注意要加冒号，因为后面还要用模板字符串，值是 `#channel-url-${channel.id}`，前面加井号，因为它指向 ID，是一个 CSS selector。

这两步做完，把库引入并初始化。`import ClipboardJS from 'clipboard'`，在 onMounted 中初始化：`const clipboard = new ClipboardJS('.copy-button')`。参数是触发复制地方的 class，我们的复制按钮有一个 copy-button 的 class，注意前面要加一个点。

页面中尝试：点击复制，它会全选这个值，然后按 Command 加 V，能粘贴出 URL，说明复制成功了。它默认是 copy 操作，还支持剪切，同样通过自定义属性添加：data-clipboard-action，有两种值，copy 和 cut，默认是 copy。把它加到按钮上试试 cut，点击时会报错，原因写得很直接：Invalid target attribute, you cannot cut from elements with read-only or disabled attributes。意思是 input 上有 readonly 属性，不支持从这样的元素剪切数据。这里我们也不需要剪切，只是尝试一下方法，把这个属性删掉就好。假如去掉 readonly，它就可以成功完成剪切。

这种直接在 DOM 上添加信息的做法，我称之为指令式的做法，是另一种设计 API 的思路。拷贝是很贴近 DOM 的操作，所以这种复古的 API 设计也挺有意思，让我想到 jQuery 插件的设计风格。此外它还提供了事件机制，可以在剪切过程中捕获事件。clipboard 的实例是基于事件的，拿到实例之后可以在上面调用 on，有两个事件：success 成功时触发，error 报错时触发。回调里的 e 是一个特殊的事件对象，点进 ClipboardJS.Event 的定义可以看到：action 是什么操作，text 是对应的值，trigger 是哪个元素触发的，还有一个 clearSelection 方法，因为拷贝时会选中字符，这个方法可以取消选中。我喜欢 TS 的一点就是可以直接进定义文件看，比文档更直接。

现在做一个操作：复制成功后弹出一个提示，并把默认的选区清除掉。用 ant-design-vue 的 message，在 success 回调里先 `message.success('复制成功')`，然后调用 e.clearSelection()。

验证效果：点击复制时弹出复制成功，选区也被清除了，粘贴也能看到 URL 被成功复制到剪贴板。至此我们用 clipboard.js 完成了复制操作，下节课一起研究它的原理。
