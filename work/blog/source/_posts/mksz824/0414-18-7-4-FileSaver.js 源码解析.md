---
disableNunjucks: true
title: 18-7-4 FileSaver.js 源码解析
date: 2026-11-17 12:54:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课来分析 FileSaver.js 的源码，看看它是怎么实现的。它的源码并不难，体量很小，主要是为了处理浏览器兼容性添加了大量 polyfill 代码。这个库写得比较早，最后一次提交是两年前，语言特性上也没有用到多少 ES6 的方法。

代码开始之前有几个通用的工具方法。一个是 download，我们很熟悉，就是发送异步请求获取对应的 blob 数据。另一个叫 CORSEnable，用来判断文件是否支持 CORS 跨域访问。注意这个方法里使用了同步发送 xhr 的特性：xhr 有三个参数，最后一个参数为 false 时会同步发送请求，现代浏览器里这么调用还会爆出警告，你可以在 Chrome 的控制台里实际看到。最后还有一段点击节点的处理，为了兼容不支持 `new MouseEvent` 的环境做了相应处理。

主函数从 74 行左右开始，采用了大量的单元表达式（IIFE），根据不同特性走不同的分支，最终给 saveAs 变量赋值。一开始它先判断 `window` 是否不等于 object 类型，因为代码有可能会跑在 Web Worker 里，Web Worker 里这个方法没有意义，所以这里是个 no-op，什么都不处理。

进入正题后，第一步判断 download 属性是否存在于 HTML anchor element，也就是 `'download' in HTMLAnchorElement.prototype`。存在的话，走的流程跟我们自己的实现完全一样：创建 a 链接，设置 download 属性和 rel 属性，然后判断下载文件是否为字符串。我们自己实现时文件本身就是字符串，没有考虑另一种情况；如果传入的不是字符串，它会先用 XHR 获取 Blob，再通过 `URL.createObjectURL` 创建内存 URL 并赋值，最后点击完成下载。

字符串的情况跟我们一样，先判断是否跨域：`a.origin !== location.origin`。不是跨域就直接 click，触发链接的点击，因为我们设置了 download 属性，可以直接开始下载。如果是跨域文件，就要判断它是否支持跨域访问，调用前面看到的 CORSEnable。支持跨域时调用 download，也就是走 XHR 获取 Blob 的那条完整流程；不支持时直接 click，并给它设置 `target = '_blank'`，在新窗口打开。支持跨域的流程和我们实现的大同小异，前面都讲过了。

接下来是两处关键的兼容性处理。第一处是判断 `msSaveOrOpenBlob` 是否存在于 navigator 中。如果在，就走另一条路径：整体流程一样，唯一区别是保存 Blob 的方法。我们用的是 a 链接方式，它用的是 `msSaveOrOpenBlob`。查文档可以看到，这是一个 non-standard（非标准）方法，同时被标记为 deprecated，说明它就是为了特定浏览器的兼容性而存在的。看到 MS 前缀就知道，它大概率是给微软的浏览器准备的。这个方法很简单，接收两个参数：一个是 Blob 文件，另一个是默认文件名 defaultName，调用它就直接完成下载。

第二处是 `msSaveOrOpenBlob` 也不存在时的最终兜底。注释里写得很清楚：fallback to using FileReader and popup。方式是先用 `open('', '_blank')` 创建一个新窗口，给窗口设置 innerText 显示 downloading，然后使用 FileReader。FileReader 我们之前接触过，可以读取特定的文件类型，这里用的是 `readAsDataURL`。查文档：这个方法开始读取指定 Blob 的内容，读取完成后，result 属性中会包含一个 data 开头、base64 编码的字符串，表示所读取的文件内容。这个字符串会被赋给 popup 的 location.href，把 base64 字符串赋给一个窗口的 href 时，浏览器就会自动触发下载过程。这就是最后一种兼容性下载方式。

整个 FileSaver.js 源码解析下来可以发现，它和我们的实现差别不大，只是多了两处兼容性考虑：一个是 `msSaveOrOpenBlob`，一个是 FileReader 的兜底方案。通过源码解析，希望大家掌握两个之前用过、和文件处理相关的重要方法。第一个是 `URL.createObjectURL`，用来获取内存中的 URL 对象。第二个是 FileReader 及其三个读取方法：`readAsArrayBuffer` 返回 ArrayBuffer 数据；`readAsDataURL` 返回 base64 编码的字符串；`readAsText` 返回字符串形式的内容。这就是读取文件的几种方式。源码解析这节课就到这里。
