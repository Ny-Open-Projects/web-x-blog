---
title: "NestJS 的管道验证 DTO"
date: 2026-11-17 07:00
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestJS 的管道验证 DTO

> **导语**：接口光能收到参数还不够，得能拦住不合法的参数。本文讲 NestJS 管道（Pipe）的第二个用途：用 DTO 配合 class-validator 做请求体校验。从 `@Body()` 接参、编写 `RegisterDto`、全局开启 `ValidationPipe`，到 `@IsString` / `@Length` 与自定义错误提示，把前端「表单验证」那套思路搬到服务端。

## 前置知识

- 建议先了解《Nest的管道Pipe转换》，理解管道在请求链路中的位置。
- 建议先了解《NestjsRESful风格API开发》，本文沿用其中的控制器与 `@Post` 写法。
- 需要 TypeScript 装饰器与类的基础。

## 正文

### DTO 是什么，为什么像表单验证

DTO（Data Transfer Object）本质是一份**参数约束配置**：规定某个接口的参数必须以什么类型、什么格式传进来。它很像前端做表单校验——提交的账号必须是手机号格式、密码必须够位数，不满足就不给通过。DTO 把同样的事放到服务端做，由管道在请求进入控制器之前完成校验。

### 先把接口改成 POST 并接住请求体

以上一节的 `user` 控制器为起点：它原本只有一个 GET，先改成 POST 的注册方法 `register`，`user.service` 里对应的方法名同步调整。要拿到请求体，用 `@Body()` 装饰器接收，先把数据原样返回给前端，确认到底传了哪些参数：

```ts
@Post()
register(@Body() body) {
  return body;
}
```

在 ApiFox 里用 POST 请求 `/user`，body 传 `name`、`form`、`password` 三个字段，响应里能看到它们被原样带回。这里有个小插曲：讲师一开始把路径写成了 `course`，改回 `user` 才请求成功——联调时路径写错是很常见的低级问题。

此时如果把 `name` 换成 number 类型再发，接口照样通过。原因很简单：还没写 DTO，也没有开启校验。

### 编写 RegisterDto

模块创建时自动生成了 `dto` 目录，把 `create-user.dto.ts` 重命名为 `register.dto.ts`，类名改为 `RegisterDto`。先安装校验依赖 `class-validator`（NestJS 的 `ValidationPipe` 还依赖 `class-transformer` 完成类型转换），再引入 `IsString`、`Length` 两个装饰器：

```ts
import { IsString, Length } from 'class-validator';

export class RegisterDto {
  @IsString()
  name: string;

  @IsString()
  @Length(11, 11)
  form: string;

  @IsString()
  password: string;
}
```

要点：

- 三个字段都加 `@IsString()`，规定必须是字符串；`form` 额外用 `@Length` 限制长度（演示里按 11 位手机号来约束）。
- 多个属性装饰器之间换行分隔，**不要用逗号**——讲师在这里踩过一次语法错误。
- `@Length(min, max, validationOptions?)` 接收三个参数：最小长度、最大长度，第三个是可选的校验选项（可以放 `message`）。

### 关键一步：全局开启 ValidationPipe

只写 DTO 是不生效的。必须在 `main.ts` 里全局开启管道：

```ts
import { ValidationPipe } from '@nestjs/common';

app.useGlobalPipes(new ValidationPipe());
```

然后在控制器的 `register` 方法里引入 `RegisterDto`，把 `@Body()` 的参数类型标注上去，校验才会真正跑起来：

```ts
@Post()
register(@Body() body: RegisterDto) {
  return body;
}
```

### 验证效果与自定义提示

开启之后，非法参数会被拦下并返回明确的错误：

- `name` 传 number → 提示 `name must be a string`。
- `password` 同时传 number → 两条不满足条件的提示一起返回。
- `form` 只传 3 位 → 既提示必须为字符串，也提示长度不满足 11 位。

默认英文提示不够友好时，可以自定义 `message`：

```ts
@IsString({ message: 'name 必须为字符串' })
name: string;
```

`@Length` 的自定义提示要放在**第三个参数**里：

```ts
@Length(11, 13, { message: 'form 长度必须在 11~13 位' })
form: string;
```

这里有个值得记下的坑：`@Length` 的参数必须按顺序传，如果把配置对象塞到第二个 `max` 的位置，会直接报 `is not number`。讲师当场翻了类型定义才确认——不熟的 API 直接看源码或声明文件最快。另外若只想限制最小长度，给 `max` 传一个合适的数值即可，演示里最后用 `min 11`、`max 13` 通过了验证。

### 三步流程

把本节收拢成可复用的流程：

1. 生成 DTO 配置文件，用装饰器写好字段约束。
2. 在 `main.ts` 全局 `useGlobalPipes(new ValidationPipe())`。
3. 在目标接口的 `@Body()` 上标注 DTO 类型，完成「注入」。

### 工程里的严格模式

配套代码 `代码（已8期）/代码（已8期）/8-5/lowcode/packages/client/tsconfig.json` 开启了严格的 TypeScript 检查：

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

在 `strict` 下，DTO 类的属性必须显式标注类型；受 `strictPropertyInitialization` 影响，声明式属性通常会写成 `name!: string` 这样的非空断言形式，避免初始化报错。配套资料：`代码（已8期）/代码（已8期）/8-5/lowcode/packages/server/package.json`、`代码（已8期）/代码（已8期）/8-5/lowcode/packages/server/tsconfig.json`。

## 小结

- DTO 是接口参数的约束配置，作用类似前端表单验证，由管道在进入控制器前执行。
- 用 `@Body()` 接请求体后，先原样返回确认参数，再谈校验。
- `RegisterDto` 里用 `@IsString()`、`@Length(min, max, options?)` 约束字段；装饰器之间换行分隔，不能用逗号。
- 必须在 `main.ts` 全局开启 `ValidationPipe`，并在 `@Body()` 上标注 DTO 类型，校验才生效。
- 自定义 `message` 放 `@IsString({ message })` 或 `@Length` 的第三个参数；参数顺序不能错。

## 下一步

DTO 验证在实战项目里会直接用于注册、登录等接口，建议接着看《项目初始化—接口参数DTO验证》把它接入正式工程；响应与异常的统一处理可以接着看《Nest的响应拦截器》与《Nest的异常拦截器》。
