# 审稿 B6-P5：05.第五期（26 篇）专家复核报告

- 审稿对象：`work/target/25-lowcode/posts/05.第五期/`（17-1~17-5、18-1~18-8、19-1~19-5、20-1~20-8，共 26 篇）
- 真源对照（SRC）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`——本批重点核对 `packages/server/src/resources/*`、`src/utils/modules/ali-oss.module.ts`、`src/low-code/*`、`packages/client/src/components/LowCodeComponents/utils/components.tsx`、`hooks/useStoreComponents.ts`、`hooks/useComponentKeypress.ts`、`pages/Editor/*`、`pages/DataCount/*`、`utils/excel.ts`、`api/*.ts`、`packages/release/src/**`
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`、`reports/review-eng-b.md`（表述风险清单）、`reports/review-b5-p4.md`（判例与口径）
- 命名口径：沿用 b5-p4 裁定——**API / 类型 / 字段名一律以最终仓库（SRC）为准，教学期别名首次出现括注**；title/H1 与文件名（即全批引用名）不一致时改偏离方。
- 审查维度：技术硬伤（ali-oss 链路、ECharts/ExcelJS、H5 防重）· 代码块与源码一致性（函数/字段/类型名逐一对照）· 可编译性与语言标签 · 六段结构与互链 · 去 AI 味
- 结论口径：【合格】= 无 P0/P1（可附 P2 建议）；【需修】= 存在 P0/P1。只出报告，未改任何文件。

---

## 〇、残留复查（对齐 scan6 / review-eng-b / review-b5-p4 已修点）

| 检查项 | 结果 |
|---|---|
| A3 MouseSensor/distance:2（18-4） | 无回潮：L11「MouseSensor 与 closestCenter」、L41「激活约束 `distance: 2`……不是每 2 像素周期性重判」均正确 |
| A4 trackUndo（18-5） | 无回潮：L75 用 `trackUndo`，描述与 `useStoreComponents.ts:16-22` 一致 |
| A5 getQuestionComponentValueField / defaultChecked | 20-6 已全部正确（L51/L60）；**20-8 仍残留同源错误**（`getQuestionComponentValueFeed` ×2、`defaultCheckbox` ×2），本次正式上报并入 20-8 条目 1 |
| A8 `/local/...` 旧路由 | 19-5（L17/L36/L70）、20-2（L23/L39）、20-6（L30/L58）已修无回潮；**19-4、20-3、20-4、20-7、20-8 仍残留**（scan6 清单外已列，本次正式上报，见共性簇一） |
| A10 17-1 模块目录/公共模块名 | 无回潮：L27 `src/utils/modules`、`redis.module.ts`、`wechat-login-tool.module.ts` 均正确 |
| review-b5-p4 簇二命名策略 | 本批沿用；发现教学期命名残留集中在 18-1~18-3、18-5、19-2~19-5、20-1（见各篇条目） |
| review-eng-b 风险 #4/#6/#19（发布保留问卷数据、ip+ua 防重、防重复提交） | P5 各篇涉及 ip+ua 防重（20-1/20-3/20-4/20-7/20-8）均**未加口径限定**，本次以 P2 上报（簇八）；「发布保留问卷数据」口径本批未涉及 |
| transcript 残留 / 拓展运算符 | 0 处（grep 证实）；「扩展运算符」为系列既有用法（03/04 期同款未改），不计入问题 |

---

## 一、共性簇（跨篇问题，逐篇条目只留指针）

### 簇一：`/local/...` 旧路由与旧接口名残留（scan6 清单外，正式上报，P1）

最终仓库为 `@Controller('low_code')` + snake_case 路径（`release_with_user` / `is_question_data_posted` / `question_data` / `get_question_data_by_id`），全局前缀 `api`，client 侧封装于 `api/low-code.ts`。残留清单：

| 篇 | 位置 | 现状 | 应为 |
|---|---|---|---|
| 19-4 | L37 | 「封装在 `api/local` 中，路径为 `local/release`」 | `api/low-code`，`POST /api/low_code/release` |
| 19-4 | L60 | `GET /local/releaseWithUser` | `GET /api/low_code/release_with_user` |
| 19-4 | L69 | `POST /local/release` | `POST /api/low_code/release` |
| 19-5 | L35/L36 | 「api/local 中定义」「`getLocalPage()`」 | `api/low-code`；函数名 `getLowCodePage()` |
| 19-5 | L39 | 「控制器中的 `releaseWithUser`」 | 控制器方法名 `getReleaseDataWithUser` |
| 20-3 | L23/L43/L47 | `LocalController`、`isQuestionDataPost`、`GET /local/isQuestionDataPost` | `LowCodeController`；`is_question_data_posted`（方法名 `isQuestionDataPosted`）；`GET /api/low_code/is_question_data_posted?page_id=3` |
| 20-4 | L23/L43/L49 | `LocalController`、路径 `questionDataPost` | `LowCodeController`；路径 `question_data`（方法名 `postQuestionData` 正确） |
| 20-7 | L26/L48 | `GET http://127.0.0.1:3006/api/local/isQuestionDataPost?pageId=` | `${NEXT_PUBLIC_API_BASE_URL}/low_code/is_question_data_posted?page_id=` |
| 20-8 | L42/L63 | `http://127.0.0.1:3006/api/local/questionDataPost` | `${NEXT_PUBLIC_API_BASE_URL}/low_code/question_data` |

### 簇二：教学期命名 vs 最终仓库命名（P2，沿用 b5 簇二策略：改以 SRC 为准 + 首次括注）

| 博客写法 | SRC 实名 | 涉及篇 |
|---|---|---|
| `UploadEditorChoiceInput` | `UploadEditOrChooiseInput`（LowCodeComponents/utils/components.tsx） | 18-1、18-2 |
| `LowResource` | `LoadResource` | 18-2、18-3 |
| `onChoice` / `handleChoice` | `onChooise` / `handleChooise` | 18-1、18-2 |
| `itemExpandIndex` / `setItemExpandIndex` | `itemsExpandIndex` / `setItemsExpandIndex` | 18-3（另见 18-2 的 `itemsExpandIndex` 使用语境） |
| `useComponentKeepPlace` | `useComponentKeyPress`（hooks/useComponentKeypress.ts） | 18-5 |
| `isDraggable` | `isDragable`（EditorCanvas.tsx） | 18-4 |
| `showToolBar` | `showToolbar` | 18-6 |
| `ifReach` / `setIfRefresh` | `refrash` / `setRefrash`（源码即此拼写） | 18-7、18-8 |
| `ActiveCanvas` / `ActiveCanvasToolbar` | `EditorCanvas` / `EditorChooiseToolbar` | 18-8 |
| `generatorComponent` | `generateComponent` | 19-3（14-8 同簇判例） |
| `localStorageInstall` | `localStorageInStore` | 19-2 |
| `saveDraft` | `storeInLocalStorage`（Center.tsx） | 19-3 |
| `readDataFromLocal` | `localStorageInStore` | 19-5 |
| `componentConfigs` / `sortableComponentConfig` / `currentComponentConfig` / `copyComponentConfig` | `compConfigs` / `sortableCompConfig` / `currentCompConfig` / `copyedCompConig` | 18-5、18-4（store.components 语境）、19-2、19-3、19-4、19-5 |
| localStorage key：`componentConfig` / `storeTime` / `releaseTime` | `compConfig` / `store_time` / `release_time` | 19-2、19-4（与 14-1 已建立的 store_time/release_time 口径一致） |
| `userId` / `accountId` / `pageId` / `configId` / `pageName` / `dsc` | `account_id` / `account_id` / `page_id` / `page_id` / `page_name` / `desc` | 17-2、17-4、17-5、19-4、19-5、20-1、20-2、20-3、20-4、20-8 |
| 服务端返回字段 `title` / `description` | Page 列 `page_name` / `desc`（前端 updatePage 里才映射成 title/description） | 19-5、20-2 |
| store 组件结构字段 `options` | client store 内是 `props`（后端列才是 options） | 19-5（18-2/20-6 语境正确） |
| `textarea` / `text`（组件 type） | `textArea` / `titleText` | 20-6、20-8 |
| `ResourceEntity` / `ResourceModule` / `ResourceService` / `ResourceRequest` / `DeleteResourceRequest` | `Resources` / `ResourcesModule` / `ResourcesService` / `ResourcesRequest` / `DeleteResourcesRequest` | 17-2、17-4、17-5 |
| `@User()` | `@getUserMess()`（GetUserMessTool） | 17-2、17-4、17-5 |
| `EditHeader` / `edit/head` 目录 | `EditorHeader` / `pages/Editor/Header/` | 19-1 |
| `FlowButton` | antd `FloatButton` | 19-3 |
| `setExpose` / `isPost` | `setIsPosted` / `isPosted` | 20-7、20-8 |
| `resourceApi` | `request` 封装（api/resource.ts），无此对象 | 18-3 |

### 簇三：标题 / H1 与文件名（= 全批引用名）不一致（改偏离方）

| 篇 | 实际 title/H1 | 引用名（引用方） | 建议 | 严重度 |
|---|---|---|---|---|
| 18-1 | 低代码项目平台编辑模块**：**前端资源上传逻辑开发 | 《…—前端资源上传逻辑开发》（17-5、18-2、18-3） | 冒号改破折号 | P2 |
| 18-4 | 低代码项目平台编辑模块**：**页面组件拖拽排序功能开发 | 《…—页面组件拖拽排序功能开发》（8 处） | 冒号改破折号 | P2 |
| **18-6** | **编辑器工具栏《上》：用 IntersectionObserver 控制显隐与定位** | 《低代码项目平台编辑模块—页面组件工具栏功能开发《上》》（18-3、18-5、18-7、18-8 共 5 处） | title/H1 改为引用名 | **P1** |
| 18-7 | 低代码项目平台编辑模块**：**页面组件工具栏功能开发《下》 | 《…—页面组件工具栏功能开发《下》》（18-5、18-6、18-8） | 冒号改破折号 | P2 |
| 19-2 | 低代码项目平台编辑模块**：**页面头部草稿功能开发 | 《…—页面头部草稿功能开发》（19-1、19-3、19-4、19-5） | 冒号改破折号 | P2 |

其余 21 篇 title/H1 与文件名一致；P5 内互链 42 个引用名经全库 title 检索全部命中真实篇目（含 03/04/06 期跨期引用），无死链。

### 簇四：`代码（已8期）/...` 配套资料路径在协作工作区不存在（P2）

`work/source/25.xiaodi-lowcode/` 下只有 `course-reference/lowcode-platform-full`（无任何「已8期」阶段代码目录）。涉及：18-1（L77/L109）、18-2（L81）、18-3（L62）、18-4（L23/L70）、18-5（L15/L23）、18-6（L80）、18-7（L84/L97/L116）、18-8（L92）、19-1（L52）、19-2（L56/L77）、19-3（L15）、19-4（L63）、20-1（L58，`笔记+资料-已8期/…pdf`、`图.drawio`）、20-5（L31）。建议统一改为「课程配套代码/资料」泛指，或删除具体路径；保留路径会误导读者检索。

### 簇五：deps 块缺 `@ant-design/icons`、build 脚本 `tsc && vite build`（P2，沿用 b5 14-6 判例）

- 18-1（L80-94）、18-3（L76-90）、18-6（L83-94）、19-1（L66-84）：deps 块均缺 `@ant-design/icons`（本节均已使用图标：上传按钮、删除图标、工具栏三图标、CheckOutlined/EditOutlined）。
- 18-3（L72）、19-1（L62）：`"build": "tsc && vite build"` → 最终仓库 client 为 `"build": "vite build"`。

### 簇六：ip+ua 防重口径未加限定（P2，对齐 review-eng-b 风险 #6/#19）

20-1（L45/L64）、20-3（L11/L30/L48）、20-4（L11/L51）、20-7（L29）、20-8（L63）把「IP+设备加密 → 同一设备不可重复提交」写成既成事实。源码是 `MD5(ip + ua)`（SecretTool + GetUserIp/GetUserAgent），`main.ts` 未设 `trust proxy`：nginx 反代后 `request.ip` 恒为网关 IP（同 UA 互挤、换 UA 可绕）。建议在其中一篇（20-3 最合适）加一句口径注：「单机直连下有效；经 nginx 反代需配 trust proxy 与 X-Forwarded-For，否则判定失真」，其余篇目互链即可。

### 簇七：textarea/text 组件 type 名（P2）

`20-6`（L47/L51/L53/L60）、`20-8`（L23/L32/L37/L60/L61）：`textarea` → `textArea`；`20-6` L53 类型清单中的 `text` → `titleText`（b5 风险 #17）。`getQuestionComponentValueField` 的分支值 `text/defaultRadio/defaultChecked` 本身正确。

### 簇八（建议）：`release_with_user` 现状注（P2，参照 b5 14-5 条目 6）

19-5（L21-L28、L63-65）与 20-2（L23）把「编辑器从服务端恢复」描述为可用链路。最终仓库 `low-code.controller.ts:28` 实现为 `getReleaseData(null, user)` → `findOneBy({ id: null, ... })` 恒空（review-eng-b P0-7），`readDataFromServer` 里 `Object.keys(undefined)` 会抛错，编辑器实际依赖 localStorage 草稿。建议 19-5 加一句现状注（参照 scan6 A2-1 对 30-6 的处理方式），20-2 可互链。

---

## 二、逐篇明细

### 17-1.低代码项目平台编辑模块—阿里云_OSS_资源上传配置 — 需修

1. 【P1】L136-139 代码块：原句 `url.replace(/https:\/\/.*?\.oss-cn-[a-z]+-[\d]\.aliyuncs\.com/, customDomain)`
   → 该正则**匹配不了它自己 L130 给的示例 URL**（`oss-cn-guangzhou` 中没有 `-数字` 段，`[a-z]+-[\d]` 永不命中，replace 成空操作）。SRC（ali-oss.module.ts L11-13）按配置拼正则：`new RegExp(\`http[s]?:\\/\\/(?:${aliOssConfig.bucket})\\.(?:${aliOssConfig.region})(?:\\.aliyuncs\\.com)\`)`。建议代码块改为 SRC 式「bucket+region 拼 RegExp」，或至少写成能命中示例的 `/https:\/\/[^.]+\.oss-[a-z-]+\.aliyuncs\.com/`；顺带把示例 URL 的 `/fs/qd.png` 路径改成与 `upload_files/` 约定一致。
2. 【P2】L31-50 动态模块代码块为教学简化版（`private static aliOss` + `'ALI_OSS'` token + `@Global()` 装饰器）→ SRC 是实例式：`constructor(options) { this.alioss = new AliOss(options) }`，`forRoot(options)` 返回 `providers: [{ provide: AliOssModule, useValue: new AliOssModule(options) }]`、无 `@Global()` 装饰器（global 写在返回对象里）。教学写法可保留，建议加注「最终仓库为实例式 forRoot，注入的是 AliOssModule 实例本身」。
3. 【P2】L60-67 `aliOssOptions` → SRC `config.ts` 导出名是 `aliOssConfig`（且五项全部来自 env：region 默认 `oss-cn-hangzhou`，bucket/OSS_DOMAIN 由环境变量注入；「local-is」「16web.net」为讲师环境值，建议括注）。
4. 【P2】L105/L110/L113 「`upload-files`」→ SRC 对象 key 前缀是 `upload_files`（下划线）；17-2/17-3 同簇。
5. 【P2】L118-120 代码块 `await this.aliOss.put(...)` 后顺序写 `fs.unlinkSync(localTempPath)`，与「无论成功失败都删除」的表述不符（put 抛错则不删）→ SRC 用 `.finally(() => { unlinkSync(localPath) })`，建议对齐。
6. 【P2】L77 「`express.multipart.file`」→ 类型名是 `Express.Multer.File`。

### 17-2.低代码项目平台编辑模块—阿里云_OSS_资源上传接口开发 — 需修

1. 【P1】字段簇：L30 表格 `userId`、L83 service、L115 小结 → SRC `resources` 表字段为 `id / url / account_id / type / name`（resources.entity.ts），`userId` 不存在；save 块应为 `{ url, type, account_id, name }`。
2. 【P1】路由簇：L57 「`POST /resource/upload`」、L99 Apifox → SRC `@Controller('resources')` + `@Post('upload')` + 全局前缀 api，即 `POST /api/resources/upload`；模块/实体名为复数 resources（簇二）。
3. 【P1】L86-92 service 代码块：`const url = this.aliOss.uploadToAliOss(file)` 缺 `await`（url 是 Promise，下一行 `.replace` 直接运行时报错）；且域名替换发生在 `uploadToAliOss` 内部（SRC ali-oss.module.ts L63，17-1 也是这么讲的），service 里不应再 replace 一次。建议改为：
   ```ts
   const url = await this.aliOss.uploadToAliOss(file); // 已在模块内替换为自有域名
   const name = Buffer.from(file.originalname, 'latin1').toString('utf8');
   await this.resourceRepo.save({ url, type, account_id, name });
   return { msg: '上传成功' };
   ```
4. 【P2】L43 `MulterModule.register({ dest: './upload-temp' })` → SRC `{ dest: '__temps__' }`；且 ali-oss 模块从 `resolve('./__temps__/${file.filename}')` 取文件，两处路径必须一致。
5. 【P2】L91 `{ message: '上传成功' }` → `{ msg: '上传成功' }`（统一响应契约 `{code,data,msg}`）。
6. 【P2】L70-73 控制器块：`@User()` → `@getUserMess()`；`user: { id: string }` → `TCurrentUser`（id 为 number）。
7. 【P2】L62 `ResourceRequest` / `DeleteResourceRequest` → `ResourcesRequest` / `DeleteResourcesRequest`（share/types/request/resources.ts）。
8. 【P2】L83/L103 `upload-files` → `upload_files`（同 17-1 簇）。

### 17-3.低代码项目平台编辑模块—阿里云_OSS_资源删除配置 — 合格（附 P2 建议）

1. 【P2】L31/L34/L51 `customDomain` → SRC 配置变量名 `aliOssDomain`（`url.replace(aliOssDomain, '')`），建议括注。
2. 【P2】L31 示例 URL 的 `upload-files` → `upload_files`（簇）。

（204 判定、decodeURI、`deleteFromAliOss` 方法名、异常文案「删除失败，请重试」均与 SRC 逐字一致。）

### 17-4.低代码项目平台编辑模块—阿里云_OSS_资源删除接口开发 — 需修

1. 【P1】L69 代码块：原句 `await this.resourceRepo.delete({ id, userId: accountId });`
   → `accountId` 在该方法签名（`delete(id, userId)`）里**未定义**，块内自相矛盾；且 SRC 字段是 `account_id`。改为 `await this.resourcesRepository.delete({ id, account_id });`。
2. 【P1】L11 导语「接口先校验登录与资源归属，再串联…」与 SRC 相反：`deleteResource` 只校验登录与资源存在性，归属条件 `account_id` 在**最后删库一步**、且在删 OSS 之后（review-eng-b P0-4 IDOR：先删 OSS 后验归属，可越权删他人文件）。建议改为「先校验登录与资源存在性」，并补一句教学注：「源码把归属校验放在删库一步、晚于删 OSS，严格说存在越权删文件隐患（先验归属再删 OSS 才是安全顺序）」——与 #5 风险清单口径一致。
3. 【P1】路由簇：L27 `@Delete('resource/:id')`（注释「或 /resource?id=xxx，按课程实现为准」含糊）、L80 「`DELETE /resource`」→ SRC `@Delete()` 无子路径，即 `DELETE /api/resources?id=xxx`（Query 传 id，与 L81 的 Apifox 描述一致）。
4. 【P2】L30 `DeleteResourceRequest` → `DeleteResourcesRequest`；L37/L86 「resource 表」→ `resources` 表。
5. 【P2】L28 `@UseGuards(AuthGuard)` → 最终仓库为 APP_GUARD 全局守卫 + `@Public()` 白名单（与 b5 14-3 口径注一致）。
6. 【P2】L31/L41 `@User()` / `ResourceService.delete(id, userId)` → `@getUserMess()` / `deleteResource(id, account_id)`。

### 17-5.低代码项目平台编辑模块—阿里云_OSS_资源获取接口开发 — 需修

1. 【P1】字段簇：L51 代码块 `where: { type, userId: accountId }`、L56、L66、L72 → `account_id`（`findBy({ type, account_id })`）。
2. 【P1】路由簇：L32 `@Get('resource')`、L80 小结 → SRC `@Get()` 无子路径，即 `GET /api/resources?type=image`。
3. 【P2】方法名 `getResource` ×4（L25/L34/L38/L46）→ SRC 控制器/服务层均名 `getResources`。
4. 【P2】L33 `@UseGuards(AuthGuard)` 口径注（同 17-4）；L36 `@User()` → `@getUserMess()`。

### 18-1.低代码项目平台编辑模块：前端资源上传逻辑开发 — 需修

1. 【P1】L28/L113 「`UploadEditorChoiceInput`」→ SRC 组件名 `UploadEditOrChooiseInput`（LowCodeComponents/utils/components.tsx），读者按文中名检索会落空。
2. 【P2】L69-73 api 表与 L73 续句：SRC `api/resource.ts` 三个方法为 `uploadFile`（POST /resources/upload，FormData）、`getResources`（GET /resources，Query 传 `type`）、`deleteResource`（DELETE /resources，Query 传 `id`）——获取/删除都是 **Query 参数**而非「路径带类型/资源 ID」；「上传与删除的路径参数一致，都是『类型 + 资源标识』」不成立（上传是 type+file 表单体，删除只有 id）。建议按 SRC 重写该表。
3. 【P2】L33 「`listOptions`（含 `defaultValues`、`listItem` 等）」→ SRC `listOptions` 仅两键：`keyName?` 与 `defaultValues`；`listItem` 是 ListComponentProps 里赋给 `defaultValues` 的变量名，不是字段。
4. 【P2】L45/L121 `getResource` → `getResources`；L57 `loadingVisible` → SRC `loadingWithUpload`。
5. 【P2】L35 「父组件 `FormItem`」→ `FormPropLabel`（b5 14-9 同簇）。
6. 【P2】L80-94 deps 块缺 `@ant-design/icons`（簇五）；「定义在 `utils components` 里」→ `LowCodeComponents/utils/components.tsx`。
7. 【P2】L77/L109 `代码（已8期）` 路径（簇四）。
8. 【P2】标题断链（簇三第 1 行）：title 冒号 → 破折号。

### 18-2.低代码项目平台编辑模块—前端资源获取逻辑开发 — 需修

1. 【P1】命名簇（簇二前 3 行）：`UploadEditorChoiceInput` ×4（L11/L23/L29/L85）、`LowResource` ×3（L31/L65/L88）、`onChoice`/`handleChoice` ×4（L11/L33/L35/L86）→ 依次 `UploadEditOrChooiseInput` / `LoadResource` / `onChooise` / `handleChooise`。
2. 【P2】L40-48 示意块：`updateListComponent({ keyName, value: src })` 不存在。SRC `handleChooise` 是两分支：`props[keyName]` 为 undefined 时 `updateCurrentComponent({ [keyName]: [{ ...defaultValues, [propName]: url }] })`（先建数组），否则 `updateCurrentCompConfigWithArray({ key, field: propName, index: store.itemsExpandIndex, value: url })`。文中已有「以工程源码为准」免责，建议把两个真实方法名写进括注。
3. 【P2】L43/L87 「keyName：图片 image、视频 video」→ SRC 实际取值：轮播 `images`、单/多选 `options`、List 未传（默认 `items`）；「image/video」与源码不符。
4. 【P2】L71 「整理成 `{ code, message, data }`」→ `{ code, msg, data }`；「服务层在包装响应数据时」→ 全局拦截器 `ResponseIntercept`（server/src/common）。
5. 【P2】L32/L86 `listOption` → `listOptions`；L35 `FormItem` → `FormPropLabel`；L81 `代码（已8期）` 路径。
6. 【P2】L73-77 Bearer 注：SRC 是在 `useStoreAuth` 的 `login` action 里 `storeAuth.token = \`Bearer ${token}\``（useStoreAuth.ts L13），文中「useStore 里 auth hooks」建议写准为 `useStoreAuth`；示例变量 `authorization` 源码无此名（机制描述正确）。

### 18-3.低代码项目平台编辑模块—前端资源删除逻辑开发 — 需修

1. 【P1】store 字段簇：`itemExpandIndex` ×5（L11/L43/L47/L50/L105/L112）、`setItemExpandIndex`（L48）→ SRC `itemsExpandIndex` / `setItemsExpandIndex`（store/components.ts L9、useStoreComponents.ts L92）。L52 刚提醒「少一个 s 会导致取不到值」，本篇自己恰好少了一个 s。
2. 【P1】L49 「`useStoreComponent` 这个自定义 hook」→ `useStoreComponents`。
3. 【P2】L21/L109 `LowResource` → `LoadResource`（同 18-2 簇）。
4. 【P2】L31 「传入 `coverImage` / `image` 等参数」→ SRC CardComponentProps 是 `propName="coverImg"`（与 b5 15-5 同簇）；「image」无对应参数。
5. 【P2】L23/L105 「底层走 `resourceApi.delete`」「axios 封装 `resourceApi`」→ 源码无 `resourceApi` 对象，`deleteResource(id)` 内部走 `request('/resources', { params: { id }, method: 'DELETE' })`。
6. 【P2】L32/L111 `listOption` → `listOptions`。
7. 【P2】L72 `"build": "tsc && vite build"` → `"vite build"`；L76-90 deps 缺 `@ant-design/icons`（簇五）。
8. 【P2】L62 `代码（已8期）` 路径（簇四）。

### 18-4.低代码项目平台编辑模块：页面组件拖拽排序功能开发 — 需修

（A3 已修点无回潮；dnd-kit 三层结构、scaleY 正则、closestCenter、arrayMove 链路与 SRC 一致。）

1. 【P2】L52/L58/L83 `isDraggable` → SRC 变量名 `isDragable`（EditorCanvas.tsx L274，源码拼写如此）。
2. 【P2】L63-67 代码块 `store.components = arrayMove(store.components, ...)` → SRC `storeComponents.sortableCompConfig = arrayMove(storeComponents.sortableCompConfig, oldIndex, newIndex)`（且在 `action` 内，非 `runInAction`）；已有「结构对应视频演示」括注，建议把字段名换成 SRC 名。
3. 【P2】L21 「画布里选中多个组件后，可把某个组件向上/向下移动一位」→ 编辑器是单选模型（同时只有一个选中组件），改「画布里渲染多个组件后」。
4. 【P2】L60 整句加粗「**所有拖拽动作，最终都被转换成数组里两个索引的位置交换**」→ 只加粗关键词（簇三）。
5. 【P2】标题断链（簇三第 2 行）：title 冒号 → 破折号；L23/L70 `代码（已8期）` 路径。

### 18-5.低代码项目平台编辑模块—页面组件键盘操作功能开发 — 需修

（A4 已修点无回潮：L75 `trackUndo` 描述与 SRC 一致。）

1. 【P1】L21/L85 「`useComponentKeepPlace`（在 `editCanvas` 中执行）」→ SRC hook 名 `useComponentKeyPress`（hooks/useComponentKeypress.ts），调用处在 `pages/Editor/EditorCanvas.tsx` L299。
2. 【P1】L62-66 粘贴代码块 `store.componentConfigs[id] = { ...copied.props, id };` 与上句「先整体拷贝一份配置」矛盾，且与 SRC 不符：`pasteCopyedComponent` 是整份配置深拷贝后重排 id——`const comp = { ...JSON.parse(JSON.stringify(storeComponents.copyedCompConig)), id: ulid() }; storeComponents.compConfigs[comp.id] = comp;`（存 `{id,type,props}` 完整结构）。按博客写法存进去的条目缺 `type`，画布渲染直接失败。
3. 【P2】簇二：`sortableComponentConfig` ×4（L15/L43/L51）、`componentConfigs`（L52）、`currentComponentConfig`（L66）、`copyComponentConfig`（L58）→ `sortableCompConfig` / `compConfigs` / `currentCompConfig` / `copyedCompConig`。
4. 【P2】L39 「通过 `getCurrentComponent` 取…若为 `none` 就提示」→ SRC `validateComponent` 用 `getCurrentComponentConfig.get() !== null` 判空，提示文案「请先选择组件」；「getCurrentComponent」应为 `getCurrentComponentConfig`。
5. 【P2】L73 整句加粗「**必须先有撤销，才有可重做的步骤**」→ 只加粗关键词（簇三）。
6. 【P2】L15/L23 `代码（已8期）` 路径（簇四）。

### 18-6.低代码项目平台编辑模块—页面组件工具栏功能开发《上》（现题《编辑器工具栏《上》：用 IntersectionObserver 控制显隐与定位》） — 需修

1. 【P1】标题断链（簇三第 3 行）：title/H1 与文件名及 5 处引用名《低代码项目平台编辑模块—页面组件工具栏功能开发《上》》完全不一致（b5 对 14-9/15-6/16-4 同型问题判 P1）。改 title/H1，一处修复全部引用。
2. 【P2】L38/L102/L110 `showToolBar` → SRC `showToolbar`（editor.tsx/EditorCanvas.tsx）。
3. 【P2】L74 「来自 `componentList` 配置数组」→ SRC ComponentList.tsx 导出名为 `components`（`export const components = [...]`，每项 type/name/icon 与文中一致）。
4. 【P2】L44 「所有组件属性数组」→ `compConfigs` 是「ID → 配置」对象字典（Record），非数组。
5. 【P2】L83-94 deps 块缺 `@ant-design/icons`（本节已渲染删除/上移/下移三图标，簇五）；L80 `代码（已8期）` 路径（簇四）。

### 18-7.低代码项目平台编辑模块：页面组件工具栏功能开发《下》 — 需修

1. 【P2】L22 图标名 `DeleteOutline`、`UpOutline`、`DownOutline` → SRC `DeleteOutlined` / `UpOutlined` / `DownOutlined`（少 ed 后缀，照抄会 import 失败）。
2. 【P2】L22 `EditChoiceToolbarIconContainer` → SRC `EditorChooiseToolbarIconContainer`；L26 「`moveUp`、`moveDown`」→ `moveUpComponent` / `moveDownComponent`。
3. 【P2】L33-50 `ifReach` 强制刷新机制描述与 SRC 一致（`isFirst` + `refrash` 双 state 驱动 useEffect 重跑），建议括注源码名 `refrash`/`setRefrash`（源码即此拼写）。
4. 【P2】标题断链（簇三第 4 行）：title 冒号 → 破折号。
5. 【P2】L84/L97/L116 `代码（已8期）` 路径（簇四）。

（两段 deps 块分别与根 package.json、client package.json 核对无误；IntersectionObserver root/threshold/disconnect 清理描述与 EditorChooiseToolbar 一致。）

### 18-8.低代码项目平台编辑模块—页面组件滚动时工具栏的显隐开发 — 需修

1. 【P2】防抖时长：L11/L43-57/L96/L98 写「200ms」→ SRC editor.tsx `setTimeout(..., 300)`（300ms；源码注释写「30ms」与代码自相矛盾，博客宜如实写 300 并可括注该注释瑕疵）。
2. 【P2】L64/L78 `ActiveCanvas` / `ActiveCanvasToolbar` → `EditorCanvas` / `EditorChooiseToolbar`；L82/L85/L100 `setIfRefresh` → `setRefrash`（簇二）。
3. 【P2】L90 useTitle 文案「小滴课堂低代码平台页面编辑页」→ SRC `useTitle("小滴低代码平台 - 页面编辑")`（editor.tsx L10）。
4. 【P2】L34-38 代码块与 editor.tsx 结构一致（含 cleanup removeEventListener + clearTimeout），但源码 handleScroll 是 `if (scrolling) clearTimeout(...)`（条件清除），示意块为无条件清除——机制等效，可不动；L92 `代码（已8期）` 路径（簇四）。

### 19-1.低代码项目平台编辑模块—页面头部动态标题开发 — 合格（附 P2 建议）

1. 【P2】L27/L104 `EditHeader` / 「`edit/` 下新建的 head 目录」→ `EditorHeader` / `pages/Editor/Header/`（簇二）。
2. 【P2】L62 `"build": "tsc && vite build"` → `"vite build"`；L66-84 deps 缺 `@ant-design/icons`（CheckOutlined/EditOutlined 本节在用，簇五）。
3. 【P2】L52 `代码（已8期）` 路径（簇四）。

（store/page.ts 的 `setPageTitle`、Left.tsx 双态切换、`publicProps` 展开写法均与源码逐字对得上；「扩展运算符」为系列既有用法。）

### 19-2.低代码项目平台编辑模块：页面头部草稿功能开发 — 需修

1. 【P1】L62 「页面初始化时执行 `localStorageInstall`」→ SRC 方法名 `localStorageInStore`（useStoreComponents.ts L245）；「外层 Edit 父组件」→ `Editor`（editor.tsx useEffect 调用，属实）。
2. 【P2】localStorage key 簇：L37/L48-50 `componentConfig` → `compConfig`；L52/L58 `storeTime` / `releaseTime` → `store_time` / `release_time`（SRC useStoreComponents.ts L235-239、Center.tsx L30；与 14-1 已核实的「谁新读谁」口径保持一致）。
3. 【P2】L40-53 代码块 `store.components.componentConfigs` 双重嵌套不存在：SRC 是 `useStoreComponents().store` 即 storeComponents 本体，直接 `storeComponents.compConfigs` 等（簇二变量名同步修正）。
4. 【P2】L69 整句加粗「**存草稿是 store → localStorage，恢复草稿是 localStorage → store**」→ 只加粗关键词（簇三）。
5. 【P2】L11 「是low-code 平台最不能忍」→ 「是 low-code 平台」（补空格）；L56/L77 `代码（已8期）` 路径；标题断链（簇三第 5 行）：title 冒号 → 破折号。

### 19-3.低代码项目平台编辑模块—页面头部预览功能开发 — 需修

1. 【P1】写缓存函数名三处两种写法且都不对：L34 代码块 `saveDraft();`、L41 「`saveDraft()` 对应…『将组件储存在本地缓存中』函数」、L88 小结「调 `localStorageInStore()` 写缓存」→ SRC（Center.tsx L39）是 `storeInLocalStorage()`；`localStorageInStore` 是**读取**函数，L88 属张冠李戴。三处统一为 `storeInLocalStorage`。
2. 【P2】`generatorComponent` ×4（L11/L75/L81/L91）→ `generateComponent`（EditorCanvas.tsx L27 导出，preview.tsx 复用；b5 14-8 同簇）。
3. 【P2】L62 「`FlowButton`」→ antd `FloatButton`；L43 「与 `edit`、`index`、`login`、`register` 同级」→ `editor`、`index`、`loginOrRegister`（pages 目录实名）。
4. 【P2】L71-78 代码块签名 `({ store }: { store: TStoreComponents })` → SRC `PreviewCanvas` 无 props，内部 `useStoreComponents()` 自取；`sortableComponentConfig` → `sortableCompConfig`。
5. 【P2】L23 整句加粗「**预览功能本身包含了草稿功能**」→ 只加粗关键词（簇三）；L15 `代码（已8期）` 路径。

### 19-4.低代码项目平台编辑模块—页面头部发布功能开发 — 需修

1. 【P1】`/local` 路由簇残留（簇一，scan6 清单外正式上报）：L37 「封装在 `api/local` 中，路径为 `local/release`」、L60 `GET /local/releaseWithUser`、L69 `POST /local/release` → `api/low-code`、`POST /api/low_code/release`、`GET /api/low_code/release_with_user`（与 scan6 A8-1 对 19-5 的修法一致）。
2. 【P2】L33/L60/L68 `dsc` → `desc`（b5 14-4 同簇笔误）；`pageName` → `page_name`；tdk 语义：「`tdk`（标题、描述、关键字）」不准确——SRC Page 列里 `tdk` 是关键字列、`desc` 是描述列、标题是 `page_name`（GlobalFields 三个独立字段 title/description/tdk），建议改为「`desc`（页面描述）、`page_name`（标题）、`tdk`（关键字）」。
3. 【P2】L50 `releaseTime` → `release_time`（与 19-2/14-1 口径，簇二）。
4. 【P2】L53 「组件存入 localStorage 时会自动执行一次『存草稿』操作」语义不通，且 L61 「发布成功后会自动执行一次存草稿」与 SRC 矛盾：Center.tsx onSuccess 只做 nav + 写 `release_time` + message.success，**不调 storeInLocalStorage**；若发布真自动存草稿，`store_time > release_time`，19-2 的「谁新读谁」判定反而失效。建议改为「发布成功只记录 release_time；刷新后若草稿时间早于发布时间则自动转服务端读取」。
5. 【P2】L15 簇二 store 变量名；L60 `pageId=3`、`accountId=8` → `page_id` / `account_id`；L63 `代码（已8期）` 路径。

### 19-5.低代码项目平台编辑模块—页面组件服务端获取开发 — 需修

（scan6 A8-1 已修点无回潮：L17/L36/L70 路径正确。）

1. 【P1】簇一残留：L35 「api/local 中定义」、L36 `getLocalPage()`、L39 「控制器中的 `releaseWithUser`」→ `api/low-code`；函数名 `getLowCodePage()`（api/low-code.ts L16）；控制器方法名 `getReleaseDataWithUser`（low-code.controller.ts L28）。
2. 【P2】L16/L25 `readDataFromLocal` → `localStorageInStore`（读取方法实名；readDataFromServer 名字正确）。
3. 【P2】L43/L45/L48/L71 簇二：`componentConfigs` / `sortableComponentConfig` → `compConfigs` / `sortableCompConfig`；L43 「包含 id、type 以及 options」→ store 元素结构是 `{ id, type, props }`（`props: cur.options ?? {}`，与 15-2「store 字段是 props」口径一致）。
4. 【P2】L59/L73 「服务端…返回 title、description、tdk…用户 ID、页面 ID」→ SRC 返回的是 `objectOmit(lowCode, ['components'])` 展开的 `page_name / desc / tdk / account_id / id`；前端 `updatePage({ tdk, title: data.page_name, description: data.desc })` 完成映射。建议按 SRC 列名表述并括注前端映射。
5. 【P2】建议补现状注：`release_with_user` 在最终仓库传 null 恒空（review-eng-b P0-7），「已自动从服务器读取数据」分支实际不可用，编辑器依赖草稿恢复（簇八；参照 14-5 的处理方式）。

### 20-1.低代码项目发布页面—需求分析 — 需修

1. 【P1】L41-46 component_data 字段清单 → SRC（low-code.entity.ts L45-61）只有 `id / page_id / user / props`：`componentId` **列不存在**（组件 id 存于 `props` 数组每项的 `{ id, value }` 中，即提交时组装的 item.id）；`pageId` → `page_id`；`userKey` → `user`（值 = `MD5(ip + ua)`）。建议按 SRC 四列重写并补一句「组件 ID 在 props[i].id 里，不在表列上」。
2. 【P2】L26/L54 「把返回的 HTML URL 转成 JSON 后在编辑平台内嵌渲染」→ SRC client release.tsx 是 `<embed type="text/x-scriptlet" src={url}>` 直接内嵌 URL，无 JSON 转换环节（转写残留表述）。
3. 【P2】L58 `笔记+资料-已8期/全栈低代码平台需求文档.pdf`、`图.drawio` 在工作区不存在（簇四），建议泛指。
4. 【P2】L45 「用户 IP + 设备」建议括注 SRC 实现：`GetUserIp()` + `GetUserAgent()`（User-Agent）拼接后 MD5（簇六口径注挂本篇或 20-3）。

### 20-2.低代码项目发布页面—后端接口低代码组件获取 — 合格（附 P2 建议）

（scan6 A8-2 已修点无回潮：L23/L39 路径正确。无 P1。）

1. 【P2】L31 「若 `id` 为空则按 `user.id` 查，若 `user.id` 为空则按页面 `id` 查」→ SRC 无该分支：固定 `findOneBy({ id, account_id: user?.id })`，undefined 字段被 TypeORM 忽略从而实现「只传 id / 只传 user」两种形态。
2. 【P2】L35/L47 返回字段 `title` / `description` → `page_name` / `desc`（同 19-5 条目 4）。
3. 【P2】L41 `pageId` / `accountId` → `page_id` / `account_id`（簇二）。
4. 【P2】建议补现状注（簇八）：C 端接口 `id` 无校验、不带 id 时 TypeORM 空条件会返回表中第一行（review-eng-b P2#2）；`release_with_user` null bug 见 19-5。

### 20-3.低代码项目发布页面—是否有提交过问卷后端接口 — 需修

1. 【P1】接口名簇（簇一）：L23/L47 `LocalController` / `isQuestionDataPost`、L43 `GET /local/isQuestionDataPost`、传 `id=3` → `LowCodeController`；路径 `is_question_data_posted`（方法名 `isQuestionDataPosted`）；`GET /api/low_code/is_question_data_posted?page_id=3`（Query 参数也是 `page_id`，L25 `configId` → `page_id`）。
2. 【P2】L26 「设备信息」→ `GetUserAgent()` 取 User-Agent；L47 小结「接收配置 ID、IP、设备信息」同步为「page_id、IP、User-Agent」。
3. 【P2】簇六：建议本篇挂防重口径注（单机直连有效；反代需 trust proxy + XFF）。
4. 【P2】L39 提示文案「问卷已提交，感谢参与」→ SRC「您已提交过问卷，感谢您的参与」（ComponentRender.tsx L97）。

（`!!` 转布尔、查到 true/查不到 false、按 key+page_id 查 component_data 均与 SRC 一致。）

### 20-4.低代码项目发布页面—后端接口提交问卷信息 — 需修

1. 【P1】接口名簇（簇一）：L23/L43/L49 `LocalController`、路径 `questionDataPost` → `LowCodeController`、`question_data`（SRC `@Post('question_data')`，方法名 `postQuestionData` 文中写对了）。
2. 【P2】`configId` ×3（L32/L45/L51）、`pageId` ×3（L26/L44/L49）→ `page_id`（PostQuestionDataRequest = `Pick<IComponentData, "page_id" | "props">`；L28 IComponentData 属性清单里的 `pageId` 同步）。
3. 【P2】L28 「入参类型 `IComponentData`」建议括注：实际入参类型是 `PostQuestionDataRequest`（Pick 子集），IComponentData 是表实体类型。
4. 【P2】簇六口径注；可补一句 SRC 现状「props 原样入库、无大小/结构校验」（review-eng-b P1-13，教学注可选）。

### 20-5.低代码项目发布页面—前端_Nextjs_项目初始化 — 合格（附 P2 建议）

1. 【P2】L45 「默认端口 3001」→ `next dev` 默认 3000（3001/3002 是课程自选端口，建议改述）。
2. 【P2】L29 「执行 `pnpm --filter release` 关联公共包」表述不完整——实际是 `pnpm --filter @lowcode/release add @lowcode/share` 之类的安装动作。
3. 【P2】L43 「`page.css`」→ App Router 脚手架是 `globals.css` + `page.module.css`；L31 `代码（已8期）` 路径（簇四）。

（AntdRegistry 包裹 layout、@ant-design/nextjs-registry 适配、`@lowcode/release` 命名均与 SRC release 包一致。）

### 20-6.低代码项目发布页面—获取页面渲染 — 合格（附 P2 建议）

（scan6 A5-1/A5-2/A8-3 已修点无回潮：`getQuestionComponentValueField`、`defaultChecked`、`/api/low_code/release?id=` 均正确。无 P1。）

1. 【P2】L23 「访问 `/release/3`」→ SRC 动态路由是根级 `app/[id]/page.tsx`，访问 `/<id>`（如 `/3`），无 `/release` 前缀（client release.tsx 的 `VITE_RELEASE_BASE_URL/${id}` 拼接亦证实）。
2. 【P2】簇七：`textarea` → `textArea`（L47/L51/L53/L60）；L53 类型清单 `text` → `titleText`。
3. 【P2】L30-35 代码块硬编码 `http://127.0.0.1:3006` → 建议括注 SRC 用 `process.env.NEXT_PUBLIC_API_BASE_URL`（构建期注入，release/.env.example）。
4. 【P2】L37 「用 `!` 断言数据存在」与 SRC `toJson.data!` 一致；补一句 SRC 还有 `res.ok` / `!toJson.data` 双重抛错（文中已提 res.ok，属实）。

### 20-7.低代码项目发布页面—前端项目检查是否提交问卷 — 需修

1. 【P1】接口簇（簇一）：L26 注释块与 L48 小结 `GET http://127.0.0.1:3006/api/local/isQuestionDataPost?pageId=` → `${NEXT_PUBLIC_API_BASE_URL}/low_code/is_question_data_posted?page_id=${data.id}`（SRC ComponentRender.tsx L87-89）。
2. 【P2】L23 「用 `axios` 的 `useRequest` 封装」→ `useRequest` 来自 ahooks，且 SRC 此处用的是原生 `fetch`（非 axios）。
3. 【P2】L37 `setExpose` → SRC `setIsPosted`；提示文案对齐「您已提交过问卷，感谢您的参与」。
4. 【P2】L29 `pageId = data.id` → `page_id`；簇六口径注。

（非 manual 自动请求、置灰三件套 select-none/pointer-events-none/降透明度均与 SRC 一致。）

### 20-8.低代码项目发布页面—发布页面提交问卷 — 需修

1. 【P1】scan6 A5 同源残留（正式上报）：L17/L29 `getQuestionComponentValueFeed` ×2 → `getQuestionComponentValueField`；L29/L37 `defaultCheckbox` ×2 → `defaultChecked`（SRC ComponentRender.tsx L38）。
2. 【P1】提交路径簇（簇一）：L42 代码块 `fetch('http://127.0.0.1:3006/api/local/questionDataPost', ...)`、L63 小结 → `${NEXT_PUBLIC_API_BASE_URL}/low_code/question_data`；body `{ pageId: data.id, props }` → `{ page_id: id, props }`（SRC 用的是 props.id 字符串，L45 正文 `pageId` 同步）。
3. 【P2】L39 「注意路径中的下划线」在现路径 `questionDataPost` 下自相矛盾（驼峰无下划线）——按上条改为 `question_data` 后即自洽，顺带核对该句。
4. 【P2】L54/L63 `isPost` → `isPosted`；L56 `configId=3` → `page_id=3`；簇七 `textarea` → `textArea`（L23/L32/L37/L60/L61）。
5. 【P2】L33 「请填写完整的问卷信息」→ SRC「请填写完整问卷信息」；L56 成功提示 SRC 为「提交成功！感谢您的参与！」（文中「感谢您的参与」为节选，可接受，建议写全）。
6. 【P2】簇六口径注（「整页置灰防重复提交」的判定边界同 20-3）。

（按钮显隐 some 判断、完整性校验排除 radio/checkbox、`{id, value}` 组装、成功/警告分支逻辑均与 SRC 一致。）

---

## 三、统计

| 项 | 数量 |
|---|---|
| 总篇数 | 26 |
| 合格（含附 P2 建议 3 篇：17-3、19-1、20-5；另 20-2、20-6 合格附建议） | **5** |
| 需修 | **21** |
| P0 | 0 |
| P1 | 24（硬伤集中于：`/local` 路由与旧接口名残留 9 篇（簇一）；字段/函数/组件名与 SRC 不符 9 处（17-1 正则、17-2 userId+await、17-4 删库块+导语归属、17-5 userId、18-1/18-2 组件名、18-3 itemsExpandIndex+useStoreComponent、18-5 hook 名+粘贴块、19-2 localStorageInstall、19-3 saveDraft、19-5 api/local、20-1 componentId、20-8 Feed/defaultCheckbox）；标题整体断链 1 处（18-6）） |
| P2 | 71（命名簇约 28、标题标点变体 4、资料路径不存在 14 篇、deps/build 块 6、防重口径注 5、useTitle/端口/表述精度约 8、整句加粗 4、其余细节） |

需修优先级建议：

1. **先修簇一 `/local` 路由残留**（19-4、19-5、20-3、20-4、20-7、20-8 共 6 篇 15 处）——与 scan6 A8 已修篇目口径对齐，一次批量替换可完成（`/local/isQuestionDataPost`→`/api/low_code/is_question_data_posted?page_id=`、`questionDataPost`→`question_data`、`releaseWithUser`→`release_with_user`、`api/local`→`api/low-code`、`getLocalPage`→`getLowCodePage`、`LocalController`→`LowCodeController`）。
2. **再修「照着写会对不上源码」的命名/结构 P1**：18-6 标题断链；17-1 正则、17-2 userId+await、17-4 删库块与归属顺序、17-5 userId、18-1/18-2 UploadEditOrChooiseInput/LoadResource/handleChooise、18-3 itemsExpandIndex、18-5 useComponentKeyPress+粘贴块、19-2 localStorageInStore、19-3 storeInLocalStorage、20-1 component_data 四列、20-8 Feed/defaultCheckbox。
3. **簇二命名统一**（snake_case 字段 + 教学目录别名括注）与**簇三标题标点**（18-1/18-4/18-7/19-2 冒号改破折号）可一次批量处理。
4. **簇四资料路径、簇五 deps/build、簇六防重口径注**属系列级卫生项，可与第六期（21-x 数据统计/Excel 导出）审稿合并批量执行，避免两期口径不一。
