# 后端接口开发—课程的查询接口开发

> **导语**：本文用 RESTful 风格实现课程查询接口 `GET /course`，重点演示如何在接口中校验 JWT、从请求头取出 Token 并解密，以及如何用逻辑删除字段 `deleted` 过滤已删除数据，返回合法课程列表。

## 前置知识

阅读前建议先看《后端接口开发—用户的注册接口开发》，本文复用其中的 JWT 配置与「用户已登录才能操作课程」的权限模型。对 JWT 与 TypeORM 基础可回顾《Nestjs框架课程介绍+适合人员+学后水平》。

## 正文

### 接口定义与权限要求

课程相关的查询、修改、删除都需要用户登录后才有权限操作，因此接口需要前端在请求头携带 Token，后端先解密校验合法性。

接口地址：

```
GET http://localhost:3000/course
```

同一个 `/course` 路径后面会通过不同 HTTP 方法实现多个接口（查询、新增、修改、删除），这是 RESTful 风格的典型用法。

### 在 Course Module 中注入依赖

`course.module.ts` 中需要：

- 引入 `JwtModule.register(jwtConfig)`，用于解密 Token；
- 引入 `TypeOrmModule.forFeature([Course])`，把 `Course` 实体纳入本模块仓储。

```ts
@Module({
  imports: [
    JwtModule.register(jwtConfig),
    TypeOrmModule.forFeature([Course]),
  ],
  controllers: [CourseController],
  providers: [CourseService],
})
export class CourseModule {}
```

### 控制器：取 Token 并校验

课程查询是 GET 请求。控制器先从请求头取出 `authorization`，调用 JWT 工具解密；Token 不合法则抛异常提示「请先登录」，合法则放行并调用服务层 `findAll`。

```ts
@Controller('course')
export class CourseController {
  constructor(private readonly courseService: CourseService) {}

  @Get()
  findAll(@Headers('authorization') authorization: string) {
    // 校验 Token，不合法会在工具内部抛异常
    this.jwtService.verify(authorization);
    return this.courseService.findAll();
  }
}
```

> 若编译器提示 `Headers` 重复引入或暂时未用到 `@Post`，可先移除未使用装饰器，避免冗余告警。

### 服务层：按逻辑删除过滤查询

`CourseService` 通过 `@InjectRepository(Course)` 拿到仓储，查询时只返回 `deleted = 0`（未删除）的课程：

```ts
@Injectable()
export class CourseService {
  constructor(
    @InjectRepository(Course)
    private readonly courseRepository: Repository<Course>,
  ) {}

  findAll() {
    return this.courseRepository.find({ where: { deleted: 0 } });
  }
}
```

这里的 `deleted` 是**逻辑删除**标记：值为 `0` 表示未删除、`1` 表示已删除。判断标准可自行约定，只要前后端一致即可。这样已删除的课程不会返回给前端。

### 接口联调验证

1. 先调用登录接口拿到 Token；
2. 在课程查询接口的请求头带上该 Token，发送 `GET /course`，即可返回当前已有的课程列表；
3. 若传入不合法的 Token，接口会响应「请先登录」，无权限时不会返回任何数据。

## 小结

- 课程类接口需登录态，前端在 `authorization` 请求头携带 Token，后端用 `jwtService.verify` 校验。
- 同一资源路径（如 `/course`）可通过不同 HTTP 方法承载多个接口，符合 RESTful 风格。
- 模块注入：课程模块需 `JwtModule` 与 `TypeOrmModule.forFeature([Course])`。
- 查询用 `@InjectRepository(Course)` 拿仓储，`find({ where: { deleted: 0 } })` 过滤已删除数据。
- 逻辑删除用 `deleted` 字段区分（0 未删 / 1 已删），避免物理删除带来的数据风险。

## 下一步

课程查询打通后，下一步建议接着看《后端接口开发—课程的创建接口开发》，继续完善课程资源的增、改、删接口，把完整的课程 CRUD 闭环补齐。
