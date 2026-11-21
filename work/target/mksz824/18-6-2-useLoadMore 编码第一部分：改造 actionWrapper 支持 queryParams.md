# 18-6-2-useLoadMore 编码第一部分：改造 actionWrapper 支持 queryParams

上节课完成了剩余页面的功能分析，我们会从中挑选比较有意思的功能来实现，第一个就是首页的加载更多。这是一个很常见的需求，还能演化出另一种形式：除了按钮点击，还可以做成 infinite scroll，页面滑动到下面某个位置时自动加载。

这两种形式，根本都依赖后端 API 的分页支持。我们要完成模板列表的加载，先看它的 API。上节课说过，它有两个重要的 searchParams：pageIndex 是当前页数，pageSize 是每页条目数。演示一下用法：pageIndex 等于 0 即第一页，pageSize 设为 8，点击 send，返回的数据除了 list 里的内容，还有一个重要的字段 count，它是数据的总和，即总共有多少个 templates。看到这个数字可以想到能算出总页数。我们这个情况总共有 9 条，第一页展示 8 条，应该有两页，第二页只有一条。验证一下：pageIndex 等于 1 加载第二页，返回确实只有一条，和推断一致。

接口分析完了，再看前端怎样完成。按正常逻辑，解决方案很容易想到：第一步发送第一页的请求，pageIndex 为 0，pageSize 为 8；数据返回后把当前页记录为第一页，算出 totalPage 是 2；第三步判断当前页是否小于 totalPage，小于就显示加载更多按钮；点击按钮发起一次新的请求，pageIndex 加一，pageSize 不变；请求完成后 currentPage 加加，循环第三步，直到 currentPage 等于 totalPage。

这样做确实能解决问题，但假如其他列表也有这种需求，相同的逻辑就要完全重写一遍，这不是我们想要的方式。需要把加载这段逻辑抽象出来，而且最好不要和任何界面展示挂钩，让界面可以用这些 function 和变量自定义展示形式。听完这个分析，答案已经很明显了：使用自定义 hooks。

第一步，代码中需要发送这种带 searchParams 的请求，但现在的 actionWrapper 还不支持。Node.js 的 URL 有一个经典的分割图：我们现在支持的是动态的 pathName，用的是 path-to-regexp 这个第三方库，但还不支持 search 部分，也就是问号加上 key=value 的这段字符串。所以第一步是改造 actionWrapper，让它支持 search 参数。

改造应该在参数上做修改。payload 现在有 data 和 urlParameters，要添加一个 searchParams，可选，类型同样是 indexable type（key-value 对）。有了它就可以做判断：假如有传这个参数，就做对应处理，输出 key=value、中间用 & 连接的字符串。

我会采用两种方式完成。第一种很简单：循环对象输出字符串。在 helper.ts 中创建一个新函数 objectToQueryString，参数 queryObject 的类型和 searchParams 一致。用 Object.keys 拿到它的 key，调用 map 组装字符串模板：`${key}=${queryObject[key]}`，最后 join 用 & 连接，函数就完成了。把它从 helper 引入，然后生成新的 URL：在原来 URL 的基础上加上问号，再拼上 objectToQueryString(searchParams) 的结果。

试试好不好使：在 HomeView 里调用对应的 action 时添加新参数 searchParams，是 key-value 对，pageIndex 暂时设为 0，pageSize 设为 8。刷新页面，请求成功发送了。

第二种方式很有意思，大家比较少见，它是浏览器提供的内置对象 URLSearchParams，对 search 参数提供了更强大的分析和处理能力。它有构造函数可以 new 一个实例，上面有一系列方法，比如 append、delete、get、getAll。用这种方式实现同样的功能：创建 `const search = new URLSearchParams()`，然后对传入的对象做 forEach，这里可以用 lodash 的 forEach，第一个参数是 searchParams，回调第一个参数是 value，第二个是 key。在回调里用实例的 append 方法添加 key 和 value。最后它还有一个 toString 方法，可以转换回 query 字符串，所以直接 `search.toString()` 即可，不需要之前的 join 逻辑。测试可以看到完成了相同的功能，返回了同样的 URL。用这个内置对象完成这个任务有点大材小用，但目的是给大家拓宽视野，以后遇到比较复杂的 searchParams 处理，可以想到 DOM 上面有这个内置对象。

actionWrapper 的改造完成后，还需要把 total 保存起来。来到 store 的 templates 模块，添加一个字段 totalTemplates，number 类型，初始值 0，在 fetchTemplates 的 mutation 里赋值：`state.totalTemplates = payload.count`。

到这里，加载更多的分析以及 actionWrapper 的前期改造就完成了，下节课一起实现功能本身。
