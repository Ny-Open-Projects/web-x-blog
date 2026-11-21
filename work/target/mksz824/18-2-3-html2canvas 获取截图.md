# 18-2-3-html2canvas 获取截图

上节介绍了 html2canvas 的 API，这节试用一下看它是否好用。先不完成截图后上传的整体功能，只做截图，并把截图结果显示在页面上，看看是否符合要求。

## 基本用法

为了测试效果，在左侧组件列表下方添加一个 image 元素，id 设为 testImage，样式宽 300px。然后创建 publish 函数，绑定到发布按钮的点击事件上：

1. 取要截图的 DOM 节点，中间编辑区域，给它加过 id 叫 canvasArea，用 `document.getElementById('canvasArea')` 取得，类型断言成 HTMLElement（它肯定存在）；
2. 引入 html2canvas（需自行安装）并调用。第一个参数是 el 这个 DOM 节点，第二个是 options，这里先加一项 width：希望截图的宽度，中间区域宽 375px；
3. 它返回 Promise，then 里拿到 canvas element；
4. 把 canvas 显示到 image 上：还是 getElementById 拿到 testImage，断言成 HTMLImageElement，然后赋值 `image.src = canvas.toDataURL()`。

canvas 上的 toDataURL 方法可以把这个 canvas element 转换成 base64 编码的图片资源内容，正好能直接赋给 img 的 src。

```ts
const el = document.getElementById('canvasArea') as HTMLElement
html2canvas(el, { width: 375 }).then((canvas) => {
  const image = document.getElementById('testImage') as HTMLImageElement
  image.src = canvas.toDataURL()
})
```

## 第一次测试：背景图丢了

到浏览器，打开作品 71 点击发布，截图出现了，但背景图片没有了。页面上所有图片元素用的都是阿里云 OSS，图片地址自然是跨域的，而 html2canvas 默认对任何跨域资源都不做处理，所以背景图没有被截进来。

想让它用 CORS 读取跨域资源，options 里有一个 useCORS 设置，默认 false，改成 true 即希望使用 CORS 读取远程资源。加上后再试：图片完美显示出来了。同时看 Network，截图过程中确实访问了我们的资源，这是测试环境的上传接口，response header 里有 access-control-allow-methods 和 access-control-allow-origin，跨域访问成功。

但注意：这些 header 是要在 OSS 那边配置的，默认不允许跨域请求。

## 反例：未开启跨域的 OSS

我创建了另一个作品 232，用的是给大家测试上传的接口（123.57.138.48），它的图片返回的域名不支持跨域。点击发布，弹出一个 CORS Error，这个资源的 response header 不包含刚才那两个 header，不支持跨域；关掉错误后，背景图片没有出现，取而代之是一个错误。原因就是它的 OSS 没有开启跨域支持。

想在阿里云 OSS 中开启跨域，操作路径是：Bucket 列表 → 点击对应 Bucket → 权限管理 → 跨域设置 → 创建规则并配置允许的 header。设置完毕后就可以允许跨域访问了。

图片跨域是使用 html2canvas 的一大坑，网上查这个问题的人非常多，请特别注意。

## 留一个悬念

还有个奇怪现象：回到作品 71 打开 console 点击发布，图片成功出现，但它的实际宽度是 750px，我们设置的容器宽度明明是 375px，图片实际大小正好是设置的两倍，这是为什么？带着这个疑问，下节继续解决 html2canvas 剩下的几个棘手问题。
