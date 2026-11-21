# 12-15-koa session 源代码分析第二部分

上节课分析了 koa-session 的赋值流程：通过 context.js 和 session.js 两个类的相互作用，把一个 JSON 对象经过 Base64 编码和加密，放进名为 egg_session 的 Cookie，并通过 Set-Cookie 响应头返回，让客户端浏览器持久化这些信息。

赋值分析完了，再次访问时要判断 Session 是否存在，对应的是取值过程，这就是源码解析第二部分的任务。先设想一下：它应该和赋值正好相反，从 Cookie 中把数据 decode 出来。是不是这样？一起来看。

## 从 getter 到 ContextSession.get

代码里有 Session 的读取逻辑，比如 controller 里写了 `ctx.session.username`。取值会触发 getter：getter 里 return `this[CONTEXT_SESSION].get(...)`。所以 `ctx.session.username` 实际转化为对 ContextSession 实例调用 get，再从返回结果上取 username。

CONTEXT_SESSION 之前已经分析过：是扩展 context 时用 Symbol 定义的属性，保存着一个 ContextSession 类的实例化对象。现在转入 ContextSession 类，看它的 get 方法。

## get：从 Cookie 初始化

get 方法开头是一些边界条件的判断，比如 Session 已存在就直接返回，略过。关键在这一行的注释："create an empty session or init from cookie"。这里出现一个特别的东西 `this.store`，它支持从外部传入一个存储器做外部存储。这里只分析默认情况，store 不存在，于是走到 `initFromCookie`，最终 return `this.session`。

`initFromCookie` 顾名思义，数据从 Cookie 里初始化。核心一句是 `const cookie = ctx.cookies.get(key)`，从 Cookie 中取值。取到的值是经过 encode 的，必然有一个解码过程。往下看，try 里执行 `opts.decode(cookie)` 返回 JSON，也就是解析 Base64 编码后的 Cookie 内容。和猜想一致：从 Cookie 取出，再做解析，拿到当初保存的那段 JSON 对象。catch 是错误处理，还有有效性检查，略过。

最终使用的是 `this.create(json)`，这个方法上节课见过：内部就是 `new Session(this, val)` 进行创建，最终 `this.session` 等于 Session 实例返回的对象。

## 取到值

这个实例上有什么？除了应有尽有的业务数据，还有一些带下划线的私有属性，包括 session context 对象、ctx 之类。get 的最后一步把 `this.session` 返回出去，所以 `ctx.session.username` 等于在这个对象上取值，经过 decode 之后里面确实有 username，取出来就是 viking。整个取值过程结束。

## cookie session 的优劣

分析完毕可以发现：默认配置下，它用 Cookie 存储全部 Session 信息，实现的是一种 "cookie session" 方式。这对服务器比较轻松，服务器端不需要额外记录任何 Session，所有信息都加密记录在 Cookie 字符串里。

但这样做限制也不少。一是大小限制：Cookie 里不能存太多信息，存多了 Cookie 会变得很大、字符串很长，突破大小限制；二是安全考虑：一旦 Cookie 泄露，整个用户信息就泄露了。

## 外部存储的入口

同时，略过的代码里反复出现了 externalKey 和 store 两个东西。其实 koa-session 支持自定义的外部存储（external session stores），存储系统可以是本机内存、Redis，也可以是 MongoDB 等远程数据库。只要按它的约定实现 get 和 set 两个方法，就可以接入外部存储，当然这会突破 Cookie 的限制，但也有其他弊端。

看 index.js 最开始的中间件处理：如果设置了外部存储，就会从外部初始化，也就是走 `initFromExternal` 分支，对应方法就在那里。建议课下把这部分代码读一遍当作业，有了这两节课的基础，看起来应该不难。

下节课我们验证源码研究的成果：使用一个外部存储器（这里直接用内存）保存 Session 信息，看看它和 Cookie 方式有怎样的区别。
