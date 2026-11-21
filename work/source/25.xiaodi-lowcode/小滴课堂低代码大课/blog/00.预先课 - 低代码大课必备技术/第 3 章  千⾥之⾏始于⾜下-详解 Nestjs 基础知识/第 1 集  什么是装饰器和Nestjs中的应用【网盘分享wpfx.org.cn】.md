# 什么是装饰器和Nestjs中的应用

> **导语**：装饰器（Decorator）是 NestJS 的基石。本文用纯 TypeScript 代码逐一演示四种装饰器——类、属性、方法、参数装饰器，并对照它们在 NestJS 框架（@Controller、DTO 校验、@Post、@Body 等）中的真实用法，帮你建立扎实的认知。

## 前置知识

阅读前建议先看《Nestjs环境搭建和项目创建》，确保本地已装好 Node 与 TypeScript 环境。本文涉及 `tsconfig.json`、`ts-node` 等工具，需对 TypeScript 有最基础的了解。

## 正文

### 装饰器是什么

本质上，**装饰器就是一个函数**。当你把它（通过 `@` 符号）放到类、属性、方法或参数上方时，框架会把被修饰的目标作为参数「喂」给这个函数，从而让你在不动原结构的前提下，给目标增加或修改行为。

在动手前，新建一个 `test.ts` 并初始化 TS 配置：

```bash
tsc --init
```

由于装饰器属于实验性特性，需要在 `tsconfig.json` 中打开：

```json
{
  "compilerOptions": {
    "experimentalDecorators": true
  }
}
```

若本机没有 `ts-node`（用于直接执行 ts 文件），可执行 `npm install -g ts-node`。

### 类装饰器（Class Decorator）

定义一个类，并在它顶部叠加一个装饰器：

```ts
function doc(target: any) {
  console.log(target);
}

@doc
class StudyClass {
  constructor() {}
}

const a: any = new StudyClass();
```

执行 `ts-node test.ts` 后，`doc` 会打印出 `StudyClass` 这个类本身——也就是说，类装饰器接收的 `target` 就是**被修饰的类**。

这与下面这种「手动传参」写法等价：

```ts
doc(StudyClass);
```

利用这一点，你可以给类的原型增加属性：

```ts
function doc(target: any) {
  target.prototype.name = '小滴课堂';
}

@doc
class StudyClass {}

const a: any = new StudyClass();
console.log(a.name); // 小滴课堂
```

原本 `StudyClass` 没有 `name` 属性，装饰器在原型上补了一个，相当于「修饰」了这个类。

**在 NestJS 中的应用**：打开任意 Controller，例如 `user.controller.ts`，`@Controller()` 就是一个类装饰器。它把当前类标记为控制器，框架据此识别路由归属。

### 属性装饰器（Property Decorator）

属性装饰器接收两个参数：`target`（类的原型对象）与 `propertyKey`（被修饰的属性名）。

```ts
function doc(target: any, propertyKey: string) {
  console.log(target, propertyKey);
}

class TargetClass {
  @doc
  title: string;

  constructor() {
    this.title = '小滴课堂';
  }
}
```

执行后会打印出类的原型对象以及被修饰的属性名 `title`。

**在 NestJS 中的应用**：DTO 校验就是典型场景。定义一个接口接收哪些前端参数、各有什么约束，常用 `class-validator` 提供的属性装饰器：

```ts
import { IsString, IsNotEmpty } from 'class-validator';

export class RegisterDto {
  @IsString()
  @IsNotEmpty()
  username: string;
}
```

`@IsString()` 限制该属性必须是字符串且不能为空，对应「属性装饰器」的用法。

### 方法装饰器（Method Decorator）

方法装饰器接收三个参数：`target`（原型对象）、`propertyKey`（方法名）、`descriptor`（方法描述符）。

```ts
function doc(target: any, propertyKey: string, descriptor: any) {
  console.log(target, propertyKey, descriptor);
}

class TargetClass {
  @doc
  getTitle() {}
}
```

打印出的 `descriptor` 是对象，包含 `value`（函数体）、`writable`（是否可写）、`enumerable`（是否可枚举）、`configurable`（是否可配置）等描述信息。

**在 NestJS 中的应用**：控制器里定义接口方法时，`@Post()`、`@Get()` 就是方法装饰器，赋予该方法对应的 HTTP 请求能力：

```ts
@Controller('user')
export class UserController {
  @Post('register')
  register() {}

  @Get('list')
  findAll() {}
}
```

### 参数装饰器（Parameter Decorator）

参数装饰器接收 `target`、`propertyKey` 以及 `index`（参数在方法形参列表中的下标，从 0 开始）。

```ts
function doc(target: any, propertyKey: string | undefined, index: number) {
  console.log(target, propertyKey, index);
}

class TargetClass {
  getTitle(title: string, @doc length: number) {}
}
```

`title` 下标为 0，`length` 下标为 1，装饰器据此定位要修饰的是第几个参数。

**在 NestJS 中的应用**：`@Body()` 就是参数装饰器，用来提取请求体并绑定到方法参数：

```ts
@Post('register')
register(@Body() registerDto: RegisterDto) {}
```

框架自动把 POST 请求体解析后注入 `registerDto`，后端即可直接拿到前端传来的数据。

## 小结

- 装饰器本质是一个函数，通过 `@` 叠加在被修饰目标上，接收该目标作为参数。
- TypeScript 共四类装饰器：类、属性、方法、参数，分别接收不同参数（类/原型对象、属性名、方法描述符、参数下标）。
- 使用装饰器前需在 `tsconfig.json` 开启 `experimentalDecorators`。
- NestJS 中 `@Controller()` 是类装饰器，`class-validator` 的 `@IsString()` 等是属性装饰器，`@Post()/@Get()` 是方法装饰器，`@Body()` 是参数装饰器。
- 装饰器把「路由、校验、参数提取」等横切逻辑与业务代码解耦，是 NestJS 约定优于配置设计的核心。

## 下一步

理解了装饰器后，下一步建议接着看《后端接口开发—用户的注册接口开发》，看这些装饰器如何在真实的用户注册接口中组合使用（@Controller、@Post、@Body、DTO 校验与 JWT）。
