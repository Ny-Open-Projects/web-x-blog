# 18-3-3-添加 usePublishWork

上节课我们完成了整个发布流程，连续发送了多个异步请求，完成了对应的操作。在这个过程中，editor 里的代码量又开始上升了。这时候可以照猫画虎，把和发布相关的内容移到另外一个函数中。既然已经有了 useWork，自然可以再写一个 usePublishWork，专门负责发布的一系列工作。

组件里的逻辑太多怎么办？答案就是把一整块功能提取出去。可以用插件的方式，也可以用我们已经创建的 hooks 方式。这里再强调一次：hooks 只不过是用在 setup 中的普通函数而已。创建它的时候，不要觉得非得足够通用才值得提取，任何重复的或者冗长的逻辑，都可以尝试抽出来。

那么要把哪些代码提取到 usePublishWork 里？观察 editor 中的 publish 逻辑，一开始有一系列和 editor 元素样式相关的内容，比如 setActive、canvasFix，这些不应该抽象到 publish 当中。而 isPublishing 是和整个发布过程相关的状态变量，可以把它添加到函数中，返回供界面使用。

和 useWork 一样，usePublishWork 只是把这里的逻辑提取过去，我采用复制的方法一部分一部分来写。第一步是把需要的依赖都拿过来。这里有个特殊的点：publish 中需要 saveWork 的逻辑。也就是说，我们要在一个钩子函数中引用另一个钩子函数。

看一下 useWork 中的逻辑。除了我们需要的 saveWork 这个保存函数之外，它还有其他一系列逻辑：当你调用这个函数时，它会自动执行自动保存，以及离开路由前的提示。这两个功能和发布无关，可以称之为 side effects。发布中不需要这些，它们只在 editor 中才需要。

怎么解决这个问题？最简单的想法是给 useWork 添加一个布尔类型的参数，用来关闭 side effects，默认为 false。传入 true 时就跳过这两个功能。我们把这个参数称为 disableSideEffect，默认 false。当它等于 false 的时候，也就是 `!disableSideEffect` 时，才把自动保存和离开提示这两段逻辑包裹进来。

当然还有另外一种实现：把两个副作用包裹在另外一个函数中返回，想使用的时候直接调用那个函数即可。

继续补全 usePublishWork，基本就是从 editor 中拷贝逻辑。创建 usePublishWork 函数，把数据准备拷贝进来。注意 saveWork 调用时传入参数，这样它就不会执行那两个副作用。然后编写主要的作品发布函数，称之为 publishWork，它是一个 async 函数，并且有一个参数：在哪里截图，也就是 HTML element。把对应的逻辑拿进来，这么多的步骤现在就提取到 publishWork 当中了。注意 isPublishing 也包括在内，finally 中把它置为 false。

现在 publishWork 和 isPublishing 都有了，直接 `return { publishWork, isPublishing }`，最后 export default usePublishWork。

有了这个东西，就可以在 PublishView 中进行替换。把 usePublishWork 导进来，照猫画虎地解构出 publishWork 和 isPublishing，然后把原来那些复杂的逻辑都删除掉，最后只需要调用 publishWork，传入 el 参数即可。

这里还有一个很多人在问的问题：使用 setup 时，要返回的变量非常多。我认为这是一个很自然的事情，你要在模板中使用哪些变量，就返回哪些，这样也能很清楚地表明需要哪些数据。假如觉得繁琐，Vue 有一个新的 RFC 提案，并且已经合并到了 master，它大约是从 3.0.3 提出的语法糖，叫 script setup：写一个 script 标签并标记 setup 属性，就可以直接在模板中使用这些变量，最终所有变量都不需要返回，等于自动帮你返回了。

不过这个语法也引发了大量讨论，相关帖子的讨论非常长。有人表示不太喜欢这个主意，因为太多魔法发生了，已经长得不太像 JavaScript 了。对于这个特性，大家可以按照自己的喜好酌情使用，我这里不采取这种写法。

至此第二次改写完毕，我们把另一个模块抽象到了钩子函数中。大家可以课下试一试修改后的逻辑是否好用。
