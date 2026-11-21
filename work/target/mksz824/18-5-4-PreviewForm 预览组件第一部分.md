# 18-5-4-PreviewForm 预览组件第一部分

完成发布和渠道的添加、删除之后，还剩最后一个功能：发布为模板。这个任务非常简单，展示的内容跟发布为作品完全一致，只是只有这么一项，没有渠道的概念：展示一个图、一个名称、一个 URL 和一个复制按钮。下面有一个按钮，点击后发送发布为模板的请求，请求也很简单，就是 works/publishTemplate 加上对应的 ID。模板和作品的区别在于：模板最终可以通过后台审核变成公共模板供别人使用，而作品就是自己的私人作品。编码方式大家都已经掌握，我就不浪费时间带着写了。

现在编辑器中剩下最后一部分：预览和设置。这个功能并不复杂。左侧是一张手机的图片，中间展示真实的预览效果。这里采用了 H5 端提供的一个 URL，它是真实渲染完毕的页面，所以跟最终在手机上的展示完全一致。我们可以用现有配置上的数据拼接出这个 URL。具体来说，左侧显示的是一个 iframe；右侧分为几块：第一块是生成二维码，用 QRCode 就可以完成；第二块是上传封面，这是分享时用的封面，跟编辑器里的截图不太一样，对应 settings 里设置的字段；下面是标题和描述；最后是一系列功能按钮，两大功能是发布和保存，对应的逻辑已经提前提取好了 hook 函数，用起来得心应手，这就是把逻辑都提取出来的好处。

开始完成预览和设置。首先像 PublishForm 一样建立一个子组件，为了给 EditorView 解耦，预览组件也作为 editor 中弹框的独立部分。我新建好了对应文件，先给它创建一个属性 visible，判断 PreviewForm 是否应该出现：props 里添加 visible，布尔类型，默认值 false，即不出现。

接下来把 visible 加到对应的节点上，用 v-if="visible"，只有 visible 为真时组件才渲染。

右侧的浮层是一种特殊的展示形式：从右侧滑出，这种形式叫抽屉展示，也就是 drawer，一般有四个位置可选。Ant Design Vue 提供了 a-drawer 组件，使用很简单，属性有一系列，最关键的是 visible，控制它是否出现；其他还有 title 标题、placement 位置、closable 是否显示关闭按钮等等。closable 为 false 时就没有关闭按钮，点击遮罩也可以关闭。

现在来添加 a-drawer：title 设置为设置面板；placement 是右侧；width 设置为 400；closable 是变量，设置为 true；最后是重要的 visible 属性，与 props 保持一致即可。

添加完毕后，在 EditorView 中挂到页面上尝试。需要一个响应式对象判断是否出现，和 showPublishForm 放在一起，称为 showPreviewForm，初始 false。还需要创建一个函数完成展示，称为 preview。这里除了把 showPreviewForm 设置为 true 之外，还有一个额外的逻辑：想展示预览，后端要有最新的数据，所以首先要将数据持久化，也就是先保存。因此先 `await saveWork()`，直接使用已有的 hook 函数，保存完毕之后再设置 showPreviewForm.value 为 true。把 preview 和 showPreviewForm 导出，挂到组件上：visible 传 showPreviewForm，点击预览按钮时调用 preview 函数。

来看结果：点击预览和设置，它会先保存，然后设置面板这个抽屉组件就出现了。下节课我们在左侧添加对应的 iframe 预览效果，并给它添加一个比较好看的样式。
