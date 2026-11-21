# Nest的管道Pipe转换

> **导语**：URL 上的动态参数本质都是字符串，可业务里往往要的是 number、boolean。NestJS 的 Pipe 就是干这个的：在参数进入 Controller 之前完成类型转换，转不动直接返回 400。本文用 course 的动态路由把 ParseIntPipe、ParseBoolPipe 讲透，并顺带列出 NestJS 内置的全部转换型 Pipe，以及 Pipe 的另一半职责——DTO 验证。

## 前置知识

- 熟悉 Controller 里 `@Get()`、`@Param()` 等装饰器与动态路由参数的写法，可回顾《详解Nestjs控制器《上》》。
- 已经看过《Nest的响应拦截器》《Nest的异常拦截器》，知道请求在到达处理方法前会经过一层预处理。
- 了解 TypeScript 的基本类型，知道 string 与 number、boolean 的区别。

## 正文

### Pipe 的两大职责

NestJS 里的 Pipe 主要做两件事：

1. **转换**：把前端传进来的参数转换成后端需要的类型；
2. **验证**：结合 DTO 校验参数是否合法，不合法就抛错。

本集聚焦第一件——转换；验证部分留到《Nest的管道验证DTO》展开。转换这件事听着小，却省掉了每个接口里手写 `Number(id)`、再判断 `isNaN` 的重复代码。

### 第一个例子：ParseIntPipe 约束动态路由参数

打开 course 的 Controller，找到一个带动态路径的 GET 请求。路径参数从 URL 里取出来永远是字符串，如果业务逻辑要的是数字，就把类型标注成 `number`，并把 NestJS 原生的 `ParseIntPipe` 放进参数装饰器的第二个参数：

```ts
@Get(':id')
findOne(@Param('id', ParseIntPipe) id: number) {
  return this.courseService.findOne(id);
}
```

（工程里的接口命名与具体实现以 `代码（已8期）/8-5/lowcode/packages/server` 下源码为准。）

保存后验证两种请求：

- 请求 `/course/abc`：返回 **400**，响应里的 message 提示「验证失败，期望的是数字字符串」——因为 `abc` 转不成 number；
- 请求 `/course/123`：正常返回数据。

也就是说，类型转换失败时 Pipe 会直接拦下请求，Controller 里的 `id` 拿到的永远是干净的 number。

### NestJS 内置的转换型 Pipe

NestJS 提供了一整套现成的转换 Pipe，按需替换即可：

| Pipe | 作用 |
| --- | --- |
| `ParseIntPipe` | 转整数 |
| `ParseFloatPipe` | 转浮点数 |
| `ParseBoolPipe` | 转布尔值（true / false） |
| `ParseArrayPipe` | 转数组 |
| `ParseUUIDPipe` | 校验并转 UUID |
| `ParseEnumPipe` | 校验并转枚举值 |
| `DefaultValuePipe` | 参数没传时补一个默认值 |

最后一个 `DefaultValuePipe` 值得单独说：有些参数允许前端不传，用它就能在后端自动补默认值（比如 id 默认给 1），避免方法里到处写 `id ?? 1`。

### 第二个例子：ParseBoolPipe

把上面的 `ParseIntPipe` 换成 `ParseBoolPipe`，再请求 `/course/123`——因为 `123` 不是 boolean，同样返回 400 并提示验证失败；只有传 `true` 或 `false` 才能成功拿到响应。

这个例子说明转换型 Pipe 的用法是统一的：**换一个 Pipe，就换一套类型约束**，Controller 代码本身几乎不用动。其余几个 Pipe 可以照这个套路自行演练。

### 什么时候该用、什么时候别用

讲师也点明了：这些转换型 Pipe 在实际项目里用得不算多，真正高频的是下一节的 DTO 验证。原因不难理解——动态路由参数通常就一两个 id，而真正复杂的是请求体（body）里那一大堆字段，那才是 DTO + 验证管道的主场。所以本集的价值在于把「Pipe 会在参数进方法前先跑一遍」这个机制建立起来。

放到低代码平台里，发布页面按 id 取组件、编辑模块按 id 取页面数据，这些动态参数用 `ParseIntPipe` 收口，能挡掉大量脏输入。工程结构可对照 `代码（已8期）/8-5/lowcode/package.json` 的 `run:server`、`build:server` 脚本。

## 小结

- Pipe 有转换与验证两大职责，本集讲转换，DTO 验证留到下一节。
- URL 动态参数是字符串，用 `ParseIntPipe` 转成 number，转不动直接 400。
- 内置 Pipe 覆盖 int / float / bool / array / UUID / enum，`DefaultValuePipe` 负责补默认值。
- 用法统一：把它作为 `@Param()` 等参数装饰器的第二个参数传入即可。
- 转换型 Pipe 用在少量路径参数上，复杂请求体更适合 DTO 验证。

## 下一步

建议接着看《Nest的管道验证DTO》——讲师明确说了那才是 Pipe 用得最多的场景，本集建立的「参数先过一层处理」机制会在那里配合校验规则发挥真正作用。也可以回头看《你知道Nest如何进行上传文件吗》，把 NestJS 请求预处理的其它能力补齐。
