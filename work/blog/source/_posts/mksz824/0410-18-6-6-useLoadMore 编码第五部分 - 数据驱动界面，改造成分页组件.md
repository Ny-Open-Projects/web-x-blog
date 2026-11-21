---
disableNunjucks: true
title: 18-6-6 useLoadMore 编码第五部分 - 数据驱动界面，改造成分页组件
date: 2026-11-17 08:50:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们在我的作品页把 useLoadMore 改造得支持了上一页和下一页，现在这个 hook 叫 usePagination 更贴切。但上节课最后留下了一个问题：切换 tab 时参数没法同步变化。这节课一起解决这个问题，并进化这个钩子函数，让它完全支持分页。通过这个过程，大家可以感受钩子函数的魔力以及数据和展示分离的妙处。

先观察现在的解决方案。requestParams 是基于新建的响应式对象 pageIndex 的计算属性，这意味着只有 pageIndex 的更新能被感知并触发更新，而且只能更新其中的 pageIndex 值，其他属性都无法更新。

自然想到：为了让所有参数都能被更新，为什么不把整个 params 都做成响应式的呢？使用 reactive：不再需要单独的 pageIndex ref，把 requestParams 改造为直接接收 reactive 包装的 params。相应地，加加操作不再作用于 ref，而是直接在 `requestParams.pageIndex` 上进行，把所有 .value 都去掉。这里顺便做一个小的改进：把 pageIndex 单独拿出来做一个响应式对象，这样它可以被单独返回出去，界面想使用这个变量时可以很方便地拿到，内部就用它来代替。

还有一点：希望 pageIndex 作为一个单独的 ref 变量返回出去，它比使用 requestParams.pageIndex 更简单、更语义化，可以当作一种快捷方式。现在的问题是 react 对象的某一项怎样转换成 ref，可以使用 toRef 函数，官方文档有具体描述：使用 toRef 时，第一个参数传入 reactive 对象，第二个参数是它的 key，返回的 ref 和原对象的这一项是完全相同的引用，更新 toRef 时 state 也会同步更新。完成这项工作：`const pageIndex = toRef(requestParams, 'pageIndex')`，别忘了返回出去。

修改完毕，回到 WorksView 改造使用处。参数比较长，我给它换了个行。这里希望把 requestParams 也拿出来，直接修改 `requestParams.isTemplate` 等于 t，这样参数就完成了更新。之前代码里还有两个小 bug：原来用的 `.value` 要去掉，因为现在已经是 reactive 对象了。

页面里测试：点击下一页，能拿到新的数据；再点下一页，没问题。测试之前的 bug：点击切换到我的模板，isTemplate 等于 1，正确；点击下一页，isTemplate 等于 1，pageIndex 等于 1，没问题。任务完成，而且大家可以看到这个分类下只有七条数据，到达最后一页时下一页消失了，只留下上一页。

完成这个任务后不难发现，我们不知不觉已经有了翻页功能的所有要素。现在用这个函数把它改造成一个翻页界面。首先再添加一个 function，跳到固定某一页，叫 goToPage，参数是 index（到哪一页），number 类型。实现很简单：直接把 requestParams.pageIndex 设置成要到达的页码，dispatch 逻辑和 loadMorePage 完全一样，然后把 goToPage 返回。在 WorksView 中把 goToPage 和 totalPage（总页数）都拿过来并返回。

有了这些数据，很快就能构建出翻页功能。我使用 ant-design-vue 自带的翻页样式，注意只用它的样式，不用它的功能。最开始是一个 ul，class 为 pagination，把原来的 a-button 改成 li。上一页是一个 li，用 click 触发 loadPrevPage，并加上 disable 状态，用 isFristPage 判断；下一页复制过来，逻辑完全一样，disable 用 isLastPage，点击调用 loadMorePage。

中间是分页的主体。需要一个 li 配合 `v-for="item in totalPage"` 遍历总页数，t 改成 item。class 添加 pagination-item，此外还有一个动态 class：pagination-item-active，当当前页等于 item 时高亮。注意 pageIndex 和展示页码总是差一，所以判断条件是 `pageIndex + 1 === item`。里面的 a 链接是真正处理逻辑的地方：把 href 去掉，添加 click，调用 goToPage(item - 1)，同样要减一，并加上 .prevent。li 里输出 item 作为页码文字。

看一下界面效果：分页完美出现。点击第四页，pageIndex 等于 3，没问题；点最后一页，下一页被 disable，active 高亮效果都有；切到我的模板，只有两页，点击下一页也正常。所有翻页功能都实现了。

通过这几节课的进化过程，我的目的是希望大家更深刻地理解钩子函数的意义，以及数据驱动界面的理念：提供数据，界面就有可能根据数据进化出无限可能。上下翻页、更精细的 pagination、下拉加载等一系列功能，都可以从这个 hook 进化出来。大家课下可以再回顾一下这个函数的进化过程。
