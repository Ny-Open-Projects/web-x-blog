# 18-6-4-useLoadMore编码第三部分 - 页面实践以及支持无限滚动加载

上节课写完了 useLoadMore 的函数实现，现在把它应用到程序中试一下。首先给 Template 相关的 interface 做个优化。从后端返回的值可以得知 template 有很多字段，而我们目前只声明了几个，不够用。看到这些字段我觉得似曾相识：编辑器取得的页面信息里有一模一样的字段。发送请求 works/232 时，返回的内容里除了 content，其他字段和 templates 的信息一模一样，所以完全可以把当时的类型拿过来用，只需要做一个简单的转换。

我在 editor.ts 里添加的那一系列属性都定义在 PageData 中。转换要做两件事：第一，把里面的 setting 和 props 两个属性省略掉；第二，PageData 上的所有属性都是可选的，而 TemplateProps 中我们希望它们是必选的。所以要用两个内置的工具类型来完成转换：先使用 Omit，第一个参数是源类型，后面是要省略的属性名的联合类型，也就是 'props' | 'setting'，这样完成了省略；再套上 Required，它接受一个泛型，把所有属性转成必选。新的 TemplateProps 就等于 `Required<Omit<PageData, 'props' | 'setting'>>`。删掉旧的类型定义后，模板列表上现在可以打出更多的属性了，比如 isHot 和 isNew 这两个布尔值。有了它们，可以在卡片上多显示一个 hot 和 new 的标记，页面上就能看到了。

现在正式完成功能，位置在 HomeView。useLoadMore 需要一个重要参数 total，把它拿出来：`const total = computed(() => store.state.templates.totalTemplates)`。然后导入 useLoadMore 并初始化：第一个参数是 actionName，和 fetchTemplates 一样；第二个是 total；第三个是 params，一开始采用页面里已有的值，pageSize 这里改成 4，可以多测试几页。把需要的变量取出来：一个是 loadMorePage，一个是 isLastPage，然后导出。

接着在页面上添加内容。用一个 a-row 把列表和按钮分割开，里面再创建 a-row 放按钮的位置，a-row 上有一些对应 CSS 的属性让内容居中。按钮用 a-button：type 设为 primary（蓝色），size 设为 large，click 时调用 loadMorePage；用 v-if="!isLastPage" 控制它到达最后一页时消失；再加 loading 属性，直接使用 fetchTemplates 对应的 isLoading。

还要在 templates.ts 里做一个简单转换：现在 mutation 直接替换数据，而我们需要把数据持续追加。把 raw data 中的 count 和 list 拿出来，count 直接简写赋值，list 用数组展开：`state.data = [...state.data, ...list]`。另外之前有个小 typo，应该是 a-button，我已经修改了。

现在界面上出现了加载更多按钮。特别注意验证请求是否正确：点击第一次加载更多，发送的是 pageIndex 等于 1，也就是第二页，没问题；总共三页，所以按钮还在；再点击一下，加载第三页，此时它知道到达了最后一页，按钮就消失了。大家还可以把 pageSize 调小再测试，最后都非常好用。useLoadMore 已经可以良好运行了。

为了让大家更深刻地理解逻辑和界面解耦的规则，我们再用 useLoadMore 快速添加一个新功能，也就是之前说过的无限下拉加载。有了现成的 function 和变量，这很容易：在 window 上添加事件监听 addEventListener('scroll', ...)，回调里先判断是否到了页面最底部。需要两个值：整个文档的高度 totalPageHeight，用 `document.body.scrollHeight` 拿到；以及当前滚动到的位置 scrollPoint，等于 `window.scrollY + window.innerHeight`。有了这两个值就可以比较：如果 scrollPoint 大于等于文档高度，说明到了页面最下方；再加上 `!isLastPage.value` 的判断，满足条件就调用 loadMorePage，测试阶段可以先 console.log('at the bottom')。

刷新页面验证：第一页加载完，滚动到最下方，触发了第一次请求，pageIndex 等于 1，也就是第二页的内容；再往下滚到最下面，又成功读取了第三页；所有数据加载完之后，再往下滚就不会继续加载了。

这节课的演示就到这里。我们很快地用 useLoadMore 完成了两种不同的界面展示方式。通过这种方式，你是否对把界面交互抽象成逻辑上的变量和 function 有了更深刻的理解呢？
