# 你知道Nest如何进行上传文件吗

> **导语**：前端要把图片传到后端，NestJS 该怎么接收、存到哪、又怎么让浏览器访问到？本文用 `MulterModule` + `FileInterceptor` 走通完整链路：安装依赖、配置磁盘存储并重命名文件、写上传接口、联调验证，最后用 `useStaticAssets` 开放静态访问。文末还会点出两个真实踩过的坑——全局中间件拦截请求，以及 `__dirname` 相对路径导致图片没落到预期目录。

## 前置知识

需要理解 NestJS 的模块与依赖注入，建议先看过《如何理解Nestjs的模块Module》和《什么是装饰器和Nestjs中的应用》；上传接口是 POST 请求，可对照《Nestjs提供Get和Post请求》。本节还会临时注释掉一个全局中间件，相关背景在《掌握Nestjs中间件的使用》。

## 正文

### 准备依赖与上传模块

先在工程里安装 `multer` 及其类型声明 `@types/multer`。然后新建一个专门的 `upload` 模块，把文件上传相关接口集中放进去，而不是散落在业务控制器里——这和前面按业务域拆模块的思路一致。

### 配置 MulterModule：两种方式

在 `upload.module.ts` 的 `imports` 数组里调用 NestJS 提供的 `MulterModule.register({...})`。配置有两种写法：

- **只给 `dest`**：例如 `dest: './temp'`，图片会存进项目新建的临时目录，最省事。但文件名是随机乱码、不带原始后缀，想预览也预览不了，只适合临时存放。
- **自定义 `storage`**（推荐）：用 `multer.diskStorage({ destination, filename })` 自己决定存哪、叫什么。`destination` 里用 Node 原生 `path` 模块的 `join` 拼出目标目录，比如定位到项目工作区下的 `images`；`filename` 里用 `Date.now()` 生成时间戳做文件名，再用 `path.extname(file.originalname)` 取回原始后缀拼上去，最后通过 `callback(null, filename)` 返回。这样存下来的文件既不会重名，又保留 `.jpg` 之类后缀，可以直接预览。

这里有个关键认知：项目编译后运行的是 `dist` 目录里的代码，`__dirname` 指向的是编译结果所在位置，而不是源码目录。所以拼路径时要从 `__dirname` 往回退到工程根，才能把图片统一放到顶层的 `images`，而不是落到 `dist/upload` 下面。口播里演示的「去掉前面的 `../` 会怎样」正是这个陷阱：目录没写对，图片会存进打包后的 `upload` 文件夹中，静态访问自然找不到。

### 写上传接口

在 `upload.controller.ts` 里定义一个 `@Post('image')` 方法，路径即 `http://localhost:3000/upload/image`。三件套：

- `@UseInterceptors(FileInterceptor('file'))`：方法级拦截器，参数为表单里的文件字段名 `file`，来自 `@nestjs/platform-express`。
- `@UploadedFile()`：参数装饰器，把上传的文件对象注入进来，可以打印它的文件名、类型、大小等信息做核对。
- 方法返回一句「上传成功」即可，落盘逻辑已由 Multer 配置完成。

拦截器负责把 multipart 请求里的文件接住并按 storage 规则写盘，控制器只管拿结果，分层很干净。

### 联调验证

用接口调试工具（Apifox / Postman）发一个 POST 到 `/upload/image`，body 选 form-data，加一个名为 `file`、类型为 File 的字段，选一张图片发送。有两点要注意：

- 如果之前定义过全局中间件对所有请求做校验，这一版测试接口会被拦下来，先把它注释掉再发。
- 成功后到 `dist/images` 下能看到以时间戳命名、带正确后缀的图片，打开即可预览；对照只配 `dest` 的乱码文件名，就能看出自定义 `storage` 的价值。

### 开放静态资源访问

上传完还要能访问。在 `main.ts` 里把应用声明为 `NestExpressApplication`，再调用 `app.useStaticAssets(join(__dirname, '..', 'images'), { prefix: '/自定义前缀' })`，把 `images` 目录挂到一个 URL 前缀下。浏览器访问 `http://localhost:3000/前缀/文件名` 就能看到图片。

这里踩过一个很小的坑：`prefix` 忘了写开头的斜杠，访问时直接报「找不到路径的接口」，补上 `/` 后立刻正常。路径拼接、前缀格式这类细节在本地静态资源调试里格外容易漏。

### 关联工程配置

本阶段工程仍是 pnpm workspace 多包结构，根目录 `代码（已8期）/代码（已8期）/8-4/lowcode/package.json` 用 `pnpm --filter ...` 调度各子包：

```json
{
  "name": "lowcode",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "run:share": "pnpm --filter share run dev",
    "run:release": "pnpm --filter release run dev",
    "build:client": "pnpm --filter client run build",
    "build:server": "pnpm --filter server run build",
    "build:release": "pnpm --filter release run build",
    "build:share": "pnpm --filter share run build",
    "start:server": "pnpm --filter server run start:prod",
    "start:release": "pnpm --filter release run start"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/lodash": "^4.14.201",
    "@types/node": "18",
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "typescript": "^5.2.2"
  },
  "dependencies": {
    "@ant-design/icons": "^5.2.6",
    "antd": "^5.11.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

`upload` 模块位于 `server` 子包，配套资料里还有 `packages/server/nest-cli.json`、`packages/server/tsconfig.json` 等配置可对照。预先课把图片存本地只是为了讲清原理；到了正式的低代码平台项目，资源上传会升级为阿里云 OSS 方案，接口形态与这里的 `FileInterceptor` 一脉相承，只是落点从本地磁盘换成了对象存储。

## 小结

- 安装 `multer` 与 `@types/multer`，新建独立的 `upload` 模块承载上传接口。
- `MulterModule.register({ dest })` 最简但文件名乱码不可预览；`diskStorage` 的 `destination` + `filename` 可自定义目录与「时间戳 + 原后缀」文件名。
- 控制器用 `@Post('image')` + `@UseInterceptors(FileInterceptor('file'))` + `@UploadedFile()` 接文件。
- 编译后 `__dirname` 指向 `dist`，拼路径要回退到工程根，否则图片会落进 `dist/upload`。
- `main.ts` 用 `NestExpressApplication` + `useStaticAssets` 挂静态目录，`prefix` 必须以 `/` 开头。

## 下一步

文件上传打通后，课程这一组接口还差删除，建议接着看《后端接口开发—课程的删除接口开发》把 CRUD 收尾。本地磁盘方案只是过渡，进入低代码平台实战后可继续看《低代码项目平台编辑模块—阿里云 OSS 资源上传配置》，把资源上传替换成生产可用的对象存储方案。
