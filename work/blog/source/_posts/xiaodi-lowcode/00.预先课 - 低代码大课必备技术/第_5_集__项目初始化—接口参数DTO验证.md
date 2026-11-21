---
title: "项目初始化—接口参数DTO验证"
date: 2026-11-17 03:38
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# 项目初始化—接口参数DTO验证

> **导语**：DTO 写好了不等于会生效——还必须全局开启 `ValidationPipe`，接口才会真的按装饰器规则校验入参。本文把项目初始化阶段的这一步讲清：安装校验依赖、在 `main.ts` 用 `useGlobalPipes(new ValidationPipe())` 开全局管道、给注册/创建课程/修改课程/删除课程补齐各自的 DTO，并解释 `@IsNotEmpty`、`@IsString`、`@IsNumber` 的选项含义。读完你会明白「校验为什么不生效」以及「字段级错误提示从哪来」。

## 前置知识

建议先理解管道在请求生命周期里的位置，可对照《Nest的管道Pipe转换》与《Nest的管道验证DTO》；异常返回如何把校验提示送回前端，见《项目初始化—接口响应和异常拦截器》。本节以《后端接口开发—用户的注册接口开发》的注册接口为第一条落地案例。

## 正文

### 为什么 DTO 写好了还要「开启」

`CreateUserDto`、`CreateCourseDto` 这类文件里只是用装饰器声明了规则，比如某个字段不能为空、必须是字符串。这些声明本身不会自动执行，需要一条管道在参数进入 Controller 之前触发校验。最省心的做法是全局开启：在入口 `main.ts` 里调用

```ts
app.useGlobalPipes(new ValidationPipe());
```

`ValidationPipe` 从 `@nestjs/common` 引入，`new` 实例化后作为参数传进 `useGlobalPipes`。开启一次，全工程所有声明了 DTO 的接口都受约束，不必在每个控制器上重复挂管道。

配套要安装校验依赖 `class-validator`。安装完成、管道开启后，启动项目若报「`CreateUserDto` 找不到」，多半是重命名 DTO 后旧引用没清干净，把使用到旧名字的位置删掉或改掉即可，等正式开发接口时再补回来。

### 注册接口：把 DTO 挂到参数上

以用户注册为例，把注册接口的 DTO 贴进 `user` 相关的 DTO 目录，然后在 POST 方法的参数上声明这个类型。声明之后调用接口，管道就会自动校验：字段缺失、类型不符都会在进入业务逻辑之前被拦下。登录接口、用户查询接口同理，需要校验就新建对应的 DTO 文件——这一步留作练习自行补齐。

### 课程相关三份 DTO 的校验规则

课程接口按操作拆成三份 DTO，查询接口是 GET、不带参数，因此不需要 DTO：

- **`CreateCourseDto`（创建课程）**：`title` 等字段用 `@IsNotEmpty()` 约束「不能为空」，并配了自定义提示文本；再用 `@IsString()` 限制「必须为字符串」。几条规则叠起来，前端传空值或传数字都会被挡住。
- **`UpdateCourseDto`（修改课程）**：除「不能为空」「必须为字符串」外，还用到 `@IsNumber()`，并通过选项把 `allowNaN`、`allowInfinity` 都设为 `false`——即不允许 `NaN`，也不允许正无穷/负无穷这种非法数值。口播里念的 `allow num`、`allow infinity` 对应的就是这两个选项。
- **`DeleteCourseDto`（删除课程）**：复制一份配置改名而来，同样包含 `@IsNotEmpty()` 与 `@IsNumber()` 一类约束，用来校验删除时传入的标识。

这里能看出 DTO 的设计原则：**按操作建类，而不是一个 DTO 通吃所有接口**。创建、修改、删除要校验的字段集合并不相同，拆开才不会互相干扰。

### 校验提示如何回到前端

管道校验失败会抛异常，异常过滤器负责把它转成响应。前面《后端接口开发—课程的修改接口开发》里专门处理过这件事：异常过滤器不能只取 `exception.message`，要通过 `exception.getResponse().message` 才能拿到 DTO 的字段级提示（例如「title 必须为字符串」）。两处配合起来，前端才能精确知道是哪个参数出了问题，表单上做对应标红。

对低代码平台而言这一层尤其关键：组件属性、页面配置都由 Schema 驱动，字段多、嵌套深，靠手写 `if` 逐个判断不现实。「DTO 声明规则 + 全局管道 + 统一异常返回」这套组合，本质上就是服务端对结构化入参做 Schema 校验，思路与低代码引擎校验组件配置完全一致。

### 关联工程与配套资料

前端 `client` 子包开启了严格模式，和 DTO 的强约束思路相互呼应，见 `代码（已8期）/代码（已8期）/9-1/lowcode/packages/client/tsconfig.json`：

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

根目录 `9-1/lowcode/package.json` 里是 `pnpm --filter ...` 的多包脚本，`server` 子包承载这些 DTO 与管道配置。配套资料：`笔记+资料-已8期/笔记+资料-已8期/全栈低代码平台需求文档.pdf`，以及 `全栈多端低代码平台项目大课.pdf`、`图.drawio`，需要对照需求字段与结构图时可按相对路径查阅。

## 小结

- DTO 装饰器只是声明规则，必须在 `main.ts` 用 `app.useGlobalPipes(new ValidationPipe())` 全局开启管道才会生效。
- `ValidationPipe` 来自 `@nestjs/common`；校验依赖需安装 `class-validator`。
- 注册、创建课程、修改课程、删除课程各自建 DTO；GET 查询无入参，不需要 DTO。
- 常用规则：`@IsNotEmpty()` 非空并支持自定义提示、`@IsString()` 限字符串、`@IsNumber({ allowNaN: false, allowInfinity: false })` 限合法数值。
- 字段级错误提示要靠异常过滤器从 `exception.getResponse().message` 取值，与全局管道配合才能回传前端。

## 下一步

DTO 与管道就绪后，就可以把校验过的接口接到前端表单上，建议接着看《页面和数据联调—课程创建和编辑模块开发》，实际体验参数不合法时前端如何收到精确提示。想把管道机制本身吃透，可回看《Nest的管道验证DTO》与《Nest的管道Pipe转换》。
