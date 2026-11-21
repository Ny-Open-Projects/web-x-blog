# 审稿 B7-P6：06.第六期（25 篇）专家复核报告

- 审稿对象：`work/target/25-lowcode/posts/06.第六期/`（21-1~21-10、22-1~22-5、23-1~23-6、24-1~24-4，共 25 篇）
- 真源对照（SRC）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`——本批重点核对 `packages/server/src/low-code/low-code.{controller,service}.ts`、`packages/client/src/pages/dataCount.tsx`、`pages/DataCount/{ComponentDatas,DataSource,ComponentSelect}.tsx`、`pages/release.tsx`、`api/low-code.ts`、`utils/excel.ts`、`store/page.ts`、`pages/Editor/Header/Right.tsx`、`server.Dockerfile`、`release.Dockerfile`、`server.nginx.Dockerfile`、`release.nginx.Dockerfile`、`nginx/{server,release}.nginx.conf`、`docker-compose.yml`、根 `package.json`、各子包 `package.json`
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`、`reports/review-eng-b.md`（表述风险清单）、`reports/review-b5-p4.md` 与 `reports/review-b6-p5.md`（判例与口径）
- 命名口径：沿用 b5/b6 裁定——**API / 类型 / 字段 / 文件名一律以最终仓库（SRC）为准，教学期别名首次出现括注**；`/local/` 旧路由簇一律上报；title 必须与文件名一致，整体偏离报 P1、标点/空格变体报 P2。
- 审查维度：技术硬伤（统计接口、ECharts、防重逻辑、发布页渲染链、Docker 链路）· 代码块与源码一致性（函数/字段/类型名逐一对照）· 可编译性与语言标签 · 六段结构与互链真实 · 去 AI 味
- 结论口径：【合格】= 无 P0/P1（可附 P2 建议）；【需修】= 存在 P0/P1。只出报告，未改任何文件。

---

## 〇、残留复查（对齐 scan6 / review-eng-b / b5 / b6 已修点）

| 检查项 | 结果 |
|---|---|
| A3 MouseSensor / A4 trackUndo / A5 Feed/defaultChecked | 本批不涉及拖拽/撤销/提交链路，grep 证实 0 处残留 |
| A8 `/local/...` 旧路由（scan6 清单外残留） | 19-4/19-5/20-3/20-4/20-7/20-8（第五期）之外，**本批 21-3/21-4/21-5/21-7/21-8/22-3 又出现 6 篇**（`LocalController`、`api/local`、`local/questionnaireData`、`local/getQuestionDataById`），见簇一，本次正式上报 |
| A9 `component_data` 四列 / `ILowCode` / `titleText` | 本批 20-1 相关口径未被推翻；21-2/21-8 对 `component_data` 的描述（props 内 `{id,value}`、`user` 匿名标识）与 SRC 一致 |
| b6 簇七 textarea/text 组件 type 名 | **21-3、22-2、22-3 三篇沿用 `textarea`**（SRC 为 `textArea`），见簇二 |
| b6 簇四 `代码（已8期）` 资料路径 | **本批 10 篇 14 处继续出现**，且 7 处目录名重复为「代码（已8期）/代码（已8期）」，见簇四 |
| b5/b6 簇二 snake_case 策略 | 21-x 后端三篇仍有 `accountId`/`pageId` 残留（代码块 1 处、正文多处），见簇二 |
| review-eng-b 风险 #4/#6/#19（发布保留问卷数据、ip+ua 防重） | 本批 21-x 统计链路正确呈现「按组件 ID 查 props」，未触碰「防重」口径；无冲突表述 |
| transcript 类转写残留 | `transcript` 0 处；**24-4 出现「任务包」「materials」两处制作流程残留词**（见 24-4 条目 2） |

互链总体结论：P6 全批 43 个《》引用名，除指向本批 title 偏离篇目（23-1/23-5/24-1，见簇三）外，全部能在 00~07 期文件名/标题中命中真实篇目，无死链；21-x/22-x 内部互链与「下一步」链条完整成环（21-1→…→22-5→23-1→…→24-4→25-1/25-2）。

---

## 一、共性簇（跨篇问题，逐篇条目只留指针）

### 簇一：`/local/...` 旧路由与 `LocalController` 残留（scan6 清单外，正式上报，P1，6 篇）

最终仓库为 `@Controller('low_code')` + snake_case 路径 + 全局前缀 `api`，统计三接口为 `GET question_components` / `GET question_data` / `POST get_question_data_by_id`，client 侧封装于 `api/low-code.ts`。残留清单（修法与 b6 簇一批量替换一致）：

| 篇 | 位置 | 现状 | 应为 |
|---|---|---|---|
| 21-3 | L11 / L23 | 「在 `LocalController` 中新增」 | `LowCodeController`（low-code.controller.ts） |
| 21-3 | L49 | 小结「`GET /question_components`」 | `GET /api/low_code/question_components` |
| 21-4 | L23 | 「在 `LocalController` 中新增 `questionData`」 | `LowCodeController`；路径 `question_data`，控制器方法名 `getQuestionData` |
| 21-5 | L23 / L51 | 「在 `LocalController` 中新增 `getQuestionDataByIdRequest`」 | `LowCodeController`；`POST /api/low_code/get_question_data_by_id` |
| 21-7 | L23 | 「封装于 `api/local`，底层 axios 请求 `local/question_components`」 | `api/low-code`，`/low_code/question_components` |
| 21-8 | L23 | 「（路径 `local/questionnaireData`）」 | **路径名整体不存在**：`/low_code/question_data`（api/low-code.ts `getQuestionData`） |
| 22-3 | L17 | 「对应路径类似 `local/getQuestionDataById`，POST 请求」 | `POST /api/low_code/get_question_data_by_id`（POST 说法正确） |

### 簇二：教学期命名 vs SRC 命名（P2，沿用 b5/b6 策略：改以 SRC 为准 + 首次括注）

| 博客写法 | SRC 实名 | 涉及篇 |
|---|---|---|
| `textarea`（组件 type 枚举值） | `textArea`（low-code.service.ts `In([...])`、IComponent 枚举） | 21-3（L29/L35/L50）、22-2（L26/L29）、22-3（L11/L32/L93） |
| `accountId` / `pageId` | `account_id` / `page_id` | 21-3（L34 代码块，P1；L43）、21-4（L30）、21-5（L11/L52）、21-7（L33） |
| 「`get-user-message` 装饰器」 | `getUserMess`（GetUserMessTool） | 21-3（L17/L23） |
| `isInput`（含语义取反） | `isMore`（DataSource.tsx：radio/checkbox 为 true） | 22-3（L26-30 及全文） |
| `getQuestionDataById` | `getQuestionDataByTypeRequest`（api/low-code.ts；share 类型名恰为 `getQuestionDataByIdRequest`） | 22-3（L69） |
| `pieData` / `columnOptions` / `cloneData` | `data` / `currentOptions` / `currentData`（DataSource.tsx） | 22-4（L63-69、L74-80） |
| `getBarOptions` | `getTopOptions` | 22-5（L23/L26/L34） |
| `setCurrentSelect` / `defaultId` / `currentSelect` | `setCurrnetSelected`（源码即此拼写）/ `currentSelected`（值为组件对象，另传 `currentSelected?.id ?? 0`） | 22-2（L36-47，代码块部分并入该篇 P1） |
| 「父组件 `DataCount`」 | 组件名 `Statistics`（dataCount.tsx export default） | 22-2（L33） |
| `EditHeader` | `EditorHeader`（pages/Editor/Header/） | 21-6（L23） |
| `nav('edit')` | `nav("/editor")` | 21-6（L29） |
| `store.pageTitle` | `store.title`（store/page.ts） | 22-3（L44，并入该篇 P1） |
| `generateText` | `generatorTexts` | 22-3（L43） |

### 簇三：title / H1 与文件名不一致（互链引用名全部按文件名书写，改偏离方一处即修复全部引用）

| 篇 | 实际 title/H1 | 全批引用名（引用方） | 建议 | 严重度 |
|---|---|---|---|---|
| **23-1** | **Dockerfile 入门：把三个项目打包成可运行的镜像** | 《项目部署上线—构建自定义镜像的利器 Dockerfile》（22-5、23-2、23-3、23-4、24-1 共 5 处） | title/H1 改为文件名形式 | **P1** |
| 23-2 | 项目部署上线**：**构建自定义镜像 Dockerfile 的配置介绍 | 《项目部署上线—构建自定义镜像Dockerfile的配置介绍》（23-1、23-3、23-4、23-5 共 4 处） | 冒号改破折号、去空格 | P2 |
| **23-5** | **项目部署上线：构建前端发布 Next.js 镜像的 Dockerfile 配置** | 《项目部署上线—构建前端发布Nextjs镜像的Dockerfile配置》（23-2、23-4、23-6、24-2 共 4 处） | title/H1 改为文件名形式（冒号 + `Next.js`→`Nextjs` + 去空格） | **P1** |
| 23-6 | 项目部署上线—构建前端 **N**ginx 镜像的 Dockerfile 配置（多空格、大写 N） | 《项目部署上线—构建前端nginx镜像的Dockerfile配置》（23-4、23-5、24-1 共 3 处） | 去空格、小写 nginx | P2 |
| **24-1** | **Docker Compose 入门：一条命令编排多个容器** | 《项目部署上线—运行容器Docker-compose的介绍和使用》（23-3、23-4、23-5、23-6、24-2、24-3 共 6 处） | title/H1 改为文件名形式 | **P1** |
| 24-2 | 项目部署上线**：**Docker Compose 运行多容器的配置 | 《项目部署上线—Docker-compose运行多容器的配置》（23-6、24-1、24-3、24-4 共 4 处） | 冒号改破折号、`Docker Compose`→`Docker-compose` | P2 |

其余 19 篇 title/H1 与文件名一致。

### 簇四：`代码（已8期）/...` 配套资料路径在协作工作区不存在（P2，10 篇 14 处，沿用 b6 簇四）

`work/source/25.xiaodi-lowcode/` 下只有 `course-reference/lowcode-platform-full`，无任何「已8期」阶段目录；且 21-10 L17、22-1 L16、23-4 L50、23-5 L42/L59、23-6 L15、24-2 L22/L80/L98、24-4 L63 七处把目录写成重复的「代码（已8期）/代码（已8期）」。涉及：21-6（L42）、21-9（L17）、21-10（L17）、22-1（L16）、23-3（L55/L78）、23-4（L50）、23-5（L42/L59）、23-6（L15）、24-2（L22/L80/L98）、24-4（L63）。建议统一改为「课程配套代码/资料」泛指或删除具体路径。

### 簇五：整句加粗（P2，沿用 b5 簇三）

- 23-5 L63：「**需要服务端运行的（server、release）进容器，纯静态的（client）进 OSS**」（整句加粗 → 只加粗关键词）
- 24-2 L55：「**Dockerfile 构建出来的是镜像，Docker Compose 运行起来的是容器**」（同上）
- 24-3 L53：「**DevOps 就是开发 + 测试 + 运维的交集**」（同上）

### 簇六（建议）：部署链路现状注缺失（P2）

SRC 部署链的三个关键事实在本批叙述中缺位，建议在 24-2（修 compose 块时一并处理）加口径注、其余篇互链：(1) nginx conf 的 upstream 指向 `host.docker.internal:5001/4001`，靠 compose `extra_hosts: host-gateway` 解析（23-6 L40、24-2 compose 块均未提，24-2 因此缺行，见该篇 P1）；(2) compose 无 MySQL/Redis 服务（宿主机自装，review-eng-b P1-16），24-1 L88「容器名、环境变量（密码）」与 24-4 L43「Redis 镜像」宜加限定；(3) nginx conf `X-Forwarded-For $remote_addr` 为覆盖式写法、未设 trust proxy（review-eng-b P0-3/P1-14 关联），23-4 L43「其余保持默认即可」宜如实列举。

---

## 二、逐篇明细

### 21-1.编辑页面渲染Nextjs发布页面—编辑页面渲染Nextjs发布页面 — 合格（附 P2 建议）

（发布回调 `release?id=` 路由、`useLocation`+`replace` 取参、antd `QRCode`、`nav(-1)` 均与 SRC release.tsx / Center.tsx 一致；互链 4 个目标全部存在。）

1. 【P2】L30 代码块 `<embed type="text/html" …>` → SRC 用 `type="text/x-scriptlet"`（IE 时代类型，review-eng-b P2#16）。教学写 `text/html` 更规范可保留，建议括注「最终仓库为 text/x-scriptlet，现代浏览器下二者表现等价」，与 20-1 的既有口径呼应。
2. 【P2】L33 「url 拼接为：`http://localhost:3001/` + 页面 ID」→ SRC 为 `${import.meta.env.VITE_RELEASE_BASE_URL}/${id}?forceUpdate=1`（release.tsx L10-12）。建议括注环境变量与 `?forceUpdate=1` 防缓存参数。
3. 【P2】L23 「与 `preview`、`index`、`edit`、`login`、`register` 同级」→ SRC pages 目录实名 `editor`、`index`、`loginOrRegister`、`preview`、`release`、`dataCount`（b6 19-3 条目 3 同簇）。
4. 【P2】L37 「否则 Next.js 路由 `/release/3` 收不到正确参数」→ Next 动态路由是根级 `app/[id]/page.tsx`，实际访问 `/3`，无 `/release` 前缀（b6 20-6 条目 1 同源；本篇 L15 恰好引用 20-6，口径应一致）。

### 21-2.后台数据统计模块—页面需求分析+接口分析 — 合格（附 P2 建议）

（左右两栏结构、三个接口及登录鉴权要求、radio/checkbox 才能聚合、component/component_data 分工，与 SRC 控制器/service 及 dataCount 页完全对应；互链 3 个目标存在。）

1. 【P2】L47 配套资料「`笔记+资料-已8期/全栈低代码平台需求文档.pdf`、`图.drawio`」不存在（簇四），建议泛指。

### 21-3.后台数据统计模块—后端接口获取问卷组件开发 — 需修

1. 【P1】（簇一）L11/L23 「`LocalController`」×2、小结 L49 「`GET /question_components`」→ `LowCodeController`；路径补全 `GET /api/low_code/question_components`（SRC `@Controller('low_code')` + `@Get('question_components')`）。
2. 【P1】L34-36 代码块：原句 `this.componentRepository.find({ where: { accountId: user.id, type: In(['input', 'textarea', 'radio', 'checkbox']) }, });`
   → SRC（low-code.service.ts `getQuestionComponents`）为 `findBy({ account_id: user.id, type: In(['input', 'textArea', 'radio', 'checkbox']) })`。三处偏差：`accountId`→`account_id`；**`'textarea'`→`'textArea'`（枚举值按文中写法查不到文本域组件，属功能性错误，非拼写洁癖）**；`find`→`findBy`（与 SRC 一致）。正文 L29 与小结 L50 的 `textarea` 同步。
3. 【P2】L17/L23 「`get-user-message` 装饰器」→ `getUserMess`（簇二）。
4. 【P2】L23/L28 「服务层方法 `getQuestionComponents(user.id)`」→ SRC 控制器传整个 `user`（`getQuestionComponents(user)`），service 内取 `user.id`，建议写准。
5. 【P2】L43 「含 `type`、`pageId`、`accountId`、`options` 等」→ `page_id`/`account_id`（簇二）。

### 21-4.后台数据统计模块—后端接口获取问卷组件内容开发 — 需修

1. 【P1】（簇一）L23 「在 `LocalController` 中新增 `questionData`」→ `LowCodeController`；接口路径 SRC 为 `question_data`、控制器方法名 `getQuestionData`，建议写实（本篇通篇未给路径）。
2. 【P1】L37-46 代码块结构与 SRC 不符且与本文自述矛盾：原句
   ```ts
   const result = await Promise.all(
     componentDatas.map(async (item) => {
       const componentResult = await this.componentRepository.findOne({ where: { id: item.id } });
       return { type: componentResult.type, options: componentResult.options?.options ?? null };
     })
   );
   ```
   → 外层 map 的 `item` 是 `component_data` 行（其 `id` 是提交记录主键，不是组件 ID），**缺内层 `comp.props` 遍历**——与本文 L31「对其中每个组件项用 `item.id`」和小结「数组包裹数组」直接矛盾；返回缺 `result: item`（下篇 21-8 L31 明确依赖 `{ result: { id, value }, type, options }` 结构）；兜底 SRC 为 `|| {}` 非 `?? null`；`findOne({ where })` → SRC `findOneBy({ id: item.id })`。按 SRC `getQuestionData` 重写：
   ```ts
   const matchesComponetDatas = await Promise.all(
     componentDatas.map(async (comp) => await Promise.all(
       comp.props.map(async (item) => {
         const componentResult = await this.ComponentRepository.findOneBy({ id: item.id });
         return { result: item, type: componentResult?.type, options: componentResult?.options?.options || {} };
       }),
     )),
   );
   ```
3. 【P2】L30 「按 `pageId`」→ `page_id`（簇二）。

### 21-5.后台数据统计模块—后端接口通过ID获取某个问卷组件内容开发 — 需修

1. 【P1】（簇一）L23 「在 `LocalController` 中新增 `getQuestionDataByIdRequest`，`POST` 请求」、小结 L51 → `LowCodeController`；建议写实路径 `POST /api/low_code/get_question_data_by_id`（SRC `@Post('get_question_data_by_id')`；「POST」判断正确，予以保留）。
2. 【P2】L23 「调用同名服务层方法」→ SRC 控制器方法名 `getQuestionDataByTypeRequest`、服务层 `getQuestionDataByIdRequest`，并非同名；API 客户端函数名也是 `getQuestionDataByTypeRequest`。建议括注。
3. 【P2】L11/L52 「`pageId`」→ `page_id`（簇二）。
4. 【P2】L38 「若不是数组，用 `[]` 包裹成数组」、小结 L53 「非数组则 `[]` 包裹」→ SRC 为包成**单项数组** `[item.value]`，且前置 null 分支（`item.value == null` 时返回 null）。建议改写为「非数组包成 `[item.value]`，null 保持 null」，避免读者误以为是塞进空数组。

（filter 按 `item.id === id` 筛选、options 来自 `component.options.options` 输入型为 null、flat 降维、id=337/339/340 联调示例均与 SRC 一致。）

### 21-6.后台数据统计模块—前端页面布局开发 — 合格（附 P2 建议）

（`/dataCount` 路由、头部「后台数据统计」按钮 + LineChartOutlined、左右两栏、导出双按钮预留、disable 置灰思路均与 SRC dataCount.tsx / Header/Right.tsx 对应。）

1. 【P2】L23 「`EditHeader`」→ `EditorHeader`（簇二）。
2. 【P2】L29 标题「小滴课堂低代码平台数据统计」→ SRC「小滴低代码平台数据统计」；「`nav('edit')`」→ `nav("/editor")`（簇二）。
3. 【P2】L36 置灰「opacity 降低 + 鼠标事件禁用 + 灰色背景」→ SRC 仅 `opacity-50 select-none pointer-events-none`，无背景变更（视觉显灰来自底色），建议删「灰色背景」。
4. 【P2】L42 配套依赖路径（簇四）。

### 21-7.后台数据统计模块—用户表格数据表头开发 — 需修

1. 【P1】（簇一）L23 「（封装于 `api/local`，底层 `axios` 请求 `local/question_components`）」→ `api/low-code`、`/low_code/question_components`（全局前缀 api）。
2. 【P2】L26 提示文案「请至少创建一个表单组件」→ SRC「请先创建至少一个表单组件」（dataCount.tsx message.warning）。
3. 【P2】L31 「`pages/dataCount` 目录下」→ 子组件在 `pages/DataCount/`（大写 D），父组件是 `pages/dataCount.tsx`，建议写准。
4. 【P2】L33 「`pageId`」→ `page_id`（簇二）。
5. 【P2】L36-40 代码块：`item.options?.title ?? '默认标题'` → SRC `item.options.title ?? "默认展示的标题"`（SRC 无可选链、兜底文案不同），建议对齐或括注。

### 21-8.后台数据统计模块—用户表格数据内容开发 — 需修

1. 【P1】（簇一，且路径名整体错误）L23 「用 `useRequest` 请求 `getQuestionData`（路径 `local/questionnaireData`）」→ `questionnaireData` 在 SRC 不存在；实际为 `api/low-code.ts` 的 `getQuestionData` → `/low_code/question_data`。改「封装于 `api/low-code`，请求 `GET /api/low_code/question_data`」。
2. 【P1】L42-44 radio/checkbox 取值链描述漏掉关键映射，照写会显示 ID 而非选项文本：原句三步「radio/checkbox 若 value 为空 → 给默认值『选项一』」「checkbox 的 value 是数组 → 用 `join(',')` 转成逗号分隔字符串」「数字类型兜底转字符串」
   → 存储值是**选项 ID**；SRC（ComponentDatas.tsx onSuccess）三步实为：空值 → `item.options[0].value`（无 options 才兜底字符串「选项1」，非「选项一」）；数组 → 先 `item.options.find(option => option.id === v)?.value` 把每个 ID 映射回选项文本，**再** `join(',')`；单值（radio 数字 ID）→ 同样按 ID 查选项文本（不是「转字符串」）。建议整段按 SRC 重写，否则读者实现的表格出现「339/340」而非「男/按摩」。
3. 【P2】L26 提示「还未有用户提交数据」→ SRC「还未有用户提交数据哦」（微）。
4. 【P2】L52 key 冲突归因建议写准：SRC reduce 展开顺序使每行 `key` 都被 `...pre` 覆盖为第一个组件 ID（337），Table 行 key 重复告警；「多条记录各自带 337/338…」表述含糊。

### 21-9.后台数据统计模块—用户表格数据导出Excel — 合格（附 P2 建议）

（ExcelJS `^4.4.0` 与 client package.json 一致；`jsonToExcel` 参数表、`generateHeader` 的 `{header,key,width}` 映射、`defaultRowHeight=20`、`isWriteFile` 缺省 true、`addRows` 直写均与 SRC excel.ts / ComponentDatas.tsx 逐字对得上。）

1. 【P2】L17 配套资料路径（簇四）。

### 21-10.后台数据统计模块—用户表格数据导出Excel《下》 — 合格（附 P2 建议）

（writeBuffer → Blob(`application/octet-stream`) → `createObjectURL`/`download`/`click`/`revokeObjectURL` 下载链与 SRC saveFile/saveFileWithBlob 一致；Blob 数组包裹、isWriteFile 分支描述正确。）

1. 【P2】L17 配套资料路径且目录重复「代码（已8期）/代码（已8期）」（簇四）。
2. 【P2】L30 「`Workbook.XLSX.writeBuffer()`」→ `workbook.xlsx.writeBuffer()`（小写 xlsx；L33 代码块本身正确，正文用词改齐）。
3. 【P2】L34 代码块 `` saveFile(buffer, `${title}数据统计.xlsx`) `` → SRC `` `${title}-数据统计.xlsx` ``（少连字符）；L88 示例文件名「小滴课堂低代码开发页面数据统计.xlsx」同（且 SRC store.title 默认值是「小滴低代码开发页面」，无「课堂」二字）。
4. 【P2】L44 `function saveFile(buffer: ArrayBuffer, …)` → SRC 为 `async function saveFile(buffer: any, …)`（调用处 await）；示意可保留，建议括注。

### 22-1.后台数据统计模块—用户表格数据导出Excel压缩包 — 合格（附 P2 建议）

（「复用生成、isWriteFile=false、JSZip 产 Blob、复用 saveFileWithBlob」思路与 SRC handleExportZip/excelToZip 一致；`jszip ^3.10.1` 与 package.json 一致。）

1. 【P2】L16 配套资料路径且目录重复（簇四）。
2. 【P2】L34-38 调用块 `const buffer = await jsonToExcel(data, { isWriteFile: false }); excelToZip(buffer, title);` → SRC 两个函数都是**单 options 对象**入参：`jsonToExcel({ columns, dataSource, title, isWriteFile: false })`、`excelToZip(excel)`（excel = `{ buffer, title }`，由 jsonToExcel 返回）。文中块内部自洽但与 SRC 签名不同，建议对齐或括注。
3. 【P2】L52 `` zip.file(`${title}数据统计.xlsx`, buffer) `` → SRC `` jszip.file(`${title}.xlsx`, buffer) ``（title 已含「-数据统计」后缀，来自 jsonToExcel 返回值）。
4. 【P2】L67 「如果你在 Windows 上，系统自带的是 `.rar` 解压能力，但 JSZip 生成的是 `.zip`，装一个 ZIP 解压工具即可正常打开」→ **事实写反**：Windows 10/11 自带 ZIP 解压（双击即可），RAR 才需要装第三方工具（WinRAR 等）。建议整句改为「Windows 自带 ZIP 解压可直接打开；若想产出 RAR 才需要另装工具」。

### 22-2.后台数据统计模块—动态输入型问卷组件开发 — 需修

1. 【P1】L36-41 JSX 块与 L43-47 入参释义：`<ComponentSelect components={components} setCurrentSelect={setCurrentSelect} defaultId={defaultId} />` → SRC（dataCount.tsx L49-52）props 为 `components` / `setCurrnetSelected`（源码即此拼写）/ `currentSelected`（传 `currentSelected?.id ?? 0`）；`setCurrentSelect`、`defaultId` 在源码不存在，读者按文中名检索/对参会落空（b5 15-2 FormPropLabel 入参同型判例）。
2. 【P1】L56-71 columns 块与 L80-87 dataSource 块：
   - `disabled={record.key === currentSelect?.id}` + `onClick={() => setCurrentSelect(record)}` → SRC `disabled={currentSelected === record.key}`、`onClick={() => setCurrnetSelectedComponent(record.component)}`（回传原组件而非行包装对象）；按文中写法 `currentSelect` 是行对象（只有 key/title/type/component，无 `.id`），disabled **永不生效**。
   - `title: item.title || '未命名组件'` → SRC `title: item.options.title ?? "默认展示的标题"`（IComponent 无顶层 title，标题在 `options.title`；照文中写法表头全部落到兜底文案）。Button 缺 `type="primary" size="small"` 可忽略。
3. 【P2】L26/L29 「textarea」→ `textArea`（簇七）。
4. 【P2】L33 「父组件 `DataCount`」→ SRC 组件名 `Statistics`；L26 「表格内容来自上一节请求回来的问卷组件数据」——「上一节」（22-1）是压缩包导出，组件数据实际在 21-7 的父组件请求，叙述顺一下。

### 22-3.后台数据统计模块—动态输入型用户数据开发 — 需修

1. 【P1】（簇一）L17 「对应路径类似 `local/getQuestionDataById`，POST 请求」→ `POST /api/low_code/get_question_data_by_id`（「POST」正确）。
2. 【P1】L80 请求触发机制与 SRC 相反：原句「因为父组件已传了默认选中项，首屏不用自动请求，故设 `manual: true`」→ SRC（DataSource.tsx）`useEffect(() => { currentSelected && execGetQuestionData(); }, [currentSelected])`：**首屏挂载即自动请求默认选中组件的数据**——这正是 21-2「默认展示第一个组件（姓名）的列表」与 22-2「保证首屏刷新就有内容展示」的落点；`manual: true` 只是禁用 useRequest 自动执行，真正触发靠 effect。建议改为「manual: true + useEffect 监听 currentSelected（含首屏）触发请求」，并补进「按 ID 重新请求接口」一节与 L90-94 数据流小结；否则照文中实现首屏空白，与前两篇自相矛盾。
3. 【P1】L44 代码块 `const pageTitle = store.pageTitle;` → SRC `store.title`（store/page.ts 只有 title/description/tdk，`store.pageTitle` 取值 undefined）；同块 `generateText` → SRC 函数名 `generatorTexts`。
4. 【P2】（簇七）L11/L32/L93 「textarea」→ `textArea`。
5. 【P2】（簇二）L26-30 `isInput` → SRC 变量名 `isMore`（语义相反：`isMore` 为 true 表示 radio/checkbox 图表型）；保留教学名需括注并说明方向相反。L69 `getQuestionDataById` → `getQuestionDataByTypeRequest`。L72-73 `onSuccess: (res) => { const data = res.map(…) }` → SRC `onSuccess: ({ data }) => …`（统一响应外层是 `{code,data,msg}`，按文中写法对响应对象直接 map 会报错）。L84 「简单类型直接 `{ id: number }` 即可」→ share 里实际有 `getQuestionDataByIdRequest = Pick<IComponent, "id">` 类型且 api 层已用，建议括注。
6. 【P2】L43-54 渲染示意（p/span、文案「的问卷填写信息」）与 SRC `generatorTexts`（`《{store.title}》问卷填写数据：`+「填写: 」前缀）为示意差异，可保留，建议括注。

### 22-4.后台数据统计模块—动态饼状图开发 — 合格（附 P2 建议）

（`echarts ^5.4.3` / `echarts-for-react ^3.0.2` 与 package.json 一致；`{name,value}` 格式、`result` 以选项 ID 计数、`itemTitle` 取 `options.title` 兜底、ReactECharts 只传 option、悬浮计数，均与 SRC getPieOptions 一致。）

1. 【P2】（簇二）L63-69 `pieData`/`columnOptions` → SRC `data`/`currentOptions`；L74-80 `cloneData`（「currentData 的副本」）→ SRC 直接遍历 `currentData`，且键写法是 `acc[id ?? ""]`（null 选项 ID 归到空串键）——文中代码缺 `?? ""`，与 L83「第一个选项无 ID 时 key 为空」的自述不一致，建议补上。
2. 【P2】L38 `title: { text: itemTitle }` → SRC 另有 `left: "center"`（示意可保留）。
3. 【P2】补一句数据来源：`currentOptions` 是 onSuccess 里 `isMore && setCurrentOptions(data[0].options.map(…))` 设置的——22-3 的简化版 onSuccess 没写这一步，两篇连读会让读者以为图表没有数据来源，建议在 22-3 或本篇补一句。

### 22-5.后台数据统计模块—动态横向柱状图开发 — 需修

1. 【P1】L34-53 配置块与 L59-61 要点把背景条机制写成了另一套实现，照写复现不了课程效果：原句「背景条：`showBackground: true` + `backgroundStyle` 把每条槽位铺成灰色 100%」「`xAxis: { max: 100 }`」「`legend: { data: [] }`」
   → SRC `getTopOptions` 的实现是：背景条为**第二个 bar 系列**（name「背景」、`barWidth: 20`、`barGap: "-100%"`、`data: Array.from({ length }).fill(100)`、色 `#ededed`）；X 轴为 `{ show: false, type: "value" }`（无 `max`）；**双 yAxis**——第二根 category 轴以 `formatter: "{value}%"` 显示百分比标签；`grid.left: "25%"`；series data 传 `{name,value}` 对象（tooltip 才能带分类名）。建议对齐 SRC，或明确标注「教学简化写法，源码为双系列背景条 + 双 Y 轴百分比」，并把函数名改 `getTopOptions`。
2. 【P2】（簇二）L23/L26 `getBarOptions` → `getTopOptions`（并入上条）。
3. 【P2】L68-69 `barNames`/`barValues` 两个派生数组 → SRC 是同一份 `{name,value}` 数据分别喂 `yAxis.data`（`data.map(item => item.name)`）与 `series.data`，建议括注。

### 23-1.项目部署上线—构建自定义镜像的利器_Dockerfile（现题《Dockerfile 入门：把三个项目打包成可运行的镜像》） — 需修

1. 【P1】title/H1 与文件名完全不一致（簇三第 1 行）：title/H1「Dockerfile 入门：把三个项目打包成可运行的镜像」vs 文件名《项目部署上线—构建自定义镜像的利器_Dockerfile》；全批 5 处互链按文件名书写（22-5 L83、23-2 L15、23-3 L15、23-4 L15、24-1 L15）。改 title/H1 为文件名形式，一处修复全部引用（b5 14-9/15-6/16-4、b6 18-6 判例）。

（内容本身无技术硬伤：三项目分工、「仓库/镜像/容器」三大核心、`docker build -t` 命令、Dockerfile 定义与赛车类比均可成立；互链 5 个目标全部存在。）

### 23-2.项目部署上线：构建自定义镜像 Dockerfile 的配置介绍 — 合格（附 P2 建议）

1. 【P2】title/H1 标点变体（簇三第 2 行）：冒号→破折号、去空格，与文件名对齐。
2. 【P2】L52-62 示意块（node:16-alpine / yarn / pm2 / EXPOSE 8081）已声明「不代表工程里的具体文件」，可保留；建议顺带一句「最终仓库 server.Dockerfile 为 node:18-alpine + pnpm、EXPOSE 3000」，与 23-3 衔接更顺。
3. 【P2】L43 「启动前端项目一般就是 `pnpm run dev`」→ 生产镜像语境下是 `pnpm start:release`（dev 仅本地开发），建议限定「本地开发时」。

### 23-3.项目部署上线—构建后端镜像的Dockerfile配置 — 需修

1. 【P1】L23 「在工程根目录新建一个 `Server.Dockerfile`。注意命名：**首字母 `Server` 要大写**，编辑器才能识别并显示 Docker 图标」、小结 L82 → SRC 文件名是 `server.Dockerfile`（前缀小写、后缀 `.Dockerfile` 大写 D）。「必须大写才能识别」不成立（SRC 即反例，23-4 也正确用了小写 `server.nginx.Dockerfile`）。改为 `server.Dockerfile` 并括注课程演示曾用大写。
2. 【P2】L28-42 代码块与 SRC 三处偏差：`FROM node:18` → SRC `node:18-alpine`；`COPY . .` → SRC `COPY . /app`；镜像源 SRC 是实际执行行 `RUN npm config set registry https://registry.npmmirror.com`，文中只作注释。块自称「真正能用的 Server.Dockerfile」，建议逐项对齐或括注「教学演示版」。
3. 【P2】L55/L78 配套资料路径（簇四）。

（scripts 块 L57-65 与根 package.json 逐字一致；`build:share` 先于 `build:server` 的顺序说明与 SRC 一致。）

### 23-4.项目部署上线—构建后端nginx镜像的Dockerfile配置 — 合格（附 P2 建议）

（`nginx:1.25.0-alpine` + `ADD nginx/server.nginx.conf → /etc/nginx/nginx.conf` + `EXPOSE 80` 与 SRC 逐字一致；upstream/weight/location/worker_connections 讲解正确；client package.json 块 L52-99 与 SRC 逐字一致；「部署阶段 build 是 vite build」与 b5 14-6 修后的口径一致。）

1. 【P2】L43 「其余保持默认即可」→ SRC conf 显式设置了 `X-Real-IP`、`X-Forwarded-For`、`Host`、`Upgrade/Connection` 等头（非默认值），且 XFF 用 `$remote_addr` 覆盖、后端未设 trust proxy（review-eng-b P0-3/P1-14 关联）；建议如实列出这几个头的作用，顺带一句反代场景 IP 失真的已知缺陷。
2. 【P2】L50 配套资料路径且目录重复（簇四）。
3. 【P2】L107 小结「`ADD ./nginx/server.nginx.conf …`」→ SRC 无 `./`（微）。

### 23-5.项目部署上线：构建前端发布 Next.js 镜像的 Dockerfile 配置 — 需修

1. 【P1】title/H1 与文件名不一致（簇三第 3 行）：冒号 + `Next.js` 拼写 + 空格，全批 4 处互链按文件名形式《项目部署上线—构建前端发布Nextjs镜像的Dockerfile配置》书写（23-2 L95、23-4 L114、23-6 L15、24-2 L16）。title/H1 改为文件名形式。

（指令序列 L31 与 SRC release.Dockerfile 逐项一致；scripts 块 L44-55 与根 package.json 一致；「只改 build:server→build:release、start:server→start:release」与 SRC diff 完全吻合。）

2. 【P2】L63 整句加粗「**需要服务端运行的（server、release）进容器，纯静态的（client）进 OSS**」→ 只加粗关键词（簇五）。
3. 【P2】L42/L59 配套资料路径且目录重复（簇四）。

### 23-6.项目部署上线—构建前端nginx镜像的Dockerfile配置 — 需修

1. 【P1】文件名与 SRC 不符：L11/L25/L27/L68 「`release.nginx.dockerfile`」（小写 d）、「`server.nginx.dockerfile`」→ SRC `release.nginx.Dockerfile` / `server.nginx.Dockerfile`（后缀大写 D；23-4 用对了，本篇统一）。
2. 【P2】L23 「每个容器各自监听 80 端口，互不冲突」→ server 与 release 容器 `EXPOSE 3000`（本系列 23-3/23-5 自己都写了），只有两个 nginx 容器监听 80；宿主机侧由 compose 映射 5001/5000/4001/4000。建议改写，避免与姊妹篇矛盾。
3. 【P2】L30 「不再 `COPY server.nginx.conf`，而是 `COPY release.nginx.conf`」→ SRC 两个 nginx Dockerfile 都用 `ADD`（23-4 讲的也是 ADD），指令名统一。
4. 【P2】L40 「配置里写的服务器 IP……一定要改成自己阿里云服务器的 IP」→ SRC conf 的 upstream 写的是 `host.docker.internal:4001`，靠 compose `extra_hosts: host.docker.internal:host-gateway` 解析到宿主机（簇六；本篇与 24-2 全未提 extra_hosts）。建议括注最终仓库写法，「换 IP」是课程原始版本的做法。
5. 【P2】L15 配套资料路径且目录重复（簇四）。

（release scripts 块 L55-63 与根 package.json 一致；四容器分工表正确。）

### 24-1.项目部署上线—运行容器Docker-compose的介绍和使用（现题《Docker Compose 入门：一条命令编排多个容器》） — 需修

1. 【P1】title/H1 与文件名完全不一致（簇三第 4 行）：全批 6 处互链按文件名书写（23-3 L90、23-4 L114、23-5 L75、23-6 L75、24-2 L15、24-3 L15）。title/H1 改为文件名形式。
2. 【P2】L88 「下一节会实际启动低代码平台的四个容器，把 restart（总是重启）、启动后的容器名、环境变量（密码）、宿主机与容器的端口映射逐项配齐」→ 最终仓库 compose 无 `container_name`、无 `environment`，MySQL/Redis 也不在 compose 内（宿主机自装，review-eng-b P1-16）；实际逐项配齐的是 `image`（tag 变量）/`restart`/`ports`/`extra_hosts`。建议降格表述，免得读者在下一篇找不到「容器名、环境变量」。
3. 【P2】L29 「文件名通常是 `docker-compose.yaml`」→ 最终仓库为 `docker-compose.yml`（微，括注即可；L81 命令、L88 引用同理）。
4. 【P2】L51-65 示意块（mysql-db + redis:4.0）已声明「示意」，可保留；建议括注「最终仓库四服务不含 MySQL/Redis」（簇六）。

### 24-2.项目部署上线：Docker Compose 运行多容器的配置 — 需修

1. 【P1】L24-47 compose 块自称「完整配置如下」，却缺两个 nginx 服务的 `extra_hosts`：SRC `backend_nginx` 与 `frontend_nginx` 均有
   ```yaml
       extra_hosts:
         - "host.docker.internal:host-gateway"
   ```
   ——nginx conf 的 upstream 指向 `host.docker.internal:5001/4001`（23-6 讲的代理目标），Linux 下没有这行 host.docker.internal 无法解析，反代链路直接断；且 24-4 的部署步骤依赖这份 compose。务必补全并加一句「upstream 里的 host.docker.internal 由 extra_hosts 映射到宿主机」（簇六挂本篇落实）。
2. 【P2】title/H1 标点变体（簇三第 5 行）：冒号→破折号、`Docker Compose`→`Docker-compose`，与文件名对齐。
3. 【P2】L82-96 scripts 块缺 `build:share`（SRC 根 package.json 有；23-3 刚强调过它是构建链第一步），建议补上。
4. 【P2】L80 「四个子项目的启停入口，正好对应上面要容器化的服务」→ 容器化的是 server/release + 两个 nginx（nginx 无脚本、client 不进容器），「正好对应」不成立；改「覆盖了 server/release 的构建与启动，client 产物走 OSS」。
5. 【P2】L22/L80/L98 配套资料路径且目录重复（簇四）。

### 24-3.项目部署上线—互联公司的DevOps和CI-CD你知道多少？ — 合格（附 P2 建议）

（概念篇无代码；产研七步、瀑布→敏捷、DevOps=Development+Operations、CI/CD 与云效定位均与课程叙事一致，无技术硬伤；互链 3 个目标（24-1、24-2、2-1）全部存在。）

1. 【P2】L53 整句加粗「**DevOps 就是开发 + 测试 + 运维的交集**」→ 只加粗关键词（簇五）。

### 24-4.项目部署上线—云效DevOps开通使用介绍 — 合格（附 P2 建议）

（流水线两阶段结构、Codeup 代码源、OSS 上传 `packages/client/dist`、compose 制品上传/下载、「先删旧容器旧镜像再 up -d」顺序、`docker compose -f … up -d` 均可成立；互链 4 个目标（24-3、23-4、24-2、9-1、25-1、25-2）全部存在。）

1. 【P2】L43 「镜像构建：……release nginx 镜像、Redis 镜像」→ 最终仓库 compose 只有四个服务、无 Redis 服务（Redis 宿主机自装，review-eng-b P1-16；scan3：CI 配置不在仓内）。课程流水线构建 Redis 镜像属课程版编排范围，建议加口径注「最终仓库 compose 未纳入 Redis」，与 24-2 的四服务对齐。
2. 【P2】L59 「本篇任务包未附带代码类物料」、L63 「本节 materials 未附带代码片段」→ 制作流程残留词（对照 b5 16-5 对 transcript 的处理）：「任务包」「materials」是博客生产链路的词，读者视角不通。改为「本节课程未提供配套代码物料」等表述，英文词 materials 必须清除。
3. 【P2】L37/L50 `docker-compose.yaml` → 最终仓库 `docker-compose.yml`（与 24-2 统一）。
4. 【P2】L63 配套资料路径且目录重复（簇四）。

---

## 三、统计

| 项 | 数量 |
|---|---|
| 总篇数 | 25 |
| 合格（含附 P2 建议 11 篇：21-1、21-2、21-6、21-9、21-10、22-1、22-4、23-2、23-4、24-3、24-4） | **11** |
| 需修 | **14** |
| P0 | 0 |
| P1 | 20 处 / 14 篇（路由簇 7 处：21-3×2、21-4、21-5、21-7、21-8、22-3；代码块/机制类 8 处：21-3 In 枚举块、21-4 props 嵌套块、21-8 ID→文本映射链、22-2 props+columns/dataSource 块、22-3 触发机制、22-3 store.pageTitle、22-5 背景条机制、24-2 缺 extra_hosts；命名类 2 处：23-3 Server.Dockerfile、23-6 release.nginx.dockerfile；标题断链 3 处：23-1、23-5、24-1） |
| P2 | 约 60 处（簇二命名约 15、簇四资料路径 10 篇 14 处、簇三标点变体 3 篇、文案/提示语对齐约 8、示意块括注约 8、整句加粗 3、其余细节约 10） |

需修优先级建议（批量修复顺序）：

1. **簇一 `/local` 路由残留**（21-3、21-4、21-5、21-7、21-8、22-3 共 6 篇）：`LocalController`→`LowCodeController`、`api/local`→`api/low-code`、`local/question_components`→`/api/low_code/question_components`、`local/questionnaireData`→`/api/low_code/question_data`、`local/getQuestionDataById`→`/api/low_code/get_question_data_by_id`，一次批量替换可完成，并与 scan6 A8、b6 簇一已修篇目口径对齐。
2. **三处标题断链**（23-1、23-5、24-1）与三处标点变体（23-2、23-6、24-2）：title/H1 统一按文件名改，一次批量完成，6 篇共 22 处互链随即全部对上。
3. **「照着写会对不上源码」的代码块/机制 P1**：21-3（In 枚举 `textArea`/`account_id`）、21-4（双层 Promise.all + `result` 字段）、21-8（选项 ID→文本 find 映射，空值「选项1」）、22-2（props 实名 `setCurrnetSelected`/`currentSelected`、`options.title`）、22-3（useEffect 首屏自动请求 + `store.title`）、22-5（对齐 SRC `getTopOptions` 双系列背景条 + 双 Y 轴，或明确标注教学简化）、24-2（补 `extra_hosts: host.docker.internal:host-gateway` 两处并加说明）。
4. **文件名 P1**：23-3（`server.Dockerfile`，删「首字母大写才能识别」）、23-6（`release.nginx.Dockerfile`，大写 D）。
5. **簇四资料路径**（10 篇统一改「课程配套代码/资料」泛指，顺带修掉 7 处重复目录名）、**簇二命名**（`textArea`、snake_case、`isMore`/`getTopOptions` 等首次括注）、**簇五整句加粗**（3 处）与**文案对齐**（提示语、标题文案、nav、文件名连字符）可一次批量收尾；24-4 两处流程残留词（任务包/materials）随手清除。
6. 簇六部署链路现状注（extra_hosts 说明、compose 无 MySQL/Redis、XFF 覆盖/trust proxy）在修 24-2 时一并落注，23-4/23-6/24-1/24-4 互链即可，避免第五期与第六期口径不一。
