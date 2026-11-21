# 审稿报告 B1：00 预先课（40 篇）

- 审核对象：`work/target/25-lowcode/posts/00.预先课 - 低代码大课必备技术/`（40 篇）
- 审核基准：scan3-code（技术栈/事实）、scan6-applied（已修点，未重复报）、scan9-index（红线：禁写 RBAC、参考实现注明）
- 结论速览：**3 篇需修（各含 1 处 P1），其余 37 篇合格**（部分合格篇附 P2 润色建议，可修可不修）。
- 全批共性检查：40 篇六段结构（导语/前置知识/正文/小结/下一步）全部完整；「下一步」互链篇目逐一对照过实际文件名（含 02 期 `TypeORM_框架-*`、01 期 `1-1.低代码平台项目大课介绍`、05 期 `17-1 OSS 资源上传配置` 等），**全部指向真实存在的篇目，无编造篇名**；未发现 RBAC 表述、未发现把工程 A 的工作流/沙箱/AI 能力安到项目上、参考实现处均按红线注明。去 AI 味整体到位：无机械整句加粗、小结有具体信息量、口播腔已清理。

---

## 需修篇目

### 第_3_集__NestjsRESful风格API开发.md —— 需修

1. **P1（API 名称硬伤，代码无法编译）** L92-94 版本控制代码块：
   - 原文：`import { VersionType } from '@nestjs/common';` + `app.enableVersioning({ type: VersionType.URI });`
   - 改法：NestJS 的正确导入与枚举名是 `VersioningType`，不是 `VersionType`。改为 `import { VersioningType } from '@nestjs/common';` / `app.enableVersioning({ type: VersioningType.URI });`；L145 小结同步改 `VersionType.URI` → `VersioningType.URI`。
   - 理由：`@nestjs/common` 导出的是 `VersioningType`（URI / HEADER / MEDIA_TYPE / CUSTOM），写 `VersionType` 编译直接报错，读者照抄必失败。其余内容（`@Controller({ path, version })`、方法级 `@Version('1')`、加版本后必须请求 `/v1/user`）均正确。

### 第_1_集__Nestjs环境搭建和项目创建.md —— 需修

1. **P1（事实错误）** L34：「Node.js 18 已经内置了 pnpm，可先检查是否已携带」。
   - 改法：改为「Node 16.13+ 自带的是 **corepack**（包管理器管理工具），可以通过它启用 pnpm（`corepack enable`）；也可以直接 `npm install -g pnpm` 全局安装。多数情况下直接全局安装最省事」。
   - 理由：Node.js 从不捆绑 pnpm 本体，只捆绑 corepack；`node -v` 装完 18 后直接 `pnpm -v` 通常报找不到命令，与文中「可先检查是否已携带」的暗示矛盾，照做会卡住新手。

### 第_1_集__后端接口开发—课程的查询接口开发.md —— 需修

1. **P1（代码自相矛盾，无法编译）** L57-64 控制器代码块：
   - 原文：`constructor(private readonly courseService: CourseService) {}` 但方法体用了 `this.jwtService.verify(authorization)`。
   - 改法：构造函数补上注入：`constructor(private readonly courseService: CourseService, private readonly jwtService: JwtService) {}`，并在代码块顶部补 `import { JwtService } from '@nestjs/jwt';`（与 L84 模块代码里 `JwtModule.register(jwtConfig)` 呼应）。
   - 理由：`jwtService` 从未声明，TypeScript 编译报「Property 'jwtService' does not exist」。同批《用户的查询接口开发》篇的写法（JwtTool 工具类）是自洽的，本篇最小改法是补注入。

---

## 合格篇目（附个别 P2 润色建议）

以下 37 篇判定【合格】。技术点抽核均正确：装饰器四分类参数签名、`@Param()` 无 s、`NestInterceptor/NestMiddleware/NestModule` 与 implements 用法、`@Catch + ExceptionFilter + useGlobalFilters`、`exception.getResponse().message` 取 DTO 校验提示、`ParseIntPipe` 400 行为、`ValidationPipe` 全局开启、`TypeOrmModule.forRoot/forFeature`、`@InjectRepository`、`update` 双参数、TypeORM 无 `findAll` 的纠正、`useFactory + inject + exports` 跨模块、`@Global`/`forRoot/DynamicModule`、`FileInterceptor + MulterModule.register + useStaticAssets`、`createHashRouter` 与 `.ts/.tsx` 区分、ahooks `useRequest manual:true`、`Omit/Partial` 用法——全部与 NestJS 10 / TypeORM 0.3.x 真实行为一致。逐篇附注：

- 第_1_集__Nestjs框架课程介绍+适合人员+学后水平.md：合格。pnpm-workspace、模块/控制器/服务分层、React+AntD+Tailwind 说法与 scan3 对 B 工程的核实一致；未夸大（未提工作流/沙箱/RBAC）。
- 第_2_集__Nestjs初始化目录结构介绍.md：合格。`nest g resource` 生成物清单、调用链、`pnpm-lock.yaml` 说明均正确。
- 第_3_集__Nestjs的基本介绍.md：合格。**P2（建议）**：L41「Star 数量…（当时约 62.1k，NestJS 约 60.4k）」，2023 年时点 NestJS 实际约 50k+，与 Express 差距没这么小，且此数据无法从课程资料核实；建议改为「Star 数快速逼近老牌 Express」这类不带具体数字的表述，或标注「约数」。其余（2017 年发布、Express/Fastify 底层、IoC/DI 讲法）正确。
- 第_1_集__什么是装饰器和Nestjs中的应用.md：合格。四类装饰器参数与 NestJS 对照正确，`experimentalDecorators` 说明正确。
- 第_1_集__如何理解Nestjs的提供者Providers.md：合格。useClass/useValue/useFactory+inject 与 exports 要求均正确。
- 第_2_集__如何理解Nestjs的模块Module.md：合格。共享模块 vs 工厂模式辨析、`forRoot` 返回必须含 `module` 均正确；示例代码用占位符 `<站点基础地址>` 明示非源码，处理得当。
- 第_2_集__详解Nestjs控制器《上》.md：合格。`@Query/@Body/@Param/@Headers/@HttpCode` 与 GET/POST 取参位置正确；「@Param 没有 s」的提醒准确。
- 第_3_集__Nestjs提供Get和Post请求.md：合格。`setGlobalPrefix`、类前缀+方法路径正确。（`@Get('hello')` 是视频演示上下文，已用括注来源，不算硬伤。）
- 第_3_集__NestCli常用命令提高开发效率.md：合格。**P2（建议）**：L48「以及 `*.spec.ts` 端到端测试文件」——resource 生成的是单元测试 spec 文件，端到端测试在脚手架 `test/` 目录（jest-e2e）；建议改为「以及 `*.spec.ts` 测试文件」。别名 `g/mo/co/s` 与抢路由坑描述正确。
- 第_1_集__掌握Rxjs和在Nest中的应用.md：合格。Observable/interval/take/of/pipe/map/filter/unsubscribe 示例输出描述均正确（take(6)→0..5、filter 偶数、无 take 不停流）。
- 第_3_集__掌握Nestjs中间件的使用.md：合格。`NestMiddleware`、`forRoutes` 三种粒度、`enableCors`、send/render 坑均正确。
- 第_2_集__Nest的响应拦截器.md：合格。`NestInterceptor + useGlobalInterceptors` 与代码正确。
- 第_3_集__Nest的异常拦截器.md：合格。「异常过滤器」正名处理到位，代码与注册 API 正确。
- 第_4_集__Nest的管道Pipe转换.md：合格。内置转换 Pipe 清单完整准确，`ParseBoolPipe` 对数字 123 返回 400 的描述正确。
- 第_5_集__Nest的管道验证DTO.md：合格。**P2（建议）**：L53 DTO 字段名 `form` 配「按 11 位手机号来约束」，`form` 疑似口播「phone」的转写残留；若工程源码确实叫 `form` 可保留，否则建议改 `phone`。另 L103 自定义提示「form 长度必须大于 11」与 `@Length(11, 13)`（min=11）语义略不符，建议改「长度必须在 11~13 位」。`@Length` 第三参数放 message、装饰器间不用逗号均正确。
- 第_1_集__安装Mysql数据库和可视化工具安装使用.md：合格。docker run 参数、Navicat 流程正确。
- 第_2_集__Nest通过TypeORM链接Mysql数据库.md：合格。「容器名≠数据库名」「漏装 mysql2」两个坑描述真实；`synchronize` 生产警告到位。
- 第_3_集__TypeORM配置实体和操作数据库.md：合格。**P2（建议）**：L121 小节标题「查：find 与 find()」重复，应为「查：find(条件) 与 find()」。`find` 返回数组、无 `findAll` 的纠错正确。
- 第_4_集__你知道Nest如何进行上传文件吗.md：合格。`dest` vs `diskStorage`、`__dirname` 指向 dist、`prefix` 要带 `/` 均正确；OSS 升级说法与 scan3（B 工程 ali-oss）一致。
- 第_1_集__项目需求分析—前端页面需求分析.md：合格。需求拆解与路由规划自洽。
- 第_1_集__项目需求分析—接口和数据库数据结构分析.md：合格（软删除、七接口拆分正确）。**P2（跨篇一致性，建议）**：本篇 user 表字段写作 `image`，而《用户的注册接口开发》篇落库字段是 `head_img`（与参考实现 user.entity 的 `head_img` 一致）、《项目初始化—安装配置TypeORM和Mysql》实体示例又是 `headImage`。三处字段名不一致，建议统一（推荐 `head_img`，与参考实现和注册篇一致）。
- 第_1_集__后端接口开发—用户的注册接口开发.md：合格。MD5 密码入库符合课程原实现，未夸大为「安全加密」；token 只放 id 正确。**P2（跨篇一致性，建议）**：加密工具本篇叫 `InternalTools`（utils/internal-tools.ts），登录/查询篇叫 `SecretTool`；各篇已带「以源码为准」括注，但建议统一为 `SecretTool` 减少读者困惑。
- 第_2_集__后端接口开发—用户的登录接口开发.md：合格。「账号不存在与密码错误统一提示」的防枚举讲法正确。
- 第_3_集__后端接口开发—用户的查询接口开发.md：合格。`verify` try/catch、exp 判断、返回脱敏（不带 password）正确。
- 第_2_集__后端接口开发—课程的创建接口开发.md：合格。软删除字段、鉴权前置正确（本篇已按 scan6-A1 用「接口权限守卫」表述，无 RBAC）。
- 第_3_集__后端接口开发—课程的修改接口开发.md：合格。`getResponse().message` 是本批最有价值的技术点之一，讲得准确。
- 第_4_集__后端接口开发—课程的删除接口开发.md：合格（`del` 软删、DTO 拦 "1" 正确）。**P2（跨篇一致性，建议）**：本篇与需求分析篇用 `del`，而《课程的查询接口开发》《用户的注册接口开发》下一步段落用 `deleted`；同一软删字段两个名字，建议统一（查询篇代码块用 `deleted`，删除篇用 `del`，至少在小结/括注里点明「字段名以工程实体为准」）。
- 第_2_集__项目初始化—创建React项目和初始配置.md：合格。`.ts`/`.tsx` 坑、Tailwind 三指令与重启要求、最简路由守卫正确。
- 第_2_集__项目初始化—创建项目和接口.md：合格。单项目→多包衔接讲法清楚，`enableCors` 位置正确。
- 第_3_集__项目初始化—安装配置TypeORM和Mysql.md：合格。**P2（跨篇一致性，建议）**：实体示例字段 `headImage`，见上文统一建议。
- 第_4_集__项目初始化—接口响应和异常拦截器.md：合格。两个注册 API 的区分与 `new` 实例化强调正确。**P2（建议）**：L49「这一步有点像 Express 里把数据转成 stream 流来处理」类比牵强（RxJS map 与 Node stream 是两回事），建议删掉这半句或改为「类似中间件链上对响应做加工」。
- 第_5_集__项目初始化—接口参数DTO验证.md：合格。`@IsNumber({ allowNaN, allowInfinity })` 选项真实存在；「按操作建类」原则正确。
- 第_3_集__页面和数据联调—登录模块开发.md：合格。AntD Form/ahooks/axios 双拦截器链路自洽。
- 第_4_集__页面和数据联调—注册模块开发.md：合格。复用逻辑、lockfile 片段标注来源正确。
- 第_5_集__页面和数据联调—课程获取和删除模块开发.md：合格。Popconfirm + DELETE + reloadData、软删 del=1 描述正确；`Omit` 讲解正确。
- 第_6_集__页面和数据联调—课程创建和编辑模块开发.md：合格。单弹窗双态、`Partial<CourseWithoutId>` 正确；伪代码块已明确标注「伪代码示意」。互链《低代码平台项目大课介绍+适合人员+学后水平》对应 01 期 `1-1`，真实存在。
- 第_2_集__课程章集目录速览.md：合格。**P2（建议）**：小节从「第 1 章」直接跳「第 3 章」，缺第 2 章交代；若原目录即如此（第 2 章可能并入），建议加一句括注说明，避免读者以为是漏写。互链目标均存在。

---

## 红线复核（scan9）

- 全批 40 篇 grep 核对：无「RBAC」「角色权限」表述；鉴权统一写作「登录态 / 接口权限守卫 / JWT 校验」，与两工程实况（B 有 JWT 守卫、无角色模型）相符。
- 「配套工程/配套资料」引用均指向课程资料路径（`代码（已8期）/…`），工作流/沙箱/AI 等仅属于工程 A 的能力在本批未被提及或声称，无越界。

## 本批统计

| 指标 | 数量 |
|---|---|
| 总篇数 | 40 |
| 合格 | 37 |
| 需修 | 3（各 1 处 P1：`VersionType`→`VersioningType`；「Node 18 内置 pnpm」；课程查询控制器漏注入 `jwtService`） |
| P0 硬伤 | 0 |
| P1 错误 | 3 |
| P2 润色/一致性建议 | 9 处（集中在：Star 数据、spec 测试表述、`form`/`phone` 字段疑点、`find` 标题笔误、stream 类比、章节号跳跃，以及 `del`/`deleted`、`image`/`head_img`/`headImage`、`InternalTools`/`SecretTool` 三组跨篇命名不一致） |
| 六段结构完整率 | 40/40 |
| 互链有效率 | 100%（抽核全部「下一步/前置知识」引用篇目，均真实存在） |
| 红线违规 | 0 |
