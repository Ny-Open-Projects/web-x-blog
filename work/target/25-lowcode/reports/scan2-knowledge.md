# 扫描2：小滴课堂低代码大课 正文知识点总账

> 源：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/blog`（00 预备课 + 01~08 期，共 229 篇）。
> 组织：按「期 → 章」列条目级知识点，标注出处文章文件名（去掉网盘水印后缀）。

## 00. 预备课：NestJS 必备技术（目录：00.预先课 - 低代码大课必备技术）

**期摘要**：预先课用一个小型「用户+课程 CRUD」项目把 NestJS 全家桶走一遍：装饰器/控制器/Providers/Module/中间件/拦截器/管道/DTO，再到 TypeORM 连 MySQL 做实体同步与增删改查，最后 React 前端联调完成全栈闭环。它同时铺垫了 Docker 装 MySQL、pnpm workspace 多包工程等正式课基础设施。

### 第 1~2 章：认识 NestJS 与初始化
- NestJS 定位：构建高效、可扩展 Node 服务端应用的渐进式框架；原生 TS，融合 OOP/FP/FRP（内置 RxJS）；底层兼容 Express/Fastify 可复用其中间件。设计思想 = IoC（思想）+ DI（实现），框架负责实例化注入，类间解耦；与 Java Spring 思想高度相似，Java 工程师上手快。〔第 1 章  Nestjs 框架课程介绍/第 3 章 初来乍到〕
- 招聘市场：Node 岗 8K~13K 起步，中高级前端岗也要求会用 Node 做 CRUD（NestJS/Express）。〔第 1 章〕
- 环境：Node 16+（演示 18 LTS）、pnpm 提速、`@nestjs/cli` 全局安装、`nest new` 创建；`start:dev` 热重载；端口在 `main.ts` 的 `app.listen(3000)`。〔第 2 章 烽火四起-用户接口开发前置：Nestjs 环境搭建和项目创建〕
- 目录结构：`dist/`（编译产物）、`src/`（源码）、`test/`（Nest 比 Express 多出的 e2e 测试目录）、`nest-cli.json`、`tsconfig(.build).json`、`pnpm-lock.yaml` 锁版本保协作一致。请求链路：`main.ts bootstrap()` → AppModule → @Controller → Service；控制器只接请求，业务下沉 Service。`nest g resource <name>` 一键生成 module/controller/service/dto/entity/spec 全套 RESTful 骨架。〔第 2 章 Nestjs 初始化目录结构介绍〕
- 路由：`@Controller('app')` 类前缀 + `@Get('get')` 方法路径组成 `/app/get`；`setGlobalPrefix('api')` 全局前缀；POST 需 Apifox 调试（方法/路径/前缀三要素核对）。〔第 3 章 Nestjs 提供 Get 和 Post 请求〕

### 第 3~4 章：装饰器、控制器、CLI、RESTful、Providers、Module、中间件、文件上传
- 装饰器本质是函数，`@` 叠加；TS 四类：类/属性/方法/参数装饰器，接收参数各不同（类本身、原型+属性名、方法描述符、参数下标）；需 `tsconfig` 开 `experimentalDecorators`。Nest 中 `@Controller` 类装饰器、`class-validator` 的 `@IsString` 属性装饰器、`@Post/@Get` 方法装饰器、`@Body` 参数装饰器；装饰器把路由/校验/取参等横切逻辑与业务解耦。〔第 3 章 什么是装饰器和 Nestjs 中的应用〕
- 参数装饰器分工：`@Request/@Req` 整个请求对象；GET 取 query 用 `@Query()`；POST 取 body 用 `@Body()`；动态路由 `@Get(':id')` 取值 `@Param()`；`@Headers()` 取请求头（含自定义 token）；`@HttpCode()` 设状态码。〔第 4 章 详解 Nestjs 控制器（上）〕
- CLI 命令与别名：`g`/`mo`/`co`/`s`；按业务域拆模块，CLI 自动注册进根模块；坑：旧控制器的 `:id` 动态路由会抢占 `/user` 等固定路径。〔第 4 章 NestCli 常用命令〕
- RESTful 是风格不是标准：同一路径换 HTTP 方法（GET 查/POST 增/PUT+PATCH 改/DELETE 删），动态路由拼 ID 与查询参数不要混用；版本控制 `app.enableVersioning({type: VersionType.URI})`，`@Controller({version:'1'})` 或 `@Version('1')`，请求变 `/v1/user`。实战常只用 GET+POST。〔第 4 章 RESTful 风格 API 开发〕
- Providers 是依赖容器：`providers:[Service]` 基础注入（类需 `@Injectable()`）；`{provide:'Token', useClass}` + `@Inject('Token')` 改名注入；`useValue` 注入常量/配置；`useFactory`+`inject` 工厂注入做跨模块复用，提供方需 `exports`。〔第 4 章 Providers〕
- Module 是更高层容器：主模块聚合子模块；共享模块=提供方 exports、使用方注入；`@Global()` 全局模块一次注册处处可注入；动态模块 `static forRoot(options)` 返回 DynamicModule 接收参数。〔第 4 章 Module〕
- 中间件：请求前后处理 req/res（鉴权/日志/转换）；类中间件 `implements NestMiddleware` + `use(req,res,next)`，`next()` 必调否则卡住；模块内 `configure` + `MiddlewareConsumer.apply().forRoutes()`，支持路径串、`{path,method}`、Controller 三种粒度；全站函数式中间件 `app.use(...)` 可做白名单/token 校验；跨域 `cors` 中间件或 `app.enableCors()`。〔第 4 章 掌握 Nestjs 中间件〕
- 文件上传：装 `multer`+`@types/multer`；`MulterModule.register({dest})` 最简但乱码名不可预览；推荐 `diskStorage({destination, filename})` 自定义目录 + `Date.now()` 时间戳名 + `path.extname` 保留后缀；接口 `@UseInterceptors(FileInterceptor('file'))` + `@UploadedFile()`；坑：编译后 `__dirname` 指向 dist 要回退工程根拼路径；`NestExpressApplication` + `useStaticAssets` 开静态访问，prefix 须以 `/` 开头。〔第 4 章 文件上传〕

### 第 5 章：RxJS、响应拦截器、异常过滤器、管道
- RxJS：Nest 自带，服务端用于异步；Observable 发布（next/complete）+ subscribe 订阅；`interval/take/of` 组合；`pipe` 串 `map/filter`；`unsubscribe()` 主动终止。〔第 5 章 RxJS〕
- 响应拦截器：统一成功返回为 `code/message/data`；实现 `NestInterceptor.intercept(context,next)`，`next.handle()` 返回 Observable，`pipe(map(...))` 包装；类加 `@Injectable()`，`main.ts` `useGlobalInterceptors(new Xxx())` 全局注册；格式化/加密/日志等横切逻辑也放这。〔第 5 章 响应拦截器〕
- 异常过滤器：正式名称 Exception Filter（非"异常拦截器"）；实现 `ExceptionFilter` + `@Catch()`，`host.switchToHttp().getResponse()` 拿响应；`exception.getStatus()`/`exception.message` 缺省兜底 `Service error`；注册用 `useGlobalFilters`（别混用拦截器 API）。〔第 5 章 异常拦截〕
- Pipe 两大职责=转换+验证：转换型 `ParseIntPipe/ParseFloatPipe/ParseBoolPipe/ParseArrayPipe/ParseUUIDPipe/ParseEnumPipe/DefaultValuePipe`，作为参数装饰器第二参传入，转不动直接 400；转换型只适合少量路径参数。〔第 5 章 管道转换〕
- DTO 验证：DTO 是接口入参约束（类前端表单验证）；`class-validator` 的 `@IsString/@IsNotEmpty/@Length(min,max,{message})/@IsNumber({allowNaN:false,allowInfinity:false})`；必须在 `main.ts` `useGlobalPipes(new ValidationPipe())` 且 `@Body()` 标注 DTO 类型才生效；装饰器间换行分隔不能用逗号；字段级提示靠异常过滤器取 `exception.getResponse().message`。〔第 5 章 管道验证 DTO〕

### 第 6 章：TypeORM + MySQL
- Docker 装 MySQL：`docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=xxx --name xx --restart always -d mysql:8.0`；`docker images/ps/ps -a` 排查三件套；Navicat 建库表。〔第 6 章 安装 Mysql〕
- 连接：依赖三件套 `typeorm` + `mysql2`（驱动最常漏装）+ `@nestjs/typeorm`；配置抽 `config.ts`（`TypeOrmModuleOptions`），根模块 `TypeOrmModule.forRoot()`；`entities` 扫 `.entity.ts`、`autoLoadEntities:true` 自动加载 forFeature 注册的实体、`synchronize:true` 实体同步表结构（开发开、生产慎开）；坑：`database` 填数据库名不是 Docker 容器名。〔第 6 章 连接 Mysql〕
- 实体与 CRUD：`@Entity()+@Column()+@PrimaryGeneratedColumn()` 映射表；`TypeOrmModule.forFeature([X])` 注册实体 + `@InjectRepository(X)` 注入 `Repository<X>`；`save/delete/update(条件,新值)/find({where})`；TypeORM 无 `findAll`，`find()` 查全部返回数组。〔第 6 章 配置实体和操作数据〕

### 第 7~9 章：项目实战（需求分析 → 初始化 → 用户/课程接口）
- 需求拆解方法：页面功能 → 接口清单 → 表字段正向推导，先看成品反推；软删除字段 `del`（0/1），查询必须过滤 `del=0`；建表两条路：entity 自动同步 或 Navicat 转储 SQL 导入。〔第 7 章 接口和数据库数据结构分析〕
- 正式初始化：干净骨架 + `nest g resource` 生成 user/course；`@Controller('user')` 前缀需手动补；跨域 `enableCors()` 写在 listen 前；端口占用排错。〔第 7 章 创建项目和接口〕
- 用户接口：注册 `POST /user/register`——密码 MD5（`crypto.createHash('md5')`）加密入库，注册成功直接签发 JWT（`@nestjs/jwt`，payload 只放 id 不放密码）免二次登录；模块注入三板斧 providers 工具类 + imports `JwtModule.register` + `TypeOrmModule.forFeature`；查重失败抛 `BadRequestException`。〔第 8 章 注册接口〕
- 登录接口：三步校验——查账号存在 → 前端密码过同一加密工具再比对 → 签发 token；账号不存在与密码错误统一提示「账号或密码错误」防账号枚举（安全细节，面试点）。〔第 8 章 登录接口〕
- 查询用户信息：请求头带 token → 解密（`verify` 需 try/catch 兜非法 token → `BadRequestException('Token 有误')`），解密结果含 `iat/exp` 判过期；解密与查库解耦成两个可注入工具类；返回字段脱敏绝不带密码。〔第 8 章 用户查询接口〕
- 课程接口：RESTful 同路径 `/course` 多方法；查询 `find({where:{deleted:0}})` 逻辑删除过滤；创建时后端自补软删字段默认 0，DTO 展开直接 `save`；修改 `repository.update(id, dto)` 两参数；删除=软删 update del 0→1；写操作必须 JWT 鉴权「请先登录」。〔第 9 章 课程查询/创建/修改/删除接口〕

### 第 10 章：React 前端与联调
- 前端初始化：Vite 建 React+TS 项目；`react-router-dom` 用 `createHashRouter`+`RouterProvider`，子路由出口 `Outlet`；含 JSX 文件须 `.tsx`；Tailwind 需 `tailwind.config.js`+`postcss.config.js`+样式指令三者齐备，改配置要重启。〔第 10 章 项目初始化〕
- 最简路由守卫：`useEffect`+`useLocation`+`useNavigate`+`Outlet`，localStorage 存 token；无 token 只许 login/register，有 token 访问登录页重定向到管理页。〔第 10 章 项目初始化〕
- 请求层：axios 二次封装 `makeRequest` 收口 url/method/data/泛型；请求拦截器注入 token，响应拦截器统一 `message` 提示与抛错；ahooks `useRequest` `manual:true`+`run` 手动触发，`loading` 直接渲染加载态，`onSuccess` 集中写缓存/提示/跳转。〔第 10 章 登录模块/注册模块〕
- 列表页：AntD `Layout` Header/Content/Footer；`Table` columns+render 渲染缩略图与操作列、`pagination.pageSize`；删除用 `Popconfirm` 二次确认 + DELETE，成功后必须重新拉列表；退出登录清 localStorage token。TS 技巧：`Omit` 剔除 id 类型、`Partial` 用于编辑回填。〔第 10 章 课程获取和删除/创建和编辑模块〕

## 01. 第一期：导学 + 技术选型 + 需求分析（1-1~5-3）

**期摘要**：第一期是「定盘子」：明确平台三端架构（React 编辑端 client / Next.js H5 发布端 release / Nest 后端 server）与两大业务（零代码发布官网、问卷系统），按大厂产研流程做需求分析并产出需求文档（流程图+原型图+术语表），同时铺垫技术选型方法论（项目/团队/技术三维度）与面试话术。Next.js App Router 快速入门也在本期完成。

### 课程定位与项目亮点
- 平台目标：零代码发布网站 + 问卷系统（收集数据→ECharts 可视化→在线 Excel 下载）。〔1-1〕
- 三端技术栈：B 端编辑端 React+TS+ahooks+MobX（比 Redux 配置更简单）+AntD+ECharts+Tailwind；后端 Nest+TypeORM+MySQL+Redis+Docker+Nginx+阿里云 OSS+JMeter；C 端 Next.js SSR+TS+AntD+Tailwind。〔1-1〕
- 难度三档：P3 中级（技术栈+组件库+ECharts）、P2 高级（ahooks+自定义 Hooks、组件数据结构设计、编辑端/发布页复用同一套组件、拖拽排序/预览/一键发布、Redis 自定义 key + 图形验证码 + 原子性防重提交保证 Redis 与 MySQL 一致性、前端性能优化）、P1 技术组长（三端协同、Nginx 代理/负载均衡/压缩、自定义字段、OSS 存大资源、Docker 镜像+容器、云效 CI/CD、JMeter 压测决策服务器配置）。〔1-2〕
- 面试话术：被问「有没有在线地址」——在校生说比赛/毕设，在职说停止维护；关键是亮点与技术方案必须真正掌握。〔1-2〕

### 大厂产研流程与协同工具
- 标准流程 10 步：需求调研→梳理→需求评审（原型图，技术 Leader 评估工时裁剪需求）→UI 设计→团队需求会议（甘特图排期、后端先定接口协议、前端 Mock 并行开发）→研发测试→测试用例评审→协作日常（晨会、不可私自接受变更、Code Review）→上线（避免无人值班时段发版、产品线上二次验收）→复盘。〔2-1〕
- 协同工具链：代码仓库（Codeup/GitLab）、文档（语雀/飞书/腾讯文档）、接口管理（Apifox/Postman）、bug 管理（PingCode/禅道/阿里 AOne）、CI/CD（Jenkins/阿里悍马/云效）。〔2-2〕

### 技术选型方法论（面试重点）
- 选型三维度：项目（周期长短、规模、是否 SEO/动态渲染→Next.js/Nuxt、是否跨端→Uni App/Flutter/RN）；团队（成员技术栈、要有「兜底人」、招聘成本与冷门技术风险）；技术（GitHub star/npm 下载量、可维护性与生态是否还在维护、兼容性）。〔2-3〕
- 面试考察点：技术选择依据（需求/团队/性能/可拓展/安全）、决策过程解释、兼容性及对后续开发部署维护的影响、可持续性；两份简历案例：①图形验证码+短信验证码+Redis 原子性防重提交；②DevOps CI/CD 一键部署。〔2-4〕
- Vue vs React：Vue 206k star（尤雨溪，组合式 API、静态提升优化），React 215k（Facebook，18 起全面函数组件、单向数据流+虚拟 DOM）；React 纯前端推荐 Vite、全栈/SSR 推荐 Next.js；状态管理 Vue→Pinia，React→Redux Toolkit/MobX。注意 Next.js（React SSR 框架）≠NestJS（Node 后端框架）。〔2-5〕
- Express（62.2k，轻量路由强）/NestJS（60.8k，2017 年 Kamil Mysliwiec，全功能企业级：内置 DI、Pipe、Guard，TS 优先，适合中大型）/Koa（34.4k，async/await 中间件，极简需自行组合）。〔2-6〕
- Next.js（114k，Vercel，「生产环境 React 框架」，静态+SSR 融合、路由预取、几乎零配置）vs Nuxt（48k，Vue 生态，坑略多看英文文档）；SSR 服务端直出 HTML 利于 SEO。〔2-7〕
- 组件库选型：AntD React（88.2k，蚂蚁金服 2015，中后台）、AntD Mobile（11.2k）、AntD Vue（社区维护，风险略高）、Element Plus（饿了么，Vue3 PC 首选）、Vant（有赞，移动端 Vue）。〔2-8〕
- 本课拍板：编辑端 React+AntD，后端 NestJS，发布端 Next.js。〔2-9〕

### Next.js 快速入门（App Router）
- `create-next-app` 选项（TS/ESLint/Tailwind/src 目录/App Router）；包管理工具 npm/pnpm/yarn vs 包执行器 npx。〔3-1〕
- 目录：`.next` 构建产物、`public` 静态资源、`src/app` 文件路由、`layout.tsx` 根布局（metadata SEO+字体+全局样式）、`page.tsx` 首页；lock 文件锁版本保协作一致。〔3-2〕
- App Router（13+ 官方推荐）vs Pages Router；嵌套路由；非根布局 `layout.tsx` 不写 html/body、共享组件放 children 前；跳转：`<Link>` 与 `useRouter` 编程式；`usePathname` 取当前路径。〔3-3〕
- Route Groups 路由组（分类不污染 URL）、动态路由 `[slug]`、批量 `[...slug]`、并行路由/路由拦截/Route Handlers。〔3-4〕
- 传参：Link 字符串 `?id=..&name=..` 或对象 `{pathname, query}`；接收：客户端 `useSearchParams().get()`（须 'use client'，需空断言兜底）、服务端组件 `props.searchParams`；`router.push` 只支持字符串，第二参仅 scroll。〔3-5〕
- 服务端取数：`fetch` 全局可用，组件可 `async` 直接 `await`；两层校验 `response.ok` + `result.data`；SSR 下 Network 看不到请求但页面源码含完整内容（SEO）；`pnpm build` 出 `.next` 产物，`npm start` 跑生产。〔3-6〕

### 需求分析（前端功能点 / 后端接口 / 需求文档）
- 注册：手机号+图形验证码+短信验证码两级闸门（图形验证码比对依赖 Redis 防短信盗刷）；登录三种方式：账号密码/手机验证码/微信扫码（未注册用户扫码后直接登录）。〔4-1〕
- 编辑页核心交互：时间戳比对决定用 localStorage 草稿还是接口数据（存草稿不发请求）；组件分展示类（视频/图片/轮播图/文本/富文本/卡片/列表等）与问卷类（输入框/文本域/单选/多选）；右侧属性面板配置；上传统一进 OSS；编辑交互：上下移动、删除（含键盘 Delete）、拖拽排序、键盘撤销重做（Mac Cmd+Z）；预览/草稿（localStorage）/发布（生成二维码，上线后公网域名可访问）。〔4-1〕
- 后台数据统计：表格+导出 Excel/压缩包；动态图表（饼状图、横向柱状图）按组件 ID 查看分布；同一用户同一页面问卷只收集一次（后端去重）。〔4-2〕
- 接口清单四类：用户相关（图形验证码、手机验证码、注册、密码登录、验证码登录、微信扫码校验/二维码/回调/轮询、用户信息）；低代码编辑（发布、组件获取、OSS 上传/查询/删除）；H5 发布页（组件获取、检测是否有问卷组件、提交问卷）；数据统计（问卷表头、问卷数据、按 ID 查某组件数据）。验证码在 Redis 用 register/login 字段分类防冲突。〔4-3、4-4〕
- 业务规则：重新发布页面会重置历史问卷数据；问卷检测接口决定提交按钮显隐。〔4-4〕
- 需求文档写法：前言（低代码价值：降门槛/加速交付/易应对变更）+自研动机（自定义需求/数据安全合规/流量入口营收）+版本信息与变更日志+术语表（低代码平台、SaaS、私有化部署等，统一认知减少沟通成本）。〔5-1〕
- 功能描述：产品流程图（注册登录/编辑发布/组件管理/问卷分发统计）+交互原型图（编辑页=主体编辑区+右侧属性页+顶部工具栏；统计页=左表格右图表）+页面前置条件表（未登录置灰等）；原型工具墨刀/蓝湖/Sketch/Figma。〔5-2〕
- 项目规划：评审→UI→同步开发（先对接口协议）→联调→提测→用例评审→上线；甘特图任务到人；二次迭代重走需求评审；非功能需求（市场定位/品牌/财务法务）了解即可。〔5-3〕

## 02. 第二期：架构设计 + 服务器环境 + monorepo 工程初始化 + TypeORM 专题（6-1~10-8）

**期摘要**：第二期从架构蓝图落地到工程：绘制系统架构图与数据库 ER 图（五张核心表），购买云服务器并用 Docker 容器化装 MySQL/Redis，用 pnpm workspace 搭起 client/release/server/share 四包 monorepo（share 用 unbuild 打包出 ESM/CJS/d.ts），Nest 端配好 TypeORM+统一响应/异常/DTO，React 端接入 AntD+Tailwind；第 10 章是 TypeORM 系统专题（CRUD、一对一/一对多、事务）。

### 系统架构与数据库设计
- 架构四要素：层级、角色、关系、归类；架构图决定结构组织、明确基础设施（数据库/网络/安全/服务器规格）。〔6-1〕
- 低代码平台架构分层：访问层（编辑端+H5 发布页）→ Nginx 网关（反向代理/负载均衡）→ 后端服务（Nest）→ 存储层（MySQL 主业务 + Redis 缓存高频接口 + OSS 存静态文件返回 CDN 地址）；基础设施：ECS 云主机、域名 DNS、CDN；外部服务：云效 DevOps、云短信、微信登录、JMeter 压测（决策带宽/内存/CPU）、Docker。绘图规范：draw.io、虚线框分组、配色≤3、层级自上而下。〔6-2〕
- ER 图：E=实体（矩形，≈表）、R=关系（菱形）、属性（椭圆）、主键（下划线）；关系 1:1 / 1:n / n:1 / n:m（学生-课程 n:m、老师-课程 1:n）；多后端协作靠 ER 图统一认知。〔6-3〕
- 本项目五张核心表：user / page / component / component_data / resource；组件属性统一以 JSON 存 `option` 字段；resource 存 OSS 返回 URL 而非文件本体；关系：user:page 1:1、user:component / user:resource / page:component / page:component_data 均 1:n；工具：Navicat 查看+导入 `xdclass-local.sql`、MySQL Workbench `Database→Reverse Engineer` 反向生成 ER 图。〔6-4〕

### 云服务器与容器化环境
- 选配：阿里/腾讯/华为大厂云，2 核 8G（或活动价 2 核 2G 3M），CentOS 7.8+ 64 位，带宽 1-5M；勿用本地虚拟机；SSH `root@IP` 连接，`ServerAliveInterval` 保持持久连接。〔7-1〕
- Docker 安装：更新 yum 源→依赖→阿里云 Docker CE 仓库→安装→`docker -v`；命令：容器 start/stop/restart/ps/ps -a/rm，镜像 images/rmi（按 image ID）；镜像来自 Docker Hub 注意版本标签。〔7-2〕
- 容器化装 MySQL：`docker run --name -e MYSQL_ROOT_PASSWORD -p 3306:3306 -d mysql:8.0`；须在阿里云安全组放行 3306；Navicat 公网 IP 连接建库导 SQL。〔7-3〕
- 容器化装 Redis：`docker run -p 6379:6379 -d redis redis-server --requirepass 密码`；放行 6379；进容器先 `auth`；QuickRedis 可视化管理 key 与过期时间。〔7-4〕

### pnpm workspace 多包工程
- 子包：client（React 编辑端+统计前端）、release（Next.js H5）、server（Nest）、share（公共组件+类型）。workspace 优势：单代码库、公共依赖提升根 node_modules、版本一致、一次 install 全装、结构清晰。〔8-1〕
- 初始化：根 `pnpm init`；`pnpm-workspace.yaml` 用 `packages:["packages/*"]` 声明；`pnpm add -w -D` 装公共依赖到根；`@types/node` 版本与 Node 大版本一致；根脚本用 `--filter` 调度子包。〔8-2〕
- client：`pnpm create vite`（React 模板）→删重复公共依赖→重命名 `@lowcode/client`→根脚本 `--filter client run dev`。〔8-3〕
- server：`nest new server`→删自带 node_modules 与重复依赖→`@lowcode/server`→删子项目 `.git` 统一托管。〔8-4〕
- share：打包工具 `unbuild`（内置 Rollup），`build.config.ts`：entries/outDir/`declaration:true`（.d.ts）/`emitCJS:true`（CommonJS）/external 排除 react/antd 等；package.json：`type:module`，exports/main/module/types 分别指 ESM(.mjs)/CJS(.cjs)/类型；`files:["dist"]`。〔8-5〕
- 跨包引用：依赖里写 `@lowcode/share: workspace:^`；`--filter 包名` 对指定子包执行命令；公共变量一处维护处处生效。〔8-6〕

### 代码托管与项目基础配置
- 云效 Codeup：SSH 公钥（口令留空）→关联远程→根目录统一 `git init`（删子目录 .git）、`.gitignore` 忽略 node_modules。〔9-1〕
- server 配置：TypeORM 三件套 + config.ts（host 填公网 IP、database 填库名非容器名）+ User 模块实体验证联通。〔9-2〕
- 统一响应/异常/DTO：响应拦截器统一 `{code:0,data}`，异常拦截器统一 `{code:-1,data}`；`useGlobalInterceptors/useGlobalFilters` 注册；DTO+class-validator+全局 ValidationPipe。〔9-3〕
- client 配置：AntD（开箱即用）+ Tailwind（content 扫描、postcss+autoprefixer、base/components/utilities 三段指令）；改配置必须重启。〔9-4〕

### 第 10 章：TypeORM 专题
- ORM 概念与对比：对象关系映射，优势=抽象/少写 SQL/自动关系管理与表同步/可回退原生 SQL；TypeORM（32.5k，Active Record+Data Mapper、装饰器贴近 Nest）vs Prisma（34k，类型安全但缺多库联合查询、支持库少）vs Sequelize（28.6k，Promise、库广事务强但配置繁琐易嵌套）；选 TypeORM 因与 Nest+TS 高度集成。〔10-1〕
- 连接：三件套 typeorm/@nestjs/typeorm/mysql2；config.ts 用 `TypeOrmModuleOptions` 约束；`forRoot` 全局注册；`database` 填库名不填容器名（高频坑）；`synchronize:true` 代码驱动表同步，线上关闭改手动迁移。〔10-2〕
- 实体：`@Entity()/@Column()/@PrimaryGeneratedColumn()`；`forFeature([User])` 注册到模块。〔10-3〕
- 增查：`repository.save(对象)`；`find({where})` 单对象=AND 多条件、数组=OR；条件属性名须与实体字段一致否则查不到。〔10-4〕
- 改删：`update(条件,新字段)` / `delete(条件)` 靠条件控制影响范围；返回 `affected` 影响条数用于确认误改误删；条件要精确（name+form 同查只命中一条）。〔10-5〕
- 一对一：`@OneToOne(()=>Student)` + `@JoinColumn({name:'studentId'})` + 实体自定义属性存关联数据；查询 `find({relations:{studentDetail:true}})` 一次带出；relations 写属性名非列名；自动同步只建结构，关联数据需手动补。〔10-6〕
- 一对多：`@OneToMany`（一侧，指向数组属性）与 `@ManyToOne`（多侧）成对定义，回调指定回指属性；`relations:['classes']`/`['studentList']` 一次带出；坑：外键 classId 不填关联结果为空、relations 属性名拼错直接报错；实体类改名 `Classes` 避命名冲突。〔10-7〕
- 事务：多条写操作原子性（转账红包例子）；新版 `DataSource.createQueryRunner()`（弃用 getConnection，中文官网旧写法要避开）；流程 createQueryRunner→connect→startTransaction→try 内 commit / catch 内 rollback→finally release 防连接泄漏；事务内操作必须走 `queryRunner.manager`，混用普通 repository 脱离事务管辖；版本 Nest 10+TypeORM 0.3.17+mysql2 3.6.3。〔10-8〕

## 03. 第三期：用户体系后端 + 微信扫码登录 + 前端登录注册联调（11-1~13-10）

**期摘要**：第三期完成用户体系全链路：IP/设备自定义装饰器 → MD5 加密工具 + Redis 全局动态模块 → 图形验证码（svg-captcha）→ 第三方短信接入 → 手机验证码六步防刷 → 注册/双方式登录（JWT 7 天）；然后接入微信场景二维码扫码登录（接入验证 SHA1 签名、access_token→ticket→二维码、XML 回调、Redis isScan + 前端轮询）；前端用 MobX 公共状态 + 自定义 hooks + axios 二次封装完成注册/登录联调。

### 验证码与注册登录后端（第 11 章）
- 自定义参数装饰器：`createParamDecorator` 工厂回调拿 `ExecutionContext`，`switchToHttp().getRequest()` 取请求；封装 `GetUserIp`/`GetUserAgent`；`request.ip` 本地是 `::1/::ffff:127.0.0.1` 需正则匹配 IPv4；`headers['user-agent']` 拼写敏感。设计动机：IP+设备拼成唯一标识绑定验证码防串号。〔11-1〕
- 加密与 Redis 模块：隐私信息（密码/IP/设备）一律 MD5（`crypto.createHash('md5').update().digest('hex')`）后再存；Redis 模块 `@Module` + 静态 `forRoot` 返回 DynamicModule + 全局导出；封装 `set(支持 EX 过期)/del/get(值需转字符串)/exists`；验证码 key=「IP+设备」MD5。〔11-2〕
- 图形验证码：`svg-captcha` 生成 SVG（长度/排除字符/干扰线/背景色配置），后端只返回数据前端渲染；`CaptchaDto.type` 区分 register/login 场景实现缓存隔离；Redis 冒号分层 key、60 秒过期；坑：全局模块要走 `imports` 不能放进子模块 `providers`。〔11-3〕
- 短信平台选型：五维度（价格/到达率与时间/内容可配/推广场景/数据统计）；官方（阿里云腾讯云，自申请签名+模板+资质）vs 云市场第三方（代申请，适合学习）；appSecret 定时更新要重置；链路=生成随机码→调 API→存 Redis→前端回传比对。〔11-4〕
- 短信发送封装：`@Injectable()` Provider `sendMsgCode(form, randomCode)`，内部 `fetch` POST（`Content-Type: application/json`，body 含 appId/appSecret/code/form/templateCode）；必须在模块 providers 注册；属性名大小写敏感（appSecret）。〔11-5〕
- 手机验证码接口六步防线：①60 秒限流（dayjs diff）→②图形验证码存在性检查→③忽略大小写比对→④发短信→⑤删图形验证码 + 按「时间戳_验证码」写 Redis 60 秒→⑥按返回 code 处理；失败清理 Redis 并抛异常交统一拦截器；`request:code:phone` 三层 key；RandomTool 提供 randomCode/randomAvatar/randomNickname。〔11-6〕
- 注册接口：POST `/user/register`；链路=手机号查重→Redis 短信验证码比对（按 `_` 拆时间戳_验证码）→两次密码一致→随机昵称/头像→密码 MD5→入库→签发 7 天 JWT 自动登录。〔11-7〕
- 登录接口：账号密码 `/user/password`（比对加密后密码）+ 手机验证码 `/user/form`（比对 `login:code:phone`）；查用户逻辑复用；共用 JWT 配置；坑：验证码 type 必须传 login 否则 key 不匹配。〔11-8〕

### 微信扫码登录（第 12 章）
- 三种形态：PC 场景二维码（本项目）、App/H5 OAuth2.0 授权；微信登录/支付必须企业服务号（订阅号不行）；无资质用课程二次封装参数实操。〔12-1〕
- 时序图四要素：对象/生命线/控制焦点/消息；链路：点击登录→接入验证→微信生成 ticket/二维码→Redis 存 `isScan:false`→扫码→微信回调→查/建用户签发 token、`isScan:true`→前端轮询拿 token；ticket=扫码会话 key，openId=微信用户唯一标识；用轮询不用 WebSocket。〔12-2〕
- 接入验证：GET `/wechat_login/callback`；花生壳内网穿透暴露本地 3000 给微信回调；微信回传 signature/timestamp/nonce/echostr，校验=三参数字典序排序+SHA1 比对 signature，通过原样返回 echostr；响应拦截器需兼容直接返回字符串。〔12-3〕
- 二维码生成三步：`getAccessToken`（所有微信能力的钥匙）→`getTicket`→拼 `qrUrl?ticket=xxx`；临时二维码 `expire_seconds:120`；Redis key `wechat:ticket:${ticket}` value `{isScan:false}` 过期 120 秒；课程环境与正式仅域名不同。〔12-4〕
- 扫码回调处理：POST 接口收 XML，`xml2js` 解析+`getLastData` 拍平多层对象；`FromUserName` 即 openId，按其查用户、无则插入（phone/password 为空）；新老用户都签发 JWT；更新 Redis `isScan:true` 并写入 token（Redis 存对象必须 JSON.stringify）；按 Event 返回关注/欢迎回复。〔12-5〕
- 轮询接口：GET `/wechat_login/check_scan?ticket=xxx`，查 Redis `isScan`，true 返回 token，否则「等待用户扫码」。〔12-6〕

### 前端登录注册（第 13 章）
- 路由：`createHashRouter` 根路由 `/` + 子路由 `loginOrRegister`/`edit`；路由守卫 `useLocation`+`useNavigate`：已登录访问登录页跳编辑页、未登录访问权限页跳登录页。〔13-1〕
- MobX 状态管理：`makeObservable` 返回响应式对象；权限 store 的 token/details 从 localStorage 初始化；自定义 hooks `useStoreAuthor` 用 `computed(()=>!!token).get()` 推导 isLogin；store 与 hooks 分模块维护、index 统一导出。〔13-2〕
- 注册组件：父组件控制登录/注册切换；AntD Form+Form.Item+useForm 五项校验（手机号/密码/确认密码/协议 `valuePropName:"checked"`/按钮）；`ahooks useTitle` 设标题；Tailwind `bg-[url(...)]` 背景图。〔13-3〕
- axios 二次封装：统一 baseURL（含 /api）+请求拦截器注入 token+响应拦截器统一处理；三接口 `/user/captcha`、`/user/sendCode`、`/user/register`；类型收敛到 share 用 `Pick<IUser,...>` 复用实体字段；约定 interface 定义可扩展实体、type 定义固定派生类型；后端 `enableCors()`。〔13-5〕
- 注册联调：`useRequest` 三接口串联；`run` 重命名 refreshCaptcha（点击图片刷新、失败重置）；`ready:true` 手动触发；短信成功启动 60 秒倒计时禁用按钮；注册成功经 MobX action 写 token 到状态+localStorage 并跳转。〔13-6〕
- 登录组件：父组件 activeKey 切换账号密码/验证码两个子组件；手机号必填+正则校验；验证码 hooks 传 type='login'；新增 `/user/password` 与 `/user/form` 接口。〔13-7、13-8〕
- 微信登录前端：按钮+Modal 弹窗；`classnames` 动态置灰；`activeQrCode` 控制 120 秒有效期过期提示刷新；轮询 `debounceWait:2000`（2 秒一次）；坑：过期时间单位毫秒（120*1000）、关闭按钮放 Modal 外层防误触。〔13-9、13-10〕

## 04. 第四期：编辑模块后端（发布/组件获取）+ 前端编辑器骨架与全部组件（14-1~16-7）

**期摘要**：第四期先做编辑模块后端：五接口梳理（发布、组件获取、OSS 上传/查询/删除）、三张实体表（page/component/component_data）、JWT Guard 鉴权（passport-jwt 策略）与事务化 upsert 发布逻辑；然后搭前端编辑器「上下+左中右」骨架与 MobX store 五状态，最后按固定范式（share 视图组件 + client 属性面板 + store 双向绑定）批量完成视频/图片/轮播/卡片/列表/文本/分割/空状态/富文本/二维码/警告等展示组件与问卷输入框/文本域/单选/多选等采集组件。

### 编辑模块后端（第 14 章）
- 接口清单与数据策略：五接口（发布、组件获取、OSS 上传/查询/删除）；进入编辑页取数顺序：localStorage 缓存最新优先 → 服务端草稿/发布按时间取最新 → 都没有画布为空；推荐开发顺序=先做复杂接口定数据结构→组件展示与属性→资源与交互。〔14-1〕
- 数据模型：三张实体表 page/component/component_data（component 的 options 用 `simple-json` 列类型）；公共类型集中 share 包，options 用 `Record<string,any>`，组件类型用 `TComponentTypes` 字面量映射；改 share 后要 `build:share` 打包别处才能引入。〔14-2〕
- JWT 鉴权链路：`@nestjs/passport` + `passport-jwt`；`JwtStrategy` 继承 `PassportStrategy(Strategy)`，`secretOrKey` + `jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken()`；`validate` 依次校验 token 有效→未过期→用户存在，并把用户挂 request；`getUserMessage` 参数装饰器从 `request.user` 取用户（返回 `Omit<IUser,'password'>`）；接口挂 `@UseGuards(AuthGuard('jwt'))`；请求头 `Bearer <token>` 注意空格。〔14-2、14-3〕
- 发布接口（事务化 upsert）：路由 `POST /local/release`；入参类型收敛 share 的 `types/local.ts`，用 `Omit` 排除前端不该传的 id/accountId（accountId 由 token 解出更安全）；流程=事务内按「用户 ID+页面 ID」查——存在则更新（Page 置空 components→删旧 Component→删旧 ComponentData→插新组件→回填 ID 数组）、不存在则创建；插入逻辑抽 `insertComponent(configId)` 共用；删除旧数据必须限定页面/用户范围、ComponentData 先查后删；三个坑：body 不传 components 后端实际报错但接口"成功"、catch 必须回滚、失败要抛 `InternalServerErrorException` 带具体 error。〔14-3、14-4〕
- 组件获取（发布接口反向回显）：GET `release/withUser` 不传参只靠 token；Service 按用户查页面→遍历 componentIds 逐个查组件表（id 要 `Number()` 转换，页面表存的可能是字符串）；返回 components（渲染用）+ componentIds（维护顺序用）；Module 少注册依赖启动报「找不到依赖」。〔14-5〕

### 编辑器前端骨架（14-6~14-9）
- 布局：`flex flex-col` 上下 + `flex` 左中右三栏；头部=标题/预览/草稿/发布/统计入口/头像；画布 `overflow-y:auto` 横向隐藏；左右面板 AntD `Tabs`+items 数组，图标 `@ant-design/icons`；目录规范：页面专属组件放 `pages/editor/`，公共组件才放 `components/`。〔14-6〕
- 左侧组件列表：两份配置数组（展示型/问卷输入型，每项 type/name/icon）+ 公共样式组件 EditComponent 循环渲染，Divider 分组；map 渲染补唯一 key；type 提前入配置留扩展点。〔14-7〕
- MobX store 五状态：`componentConfigs`（id→完整配置字典）、`sortableComponentConfig`（只存 ID 数组表达画布顺序，供拖拽）、`currentComponentConfig`（选中 ID）、`copyComponentConfig`（复制中间变量）、`itemsExpandIndex`（属性展开/折叠）；push 用 `ulid` 生成唯一 ID，同时写字典与排序数组并设选中；React 用 MobX 必须 `observer` 包裹，`toJS` 转普通对象；工具函数 `objectOmit` 剔除非原生属性、`getDefaultValueByConfig` 压深层配置为默认值。组件抽到 share 公共包（编辑页与发布页共用），`componentExport/componentList` 统一出口。〔14-8〕
- 属性面板：`GlobalFields`（全局页面属性 title/description/TDK，`onValuesChange` 经 `updatePage` MobX action 写回 store）+ `ComponentFields`（`getComponentPropsByType` 按类型映射配置组件；视图映射放 share、配置映射只放 client）；核心转换：props 在「一维表单值」与「{defaultValue, isHidden, value} 二维对象」间来回转换，数字/布尔字符串做类型归一；二次封装 FormItem 用 isHidden 控制显隐。〔14-9〕

### 组件批量开发（第 15~16 章）
- 通用组件开发范式（所有组件共用）：①share 放视图组件+类型+默认值，②client 放属性配置组件，③新增组件必改三处（组件 index.ts 导出、types.ts 加类型、componentExport 注册），④改 share 必须 `pnpm build:share`，⑤数据流=右侧表单改值→store（action）→视图 `useMemo`/observer 响应式刷新；通用配置形态=`value/defaultValue/isHidden` 三件套；列表型组件（轮播/列表/单选多选）复用 `FormContainerWithList`，非列表用 `FormContainer`。〔15-1~16-7 贯穿〕
- 图片组件：属性 id/url/name/height/handleClick('open-url'|'none')/fit/link；`open-url` 时 `<a>` 包裹；`fit` 对应 object-fit 默认 cover；配置面板坑：函数被当 type 导入（fillComponentPropsByConfig 是函数）。〔15-1、15-2〕
- 轮播图：AntD Carousel 遍历 images（每项复用 ImageComponent）；属性 id/interval(默认 3000ms)/autoplay/images/showIndicators/指示器方位 bottom/top/left/right；双层表单封装 FormContainer（整体设置）+ FormContainerWithList（图片列表，keyName/id/value 数组/newItemDefaultValue 四参）；双向绑定闭环=handleValuesChange（视图→数据，Object.entries+toJS+两个 update）+ omit+form.setFieldsValue（数据→视图）。〔15-3、15-4〕
- 卡片：AntD Card+Card.Meta，三属性封面图/标题/描述；React 双向数据流需自己实现（改数据写回 store、视图从 store 取数）。〔15-5〕
- 列表：AntD List+List.Item.Meta，`itemLayout` 横排、dataSource 来自 store、renderItem 自定义；属性=每项标题/描述/标题跳转/头像+新增项。〔15-6〕
- 文本：`<span>` + switch 映射五档 Tailwind 字号（text-xs~text-xl）；属性仅 title/size；用 Segmented 做选项。〔15-7〕
- 分割线：AntD Divider，属性 text/dash/orientation；透传前 objectOmit 剔除 Divider 不接收的 text，文本用自定义 span 承载。空状态：Empty，可配 description/图片/宽高/填充。〔15-8〕
- 富文本：视图 `dangerouslySetInnerHTML`（空内容显示占位提示），配置用 `react-quill`（useRef+ref 绑实例、theme="snow"、value 绑 store、onChange `editor.getHTML()` 写回、modules 配工具栏 h1-h4/加粗/颜色/对齐/列表/code-block）；样式坑：Tailwind base 重置了 h1~h6/ol/ul 默认样式，须在全局样式补回且放在 Tailwind 之后。〔16-1〕
- 二维码：AntD QRCode，属性 value/icon/size/iconSize/color/bgColor/errorLevel；纠错等级 L/M/Q/H≈可容忍 7%/15%/25%/30% 缺损（等级越高越耐遮挡，缺损需分散分布）；value 默认 "-" 占位保证画布可见；坑：ColorPicker 回调返回颜色对象，需断言后 `toHex()` 存字符串。〔16-2〕
- 警告：AntD Alert 四属性 type(success/info/warning/error)/message/showIcon/closable；布尔项用 Switch、枚举项用 Select。〔16-3〕
- 采集型组件（问卷）：与展示型区别=视图组件必须预留 `onChange/onUpdate` 回调把用户输入抛给发布页；输入框 LocalInput（title/text/placeholder/onUpdate，onChange 取 event.target.value）；文本域 LocalTextarea=复用输入框配置面板只把 Input 换成 `Input.TextArea`（零成本复用）；单选 LocalRadio（Radio.Group，defaultRadio+options[{id,value}]，按选项 id 比对回传）；多选 LocalCheckbox（Checkbox.Group，选中态是数组、onChange 抛 id 数组，默认选第一项）；组件清单靠类型名映射，导出名写错触发遍历断链+TS 警告。〔16-4~16-7〕

## 05. 第五期：OSS 资源体系 + 编辑器高级交互（拖拽/键盘/工具栏/草稿/预览/发布）+ H5 发布页（17-1~20-8）

**期摘要**：第五期两条主线：①资源体系——阿里云 OSS 动态模块（uploadToAliOss/deleteFromAliOss）、resource 表三接口（上传/获取/删除，RESTful DELETE）、前端三层公共资源选择组件与 FormData 上传；②编辑器高级交互——dnd-kit 拖拽排序、键盘快捷键（含 mobx-shallow-undo 撤销重做）、IntersectionObserver 工具栏定位与滚动显隐、localStorage 草稿与 storeTime/releaseTime 时间戳取舍、预览、发布与 readDataFromServer；最后用 Next.js release 子项目实现 H5 发布页（免登录渲染 + 设备指纹防重复提交问卷）。

### 阿里云 OSS 资源后端（第 17 章）
- 接入动机：图片/视频大资源托管 OSS，减轻应用服务器存储与带宽压力；`AliOssModule` 动态模块 + `@Global` 全局可用；配置 region/accessKeyId/accessKeySecret/bucket/自有域名（CNAME 解析替换 OSS 默认域名）；AccessKeySecret 只展示一次要保存好。〔17-1〕
- 上传配置：multer 中间件拿 file 对象；`uploadToAliOss`：文件名转码→OSS 路径拼接（`upload-files/原名-时间戳.扩展名`）→`put` 上传→删除本地临时文件→正则替换默认域名为自有域名。〔17-1〕
- 上传接口：`POST /resource/upload`；ResourceEntity 五字段（id/url/userId/type/name）——先落库 URL 让前端按记录取资源；`FileInterceptor('file')`+`@UploadedFile()`+`@Body()` type；复用登录鉴权解 token 取 userId；中文名转 UTF-8 防乱码；跨服务器域名通过阿里云「添加记录」绑定 Bucket。〔17-2〕
- 删除：`deleteFromAliOss(url)` 三步——剔除自定义域名→保留文件名+后缀（即对象 key）→decodeURI 解码；`res.status===204` 判成功，失败抛 BadRequestException。〔17-3〕
- 删除接口：RESTful `DELETE /resource`，Query 传记录 id（≠OSS 对象 URL）；service 四步=查存在→删 OSS→按 id+userId 双条件删库→返回；不存在抛「资源不存在」；OSS 与 DB 同步清理。〔17-4〕
- 获取接口：GET 按 userId+type（image/video）find 全量返回，供上传弹窗回显复用。〔17-5〕

### 前端资源管理（18-1~18-3）
- 上传链路：`UploadEditorChoiceInput`（type+propName）替换占位 input；弹窗 AntD Modal（visible 控制、loading 三元切换旋转图标）；`useRef` 触发隐藏 `input[type=file]`，选中后 `FormData` 传 type+文件，headers `multipart/form-data`；上传成功必须重新请求资源获取接口刷新列表并清空 input；视频缩略图用 OSS「截取第一帧」参数。〔18-1〕
- 资源选择三层组件：UploadEditorChoiceInput（按钮）→ UploadComponent（弹窗拉列表）→ LowResource（单卡：图片/名称/悬浮/删除/选中）；`handleChoice` 按 listOption 区分单图（updateCurrentComponent）与列表多项（keyName 定位 image/video/items 数组，展开运算加新值；数组更新走多维取值路径不能与单个混用）；弹窗 useEffect 监听 visible 拉资源；顺带修：统一 `{code,message,data}` 响应格式、token 拼 `Bearer ` 前缀。〔18-2〕
- 删除联调：useRequest→deleteResource→成功提示并刷新列表；典型 bug：轮播多图改第二张总改到第一张——根因是没维护当前展开项索引，补 store `itemExpandIndex`+action `setItemExpandIndex`+FormContainerWithList 里 useEffect 同步修复；公共组件铺到卡片/轮播（listOption）/视频面板。〔18-3〕

### 编辑器高级交互（18-4~18-8）
- 拖拽排序（dnd-kit）：DndContext+SortableContext（传组件 ID 数组+垂直策略）+useSortable（每项解构 attributes/listeners/setNodeRef/transform/transition）；useSensors 设 2 像素激活约束提升灵敏度；closestCenter 中心点碰撞检测；transform 的 Y 轴 replace 为空避免样式跳变；onDragEnd 取 active/over（over null 直接 return），MobX action+`arrayMove(oldIndex,newIndex)` 重排——拖拽本质是数组索引交换；onDragStart 设选中+isDraggable 蓝色边框。〔18-4〕
- 键盘操作：事件集中 hook + ahooks `useKeyPress`；上移/下移=取旧索引+arrayMove（首尾边界提示）；删除=同时清排序数组与配置字典并重设选中；复制粘贴必须 ulid 重新分配 ID（粘贴项默认选中）；撤销/重做交给 `mobx-shallow-undo`（hasUndo/hasRedo 判定可用性）；核心思想=把视图操作翻译成 store 数据的增删改查。〔18-5〕
- 工具栏定位：`IntersectionObserver`（threshold:0.9，露出<90% 隐藏，root=canvas 容器，useEffect return 里 disconnect 清理）；`data-id` 匹配选中 DOM→`getBoundingClientRect()`（top/bottom/left/right 相对视口零点，right 是到零点不是到右边缘）→绝对定位 left=rect.right、top=rect.bottom-工具栏高度；显隐双来源=父 showToolBar（滚动）+子 localHidden（可见性）；组件名由 componentList 按 type 匹配。〔18-6〕
- 工具栏刷新技巧：布尔 state `ifReach` 作 useEffect 依赖，点击置 true 触发重算、非首次分支改回 false 借第二次执行「强制刷新」；首次挂载 setTimeout 延迟 500ms 再 resizeComponent（DOM 未就绪拿不到坐标）；删除/上移/下移按钮复用键盘操作方法。〔18-7〕
- 滚动显隐：策略=滚动即隐藏、停止 200ms 再显示、滚出超 10% 保持隐藏；useRef 绑画布父容器+addEventListener('scroll')，清理函数移除监听与定时器；handleScroll 反复 clearTimeout 实现防抖；父调子方法用 `useImperativeHandle`+ref；classnames 拼 hidden 类；拖拽结束 setIfRefresh(true) 强制重算坐标。〔18-8〕

### 头部功能与数据取舍（第 19 章）
- 动态标题：标题值在 store `page.title`，`useStorePage`+`setPageTitle` action；`isEditState` 双态切换（h1+编辑按钮 ↔ Space+Input+CheckOutlined）；扩展运算符抽公共 className/onClick props。〔19-1〕
- 草稿机制：存三份 store 状态（componentConfigs/sortableComponentConfig/currentComponentConfig）；MobX 数据先 `toJS` 再 `JSON.stringify` 写 localStorage，额外记 storeTime；恢复时 getItem+JSON.parse 覆盖回 store；`storeTime` vs `releaseTime` 转 number 比大小决定读本地草稿还是服务端发布；缓存为空或更早走服务端分支。〔19-2〕
- 预览：点击=先写 localStorage 草稿+`useNavigate` 跳 `/preview`；预览页 useEffect 恢复数据；PreviewCanvas 复用编辑页渲染链路（getComponentById→generatorComponent→getComponentByType→toJS→展开 props），observer 包裹；返回按钮 `navigate(-1)`。〔19-3〕
- 发布：把 store 数据（排序数组+配置映射）转后端入参结构；useRequest manual:true 调发布接口，onSuccess 拿 data 跳转+提示；发布成功缓存 releaseTime 并自动执行一次存草稿。〔19-4〕
- readDataFromServer：本地草稿时间晚于发布→readDataFromLocal；否则 GET `/local/releaseWithUser`→后端结构转 store 结构（componentConfigs 映射+sortableComponentConfig 数组）→默认选中第一个组件→updatePage 更新标题/TDK/描述；修正后端少返回字段。〔19-5〕

### H5 发布页（第 20 章）
- 需求与表设计：发布页=Next.js SSR，面向第三方用户免登录；三接口（获取发布页面组件、是否提交过问卷、提交问卷）；component_data 表四字段 pageId/componentId/userKey（IP+设备加密，实现同设备不可重复提交）/props（用户填写内容）。〔20-1〕
- 组件获取接口：与编辑平台逻辑几乎一致但不需要登录；复用服务层；坑：user 为空导致报错的处理。〔20-2〕
- 是否提交过问卷：按 configId+IP+设备加密 key 查 component_data，`findOne` 查到 true/查不到 false，前端据此整页置灰（`select-none`+`pointer-events-none`+降透明度）。〔20-3〕
- 提交问卷：POST body 传 pageId+props（`{id,value}` 数组）；key 不存在 save 插入、存在理论上更新。〔20-4〕
- release 子项目初始化：workspace 中 create-next-app→删 package-lock.json（pnpm 统一管理）→改名 `@lowcode/release`→`pnpm --filter` 关联 `@lowcode/share`；AntD 接入（App Router 模式）。〔20-5〕
- 页面渲染：动态路由取参→fetch 请求→ComponentRender 子组件复用 share 公共组件渲染；输入型组件回写逻辑（onUpdate 回调收集 `{id,value}`）；`useImmer` 管理本地组件数据。〔20-6〕
- 提交交互：检查接口 useRequest→置灰切换；提交前完整性校验（单选/多选有默认值排除，只校验 input/textarea 映射的 options.text）；提交成功 isPost=true 整页置灰不可再点。〔20-7、20-8〕

## 06. 第六期：后台数据统计 + Excel/压缩包导出 + ECharts 动态图表 + Docker 部署与 DevOps 认知（21-1~24-4）

**期摘要**：第六期前半做后台数据统计模块：三个后端接口（问卷组件/问卷内容/按 ID 查组件数据，In 操作符、Promise.all 聚合、flat 降维），前端表格（antd Table 动态表头/数据重组）、ExcelJS 导出 Excel + JSZip 压缩包、echarts-for-react 饼状图与横向柱状图；后半进入部署：编辑端 `<embed>` 内嵌发布页、Dockerfile 指令详解与四个镜像（server/release + 两个 nginx）、docker-compose 编排四容器、DevOps/CI-CD 概念与云效流水线全貌。

### 编辑端内嵌发布页
- React 编辑项目新增 `release` 路由，HTML `<embed>` 标签内嵌 Next.js 发布页 URL，路由参数透传页面 ID；AntD QRCode 把发布页 URL 生成扫码二维码；返回按钮 `nav(-1)`。〔21-1〕

### 后台数据统计后端（21-2~21-5）
- 页面结构：左=用户数据表格（表头来自问卷组件 title，内容来自 component_data），右=组件列表+动态图表（输入型只列填写者名单，radio/checkbox 才能出图）；三接口=获取问卷组件（表头）、获取问卷组件内容（行数据）、按 ID 查某组件数据（图表数据源）。数据澄清：component 表存组件配置（类型/title/options），component_data 存用户填写结果。〔21-2〕
- 获取问卷组件：TypeORM `In` 操作符一次性查出 input/textarea/radio/checkbox 四种类型组件。〔21-3〕
- 获取问卷内容：先校验页面存在→查 component_data→`Promise.all` 聚合每条记录的异步查表结果成数组。〔21-4〕
- 按 ID 查组件数据：按 pageId 查→`filter` 筛目标组件→value 统一为数组（输入型字符串用 [] 包裹）→`flat` 降维；radio/checkbox 的 options 来自 `component.options.options`，输入型为 null。〔21-5〕

### 后台统计前端（21-6~22-5）
- 布局：编辑头部加统计入口、dataCount 路由；左表格区右图表区；无问卷组件/无提交数据时置灰（handleDisable）。〔21-6〕
- 动态表头：useRequest 未设 manual 进页即请求；`data.length===0` 置灰提示「请至少创建一个表单组件」；表头重组为 antd Table `{title, dataIndex, key}`（key/dataIndex=组件 id，title 取 options.title 有兜底）。〔21-7〕
- 表格内容：数组包数组二维结构重组为 dataSource；radio/checkbox value 为空给默认值「选项一」；checkbox 数组 `join(',')` 转逗号串；数字兜底转字符串；组件 id 当 key 会触发 React key 冲突警告（课程暂忽略）；组件 ID vs 选项 ID 要区分。〔21-8〕
- Excel 导出（ExcelJS）：`jsonToExcel`（utils/excel）把 antd 表头改造成 Excel 列头+填行数据；`workbook.xlsx.writeBuffer()` 转 Buffer→Blob（数组包裹+`application/octet-stream`）→`URL.createObjectURL` 生成临时 blob: URL→`<a download>`+click() 触发下载→**`revokeObjectURL` 释放内存**；`isWriteFile` 开关区分导出 Excel/压缩包两条分支。〔21-9、21-10〕
- 压缩包导出（JSZip）：复用生成 Buffer 逻辑，`isWriteFile=false` 走 `excelToZip`；`zip.file(name, content)`+`zip.generateAsync({type:'blob'})`（JSZip 内部处理 Blob 转换）；下载复用 saveFileWithBlob 链路。〔22-1〕
- 动态图表：右侧组件表格三列（标题/类型/操作）写死表头，ComponentSelect 子组件 useState 维护 currentSelect 默认选第一项，已选行按钮 disabled；`useMemo`+['radio','checkbox'] 判断 isInput 分流输入型（generateText 文本列表，二维数组 `flat()` 拍平）与图表型；useRequest manual:true 点「查看数据」run(id) 重请求。〔22-2、22-3〕
- ECharts：`echarts`+`echarts-for-react`（ReactECharts 只吃 option）；数据整理成 `{name,value}`（reduce 统计选项出现次数），title/数据用 useMemo 随 currentSelect 动态计算；饼状图 `series[0].type='pie'`+radius 控制圆大小+legend 图例位置；横向柱状图 `yAxis.type='category'` 放分类名（横向的关键在 Y 轴）、xAxis 放数值+max=100、`showBackground:true`+backgroundStyle 铺灰底 100% 做对比、`grid.containLabel:true` 防长名被裁。〔22-4、22-5〕

### Docker 部署（23-1~24-2）
- Docker 三大核心：仓库（Docker Hub）/镜像（静态模板）/容器（运行实例）；链路=Dockerfile→`docker build` 镜像→容器→启动项目；解决传统部署「每次迭代重配环境」。〔23-1〕
- Dockerfile 指令表：FROM（基础镜像）/MAINTAINER/RUN（构建时）/CMD（启动时，数组形式）/EXPOSE/ENV/ADD|COPY（宿主机文件进镜像，ADD 可自动解压）/VOLUME（持久化映射）/USER/WORKDIR/ONBUILD；文件命名 `.Dockerfile`（D 大写）；示例：`FROM node:16 alpine`（体积小）+国内镜像源+yarn+PM2 管进程+EXPOSE 8081。〔23-2〕
- 部署分工：React 编辑平台是 SPA 纯静态→直接传阿里云 OSS Bucket 指定 index.html+绑域名，不打镜像；Next.js release 与 NestJS server 需常驻→打镜像；后端前面再架 Nginx 反向代理/负载均衡。〔23-2、23-3〕
- Server.Dockerfile：FROM node:18→WORKDIR /app→COPY . .→npm config set registry 国内源→npm i -g pnpm→pnpm install→**先 `pnpm build:share` 再 `build:server`**（后端依赖 share 的 TS 类型，顺序不能错）→EXPOSE 3000→`CMD ["pnpm","start:server"]`。〔23-3〕
- Nginx 镜像：`FROM nginx:1.25.0-alpine`+`ADD ./nginx/server.nginx.conf /etc/nginx/nginx.conf`（覆盖默认，未写的模块沿用默认值）+EXPOSE 80；nginx.conf：http{} 里 `upstream backend`（每条 `server IP:port weight=N` 权重决定分发）+`server{listen 80; location / {proxy_pass http://backend}}`（proxy_pass 名字须与 upstream 一致）+`events{worker_connections 1024}`（按负载调整）；命名坑：后端配置别写成 release.nginx.conf。〔23-4〕
- release 镜像：复制 server.Dockerfile 改构建/启动命令（build:release/start:release），其余通用；release 也要单独一层 nginx（SSR 不能像静态站直接部署），服务名必须改 release 防撞名；服务器 IP 要换成自己的。〔23-5、23-6〕
- Docker Compose：YAML 编排多容器替代一长串 docker run；version 3 系、services 缩进即服务，image/restart/container_name/environment/ports 对应 run 参数；`docker compose -f docker-compose.yaml up -d`；本项目四容器：backend(5001:3000)、backend_nginx(5000:80)、frontend(4001:3000)、frontend_nginx(4000:80)，服务器须放行四端口，`restart:always`；image 用 `${xxx_tag}` 变量为云效镜像仓库做映射（Dockerfile 产镜像、Compose 跑容器，别混淆）。〔24-1、24-2〕

### DevOps 认知（24-3、24-4）
- 团队演进：一人全包→瀑布模型（阶段串行、人工上线）→敏捷开发+CI/CD；完整上线流程=需求评审→设计→前后端开发→测试→缺陷修复→预发/灰度→上线→迭代。DevOps=Development+Operations 开发测试运维一体化；CI/CD 是构建/测试/部署自动化流水线，是 DevOps 的技术落地。〔24-3〕
- 云效流水线全貌：控制台搜「云效 DevOps」→流水线 Flow；代码须先托管 Codeup；空模板+流水线源（仓库+分支）；阶段一=构建 monorepo（先 share）→前端产物传 OSS（packages/client/dist）→上传 compose 制品；阶段二=并行构建推送四个镜像（标签变量映射）→下载制品→删旧容器旧镜像→`docker compose -f ... up -d`。〔24-4〕

## 07. 第七期：云效流水线实操 + 自动化部署上线排错 + JMeter 入门（25-1~28-3）

**期摘要**：第七期把部署做成真流水线：云效 Codeup 关联代码源→React 打包构建传 OSS→compose 文件归档公共存储→四个镜像并行构建推送 ACR→主机部署下载制品/清理旧容器/`docker compose up -d`→修一轮真实 BUG（多冒号、文件名、tar -c/-C）→换线上 IP 端口→绑定域名→全功能线上验收；随后引入 JMeter 压测（为什么学、性能测试分类、工具对比、"不是浏览器"的关键认知）。

### 云效流水线构建阶段（25-1~25-8）
- 流水线源两条路径：Codeup 仓库内创建（自动带出仓库与服务连接）vs 流水线 Flow 模块新建（需手填仓库地址+服务连接，支持 GitHub/Gitee/GitLab）；分支选 master。〔25-1〕
- React 打包构建：任务步骤改「Node.js 构建」，Node 18.12；构建脚本五动作=设镜像源→`npm install pnpm -g`→`pnpm install`→`build:share`→`build:client`（必须先 share）；产物 dist。〔25-2〕
- OSS 上传：新建 Bucket 三项配置=绑定域名（可后补）、静态页面首页 `index.html`、读写权限**公共读**；流水线 OSS 上传步骤：Bucket 目录可不填、**源文件目录必填**=`packages/client/dist`；dist 不进代码库由流水线生成，上传必须接在构建后。〔25-3〕
- compose 制品：构建物上传步骤→「归档至云效公共存储空间供后续任务拉取」；制品名（Artifact）用于部署阶段凭名称下载；镜像推送目标是阿里云容器镜像服务 ACR。〔25-4〕
- 四镜像构建（并行任务）：开通 ACR 个人版免费实例+命名空间；「阿里云镜像构建个人版」步骤：地域与服务器同域（广州）、仓库/命名空间 `local-images`、标签自定义且对应 compose 变量——`backend-nginx-*`（server/nginx.dockerfile）、`backend-*`（server.dockerfile）、`frontend-nginx-*`（release/nginx.dockerfile）、`frontend-*`（release.dockerfile）；任务输出含镜像公网地址；命名 frontend-nginx vs frontend 别混淆；ACR 留历史镜像占空间可清理。〔25-5~25-8〕

### 部署阶段与排错（26-1~27-8）
- 主机部署：新建部署阶段+「主机部署」任务；勾选部署时下载制品（凭制品名）；主机组关联自有服务器（首次新建主机组）；下载路径如 `/root/yx/backend.tgz`（目录不存在自动创建）；执行脚本解压。〔26-1〕
- 清理脚本：`docker ps -a | grep local | awk '{print $1}'` 提取容器 ID 再 stop/rm；删镜像取 `docker images` 第三列（IMAGE ID）而非第一列；`|| true` 关键——首次部署无容器时命令失败不能中断流水线。启动 `docker compose up -d`。〔26-2〕
- 镜像变量：部署任务配置 `backend_tag/backend_nginx_tag/frontend_tag/frontend_nginx_tag` 四变量关联上游制品标签，注入 compose 的 `${xxx_tag}`；触发方式手动或自动（每次提交）。〔26-3〕
- 上线改配置：两处 Nginx 代理地址（server nginx→后端 5001、release nginx→前端 4001）；开放阿里云安全组；React client 请求地址与 release 服务端渲染请求后端地址（componentRender.tsx/page.tsx）改为线上后端 Nginx 代理 5000；提交代码触发流水线。〔27-1〕
- 真实 BUG 三连：①Dockerfile `FROM nginx` 多写冒号致拉基础镜像失败（海外拉取慢是提醒非报错可忽略）；②`release.dockerfile` 文件名多了字母 s（Releases）；③解压脚本 tar 的 `-C`（切换目标目录）误写 `-c`（创建归档）——修完流水线三阶段全通。〔27-2~27-4〕
- 线上验收：后端直连 5001/代理 5000；发布页直连 4001/代理 4000；实测问卷提交落库；编辑平台 Bucket 绑已备案域名（支持跨账号+所有权验证）+CNAME 解析（主机记录=二级前缀，记录值=Bucket 地址）；逐项验收登录/增删/拖拽/上传/草稿/预览/发布/统计/导出/图表；安全提醒：OSS accessKeySecret 必须换真实密钥否则资源传到他人账户。〔27-5~27-8〕

### JMeter 入门（28-1~28-3）
- 学压测的价值：上线前流量瓶颈评估、判断并发上限；面试加分（全栈工程师）；JMeter vs Postman=性能压测 vs 接口功能调试。〔28-1〕
- 性能测试四分类：性能测试/压力测试（极限探测）/负载测试（递增加压找拐点）/稳定性测试（长时间）；工具对比：LoadRunner（稳定精细但笨重）、Apache ab（轻量单接口、对目标负载大）、Web Bench（老牌少用）、JMeter（开源免费、多协议、分布式、大厂二次封装、主流）、Postman（功能测试不擅压测）。〔28-2〕
- 关键认知：JMeter 是 Apache 基于 Java 的开源性能测试工具；**不是浏览器**——协议层工作、不执行 JS/不渲染 HTML，适合压测后端异步接口（axios/fetch 请求），不适合 UI 功能测试（与 UI 自动化测试区分）。〔28-3〕

## 08. 第八期：JMeter 实战全流程 + 接口优化 + 简历面试（28-4~31-4）

**期摘要**：第八期把 JMeter 从安装讲到实战闭环：JDK8 环境与汉化、线程组/取样器/监听器/聚合报告、setUp/tearDown/调度器、请求默认值与信息头管理器复用、响应断言与集合点；然后对低代码平台五个真实接口逐一压测，并用 Redis 缓存 `getCacheData` 优化取组件接口做 QPS 前后对比；最后是简历面试篇：技术栈写法铁律、项目经验面试官视角、完整简历模板与低代码项目亮点话术。

### JMeter 基础（28-4~28-9）
- 安装：必须 JDK 8（高版本有兼容问题，生产也以 JDK8 为主）；JMeter 5.6.3 zip 跨平台解压即用；启动 `jmeter`（macOS/Linux）/`jmeter.bat`（Windows）/`jmeter-server`（分布式主节点）；目录 bin（脚本+`jmeter.properties` 配置）/extras（插件）/lib（依赖 jar）；永久汉化改 `language=zh_CN`。〔28-4〕
- 线程组三参数：线程数（虚拟用户数）× Ramp-Up（多少秒启动完）× 循环次数（总请求=线程×循环）；「永远」循环用于稳定性测试；一个线程组可挂多个取样器、可多线程组分模块。〔28-5〕
- 取样器（HTTP 请求）：填协议/IP/端口/方法/路径；GET 参数在「参数」面板，POST JSON 在「消息体数据」。〔28-5〕
- 监听器作用域：放取样器下只看单接口、线程组下看全组、测试计划下看全部；查看结果树=逐条明细（Sampler result/Request/Response）；聚合报告=汇总指标；`.jmx` 只存脚本结构监听器需每次添加；调试先小规模（10 线程/1s/循环1）跑通。〔28-6〕
- 结果解读与乱码：跑前用「扫把」清空旧数据；**90% Line=90% 请求响应时间低于该值**（不是 90% 不出错，错误率看异常%）；中文乱码改 `jmeter.properties` 的 `sampleresult.default.encoding=UTF-8` 重启。〔28-7〕
- 特殊线程组：setUp（最先，前置准备：登录拿 token/初始化数据）→普通线程组→tearDown（最后，清理数据/释放资源）；调度器=持续时间+启动延迟（秒），用调度器必须循环设「永远」；换算：1 小时=3600 秒。〔28-8〕
- 复用利器：HTTP 请求默认值（公共协议/IP/端口）+HTTP 信息头管理器（统一请求头），推荐放测试计划级全局复用；POST+JSON 必须设 `Content-Type: application/json`（否则 text/plain 后端解析失败）。〔28-9〕

### JMeter 实战进阶（29-1~29-3）
- 核心指标：TPS（每秒事务，侧重增删改写库业务）、QPS（每秒查询，侧重读）、RT（响应时间，核心接口建议 <200ms，Network 面板看 Time）；纯查询吞吐 TPS/QPS 口语混用。聚合报告列：Label/# Samples/Average/Median（50% Line）/90%/95%/99% Line（长尾延迟）/Min/Max/Error%/Throughput/Received-Sent KB/sec；数值与机器强相关，重点读数与加压方法。〔29-1〕
- 压测方法论：低线程起步逐步加压（1→50→100→200），以「异常%=0 且吞吐量最大」定位性能水位=最优 TPS。〔29-1、30-1〕
- 响应断言：默认只看 HTTP 200 会漏掉业务层「假成功」；响应断言=校验字段（响应文本/响应代码/响应信息/头/URL）+匹配规则（包括 Contains/匹配 Matches 正则/相等 Equals）；性能注意：高并发下优先简单断言，少用正则（开销大拖垮压测机数据失真）。〔29-2〕
- 集合点（Synchronizing Timer 同步定时器）：普通线程组+Ramp-Up 是分批并发非同一时刻；集合点把线程凑齐同时释放，模拟秒杀/抢课瞬时高压；参数=模拟用户组数量（≤线程数、最好整除）+超时毫秒（>0 如 10ms 防个别线程异常整组卡死）。〔29-3〕

### 平台接口压测与优化（30-1~30-6）
- 登录接口：POST `/api/user/password_login`+JSON 体；四件套=线程组+请求默认值+信息头管理器+监听器；登录涉及写库/查库/token 生成用测试账号。〔30-1〕
- 带鉴权接口：获取问卷组件（GET 需 `Authorization: Bearer <token>`）；复用脚本=复制线程组→改路径→清空消息体→加鉴权头；自动化可结合正则/JSON 提取器把登录响应 token 提取为变量。〔30-2、30-3〕
- 写接口：提交问卷（POST+JSON，真实入参可先手动提交抓包获得）；写库加压观察异常%与数据库负载。〔30-4〕
- 是否提交过问卷：GET+query pageId，基线约 18ms、约 55/s。〔30-5〕
- 缓存优化对比：压测口径一致（清空报告/禁用其他取样器/固定线程数）；`getCacheData(cacheKey, callback, {ttl, force})`——命中直接返回，未命中执行 callback 查库并 set 回填（TTL 过期），force=true 强制清缓存主动失效；回调内 Promise.all 并发查+filter 筛空值组装 components/id 数组；实测有缓存 QPS 约 428~440 vs 无缓存约 410（提升有限但稳定）；该方法可推广到其它接口，优化不改业务查询本身。〔30-6〕

### 简历与面试（31-1~31-4）
- 技术栈写法「有横有纵」：核心框架（React）懂原理；周边框架（Next.js/NestJS）会用+知道设计思想与优缺点；必须有几个「很懂」的框架（React、Vue 3，能讲原理+同类方案对比）；**铁律：绝不写「精通」**（用熟悉/掌握/了解）；不懂的不写、学会引导面试官到熟悉的框架、初中级适当删减、目标高级岗着重准备安全/测试/自动化部署/性能优化。面试知识面：语言基础/框架（含目标公司实际技术栈）/网络/算法/数据库/设计模式/高并发高可用分布式/性能优化/测试/安全/产品运营思维。〔31-1〕
- 项目经验面试官视角：公司介绍只写名/业务/产品/规模；项目描述除负责模块外必须提前备好团队规模（如前端组 3 人任组长）、团队配置、运维测试安排（无专职运维、开发用云效部署）、开发周期（1-2 年迭代、初版 1-2 个月跑通主流程）；并发类刁钻问题用 JMeter 压测数据+Redis 缓存/代码优化前后对比作答；包装边界=可润色但前提真懂、经得起细节追问，非实际参与的项目不写。〔31-2〕
- 简历技术栈分类法：编程语言与样式（HTML/CSS/JS/ES6/TS/Less-Sass/Tailwind）、框架与多端（Vue3 全家桶/Nuxt/Next.js/小程序+APP 多端/React+自定义 Hooks+ahooks+immer+MobX）、开发工具（Webpack 包体积优化/Vite/Babel/Git）、服务端（Linux 命令/Docker+Compose/Nginx 反代负载均衡/MySQL+ORM/Express-NestJS/Redis 自定义 key+发布订阅/RabbitMQ 死信队列延时关单）、运维云服务（CI/CD+DevOps 云效/阿里云服务器域名 HTTPS/OSS 加速/视频点播/微信支付/OAuth2.0）；没学的如实删减防露怯。〔31-3〕
- 低代码项目简历结构：项目名称→项目描述（非开发人员也能发布官网与问卷系统，提效省人力）→分模块技术栈（前端/后端/第三方服务/运维）→个人职责→项目亮点。个人职责真实项：@dnd-kit 拖拽+键盘排序并同步状态、自定义 Hooks（键盘事件/登录权限/选中移动/页面信息）、useMemo 渲染优化+高阶函数封装+TS 静态校验、ahooks+AntD 二次封装、MobX+observer 全局状态（易错点：Vuex 默认响应式而 MobX 必须 observer）、DevOps CI/CD+Docker+ECS 一键部署+OSS 静态资源、Next.js SSR 优化 SEO（注意别误写 Nest）、pnpm workspace 跨项目复用（share 放 AntD 组件/types 实体与入参类型/utils 工具方法/componentExpose 统一导出）、自定义字段在线 Excel+压缩包下载+动态图表+Nginx 反代负载均衡。亮点：workspace 最大复用、拖拽+键盘、一键部署、Redis 自定义 key+企业级图形/短信验证码+原子性防重提交、在线 Excel 预览与压缩包下载；三个子项目部署位置区分（React 上 OSS、Next.js/NestJS 上服务器）；亮点要能讲清「为什么做」（如验证码防刷背后的短信套餐成本）。〔31-4〕

---

## 技术栈全景（课程出现的所有技术/库/工具及用途）

### 前端
| 技术 | 用途 |
| --- | --- |
| React 18（函数组件） | B 端编辑器与数据统计前端（client 子包） |
| TypeScript | 全端静态类型（interface 实体/type 派生、Omit/Partial/Pick/Record、泛型组件） |
| Next.js 14 App Router | C 端 H5 发布页 SSR（SEO）、动态路由/路由组/服务端 async fetch |
| MobX + mobx-react-lite | 编辑器公共状态（componentConfigs/sortableComponentConfig 等五状态）、observer 响应式 |
| mobx-shallow-undo | 撤销/重做（hasUndo/hasRedo） |
| ahooks | useRequest（manual/ready/loading/run/onSuccess/debounceWait 轮询）、useKeyPress、useTitle |
| @dnd-kit | 画布组件拖拽排序（DndContext/SortableContext/useSortable/closestCenter/arrayMove） |
| ulid | 组件唯一 ID 生成 |
| immer（useImmer） | 发布页本地组件数据管理 |
| Ant Design 5 | 全套 UI（Form/Table/Tabs/Modal/Carousel/Card/List/Alert/QRCode/ColorPicker/Segmented/Popconfirm 等） |
| Tailwind CSS | 原子化样式（bg-[url]、flex 布局、text-xs~xl），坑：base 重置富文本标题样式 |
| ECharts + echarts-for-react | 问卷数据饼状图/横向柱状图（{name,value} 数据流） |
| ExcelJS | 前端生成 Excel（writeBuffer→Blob→a.download 下载） |
| JSZip | Excel 打包 ZIP 压缩包导出 |
| axios | 二次封装（baseURL/请求拦截器注入 token/响应拦截器统一处理） |
| react-router-dom | createHashRouter/RouterProvider/Outlet/useNavigate/useLocation 路由守卫 |
| react-quill | 富文本编辑组件 |
| classnames | 动态类名（按钮置灰、工具栏 hidden） |
| xml2js | 微信回调 XML 解析（编辑端没有，后端） |
| local-captcha 相关：svg-captcha | （后端）图形验证码 SVG 生成 |

### 后端
| 技术 | 用途 |
| --- | --- |
| NestJS 10 | 后端框架（client/server/share 三板斧架构、IoC/DI） |
| TypeORM 0.3.x | ORM：实体同步、Repository CRUD、In 操作符、事务 QueryRunner、一对一/一对多 relations |
| mysql2 | MySQL 驱动 |
| Redis（ioredis 类封装） | 验证码短时存储（自定义 key、EX 过期）、图形验证码防刷、接口缓存 getCacheData、轮询扫码状态 isScan |
| @nestjs/jwt + @nestjs/passport + passport-jwt | token 签发/校验、JwtStrategy+AuthGuard('jwt') 鉴权链路 |
| class-validator + ValidationPipe | DTO 入参校验（@IsString/@IsNotEmpty/@Length/@IsNumber/@IsMobile 等） |
| Multer | 文件上传中间件（diskStorage 自定义目录与文件名） |
| svg-captcha | 图形验证码生成 |
| 阿里云 OSS SDK（ali-oss） | 图片/视频上传（put）、删除（delete，204 判定）、URL 域名替换 |
| crypto（Node） | MD5 加密（密码、IP+设备指纹 key） |
| dayjs | 验证码 60 秒限流时间差计算 |
| RxJS | 拦截器 Observable/pipe/map |
| 微信公众号能力 | 场景二维码登录（access_token→ticket→qrUrl、SHA1 接入验证、XML 回调） |
| 第三方短信服务 | 手机验证码发送（appId/appSecret/templateCode） |
| PM2 | （Dockerfile 示例中）Node 进程管理 |

### 工程化
| 技术 | 用途 |
| --- | --- |
| pnpm + pnpm workspace | monorepo（client/release/server/share 四包、--filter、workspace:^、依赖提升） |
| unbuild | share 公共包打包（ESM/CJS/d.ts 三产物、external 排除公共依赖） |
| Vite | React 子项目脚手架 |
| Nest CLI | nest g resource 等 RESTful 骨架生成 |
| ESLint/Prettier/tsconfig | 代码规范与编译配置（experimentalDecorators） |
| Git + 云效 Codeup | 代码托管（SSH 公钥、monorepo 统一 init） |
| Apifox / Postman | 接口调试（POST/form-data/Bearer） |
| Navicat / QuickRedis / MySQL Workbench | 数据库与 Redis 可视化、ER 图反向生成 |
| draw.io | 架构图/时序图/ER 图绘制 |

### 部署与运维
| 技术 | 用途 |
| --- | --- |
| Docker | 容器化装 MySQL/Redis、项目镜像构建 |
| Dockerfile | 四镜像：Server/release（node:18+pnpm+先 build:share）/两个 nginx（nginx:1.25.0-alpine+conf 覆盖） |
| Docker Compose | 一键编排四容器（backend 5001:3000、backend_nginx 5000:80、frontend 4001:3000、frontend_nginx 4000:80、${tag} 变量） |
| Nginx | 反向代理/负载均衡（upstream+weight+proxy_pass+worker_connections） |
| 阿里云 ECS/CentOS 7.8+ | 云服务器（安全组放行端口） |
| 阿里云 OSS + CDN | React SPA 静态托管（index.html+公共读+绑域名 CNAME）、图片视频存储、视频截帧封面 |
| 云效 DevOps（Flow/ACR/公共存储） | CI/CD 流水线：构建→OSS 上传→compose 制品归档→四镜像推 ACR→主机部署（下载制品/清理脚本/`|| true`）→docker compose up -d |
| 花生壳内网穿透 | 本地服务暴露公网供微信回调 |
| JMeter 5.6.3（JDK8） | 性能压测：线程组/取样器/监听器/聚合报告/断言/集合点/调度器，压测全平台接口并验证 Redis 缓存优化 |
| 域名/DNS/HTTPS | 域名解析、CNAME 绑 Bucket、已备案域名 |

### 数据库
| 技术 | 用途 |
| --- | --- |
| MySQL 8.0 | 五张核心表 user/page/component/component_data/resource；软删除 del、options 用 simple-json 存组件属性 |
| Redis | 见后端；key 设计：`request:code:phone`/`login:code:phone`、`wechat:ticket:${ticket}`、IP+设备 MD5 指纹 |

### 测试
- JMeter（详见 08 期）：性能/压力/负载/稳定性测试、聚合报告指标（TPS/QPS/RT/90% Line）、响应断言、集合点；Postman/Apifox 偏接口功能调试；Nest 自带 test/ 目录 e2e（提及）。

## 面试/求职向要点汇总

1. **技术选型话术**（2-3、2-4）：三维度（项目周期规模/SEO→Next.js/Nuxt、跨端→Uni App；团队兜底人与招聘成本；GitHub star/维护状态/兼容性）；面试官考察点=选择依据+决策过程+可替换方案对比+可持续性。经典案例：图形验证码+短信验证码+Redis 原子性防重提交；DevOps CI/CD 一键部署。
2. **安全类**：密码 MD5 不明文；登录失败统一提示防账号枚举；JWT payload 只放 id、verify try/catch、iat/exp 过期判断；返回脱敏不带密码；验证码 60 秒限流+图形验证码前置校验防短信盗刷（成本动机）+Redis 原子性防重提交保证与 MySQL 一致。
3. **架构与性能**：Nginx 反代+负载均衡（upstream weight）；Redis 缓存高频接口（getCacheData：cacheKey/callback/ttl/force）+JMeter 压测前后 QPS 对比（410→428~440）；OSS 托管大资源减轻服务器带宽；SSR/SEO（Next.js 服务端渲染页面源码含完整内容）。
4. **低代码平台亮点话术**（1-2、31-4）：组件数据结构设计（配置字典+排序数组分离）；编辑端/发布页复用同一套组件（pnpm workspace + share 包）；拖拽排序+键盘操作+撤销重做；localStorage 草稿与发布时间戳取舍；企业级验证码防刷；在线 Excel/压缩包导出+动态图表；一键部署。
5. **项目经验问答**（31-2）：公司介绍简洁；团队规模/开发周期/迭代方式提前备好（前端组 3 人任组长、无专职运维用云效、1-2 年迭代）；「有没有在线地址」——在校说比赛/毕设、在职说停止维护，关键是真懂；并发问题用 JMeter 数据说话；可润色不可虚构。
6. **简历写法**（31-1、31-3）：技术栈「有横有纵」、绝不写「精通」、不懂不写、学会引导面试官；按语言样式/框架多端/开发工具/服务端/运维云服务五类分组；低代码项目按名称→描述→分模块技术栈→个人职责→亮点结构；名词别写错（Next.js≠NestJS、TypeORM≠SQLAlchemy）；没学的技术如实删减。
7. **高频易错/踩坑合集**（面试可当实战谈资）：database 填库名非容器名；事务 catch 必须 rollback+抛错；relations 属性名拼错报错；MobX 必须 observer 才响应式；tar -c 与 -C；POST+JSON 忘设 Content-Type；Bearer 后有空格；share 改完必须重新打包；列表型组件展开项索引错位 bug；Tailwind base 重置富文本样式。

