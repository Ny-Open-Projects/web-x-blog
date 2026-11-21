# 如何理解 NestJS 的模块 Module

> **导语**：Provider 解决了"对象从哪来"，Module 则解决"代码怎么组织"。本文系统梳理 NestJS 中模块的定位：主模块如何聚合子模块、共享服务如何跨模块复用、@Global 全局模块与 forRoot 动态模块各自的适用场景。读完你能判断什么时候该拆模块、什么时候该导出服务，也能看懂项目里 @Module 装饰器的每一行配置。

## 前置知识

上一篇《如何理解Nestjs的提供者Providers》讲了依赖注入与 Provider 工厂模式，本篇的"共享模块"会与它做对比，建议先读。若对 @Module、Controller、Service 三者的职责还不熟，可先补《什么是装饰器和Nestjs中的应用》与《详解Nestjs控制器《上》》。

## 正文

### Module 到底是什么

在 NestJS 里，模块是组织和管理应用功能的一种方式，可以理解成一个容器——和 Provider 一样是容器，但层级更高。它把相关的组件、Provider、路由聚合在一起，让应用能被拆分成更小、可复用的单元，再组合成一个整体。

落到代码上，app.module.ts 就是主模块入口。随着业务变多，主模块不再直接塞满所有 Controller 和 Service，而是引入 UserModule、CourseModule 这样的子模块——这正是"拆分成更小、可复用组件"的体现。打开 user.module.ts 会看到，controllers 聚合了路由，providers 聚合了提供者，一个模块就把用户相关的全部能力收拢在一起。

### 共享模块：把服务导出给别的模块用

模块默认是封闭的：UserModule 里的 Controller 想调用 CourseModule 中 CourseService 的 findAll，直接注入是拿不到的。做法是两步——在 CourseModule 里通过 exports 把 CourseService 导出，再在 UserController 里像声明普通依赖一样注入 CourseService，之后调用 this.courseService.findAll() 即可。演示中刷新用户接口，成功拿到了课程模块提供的服务，说明共享生效。

它和上一节的 Provider 工厂模式很像，但有个关键区别：工厂模式（useFactory）在返回服务之外还能顺带执行其他业务逻辑；共享模块只是"导出—引入"这一层声明，不额外夹带逻辑。需要加工逻辑时用工厂，纯粹复用实例时用共享模块，各司其职。

```ts
@Module({
  controllers: [CourseController],
  providers: [CourseService],
  exports: [CourseService], // 导出后其他模块才能注入
})
export class CourseModule {}
```

（该写法对应视频演示的 course 模块结构；配套工程见 `代码（已8期）/代码（已8期）/8-4/lowcode/`。）

### 全局模块：一次声明，处处可用

共享模块是一对一的：哪个模块要用，就得在 imports 里引一次。当模块变多，比如用户模块、视频模块、其他业务模块都想用课程模块里某个全局配置时，逐个引入就很啰嗦。这时可以用 @Global() 把模块声明为全局模块，效果类似 Vue 里的全局状态管理——注册一次，任意模块直接注入。

具体做法：用 @Global() 装饰 CourseModule，在 providers 里通过 useValue 提供一个全局配置对象（例如包含 baseUrl 的地址对象），并在 exports 中把它抛出。之后在 UserController 里只需多声明一条依赖（如 GlobalUrl）就能直接读到，无需再 import CourseModule。演示里浏览器刷新后成功打印出了这个全局 URL，验证全局注册完成。

区分一下两个 provider 写法：全局配置这种"值"用 useValue；若全局提供的是一个类，则改用 useClass。

### 动态模块：让模块接收参数

静态的全局 URL 是写死的，如果想在使用方动态拼接路径，就要用动态模块。思路是给模块加一个静态方法（约定叫 forRoot），接收 options 参数，返回一个描述模块的对象，其中 module 指向 CourseModule 本身——少了这个属性会直接报错。返回值类型可以用 NestJS 原生的 DynamicModule 标注。

在方法内部，把全局 URL 改成模板字符串，用 options.path 参与拼接；再用 exports 把 provider 抛出。使用方在 AppModule 的 imports 里不再直接写 CourseModule，而是调用 CourseModule.forRoot({ path: 'api' })，由 IDE 提示补全参数。演示中还踩了一个典型坑：模板字符串里漏了取值，写成整个 options 对象，结果拼出 [object Object]；改成 options.path 后才正确得到预期地址。

```ts
@Global()
@Module({})
export class CourseModule {
  static forRoot(options: { path: string }): DynamicModule {
    return {
      module: CourseModule,
      providers: [
        {
          provide: 'GLOBAL_URL',
          // 用模板字符串拼接 options.path，地址前缀由站点配置提供
          useValue: { baseUrl: `<站点基础地址>/${options.path}` },
        },
      ],
      exports: ['GLOBAL_URL'],
    };
  }
}
```

调用侧：

```ts
@Module({
  imports: [CourseModule.forRoot({ path: 'api' })],
})
export class AppModule {}
```

（示例还原视频中 forRoot 动态传参、模板字符串拼接与 DynamicModule 返回结构；工程配置见 `代码（已8期）/代码（已8期）/8-4/lowcode/package.json`，其 scripts 通过 `pnpm --filter` 管理 client / server / share / release 子包。）

动态模块和全局模块在业务项目里使用频率并不高，作为了解即可；真正天天打交道的是最基础的 @Module 组织与 exports 共享。

## 小结

- Module 是比 Provider 更高层的容器，用 @Module 把 Controller、Provider、路由聚合为可复用单元。
- app.module.ts 作为主模块引入 UserModule、CourseModule 等子模块，避免所有逻辑堆在一个文件。
- 跨模块复用服务：提供方 exports，使用方注入，这是共享模块；与可执行额外逻辑的 useFactory 工厂模式区分开。
- @Global() + useValue/exports 实现全局模块，一次注册处处可注入，类比 Vue 全局状态。
- 动态模块用 static forRoot(options) 返回含 module 的 DynamicModule，调用处以 CourseModule.forRoot({...}) 传参；注意模板字符串要取到 options.path。

## 下一步

模块讲完，NestJS 进阶用法还差"请求进入应用后如何被层层处理"这一环。建议接着看《掌握Nestjs中间件的使用》，它正好是同章下一集，会讲自定义中间件、全局中间件与第三方 CORS 中间件，和本篇的模块注册（NestModule 的 configure）直接衔接。想继续深入可再跟进《Nest的响应拦截器》与《Nest的管道Pipe转换》。
