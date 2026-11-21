# 17-4-5-使用高阶函数 actionWrapper 包装 action 通用逻辑

开始对接后端 API 后，action 里写进了大量逻辑，但基本都是重复的：login 和 fetchCurrentUser 的内容几乎一样，无非是用 axios 发不同的请求，然后 commit 对应的数据。往后接入的异步请求只会越来越多，这些重复代码必须想办法省掉。

先分析这两个 action 里真正不同的部分，一共三处：

1. 请求的 URL；
2. axios 用什么方法发送（get 还是 post）、是否携带 payload 数据；
3. commit 的名称。

处理重复逻辑，直接用之前在 hotkeys 里见识过的高阶函数：一个函数返回另一个函数，内部完成通用的处理。高阶函数写起来确实有点抽象，这次结合上次的思路再写一遍，提炼出一套通用做法。

## 三步写出一个高阶函数

**第一步：不管三七二十一，先返回一个和原处理函数签名一模一样的函数。** 原来的 action 长什么样？看 login 的类型：一个或两个参数，第一个是特殊的 `ActionContext`，上面带着一系列属性和方法；第二个是 payload，可有可无。

于是先照原样返回：

```ts
function actionWrapper() {
  return function (context: ActionContext<any, any>, payload?: any) { }
}
```

Vuex 提供了 `ActionContext` 类型，它接受两个泛型。这里直接用 any 就够了：我们只用 context 上的 commit 方法，和具体的数据类型没有关系。第二个参数 payload 加问号表示可选，类型 any。

**第二步：确定参数。** 要通用，就需要把三处差异作为参数传进来：第一个是 URL（string）；第二个是 commitName，也就是 mutation 名称；第三个是请求配置。既然要通用，就不能再用 axios.get/axios.post 这种快捷方式，改用 axios 函数形式，第一个参数 URL，第二个是 config，里面可以配 method、responseType、data 等。config 类型 axios 有暴露，是 `AxiosRequestConfig`，给它一个默认值 `{ method: 'get' }`。

**第三步：把内部重复逻辑放进返回的函数里。** 由于 payload 可能存在，先基于原始 config 创建一个新对象，加上 `data: payload`，然后用它发送请求。这里顺便用 async/await 做一次改写，它是基于 Promise 的语法糖，异步代码写起来更像同步代码，更易于阅读。编辑器也会提示 "This may be converted to an async function"，顺着提示加上 async 关键字即可：

```ts
return async function (context: ActionContext<any, any>, payload?: any) {
  const newConfig = { ...config, data: payload }
  const { data } = await axios(url, newConfig)
  context.commit(commitName, data)
  return data
}
```

拿到响应里的 data 后执行 `context.commit(commitName, data)`，和原来的逻辑一一对应，最后别忘了把 data 返回。

对照 hotkeys 里的 wrapper，流程完全一致：先返回同签名函数，再确定参数，最后放内部逻辑。记住这三步，以后写高阶函数就不容易挠头了。

## 替换原有 action

现在用它替换原来的代码。login 注释掉，换成新写法：第一个参数传 URL，第二个传 mutation 名 login，第三个是个性化配置，因为默认 method 是 get，这里改成 post：

```ts
const login = actionWrapper(url, 'login', { method: 'post' })
```

fetchCurrentUser 同样照搬替换。完成后到页面验证：输入手机号、获取验证码、点击登录，loginByPhoneNumber 和 getUserInfo 都成功调用，登录状态正常更新。

至此，action 重复逻辑的抽取就完成了，用到的就是高阶函数的概念。课后可以把其他 store 里的 action 也替换掉，并把 actionWrapper 这个通用方法放到公共文件（比如 index.ts）里。
