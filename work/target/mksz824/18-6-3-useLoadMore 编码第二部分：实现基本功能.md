# 18-6-3-useLoadMore 编码第二部分：实现基本功能

上节课分析了加载更多的功能点，并完成了 actionWrapper 的前期改造，这节课来完成 useLoadMore 的编码。

先创建函数 useLoadMore，想清楚它有哪些参数。第一个是调用它的 action，因为内部要用 store.dispatch，所以传 actionName，string 类型。第二个是很重要的值：total。它一开始就要传入，并且是响应式的值，会动态变化，所以类型是 ComputedRef<number>。第三个是加载参数：加载哪一页、每页 size 是多少，还可能有更多参数（比如搜索时的 title），因为它们都会传到 URL 里。所以创建一个 interface 来代表这个类型，称之为 LoadParams：pageIndex 和 pageSize 都是 number，另外用一个 indexable type（key 为 string、值为 any）表示其他参数。

第三个参数命名为 params，并给初始值：pageIndex 为 0，从零开始，pageSize 给 8。参数准备工作完成。先拿到 store，等会儿要调用 dispatch：`const store = useStore()`。

在函数里创建一个响应式对象，值来自最初传入的 pageIndex。这是一个很关键的值，它是变化请求参数的根源：每次请求成功后会把它加一，所以必须是响应式的。`const pageIndex = ref(params.pageIndex)`，它就获得了初始值的响应式对象。

接下来用这个值构建 requestParams，也就是发送请求时需要的参数。特别注意它应该是 computed，因为它要根据 pageIndex 做相应变化，让它是动态更新的。实现里直接 return：先展开 params，再覆盖变化的值 pageIndex，值为 `pageIndex.value + 1`。为什么要加一？因为传入的初始值是 0，代表第一页，而下一次请求应该是 pageIndex 等于 1，即初始值加一。这里加两个注释：一个是变化的参数，另一个是根据变化的参数更新的请求参数。

这两个参数有了，就可以把方法暴露出去了。方法称为 loadMorePage，它是一个 function，因为会在各种情况下触发，比如点击按钮，或者下拉到页面底部自动触发。里面调用 dispatch：第一个参数 actionName，第二个是 payload，其中 search 相关的参数放在 searchParams 里，值就是我们创建的 `requestParams.value`。它返回 Promise，调用 then：请求完毕后把 pageIndex.value 加一，为下一次请求做准备。

除了最主要的 loadMorePage，还需要另一个属性：是否到了最后一页，这对 UI 判断非常有用。称为 isLastPage，肯定是一个 computed。返回什么值呢？先算总页数，使用 Math.ceil 向上取整：`Math.ceil(total.value / params.pageSize)`，pageSize 是定死不变的。什么时候是最后一页？当 `pageIndex.value + 1` 大于等于总页数的时候。特别注意 pageIndex 要加一，因为它和当前展示的页码总是差一。

最主要的两个成员写完了：loadMorePage 触发请求，isLastPage 判断是否到最后一页。把它们都返回出去。这里可以多做一步思考：不仅可以做 useLoadMore，甚至可以做翻页，有了 isLastPage 再加上 isFristPage、nextPage、prevPage 这几个值，其实就能做翻页了。这是后话，之后会添加这样的逻辑。现在暂时写到这个程度，把需要的都返回出去：loadMorePage 用于点击触发请求，isLastPage 用于判断最后一页，pageIndex 告诉我们现在加载到了第几页，这三个值在界面上都需要使用。最后 export default useLoadMore。

复盘一下整个过程：根据最初传入的值拿到一个变化的参数 pageIndex，每次加载成功后给它加一；再根据它构建一个动态更新的 requestParams，每次发送请求时自动取到最新的值；然后返回一个函数和一个计算属性，store.dispatch 在 loadMorePage 里调用，isLastPage 用计算属性判断是否到了最后一页。

函数的编码就到这里，看起来功能已经完整了。至于好不好用，下节课见分晓。
