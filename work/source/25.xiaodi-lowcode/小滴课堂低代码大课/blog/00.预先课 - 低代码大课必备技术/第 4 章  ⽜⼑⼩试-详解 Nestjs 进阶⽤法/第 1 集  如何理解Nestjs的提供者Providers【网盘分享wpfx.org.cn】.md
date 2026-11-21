# 如何理解Nestjs的提供者Providers

> **导语**：Providers（提供者）是 NestJS 依赖注入体系的容器。本文从「它是什么、为什么要它」讲起，逐一演示最基础的类注入、自定义名称注入、自定义值注入，以及跨模块复用依赖的工厂模式（useFactory），帮你彻底搞懂 `@Injectable`、`@Inject` 与 `providers` 数组的协作。

## 前置知识

阅读前建议先看《什么是装饰器和Nestjs中的应用》，理解装饰器与 `@Injectable` 的基本用法。本文会频繁用到模块（Module）与控制器（Controller）的配合。

## 正文

### Providers 是什么：依赖的容器

新建项目时，`app.module.ts` 是主入口模块，里面默认带 `AppController`、`AppService`。实际开发中可以删掉这些占位代码，主模块只负责引入其他业务模块。

每个业务模块（如 `user.module.ts`）通过 `@Module` 装饰器声明时，都有一个 `providers` 属性。它本质上是一个**容器**：你在数组里放进什么依赖，NestJS 就会帮你在控制器中按需注入并提供实例，省去自己 `new` 对象的麻烦。

```ts
@Module({
  controllers: [UserController],
  providers: [UserService],
})
export class UserModule {}
```

`providers: [UserService]` 是快捷写法，等价于后面会讲的标准写法。被注入的类需要加 `@Injectable()` 类装饰器（从 `@nestjs/common` 引入），NestJS 才会识别并管理它的生命周期。

### 基础用法：注入业务服务

只要把 `UserService` 放进 `providers`，并在控制器构造函数里声明，就能直接使用：

```ts
@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  findAll() {
    return this.userService.findAll();
  }
}
```

NestJS 会扫描声明、自动实例化，控制器无需关心对象怎么创建。

### 自定义名称注入（useClass + @Inject）

如果想给 Provider 起一个自定义 token 名称，把数组元素从「类名」改为「对象」：

```ts
providers: [
  {
    provide: 'ChatClass',
    useClass: UserService,
  },
]
```

使用时必须通过 `@Inject('ChatClass')` 显式指定名称：

```ts
constructor(@Inject('ChatClass') private readonly chatClass: UserService) {}
```

请求接口验证，返回内容不变，说明自定义名称注入成功。

### 自定义值注入（useValue）

除了注入类，还能直接注入一个值，比如一个固定的数组：

```ts
providers: [
  {
    provide: 'car',
    useValue: ['奔驰', '宝马', '奥迪'],
  },
]
```

控制器中同样用 `@Inject('car')` 接收：

```ts
constructor(@Inject('car') private readonly car: string[]) {}

@Get()
findAll() {
  return this.car; // ['奔驰', '宝马', '奥迪']
}
```

请求后直接拿到这三个值，这就是 `useValue` 自定义注入值的能力。

### 工厂模式注入（useFactory + 跨模块复用）

场景：在用户模块里，`findAll` 想复用课程模块 `CourseService` 的某个方法。这就需要**工厂模式**，通过 `useFactory` 拿到其他模块的依赖并做逻辑处理。

```ts
providers: [
  CourseService,
  {
    provide: 'course',
    useFactory: (courseService: CourseService) => {
      // 在这里使用 courseService 的方法
      return '工厂执行了';
    },
    inject: [CourseService],
  },
]
```

注意两点：

1. `inject` 是**数组**，把需要依赖的 `CourseService` 放进去；
2. 要让别的模块能用 `CourseService`，**课程模块必须把它 `exports` 出来**（不是 import，是 export），否则用户模块无法访问。

控制器中用 `@Inject('course')` 接收工厂产物即可。这样就实现了「在一个模块里使用另一个模块的能力」。

## 小结

- `providers` 是 NestJS 的依赖容器，模块里声明、控制器里按需注入。
- 被注入的类需加 `@Injectable()`；基础写法 `providers: [Service]`。
- 自定义名称：`{ provide: 'Token', useClass: Service }`，配合 `@Inject('Token')`。
- 自定义值：`{ provide: 'Token', useValue: 任意值 }`，适合注入常量/配置。
- 跨模块复用依赖用 `useFactory` + `inject`，且提供方模块需 `exports` 该 Service。

## 下一步

掌握 Providers 后，下一步建议接着看《如何理解Nestjs的模块Module》，深入理解 Module 如何组织 Provider、Controller 以及模块间的 import / exports 边界。
