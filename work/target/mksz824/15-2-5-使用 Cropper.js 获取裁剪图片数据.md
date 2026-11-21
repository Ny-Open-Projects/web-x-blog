# 15-2-5-使用 Cropper.js 获取裁剪图片数据

上节课使用云服务的特性非常轻松快捷地完成了图片裁剪。只不过这个特性只有使用阿里云 OSS 这样的对象存储才提供，当你使用自己的服务器储存图片时，是没法完成这个需求的。所以通用的方法应该是：拿到裁剪的数据，重新上传完成图片，获得新的 URL，然后发送 change 事件来更新这个新的 URL。

## getCroppedCanvas 与 Canvas

上传我们已经很清楚了，已经写了 uploader 组件：使用 FormData，把最重要的 file 对象添加进去。现在的问题是怎样获得截取区域的 file 数据。到 Cropper.js 的文档中寻求答案：实例上有一系列方法，其中有一个称为 getCroppedCanvas。它有一堆 options（长度宽度等），我们看最后的 return value：返回一个 HTMLCanvasElement。

看到这个类型突然想到，之前在获取图片真实大小那节讲过 HTMLImageElement 和它平级的元素就是 HTMLCanvasElement。canvas element 是 HTML5 标准的一部分，本身提供一个容器，通过 JavaScript 获取元素实例后，用脚本绘制各种图形。看一个最简单的例子：先 getElementById 获得 DOM 节点，然后 `c.getContext('2d')`，设定 canvas 元素的类型，2d 是其中一种。设定类型后就可以修改属性、调用方法来绘制内容，比如把背景色改成某个颜色，再绘制一个正方形，运行出来就显示出这么一个图形。这里不研究 canvas 具体的 API，它本身挺复杂，有兴趣可以自己了解，我们只是介绍。

回到文档：从图中可以看到 HTMLCanvasElement 和之前的 HTMLImageElement 有着同样的继承关系（Element、Node、EventTarget），因为它是标准的 HTML 标签，同时可以通过 JS 绘制图形，所以有丰富的属性和方法。

## toDataURL

现在有了 Canvas，怎样把它转换成文件类型呢？看上面的一系列方法，有两个引起我的兴趣。第一个称为 toDataURL。这个 dataURL 看起来似曾相识，学习预览图片时我们用过另一个方法 readAsDataURL，两者相似点就是 dataURL 这个特殊格式：使用 base64 编码的 URL。有了这个 URL，应该可以将裁剪后的图片显示在页面上。试试看这个猜测对不对。

来到 ImageProcessor，暂时做实验：创建一个 dataUrl，是一个响应式对象，初始为空。在 handleOk 里多加一行：`dataUrl.value = cropper.getCroppedCanvas().toDataURL()`，cropper 实例调用 getCroppedCanvas 方法返回 HTMLCanvasElement，再调用它上面的 toDataURL，返回一系列字符串，赋值完毕。把 dataUrl return 出去放在模板中，暂时把关闭 modal 的逻辑注释掉（我们希望 modal 不关闭，好查看效果），再添加一个 img，src 改成 dataUrl。

刷新测试：点击裁剪图片，选择一个大小，点击确定，图片显示出来了。检查一下，src 就是我们之前说的 base64 编码的 dataURL，这个方法的作用就搞清楚了。

## toBlob 与 Blob

接下来看第二个方法，一个很重要的、我们最终要使用的方法：toBlob，它是完成这个任务的重头戏。有的同学可能听过 Blob，有的可能不熟悉。它是浏览器 DOM API 中一个比较高级的特性。文档的官方说法是：Blob 对象表示一个不可变、原始数据的类文件对象，它的数据可以按文本或二进制的格式进行读取。用简单的语言理解：Blob 对象代表一个保存了文本或二进制数据文件的片段，就是一个二进制数据的片段。

新建一个看看它到底是什么。它有构造函数，用 new 创建：`const myBlob = new Blob([...], { type: 'text/plain' })`，第一个参数是要创建的数据，第二个是选项，这里添加 type 为 text/plain。打印出来就是一个对象，上面有一系列属性和方法。

重点是第二句：文档特别写了，"File 接口基于 Blob，继承了 Blob 的功能，并扩展使其支持用户系统上的文件"。这一看就是我们需要使用的。我们最终想获得的是 file，而文档告诉我们 file 接口基于 Blob，说明可以把它等同于 file 使用。在 TypeScript 里看一下定义：interface File extends Blob，File 上添加了两个 read-only 属性，lastModified 和 name；再点进 Blob 看，它也有一些 read-only 属性和一系列方法。

也就是说，有了 Blob 对象就等于有了 File 对象；有了 File 对象，完成上传自然不在话下。

这节课首先搞清楚了什么是 Canvas Element，以及上面两个非常有用的方法（toDataURL 和 toBlob），最后引申出了 Blob 这个特殊的数据类型以及它和 File 对象的关系。下节课就可以完成截图并且上传的任务了。这节课到这里，谢谢大家。
