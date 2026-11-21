# 审稿 B5-P4：04.第四期（24 篇）专家复核报告

- 审稿对象：`work/target/25-lowcode/posts/04.第四期/`（14-1~14-9、15-1~15-8、16-1~16-7，共 24 篇）
- 真源对照：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full/packages/client`、`packages/share`（含 server 侧 low-code 模块用于 14-1~14-5）
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`、`reports/review-eng-b.md`（已修点不重复上报；本期待核残留：A3 MouseSensor、A4 trackUndo、A5 命名、组件 id 发布后重生成口径）
- 审查维度：前端硬伤（MobX6/dnd-kit/React18/撤销快照模型）· 代码可编译性与语言标签 · 与源码一致性 · 六段结构与互链 · 去 AI 味
- 结论口径：【合格】= 无必须修项（可附 P2 建议）；【需修】= 存在 P0/P1。只出报告，未改任何文件。

---

## 〇、残留复查（对齐 scan6 / review-eng-b 已修点）

| 检查项 | 结果 |
|---|---|
| PointerSensor 残留（A3 同源） | P4 全 24 篇 **0 处**（grep 证实），A3 修复无回潮 |
| `triggerUndo` 残留（A4 同源） | 0 处；P4 未展开 undo 实现（在第五期 18-5），仅 15-8/16-3 路线图提及"撤销/前进"，口径中性 |
| `getQuestionComponentValueFeed` / `defaultCheckbox`（A5 同源） | 0 处 |
| scan6「清单外残留」中的 14-3 `/local/release` | **仍在**（3 处），本次正式上报并入 14-3 条目 1 |
| 组件 id 口径 | 15-1「每个组件都必须有的唯一 ID」、16-4 类型故事均未宣称"发布后 id 不变"，无与 review-eng-b P1-7 冲突的表述 |
| MouseSensor/dnd-kit 专题 | P4 不涉及传感器（拖拽在第五期 18-4），无越界描述 |

---

## 一、共性簇（跨篇问题，逐篇条目只留指针）

### 簇一：标题 / H1 与互链引用名不一致（12 篇）——互链"真实存在但按名检索会断"

系列惯例（review-b1-pre：互链逐一对照文件名；review-b2-p1 对 4-1 的裁定）：**引用名以文件名标题为准，改偏离方的 title/h1，引用方不动**。P4 内引用名全部按文件名风格（「前端页面开发—xxx」「后端接口开发—xxx」）书写，以下各篇的 frontmatter title / H1 偏离：

| 篇 | 实际 title/H1 | 全批引用名（引用方） | 建议 | 严重度 |
|---|---|---|---|---|
| 14-2 | 发布接口《上》：三张表定义与 JWT 权限校验准备 | 《后端接口开发—低代码项目编辑模块发布接口《上》》（14-1、14-3） | title/h1 改为引用名 | P2 |
| 14-4 | 后端接口开发**：**…发布接口《下》 | 《后端接口开发**—**…发布接口《下》》（14-5 ×2） | 冒号改破折号 | P2 |
| 14-7 | 前端页面开发**：**…左侧组件列表样式 | 《前端页面开发**—**…》（14-6、14-8、14-9） | 冒号改破折号 | P2 |
| **14-9** | **编辑器右侧属性面板：全局属性与视频组件配置** | 《前端页面开发—视频组件配置属性》（14-7、14-8、15-1、15-2 共 4 处） | title/h1 改为引用名 | **P1** |
| 15-1 | 前端页面开发**：**图片组件展示视图 | 《…**—**图片组件展示视图》（14-9、15-2、15-3、16-1） | 冒号改破折号 | P2 |
| 15-4 | 前端页面开发**：**轮播图组件配置属性 | 《…**—**轮播图组件配置属性》（15-3、15-5、15-6、16-2 ×2） | 冒号改破折号 | P2 |
| 15-5 | …卡片视图组件**与**属性配置组件 | 《…卡片视图组件**+**属性配置组件》（15-3、15-4、15-6） | 「与」改「+」 | P2 |
| **15-6** | **列表组件开发：视图渲染与属性配置** | 《前端页面开发—列表视图组件+属性配置组件》（15-5、15-8） | title/h1 改为引用名 | **P1** |
| 15-7 | 前端页面开发**：**文本视图组件 **+** 属性配置组件 | 《前端页面开发**—**文本视图组件**+**属性配置组件》（15-8、16-1） | 冒号改破折号、去加号两侧空格 | P2 |
| 16-2 | 前端页面开发**：**二维码视图组件+属性配置组件 | 《…**—**二维码视图组件+属性配置组件》（15-8、16-1、16-3） | 冒号改破折号 | P2 |
| 16-3 | …警告视图组件**与**属性配置组件 | 《…警告视图组件**+**属性配置组件》（16-1、16-4） | 「与」改「+」 | P2 |
| **16-4** | **问卷系统输入框组件：从编辑器配置到发布页数据回显** | 《前端页面开发—问卷系统输入框组件》（16-3、16-5） | title/h1 改为引用名 | **P1** |

16-5/16-6/16-7 标题与引用名一致（含 16-7「多选框框组件」——引用方 16-6 用同名，暂不算断链，见 16-7 条目）。

### 簇二：教学阶段命名 vs 最终仓库命名（约 20 处，P2）

课程阶段性代码用了 `local-xxx` / `LocalXxx` 目录名、camelCase 字段与可读化变量名；最终仓库（SRC）为 `LowCodeXxx` 目录 + snake_case 列名 + 源码缩写变量。建议统一策略：**API、类型名、字段名一律以最终仓库为准**（scan6 A9-3、A4 即此口径）；目录别名允许保留但**首次出现时括注最终仓库名**。高频对照：

| 博客写法 | 最终仓库（SRC） | 涉及篇 |
|---|---|---|
| local-video / local-image / local-wrapper / local-text / localList / localCard / local-rich-text / local-empty / local-sprite / LocalInput / LocalTextarea / LocalRadio / LocalCheckbox / LocalQRCode / LocalSwiper / local-components | `LowCodeVideo` `LowCodeImage` `LowCodeSwiper` `LowCodeText` `LowCodeList` `LowCodeCard` `LowCodeRichText` `LowCodeEmpty` `LowCodeSplit` `LowCodeInput` `LowCodeTextArea` `LowCodeRadio` `LowCodeCheckbox` `LowCodeQrcode`；client 属性面板目录 `LowCodeComponents` | 14-8、14-9、15-1~15-8、16-1~16-6 |
| accountId / pageId / configId / pageName / userId | `account_id` / `page_id` / `page_id` / `page_name` / `account_id` | 14-2、14-3、14-4、14-5 |
| componentConfigs / sortableComponentConfig / currentComponentConfig / copyComponentConfig | `compConfigs` / `sortableCompConfig` / `currentCompConfig` / `copyedCompConig` | 14-8、15-5 |
| getUserMessage | `getUserMess`（GetUserMessTool.ts） | 14-2、14-3 |
| local.ts / IPage / TokenUser | `types/request/low-code.ts` / `ILowCode` / `TCurrentUser` | 14-3、14-5 |
| lowcode 模块 / local（低代码）模块 | `low-code` 模块（low-code.module.ts / low-code.entity.ts / low-code.service.ts） | 14-2、14-3 |

### 簇三：去 AI 味零星项（P2）

- 整句加粗（应只加粗关键词）：15-2 L30、15-5 L78、15-8 L53、16-3 L56、16-7 L65。
- 「拓展运算符」→「展开运算符」：14-7 L52/L98、15-4 L57。
- 转写流程词残留："transcript"（16-5 L48，已单列 P1）。

---

## 二、逐篇明细

### 14-1.低代码项目平台编辑模块后端接口梳理 — 合格

五接口清单（发布 / 组件获取 / OSS 上传·查询·删除）与最终仓库一一对应；「草稿与发布谁新读谁」与 `useStoreComponents.localStorageInStore` 的 `store_time`/`release_time` 对比逻辑一致；互链（13-10、14-2、14-5）真实。无修改项。

### 14-2.后端接口开发—低代码项目编辑模块发布接口《上》 — 需修

1. 【P1】`14-2.…《上》.md` L48-56 代码块：原句 `pageId: number; userId: number;`（IComponent）
   → 改为源码 `share/src/types/entity/low-code.ts` 实际字段：`id: number; account_id: number; page_id: number; type: TComponentTypes; options: Record<string, any>;`。现块与同文 L38「字段包括组件 type…`page_id`、`account_id`」（scan6 A9-1 已修）自相矛盾，且 `userId` 字段在源码中不存在。
2. 【P2】标题断链（簇一第 1 行）：title/h1「发布接口《上》：三张表定义与 JWT 权限校验准备」→ 改《后端接口开发—低代码项目编辑模块发布接口《上》》。
3. 【P2】L36 原句「以及 TDK（页面描述）与关键字等 SEO 相关字段」→ page 表是 `tdk`（关键字）与 `desc`（描述）两个独立列；改「页面描述（`desc`）与关键字（`tdk`）」。
4. 【P2】L86-90 validate 描述「用解析出的过期时间与当前时间比对，小于零说明已过期」→ 源码判据是 `data.exp - data.iat <= 0`（比对的是签发时刻，非当前时间；且 passport-jwt 已先行校验 exp，该分支实际不可达——review-eng-b P1-10）。建议如实写「比对 `exp` 与 `iat`，过期拦截主要由 passport-jwt 兜底」。
5. 【P2】L96/L107 `getUserMessage` → 源码装饰器名 `getUserMess`（簇二）。
6. 【P2】L34 「用 NestCLI 生成 lowcode 模块后，在 `entity.ts` 里…」→ 最终仓库模块/实体文件为 low-code（`low-code.entity.ts` 一次定义 Page/Component/ComponentData 三实体），建议括注。

### 14-3.后端接口开发—低代码项目编辑模块发布接口《中》 — 需修

1. 【P1】路由簇（scan6 清单外残留，本次上报）：L53 `@Controller('local')`；L70 「路由为 `POST /local/release`」；L80 「用 Apifox 请求 `POST /local/release`」；L23 「`packages/server` 的 local（低代码）相关模块」
   → 最终仓库为 `@Controller('low_code')` / `POST /low_code/release`（前端 request 封装后为 `/api/low_code/release`）；模块名 low-code。与 scan6 A8 对 19-5/20-2 的修法一致。
2. 【P1】类型簇：L27/L30 「新建 `local.ts`」→ `types/request/low-code.ts`；L33-38 `IPage`→`ILowCode`、`'accountId'`→`'account_id'`、`Omit<IComponent, 'configId' | 'id'>`→`Omit<IComponent, 'account_id' | 'page_id'>`；L101 `findBy(Page, { accountId: user.id })`→`account_id`。注意源码 `PostReleaseRequest` 的 components 排除的是 `account_id`/`page_id` 而非 `id`（真实 `Omit` 集合与本文不同）。
3. 【P2】`getUserMessage` ×4（L16 前置知识语境、L61、L63、L71）→ `getUserMess`（簇二）。
4. 【P2】L76 「注意 `forFeature` 需传入字符串参数形式的实体数组」→ TypeORM `forFeature` 传实体类数组（`[Page, Component, ComponentData]`），"字符串参数"说法错误。
5. 【P2】L58/L72 「`@UseGuards(AuthGuard('jwt'))` …确保只有携带合法 JWT 的请求才能进入」→ 最终仓库已改为 `APP_GUARD` 全局守卫 + `@Public()` 白名单（app.module.ts providers），建议加一句口径注，免得读者按接口级守卫复刻。
6. 【P2】L115 返回 `{ message: '请求成功' }` → 最终仓库 release 返回 `{ msg: '发布成功', data: id }`（client `Header/Center.tsx` 取 `msg`/`data` 跳转），建议加注。

### 14-4.后端接口开发：低代码项目编辑模块发布接口《下》 — 需修

1. 【P1】L30 步骤 3「**删除组件数据**：`ComponentData` 表里先按页面 ID 查…循环逐条 `delete(ComponentData, id)`」与小结 L87「删旧 Component → 删旧 ComponentData」
   → 最终仓库 `low-code.service.ts` 的生产化修正**保留 component_data**（仅删旧组件行，源码注释明示"原课程实现会连带清空问卷数据"）。与 14-2 L40「组件数据表提前建好」的口径也不一致。建议在该步与小结加注：「课程原始实现会删；最终仓库修正为保留问卷数据行（组件 id 发布后重生成，统计端对失效 id 容错——详见终审 P1-7）」。
2. 【P2】L28 「用展开运算符合并 `pageName`、`tdk`、`dsc` 等属性」→ `dsc` 笔误应为 `desc`；且最终仓库列名为 `page_name`/`desc`/`account_id`（snake_case，簇二）。
3. 【P2】L31 「每条执行 `insert(Component, { ...展开字段, configId, accountId })`」→ `page_id`、`account_id`。
4. 【P2】L50/L55 「补 `InternalServerErrorException`，把「发布失败」和具体 `error` 一并返回给前端」→ 与源码一致（`` `发布失败，${err}` ``），但这是 review-eng-b P1-12 的已知负面项（原始驱动错误外泄）。建议补一句「教学实现如此；生产上错误详情只进日志，对外固定文案」。
5. 【P2】标题断链（簇一第 2 行）：title 冒号 → 破折号。

### 14-5.后端接口开发—低代码项目编辑模块页面组件获取接口 — 需修

1. 【P1】L32 「路径用 `release`，组件数据命名为 `withUser`」、L37 `@Get('release/withUser')`、L85 「发 `GET /release/withUser`」、小结 L99 「Controller 用 `GET release/withUser`」
   → 最终仓库 `@Get('release_with_user')`（`GET /low_code/release_with_user`）。scan6 A8-1 对 19-5/20-2 已按 snake_case 修，此处为同源残留。
2. 【P1】L49 「到页面表里 `findOneBy({ codeId: userId })`」及 L55-57 代码块同句
   → Page 实体没有 `codeId` 字段，属硬错误；教学口径应为 `accountId`（最终仓库为 `account_id`）。代码块建议改为 `findOneBy({ account_id: user.id })`。
3. 【P2】L50/L60/L74 「从记录里拿到 `componentIds`（组件 id 数组）」→ Page 实体列名是 `components`（simple-array）；`componentIds` 只存在于响应类型 `GetReleaseDataResponse`。建议括注，避免读者去实体里找。
4. 【P2】L92 「发布时会把组件类型、pageId、accountId…传过来」→ `page_id`/`account_id`（簇二）。
5. 【P2】L47/L54 `TokenUser` → 最终仓库装饰器侧类型为 `TCurrentUser`（`Omit<IUser,'password'>`）。
6. 【P2】建议补现状注：最终仓库该接口 controller 实现为 `getReleaseData(null, user)`（review-eng-b P0-7：恒空、编辑器实际依赖草稿恢复），与本文「按用户 id 查页面记录」的教学描述不同。参照 A2-1 对 30-6 的处理方式加一句即可。

### 14-6.前端页面开发—低代码项目编辑模块整体布局 — 合格（附 P2 建议）

1. 【P2】L71-74 package.json 块 `"build": "tsc && vite build"` → 最终仓库 client 为 `"build": "vite build"`。
2. 【P2】L38 「布局相关组件抽离成 `EditHeader`、`EditLeftPanel`、`EditRightPanel`」→ 源码组件名 EditorHeader / EditorLeftPanel / EditorRightPanel（pages/Editor/）。
3. 【P2】L77-88 依赖块缺 `@ant-design/icons`（本集左右面板已用 AppstoreOutlined/SettingOutlined 等，最终仓库 ^5.2.6），建议补上。

### 14-7.前端页面开发：低代码项目编辑模块左侧组件列表样式 — 需修

1. 【P1】L11 导语「编辑器左侧那排**可拖拽的组件入口**」→ 物料面板是**点击添加**（ComponentList.tsx `onClick` → `store.push(type)`），dnd-kit 拖拽只发生在画布内排序（review-eng-b 口径风险 #11）。改「可点击添加的组件入口（拖拽排序发生在画布内）」。
2. 【P2】L40/L96 公共组件名 `EditComponent` / `EditComponentProps` → 源码 `EditorComponent`（接口名 `ComponentProps`，ComponentList.tsx L112/L105）。
3. 【P2】L55-57 示例 `key={item.type}` → 源码为 `key={index}`（`components.map((item, index) => ...)`）。两写法皆合法，但既称"结构对应视频演示"，建议注明与源码的差异。
4. 【P2】L62 「二维码这一项的 icon 暂时用了一张本地图片（`qrCode.svg`）」→ 源码引入 `assets/xdclass.net.svg`。
5. 【P2】L52/L98 「拓展运算符」→「展开运算符」（簇三）。
6. 【P2】标题断链（簇一第 3 行）：title 冒号 → 破折号。

### 14-8.前端页面开发—视频组件展示视图 — 需修

1. 【P1】L110 「配置默认值来自 `videoComponentDefaultConfig`（`autoPlay`、`post` 封面、`loop`、`muted`、`src`、`startTime` 等）」→ 属性名为 **`poster`**（IVideoComponentProps），`post` 会让读者对不上源码。
2. 【P2】L11 导语「`observe` 为什么不能省」→ `observer`（L79 正文用词正确）。
3. 【P2】L23/L108/L129 「视频组件放在 `localVideo`」→ share 目录 `LowCodeVideo`（导出 VideoComponent；视图组件在 `components/LowCodeVideo/VideoComponent.tsx`）。
4. 【P2】L50-54 store 五变量可读名 → 源码为 `compConfigs / sortableCompConfig / currentCompConfig / copyedCompConig / itemsExpandIndex`（store/components.ts），建议括注源码名（簇二）。
5. 【P2】L82-97 EditCanvas 示例 `getCurrentComponentConfig()?.id === id` → 源码 `getCurrentComponentConfig` 是 **computed**，须 `.get()`：`getCurrentComponentConfig.get()?.id`（EditorCanvas.tsx L322）；`generatorComponent` → 源码函数名 `generateComponent`（EditorCanvas.tsx L27）。MobX computed 漏 `.get()` 是本专题（MobX 用法）的实质错误，建议至少加注。
6. 【P2】L108 「`controls` 按参数决定是否展示」→ 源码 `controls={!!_props || isReady}`，`_props` 恒为对象故控制器实际**始终展示**；建议如实描述，顺带解释 `isReady` 真正的作用在起播时间。
7. 【P2】L54 「`itemsExpandIndex`：`number`，属性选项的展开 / 折叠（0 折叠、1 展开）」→ 源码语义是"当前展开项的下标"（`setItemsExpandIndex(expandIndex)`），不是布尔开关。
8. 【P2】L50 「后端把 `props` 叫 `Options`」→ 后端列名为小写 `options`（component 表 simple-json 列）。

### 14-9.前端页面开发—视频组件配置属性（现题《编辑器右侧属性面板：全局属性与视频组件配置》） — 需修

1. 【P1】标题断链（簇一第 4 行）：title/h1「编辑器右侧属性面板：全局属性与视频组件配置」与 4 处引用名《前端页面开发—视频组件配置属性》完全不一致（review-b2-p1 对 4-1 的同型问题判 P1）。改 title/h1 侧，一处即修复全部引用。
2. 【P1】L55 「中间最关键的一步是 `formatComponentPropsByConfig`」→ 源码函数名为 **`fillComponentPropsByConfig`**（share components/func.ts）。一维↔二维转换全文多处以本名展开，须统一。
3. 【P2】L83 「初始播放时间（`InputNumber`，默认 0）」→ 源码是 `<Input type="number" placeholder="请输入初始播放时间" />`（VideoComponentProps.tsx L27）。
4. 【P2】L55 「表单放在 `components/localVideo` 下…子项是二次封装的 `FormItem`」→ 目录 `LowCodeVideo`；子项组件名为 **`FormPropLabel`**（client utils/components.tsx）。
5. 【P2】L33/L37 「`TDK`：页面关键字」→ store 字段与 Form.Item name 均为小写 `tdk`（store/page.ts、GlobalFields.tsx）。

### 15-1.前端页面开发：图片组件展示视图 — 需修

1. 【P1】`handleClick` ×4：L38 属性表、L44 「当 `handleClick === 'open-url'` 时」、L53 默认值说明、L109 小结 → 源码属性名为 **`handleClicked`**（IImageComponentProps.handleClicked；ImageComponent.tsx `props.handleClicked === "open-url"`）。
2. 【P2】L11/L24/L26/L108 「`local-image` / `local-video`」→ `LowCodeImage` / `LowCodeVideo`（簇二）。
3. 【P2】L42 「样式用 Tailwind CSS 的类名表达（`w-full`、`object-cover`、`outline` 等）」→ 源码 `<img>` 只有 `className="w-full"`，height 与 objectFit 是**内联 style**（`style={{ height: \`${props.height}px\`, objectFit: props.fit }}`）。
4. 【P2】L83 「它通过 `getComponent.get(type)` 按组件类型取配置组件」→ client 侧是 `getComponentPropsByType(type)`（attributeExport.ts）；「写死为 `'video'` 占位」与源码 `// "image"` 注释痕迹一致，故事成立。
5. 【P2】L53 「`name` 默认「图片的名称」」→ 源码默认值为「图片名称」（微小，可不改）。
6. 【P2】标题断链（簇一第 5 行）：title 冒号 → 破折号。

### 15-2.前端页面开发—图片组件配置属性 — 需修

1. 【P1】L37 「每个子项用 Form.Item 的二次封装 `formPropLabel`，传 `label`…并传 `propName` 指定要改哪个属性」+ L40-43 代码块 `<FormPropLabel label="图片名称" propName="name">`
   → 源码 `FormPropLabel` 的入参是 `name`（Form.Item 字段名）+ 必传的 `prop`（含 `isHidden` 的包装对象），**没有 `propName` 参数**（`propName` 是 `UploadEditOrChooiseInput` 的入参，两回事）。按源码改：`<FormPropLabel name="name" prop={props.name} label="图片名称："><Input /></FormPropLabel>`。
2. 【P2】L47 「对应 `propHandleClick`（图片是否可点击）」→ `handleClicked`（与 15-1 同簇）。
3. 【P2】L53-60 fitOptions 代码块止于 `scale-down` → 源码 8 项（另有 `initial`/`revert`/`unset`），补省略号或补全。
4. 【P2】L69 「改用 `getComponentConfig.get(type)` 按组件类型取对应配置」→ `getComponentPropsByType(type)`。
5. 【P2】L34 「本集新建 `local-image` 文件夹」→ client 侧目录 `LowCodeComponents/LowCodeImage`（簇二）。
6. 【P2】L63 「修改 store 里维护的 `options`」→ client store 字段是 `props`（后端列才是 options）。

### 15-3.前端页面开发—轮播图组件展示视图 — 需修

1. 【P1】L44 「默认配置是：…`autoplay` 为 `false`…」+ L101 小结「不自动播放」→ 源码 `swiperComponentDefaultConfig.autoPlay` 的 `value`/`defaultValue` 均为 **`true`**（默认自动播放）。两处同改。
2. 【P2】L39/L44/L101 字段名 `autoplay` → `autoPlay`（簇二）。
3. 【P2】L25 「本节新建一个目录（如 `local-wrapper`）」→ `LowCodeSwiper`；"wrapper" 应为笔误/口径漂移。
4. 【P2】L50 「必须执行一次 share 子包的打包（如 `pnpm build share`）」→ 根目录脚本为 `pnpm build:share`（`pnpm build share` 不是合法命令）。
5. 【P2】L54 「先把 `activeRightPanel` 设为 `images`」→ 最终实现是 `getComponentPropsByType` 映射（ComponentFields），建议用真实机制表述。
6. 【P2】L46 「含 `id`、`type`、`option` 等通用字段」→ 通用结构字段为 `props`（TBasicComponentConfig）。
7. 【P2】标题断链（簇一第 6 行）：title 冒号 → 破折号。

### 15-4.前端页面开发：轮播图组件配置属性 — 需修

1. 【P1】`updateCurrentComponentConfigWithArray` ×3（L57、L67、L102 小结）→ 源码方法名为 **`updateCurrentCompConfigWithArray`**（useStoreComponents.ts）。读者按文中名去源码检索会落空。
2. 【P2】L21 「指示点位置（左 / 右 / 上）」→ 源码 Select 有 bottom/left/right/top 四项（缺"下"）。
3. 【P2】L21/L39/L98 `autoplay` → `autoPlay`（簇二）。
4. 【P2】L47 「点击触发 addNewValue」→ 源码函数名 `addNewItem`（FormContainerWithList）。
5. 【P2】L67 「store 里早期定义的折叠/展开变量因逻辑调整已无用处，一并删除」→ 最终仓库 store 仍保留 `itemsExpandIndex`（`setItemsExpandIndex` 写入，`UploadEditOrChooiseInput` 用它定位展开项）。改为「该变量后并入 FormContainerWithList 的展开逻辑」。
6. 【P2】L57 「用拓展运算符…」→ 展开运算符（簇三）；标题断链（簇一第 7 行）：冒号 → 破折号。

### 15-5.前端页面开发—卡片视图组件与属性配置组件 — 需修

1. 【P1】属性名 `coverImage`：L31/L34 代码块 `props.coverImage`（两处）、L39 「600×200 的 `coverImage`」、L46 「卡片属性类型（`coverImage`、`title`、`description`）」→ 源码属性名为 **`coverImg`**（ICardComponentProps.coverImg；CardComponent.tsx `src={props.coverImg}`）。
2. 【P2】L27/L62 「localCard 文件夹」→ share 侧 `LowCodeCard`、client 侧 `LowCodeComponents/LowCodeCard`（簇二）。
3. 【P2】L30 代码块签名 `(props: TCardProps)` → 源码 `ICardComponentProps`；且源码是 `export default function CardComponent`，非 `export const`（教学期快照可保留，建议加注）。
4. 【P2】标题断链（簇一第 8 行）：title「与」→「+」。

### 15-6.前端页面开发—列表视图组件+属性配置组件（现题《列表组件开发：视图渲染与属性配置》） — 需修

1. 【P1】`TBasicComponentsConfig` ×3（L17 前置知识、L44 正文、L76 小结）→ 源码类型名为 **`TBasicComponentConfig`**（share components/type.ts）。
2. 【P1】标题断链（簇一第 9 行）：title/h1「列表组件开发：视图渲染与属性配置」与 2 处引用名《前端页面开发—列表视图组件+属性配置组件》完全不一致。改 title/h1。
3. 【P2】L34/L52 「`components/localList`」「`client/src/components/localComponent/localList`」→ share 侧 `LowCodeList`；client 侧 `LowCodeComponents/LowCodeList`（簇二）。
4. 【P2】L40 「`List.Item.Meta` 的图标、标题、描述三要素」→ antd 官方是 **avatar（头像）/title/description**；"图标"不准确。
5. 【P2】L56 「头像上传暂时先用空值维护并注释/隐藏」→ 最终仓库 ListComponentProps 头像项已接 `UploadEditOrChooiseInput`（带 listOptions），建议注明现状。
6. 【P2】L52 「`index.ts` 用 `export default` 全盘抛出」→ 源码为命名导出 `export { default as ListComponentProps } from './ListComponentProps'`，"全盘抛出"表述宜改。

### 15-7.前端页面开发：文本视图组件 + 属性配置组件 — 合格（附 P2 建议）

1. 【P2】L28/L54 「local-text 文件夹」→ `LowCodeText`（share）/ `LowCodeComponents/LowCodeText`（client）（簇二）。
2. 【P2】L59 「里面放两个 `FormItem`」→ 源码子项组件为 `FormPropLabel`。
3. 【P2】标题断链（簇一第 10 行）：title 冒号 + 加号两侧空格 → 与引用名「前端页面开发—文本视图组件+属性配置组件」对齐。

（switch 五档映射表、Tailwind 数值（16px/24px、18px/28px）、Segmented options、deps 块均与源码一致；`textArea: InputComponentProps` 的复用事实与 16-5 呼应正确。）

### 15-8.前端页面开发—分割+空状态组件 — 需修

1. 【P1】`dash` ×3：L27 「`dash`：是否虚线」、L50 「是否虚线 → 改 `dash`」、L88 小结 → 源码属性名为 **`dashed`**（ISplitComponentProps.dashed；SplitComponentProps.tsx `name="dashed"`）。
2. 【P1】L63-69 Empty 代码块 `imageStyle={{ width: props.width, height: props.height, objectFit: props.objectFit }}` → 源码属性名为 **`imageWidth` / `imageHeight` / `imageObjectFit`**（IEmptyComponentProps）；`image={props.image || undefined}` → 源码为 `props.image || Empty.PRESENTED_IMAGE_DEFAULT`。现块按文中属性名取值拿不到数据。
3. 【P2】L23 「分割组件放在 share 包的 `src/components/local-sprite`」→ `LowCodeSplit`（"sprite" 应为 split 的转写笔误）。
4. 【P2】L47 「client 的 `components/local-components` 里（`LocalSpriteComponent`）」→ `LowCodeComponents/LowCodeSplit/SplitComponentProps`。
5. 【P2】L57 「空状态组件在 share 包的 `local-empty`」→ `LowCodeEmpty`（簇二）。
6. 【P2】L73 「描述项传 `name="description"`、`label`、`propName`」→ `FormPropLabel` 用 `name`+`prop`（与 15-2 同簇）。

### 16-1.前端页面开发—富文本视图组件+属性配置组件 — 需修

1. 【P1】L29 「在它上面用 React JSX 特有的 `dangerouslySetInnerHTML`…`span`、`h1`、`ol`、`ul` 等标签连同字体颜色、背景色都能**原样渲染**出来」
   → 源码渲染前经 **`sanitizeHtml`（DOMPurify 白名单净化）**（RichTextComponent.tsx L12-22），并非原样插入；"原样渲染"与源码相反且涉及安全面。建议补一句「源码在渲染前用 DOMPurify 按白名单净化；SSR 首屏分支跳过净化是终审已知的缺陷点（review-eng-b P0-6/#8）」，既符合源码又避免读者以为线上是裸 dangerouslySetInnerHTML。
2. 【P2】L29/L70 「`components/local-rich-text`」「第一次做 `local-video`」→ `LowCodeRichText` / `LowCodeVideo`（簇二）。
3. 【P2】L84 package.json 块 `"build": "tsc && vite build"` → 最终仓库 `"vite build"`（react-quill ^2.0.0 等依赖项本身核对无误）。

（getHTML 回写、quill.snow、空内容占位文案、toolbar 配置、Tailwind preflight 排查叙事均与源码/事实一致，质量高。）

### 16-2.前端页面开发：二维码视图组件+属性配置组件 — 合格（附 P2 建议）

1. 【P2】L21/L61/L100 「LocalQRCode」→ share 目录 `LowCodeQrcode`（导出 QrcodeComponent）；client 侧 `QrcodeComponentProps`（簇二）。
2. 【P2】L63 「二维码尺寸、以及中间图标大小（后两项演示里未设置，留作自行实现）」→ 源码 **size 项已实现**（`<Input type="number" max={375} min={80} />`）；注释掉的只有 icon/iconSize 两项。应改为「未实现的只有中间图标相关两项」。
3. 【P2】L70 `(color as ColorType).toHex()` → 源码断言类型为 `ColorFactory`（`antd/es/color-picker/color`）。
4. 【P2】L61 「还传入一个 `handleValuesChangeAfter` 方法」→ 传给 `FormContainer` 的回调 prop 名是 **`onValuesChangeAfter`**（组件内处理函数才叫 handleValuesChangeAfter）。
5. 【P2】标题断链（簇一第 11 行）：冒号 → 破折号。

（QRCode 参数表、纠错等级 7%/15%/25%/30% 与"缺损需分散分布"的补充说明均准确；value 默认 "-"、色值默认与 errorLevel 默认 L 全部对得上源码。）

### 16-3.前端页面开发—警告视图组件与属性配置组件 — 需修

1. 【P1】属性名簇：L24-26 「`message`：提示文本内容」「`closable`：是否显示关闭按钮」+ L34-48 代码块 `name="message"`、`name="closable"`、外层 `<WrapperForm …>`
   → 组件自有属性是 **`title` / `showClose`**（IAlertComponentProps），渲染时才映射为 antd Alert 的 `message`/`closable`（AlertComponent.tsx `message={props.title || "请输入文本"}`、`closable={props.showClose}`）；源码配置面板 Form.Item name 为 `title/type/showIcon/showClose`，外层是 `FormContainer`。按源码改代码块与属性表。
2. 【P2】L32 「前端 `src/components` 下的 `localComponents` 新建 `alert` 配置组件」→ `LowCodeComponents/LowCodeAlert/AlertComponentProps`（簇二）。
3. 【P2】L56 整句加粗「**视图改变要影响 store，store 改变也要响应式同步回视图**」→ 只加粗关键词（簇三）。
4. 【P2】标题断链（簇一第 12 行）：「与」→「+」。

### 16-4.前端页面开发—问卷系统输入框组件（现题《问卷系统输入框组件：从编辑器配置到发布页数据回显》） — 需修

1. 【P1】标题断链（簇一第 13 行）：title/h1 与 16-3/16-5 两处引用名《前端页面开发—问卷系统输入框组件》完全不一致。改 title/h1。
2. 【P2】L29/L62 「`src/pages/editor/editorCanvas` 里 `generateComponent`」→ 源码路径 `pages/Editor/EditorCanvas.tsx`（函数名 `generateComponent` 本身正确）。
3. 【P2】L29/L69/L73 「`LocalInput`」→ `LowCodeInput`（导出 InputComponent）（簇二）。

（onUpdate 出口、`event.target.value`、title/text/placeholder 语义辨析、`AlertComponentConfig` vs 带 `Result` 后缀类型不带 id 的排错故事，均与源码对得上，是本簇质量最好的一篇。）

### 16-5.前端页面开发—问卷系统文本域组件 — 需修

1. 【P1】L48 「（对应 transcript 中的 `Attribute export` / 即 `export` 出一个 `Textarea` 视图）」→ "**transcript**" 是视频转写流程残留词，必须清除；`Attribute export` 实指 client 的属性导出表 `attributeExport.ts`（源码把 `textArea` 映射到 `InputComponentProps`）。改写为：「在 client 的属性组件导出表（attributeExport）里，把 textArea 也映射到输入框的配置组件」。
2. 【P2】L36/L42-44 回调名 `onChange`、字段 `value` → 与 16-4 及源码统一为 `onUpdate` / `text`（源码 `<TextArea placeholder={props.placeholder} value={props.text} onChange={event => props.onUpdate?.(event.target.value)} />`）。文中"回调名 onChange"与 16-4 建立的 onUpdate 口径互相打架。
3. 【P2】L21 「字段结构（placeholder、默认值、**是否必填**等）完全一致」→ 实际字段 title/text/placeholder/onUpdate，无"是否必填"。
4. 【P2】L25/L64 「`LocalTextarea`」→ `LowCodeTextArea`（导出 TextAreaComponent；默认值复用 `inputComponentDefaultConfig`——文中"复用输入框 props"表述正确）。

### 16-6.前端页面开发—问卷系统单选框组件 — 合格（附 P2 建议）

1. 【P2】L78 「由它负责渲染 `ChoiceForm.Item` 的 label（也就是选项名称 `name`）」→ 应为 antd 的 **`Form.Item`**（`label="选项名称："`、`name="value"`）；"ChoiceForm" 与"选项名称 name"均系口播转写讹误。
2. 【P2】L21-25 「显示两部分内容」下却列 1/2/3 三条 → 第三条是交互行为不是组成部分，改「三件事」或把第 3 条并入说明。
3. 【P2】L31/L73 「`LocalRadio`」→ `LowCodeRadio`（导出 RadioComponent；配置面板 `RadioComponentProps`）（簇二）。

（Radio.Group 代码块、`value={defaultRadio}`、按选项 id 比对、Select 的 `{value: id, label}` 格式、`keyName="options"` 全部与源码一致。）

### 16-7.前端页面开发—问卷系统多选框框组件 — 合格（附 P2 建议）

1. 【P2】标题/文件名「多选框**框**组件」重复字（源自课程原名；引用方 16-6 用同名，若修需两处同步，属系列级小洁癖）。
2. 【P2】L65 整句加粗「**所有前端组件的逻辑就都开发完成了**」→ 只加粗关键词（簇三）。

（Checkbox.Group 代码块、`defaultChecked` 数组语义、与单选框的差异点、收尾排期与源码一致；antd 官方 defaultCheckedList 类比准确。）

---

## 三、统计

| 项 | 数量 |
|---|---|
| 总篇数 | 24 |
| 合格（含附 P2 建议 6 篇：14-1、14-6、15-7、16-2、16-6、16-7） | **6** |
| 需修 | **18** |
| P0 | 0 |
| P1 | 23（硬错误集中于：属性/类型/函数名与源码不符 14 处；路由/口径残留 4 处；标题断链 3 处；ComponentData 删除口径 1 处；"原样渲染"安全表述 1 处） |
| P2 | 89（命名簇约 40、标题断链标点变体 9、build 脚本/依赖块 3、表述精度与口径注约 20、去AI味机械项约 10、其余细节） |

需修优先级建议：
1. 先修 P1 中"读者照着写会对不上源码"的属性/函数名簇：14-2（IComponent 块）、14-5（codeId）、14-8（poster）、14-9（fillComponentPropsByConfig）、15-1/15-2（handleClicked、FormPropLabel 入参）、15-3（autoPlay 默认值）、15-4（updateCurrentCompConfigWithArray）、15-5（coverImg）、15-6（TBasicComponentConfig）、15-8（dashed、Empty 三属性）、16-3（title/showClose）、16-1（DOMPurify 表述）。
2. 再修 3 处标题断链（14-9、15-6、16-4）与簇一标点变体（一次批量可完成 12 篇）。
3. 簇二命名统一建议按"API/类型/字段名以最终仓库为准 + 目录别名首次出现括注"执行，可与后续第五期审稿（18-x/19-x/20-x）一起批量处理，避免两期口径不一。
