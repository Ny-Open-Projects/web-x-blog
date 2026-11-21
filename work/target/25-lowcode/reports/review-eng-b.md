# 深度工程审计 B：lowcode-platform-full（课程原版工程）

> 审计对象（只读）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`
> 前置阅读：`reports/scan3-code.md`（架构结论，本文不重复）
> 本文路径均相对工程根（下称 `PROJ`）。所有行号取自当前工作区文件实际内容。
> 审计方法：逐文件通读 server 全部 38 个源文件 + client 核心 20 文件 + release/share 渲染链 + 全部部署文件，对照 docs/API.md 与 docs/schema.sql 交叉验证。

---

## 分级总览

- **P0（安全/正确性硬伤）9 条**：裸 MD5 密码、短信验证码可爆破、防刷身份在反代后失真、资源 OSS 删除越权（IDOR）、发布接口 mass assignment、富文本 SSR 绕过消毒（XSS）、`release_with_user` 编辑器恢复链路断裂、微信回调无签名校验且 XML 解析不通、上传类型校验可伪造。
- **P1（质量）20 条**：CORS 全开无 Helmet 无限流、吞异常、N+1、零索引 schema、一用户一页覆盖、问卷数据孤儿化、编辑器性能与内存泄漏、JWT 无吊销等。
- **P2（建议）17 条**：DTO 校验形同虚设、C 端参数校验、next 错误页、日志残留等。

---

## P0 —— 安全 / 正确性硬伤

### P0-1 密码哈希是无盐裸 MD5（无 KDF、无盐、无强度校验）

- 证据：
  - `packages/server/src/utils/SecretTool.ts:6-9`：`createHash('md5').update(data).digest('hex')`，无盐、无迭代。
  - `packages/server/src/user/user.service.ts:118`（注册存库）、`:148`（登录比对 `foundUser.password === this.secretTool.getSecret(password)`）。
  - `packages/server/src/user/entities/user.entity.ts:17-18`：password 无任何哈希格式约束。
  - `docs/API.md`（用户模块表格）亦自述"双密码+MD5"。
- 危害：MD5 已被证实可秒级碰撞、GPU 每秒百亿级暴力；无盐意味着彩虹表直接命中。且登录失败**无任何尝试次数限制**（user.service.ts:141-155），接口级爆破零成本。
- 修复：bcrypt/argon2id（cost≥10）+ 密码强度校验（@MinLength(8) 等）+ 登录失败限流/锁定。

### P0-2 短信验证码可在线爆破：4 位码 + Math.random + 失败不失效 + 无尝试上限

- 证据：
  - `packages/server/src/utils/RandomTool.ts:6-8`：`Math.floor(Math.random() * (9999 - 1000)) + 1000` —— **4 位数（仅 9000 种），且 Math.random 非加密安全**。
  - `packages/server/src/user/user.service.ts:73-74`：码存 Redis TTL 60s。
  - `packages/server/src/user/user.service.ts:166-173`：`phoneLogin` 比对失败**不删除码、无尝试计数** → 60s 窗口内可无限制重试。9000 种组合在几十 QPS 下 60s 内大概率命中。
  - 成功登录后同样不删码（175-178）→ 码在 TTL 内可重放。
  - 注册侧同构问题：`user.service.ts:98-106`。
- 修复：6 位码 + `crypto.randomInt`；登录/注册校验失败即删码或加 attempt 计数（≥5 次作废）；成功即删；全局限流。

### P0-3 "MD5(ip+ua) 防刷/防重"在反代部署下身份失真：既误伤真用户、又挡不住攻击者

- 证据：
  - `packages/server/src/utils/GetUserMessTool.ts:11-17`：`request.ip.match(/\d+\.\d+\.\d+\.\d+)/`。
  - `packages/server/src/main.ts:8-17`：**未设置 `app.set('trust proxy', ...)`** → 生产流量经 nginx（docker-compose 的 backend_nginx）转发后，`request.ip` 恒为网关容器 IP。
  - `packages/server/src/user/user.controller.ts:31,46` 与 `packages/server/src/low-code/low-code.controller.ts:51,65`：所有防刷 key = `MD5(ip+ua)`。
  - 后果 A（误伤）：所有访客 ip 相同 → 同 UA（浏览器版本趋同，极常见）用户共享同一身份 → 第一个人提交问卷后，`is_question_data_posted`/`postQuestionData` 判定"已提交"（low-code.service.ts:192-198, 203-213），其他真用户全被挡。
  - 后果 B（绕过）：攻击者轮换 `User-Agent` 字符串即可生成全新身份 → 无限刷问卷写库（props 无校验无大小限制，见 P1-13）。
  - 后果 C：IPv6 场景 `match()` 返回 null → key 退化为 `MD5("undefined"+ua)`，进一步塌缩。
- 修复：启用 trust proxy + nginx 传 `$proxy_add_x_forwarded_for`（现配置用 `$remote_addr` 覆盖 XFF，见 P1-25）；防重改服务端签发的一次性提交凭证或登录态+存储去重。

### P0-4 资源删除越权（IDOR）：先删 OSS 文件、后做归属校验

- 证据：`packages/server/src/resources/resources.service.ts:44-53`：
  ```ts
  const resources = await this.resourcesRespository.findOneBy({ id }); // ← 无 account_id
  if (!resources) throw ...
  await this.alioss.deleteFromAliOss(resources.url);                   // ← 先删 OSS
  await this.resourcesRespository.delete({ id, account_id });          // ← 归属校验在最后、且只影响 DB 行
  ```
- 危害：任何登录用户枚举 `DELETE /api/resources?id=1..n` 即可删除**他人资源的 OSS 对象**（DB 行保留但文件已没了）→ 其他用户页面图片/视频批量挂掉；id 自增可枚举。
- 修复：查单即带 `account_id`，未命中按 404 处理；确认归属后再删 OSS。

### P0-5 发布接口 mass assignment：客户端字段直通 UPDATE，可改 id/account_id

- 证据：
  - `packages/server/src/main.ts:15`：`new ValidationPipe()` 无 `whitelist/transform`。
  - `packages/share/src/types/request/low-code.ts:3-6`：`PostReleaseRequest` 是纯 TS 类型，**无 class-validator 装饰器** → 零运行时校验。
  - `packages/server/src/low-code/low-code.service.ts:59-62`：更新分支 `update(Page, findLowCode.id, { ...otherBody, components: [] })` —— `otherBody` 是 body 除 components 外的**全量展开**。客户端传 `{"id": 42}` 或 `{"account_id": 999}` 会直接进入 UPDATE，可**改主键/转移页面归属**。
  - `low-code.service.ts:78-82`：创建分支 `{ ...otherBody, account_id: user.id, components: [] }`，account_id 被覆盖但 `id` 仍可注入（插入指定主键）。
  - 组件插入同样展开：`low-code.service.ts:42-46` `{ ...component, page_id, account_id }`，`component.id` 可控。
- 修复：请求 DTO class 化 + ValidationPipe({transform:true, whitelist:true, forbidNonWhitelisted:true})；更新/插入用显式字段列表。

### P0-6 C 端富文本 SSR 渲染跳过 DOMPurify：首屏 HTML 带未消毒 HTML（存储型 XSS）

- 证据：`packages/share/src/components/LowCodeRichText/RichTextComponent.tsx:12-13`：
  ```ts
  function sanitizeHtml(html: string): string {
    if (typeof window === "undefined") return html;  // ← SSR 时原文返回
    return DOMPurify.sanitize(html, {...});
  }
  ...
  <div dangerouslySetInnerHTML={{ __html: sanitizeHtml(props.content) }} />  // :40
  ```
  - options 内容来源：任意注册用户在编辑器随意写入并发布（`react-quill` HTML → `options.content` → DB `component.options` → C 端 `GET /low_code/release?id=` 原样下发）。
  - Next.js SSR（`packages/release/src/app/[id]/page.tsx` → `ComponentRender.tsx:24` 直接渲染 props）时 `window === undefined` → **服务端输出的 HTML 未消毒**，`<script>`/`<img onerror=...>` 在浏览器解析首屏时即执行，客户端 hydration 后的净化救不回来。
  - 注释里的理由"内容来自自家受控编辑器"不成立：平台是多用户的，任何一个低权限用户的页面都会被公众访问。
- 修复：用 `isomorphic-dompurify`（jsdom 后端）或把净化前移到发布落库时；SSR 分支同样消毒。

### P0-7 `release_with_user` 恒为空：编辑器"从服务端恢复"链路断裂（与 API 文档矛盾）

- 证据：
  - `packages/server/src/low-code/low-code.controller.ts:27-30`：`getReleaseData(null, user)` —— **id 传了 null**。
  - `low-code.service.ts:165-168`：`findOneBy({ id: null, account_id: user.id })` → TypeORM 0.3 中 null 生成 `id IS NULL` → 永不命中 → 返回 undefined。
  - 客户端后果：`packages/client/src/hooks/useStoreComponents.ts:277-296` `readDataFromServer()`：`data?.components?...` 短路为 undefined → `Object.keys(storeComponents.compConfigs)`（:296）对 undefined 抛 TypeError → 编辑器崩溃；`:303` `updatePage({ tdk: data.tdk ... })` 亦未判空。
  - `docs/API.md` #11 写的是"编辑器进入:按用户取组件配置"——实现与文档矛盾。
- 结论：编辑器实际只能靠 localStorage 草稿（`storeInLocalStorage`）活着，"服务器恢复"分支不可用。
- 修复：service 加 `getLatestByUser(user)`（按 account_id findOne）；客户端补判空。

### P0-8 微信回调：无签名校验 + XML 解析按现状根本不通

- 证据：
  - `packages/server/src/wechat-login/wechat-login.controller.ts:26-29`：`POST /wechat_login/callback` 为 `@Public()`，`wechatMessage(@Body() body)` 不校验微信 signature/timestamp/nonce（GET 接入验证有 SHA1 校验，POST 消息回调没有，`wechat-login.service.ts:49-118` 全程未验证）。
  - 伪造后果链：`wechat-login.service.ts:79-88` 未知 open_id 自动建号（刷库）；`:94-97` 把 `{isScan:'yes', token}` 写进 Redis `wechat:ticket:<ticket>`；攻击者拿自己 `GET /wechat_login/login` 获得的 ticket 伪造消息即可完成"扫码"闭环；若能得知他人 open_id 可签发他人 token（登录态伪造面）。
  - 解析问题：`wechat-login.service.ts:55-62` 注释自认"正式版本"（`getXMLStr` 读原始流，`WechatDataTool.ts:6-20`）被注释，改用 `Object.keys(body)[0]`；但 Nest 默认只装 json/urlencoded body parser（`main.ts` 无 rawBody/自定义 parser），微信真实回调 `Content-Type: text/xml` → body 为空/undefined → `parseString(undefined)` reject → 500。即真实微信回调**按当前代码是断的**，仅特定 JSON 请求形态才走得通。
- 修复：启用 rawBody（`NestFactory.create(AppModule, {rawBody:true})`）+ `text/xml` 专用 parser；回调按微信文档校验 query 上的 signature。

### P0-9 上传校验只看可伪造的 mimetype，无扩展名/魔数白名单 → CDN 域存储型 XSS

- 证据：
  - `packages/server/src/resources/resources.controller.ts:19-21`：`ALLOWED_MIME = /^(image|video)\//`，校验对象是 `file.mimetype`（客户端 multipart 里自己声明，可伪造）。
  - `packages/server/src/utils/modules/ali-oss.module.ts:44-50`：OSS 对象 key 直接沿用原始文件名扩展名（`name.split('.').pop()`）→ 传 `evil.html`（声明 image/png）或 `.svg`（`image/svg+xml` 天然命中 image/）→ 对象以 `text/html`/`image/svg+xml` 在 OSS/CDN 域可访问 → 存储型 XSS（SVG 内嵌 script）。
  - 放大面：token 存 localStorage（`packages/client/src/store/auth.ts:6,14`），若 OSS 自定义域名与主站同站，XSS 可直接偷 token。
  - 大小限制 200MB（controller:19）本身合理，但 nginx 未配 `client_max_body_size`（默认 1MB）→ 生产上传必 413（见 P1-25），该校验实际从未在部署链路生效。
- 修复：扩展名白名单（png/jpg/webp/mp4…）+ 魔数嗅探 + SVG 一律拒绝或净化 + OSS 强制 `Content-Disposition: attachment`（或独立无 Cookie 的 CDN 域）。

---

## P1 —— 质量问题

### P1-1 CORS 全开、无 Helmet、无任何速率限制

- `packages/server/src/main.ts:10`：`app.enableCors()` 无 options → `Access-Control-Allow-Origin: *`。
- `packages/server/package.json` 无 helmet、无 @nestjs/throttler 依赖；nginx conf 无 `limit_req`。
- 结合 P0-1/P0-2：密码登录与短信码爆破完全敞开。修复：CORS 白名单 + helmet + 全局/接口级 throttler + nginx limit_req（登录、send_code、question_data 单独限）。

### P1-2 错误被吞：前端拦截器不 rethrow、服务端 catch 后 return error

- `packages/client/src/utils/request.ts:27-33`：响应错误分支只弹 toast、**不 return Promise.reject** → await 方拿到 undefined 继续执行，调用方无法感知失败。
- `packages/server/src/resources/resources.service.ts:27-29`：上传失败 `catch (error) { return error }` → 原始错误对象经 ResponseIntercept 以 `{code:0}` **成功态**返回，前端还提示"上传成功"。
- 修复：前端 rethrow；服务端 `throw new InternalServerErrorException(...)`。

### P1-3 统一响应契约只覆盖 HttpException，未捕获异常直接穿透

- `packages/server/src/common/AbnormalFilter.ts:5-6`：`@Catch(HttpException)` → TypeORM 错误、xml2js reject、JSON.parse 失败等走 Nest 默认 500（`{statusCode,message}`），`{code,data,msg}` 契约破裂。
- `AbnormalFilter.ts:15`：`getResponse()` 为字符串时 `message` 为 undefined → `msg` 字段丢失；类校验失败时 msg 是数组，客户端按字符串处理（request.ts:30）。
- 修复：改 `@Catch()` 全捕 + 兜底 500 + Logger 记录原始异常（当前过滤器不打任何日志）。

### P1-4 统计链路 N+1 + 全量无分页

- `packages/server/src/low-code/low-code.service.ts:239-253`：`getQuestionData` 对每条问卷×每个 prop 逐个 `findOneBy`（提交 1000 条×10 题 = 10000 次查询）；`:272-293` `getQuestionDataByIdRequest` 同构。
- `ComponentDataRepository.findBy({page_id})` 无分页/无 limit，提交量大即拖垮接口。
- 说明：scan3 提到的 N+1 修复只覆盖 `getReleaseData`（:174-180 In 批量），统计链路未修。修复：组件表一次 In 预取后内存 join；问卷按页分页。

### P1-5 schema 零索引 + 注册查重竞态（可重复注册同手机号）

- `docs/schema.sql`：五张表仅 PRIMARY KEY，无任何二级索引/唯一约束/FK —— `user.phone` 不唯一、`component(page_id,account_id)`、`component_data(page_id,user)`、`resources(account_id)` 全表扫描。
- `packages/server/src/user/user.service.ts:94-95`：`findOneBy({phone})` 查重后 `save`，check-then-insert 无唯一索引兜底 → 并发注册同一手机号可产生重复账号（后续登录 findOneBy 行为不定）。
- 修复：phone 加 UNIQUE；component_data 加 `(page_id, user)` 唯一 + 应用层捕获冲突。

### P1-6 一用户一页面模型：第二页静默覆盖 + 并发发布无锁

- `packages/server/src/low-code/low-code.service.ts:94-101`：`findBy(Page, {account_id})` 取回全部后只处理 `findLowCode[0]` —— 用户发布第二个页面时,旧页面被原地改写,且模型上无处安放第 2 页（API 语义未定义,文档也未提）。
- 同函数事务内 SELECT（:94）未加 `FOR UPDATE` → 并发重复发布会出现两条事务同时"删旧插新",轻则报错回滚、重则死锁/组件行错乱。
- 修复：明确"单页"约束（唯一索引 account_id）或改多页模型；SELECT ... FOR UPDATE。

### P1-7 发布后组件 id 全部重生成 → "保留问卷数据"名存实亡（孤儿数据）

- 证据链：
  - 前端发布丢弃组件 id：`packages/client/src/pages/Editor/Header/Center.tsx:47-52`（只传 `{type, options}`）。
  - 服务端删除旧组件行、插入新行（新自增 id）：`low-code.service.ts:64-74`。
  - 问卷答案存的正是组件 id：`component_data.props` 的 `item.id`（low-code.service.ts:243-250 按它找组件）。
  - `low-code.service.ts:68-71` 注释声称"保留 component_data…统计端已对失效组件 id 做容错" —— 容错=查不到组件时 `type: undefined, options: {}`（:249, :289）→ **行在,但历史答案在统计页里变成无名无选项的孤儿**,统计价值归零。
- 结论：该"生产化修正"只是半闭环。修复：发布时按 (index+type) 或客户端传稳定 uuid 映射旧 id；或显式提供"清空统计"能力并按此更新文档。

### P1-8 编辑器性能：整画布 observer + 每次渲染 toJS 深拷贝 + undo 全量快照

- `packages/client/src/pages/Editor/EditorCanvas.tsx:264`：observer 粒度是整个画布;`:31` `generateComponent` 每次渲染对每个组件 `{...toJS(conf.props)}` 深拷贝 → 任一属性修改触发全部组件重渲染+全量深拷贝（大 schema 页面卡顿的直接来源）。
- `packages/client/src/hooks/useStoreComponents.ts:16-22`：`trackUndo(() => toJS(storeComponents), ...)` 每次变更对**整个 store**深拷贝入 undo 栈 → O(组件数) 内存/步。
- 组件项未用 React.memo（SortableItem/ComponentWrapper 均普通 FC）。
- 修复：按组件粒度 observer + memo;undo 只存变更路径（jsondiffpatch/zundo 类）。

### P1-9 内存泄漏实例（事件/定时器）

- `packages/client/src/hooks/useSendCode.tsx:64-77`：倒计时 `setInterval` 在组件卸载时**不清除**（无 return cleanup）→ 登录页切换后定时器继续跑并对已卸载组件 setState。
- `packages/client/src/pages/Editor/EditorCanvas.tsx:195-215`：useEffect 内 `setTimeout(resizeComponent, 500)` 无清理（:201-204）。
- `packages/client/src/components/Login/WechatLogin.tsx:34-46`：轮询用 `debounceWait: 2000` 的递归 `execCheckScan()`,停止条件依赖闭包里的 `wechatLoading`,Modal 关闭后存在继续轮询窗口;无最大轮询次数。二维码 TTL 120s 与 Redis TTL 一致（wechat-login.service.ts:44,97）这点是对的。
- 修复：三处补 cleanup/终止条件。

### P1-10 JWT 无刷新、无吊销、validate 每请求查库 + 死代码

- `packages/server/config.ts:56-60`：7 天长效 token;全工程无 refresh token、无黑名单/版本号机制 → token 泄露 7 天内不可撤销（配合 localStorage 存储放大,store/auth.ts:6）。
- `packages/server/src/utils/JwtStrategyTool.ts:28-29`：`data.exp - data.iat <= 0` 是死代码 —— passport-jwt 已在解包时校验 exp,过期 token 走不到 validate。
- `:31`：validate 每请求 `findOne` 查库（正确但无缓存,高频接口翻倍 DB 压力）。
- 修复：短 access + refresh;登出改 tokenVersion;可选 Redis 缓存用户。

### P1-11 微信 access_token 无缓存

- `packages/server/src/utils/modules/wechat-login-tool.module.ts:44-50`：每次生成二维码都现拉 access_token（微信有每日限额与有效期 7200s）→ 高频调用直接撞限。修复:Redis 缓存 token（工程已有 RedisModule 却不用）。

### P1-12 错误信息外泄给客户端

- `packages/server/src/low-code/low-code.service.ts:106-109`：`throw new InternalServerErrorException(\`发布失败，${err}\`)` —— 原始驱动错误（SQL 片段/表结构信息）直接进响应 msg;AbnormalFilter 原样透传。
- 修复：对外固定文案,内部 Logger 记录 err。

### P1-13 问卷提交无频控、props 无类型/大小校验（存储滥用面）

- `packages/server/src/low-code/low-code.service.ts:203-213`：`props` 原样 `save` 进 simple-json text 列,无长度限制、无字段校验（PostQuestionDataRequest 仅是 TS 类型）;`page_id` 不校验归属。
- 防重只有 P0-3 的 ip+ua → 换 UA 即刷;check-then-insert（:205-210）并发竞态可插重复。
- 修复：props 白名单结构 + 总大小上限 + 提交接口 throttler。

### P1-14 部署链路：nginx 默认 1MB body 上限 vs 200MB 上传限制（功能性断裂）

- `nginx/server.nginx.conf`：无 `client_max_body_size`（默认 1m）→ `POST /api/resources/upload`（controller 允许 200MB,resources.controller.ts:19）经网关必 413。
- 同文件 `:12` `proxy_set_header X-Forwarded-For $remote_addr` 用**覆盖**而非 `$proxy_add_x_forwarded_for` → 多层代理下 IP 链断裂（反哺 P0-3）。
- 无 gzip、无安全响应头（HSTS/X-Content-Type-Options/X-Frame-Options）、无 limit_req;access/error log 用容器内默认路径（非 stdout）,无轮转 → 磁盘增长无界。

### P1-15 Docker：无 .dockerignore + `COPY . /app` → .env/node_modules 进镜像层

- 根目录无 .dockerignore（find 验证为空);`server.Dockerfile:3` 与 `release.Dockerfile:3` 均 `COPY . /app` → 本地 `.env`（DB/Redis/OSS/微信密钥）、node_modules、dist 全部进镜像层并随镜像分发。
- 单阶段镜像 + 运行时 `pnpm start`（CMD）→ 生产容器携带全部 devDependencies、pnpm 本体;`npm install pnpm -g` 依赖外网;构建缓存 `COPY . /app` 在任意文件变动后全量重装。
- 建议多阶段（deps/build/runtime）+ `--mount=type=cache` + 非 root 用户 + HEALTHCHECK。

### P1-16 docker-compose 无数据层、无健康检查、无资源限制、无日志轮转

- `docker-compose.yml` 全文仅 4 个服务（backend/backend_nginx/frontend/frontend_nginx）——**MySQL/Redis 完全不在 compose 内**（靠宿主机自装,nginx 经 host.docker.internal 回环）,也就无数据卷、无备份故事;无 depends_on、无 healthcheck、无 mem/cpus 限制、无 logging max-size。
- 架构性绕路：backend 容器已发布 5001 端口,backend_nginx 再绕宿主机回环访问 `host.docker.internal:5001`（:13-14）——同 compose 网络内直接用服务名 `backend:3000` 即可,现方案多两层 NAT 且强依赖宿主端口。
- `version: '3'` 字段已废弃。

### P1-17 测试为零

- `packages/server/package.json:16-20` jest 配置齐全（含 e2e 脚本、supertest 依赖）,但全仓 find 无任何 `*.spec.ts` / `*.test.tsx` / vitest/playwright 配置 —— `"test": "jest"` 输出 "No tests found"。
- client/release/share 无测试设施。事务发布、验证码防刷、XSS 消毒这类本次审计的翻车点,恰好都是测试可拦的。

### P1-18 DTO 校验形同虚设（class-validator 覆盖率极低）

- 全部 4 个 DTO（user/dto/*.ts）只有 `@IsNotEmpty + @IsString`:无 `@IsPhoneNumber`、无 `@Length` 密码强度、无 `type` 枚举（`CaptchaDto.type`/`SendCodeDto.type` 任意字符串直通 Redis key `${type}:captcha:${key}`,user.service.ts:30）。
- 后果：任意字符串"手机号"直达短信网关（TextMessageTool.ts:9-23,费用浪费面）;低代码侧 0 个 class DTO（P0-5）。low-code/resources 控制器的 `@Query() {id:number}` 全靠 TS 类型装样子。
- 修复：全员 class DTO + 枚举 + 长度/格式校验 + transform/whitelist。

### P1-19 客户端路由守卫仅前端且为 hash 路由

- `packages/client/src/router/index.tsx:9`：createHashRouter;守卫在 `pages/index.tsx:9-15`（useEffect 里 nav 跳转）。直接敲 URL 会先渲染编辑器壳再跳,数据靠后端 401 兜底（这层是有的）。博客不应表述为"路由级权限控制"。

### P1-20 日志规范缺失

- 服务端唯一"日志"是 4 处 `console.log`：`low-code.service.ts:107`（原始 err）、`wechat-login.service.ts:32,53,63`（回调整包打印,含 open_id 等敏感字段）;前端调试残留 `EditorCanvas.tsx:164`（`console.log(111, entries)`）、`DataSource.tsx:98-100`。无 Nest Logger、无请求日志、无错误堆栈落盘。

---

## P2 —— 建议

1. `main.ts:15` ValidationPipe 加 `{transform:true, whitelist:true, forbidNonWhitelisted:true}`（配合 P0-5/P1-18）。
2. C 端 `GET /low_code/release?id=`（low-code.controller.ts:37-39）：id 无校验;**不带 id 时 where 全 undefined → TypeORM 空条件返回表中第一行**（信息面小泄漏,建议 required 校验）;`release/src/app/[id]/page.tsx:7` id 未编码直接拼 query。
3. release 包无 `not-found.tsx`/`error.tsx`：`page.tsx:13,20` throw → 用户看到 Next 默认 500 页（"未找到"业务语义丢失）。
4. SSR 取数依赖 `NEXT_PUBLIC_API_BASE_URL`（构建期注入、浏览器可见）,`.env.example` 默认 `127.0.0.1:5000` 在容器内必失败 → 容器化时 SSR 回环强依赖公网地址,配置故事要写清。
5. `low-code.service.ts:170-180`：`components` 为空时 `In([])` 边界(TypeORM 对空数组行为依版本而异,建议判空短路);`simple-array` 空数组序列化为 `''` 的已知 quirk。
6. `useStoreComponents.ts:261-263`：草稿 `JSON.parse` 无 try/catch,损坏草稿即崩溃;`store_time`/`release_time` 双 key 时间戳协议脆弱（Center.tsx:30 / release_time）。
7. `pages/Editor/Header/Right.tsx:18`、`dataCount.tsx` 头像硬编码外链 `https://sdfsdf.dev/40x40.png`（第三方占位服务,生产不可控）;用户信息未接入。
8. `pages/Editor/EditorCanvas.tsx:131-150,227-229`：工具栏用 `document.querySelectorAll` + `getBoundingClientRect` 定位,绝对定位坐标与滚动容器换算靠 500ms 延时+强制 re-render 修补,滚动/缩放下会漂移;`editor.tsx:15` 每渲染 `createRef`（应 useRef）;`:26-56` 滚动 effect 依赖 `[scrolling]` 自我重挂。
9. `ComponentFields.tsx:11-14`：early return 后调用"伪 hook" `useStoreComponents()`(当前未含真 hook 故不炸,但 anyone 往里加 useEffect 即触发条件 hook 违规)。
10. `TextComponent.tsx:16-37`：useEffect+setState 派生 className,应 useMemo;多余一帧渲染。
11. `VideoComponent.tsx:31` `{...objectOmit(props,["startTime"])}` 与 `QrcodeComponent.tsx:12` `<QRCode {...props}>` 全量透传用户 options 到 DOM/antd 组件 —— 运行时多余属性、未来 antd 属性冲突面。
12. `ResponseIntercept.ts:20`：魔字符串 `'微信验证回调'` 耦合协议,建议 header/枚举。
13. `redis.module.ts`：无 `onModuleDestroy` 优雅关闭;`getCachedData` 对 `fetchFunction` 返回 undefined 时 `redis.set(key, undefined)` 会抛(目前唯一调用点已注释,属埋雷);JSON.parse 无容错。
14. `user.service.ts:47-54`：60s 防重判断与 TTL=60s 重复,exists 分支永真,属冗余代码(无害)。
15. 根 `package.json` 把 antd/react 放 dependencies(应为各包私有);无 lint-staged/husky;CI 配置不在仓内(README 提云效)。
16. `pages/release.tsx:19` `<embed type="text/x-scriptlet">` 为 IE 时代类型,现代浏览器等价 iframe;二维码含 `VITE_RELEASE_BASE_URL`,生产配错则扫码失效。
17. `docs/API.md` 与实现的偏差集中在:`release_with_user` 行为、发布"整体替换(页面+组件+问卷数据)"描述(代码实际保留 component_data 行)、错误约定表称 500 走统一包装(实际仅 HttpException)。

---

## 博客表述风险清单（成稿修正依据）

| # | 博客可能的说法 | 风险 | 建议表述 |
|---|---|---|---|
| 1 | "密码 MD5 加密存储" | 机制属实但是**负面项**:无盐无 KDF(SecretTool.ts:6-9),彩虹表秒破;配合无登录限流更糟 | 如实写并自评:"教学实现用了裸 MD5,生产必须换 bcrypt/argon2"——这反而是好素材 |
| 2 | "图形码+短信码+60s 防刷体系" | 4 位码+Math.random+失败不失效无上限(user.service.ts:73-74,166-173),60s 内可爆破 | 写成"防刷骨架,三个具体漏洞待补",别写成"完整防刷体系" |
| 3 | "事务化发布保证一致性" | 事务与回滚真实存在(low-code.service.ts:88-112);但客户端可注入字段改 id/account_id(:59-62)、并发无行锁、统计链路一致性被 P1-7 打破 | 限定为"对页面行+组件行的原子替换;字段白名单/行锁/统计一致性未闭环" |
| 4 | "发布保留历史问卷数据(修正)" | 行保留了,但组件 id 每次发布重生成,历史答案全部变孤儿(:68-74 + Center.tsx:47-52) | 删除或如实写"保留了行但失去关联,统计价值归零" |
| 5 | "全局 JWT 守卫杜绝越权" | 守卫机制属实;但 resources DELETE 先删 OSS 后验归属(resources.service.ts:44-53),存在真实越权删文件 | 守卫亮点照写,另补一节"IDOR 案例:OSS 删除的归属校验顺序" |
| 6 | "MD5(ip+ua) 匿名防重复提交" | 反代后 request.ip=网关 IP(main.ts 未设 trust proxy):同 UA 用户互挤、换 UA 即绕过 | 加限定"单机直连下有效;反代场景需 trust proxy+XFF 链" |
| 7 | "上传有大小/类型校验" | mimetype 可伪造、SVG/HTML 可入库上 CDN(resources.controller.ts:20-21 + ali-oss.module.ts:48-50);nginx 默认 1MB 让 200MB 限制在生产必 413 | 写"校验存在但可绕过+网关配置缺失",或修完再吹 |
| 8 | "富文本用 DOMPurify 防 XSS" | SSR 分支显式跳过消毒(RichTextComponent.tsx:12-13),首屏 HTML 未净化 | 必须点破这个洞;若成稿前已修,改为"isomorphic-dompurify" |
| 9 | "微信扫码登录全链路跑通" | 回调无签名校验 + Nest 默认解析不了 text/xml(代码注释自认"正式版本"被注释,wechat-login.service.ts:55-62) | 写"链路设计完整;回调签名校验与 XML 解析在工程里是留白" |
| 10 | "进入编辑器自动加载已发布页面" | `release_with_user` 传 null 恒空(low-code.controller.ts:29),客户端 Object.keys(undefined) 崩溃(useStoreComponents.ts:296)——实际只靠 localStorage 草稿 | 修正为"草稿驱动;服务端恢复链路有 bug" |
| 11 | "拖拽添加组件" | 物料面板是**点击**添加(ComponentList.tsx:112-127 onClick push);dnd-kit 只用于画布内**排序**(SortableContainer/Item) | 精确表述:"点击添加 + 画布内拖拽排序" |
| 12 | "优化了 N+1 查询" | 只优化了 getReleaseData(In 批量);getQuestionData/getQuestionDataByIdRequest 仍双层 N+1(low-code.service.ts:239-253,272-293) | 限定范围,或把统计链路一起修了再写 |
| 13 | "统一异常处理保证 {code,data,msg}" | 仅 HttpException 被包装(AbnormalFilter.ts:5);未捕获异常穿透默认 500 | 补一句"非 HTTP 异常路径未覆盖" |
| 14 | "Docker+Nginx 生产级部署" | compose 无 MySQL/Redis 服务、无 healthcheck/资源限制/日志轮转;单阶段镜像+COPY . 带入 .env 与 node_modules(无 .dockerignore);运行时 pnpm start | 降格为"教学级/参考级部署",并列出五个缺口(正好是成稿的生产化 checklist) |
| 15 | "有测试保障/ Jest 测试" | jest 配置齐全但**0 个测试文件** | 删除该表述;或以"从 0 到 1 补测试"为续篇选题 |
| 16 | "JWT 7 天有效期" | 无 refresh、无吊销、validate 每请求查库(JwtStrategyTool.ts:28-29 的过期检查是死代码) | 写现状可以,别写成"安全可靠的无状态会话" |
| 17 | "15 种组件、两端共用物料" | **无风险,可放心写**(share 包 componentList 恰 15 个,componentExport.ts:22-38) | 注意文本组件的 type 名是 `titleText` 不是 `text` |
| 18 | "撤销/重做/快捷键/草稿" | 功能属实(mobx-shallow-undo + useComponentKeyPress);但 undo 对整 store 深拷贝、`_replace` 不恢复 copyedCompConig,大页面有内存放大 | 可写,建议加"实现取舍"一段 |
| 19 | "C 端问卷防重复提交" | 仅 ip+ua(见 #6),换 UA 即刷,且 props 无校验可注入任意 JSON | 同 #6 一并降格 |

### 修正优先级建议（落地顺序）

1. 成稿即改口径(无需改代码)：#3、#4、#7、#10、#11、#14、#15。
2. 低成本修代码再成稿(半天)：P0-4(DELETE 加 account_id)、P0-7(controller 传 undefined→改 service 按 account 查)、P0-6(发布时落库前消毒或换 isomorphic-dompurify)、P1-2 前端 rethrow。
3. 高价值但工作量大(可开续篇)：bcrypt 迁移+验证码加固(P0-1/2)、trust proxy+XFF(P0-3)、发布字段白名单(P0-5)、compose/镜像生产化(P1-15/16)。

---

## 附：本次审计引用文件索引（绝对路径前缀 = PROJ）

```
PROJ=/Users/Wang/Code/github/web-x-blog/work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full
packages/server/config.ts · src/main.ts · src/app.module.ts
packages/server/src/user/{user.controller.ts, user.service.ts, dto/*.ts, entities/user.entity.ts}
packages/server/src/utils/{SecretTool, RandomTool, CaptchaTool, JwtStrategyTool, GetUserMessTool, TextMessageTool, WechatDataTool}.ts
packages/server/src/utils/modules/{redis.module.ts, ali-oss.module.ts, wechat-login-tool.module.ts}
packages/server/src/utils/guards/jwt-auth.guard.ts · src/utils/decorators/public.decorator.ts
packages/server/src/low-code/{low-code.controller.ts, low-code.service.ts, entities/low-code.entity.ts}
packages/server/src/resources/{resources.controller.ts, resources.service.ts, resources.module.ts, entities/resources.entity.ts}
packages/server/src/wechat-login/{wechat-login.controller.ts, wechat-login.service.ts}
packages/server/src/common/{AbnormalFilter.ts, ResponseIntercept.ts}
packages/share/src/components/LowCodeRichText/RichTextComponent.tsx · LowCode{Text,Image,Video,List,Swiper,Qrcode,Input,Radio,Checkbox,Alert,Card}/*.tsx
packages/share/src/utils/{object.ts, type.ts, componentExport.ts} · src/types/request/{low-code.ts, user.ts}
packages/client/src/{utils/request.ts, store/{auth,page,components,index}.ts, hooks/{useStoreAuth,useStoreComponents,useStorePage,useSendCode,useComponentKeypress}.ts}
packages/client/src/pages/{index.tsx, editor.tsx, preview.tsx, release.tsx, dataCount.tsx, DataCount/*.tsx, Editor/*.tsx, Editor/Header/*.tsx, Editor/LeftPanel/ComponentList.tsx, Editor/RightPanel/*.tsx}
packages/client/src/components/{DragSortable/*.tsx, Login/*.tsx, Register/RegisterOption.tsx, LowCodeComponents/LowCodeRichText/RichTextComponentProps.tsx}
packages/client/src/router/index.tsx · src/api/*.ts · vite.config.ts
packages/release/src/app/[id]/page.tsx · src/app/layout.tsx · src/components/ComponentRender.tsx · next.config.js
docker-compose.yml · server.Dockerfile · release.Dockerfile · server.nginx.Dockerfile · release.nginx.Dockerfile · nginx/{server,release}.nginx.conf · .gitignore
docs/{API.md, schema.sql} · packages/server/.env.example · 各包 package.json
```
