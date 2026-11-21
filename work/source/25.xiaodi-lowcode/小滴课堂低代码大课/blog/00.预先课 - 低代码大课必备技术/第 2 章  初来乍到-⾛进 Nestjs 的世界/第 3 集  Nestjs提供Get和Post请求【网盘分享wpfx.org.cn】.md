# NestJS 提供 Get 与 Post 请求

> **导语**：路由是后端服务的第一道门面。本文从一份最精简的 NestJS 工程出发，讲清 @Controller 与 @Get / @Post 装饰器如何定义请求方法与路径、setGlobalPrefix 如何统一加全局前缀，以及为什么 Post 接口要借助 Apifox 这类工具来调试。读完你能独立把默认的 Hello World 接口改造成带层级路由的 GET / POST 接口。

## 前置知识

建议先掌握《Nestjs环境搭建和项目创建》与《Nestjs的基本介绍》，能跑通 start:dev 并认识 main.ts、app.module.ts 的分工；再了解《什么是装饰器和Nestjs中的应用》，对"用装饰器声明路由"会有更直觉的理解。控制反转与依赖注入可参看《如何理解Nestjs的提供者Providers》。

## 正文

### 从最简工程跑起来

为了保证知识点干净，先把上一节用快捷命令生成的 user 文件夹删掉，并从 AppModule 的 imports 里移除 UserModule 的引入，只留最小骨架。项目以 start:dev 运行后，浏览器访问 localhost:3000 会看到返回的 Hello World 字符串；打开开发者工具的 Network 面板可以看到，这是一个没有附带路径的 GET 请求，指向根地址。

请求是怎么被处理的？链路很固定：main.ts 作为入口启动服务，NestJS 随后读取 AppModule 中登记的 controllers 与 providers，再由 AppController 上的 @Controller 装饰器接管路由，最后调用注入进来的 AppService。

这里顺带复习控制反转：想在 Controller 里用某个 Service，不需要自己 new 一个实例，只要在构造函数里声明 AppService，实例化和依赖关系都交给 NestJS 容器完成。声明即所得，是 NestJS 写法简洁的根源。

### 换请求方法：把 @Get 改成 @Post

定义请求方法的成本几乎为零。默认接口上标的是 @Get('hello')，把它换成 @Post() 后，同一路径就只接受 POST 请求了。装饰器即契约，方法类型、路径都写在装饰器里，不用去改动路由表文件。

### 加路径：类前缀 + 方法路径

真实项目里接口一多就必须分层。做法分两级：在类上写 @Controller('app') 给这一组接口统一加前缀，再在方法上写 @Get('get') 细分具体路径，最终得到 /app/get。启动着 start:dev 时保存即热更新，浏览器访问 /app/get 就能拿到返回的 Hello Nest。

这一步最能体现 NestJS 相对 Express 的提效：在 Express 里要新建路由文件、写路由定义、再层层引入，代码散落多处；NestJS 把这些约定收敛到装饰器参数里，配置即完成。

```ts
@Controller('app')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('get')
  getHello(): string {
    return this.appService.getHello();
  }

  @Post('post')
  postHello(): string {
    return this.appService.getHello();
  }
}
```

（写法对应视频演示的 @Controller('app') 与 @Get / @Post 分层；配套工程配置见 `代码（已8期）/代码（已8期）/8-2/lowcode/package.json`。）

### 全局前缀：setGlobalPrefix

如果还想给整个应用再加一层顶级路径，不要在 main.ts 里逐个接口改，而是调用 app.setGlobalPrefix('api')。设置后原来的 /app/get 会请求失败，必须改成 /api/app/get 才能正常返回 Hello Nest。全局前缀适合统一区分版本（如 /api）或给所有接口加命名空间，一处配置、全站生效。

```ts
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.setGlobalPrefix('api');
  await app.listen(3000);
}
bootstrap();
```

注意这个前缀是"全局"的，前端与接口调试工具里的地址都要同步带上，否则很容易误判成接口挂了。

### 用 Apifox 调试 POST 请求

GET 可以直接在浏览器地址栏发，POST 不行——浏览器地址栏只会发 GET。演示里把某个接口改成 @Post 后，改用 Apifox 新建一个 POST 练习接口，填入 http://localhost:3000/api/app/post 这样的完整路径，选择 POST 方法后点击发送，成功返回 Hello Nest。

顺带记录一个常见失误：第一次运行时把方法选成了 GET，工具提示方法设置错误，改成 POST 才通。接口联调时，"方法、路径、全局前缀"三者要逐项核对，比盲目怀疑业务逻辑更高效。

### 配套工程

本篇所在的示例工程是一个 pnpm workspace 仓库，pnpm-workspace.yaml 里用一条规则纳入所有子包：

```yaml
packages:
  - "packages/*"
```

该片段来自 `代码（已8期）/代码（已8期）/8-2/lowcode/pnpm-workspace.yaml`；根目录 package.json 里声明了 react、antd、typescript 等依赖（见同目录 `代码（已8期）/代码（已8期）/8-2/lowcode/package.json`）。理解工程结构，有助于把这里的接口代码放到正确的子包里。

## 小结

- 请求链路：main.ts 启动 → AppModule 登记 controllers/providers → @Controller 接管路由 → 调用注入的 Service。
- @Get 改 @Post 即可切换请求方法，装饰器就是接口契约。
- 路径分两级：@Controller('app') 类前缀 + @Get('get') 方法路径，组合成 /app/get；比 Express 手写路由文件省事。
- app.setGlobalPrefix('api') 给全站接口加顶级前缀，设置后所有地址都要同步更新。
- POST 无法用浏览器地址栏调试，需借助 Apifox 等工具，并核对方法、路径、前缀三要素。

## 下一步

GET / POST 只是路由的起点，接下来要系统认识 Controller 本身。建议接着看《详解Nestjs控制器《上》》，把参数获取、路由组织补全；再跟进《NestjsRESful风格API开发》，学习按 RESTful 规范设计一组接口；若想把本篇的"声明即所得"理解得更透，可回头巩固《什么是装饰器和Nestjs中的应用》。
