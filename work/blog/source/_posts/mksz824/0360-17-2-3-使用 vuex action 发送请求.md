---
disableNunjucks: true
title: 17-2-3 使用 vuex action 发送请求
date: 2026-11-17 08:00:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

之前介绍了接口相关的信息，这节课正式在应用中发送异步请求。先从最简单的入手：现在首页显示的是一些静态模板，我们希望用接口的动态数据代替，也就是「获取公共模板」接口（`api/templates`），GET 请求，无需任何权限。

## 为什么需要 Action

自然的想法是：添加一个 mutation 触发数据变化，在里面用 `axios.get` 发异步请求。但读文档时有一条特别的规则要记住：**mutation 必须是同步函数**。原因大家可以自行了解，主要是 mutation 中添加异步请求可能会破坏 vuex 的可追溯性。

所以 vuex 提出了一个新的概念代替 mutations 来做这件事：actions。它和 mutations 很相似，有两点区别：

1. action 提交的是 mutation，而不是直接变更状态；
2. action 可以包含任意异步操作，正合我们之意。

## 创建第一个 Action

store 之前分成了三部分：user、templates、editor。现在处理模板信息，来到 templates.ts，创建 actions：

```ts
actions: {
  fetchTemplates(context) {
    return axios.get('/templates').then(response => {
      context.commit('fetchTemplates', response.data)
    })
  },
}
```

直接 return 一个 `axios.get`，后面写 URL。这一系列 URL 用的都是测试服务器地址，写很多次会很繁琐，所以先在 main.ts 配置 axios 的 baseURL：

```ts
const baseBackendURL = 'http://xxx.xxx.xxx.xxx:8081'
axios.defaults.baseURL = `${baseBackendURL}/api`
```

记住 `axios.defaults` 这个属性。配置后发送任何请求都会自动加上这个基本 URL，get 后面只需写 `templates`，分页参数先不加，用默认值。

拿到 response 后发送对应的 commit。action 的第一个参数叫 `context`，它是与 store 实例具有相同方法和属性的对象：`context.commit` 可以触发 mutation，`context.state` 和 `context.getters` 可以获取本模块的 state 和 getters。特别注意：context 上的属性指代的是 module 上的 state 和 commit，要拿全局的内容得用 `rootState` 和 `rootGetters`。

mutation 的名称也叫 `fetchTemplates`，把 `response.data` 传过去。

## 给返回数据写类型

创建对应的 mutation，第一个参数是 state，第二个参数是拿到的数据，这里叫 `rawData`。注意 rawData 现在是 any 类型，我们希望把类型描述出来，后端返回的格式非常精确且统一：最外层是 `errno` 加 `data`；list 类型的返回，`data` 里是 `list`（数组）和 `count`（总条数）。描述好类型就能享受 TS 的红利。

新建 `respTypes.ts`，把这些类型都放进去：

```ts
export interface ResponseData<T> {
  errno: number
  data: T
}

export interface ListData<T> {
  list: T[]
  count: number
}

export type RespListData<T> = ResponseData<ListData<T>>
```

`ResponseData` 接受泛型 T，是所有服务器返回的大体类型；`ListData` 描述数组类数据；`RespListData` 把两者组合起来，供模板列表使用。泛型 T 对应 list 每一项的类型。

在 mutation 里导入并使用：

```ts
fetchTemplates(state, rawData: RespListData<TemplateProps>) { ... }
```

T 传 `TemplateProps`。中间顺手修正一个笔误：字段名不是 `error` 而是 `errno`。现在类型非常完美：`rawData.data` 下有 `count` 和 `list`，取 `list[0]` 就能点出 `TemplateProps` 的所有属性。

赋值就很简单了：`state.data = rawData.data`，两个都是数组直接相等，然后把初始值去掉。mutation 完成。

## 在首页触发

最后一步在首页 home.vue 发送请求。时机用 `onMounted`，通过 `store.dispatch` 触发 action：

```ts
onMounted(() => {
  store.dispatch('fetchTemplates')
})
```

有同学可能觉得 action 多此一举，有 mutation 为什么再包一层？再强调一遍：mutation 只能是同步操作，想异步，第一个想到的应该就是 action。

刷新页面，首页内容变成了从后端拿到的真实数据，和后端一一对应。首页数据的异步请求完成，vuex Action 的用法也学会了。下一步大家可以按照后端返回的真实数据格式，自行把 `TemplateProps` 对应补全，现在只定义了一部分字段，这个工作留给大家。
