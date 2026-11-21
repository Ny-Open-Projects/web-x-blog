# 8-23-通过 Image 构造函数获取图片的原始大小

上节课有了 element 家族的来龙去脉，这节课就可以完成任务了。我们需要从 HTMLImageElement 类型中找对应的属性。往下滑，有两个属性映入眼帘：naturalHeight 和 naturalWidth。看名称就知道差不多了，natural 是"自然"的意思。上面的注释清晰地写着 "original width of the image source before sizing"，image 在 size 之前的原始宽度，并且它是 read only 的。就是它了，应该没问题。

## 实现 getImageDimensions

接下来要设法通过一个 URL 拿到这个属性。首先要有这个类型的元素。看看有没有构造函数：Image 构造器可以创建一个尚未被插入 DOM 树中的 HTMLImageElement 的实例。调用 new Image 其实等于调用 document.createElement('img')，两者最终作用是一样的。

知道了怎么做，就在 helper 中新建一个函数（辅助函数），称之为 getImageDimensions。第一步创建 `const image = new Image()`，然后设置 `image.src = url`（传入的 URL）。接着等待图片读取并拿到值：添加事件监听 `image.addEventListener`，事件叫 load，在读取完毕后拿到数据。

为什么能添加这个事件？因为 image 继承自 EventTarget，而 EventTarget 天生就是基于事件的。从这个角度可以把之前"理所应当"的知识，别人告诉你 image 可以添加事件，用新的角度融会贯通，我觉得很好。

事件监听的触发是异步的。提到异步，我们使用 Promise（现在谁还用回调？）。return 一个 new Promise，里面有 resolve 和 reject 两个参数。load 时，从 image 上拿到 naturalWidth 和 naturalHeight 并 resolve。注意返回的数据结构：直接用这两个属性名太长了，希望返回 `{ width, height }` 这样的对象，可以在解构时起别名，`const { naturalWidth: width, naturalHeight: height } = image`。注意这不是 TS 在规定类型，而是 ES6 的解构别名，这样看起来清爽很多，然后 resolve 一个包含 width 和 height 的对象。

当然还要处理错误：addEventListener 的 error 事件中，直接 reject 一个错误出去。

## 在组件中调用

现在在 components-list 里调用。函数已经引进来，添加 `getImageDimensions(response.data.url)`，它是 promise，所以用 then 拿到 dimensions。

这里发现 dimensions 的类型是 unknown，很不爽：Promise resolve 的是 unknown 类型，TS 怎么可能没有类型？解决方法是给 Promise 添加泛型代表返回类型，或者在函数上添加返回值标注。这里就在 Promise 上添加泛型：resolve 的是一个对象，width 是 number，height 也是 number。现在 dimensions 上 width、height 都完美出来了。

逻辑很简单：只需宽度，height 不需要。用一个最大值判断它是否大于 max-width，然后根据真实 width 和 maxWidth 之间的情况设置 width 值。加一个 console.log 验证拿到的 width 是否正确，验证完删掉。

试一下结果。先上传一张小图（桌面头像那张）：184px，就只有这么大，没有像原来一样被定死成 318px，看起来很美观。再上传一张大图（452px 的图）：因为它大于最大值，直接设置成了最大值 375px，跟拿到的值核对没有问题，完美完成了需求。

## 扩展：支持 File 对象

还可以对这个函数做一个小改动。现在它接收的 URL 是 string 类型，但还有种常见情况：手里有的是 File 对象，比如图片还没上传，需要获得这个 file 的真实长宽。怎么办？上节课预览图片时刚学过：使用 URL.createObjectURL 生成一个存在内存里的图片地址。现学现用。

参数类型除了 string 有可能是 file。设置 src 时判断：typeof url 是 string 就直接赋值；不是就 `URL.createObjectURL(url)`（其实它是 file，这里的命名可能有些歧义，大家可以修正一下）。改动很简单，但功能拓展了很多。

把 onImageUploaded 除了 response 之外也把 file 拿过来（success 事件可以传出很多参数），直接传入 file 试试：点击上传图片，选择打开，没问题，虽然传的是 file 对象，但也能拿到 452px，非常方便。

这节课通过 HTMLImageElement 上面的一系列属性和方法完成了任务，还复习了图片预览时学到的 URL.createObjectURL 创建内存内 URL 的知识。知识都是融会贯通的，你掌握得越多，能够应用的场景也就越多，大家记住这句话。这节课就到这里，谢谢大家。
