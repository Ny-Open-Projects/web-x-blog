# 18-5-5-PreviewForm 预览组件第二部分

现在来显示左侧的 iframe，这是一个很有意思的调 CSS 的过程。我准备了一张手机背景图，让 iframe 显示在其中。课程里 CSS 写得不多，这次换换口味。CSS 的分析和书写也是前端的重要能力，我来和大家一起分析并完成这个样式。

我们希望手机图片在除抽屉之外的左侧区域居中显示。抽屉用灰色表示，其余整个区域我们希望由一个容器覆盖，可以把它想象成绿色区域。在 PreviewForm 里创建一个 class，名为 final-preview，然后添加样式。

既然要覆盖整个左侧区域，position 肯定是 absolute。宽度很关键，要正好是剩余的部分，这里需要 CSS 的计算属性 calc：width 等于 calc(100% - 400px)，也就是整个宽度减去右侧抽屉的 400px。剩下很简单：height 是 100%，background 透明，top 和 left 设置对应的值。z-index 希望比较大，让它浮在上面，至少比下面的遮罩层大，给它 1500。

剩下的工作是让子元素在容器内左右上下都居中。遇到这个问题，flex 是最佳方案：display 设为 flex，上下居中用 align-items: center，左右居中用 justify-content: center。打开页面，final-preview 正好占据了除设置面板以外的所有区域，符合预期。

接着在它内部创建容器，名为 final-preview-inner，大小应该正好是手机背景图的大小。这里我经过比较精密的测量，直接写数据。特别注意 iframe 要显示在这张图的中间部分，也就是略过背景图边框的白边，所以加一些 padding 完成效果。样式直接写：width、height 和 padding 都是测量的结果，position 是 relative，background 把我提供的图片 URL 放上去，background-size 设为 cover。刷新页面，背景图出现了。

之后需要作品的标题和对应的 iframe。先把数据拿过来，在 setup 中添加：创建 store，`useStore<GlobalDataProps>()`，这个泛型我们已经用过很多次。然后把配置属性拿过来，因为要在上面取一系列的值：`const page = computed(() => store.state.editor.page)`。

拿到 page 之后，组装 previewURL。规则和之前渠道的 URL 非常类似：前面是 baseH5URL，然后 `/p/preview`，接着是配置的 ID（比如 113）和它的 uuid。写一个 computed，名为 previewURL，用字符串模板拼起来：`${baseH5URL}/p/preview/${page.value.id}/${page.value.uuid}`。最后 return page 和 previewURL。

有了这两个值，就可以在模板中添加内容了。先添加标题，称为 preview-title，样式很简单：固定的高度，垂直和水平都居中。对一行文本，可以用 height 和 line-height 配合 text-align 完成垂直水平居中。刷新看效果，作品标题已经出现在这里了。

最后添加 iframe。先给它外面加一个容器 iframe-container，把 iframe 放在中间。iframe 的 src 用变量 previewURL；width 是定死的 375；frameborder 设为 0。

看一下现在的效果：iframe 出现了，但高度有问题，不设置的话会非常矮。所以要根据配置中存的值动态设置高度，用 `:style` 绑定：page.props 是可选的，所以要先判断它存在，存在时取 `page.props.height`，不存在时设置一个默认值，也就是我们最初界定的 560。

来看最终效果：面板显示在中间了。还可以做一点小优化：当 iframe 设置得很长时，比如把 height 设成 1000px，内容会超出容器范围延伸到下面。所以需要在中间加滚动效果，把效果加在 iframe-container 上：给它一个固定的高度，并适时添加 overflow-y 为 auto，因为纵向有可能会比较大。现在内容比较高的时候会出现滚动，而不是一直撑到外面去。

最后给 iframe 加一个 loading 效果：给它添加一个固定的 class，名为 iframe-placeholder。想给 iframe 添加预设样式，可以直接设置它的 background-image 为一张动态的 loading SVG。把 src 删掉测试一下，就会显示一直在读取的效果。这节课完成了 iframe 对应的样式，最终实现了用手机图展示预览的效果。
