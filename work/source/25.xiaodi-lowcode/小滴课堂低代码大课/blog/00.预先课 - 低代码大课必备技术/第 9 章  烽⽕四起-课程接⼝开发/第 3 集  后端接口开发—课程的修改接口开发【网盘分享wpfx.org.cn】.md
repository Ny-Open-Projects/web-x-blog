# 后端接口开发—课程的修改接口开发

> **导语**：课程组 CRUD 的第三块，本节实现「修改课程」接口，并顺手把上一节遗留的 DTO 校验打通。除了 `@Put()`、`UpdateCourseDto`、`repository.update()` 这套常规写法，真正值得记的是一个容易漏的细节：异常过滤器必须从 `exception.getResponse().message` 取值，才能把 DTO 的字段级校验提示返回给前端。读完你会同时拿到接口实现和「校验提示为什么看不到」的答案。

## 前置知识

本节直接建立在前两节之上，建议先看《后端接口开发—课程的创建接口开发》，复用它的 Controller、Service、JWT 鉴权与 DTO 结构。校验规则本身在《Nest的管道验证DTO》和《项目初始化—接口参数DTO验证》里讲得更细，异常返回的处理则与《Nest的异常拦截器》一脉相承，对照阅读会更清楚。

## 正文

### 控制器层：`@Put()` 与 `UpdateCourseDto`

在 `CourseController` 里新增一个由 `@Put()` 装饰的 `update()` 方法，用 `@Body()` 接收前端提交的修改数据，参数类型声明为 `UpdateCourseDto`。修改与创建共用同一个资源路径，靠 HTTP 方法区分：POST 是新增，PUT 是更新，这与前面《NestjsRESful风格API开发》里的方法语义保持一致。

方法内部仍然是两步：先做 JWT 校验，再调用 `CourseService.update(dto)`。鉴权放在业务逻辑之前，未登录或 token 失效的请求根本进不到数据库操作。

DTO 这一层有个刻意的加强：把 `UpdateCourseDto` 里的字段都设为必传。修改接口要求前端把这一组字段完整地传回来，缺一个、错一个类型都应该被挡在管道里，而不是等到 Service 里才发现数据不全。

### 服务层：`repository.update()` 的两个参数

`CourseService.update()` 接收 Controller 传来的 DTO，调用 TypeORM 仓储的更新方法，形如 `this.courseRepository.update(id, dto)`。两个参数含义很明确：

- 第一个参数定位「更新哪条数据」，用前端传过来的 `id`；
- 第二个参数是「改完之后这些字段是什么值」，直接把校验通过的 DTO 对象传进去即可，不必再手工拆字段。

和创建接口的 `save` 相比，`update` 不会插入新行，只改已有记录。这也是为什么修改接口一定要有 `id`，而创建接口不需要。更新完成后刷新 `course` 表，能看到目标记录的 `title` 已被改成新值，接口即生效。

### 重点：让异常过滤器吐出 DTO 的校验提示

联调时先验证三件事：带正确 token 的 PUT 请求能改成功；把 token 改坏会提示「请先登录」；把 `title` 传成数字，按理应该被 DTO 挡下。但第三件事一开始往往不生效——返回的只是一条笼统的报错，看不到「title 必须为字符串」这样的字段级信息。

原因在异常过滤器里。原来的写法直接取 `exception.message`，拿到的是异常对象上那句通用消息，而 DTO 校验失败的详细提示其实藏在 `getResponse()` 的返回值里。改成通过 `exception.getResponse().message` 取值，并给 `exception` 加一个宽松的类型约束（例如设为 `any`）消掉类型告警，就能把字段级提示原样覆盖回响应中。前端拿到后才知道具体是哪个参数、哪种类型没通过校验。

改完之后再测：把 `title` 传成数字，返回「title 必须为字符串」；把 `price` 改成字符串（本版要求字符串）同样会被拦下；逐个数一遍六个参数都能正确校验。顺带回到上一节的创建接口，把 `title` 改成数字再发一次 POST，也能得到同样的提示——说明这套 DTO 校验对整组接口一致生效。想深入的话可以把整个 `exception` 打印出来看看它的结构，里面就含着 DTO 校验的结果，只是需要主动调用方法去取。

这个改动看着小，体验差别很大：接口错误信息从「一句话」变成「能定位到字段」，前端表单才能做精确的错误提示。低代码平台里组件属性、页面配置都由 Schema 驱动，字段极多，这类可读的校验信息更是刚需。

### 关联工程配置

本阶段的工程仍是 pnpm workspace 多包结构，前端 `client` 子包开启了严格的类型检查，正好呼应 DTO 的强约束思路。见 `代码（已8期）/代码（已8期）/9-2/lowcode/packages/client/tsconfig.json`：

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

后端服务的启动与构建脚本在 `代码（已8期）/代码（已8期）/9-2/lowcode/package.json`，用 `pnpm --filter server run start:dev` 起本地服务；`packages/server/` 下另有 `nest-cli.json`、`tsconfig.json` 等配置，需要核对编译选项时按相对路径查看即可。

### 联调清单

- PUT + 完整 body + 正确 token → 数据库 `title` 更新成功。
- 篡改或删除 headers 里的 token → 提示「请先登录」，不进入 Service。
- `title` 传数字 → 返回字段必须为字符串的校验提示。
- 回归创建接口 → 同样的类型错误也能被正确拦截。

## 小结

- 修改接口用 `@Put()` + `@Body()` 接参，入参交给 `UpdateCourseDto`，字段设为必传。
- Service 用 `repository.update(id, dto)`：第一个参数定位记录，第二个参数是修改后的字段对象。
- JWT 鉴权仍放在业务逻辑之前，token 失效直接提示「请先登录」。
- 异常过滤器要从 `exception.getResponse().message` 取值，才能把 DTO 字段级提示返回给前端；类型约束可放宽为 `any`。
- 修改与创建共用同一套 DTO 校验，改完过滤器后要回归创建接口一起验证。

## 下一步

课程 CRUD 只剩最后一个，建议接着看《后端接口开发—课程的删除接口开发》，把整组接口补齐。接口全部就绪后就可以切到前端，按《页面和数据联调—课程创建和编辑模块开发》把创建/编辑表单与这两个写接口联起来；若还想巩固校验与异常返回，可回看《Nest的异常拦截器》。
