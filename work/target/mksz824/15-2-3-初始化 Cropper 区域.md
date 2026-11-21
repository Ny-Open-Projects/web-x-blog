# 15-2-3-初始化 Cropper 区域

这节课使用 Cropper.js 完成裁剪图片的第一步：将要编辑的图片生成 Cropper 提供的可编辑区域。

## 需求与浮层

首先要扩展 ImageProcessor 组件：除了重新上传，多添加一个 Button，称之为"裁剪图片"。点击以后弹出一个 Modal 浮层，在浮层中显示 Cropper 的界面并进行处理。这里有两个任务。

第一个任务相对简单：点击并显示 modal。Ant Design Vue 已经有 modal 组件，只需要添加一个响应式对象指代浮层是否显示，它接受一个 modal-visible 的值，true 时显示，false 时不显示。代码很简单：创建响应式对象 showModal 指示是否显示，在特定场景下切换这个值。将 a-modal 组件添加到 ImageProcessor 的 template 中，点击"裁剪图片"时设为 true，点击确定和取消时设为 false。运行效果：点击裁剪图片浮层出现，点击确定或取消浮层消失。第一步完成。

## 初始化 Cropper

第二步真正写代码：在浮层中显示 Cropper 的处理界面。首先安装：`npm install cropperjs`（--save），它自带 types 定义文件，不用单独安装定义文件。

按文档的 in-browser 用法：第一步添加一个 image 标签，src 设置为要编辑图片的地址。我已写好：src 的值是 value（props），id 随便起一个叫 cropped-image。第二步添加一个特殊的 CSS 属性，文档说这个属性很重要，为了适配 Cropper 的样式，照猫画虎复制过来即可，对应 `.cropper-container img` 添加两个样式。第三步在 JS 中添加功能：先 import 单独的样式文件，在 main.ts 中 import，然后把样式文件都放在这里。

接下来引入 Cropper 变量并初始化。Cropper.js 是一个类，用 new 初始化。什么时候初始化比较合理？应该在 modal 出现的时候，也就是 showModal 为 true 的时候。自然想到用 watch 函数监听 showModal 的变化：第一个参数是响应式对象 showModal，第二个是一个 function，参数是新的值 newValue。

初始化时需要拿到 DOM 节点：new Cropper 的第一个值是一个 DOM 节点，所以添加一个 ref 来拿，命名为 cropperImage，类型是 `ref<null | HTMLImageElement>(null)`。在 watch 中判断：假如 newValue 为 true（modal 已展示），先 console.log cropperImage.value，再把 cropperImage 加到 template 中 image 的 ref 上。

验证一下：点击裁剪图片，console 中出现了 null，没有拿到 DOM 节点。为什么？更新 DOM 是异步的过程，watch 的值虽然已经变成 true，但 DOM 还没有更新完毕。这个问题在 Vue2 时代大家都遇到过，解决方案是实例上的 $nextTick。在 Vue3 中它变成了一个全局的独立函数，返回一个 promise，可以等到下次 DOM update 结束后再执行后面的代码。

简单改造一下：从 vue 中导入 nextTick，把回调改成 async：`if (newValue) { await nextTick(); ... }`，等待完毕后再打印。重新点击裁剪图片，打印出了 DOM 节点，成功拿到。

## 实例化与清理

拿到 DOM 节点后就可以实例化了。照文档写：`new Cropper(cropperImage.value, { crop(event) { ... } })`，第一个参数是 DOM 节点，第二个是一个 object，上面有对应的事件。这里有类型报错，因为 cropperImage.value 有可能是 null，所以先做 type guard，判断它存在的情况下再进行赋值，错误消失。

在 crop 事件中把 event 打印出来看整体逻辑是否成功。点击裁剪图片：图片上面出现了一个新的遮罩层，这是 Cropper 修改后的 DOM 节点。在上面拖动时，回调能够成功更新，并且 detail 上面带着一系列值，能显示当前选择区域的数据。

再看页面上它生成的节点：原来的 image 在那里，Cropper 会创建一个新的 DOM 节点叫 cropper-container，除了原来的 image，还创建了一个新的 div，上面就是一系列用来处理图片的区域。原来的图片被添加了一个 class 叫 cropper-hidden，强行加了 display:none，所以我们看不到它了。

最后做一些清理工作。实例化一个对象时，特别注意要在不用的时候销毁。Cropper 实例在文档中提供了一个方法 destroy，"Destroy the cropper and remove the instance from image"，看起来就是我们想要的。在外层创建一个变量 cropper（Cropper 类型），第一次初始化时赋值；else 的时候（showModal 变回 false），假如 cropper 实例存在，调用 cropper.destroy()。

在页面上观察：选中这个 DOM 节点，点击裁剪图片，再点击取消，节点被销毁，image 的 class 也复原成了原始的值。清理任务完成。

这节课的第一步任务完成：可以使用 Cropper 将图片编辑框展示在弹窗上，并且能取得定义的坐标。下节课看看怎样完成图片截取的任务。谢谢大家。
