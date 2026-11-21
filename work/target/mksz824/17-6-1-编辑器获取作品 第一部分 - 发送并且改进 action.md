# 17-6-1-编辑器获取作品 第一部分 - 发送并且改进 action

做完一系列通用准备后，这节开始给编辑器接入后端。编辑器的第一项工作是作品的创建和展示。展示就是根据作品的 ID 获取作品信息，登录状态下直接调用 `api/works/{id}` 即可。创建则多一步：先用 POST 接口创建一个空白作品，只需传 title、description，coverImage 加不加都行，接口返回作品 ID 后再跳转到对应的编辑页面。

两项任务思路都很直接，这节完成展示部分，创建部分大家可自行完成（其实就是多一步），代码会一并提交到本节课供参考。

## 获取路由中的作品 ID

进入路由时，也就是 editor 组件进入时调用接口取数据，所以要从路由里拿 ID。路由上已经添加了动态路由参数 id，组件里用 useRouter 创建 route，然后 `route.params.id` 就能拿到，存为 currentWorkId。

请求放在 onMounted 里，先判断 currentWorkId 存在再发送，dispatch 一个叫 fetchWork 的 action，参数是 currentWorkId。

## 难点：URL 里的动态参数

到 editor.ts 里添加这个 action 时犯了难：我们有现成的通用 actionWrapper，但它的第一个参数是定死的 URL 字符串，没法把 ID 拼上去。要做的就是把 URL 中的参数以特殊形式标记，调用时再动态替换，也就是 `works/:id` 加一个 `{ id: 123 }`，转换成 `works/123`。

Vue Router、Express 等框架都有动态路由的概念：用冒号加参数名标示动态 ID。怎样把带动态段的字符串和参数对象转换成新字符串？这是一个比较复杂的正则问题。为此查阅了 Express 和 Vue Router 的源码，发现它们都在用同一个第三方库：**path-to-regexp**。它提供 parseToRegExp、match、parse、compile 几个好用的函数，这里介绍后三个：

- **match**：把动态路由的 URL 转换成一个函数，函数接受字符串，返回 path 对象，能把 id 等参数提取成 object；
- **parse**：把一个路径转换成一系列 token，按斜杠分割成转义后的对象；
- **compile**：传入带冒号的动态路由路径，返回一个 toPath 函数；toPath 再传入 `{ id: 123 }` 这样的对象，最终输出 `works/123` 字符串。

compile 正是我们想要的。

## 改造 actionWrapper

动手改造。现在 actionWrapper 的参数 payload 原来直接指代 data，现在要多一层结构把 data 和 URL 参数分开，于是新建一个 interface 叫 ActionPayload：

- `urlParameters?: { [key: string]: any }`，indexable type；
- `data`，发送 POST 请求要传的数据。

安装 path-to-regexp 后引入 compile，逻辑写在 actionWrapper 内部。先把 payload 类型改过来并给默认值空对象，从中解构出 urlParameters 和 data（注意内部用的 data 字段要改成全称，响应处改为 `resp.data`）。

处理 URL 参数时照抄库文档的写法，decode 用内置的 decodeURIComponent，URL 换成传入的参数，得到 toPath 函数；再在外部创建 newUrl 变量，等于 `toPath(urlParameters)` 生成的最终字符串，请求改用 newUrl 发送。

```ts
if (urlParameters) {
  const toPath = compile(url, { decode: encodeURIComponent })
  newUrl = toPath(urlParameters)
}
```

## 使用与回归

改造完成，editor.ts 里就能轻松发请求了：

```ts
const fetchWork = actionWrapper('/works/:id', 'fetchWork')
// dispatch 时
store.dispatch('fetchWork', {
  urlParameters: { id: currentWorkId },
})
```

别忘了修正其他 dispatch 传参的地方：数据结构多套了一层，目前只有 login 页面一处，把原来的 payload 包进 data 即可。

最后验证：打开之前创建的作品编辑页（如 editor/71），Network 里请求成功发出并返回数据，console 里打印的转换后 URL 是 `works/71`。这节完成了获取作品的一半逻辑。特别注意这个第三方库叫 path-to-regexp，以后再遇到动态 URL 转换的问题，第一个想到的就该是它。
