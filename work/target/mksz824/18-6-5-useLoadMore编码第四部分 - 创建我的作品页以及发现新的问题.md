# 18-6-5-useLoadMore编码第四部分 - 创建我的作品页以及发现新的问题

这节课继续使用已经写好的 useLoadMore，在另一块实验田，我的作品页，完成一次新的实践。页面逻辑同样简单，我已经写好了部分页面：一个新路由，名为 works，展示我的作品和模板。请求的 API 是查询我的作品或模板，也就是 works 接口。它有两类数据，一个是我的作品，一个是我的模板，支持 tab 切换。看一下 network：切换到我的模板时，请求里只有一个用来区别的参数 isTemplate 等于 1；切回来时 isTemplate 等于 0，表示我的作品，也就是没有发布成模板的作品。

store 中的代码照猫画虎：在 templates.ts 里根据 templates 和 totalTemplates 添加了 works 和 totalWorks，类型完全一样，还添加了对应的 mutations 和 actions，逻辑都非常简单。

现在页面上已经有了作品列表，下面有一个分页功能，点击上一页或下一页可以切换数据。这看起来和 useLoadMore 非常类似，但我们现在的 hook 只有下一页的功能。先看看怎样用 useLoadMore 完成下一页数据的添加。在 WorksView 里照猫画虎拿出 useLoadMore：第一个参数是 actionName，这里叫 fetchWorks；第二个参数是 total，总共有多少项；第三个是 searchParams，我创建了一个 computed 把 isTemplate 的值填进去。特别注意 searchParams 是用 computed 包裹的，因为切换 tab 时要切换这个值，用 computed 才能感知变化。取出 isLastPage 和 loadMorePage 并导出。

然后同样在页面上添加，加在 worksList 下面。worksList 是我新添加的组件，就是显示一系列作品，没有什么神奇之处。添加一个 a-row，中间放下一页按钮，type 等于 primary、size 等于 large，click 调用 loadMorePage；isLastPage 为 true 时不显示，并且有 loading 状态。

看看上次写的 useLoadMore 能否在这里复用：一开始有四条数据，点击下一页，请求的是第二页数据，pageIndex 等于 1；再点，pageIndex 等于 2，运行良好。

但分页还有上一页和是否第一页的功能，所以现在简单修改 hook，让它服务更多场景。requestParams 是为下一页准备的，里面直接把 pageIndex 加一了。现在有了上一页功能，希望它不再加一，而是保持完全相同的值；把加一的逻辑挪到点击 loadMorePage 的时候再处理，也就是 dispatch 之前手动加一，then 里的加一去掉。这样一个小修改就支持了上一页。添加 loadPrevPage：`pageIndex.value--`，值变化之后 requestParams 这个 computed 会自动更新，重新发送请求。还需要 isFristPage，更简单：判断 pageIndex.value 是否等于 0，等于 0 说明在第一页。

把这些返回出去，回到 WorksView 把 isFristPage 和 loadPrevPage 也导出，同时把 pageIndex 拿出来，调试时可以把它显示在界面上作为参考。

测试一下：pageIndex 等于 0 时，上一页自然不存在；点击下一页，pageIndex 等于 1，上一页出现了；继续点下一页，pageIndex 等于 2；点上一页，加载的是 pageIndex 等于 1 的数据，没问题；再点上一页，pageIndex 等于 0，上一页按钮消失。简单的修改没有问题。

还有一个细节：切换 tab 时要让它重新运作。我们已经暴露了 pageIndex，它是响应式对象，切到我的模板时直接把 pageIndex.value 置为 0。测试：先把页码点几页到第二页，切换到我的模板，pageIndex 归零，并且发送的请求是 isTemplate 等于 1。再点击下一页，发现问题了：pageIndex 等于 1，第二页的数据完全正确，但请求里的 isTemplate 等于 0，等于我们在我的模板 tab 里拿的是我的作品的数据。

分析一下原因。useLoadMore 的第三个参数决定用什么样的参数发送请求，而 searchParams.value 其实是一个普通 object，是一锤子买卖，不会随着响应式数据的变化而更新。我们的 isTemplate 是 ref 类型，切换 tab 时它变了，但 hook 内部保存的参数还是初始值的快照，所以出现了这个问题。

这个问题该怎样解决？下节课我们一起来解决，让这个 hook 越做越完美。
