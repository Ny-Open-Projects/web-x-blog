# 20-24-Nitro plugins

上节课深入了解了配置文件，知道了 runtimeConfig 和 appConfig 的异同以及它们和环境变量的关系。但还有一个问题没解决：想在 nuxt.config 这个配置对象中使用 runtimeConfig 的方式。当然，一开始我就明确说过，在 nuxt.config 对象中没法使用 useRuntimeConfig 这样的组合式函数。

第一种方式就是非常原始的、之前就学过的 process.env：直接把配置替换成环境变量。Nuxt 的开发环境本身支持环境变量，所以可行。但这和之前后端的做法一模一样，没什么新意还比较麻烦：要手动输入一长串字符，而且生产环境运行时还需要手动赋值。所以这节课我们追寻一条可以完全使用 runtimeConfig 的方式，同时引出一个新概念：Nitro 这端（server 端）的插件 plugins。

Nitro 允许在特定文件夹中放置插件：注意是在 server 文件夹下新建 plugins 文件夹，里面的文件会自动注册，并在后端初始化的时候被运行。插件还有一个魔力：可以拿到整个后端应用的生命周期，在里面做各种操作。

演示一下。在 plugins 中创建 test.ts，直接 export default，使用已经注册好的全局函数 defineNitroPlugin，里面是一个回调函数，有一个特殊参数叫 nitroApp，类型就是 NitroApp，其实是整个后端的实例。把它打印出来，保存后重启应用，终端就输出了这个实例的信息，上面有非常多的属性和方法。这里最重要的是 hooks 属性，hooks 上有一个 hook 方法，传入生命周期命名，可以贯穿整个请求的开始到结束。比如 request（请求开始）、beforeResponse、afterResponse 等等，看名字就知道钩子发生在什么时机。

测试两个。第一个是 request，请求开始时触发，参数是事件对象，打印 event.path。这个事件对象就是我们熟悉的 H3Event，写接口时大量使用。第二个测试 beforeResponse，第一个参数是 event，第二个参数是 response，从上面可以拿到返回的 body。发送一个请求（比如 /api/test），终端里 onRequest 和 onResponse 都能打印出对应的值：前面拿到 path，后面拿到 body 数据。

这就是插件的大体用法。接下来利用这个注册过程，用 storage 手动 mount 的方式完成 Redis 的注册（不用改生命周期，只在启动时做初始化；如果要在应用启动时初始化第三方库或工具，也可以用 plugin 来完成）。Unstorage 文档里有 Redis 手动注册的过程，我们对它做一些修改：在 plugins 下新建 storage.ts。

同样使用 defineNitroPlugin。因为是初始化时运行，不需要任何生命周期，只需要创建 Redis 实例。第一步用 useStorage 拿到 storage，插件中可以使用我们已有的一系列组合式函数，所以 useRuntimeConfig 也可以用了，这就解决了之前的问题。

先在 nuxt.config 中创建 runtimeConfig（把之前 nitro.storage 的做法注释掉）：

```ts
runtimeConfig: {
  redis: {
    host: '',
    port: 0,
  },
},
```

host 和 port 都只给默认值（空和零），之后用环境变量覆盖。打开 .env 文件，命名规则和之前一样：NUXT 前缀，嵌套 object 用下划线分割。嵌套时也是一层一层分割：NUXT_REDIS_HOST，值为 127.0.0.1；同样添加 NUXT_REDIS_PORT。有这两个参数就够测试用了。

然后回到插件，用 useRuntimeConfig 取出 redis 配置（此时已经能联想出 redis 这个参数），手动创建 Redis driver。把 redis driver 从 Unstorage import 进来，创建 driver 时传入一个 object：base 是加一个前缀，储存时会自动添加，便于区分，可加可不加，这里不加；然后是 host，取 `config.redis.host`；还有 port，取 `config.redis.port`。

driver 创建完毕后直接 mount：storage 上有一个 mount 方法，两个参数，第一个是储存的名称（这里叫 redis，和之前保持一致），第二个传入对应的驱动。这样就完成了手动注册的过程，用这种方式完成了之前在配置文件里完不成的任务。

测试一下。注册的名称还是 redis，所以路由里的代码都不需要修改。首页点击 login 成功后，访问 /api/users/1 可以成功显示，因为设置的 ttl 是二十秒，过期后会失效，这里就不测了，大家可以自行测试。

总结：这节课从上节课的配置文件引出了新话题 plugins，它可以在 Nuxt 启动时做一系列操作，还能拿到 nitroApp 上的各种生命周期。我们的 storage 场景主要没使用生命周期，就是在初始化时完成 driver 的 mount。
