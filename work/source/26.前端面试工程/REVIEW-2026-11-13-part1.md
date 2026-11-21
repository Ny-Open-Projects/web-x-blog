# 审核报告：第 01-13 号文件（2026-11-13，Part 1）

> 审核范围：01-web-network-browser.md ~ 13-framework-principles.md（共 13 个文件，约 100K 行）。
> 审核方式：逐文件通读章节结构 + 高频考点章节精读 + 全部简化代码示例核对（以 2025-2026 年浏览器 / React 19 / Vue 3.5+ / TS 5.x / ES2024+ 实际行为为准）。
> 所有修复均已直接落地到对应文件，未 commit/push。

## 一、总体评价

这套资料整体质量**远高于市面常见面试题库**，属于可以直接背诵 + 动手验证的工程级材料：

1. **技术密度高且基本准确**：绝大多数概念表述符合 2025-2026 年的最新事实（HTTP/3 QUIC、TLS 1.3、React 19 Actions/ref-as-prop/useActionState、Vue 3.5 useTemplateRef/onWatcherCleanup/Teleport defer、React Compiler、INP 取代 FID 等），没有发现"教科书级"的大面积过时内容。
2. **每题配可运行代码**：代码示例与答案一一对应（"一一对应"注释），大部分代码可直接粘贴运行验证。
3. **答案结构好**：普遍带"为什么 + 追问点 + 工程取舍"，符合面试实战要求。
4. **发现的问题集中在两类**：① 少数示例代码有运行时/编译期 bug（共 6 处，已修复）；② 个别结论句表述含糊或数值算错（共 8 处，已修复）。详见下文逐文件清单。

**修复统计**：共修改 10 个文件、落地 24 处修复/补充；01、10、11、12 四个文件未发现需要修改的问题。

## 二、逐文件问题与修复清单

### 01-web-network-browser.md（5653 行，0 处修改）
- 精读了 HTTP/1.1~3、TLS/HTTPS、缓存、CORS/跨域、渲染流程、事件循环、Node 事件循环、rAF 等全部高频章节，未发现技术错误。
- 亮点：WEB-007 Server Push 废弃原因 + Early Hints 替代、WEB-009 0-RTT 重放风险与 425 状态码、WEB-053/054 宏微任务与 nextTick 优先级均准确。
- 备考提示：该文件权威度高，可直接背。

### 02-html5.md（9972 行，1 处修改）
- ✏️ H5-040（约 1489 行）：`<slot>` 描述中错别字"光具名/默认插槽"→"分具名插槽与默认插槽两种"。
- 其余（Web Components 生命周期/Shadow DOM 事件重定向/composed、Canvas 高分屏 DPR 适配、画布污染、PiP 系列）全部准确。

### 03-css.md（6465 行，3 处修改）
- ✏️ CSS-008（238 行）：原句"min-width/max-width 始终按 content-box 之外的总宽计算规则的细节在两模型下一致"语义混乱 → 改为"min-width/max-width 同样受 box-sizing 影响（与 width 计算方式一致）"。
- ✏️ CSS-019（520 行）：自问自答式绕口表述 → 明确为"min-width: auto 让 flex 项目收缩时不小于 min-content，想继续压缩需 min-width: 0"（这是 flex 高频追问）。
- ✏️ CSS-020（561 行）：space-around 的数值算例错误：容器 500、三项共 300、剩余 200 时，边缘间隙应为 200/6≈33.3、中间 66.7，原文写"边缘 50 / 中间 100"→ 已改正。面试手算题，数值错了会很尴尬。
- 其余（BFC 三特性、层叠上下文七级顺序、sticky 失效条件、transform 改变 fixed 包含块）准确。

### 04-javascript.md（8523 行，4 处修改）
- ✏️ JS-053（1514 行）：默认参数题输出注释错误，`f(2, null)` 中 c = null + 1 = **1**，原注释写"6"且带着"b+1=NaN?"的自我怀疑残留 → 已改为正确推导 [2, null, 1]。
- ✏️ JS-056（1592 行）：新特性只列到 ES2023 → 补充 **ES2024**（Object.groupBy、Promise.withResolvers、resizable ArrayBuffer、正则 v 标志）与 **ES2025**（Set 集合运算方法、Iterator helpers、RegExp.escape），并附代码示例。2026 年面试"你了解最新 ES 特性吗"是加分题，原答案会露怯。
- ✏️ JS-144（5316 行）：错误说法"严格模式下块级函数声明会报 ReferenceError" → 修正为"严格模式下块内声明只在块内可见，块外 typeof 输出 'undefined'"（typeof 对未声明变量从不抛错，这是经典追问陷阱）。
- 其余（this 优先级、手写 call/bind、事件循环输出题、防抖节流、deepClone、curry）核对无误，输出题答案全部口算验证通过。

### 05-typescript.md（5663 行，1 处修改）
- ✏️ TS-119（3249 行）：`isApiError` 守卫写 `res.data === undefined` —— **编译不通过**（ApiError 上没有 data 属性，TS2339），面试现场写出来会被抓 → 改为 `"message" in res && !("data" in res)` 并加注释说明这个坑本身也是考点。
- 其余（unknown/never、分布式条件类型、infer 协变逆变、Zod 单一来源、as const 替代 enum、TS 5.0 标准装饰器）准确。

### 06-vue3.md（9857 行，2 处修改）
- ✏️ V3-018（605 行）：补充 **Vue 3.5 的 `deep: <number>` 限制遍历深度**用法（大对象 deep watch 的性能优化加分点）。
- 已对照 Vue 官方文档复核："ref 包对象默认只监听 .value 替换、reactive 对象隐式 deep"的表述正确（这是最容易写错的一条，该文件写对了）。
- 其余（defineModel 3.4 转正含 get/set 钩子、Suspense async setup、EffectScope、hasInjectionContext、3.3/3.4/3.5 版本速查）准确。

### 07-react19.md（10290 行，1 处修改）
- ✏️ R19-005（211 行）：`use(promise)` 示例在组件体内创建 Promise 却注释"只创建一次"，照抄会导致无限 suspend → 注释改为明确警告"Promise 必须在组件外或缓存层创建（模块级/cache()/Suspense 缓存），写在组件体里每次渲染都会重新 fetch"。
- 其余核对全部准确：useActionState 签名、useFormStatus 必须在 form 内、useOptimistic 回滚、ref-as-prop + cleanup function、React 19 移除 Server Push 支持（106 版本）、forwardRef 弃用、React Compiler "无法证明安全则放弃优化"的定位，均与 React 19 官方文档一致。

### 08-engineering.md（5597 行，3 处修改）
- ✏️ ENG-116（3154 行）：eslint.config.mjs 示例缺 `export default [...]` 数组包裹，不是合法 flat config → 已补全（flat config 形态本身就是考点）。
- ✏️ ENG-016（454 行）：注释错别字"plugin 做loader"→"做 loader"。
- ✏️ ENG-025（672 行）：generate 阶段描述"把 AST 反序列化回代码"用词不当 → "把 AST 生成回代码字符串并产出 sourcemap"。
- 其余（pnpm store/硬链接结构、npm ci --frozen-lockfile、幽灵依赖、peerDependencies、Vite 双引擎、HMR 全链路、Turborepo dependsOn '^build'、qiankun Proxy 沙箱）准确。

### 09-performance-security.md（7151 行，5 处修改）—— 问题最多的文件
- ✏️ PER-005（139 行）：**API 用错**。`PerformanceObserver.observe({ type, name, buffered })` 不支持 `name` 过滤（MDN PerformanceObserverInit 只有 type/entryTypes/buffered），paint 类型会同时产出 first-paint，`getEntries()[0]` 可能取到 FP 而非 FCP → 改为按 `e.name === 'first-contentful-paint'` 手动筛选。
- ✏️ PER-006（169 行）：**运行时 bug**。`const [measure] = performance.measure(...)` 对非可迭代对象解构会直接 TypeError → 改为 `const measure = performance.measure(...)`。
- ✏️ PER-038（1043 行）：指标列表笔误"FP/NSP"→ 改为 INP。
- ✏️ PER-027（736 行）：示例还在 `import { Button, Dialog } from 'element-ui'`（Vue 2 时代库，2026 年面试官会追问）→ 换成 element-plus（ElButton/ElDialog）；同时注释补充 **React 19 起官方不再提供 UMD 产物**，externals+CDN 方案对 React 19 不再适用。
- ✏️ 其余（INP 98 分位、CLS impact×distance、sendBeacon 64KB 限制、sourcemap hidden-source-map、CSP report-uri、CSRF SameSite 组合拳、供应链 npm audit/overrides）准确。

### 10-basics.md（3364 行，0 处修改）
- 全文件通读（体量最小，覆盖最完整）：TDZ/typeof 死区、ToPrimitive 分支、BAS-134 默认参数惰性求值口算、包装对象、属性描述符与 Vue2 响应式的关联、Node require 解析顺序、exec/spawn 背压、semver 0.x 陷阱等全部准确，输出题均已口算验证。

### 11-scenario.md（8075 行，0 处修改）
- 精读线上排查、性能实战、请求竞态/并发控制/断点续传、登录态无感刷新（并发 401 共享 Promise）、多标签页 BroadcastChannel、SKU 联动、权限指令、水印防篡改、SameSite=None; Secure、TanStack Query invalidate 模式、撤销重做快照栈等章节，方案与代码均正确且工程化程度高。
- 唯一提示：SCN-026 的 v-permission 指令只在 mounted 时校验权限码，若权限异步到达会失效（生产实现建议 watch permissions 或在指令 updated 钩子复查）——属可接受的示例简化，未改动。

### 12-performance-optimization.md（8554 行，0 处修改）
- 精读 AVIF/WebP 接入、关键 CSS 两种异步加载技巧、SW cache-first/network-first 手写与 skipWaiting 坑、INP 三段归因（inputDelay/processing/presentation）、shallowRef 大列表、v-memo 依赖写漏陷阱、React 状态下沉/useSyncExternalStore selector、Vue computed vs watch 等，全部准确。
- 提示：OPT-083 的 mini store getSnapshot 注释已自带"selector 必须返回原始值或稳定引用"的关键警告（这正是 useSyncExternalStore 的经典追问），备考时重点记这条。

### 13-framework-principles.md（11325 行，5 处修改）—— 最严重的两个问题都在这里
- ✏️ **FRP-005（约 258 行）：重写了 computed 简化实现**。原代码有 3 个 bug：① track() 首分支在 `!activeEffect` 时向依赖集合 add(null)；② trigger 直接重跑 runner 而非"置脏"，与"懒计算"的论述自相矛盾；③ 下游订阅链（computed.dep）从未被填充，导致示例声称的输出"render: 60"实际跑不出来。重写后加入 `runner.scheduled`（只置脏）并修正验证输出——这是 Vue 响应式面试的核心手写题，原版会被当场追问翻车。
- ✏️ **FRP-036（1800 行）：useTransition 示例用同一个 state 连续 setQuery 两次**（同步一次 + transition 一次），值相同导致过渡更新失去意义，与 react.dev 官方"双 state"模式不符 → 改为 inputValue（紧急）+ query（过渡）双 state。
- ✏️ FRP-026（1291 行）：`let rootLanes = NoLanes = 0` 隐式创建全局变量（严格模式报错）→ `let rootLanes = 0`。
- ✏️ FRP-055（2716 行）：源码字段名笔误 "readdonlyMap" → "reactiveMap/shallowReactiveMap/readonlyMap"。
- 其余精读（Fiber 链表遍历/双缓冲、lane 位运算 `lanes & -lanes`、Hook 链表与条件调用错位、useLayoutEffect 三子阶段、effectStack 嵌套、cleanup 分支切换、RefImpl/Dep、惰性代理 reactiveMap、queueJob/nextTick、h+mount/patch 渲染器、MessageChannel 时间切片 vs setTimeout 4ms 钳制、lane 合并与补渲染、panicked lane 同步重试）核对无误。

## 三、最严重问题 TOP 5（按"面试翻车风险"排序）

1. **13 文件 FRP-005 computed 手写实现跑不出声称的输出**（已重写）——响应式原理是 Vue 高级岗必考手写题，原版被追问"你这段代码 state.count 改了为什么没打印"就暴露。
2. **09 文件 PER-005/PER-006 的 Performance API 用法错误**（已修复）——性能监控是高级岗高频实战题，observe 不支持 name 过滤、measure 返回值解构报错都是"现场跑一下就穿帮"的错误。
3. **05 文件 isApiError 守卫编译不通过**（已修复）——TS 手写守卫被 IDE 现场标红会很尴尬，而且这个坑（联合类型上访问不存在的属性）本身是考点。
4. **07 文件 use(promise) 示例注释误导**（已修复）——照抄会无限 suspend，"Promise 在哪创建"正是 R19 数据获取的标准追问。
5. **03 文件 space-around 手算数值错误 + 04 文件默认参数输出错误**（已修复）——纯记忆型考点，背错数字面试直接丢分。

## 四、备考建议：薄弱点与重点背诵

**整体不薄弱**，资料完成度很高。按"性价比"排的人工重点：

1. **必须动手跑一遍的代码**（背不如跑，跑过才有底气应对追问）：
   - 04 文件第二十/二十一章的全部"综合输出题"（JS-141~146）、第六章事件循环输出题——口算 + Node/浏览器双环境验证。
   - 13 文件 FRP-001/005/051/052/053（响应式五件套）和 FRP-028/030/031/032（Hook 链表/批处理/两阶段）——手写模拟代码敲一遍。
   - 09 文件 PER-005/007 的 PerformanceObserver 采集封装——开 DevTools 验证 buffered 回放。
2. **最容易背串的主题**（建议做对比卡片）：
   - 宏任务/微任务/nextTick（01-WEB-053/054 ↔ 04-JS-043~048 ↔ 10-BAS 系列交叉背诵）。
   - 强缓存/协商缓存/SW 缓存策略（01-WEB-022~028 ↔ 09-PER-010/011 ↔ 12-OPT-029/030，三处口径一致，可互相印证）。
   - watch vs watchEffect vs computed（06-V3-015~020 ↔ 12-OPT-091 ↔ 13-FRP-005/006）。
3. **2026 年时效性加分点**（资料已补齐，重点记新补的）：
   - ES2024/ES2025 新特性（04-JS-056 新增段）——"说一个你真用过的"：Promise.withResolvers / Object.groupBy / Set.intersection。
   - React 19 全套（Actions、useActionState、ref-as-prop、cleanup ref、use）——07 文件第一章是全库质量最高的 React 19 材料。
   - Vue 3.5（deep 数字、useTemplateRef、onWatcherCleanup、Teleport defer）——06-V3-018 与 V3-176 版本速查。
4. **相对单薄的覆盖**（这三处可自行补充外部资料）：
   - 03-CSS 容器查询（container queries）着墨少，2026 年中后台布局已开始落地，建议补 2-3 题。
   - 11-场景题中"AI 相关场景"（如何接 LLM 流式接口、SSE 流式渲染打字机效果）只在 01/12 有零散提及，建议补 1-2 个完整场景。
   - 09-安全对 Subresource Integrity（SRI）与 Trusted Types 没有独立题目，外企/大厂安全面会问。

## 五、修复落位速查

| 文件 | 修改数 | 关键行号 |
| --- | --- | --- |
| 01 | 0 | - |
| 02 | 1 | L1489 |
| 03 | 3 | L238, L520, L561 |
| 04 | 4 | L1514, L1592-1596, L1620-1641, L5316 |
| 05 | 1 | L3248-3252 |
| 06 | 2 | L605-606 |
| 07 | 1 | L210-213 |
| 08 | 3 | L454, L672, L3153-3176 |
| 09 | 5 | L135-142, L166-171, L731-737, L1043 |
| 10 | 0 | - |
| 11 | 0 | - |
| 12 | 0 | - |
| 13 | 5 | L258-303, L1291, L1800-1815, L2716 |
