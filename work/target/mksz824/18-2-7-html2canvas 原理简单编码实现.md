# 18-2-7-html2canvas 原理简单编码实现

顺着上节的思路来编码。测试页面选 TemplateDetail 页面：点击"下载图片海报"按钮时，把页面里 author 这一列信息绘制到一个空的 canvas 上去（空 canvas 已创建好）。

## 四步实现

创建一个 drawCanvas 函数，按思路走四步。

**第一步，获取节点。** 用 `document.getElementById('canvasImage')` 拿到 canvas，断言成 HTMLCanvasElement，宽高各设为 400，一会儿好看些；再拿到想复制的元素，id 为 author 的节点（已加在页面上，包含两块内容），断言成 HTMLElement。

**第二步，创建 SVG。** 需要用 foreignObject 来创建。SVG 字符串比较长，直接复制：最外层是 svg，width 和 height 都是 400；里面是很关键的 foreignObject，宽高都是 100%；再里面是一个 div，div 中间把 `element.innerHTML` 填充进去，这就是要复制的 DOM 信息。

**第三步，创建 Blob 文件。** 用 Blob 构造函数 `new Blob([data], { type: 'image/svg+xml;charset=utf-8' })`。特别注意第一个参数是数组，第二个是类型，标准的 svg 图形图片类型，再加个 charset 为 UTF-8。

**第四步，创建图片并绘制。** 只有图片才能被绘制到 canvas 上。先用用过多次的 `URL.createObjectURL(svg)` 生成内存中的 URL（它接受一个 Blob 或 File）；然后 `new Image()`，`image.src = url`；加载完毕靠事件机制，`image.addEventListener('load', ...)`。

绘制时先拿 2D 上下文：`canvas.getContext('2d')`。ctx 的类型是 CanvasRenderingContext2D 或 null，所以要判断存在再绘制：`ctx.drawImage(image, 0, 0)`，横向纵向坐标都从 0 开始。整个过程完成。

## 效果与差距

把方法导出并绑定到下载图片海报按钮上，浏览器里点击测试：canvas 上突然多填充了一块，节点信息如约绘制到了 canvas 上面。特别注意它已经是图片形式，可以直接储存，还能用 toBlob 或 toDataURL 把 canvas 转成任何想要的文件类型。

不过和原页面相比没有样式，没有做到一比一复现。原因很简单：只添加了 HTML，没有添加样式。想做到一模一样，需要把节点的样式一一扒下来，添加到 SVG 中去，这其实就是 html2canvas 的简单原理。

真实的 html2canvas 有更复杂的处理，不是几行代码能描述的：要对截图元素做一系列遍历，根据节点类型进行复制和添加样式，还有针对不支持 foreignObject 的浏览器的兼容性代码。但大道至简，它最基本的原则离不开我们这几个步骤，这些步骤概括了它的整个流程。

通过这一系列努力，现在我们已经实现了一个最原始版本的 html2canvas。
