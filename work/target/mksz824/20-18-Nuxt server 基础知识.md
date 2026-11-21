# 20-18-Nuxt server 基础知识

上节课简介了 Nuxt 3 中 Server 的特性和架构，这节课学习它的基础知识。学习任何后端框架，我建议都按下面的顺序把这些点搞清楚。

第一是路由。上节课介绍过它是基于文件的路由，很有意思：只需在 server 下建对应的文件，就能生成路由，不用配置任何对应关系。在 server 里建了 api 文件夹，里面建 test.ts，自然会生成 /api/test 这个路由。

返回需要一个特殊的全局函数 `defineEventHandler`：

```ts
export default defineEventHandler(() => {
  return { name: 'Viking' }
})
```

回调里有一个重要参数 event，这是一个内置的事件对象，上面有很多属性和方法，用来获取本次 HTTP 请求的信息。我们先不用它，直接 return 一个 JSON。访问 /api/test，路由成功生成。它也支持 Promise：可以直接返回 `Promise.resolve` 并把数据放进去，框架会等 Promise resolve 后再返回，刷新后同样返回结果。这个路由和前端 pages 的文件映射方式非常类似。

第二是参数。在 pages 中用方括号定义动态参数，这里完全一样。想在 api 中创建 user 的 endpoints：新建 users 文件夹，里面用方括号建 `[id].ts`。要拿到参数，H3 提供了很多内置函数，与 request、response、body 相关的都有。获取参数用 `getRouterParam`：

```ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  return { id }
})
```

第一个参数传 event，第二个是变量名 id。另外，event 上有个特殊属性 context，context 里的 params 也能拿到同样的值，所以这个方法其实就是从上面取值。但推荐统一使用内置方法，它更快捷，内部还带一系列判断，更安全。保存后访问 /api/users/1，返回的 id 就是 1。

第三是 query。同样有全局函数 `getQuery`，把 event 传进去，返回 query 对象。访问时加上 `?name=hello`，就能拿到 name 等于 hello，再加一个 age 也能一一取出来。

第四是不同的 method。现在写的都是 GET 请求的路由，其他 method 怎么定义？这里非常有意思：也是通过文件名完成的。想向 test 发 POST 请求，就在 api 下新建一个同样叫 test 的文件，但后缀不同：`test.post.ts`，通过后缀名定义路由的 method。如果是 patch 或 delete，就把后面那个单词改成对应的名字即可。

验证一下 POST 路由。在 `test.post.ts` 里直接 return 一个 data 叫 post method。之前我们用 Postman 发请求，这次直接在 app.vue 里处理：添加一个按钮 Post Method，绑定一个 async 的 send 函数，用之前 data fetching 里学的方式发请求。因为是纯前端发的异步请求，直接用 `$fetch` 就可以：

```ts
const send = async () => {
  const data = await $fetch('/api/test', {
    method: 'post',
    body: { name: 'Viking' },
  })
  console.log(data)
}
```

URL 会有自动提示，非常方便；method 是 post，body 里带一个 name。清空控制台后点击按钮，console 返回了对应的数据，network 里也能看到请求成功发送、路由进行了响应。

有了 POST，怎样获取 body 中的数据？很简单，把 handler 改成 async，用 H3 提供的全局函数 `readBody`，同样把 event 传进去，然后把结果输出：

```ts
export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  return body
})
```

点击按钮，输出的是 name: Viking，body 中的参数就这样拿到了。

小结这节课的知识点：路由通过文件定义；参数用全局方法（getRouterParam）获取；query 用 getQuery 获取；不同的 method 用文件后缀名定义；body 用 readBody 获取。
