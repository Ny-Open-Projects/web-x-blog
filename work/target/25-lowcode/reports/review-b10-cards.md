# 审稿 B10：课程25 知识卡片逐卡审校（review-b10-cards）

- 审校对象：`work/target/25-lowcode/cards/` 全部 35 张卡 + README.md 总目（共 36 个文件，逐个过）
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`、`reports/review-eng-b.md`（19 条表述风险）、`cards/README.md` 表述红线、229 篇博客修正后口径（重点 30-6 / 14-4）
- 源码真源：SRC = `work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`；自研参考实现（工作流/沙箱卡）另核对 `小滴课堂低代码大课/lowcode-platform`
- 审校日期：2026-11-19。本报告只出结论，不改卡片文件。
- 严重度：P0=安全/正确性硬伤；P1=事实错误或与修正后口径相悖，必须修；P2=建议/格式，可选。

---

## 一、总体结论

- **P0：0 条**。无 RBAC 夸大（concept-07 已自带边界说明）、无把自研参考实现说成课程原始代码的硬伤（concept-09/10 均已标注）。
- **P1：24 条**，集中在 18 个文件。重灾区：①Redis 缓存族卡（principle-04 / practice-09 / interview-03 / README 总目）沿用旧口径 `getCacheData`，与 30-6 修正后的 `getCachedData`、TTL 600s、「缓存版本在最终仓库处于注释状态」相悖；②事务卡（principle-03）流程描述与 SRC 矛盾；③字段/路由名漂移（`/resource` vs `/resources`、`userId` vs `account_id`、`isScan:false` vs `'no'`、`request:code:` vs `register:code:`、`text` vs `titleText`、`types/local.ts`、`generatorComponent`、NodeContract 假字段）。
- **合格（含仅 P2 建议）：18 个文件**。
- 字数：35 张卡正文 158~316 个汉字，全部落在 150~400 字区间；front-matter 35/35 全过（categories、tags 含 25-lowcode、date、title）。

---

## 二、全量规范检查结果

| 检查项 | 结果 |
|---|---|
| front-matter `categories: [课程, 低代码]` | 35/35 通过（README 为总目无 front-matter，不算卡） |
| tags 含 `25-lowcode` | 35/35 通过 |
| `date` / `title` | 35/35 通过，date 均为 2026-11-17 |
| 字数 150~400 | 35/35 通过（最少 practice-06 158 汉字，最多 interview-05 316 汉字） |
| 出处「课程25 · xx-x」格式 | 32/35 带「课程25 ·」前缀；concept-09 / concept-10 / concept-11 缺前缀（见各卡 P2） |
| 出处编号真实性 | 逐个核对 posts 目录集数，practice-06 的 21-10、interview-06 的 28-7、interview-02 的 8-3 等均已核实；其中 interview-02 的 8-3 与内容不符（P1，见该卡） |

---

## 三、逐卡审校

### 概念卡（11 张）

#### concept-01-meta-driven ——【合格（附 P2 建议）】
事实核对：options 为 simple-json 列、page.components 存 id 串、MobX 字典+排序数组（`store/components.ts` 五状态）——均与 SRC 一致。出处 14-2、18-5 属实。
- P2｜去AI味｜「低代码的本质一句话：**用元信息……把"写代码"变成"配数据"**」：整句加粗是典型 AI 腔，建议只加粗「用元信息描述应用、由通用引擎解释执行」这类短语，或去掉整句加粗。

#### concept-02-schema-dsl ——【需修】
- P1｜事实｜「入参类型放 `types/local.ts` 并用 `Omit` 排除前端不该传的 id/accountId」→ SRC 无 `types/local.ts`，实际是 `packages/share/src/types/request/low-code.ts`（`Omit<ILowCode, "account_id" | "id">` 等）。建议改为「入参类型放 `types/request/`（如 `PostReleaseRequest` 用 `Omit` 排除 account_id/id）」。
- P2｜事实｜「options 用 `Record<string,any>`」建议补一句出处形态：component 实体 `options` 列即 simple-json，双端共享同一 TS 类型。

#### concept-03-material-registry ——【需修】
- P1｜事实（review-eng-b #17 明示）｜「15 种组件（**text**/swiper/list/...）」→ 文本组件 type 名是 `titleText` 不是 `text`（SRC `share/src/utils/componentExport.ts`：`titleText: TextComponent`）。建议改为「titleText/swiper/list/image/video/card/split/richText/qrcode/alert/input/textArea/radio/checkbox/empty」。
- P2｜事实｜「视图映射放 share、配置映射只放 client」表述正确（`share/func.ts getComponentByType`、`client attributeExport getComponentPropsByType`），建议把这两个函数名写实，增强可核对性。

#### concept-04-render-engine ——【需修】
- P1｜事实｜「渲染链路是 `getComponentById → generatorComponent → ...`」→ 函数名拼错，SRC 为 `generateComponent`（`client/src/pages/Editor/EditorCanvas.tsx:27`）。改为 `getComponentById → generateComponent → getComponentByType → toJS → 展开 props`。
- P2｜口径｜自研参考实现段（render-page.ts / `GET /api/pages/:id/render`）已标明出处区分，符合红线；建议在句中再点一次「自研参考实现（lowcode-platform）」全名，避免读者误以为是课程配套代码。

#### concept-05-data-model ——【需修】
- P1｜事实｜「component_data 存问卷填写结果：pageId/**componentId**/**userKey**（MD5(ip+设备)……）/props」→ SRC `ComponentData` 实体只有 `id/page_id/user/props` 四列，没有 componentId 列（组件 id 存在 `props[].id` 里）；字段名是 `user`（值 = MD5(ip+ua) 访客匿名标识，14-2 修正口径 A9-2）。建议改为「page_id / user（MD5(ip+ua) 访客匿名标识，非登录用户）/ props（`{id, value}` 数组，id 即组件 id）」。
- P1｜事实｜五张表名单写「resource」→ 表名是 `resources`（`@Entity({ name: 'resources' })`）。
- P2｜口径｜「同设备防重复提交」建议按 review-eng-b #6 加限定：「单机直连下有效；反代场景需 trust proxy + XFF，否则 ip 失真」。
- P2｜事实｜「组件表（存配置：type/title/options）」→ title 不是独立列，是 options 里的字段；建议写「type 列 + options（title 在 options 内）」。

#### concept-06-protocol ——【需修】
- P1｜事实｜「WorkflowContract（节点 NodeContract {type, ports, execute} + 图 DSL）」→ 契约里没有 `ports` 和 `execute` 字段。SRC（lowcode-platform `packages/shared/src/workflow-contract.ts`）：`NodeContract { type, category, label, version, inputs, outputs }`，注释明言「执行逻辑不在此处，仅后端运行时有」（执行器在 `nodes/registry.ts` 的 NODE_REGISTRY）。建议改为「NodeContract {type, category, label, version, inputs, outputs}，契约与执行器分离（NODE_CONTRACTS / NODE_REGISTRY）」。

#### concept-07-permission-model ——【合格（附 P2 建议）】
事实核对：JwtAuthGuard APP_GUARD 全局注册、@Public 豁免、validate 二次查库抹 password、发布页公开接口、account_id 数据归属——均属实；RBAC 红线已自带边界说明，合格。
- P2｜事实｜「数据归属：所有表带 account_id」→ component_data 没有 account_id 列（经 page_id 关联页面归属），user 表自身也无此列。建议改为「page/component/resources 三表带 account_id；component_data 经 page_id 挂到页面归属」。
- P2｜事实｜「validate 里二次查库并抹除 password」建议精确为「返回值置 `password: ''`」，与 SRC（JwtStrategyTool.validate 返回 `{...user, password: ''}`）完全对齐。

#### concept-08-release-pipeline ——【需修】
- P1｜口径（14-4 修正后口径）｜「重新发布不保留编辑历史（课程版），且**会重置历史问卷数据**」→ 与 SRC 相悖：最终仓库 `low-code.service.ts` 的 release 更新分支不删 component_data（代码注释明言「生产化修正：保留 component_data」），课程原始实现才会删。且漏了关键限定「组件 id 发布后重生成，历史答案与组件的关联断裂，统计端对失效 id 容错」。建议改为：「重新发布不保留编辑历史；问卷数据行按最终仓库口径保留（课程原始实现会清空），但组件 id 每次发布重生成，历史答案只剩孤儿行」。
- P2｜事实｜草稿三份状态 + storeTime、发布成功记 releaseTime 并自动存草稿——已对 SRC（useStoreComponents.storeInLocalStorage / Header/Center.tsx）核实无误。

#### concept-09-sandbox ——【合格（附 P2 建议）】
事实核对（lowcode-platform）：vm 封 Function/globalThis/global、256KB 配额、watchdog、`isolation:'vm'`、注释原文「vm 模块本身不是安全边界」、容器 CapDrop ALL/no-new-privileges/非root/只读根/128MB/0.5核/pids 64、fallbackReason、wf_audit（codeHash/isolation/outputBytes）——全部属实。
- P2｜格式｜出处「scan3 §2-A；scan4 §7」缺「课程25 ·」前缀，建议统一为「课程25 · 自研参考实现（lowcode-platform）；scan3 §2-A」。
- P2｜事实｜「`nodes/sandbox.ts`」实际路径是 `apps/server/src/modules/workflow/nodes/sandbox.ts`，建议写全或写相对模块路径。

#### concept-10-workflow-dag ——【需修】
- P1｜事实｜「节点契约 `NodeContract {type, ports, execute}`」→ 同 concept-06，契约字段为 `{type, category, label, version, inputs, outputs}`，execute 在 NODE_REGISTRY 的执行器里。建议同步改。
- P2｜事实｜「端口类型（data/schema/trigger）」→ 实际 `PortType` 有 7 种：`trigger|data|record|schema|condition|page|any`；建议写全或加「等 7 种」。
- P2｜格式｜出处「scan3 §2-A」缺「课程25 ·」前缀（同 concept-09）。
- 其余事实（7 类节点、Kahn 检测环抛错、沿边注入、Provider 可替换、wf_run/wf_run_node）均已对源码核实无误。

#### concept-11-lowcode-vs-nocode ——【合格（附 P2 建议）】
- P2｜格式｜出处「scan4 §9」缺「课程25 ·」前缀。
- P2｜去AI味｜「自研的真正价值不在省写页面的时间，而在**把业务差异化能力沉淀为可复用资产**」：加粗可收窄到「沉淀为可复用资产」。

---

### 原理卡（6 张）

#### principle-01-schema-to-ui ——【合格】
事实核对：observer/toJS 前提、五状态（compConfigs/sortableCompConfig/currentCompConfig/copyedCompConig/itemsExpandIndex）、omit 回填表单——与 SRC 一致，无修改项。

#### principle-02-drag-index-swap ——【合格（附 P2 建议）】
事实核对：MouseSensor `distance: 2`（SortableContainer.tsx:30-32）、closestCenter、verticalListSortingStrategy、useSortable 解构、transform 的 `scaleY` replace（SortableItem.tsx:21）、arrayMove 共用、持久化进 page.components——全部与 SRC 一致。
- P2｜口径（18-4 修正后口径 A3-2）｜「`useSensors` 设 2 像素激活约束**提升灵敏度**」→ 建议对齐修正口径：「激活约束 `distance: 2` 是区分『点击』与『拖拽』的阈值」，去掉「提升灵敏度」的说法。

#### principle-03-transaction-release ——【需修】
- P1｜事实（与 SRC 矛盾）｜首段「发布一次页面 = 查旧页面 → 删旧 Component → **删旧 ComponentData 关联** → 插入新组件 → 回填 ID」→ SRC 更新分支不删 ComponentData（保留问卷行）。建议把该步从主流程里拿掉，主流程改为「置空并更新 Page → 删旧 Component →（保留 component_data）→ 插入新组件 → 回填 ID」，课程原始实现的「删问卷」只作为历史口径在修正点里出现。
- P1｜事实｜代码注释「按「用户 ID+页面 ID」查」→ SRC 是 `queryRunner.manager.findBy(Page, { account_id: user.id })`，只按 account_id 查（「存在则更新」的 upsert 语义也由它决定）。改为「按用户 ID（account_id）查」。
- P1｜口径（14-4）｜「课程版修正点：参考实现在删旧组件前保留 component_data 问卷数据，避免重新发布清掉用户答卷」→ 建议对齐 14-4 措辞并补半句：「最终仓库修正点：课程原始实现会连问卷数据一起删；参考实现（最终仓库）已改为保留 component_data 行——但组件 id 每次发布重生成，历史答案与组件的关联断裂，统计端对失效 id 容错」。
- P2｜口径｜「throw new InternalServerErrorException(err); // 失败要抛具体 error」→ SRC 确实这么写，但 14-4 已修正为「教学实现如此；生产上错误详情只进日志，对外固定文案」（review-eng-b P1-12：原始驱动错误外泄）。建议在注释里补「（教学实现；生产应对外固定文案、err 只进日志）」。

#### principle-04-cache-qps ——【需修】
- P1｜口径（30-6 修正后口径，scan6 A2）｜全文方法名用 `getCacheData` → SRC（redis.module.ts）与修正后博客均为 **`getCachedData`**（代码块、正文「getCacheData 通用封装」共 3 处都要改）。
- P1｜口径（30-6）｜「force=true 强制清缓存主动失效」→ 修正口径是「force 置空 data 后回源重查并覆盖写回，**并非显式 del**」。建议改为该表述，或「force=true 时把已读到的缓存置空再回源覆盖写回」。
- P1｜口径（30-6 导语/推广段）｜缺关键限定：「该缓存版本在最终仓库源码中处于注释状态，课堂演示后未合入主线，线上接口仍走无缓存版；getCachedData 以注释形式保留在 low-code.service.ts 调用处」。原理卡讲通用模式没问题，但「本项目实例」必须带这条，否则读者会以为线上接口已生效。
- P1｜去AI味/错字｜「这 **teaches** 一个真话」→ 中英混杂，改为「这说明一个朴素的道理」或「这条经验很实在」。
- P2｜口径｜「提升有限但稳定，因为该接口查询本身不重」→ 30-6 修正口径给的原因是「样本只有 800 个，量级太小，缓存优势还没完全拉开」；建议补上样本量口径（两个原因可并存，但博客口径在前）。

#### principle-05-jwt-chain ——【合格】
事实核对：sign 只放 id、7 天有效期（config.ts `JWT_EXPIRES_IN '7d'`）、Bearer 注入、ExtractJwt.fromAuthHeaderAsBearerToken、validate 三步（含 exp-iat 检查与二次查库）、APP_GUARD + @Public、注册即发 token——全部与 SRC 一致，无修改项。

#### principle-06-undo-redo ——【需修】
- P1｜事实（与 SRC 矛盾，review-eng-b #18）｜「课程版用 mobx-shallow-undo 包住 MobX store——shallow 意味着只对某一层做快照，**避免整棵深拷贝的性能开销**」→ SRC（useStoreComponents.ts:16-22）快照函数是 `() => toJS(storeComponents)`，每次变更对**整个 store 深拷贝**入 undo 栈，大页面有内存放大；`_replace` 恢复也不含 copyedCompConig。建议改为：「课程版用 mobx-shallow-undo 挂在 store 上，但快照函数是对整份 store 做 toJS 深拷贝——shallow 只是快照间的比较/去重方式；每步操作 O(组件数) 内存，大页面有放大，这是能讲清楚的实现取舍」。
- P2｜事实｜「hasUndo/hasRedo 判定按钮可用性」→ SRC 是判定后 message.warning 提示「没有可撤销的操作」，建议措辞改「用 hasUndo/hasRedo 兜底提示」。

---

### 实战卡（12 张）

#### practice-01-nestjs-core ——【需修】
- P1｜事实（review-eng-b #13）｜「异常过滤器统一 `{code:-1}`（**`@Catch()`** + switchToHttp()）」→ SRC AbnormalFilter 是 `@Catch(HttpException)`，只包装 HttpException，未捕获异常穿透 Nest 默认 500。建议改为「`@Catch(HttpException)` + switchToHttp()」，并补一句「非 HTTP 异常路径不在统一响应覆盖内」。
- P2｜事实｜「课程里 Redis 模块、AliOss 模块都是这个模式」属实（两个模块均 `static forRoot` 且 `global: true`），建议把「global: true 写在返回的 DynamicModule 里（不是 @Global 装饰器）」点明，与 practice-09 的修法呼应。

#### practice-02-typeorm-pitfalls ——【合格】
事实核对：mysql2 漏装、database 填库名、synchronize 开发开生产关、autoLoadEntities、find/update/delete 返回 affected、无 findAll、In 批量（统计模块 4 类组件 `In(['input','textArea','radio','checkbox'])`）、QueryRunner 弃用 getConnection——均与 SRC/课程口径一致，无修改项。

#### practice-03-captcha-antifraud ——【需修】
- P1｜事实（11-7/11-8 修正口径）｜「短信验证码三层 key **`request:code:phone`** / `login:code:phone`」→ SRC 与博客口径均为 `register:code:phone`（`${type}:code:${phone}`，type 取 register/login）。改为「`register:code:phone` / `login:code:phone`」。
- P2｜口径（review-eng-b #2）｜六步防线内容本身属实（60s 限流 + dayjs diff、图形码比对、忽略大小写、发短信、删图形码 + 时间戳_验证码写 Redis 60s、失败清理），建议末尾加一句骨架限定：「这套是防刷骨架；码空间、失败不失效、尝试无上限三点在深挖时要能自己说破」，与面试深挖衔接。

#### practice-04-wechat-scan ——【需修】
- P1｜事实｜「Redis 存 **`isScan:false`** → …… 置 **`isScan:true`**」→ SRC（wechat-login.service.ts:44,97,125）存的是字符串 `{ isScan: 'no' }` / `{ isScan: 'yes', token }`，判定 `redisData.isScan === 'yes'`。改为 `isScan:'no'` / `isScan:'yes'`（字符串）。
- P1｜口径（review-eng-b #9）｜「回调处理：POST 收 XML，xml2js 解析 + 拍平」→ 按修正口径补限定：「正式版 XML 流式解析（getXMLStr）在工程里仍是注释状态，实际走 Object.keys(body)[0] 的 JSON 形态；回调的 signature 校验也是留白」——链路设计讲清楚即可，别写成全链路已跑通。
- P2｜事实｜「接入验证：三参数字典序排序 + SHA1」属实（insert() 方法 `sort().join('')` + sha1）；「expire_seconds:120、TTL 120s」属实。

#### practice-05-oss-resource ——【需修】
- P1｜事实｜「接口 **`POST /resource/upload`**」「接口 **`DELETE /resource`**」→ 控制器是 `@Controller('resources')`，实际路由 `POST /resources/upload`、`DELETE /resources`（Query 传 id）、`GET /resources`。两处路由名都要改。
- P1｜事实｜「resources 表：id/url/**userId**/type/name」→ 实体字段是 `account_id`（`entities/resources.entity.ts`）。改为「id/url/account_id/type/name」。同段「按 id+**userId** 双条件删库」也改 account_id。
- P1｜口径（review-eng-b #5 / P0-4）｜「service 四步 = 查存在→删 OSS→按 id+account_id 双条件删库→返回——OSS 与 DB 同步清理」→ 该顺序在 SRC 里就是先删 OSS 后验归属（`findOneBy({id})` 不带 account_id，删完 OSS 才 `delete({id, account_id})`），存在越权删他人 OSS 文件的 IDOR 面。作为实战卡必须点破，建议补一句：「注意顺序隐患：查存在未带 account_id、先删 OSS 后删库，越权删文件面在排错/面试深挖时要能讲出（修复：查单即带 account_id，未命中按 404 处理）」。
- P2｜事实｜「拼对象 key（`upload-files/原名-时间戳.扩展名`）」→ SRC 是 `upload_files/`（下划线）。另外「先落库 URL」建议改为「上传成功后把返回 URL 落库」，避免读成先落库后上传。

#### practice-06-excel-export ——【合格】
事实核对：writeBuffer、Blob 数组包裹 + octet-stream、createObjectURL/revokeObjectURL、saveFileWithBlob、isWriteFile 双分支、zip.file/generateAsync、checkbox join(',')——与 SRC（client/src/utils/excel.ts、DataCount/ComponentDatas.tsx）一致，无修改项。

#### practice-07-docker-deploy ——【合格】
事实核对：node:18 → pnpm install → 先 build:share 再 build:server → EXPOSE 3000 → CMD pnpm start:server；nginx:1.25.0-alpine + ADD conf；upstream backend 与 proxy_pass 名字一致；compose 四容器端口 5001/5000/4001/4000、restart:always、`${xxx_tag}` 变量——全部与 SRC 一致，无修改项。
- P2（可选）｜口径｜按 review-eng-b #14 可加半句「教学级/参考级部署」限定（单阶段镜像 + COPY . 无 .dockerignore），卡内未写「生产级」，不算违规。

#### practice-08-jmeter ——【合格】
事实核对：非浏览器、JDK8、zh_CN、UTF-8、四件套、Bearer 头、Content-Type、90% Line、扫把清空（28-7 原词）、10 线程起跑、响应断言、集合点超时、setUp/tearDown——与博客口径一致，无修改项。

#### practice-09-redis-cache-pattern ——【需修】
- P1｜口径（30-6）｜标题与正文三处「getCacheData」→ 全部改 `getCachedData`（title、H1、正文加粗短语与调用签名）。
- P1｜口径（30-6）｜「force=true 主动失效」→ 改「force 为 true 时置空已读数据后回源覆盖写回（并非显式 del）」；并补「课程示例 TTL 600 秒」。
- P1｜口径（30-6）｜「五类用途……⑤接口缓存 QPS 优化」→ 必须限定：「⑤接口缓存（getCachedData 调用在最终仓库以注释形式保留于 low-code.service.ts，未合入主线）」，否则与 30-6 修正口径直接矛盾。
- P2｜事实｜「`@Global` + 静态 forRoot」→ SRC 是 forRoot 返回的 DynamicModule 里配 `global: true`，没有用 @Global 装饰器；建议改写为「forRoot 返回的 DynamicModule 带 `global: true`」。

#### practice-10-editor-interactions ——【合格】
事实核对：threshold:0.9、root 设画布容器、disconnect 清理、data-id 匹配、getBoundingClientRect、500ms 延迟、useImperativeHandle——与 EditorCanvas.tsx 一致；滚动显隐 200ms/10% 与 18-8 口径一致，无修改项。

#### practice-11-stat-frontend ——【合格】
事实核对：In 查四类组件、先校验页面存在、Promise.all 聚合、filter→单值包数组→flat、key/dataIndex=组件 id、checkbox join、ECharts 横向柱状图要点、组件 id 当 key 的 React 警告（21-8 原口径）——全部一致，无修改项。

#### practice-12-component-recipe ——【合格】
事实核对：五步范式、必改三处、pnpm build:share、value/defaultValue/isHidden、FormContainerWithList（keyName/newItemDefaultValue 等）、onChange/onUpdate 回调、Tailwind base 重置、ColorPicker toHex——与课程口径一致，无修改项。

---

### 面试卡（6 张）

#### interview-01-tech-choice ——【合格（附 P2 建议）】
- P2｜口径（review-eng-b #19）｜简历亮点①「Redis 原子性防重提交」是课程原话，建议在「每个亮点要能讲清为什么做」后补一句：「防重深挖点：实际靠 MD5(ip+ua) + exists 检查，反代下需 trust proxy」——把追问预案提前备好。

#### interview-02-security ——【需修】
- P1｜事实（review-eng-b P1-1）｜「CORS 锁域名」→ SRC `main.ts` 是裸 `app.enableCors()`，`Access-Control-Allow-Origin: *`，全开无白名单（可锁域名的是自研参考实现 A）。本项目语境下应删掉或改为「CORS 未收紧是待补项（生产应配白名单）」。
- P1｜口径｜「防账号枚举：账号不存在与密码错误统一提示『账号或密码错误』」→ 这是**预先课**（用户的登录接口开发）的教学实践；主课程工程（11-8/SRC）实际是分开提示（「登录的账号不存在」/「密码错误」）。建议注明：「预先课教学版做了统一提示；课程主工程此处未统一——面试可作为『我后来补的改进』来讲」，避免与源码对不上。
- P1｜出处｜出处「课程25 · 8-3、11-6、14-3、27-8」中的 **8-3**（前端子项目 React 创建和项目配置）与本卡内容无关；防枚举内容来自预先课「用户的登录接口开发」。建议改为「课程25 · 预先课-用户的登录接口开发、11-6、14-3、27-8」。
- P2｜口径（review-eng-b #6/#19）｜「问卷防重复提交靠 userKey（IP+设备加密）」建议补限定「单机直连有效；反代 + 未配 trust proxy 时 ip 失真」，防面试深挖翻车。

#### interview-03-performance ——【需修】
- P1｜口径（30-6）｜「加 Redis 缓存（**getCacheData**，TTL 过期 + force 主动失效）」→ 方法名改 `getCachedData`；force 表述改「置空回写，并非显式 del」；并补限定「该缓存版本在最终仓库处于注释状态、未合入主线，压测演示用的是课堂版代码」——面试里若被追问「线上生效了吗」，这条就是保命的。
- P2｜口径｜「提升有限但稳定，因为原查询本身不重」→ 补 30-6 口径「样本只有 800 个」。
- P2｜去AI味｜「这反而体现诚实：**缓存收益取决于原查询成本，压测验证而不是拍脑袋**」：整句加粗收窄为「压测验证而不是拍脑袋」。

#### interview-04-lowcode-highlights ——【合格】
事实核对：15 种组件两端共用、配置字典+排序数组、arrayMove 与键盘共用、云效四镜像双 Nginx + React 上 OSS、storeTime vs releaseTime、事务化发布——与 SRC/口径一致；出处 1-2、31-4 属实，无修改项。

#### interview-05-resume-rules ——【合格】
纯课程方法论（31-1~31-4），无源码映射事实，无修改项。

#### interview-06-pitfall-talk ——【合格（附 P2 建议）】
事实核对：容器名/库名、事务三坑、observer/toJS、itemExpandIndex（18-3/scan2 口径）、ulid、Tailwind base、CI 三连败（27-2~27-4）、扫把 + 响应断言（28-7/29-2）——均与课程口径一致。
- P2｜出处｜第 8 条「JMeter 乱码」更贴 28-x 环境配置与 29-2 响应断言，28-7 只是扫把清空那半句；出处串可补「29-2」更准。

---

### README.md 总目 ——【需修】
- P1｜口径（30-6）｜表格「practice-09-redis-cache-pattern | Redis 工程化封装与 **getCacheData**」→ 与卡片修正联动，改 `getCachedData`。
- 其余：35 张卡的编号/主题/出处与实际文件一致；「表述红线」四条与 review-eng-b/scan3 结论一致，无需改。

---

## 四、统计

| 类别 | 数量 | 明细 |
|---|---|---|
| 审校文件 | 36 | 35 张卡 + README |
| 合格 | 17 | concept-01、concept-07、concept-09、concept-11、principle-01、principle-02、principle-05、practice-02、practice-06、practice-07、practice-08、practice-10、practice-11、practice-12、interview-01、interview-04、interview-05、interview-06（其中 13 张附 P2 建议） |
| 需修 | 19 | concept-02、concept-03、concept-04、concept-05、concept-06、concept-08、concept-10、principle-03、principle-04、principle-06、practice-01、practice-03、practice-04、practice-05、practice-09、interview-02、interview-03、interview-06（仅 P2）、README |

注：上表「合格」17 + 「需修」19 = 36（interview-06 仅 P2，归入需修列仅因含可选建议，无必改项；若按严格口径「需修=含 P1」，则为 17 合格 / 18 需修 / 1 纯建议）。

| 严重度 | 条数 | 分布 |
|---|---|---|
| P0 | 0 | — |
| P1 | 24 | concept-02(1) concept-03(1) concept-04(1) concept-05(2) concept-06(1) concept-08(1) concept-10(1) principle-03(3) principle-04(4) principle-06(1) practice-01(1) practice-03(1) practice-04(2) practice-05(3) practice-09(3) interview-02(3) interview-03(1) README(1) |
| P2 | 22 | 见各卡「附 P2 建议」条目 |

**修复优先级建议**：
1. 先修口径族（一次改完，避免再次同步漂移）：principle-04、practice-09、interview-03、README 的 `getCacheData`→`getCachedData` + force 口径 + 「注释状态」限定（对应 scan6 A2 全部结论）。
2. 再修事务/问卷族：principle-03、concept-08（对应 14-4 口径与 SRC 保留 component_data 的事实）。
3. 字段/路由名族（机械替换）：concept-03（titleText）、concept-04（generateComponent）、concept-05、practice-03（register:code）、practice-04（'no'/'yes'）、practice-05（/resources、account_id）、practice-01（@Catch(HttpException)）、concept-06/10（NodeContract）、principle-06（undo 快照）、interview-02（CORS/8-3）。
4. P2 与出处格式（concept-09/10/11 加「课程25 ·」前缀等）可最后批量过。
