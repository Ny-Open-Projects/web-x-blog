# 18-5-3-完成copyToClipBoard编码

上节课我们学习了复制文本的两个 API，最终选用 execCommand 作为基本方案。虽然它是过时的解决方案，但从浏览器兼容性来看仍是第一选择。不过它有一个痛点：不支持传入要复制的文本，必须先选中对应的文本，再运行命令。这节课就来解决这个问题。

我们希望有一个函数来完成拷贝任务，参数就是要复制的文本。解题思路是这样的：第一步，手动创建一个可编辑的区域，比如 textarea，把要拷贝的值设置为它的 value；然后将它插入到页面中；接着调用 textarea 上的 select 方法把值选中；选中之后再调用 document.execCommand('copy')，拷贝就完成了。

这里有两个特别注意的点。第一，要让 textarea 不可见：因为过程中需要把它插入页面，用户最好看不到这个元素，所以要添加一些特殊样式，让它出现在可见区域之外。第二，添加这个节点只是为了完成功能，最后必须把节点删除。

有了思路就开始编码。在 helper 中新建一个函数 copyToClipboard，参数 text 是 string 类型，按步骤加好注释。

第一步，create a fake textarea，创建一个 textarea 元素并把它的 value 设置为传入的 text：`const textarea = document.createElement('textarea')`，它返回一个具体的 DOM 元素 HTMLTextAreaElement。第二步设置值：`textarea.value = text`。

第三步，define styles to be hidden，让它不可见：position 设为 fixed，top 设为 0，left 设成一个非常大的负值，比如 -9999px，这样它就不会出现在页面上了。设置完样式后把它 append 到 body 上并选中其中的文本：`document.body.appendChild(textarea)`，然后调用 textarea 上自带的 select 方法完成选中。

准备工作都做好了，就可以运行 execCommand。注意这里使用 try catch，因为有一小部分浏览器对这个命令也有支持问题，比如很老的 IE。try 中直接 return `document.execCommand('copy')`，它返回一个布尔值；catch 拿到错误后 console.warn('copy failed', e)。最后，删除 textarea 的逻辑放在 try catch 的 finally 里，保证任何路径都会执行：`document.body.removeChild(textarea)`。

函数写好了，在 EditorView 中使用一下。从 helper 里导入 copyToClipboard，还是放在 publish 里调用：`const result = copyToClipboard('new test')`，然后 console.log(result)。

页面中测试：点击发布，返回 true；Command 加 V 粘贴，new test 出现在了界面上，说明拷贝函数已经成功了。

这节课我们了解了整个拷贝到剪贴板的来龙去脉，也了解了 clipboard.js 源代码中用来解决这个难题的比较有意思的方法，我就是从它的源代码中获得的灵感。当然，我们也希望浏览器早日全面实现现代的 Clipboard API，用一行代码一劳永逸地完成这个任务。
