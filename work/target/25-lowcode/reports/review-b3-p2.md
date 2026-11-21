# 审稿报告 · 第二期（review-b3-p2）

- 审稿范围：`work/target/25-lowcode/posts/02.第二期/` 全 26 篇（6-1~10-8）
- 审稿基准：scan3-code.md（架构与版本结论）、scan6-applied.md（已修点不重报，A9-2 涉及 component_data 字段口径）、review-eng-b.md「博客表述风险清单」（#10 编辑器恢复链路、#13 统一异常覆盖面）、scan7-materials.md（§1.1 物料名 `xdclass-lowcode.sql`/`.mwb` 唯一、§0 物料实体在外部盘）、review-b2-p1.md（5-2/5-3 同名标题改名建议，牵连 6-1）
- 源码对照：`SRC=/Users/Wang/Code/github/web-x-blog/work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`（config.ts、main.ts、common/、user/、docs/schema.sql、packages/{client,share,server}/package.json、build.config.ts、tsconfig 等逐文件核对）
- 本报告做了三项实证核验（非凭印象）：
  1. pnpm `--filter client` 能否匹配 `@lowcode/client` —— pnpm 官方文档确认"省略 scope 时任意 scope 均匹配"（`--filter=core` 会选中 `@babel/core`），8-3/8-6 写法成立；
  2. 10-6 的 `@Column() studentId` 与 `@JoinColumn({name:'studentId'})` 双声明 —— 本地装 typeorm 0.3.17 实测 buildMetadatas：两者合并为同一列，不报 Duplicate column，建表/关联查询成立，10-6 代码合格；
  3. 8-5 的 unbuild 配置键 —— 装 unbuild 2.0.0 读类型声明：顶层合法键是 `externals`（复数），`emitCJS` 只存在于 `rollup` 子对象，顶层未知键被静默忽略（DeepPartial），证实 8-5 配置两处键错。
- 视角：低代码/全栈一线专家 · 技术事实 / 代码可编译与一致性 / 六段结构与互链 / 去 AI 味 / 跨篇口径。

## 红线核查

- 26 篇未出现「RBAC 权限体系」等夸大表述，鉴权处仅讲 JWT/守卫层设计。✅
- 未把工程 A（自研参考实现）的工作流/沙箱/AI 说成课程功能。✅
- 7-3 提到「资料中提供 Navicat 的 Windows / Mac 安装包」，未触碰破解物料（scan7 §1.2 红线针对"安装和爆破包"）。✅
- 引用的课程物料名 `笔记+资料-已8期/xdclass-lowcode.sql`、`低代码平台数据库设计.mwb` 与物料清单一致（scan7 §1.1）。✅

## 逐篇结论

### 6-1 解读项目的系统架构—项目开发的重要乐章 — 合格（条件备注）

- 【P2·备注】前置知识引用《低代码项目平台需求文档—功能描述流程图+原型图》：该标题当前在 5-2/5-3 两篇同名（review-b2-p1 已建议 5-3 改名）。**改名落地后本篇引用自动消歧指向 5-2，无需改动**；若 b2 的改名建议未执行，此处引用仍有两个同名目标。本篇自身不动，待主 agent 统一处理改名即可。
- 其余：系统/架构四维度、蓝图类比专业自然；互链 6-2 真实。

### 6-2 放长线钓大鱼—规划低代码平台的系统架构 — 合格

五层拆解（访问层/网关/存储层/基础设施/外部服务）与课程技术栈完全对齐（Nginx 负载均衡、MySQL+Redis+OSS、云效/云短信/微信/JMeter/Docker）；draw.io 绘图规范（虚线分组、配色≤3）可操作。互链 6-3 真实。

### 6-3 数据舞台上的编织艺术-数据库ER图设计 — 合格

实体/属性/关系/主键四元素与 1:1、1:n、n:m 讲解正确；学生-课程 n:m、老师-课程 1:n 方向说对；「后续 TypeORM 章节会涉及关系映射」与 10-6/10-7 呼应真实。配套物料路径与清单一致。

### 6-4 实战演练—低代码平台项目数据库设计 — 需修

1. 【P1】component_data 表描述错误。原句：「字段含对应页面、用户名称、以及 `content`（即用户提交的数据）」
   → 建议：改为「字段含 `page_id`（对应页面）、`user`（访客匿名标识，服务端按 MD5(ip+ua) 生成，并非登录用户名）、`props`（用户提交的数据，simple-json 数组，形如 `[{id, value}]`）」。
   理由：SRC `docs/schema.sql` L64-70 三列为 `page_id`/`user`/`props`，无 `content` 列；scan6 A9-2 已把第四期 14-2 修正为同一口径，本篇若保留「用户名称 + content」会与后文直接矛盾，且"用户名称"与真实存值（32 位 MD5 串）不符。
2. 【P2】user 表字段名。原句：「`name`（用户名）、`phone`（手机号）、`password`、`openid`（微信扫码登录的微信索引值）」
   → 建议：`name`→`username`，`openid`→`open_id`（与 schema.sql L131-138 一致；"等"字已兜底 head_img，可不动）。
3. 【P2】组件属性字段名。原句（正文+小结两处）：「统一以 JSON 存于 `option` 字段」
   → 建议：改「`options` 字段」（schema.sql L40 列名为 `options`，text 存 JSON）。
4. 【P2】表名。原句（导语/正文/小结）：「resource」
   → 建议：改「`resources`」（实际表名复数；7-3 同，见下）。
5. 【P2】SQL 文件名自相矛盾。原句：正文「资料中提供 `xdclass-local.sql`」vs 配套资料「`笔记+资料-已8期/xdclass-lowcode.sql`」
   → 建议：正文统一为 `xdclass-lowcode.sql`（物料清单仅此名，scan7 §1.1；库名证据亦为 xdclass-lowcode）。
6. 【P2】原句：「进入编辑端时，若上次编辑过会从接口/缓存恢复」
   → 建议：改为「从草稿缓存/服务端恢复（课程设计）」并加一句限定，或删去「接口」。理由：review-eng-b 风险 #10——最终实现里 `release_with_user` 传 null 恒空，服务端恢复链路断裂，编辑器实际只靠 localStorage 草稿。

### 7-1 低代码平台云服务器选配 — 合格

配置建议（2 核 8G/2核2G、CentOS 7.8+ 64位）、重置实例密码、`ssh -o ServerAliveInterval=60` 保活均为正确可操作内容。「家人身份注册新账号享新客价」系课程原话，属厂商促销口径而非技术问题，备案不计。

### 7-2 云服务器搭建 Docker 环境和使用讲解 — 需修（轻）

1. 【P2】原句（注释行+注意框）：「`docker rmi <镜像ID>` 删除镜像（需指定镜像 ID）」「删除镜像时要指定 `image ID` 而非名称」
   → 建议：改为「删除镜像可按 ID，也可按 `镜像名:tag`（如 `docker rmi mysql:8.0`；按名删除时必须带 tag，否则默认匹配 latest）」。
   理由：`docker rmi` 同样接受仓库名，"只能 ID"是与事实不符的硬性说法，照做会误导（按名删 8.0 反而是常规操作）。
- 其余：安装顺序、systemctl/docker 常用命令、latest 语义均正确。

### 7-3 阿里云 Linux 服务器容器化安装 Mysql — 需修（轻）

1. 【P2】五张表名。原句：「五张核心表（user / page / component / component_data / resource）」→ `resource` 改 `resources`（同 6-4 条目 4）。
2. 【P2】SQL 文件名。原句：「导入课程提供的 `xdclass-local.sql` 文件」vs 本篇配套资料「`笔记+资料-已8期/xdclass-lowcode.sql`」→ 统一为 `xdclass-lowcode.sql`。
3. 【P2·建议】安全组开放 3306 一段建议补一句：「安全组来源建议只放行自己常用 IP（0.0.0.0/0 + root 密码直连公网属高危默认，生产应走内网/跳板）」。课程操作可保留，一句话提示成本低、价值高。

### 7-4 阿里云 Linux 服务器容器化安装 Redis — 合格

`docker run redis redis-server --requirepass ...` 参数顺序正确；auth 流程、QuickRedis TTL -1/-2 语义（TTL 命令返回值）均准确。

### 8-1 深度解析 pnpm-workspace 的灵动工作空间管理 — 需修（轻）

1. 【P2】原句：「所有子项目都放在 `packages/` 下，各自拥有自己的 `package.json` 与锁定文件」
   → 建议：改为「……各自拥有自己的 `package.json`；整个 workspace 只在根目录维护一份 `pnpm-lock.yaml` 锁定文件」。
   理由：pnpm（无论独立项目还是 workspace）只有根级唯一 lockfile，子项目不存在"锁定文件"，照文找文件会落空，也削弱了"统一版本"的说服力。
- 其余：四子项目职责、`packages: ["packages/*"]`、优势清单与最终工程一致。

### 8-2 项目管理 pnpm-workspace 初始化项目 — 合格

根 package.json（scripts/devDependencies/dependencies）与最终仓库逐字段一致（含 `run:*`/`build:*`/`start:*` 与 `--filter` 写法）；`-D -w`、`@types/node` 版本对齐 Node 大版本的提醒正确。

### 8-3 前端子项目 React 创建和项目配置 — 合格

- `pnpm --filter client` 匹配 `@lowcode/client`：已按 pnpm 文档实证（省略 scope 即匹配任意 scope），与最终仓库根 scripts 组合成立。
- client/package.json 节选与最终仓库 devDependencies 一致；`build: "tsc && vite build"` 是 create-vite 模板原样（最终仓库后来改为 `vite build`），属创建期快照，保留合理（备案不计）。
- tsconfig 为 Vite react-ts 模板标准内容，编译目标/strict/jsx 均正确。

### 8-4 后端子项目 Nest 创建和项目配置 — 合格

`nest new` 自带 node_modules 后统一重装的流程真实；删 `@types/node`/`typescript` 与最终 server package.json（已无这两项）吻合；getHello/端口 3000 正确；`rm -rf .git` 清理子项目 Git 的操作可行。

### 8-5 公共组件+类型子项目 share 创建和项目配置 — 需修

1. 【P1】build.config.ts 两处键名错误。原句：
   ```ts
   declaration: true,
   emitCJS: true,
   external: ['react', 'react-dom', 'antd', '@ant-design/icons'],
   ```
   → 建议：改为（与 SRC `packages/share/build.config.ts` 及 unbuild 2.0 API 一致）：
   ```ts
   declaration: true,
   rollup: { emitCJS: true },
   externals: ['react', 'react-dom', 'antd', '@ant-design/icons'],
   ```
   理由（已实测 unbuild 2.0.0 类型声明）：`emitCJS` 只在 `rollup` 子对象中存在（顶层键被静默忽略）→ 按文中配置打包**不会产出 index.cjs**，与本篇"dist 下生成 index.cjs/index.mjs/index.d.ts"及 package.json 的 `require/main: ./dist/index.cjs` 直接矛盾；顶层合法键是 `externals`（复数），`external` 会被忽略导致 react/antd 不被排除。正文要点第二条「`emitCJS: true`：借助 Rollup 同时输出 CommonJS」措辞可保留，但配置位置必须修正。
2. 【P2】tsconfig.json 与最终仓库 `share/tsconfig.json` 三处出入：`jsx: "react-jsx"` vs `"react"`、`skipLibCheck: true` vs `false`、`include: ["src"]` vs `["src", "build.config.ts"]`。两种写法都能编译，按创建期快照保留亦可；若求与源码一致建议校正（或统一加注「以最终仓库为准」）。
- 其余：unbuild 选型说明、`pnpm build:share`、三产物描述与真实产物结构一致。

### 8-6 前端 client 项目使用公共项目 share 变量 — 需修

1. 【P1】启动命令与根 scripts 不符。原句：「启动开发服务：`pnpm run client`」
   → 建议：改 `pnpm run:client`。
   理由：8-2/8-3 已确立根脚本名为 `run:client`（且 8-3 用法正确）；根 package.json 无 `client` 脚本，`pnpm run client` 直接报 Missing script，读者照抄即卡住。9-4 两处同改（见 9-4 条目 2）。
2. 【P2】示例变量名与 8-5 不一致。原句：「`import { sharedText } from '@lowcode/share';`」
   → 建议：8-5 导出的是 `export const xd = '小滴课堂'`，两篇需统一——要么 8-5 改导出 `sharedText`（9-4 也用了此名，改动最小），要么本篇与 9-4 改用 `xd`。
3. 【P2】原句：「默认 `http://localhost:5174`」→ Vite 默认端口是 5173（5174 仅在 5173 被占用时顺延）。改为「默认 `http://localhost:5173`，若被占用会顺延，以终端打印为准」（9-4 同）。
- 其余：`pnpm --filter client add @lowcode/share` 生成 `workspace:^` 与最终 client/server package.json 一致；`--filter` 说明正确。

### 9-1 低代码平台项目代码管理—云效 Codeup — 需修（轻）

1. 【P2】清理 Git 的叙述与命令脱节。原句：「根目录此前未初始化 Git，且各子目录遗留的 `.git` 需先清理，改为在根目录统一托管：`rm -rf .git` / `git init`」
   → 建议：命令改为 `rm -rf packages/*/.git`（子目录的 .git 才是要清的对象），并补一句「8-4 已删过 client/server 的 .git，此处重复执行是兜底」；或直接删掉 `rm -rf .git` 行，只保留 `git init`。
   理由：按现文，`rm -rf .git` 在根目录执行清的是根 .git（根目录恰恰没有），与叙述"清子目录"不符。

### 9-2 低代码平台项目后端 Nest 项目配置—TypeORM — 需修（轻）

1. 【P2】数据库名/容器名与 7-3 冲突。原句：「`database` 填数据库名 `study_class_local`，不要和容器名 `study_class_mysql` 混淆」
   → 建议：统一为 7-3 建立的命名 `xdclass_local` / `xdclass-mysql`；若保留课程原例，请加一句「库名与容器名以你实际创建的为准（7-3 中为 `xdclass_local` / `xdclass-mysql`）」。
   理由：7-3 读者刚按 `xdclass_local`（容器 `xdclass-mysql`）建完库，本篇突然换成另一套名字且无交接说明，照做必连不上。10-2 同源问题见该篇条目（已自注"独立练习工程"，处理可更轻）。
- 其余：三依赖、`entities: ['dist/**/*.entity{.ts,.js}']`（与最终 config.ts 逐字一致）、synchronize 双刃说明、forFeature 注入 Repository、`nest g resource user` 均正确；"暂定义 id/name/phone/password"属阶段快照（最终实体为 username/head_img/phone/password/open_id），可保留。

### 9-3 低代码平台项目后端 Nest 项目配置—接口响应+异常拦截器+DTO — 需修

1. 【P1】异常响应结构与真实代码不符。原句（JSON 块+小结）：
   ```json
   { "code": -1, "data": "错误提示信息" }
   ```
   → 建议：改为 `{ "code": -1, "data": null, "msg": "错误提示信息" }`，并把「接口外层的 `code` 与 `data` 形态都一致」相应改为「`code`/`data`/`msg` 形态一致」。
   理由：SRC `src/common/AbnormalFilter.ts` 输出 `{ code: -1, data: null, msg: message }`——错误信息在 `msg` 不在 `data`；全系列后文（第三期起、docs/API.md）均按 `{code,data,msg}` 三元契约叙述，本篇两字段版会造成前后口径分裂。
2. 【P2】文件/类名与最终仓库不一致。原句：「异常拦截器 `http-exception.filter.ts`」「`new HttpExceptionFilter()`」「`new ResponseInterceptor()`」
   → 建议：改为最终名 `src/common/AbnormalFilter.ts` / `AbnormalFilter` / `ResponseIntercept`（或注明「课程阶段命名为 http-exception.filter.ts，最终仓库为 AbnormalFilter.ts」），便于读者在源码中定位。
3. 【P2】覆盖面口径过强。原句：「异常拦截器……把**运行时报错**统一收敛为……」
   → 建议：加限定「捕获 HTTP 异常（`@Catch(HttpException)`）统一收敛为 -1 结构；非 HTTP 异常（如驱动层报错）不经过此过滤器，走 Nest 默认 500」。
   理由：review-eng-b 风险 #13——AbnormalFilter 仅 `@Catch(HttpException)`，未捕获异常穿透默认 500，契约只覆盖 HTTP 异常路径。
4. 【P2】验证话术与实际输出不符。原句：「拦截器提示『id 必须为 number 类型且不能为空』」
   → 建议：示例 DTO 未自定义 message，class-validator 默认输出英文（如 "id must be an integer number" / "id should not be empty"）。给 DTO 加自定义 message，或把验证效果改写为「返回 class-validator 的校验错误（默认英文，message 在 `msg` 字段）」。
- 其余：`{code:0, data}` 成功结构、全局注册方式、`ValidationPipe` + `@IsInt` 用法与 main.ts 真实代码一致。

### 9-4 低代码平台项目前端 React 项目配置—Ant-design+TailwindCSS — 需修

1. 【P1】Tailwind/PostCSS 配置在 ESM 包中用 CJS 导出，会启动报错。原句（两段 js 代码块）：`module.exports = {...}`
   → 建议：改为 `export default { ... }`（与 SRC `packages/client/tailwind.config.js`、`postcss.config.js` 一致）。
   理由：client 是 `"type": "module"`（8-3 已展示该字段），`.js` 文件按 ESM 解析，`module.exports` 会抛 "module is not defined in ES module scope"；最终仓库两文件均为 `export default`，是可运行的证明。读者照抄本篇配置后 Vite 起不来。
2. 【P2】`pnpm run client`（两处）→ `pnpm run:client`，同 8-6 条目 1。
3. 【P2】`localhost:5174` → 5173，同 8-6 条目 3。
4. 【P2·可选】tailwind `content` 为 `['./index.html', './src/**/*.{ts,tsx}']`，最终仓库为 `./src/**/*.{js,ts,jsx,tsx}`——项目当前 TS-only 可用，按最终仓库补全更稳。
- 其余：`pnpm --filter client add antd`、三段 @tailwind 指令、`text-red-500`/`text-8xl` 验证流程、antd 版本（^5.11.2 与最终依赖一致）均正确。

### 10-1 探索 Node 世界中的数据建模—ORM 框架 — 需修（轻）

1. 【P2】原句（Prisma 注意点）：「缺失多库联合查询，支持的数据库较少（如 Oracle、SQL Server）」
   → 建议：删去「SQL Server」或改为「Oracle 等数据库尚不支持（SQL Server 2022 年起已 GA）」。
   理由：2023 年（课程时点）Prisma 官方已支持 PostgreSQL/MySQL/SQLite/SQL Server/MongoDB/CockroachDB，不含的是 Oracle；把 SQL Server 列为"不支持"会被内行挑刺。"缺失多库联合查询"的说法成立，保留。
- 其余：ORM 本质、TypeORM/Prisma/Sequelize 三方对比框架、选 TypeORM 的理由（Nest+TS 集成）公允；star 数量级与课程时期相符。

### 10-2 TypeORM 框架-轻松掌握链接 Mysql 数据库配置 — 需修（轻）

1. 【P2】`database: 'study_class_local'`、容器名 `study_class_mysql` 与 7-3 的 `xdclass_local`/`xdclass-mysql` 不一致。本篇已自注「本项目代码为独立练习工程，非低代码正式工程」，可保留练习命名，但建议在 `database` 说明后补一句「若跟着 7-3 建库，库名填你的实际库名（如 `xdclass_local`）」，避免跨篇连不上。
- 其余：三件套、forRoot、`synchronize` 线上关闭提醒、验证方式（应用启动即代表连接成功）正确。

### 10-3 TypeORM 框架—配置实体和自动同步数据库 — 合格

实体装饰器三件套、forFeature 注册、synchronize 自动同步、练习占用 user 表的声明（与 10-2 口径一致）均正确；`nest g resource user` 描述贴近 CLI 实际交互。

### 10-4 TypeORM 框架—实现数据库增+查操作 — 合格

`save` 插入、`find` 单条件/AND（对象）/OR（数组）三种写法均为 TypeORM 0.3 正确语法；`@Get('test')` 兼做插入属练习工程演示，可接受；原生 SQL 对照准确。

### 10-5 TypeORM 框架—实现数据库改+删操作 — 需修

1. 【P1】字段名 `form` 系语音转写讹误，应为 `phone`。涉及：正文「只有 `form` 不同」「只有 `form` 为 `111` 的那条」「（如同时带 `name` 与 `form`）」及两处代码 `update({ name:'老六', form:'111' }, …)`、`delete({ name:'老六', form:'111' })`。
   → 建议：全文 `form`→`phone`（代码 2 处、正文 3 处、小结 1 处）。
   理由：10-3/10-4 实体只有 id/name/phone/password，无 `form` 列——条件对象按列名匹配，未知列会让 update/delete 落空甚至报错；原始转写稿本身 form/phone 混写（"而且 phone 呢是三个一的"），`form` 是 ASR 把 phone 听岔的产物。这是本篇唯一但致命的可复现性问题。
2. 【P1】标题与互链断链。front-matter title 与 h1 为《TypeORM 框架：实现数据库改 + 删操作》，而文件名及三处入链（10-4 下一步、10-6 前置知识、10-8 前置知识）均为《TypeORM 框架—实现数据库改+删操作》。
   → 建议：title/h1 改回与文件名一致的「TypeORM 框架—实现数据库改+删操作」（改一处即修复 3 条入链）。
- 其余：update(条件,新字段)/delete(条件) 参数语义、affected 读法、"条件宽窄决定误伤面"的强调专业且实用；依赖/lock 快照与配套代码路径（`代码（已8期）/代码（已8期）/10-5/`）格式与 scan7 清单一致。

### 10-6 TypeORM 框架—一对一关系表关联和查询 — 合格

- `@Column() studentId` 与 `@JoinColumn({name:'studentId'})` 双声明已用 typeorm 0.3.17 实测：元数据合并为同一列（不产生 Duplicate column），建表与关联查询成立。
- `@OneToOne` 回调、`relations: { studentDetail: true }` 对象语法、「relations 写属性名而非列名」「自动同步只建结构、关联值要手动补」均为准确的一线经验；互链 10-7 真实（下一步里《TypeORM 框架-Mysql事务介绍和使用》的断链计入 10-8 条目 1）。

### 10-7 TypeORM 框架—一对多关系表关联和查询 — 合格

`@OneToMany`/`@ManyToOne` 成对且回调互指写法正确；`Classes` 避开 `class` 关键字的提醒实用；`relations: ['classes']`/`['studentList']` 数组语法在 0.3 仍支持；两个坑（外键没填→null、属性名拼错→报错）是真实踩坑路径；与 6-4 的业务关系呼应自然。

### 10-8 TypeORM 框架-Mysql事务介绍和使用 — 需修（轻）

1. 【P1】标题与互链断链。front-matter title 与 h1 为《TypeORM 框架：MySQL 事务介绍和使用》，而文件名及三处入链（10-5/10-6/10-7）均为《TypeORM 框架-Mysql事务介绍和使用》。
   → 建议：二选一——title/h1 改回「TypeORM 框架-Mysql事务介绍和使用」（改一处修 3 链，推荐），或保持现标题并同步修改三处入链。
2. 【P2】前置知识《Nest通过TypeORM链接Mysql数据库》→ 预先课实际标题为《NestJS 通过 TypeORM 连接 MySQL 数据库》。
3. 【P2】下一步两篇篇名不准：《低代码项目后端接口开发—加密+Redis 模块配置》→ 实际《低代码后端接口开发：加密工具与 Redis 动态模块配置》；《低代码项目后端接口开发—图形验证码接口》→ 实际《低代码项目后端接口开发：图形验证码接口》。
4. 【P2】原句：「TypeORM 0.3.x 起，DataSource 取代了旧的 Connection，getConnection() **因此不再可用**」
   → 建议：改「已弃用（0.3 起标记 deprecated、调用会警告），新项目一律用 DataSource；后续大版本将移除」。0.3.x 中 getConnection 仍在、可调用，"不再可用"过强。
- 其余：DataSource 构造注入、createQueryRunner→connect→startTransaction→commit/rollback→release 五步流程与"事务内必须走 queryRunner.manager"的要点均为 0.3 正确范式；转账红包原子性讲解通俗准确。

## 共性观察（去 AI 味）

- 26 篇六段结构（front-matter / 导语 / 前置知识 / 正文 / 小结 / 下一步）100% 齐全；导语均为两三句内容概述，无空洞宣言。
- AI 痕迹整体很低：无 emoji、无「总之/综上」、无排比堆砌；口语细节保留好（「老王想追冰冰发红包」「千万别用本地虚拟机」「别和容器名混淆」）；破折号仅 10-4~10-8 每篇 1~3 处，属正常中文标点不构成机器腔。6-4 的「**1. 用户表 user**」等整行加粗是五表清单编号头，非机械加粗。
- 10-5~10-8 四篇明显比 6-x~9-x 成稿质量更高（每篇有"两个真实的坑/三处配置各管什么"式复盘段落），是本期的标杆写法。
- 每篇"下一步"均指向下一篇；跨期引用（6-1→第一期、10-7/10-8→第三期 11-1）除 10-8 两处篇名误差外全部真实。

## 跨篇口径一致性（抽核）

| 口径 | 第二期表述 | 对照 | 结论 |
|---|---|---|---|
| 根 package.json scripts | 8-2 逐字段 | 最终仓库 | ✅ 一致 |
| client/share/server 包名与 workspace:^ | 8-3/8-5/8-6 | 最终仓库 | ✅ 一致 |
| entities glob | 9-2/10-2 | SRC config.ts | ✅ 逐字一致 |
| 五张表名/字段 | 6-4/7-3 | docs/schema.sql + scan6 A9-2 | ❌ resource(s)/option(s)/content(props)/name(username) 四组不一致 → 已列 P1/P2 |
| DB/容器命名链 7-3→9-2/10-2 | xdclass_* vs study_class_* | 7-3 | ❌ 缺交接说明 → P2 |
| share 导出变量 | 8-5 `xd` vs 8-6/9-4 `sharedText` | — | ❌ P2 |
| 10-x「独立练习工程」声明 | 10-2 自注，10-5/10-7/10-8 沿用 | — | ✅ 口径一致 |
| 第三期篇名引用 | 10-7（对）/10-8（两处错） | 03.第三期实际标题 | ⚠️ P2 |

## 统计

- 合格：12 篇 —— 6-1（条件备注）、6-2、6-3、7-1、7-4、8-2、8-3、8-4、10-3、10-4、10-6、10-7
- 需修：14 篇 —— 6-4、7-2、7-3、8-1、8-5、8-6、9-1、9-2、9-3、9-4、10-1、10-2、10-5、10-8
- 问题计数：**P1 × 8**（6-4 component_data 字段/语义；8-5 build.config 两键错误；8-6 `pnpm run client`（牵连 9-4 两处）；9-3 异常响应结构；9-4 Tailwind/PostCSS CJS-in-ESM；10-5 `form`→`phone`；10-5 标题断链×3 入链；10-8 标题断链×3 入链）；**P2 × 26**（6-4×5、7-2×1、7-3×3、8-1×1、8-5×1、8-6×2、9-1×1、9-2×1、9-3×3、9-4×3、10-1×1、10-2×1、10-8×3）。
- 修正量估计：P1 全部为单点改写（每处 ≤10 行；两条标题断链各只改 fm title+h1 一行）；P2 为措辞/字段名/篇名级微调。合计一次编辑会话可完成。
- 涉及基准报告的既定结论引用：review-eng-b 风险 #10（6-4 恢复链路口径）、#13（9-3 异常覆盖面）；scan6 A9-2（6-4 component_data 口径）；scan7 §1.1（6-4/7-3 物料名）；review-b2-p1 5-2/5-3 改名牵连（6-1 备注）。
