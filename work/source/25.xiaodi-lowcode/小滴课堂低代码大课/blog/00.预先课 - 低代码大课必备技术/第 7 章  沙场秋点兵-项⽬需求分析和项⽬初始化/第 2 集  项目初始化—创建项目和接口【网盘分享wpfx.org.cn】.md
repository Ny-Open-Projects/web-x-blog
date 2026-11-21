# 项目初始化—创建项目和接口

> **导语**：前面几章的练习代码写得比较散，从这一集开始推倒重来，用 Nest CLI 从零建一个干净项目，并一口气生成 user、course 两组 RESTful 资源。本文把创建项目、清理模板、配置跨域、启动排错到验证接口走一遍，同时说明预备课的单项目和正式低代码平台的 pnpm-workspace 多包工程是怎么衔接的。

## 前置知识

- 已经装好 Node.js、pnpm 与 Nest CLI，会创建并运行一个最简 NestJS 项目，可回顾《Nestjs环境搭建和项目创建》。
- 了解 Controller / Service / Module / Entity / DTO 各自的职责。
- 看过《项目初始化—创建React项目和初始配置》，对前后端分目录开发有概念即可。

## 正文

### 为什么要重新建项目

预备课前面几集为了演示装饰器、Provider、拦截器等知识点，在同一个练习工程里堆了不少临时代码。继续往下写只会越来越乱，所以这一集**新建一个独立项目**，之前的工作区代码整体弃用。这其实是个很实用的习惯：知识点练习和正式项目分开，正式项目从干净骨架开始。

操作上：终端 `cd` 到资料里的代码目录，执行 Nest CLI 的创建命令，包管理器选 pnpm 速度更快：

```bash
nest new nest-project
```

第一次执行报了错——因为目录里已经存在一个同名的 `nest-project`（之前练习留下的）。把它移出去再执行就成功了。所以看到「项目已存在」类别的报错时，先检查目标目录，别急着改命令。

### 用 CLI 一次性生成 RESTful 资源

项目建好后，用 Nest CLI 的资源生成器批量产出两套接口骨架：

```bash
nest g resource user
nest g resource course
```

选择 RESTful API 风格后，`src` 下会自动生成一整套文件：模块（module）、控制器（controller）、服务（service）、实体（entity），以及 create / update 两类 DTO。DTO 的作用是对前端传进来的参数做校验，这一步由脚手架先铺好，后面再按业务逐个完善。

> 配套资料：本集对应的工程目录为 `7-2`；需求与原型可参考「全栈低代码平台需求文档.pdf」「全栈多端低代码平台项目大课.pdf」及 `图.drawio`（位于 `笔记+资料-已8期/笔记+资料-已8期/`）。

注意脚手架生成的 Controller 默认没写路径前缀，需要手动补上，让接口按模块归位：

```ts
@Controller('user')
// ...
@Controller('course')
```

### 配置跨域

前后端分离开发时，浏览器从前端页面请求本地后端必然跨域。NestJS 提供两种做法：用框架原生的 `app.enableCors()`，或安装第三方 `cors` 插件。本集用原生方式，写在 `app.listen(3000)` 之前即可：

```ts
// src/main.ts（关键一行）
app.enableCors();
await app.listen(3000);
```

验证方式也简单：随便打开一个别的网页，在浏览器控制台里 fetch 本地接口地址；配好跨域后能正常拿到响应。本集不再展开验证，因为前面的章节已经演示过。

### 启动排错：端口占用

`pnpm start:dev` 启动时报了 3000 端口被占用——原因是之前开发完成的另一个项目还在运行。把它停掉再启动就正常了。遇到这类报错，第一反应应是「本机是不是还有别的服务占着这个端口」，而不是怀疑代码写错。

启动成功后，浏览器访问 `localhost:3000/user` 与 `/course`，都能拿到脚手架默认的 `Hello World` 响应，说明两组资源与跨域配置都通了。最后把 `node_modules` 删掉、代码归入本集目录并提交到本地仓库（是否推到 Git / GitHub 远程仓库按个人习惯）。

### 从单项目到低代码平台的多包工程

这里要分清两个阶段：预备课用 Nest CLI 建的是**单项目**，方便聚焦 NestJS 本身；而正式的低代码平台工程是 pnpm-workspace 管理的**多包仓库**，包含 `client`（React + Vite）、`server`（NestJS）、`share`（公共组件与类型）、`release` 等子包。对照 `代码（已8期）/9-1/lowcode/package.json` 的脚本就能看出来：

```json
{
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "run:share": "pnpm --filter share run dev",
    "build:server": "pnpm --filter server run build"
  }
}
```

`client` 通过 `@lowcode/share: "workspace:^"` 依赖公共包（见 `代码（已8期）/9-1/lowcode/packages/client/package.json`），`tsconfig.json` 则统一开着 `strict`、`jsx: "react-jsx"` 等严格选项。预备课把 Controller/Service/DTO/跨域这套基本功练熟，进正式工程时才不会被目录结构绊住。

## 小结

- 正式项目从干净骨架开始，练习代码不混进来。
- `nest g resource` 一次生成 module / controller / service / entity / DTO 全套 RESTful 骨架。
- 生成的 Controller 需要手动补 `@Controller('user')` 之类的路径前缀。
- 跨域用 `app.enableCors()`，写在 `listen` 之前；端口占用多为本机其他服务未停。
- 预备课是单项目，正式低代码平台用 pnpm-workspace 管理 client / server / share 多包。

## 下一步

建议接着看《NestCli常用命令提高开发效率》——本节只是用了 `nest new` 和 `nest g resource`，下一集系统梳理 CLI 的常用命令，能把这类重复操作再提速一截。之后可以看《Nestjs提供Get和Post请求》，把刚生成的空壳接口替换成真正的业务实现。
