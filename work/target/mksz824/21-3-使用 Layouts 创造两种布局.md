# 21-3-使用 Layouts 创造两种布局

上节课学了 Tailwind 的简单用法，也留了一个问题：项目需要两套 UI 布局，但现在只有一套定义在 `app.vue` 里的结构。当然可以在每个页面里单独编写，但那样会非常重复。这节课接触 Nuxt 3 的一个新概念：Layouts，用它来完成这个任务。

## 创建 default 布局

首先创建一个 `layouts` 文件夹，在其中创建一个文件，命名必须是 `default.vue`。用它来做我们目前这种带头部 Header 的通用布局。

做法很简单：把 `app.vue` 的内容移动过去，删掉不需要的全局内容，去掉 `NuxtPage`（页面内容不能写死在布局里），也清理掉之前测试用的元素。然后在这个位置添加一个 `slot`，它就代表具体页面内容要放置的位置：上面是 header，下面是具体内容。

回到 `app.vue`，把原有内容全部删掉，换成全局组件 `NuxtLayout`。注意关键一步：要把 `NuxtPage` 放置到 `NuxtLayout` 里面去，让它们一层一层地起作用：

```vue
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

保存刷新，首页就变成了我们刚定义的 default 布局：上面是 header，下面是 `pages/index.vue` 里的内容（welcome to home page）。第一种布局完成。

还可以做一步修正：把整个 header 抽到一个全局组件里，结构会更清晰。

## 创建极简布局

第二种布局是极简风格，没有多余元素，就是一个整体的空页面。在 `layouts` 里新建 `custom.vue`，里面不需要任何多余元素，直接放一个 `slot` 即可。

接下来让 login 页面使用这个布局。打开 `pages/login.vue`，添加我们之前用过的全局函数 `definePageMeta`，它有一个 `layout` 参数，把名称传进去。`definePageMeta` 的提示里已经列出两种可选值：default 是其他页面都在用的默认行为，这里选我们独特的 custom：

```ts
definePageMeta({
  layout: 'custom'
})
```

保存后到 login 页面查看，它已经是独立的极简布局；而 user one、user two 这些页面仍然使用 default 布局，互不影响。

这节课的任务就完成了：通过 layouts 可以让整个应用拥有两种完全不同的布局。下节课进入 login 页面的开发，看看怎样用最新的方式完成一些通用功能。
