# 前端面试工程审核报告（第 2 批：14-26 号文件）

> 审核日期：2026-11-13
> 审核范围：`14-agent-development.md` ~ `26-av-rtc.md` 共 13 个文件（约 4MB / 7.6 万行）
> 审核方式：逐文件大纲通读 + 高风险代码段逐段静态推演（null/undefined、边界输入、this 指向、循环/并发路径）+ 事实性声明核对（2025-2026 生态现值，含微信官方文档、Vite/Rolldown、MCP 协议、WebRTC 标准的联网核实）
> 本批共修复 **17 处**问题，未 commit，全部已直接落地到文件。

---

## 总体评价

这一批文件的**底子非常好**：题库结构统一（编号 + 追问链 + 评分点）、代码示例几乎都带边界处理与版本注释、过时说法在早前的 second-pass 中已大量清理。本轮发现的问题集中在三类：

1. **代码边界 bug**（最严重）：手写题和工具函数在多轮交互/特殊输入下会出错，属于「面试官现场多问一句就露馅」的类型，已全部修复；
2. **答案与注释/示例不一致**：示例输出、代码注释与实际执行结果对不上；
3. **生态现值补漏**：构建工具一章缺 2025-2026 最重要的变化（Rolldown 接管 Vite 构建底座），已补充。

各文件修复数量一览：

| 文件 | 修复数 | 严重度 |
|---|---|---|
| 24-handwrite.md | 6 | 高（3 处真实代码 bug） |
| 23-mock-interviews.md | 4 | 中（组卷不一致） |
| 15-algorithms.md | 2 | 高（LFU 语义 bug） |
| 14-agent-development.md | 2 | 中 |
| 19-miniprogram.md | 1 | 高（this 丢失） |
| 18-build-tools.md | 1 | 中（生态现值） |
| 22-soft-skills.md | 1 | 低（格式） |
| 16/17/20/21/25/26 | 0 | 抽查通过 |

---

## 逐文件问题清单与修复清单

### 14-agent-development.md（AGT-001 ~ AGT-200）

- **[已修] AGT-043 `parsePartialJson` 尾逗号边界 bug**：原实现 `out.slice(0, -1)` 只删最后一个字符，当流式前缀是 `{"a":1, `（逗号后跟空白）时删掉的是空白而非逗号，补全后仍是非法 JSON 导致返回 undefined。改为 `out.replace(/[\s,]+$/, '')` 连同尾部空白一起清理。
- **[已修] AGT-079 模型降级链事实性标注**：示例中 `deepseek-chat` 标记为 `supportsTools: false`，但 DeepSeek V3/R1 实际支持 Function Calling。已加注释说明这是「能力降级链」的示例结构，真实选型需按各厂商能力矩阵确认，避免面试时被当作事实错误。
- 通过抽查：AGT-041 SSE 解析器（跨 chunk 状态机、`TextDecoder stream:true`、flush）、AGT-028 最小 MCP server（JSON-RPC 2.0、initialize/tools list/call、2024-11-05 协议版本）、AGT-024 余弦相似度、AGT-149 流式 Markdown 栅栏补全、AGT-150 消息树——逻辑均正确。
- 现值核对：MCP 三角色（Host/Client/Server）、stdio + Streamable HTTP 传输、A2A 协议定位、AGT-180 框架选型描述均符合 2025-2026 现状。示例代码统一用 `gpt-4o-mini` 等占位模型名，属演示性质可接受。

### 15-algorithms.md（ALG-001 ~ ALG-200）

- **[已修] ALG-049 LFU 缓存语义 bug（本批最典型的"多想一层"题）**：原实现注释称「Map 迭代序 = 插入序，同频次自然取更早插入者」，但题意要求"次数相同时淘汰**最久未访问**者"——而 `Map.set` 对已存在的 key **不会刷新插入序**，`_touch` 只更新了频次 Map，导致同频次淘汰退化成按初始插入序。修复：`_touch` 中对 kv 显式 delete + set 刷新访问序，淘汰扫描改遍历 kv。这正是面试官追问「你的 LFU 真的按访问序淘汰吗」会翻车的点。
- **[已修] ALG-003 groupBy 与自身建议不一致**：答案文字强调「用 `Object.create(null)` 或 Map 避免 `__proto__` 污染」，代码却用 `{}` 作累加器。已改为 `Object.create(null)` 并加注释。
- 通过抽查：ALG-002 版本号比较归并、ALG-047/048 LRU 双实现、ALG-054 p-limit、ALG-055 指数退避 + 抖动、ALG-076 Kadane、ALG-078 Vue3 getSequence（含 p 前驱数组回溯的说明准确）、ALG-110/111/112 Promise 系列手写、交叉引用（ALG-166 等编号均真实存在）。

### 16-ops-release.md（OPS-001 ~ OPS-200）

- 抽查通过，无需修改：OPS-004 nginx 两级 map 尾号灰度（正则捕获 `$1` 用法正确）、OPS-005 灰度观测脚本（awk 分位数统计逻辑成立）、OPS-007 版本化目录 + symlink 原子切换、OPS-169 三级资源池 fallback（熔断表 + 递归降级逻辑正确）。
- 缓存分层（hash 资源 immutable 一年、html 协商缓存）、SRI、HSTS 渐进式下发等说法均为当前最佳实践。

### 17-architecture.md（ARC-001 ~ ARC-200）

- 抽查通过，无需修改：ARC-031 组件库 exports/sideEffects 双入口设计（JSON 字段写法正确）、ARC-032 focus trap（shift+Tab 首尾循环逻辑正确、关闭归还焦点）、ARC-020 pnpm workspace、ARC-025 幽灵依赖治理。
- 微前端、Monorepo、绞杀者模式等章节的观点与权衡表述均为当前主流共识。

### 18-build-tools.md（BLD-001 ~ BLD-200）

- **[已修] BLD-078 补充 Rolldown 现状（2025-2026 生态新考点）**：原文只讲「Vite dev 用 esbuild、build 用 Rollup」，缺 2025-2026 最重要的变化——Vite 团队用 Rust 重写的 Rolldown（基于 oxc）正接管生产构建，`rolldown-vite` 已可试用，兼容 Rollup 插件 API。已在 BLD-078 答案开头补充，并注明这是面试显著加分点。
- 抽查通过：BLD-052 webpack4→5 升级清单、BLD-073 Vite 快的根因、BLD-081/082 esbuild 原理与局限、BLD-192 双格式库工程化（exports 三条件写法正确）。

### 19-miniprogram.md（MP-001 ~ MP-100+）

- **[已修] MP-016 throttle 丢失 this（页面实例）**：示例节流器用箭头函数包装并以 `fn(...args)` 调用，`this.setData` 中的 `this` 不是页面实例，真机必报错。改为普通函数 + `fn.apply(this, args)`。
- **[核实无误] 包体积上限现值**：经联网核对微信官方文档，小程序「主包/单个分包 ≤ 2M、总包 ≤ 30M（服务商代开发 20M）」仍是上传现值，文件原表述准确（4M/40M 仅限本地预览与小游戏场景，不构成错误）。
- 抽查通过：MP-002 setData 通信链路、MP-014 分包路由限制、MP-045 登录流程、getUserProfile 接口回收（2022-10）等历史节点描述准确。

### 20-nodejs-bff.md（NODE-001 ~ NODE-200）

- 抽查通过，无需修改：NODE-002 nextTick/Promise 优先级与输出题（setImmediate 先于 setTimeout 的解释正确）、NODE-003 线程池（4 线程默认、UV_THREADPOOL_SIZE 上限 1024、线程池 API 清单完整）、NODE-004 CJS 循环依赖 partial exports、stream.compose、Slowloris 对策（requestTimeout 收紧建议）。
- Node ≥11 微任务时机与浏览器对齐的版本区分写法正确。

### 21-design-patterns.md（DP-001 ~ DP-200）

- 抽查通过，无需修改：DP-001 框架-模式映射表、DP-002 SRP 拆分示例、DP-003 OCP 注册表、DP-051 策略模式表单校验（执行逻辑与示例输出一致）、DP-052 转移表驱动状态机（非法转移抛错、转移日志）。
- 「框架源码即模式库」的对应关系（Pinia=单例、axios=适配器+拦截器链、tapable=职责链等）均准确。

### 22-soft-skills.md（SOFT-001 ~ SOFT-100）

- **[已修] SOFT-003 引号格式**：`是"找"回来+“算”出来的` 半角/全角引号混用，统一为半角。
- 内容层面（STAR 改写、量化五渠道、技能分档对照表、谈薪策略）方法论扎实，无事实性问题。

### 23-mock-interviews.md（MOCK-P01 ~ P20）

- **[已修] MOCK-P01「时间分配表」与「题目清单」不一致（组卷可信度问题）**：时间分配表列了 `JS-034、JS-037、HW-011`，题目清单却只有 13 题缺这三题。已核对三个编号在原题库中的真实题面后补入清单（含考察点与要点提示），清单数改为 16 题。
- **[已修] MOCK-P05 时间分配表缺题**：清单末两题 `BAS-150、PER-019` 未分配到任何环节，已在表中补「渲染与列表原理 5min」环节。
- 全 20 套卷的题号引用抽查（JS/V3/R19/SCN/OPS/ARC/BLD/MP/NODE/DP/VIZ/AV/AGT/HW/TS/SOFT/PER/ENG/XP 各前缀）均指向真实存在的题目；追问链设计（如 P08 的 FRP-148 MessageChannel vs setTimeout 4ms、P16 三支线）真实可信，符合大厂真实面试节奏。

### 24-handwrite.md（HW-001 ~ HW-060）——本批修复重点

逐题静态推演后修复 6 处：

- **[已修] HW-052 占位符柯里化多轮补参会「卡死」（最严重的代码 bug）**：原合并逻辑在 `curryPro((a,b,c)=>...)(_,_)(1)(_,3)(2)` 这类「新参数中含占位符」的场景下，会把新占位符**既保留旧洞又追加一份**（得到 `[1,_,_,3]`），永远凑不满 arity，函数永不执行——而注释声称该用例 `=== 6`。已按 lodash 语义重写合并算法：新参数中的非占位符按序填旧洞，占位符不参与填洞、剩余参数（含新洞）按原顺序追加，推演全部官方用例通过。
- **[已修] HW-045 `useDebouncePro` 卸载同步 effect 反而破坏防抖**：`useEffect(() => () => setDebounced(value), [value])` 的 cleanup 在**每次 value 变化时**都会执行，把上一轮旧值刷进 state，防抖失效。改为「ref 保存最新值 + 空依赖数组」的卸载专用 effect，并补注释说明这个陷阱。
- **[已修] HW-013 `myInstanceofPro` 的 Symbol.hasInstance 分支使手写遍历成为死代码**：所有函数都会沿原型链继承 `Function.prototype[Symbol.hasInstance]`，`typeof right[Symbol.hasInstance] === 'function'` 恒为真，下面的手写原型链遍历永远执行不到。改为用 `Object.getOwnPropertyDescriptor` 判断**自有属性**（class 静态自定义）才走委托分支，并加注释解释原因。
- **[已修] HW-024 `dedupDeep` 示例输出错误**：注释称 `[1, [2,3,[2,4]], 3, {a:1}, {a:1}] → [1, [4], {a:1}]`，实际按代码逐层推演（`seen` 全局共享）结果为 `[1, [2, 3, [4]], {a: 1}]`（内层 2、3 占用判重名额后外层 3 被去重）。已更正并补充语义说明。
- **[已修] HW-048 `controlPro` 防抖 + maxWait 双触发**：maxWait 兜底强制执行时未清掉挂起的 trailing timer，本次 + 末次会对 fn 连调两次。已在 maxWait 分支补 `clearTimeout`。
- **[已修] HW-049 `fetchWithAutoCancel` 注释与实现不符**：finally 注释说「超时后主动 cancel」但实际没有任何 cancel 调用，且第一个参数声明 `abort => ...` 形参未用。已简化为 `() => fetch(...)`，并把取消链路（abort 触发 → wrapped reject）在注释中讲清。
- 推演通过（未改动）：HW-001 Promise then 链（含 thenable 解析与防循环）、HW-007 p-limit、HW-014/015 防抖节流（immediate 与 timer 清理顺序正确）、HW-016 深拷贝（Map/Set/WeakMap/描述符处理完整）、HW-021 双向链表 LRU、HW-030 千分位手动循环版（逐位验算正确）、HW-036 rAF 时间驱动进度、HW-040/041/042 Hooks 简版、HW-059 JSON.parse 递归下降（严格版末尾校验、转义、Unicode 处理正确）、HW-060 计时器「累计+时间戳」法。

---

## 备考建议

1. **手写题按「评分点清单」练，不要只背代码**：本批在 24 中修的 5 个代码 bug 全部藏在「多一轮交互、多一个特殊输入」里（占位符柯里化、LFU 访问序、useEffect cleanup 时机、maxWait 双触发、Symbol.hasInstance 继承）。面试官现场最常见的加压方式就是「你这个实现在 XX 场景下还对吗」——把每题的「追问点」注释当考点复习。
2. **优先回炉的 6 道手写**（本批 bug 密度最高 + 出现率最高）：HW-013、HW-024、HW-045、HW-048、HW-052，外加结语中点名的 HW-001/014/016/021/040/050。
3. **算法题注意「Map 插入序」这一类隐性语义**：`Map.set` 已存在 key 不刷新顺序、`delete+set` 才会移位——LRU/LFU/keep-alive 一族题都靠它，一个细节决定答案对错（ALG-049）。
4. **构建工具补新考点**：Rolldown/oxc 接管 Vite 构建底座是 2025-2026 必问的新话头，BLD-078 已补；面试时「Vite dev=esbuild、build=Rollup」的老答案记得主动补一句 Rolldown 动向。
5. **模拟卷严格「计时 + 录音 + 复盘」**：23 的组卷已核对到题号级真实存在，按 P01→P04→P08→P11 的路径每卷录两遍，分数曲线不涨就回对应专题补「追问链第二层」。
6. **AI/Agent 岗**：14 的协议层（MCP/A2A）与工程化章节已是最新的，重点练 AGT-015 FC 时序、AGT-043 渐进 JSON（本轮修的尾逗号边界恰好是「你会怎么测试这个解析器」的好答案素材）。

## 本轮未修改但值得用户自查的点

- 示例代码中的模型名（`gpt-4o-mini`、`claude-3-5-sonnet` 等）为演示占位，正式面试口述时建议按目标公司技术栈替换为当年主流型号。
- 16/17/20/21/25/26 六个文件本轮抽查通过，但单文件篇幅均超过 300KB，如需「逐题全量推演」级别的复核，建议按本报告的抽查维度（并发/边界/this/版本现值）再过一遍目标岗位对应的 1-2 个文件。

---

# 第二轮：内容补全（2026-11-13）

针对第一轮审核报告指出的三处内容缺口，按各文件现有格式（题干 + **答** 要点 + 自洽代码块）直接落地新增题目，编号顺延各文件原有最大编号，共 **7 题**：

## 03-css.md（新增 CSS-201 ~ CSS-203，容器查询专题）

- **CSS-201 容器查询进阶：container-type 与 @container 完整语法**：`inline-size` 与 `size` 两种模式的本质区别（size 模式切断"高度由内容决定"，必须显式给尺寸否则塌陷）；范围比较语法、命名容器精确指向；style 查询（`@container style(--theme: dark)`）的 2025-2026 支持口径——Chrome/Edge 111+、Safari 18+，**Firefox 尚未支持，只能当渐进增强**。
- **CSS-202 cqw/cqh 容器单位**：六个单位与回退行为（无容器祖先时回退小视口单位，不会失效为 0）；与 vw/rem 的分层关系；点出常见误区——cq 单位参照**最近的容器祖先**，与 `container-name` 无关。
- **CSS-203 容器查询 vs 媒体查询分工与降级**：互补而非替代的决策口径；尺寸容器查询 2023 年起已是 Baseline（Chrome 105 / Firefox 110 / Safari 16）；三段式降级——基线样式在外、`@supports` 增强、旧浏览器 ResizeObserver 挂状态类兜底。
- 与既有 CSS-055（入门题）形成"入门 → 进阶语法 → 单位 → 选型降级"的完整链路。

## 11-scenario.md（新增 SCN-201 ~ SCN-202，LLM 流式/SSE 完整场景）

- **SCN-201 打字机效果前端主链路**：`EventSource` 为什么不满足（GET-only、无 Authorization、无自定义 body）→ `fetch` + `ReadableStream` 精简版 SSE 解析（`TextDecoder` `{stream:true}` 跨 chunk 解中文、空行分帧、`frames.pop()` 保留不完整尾帧、`data: [DONE]` 终止）；`AbortController` 全链路中断（含 React StrictMode cleanup 必须 abort、中断后保留已生成文本）；渲染节流——增量缓冲进 ref + `requestAnimationFrame` 每帧批量刷 state，React（useState + ref）与 Vue（shallowRef + onBeforeUnmount）两版对照。
- **SCN-202 上线后流式踩坑排查**：Nginx `proxy_buffering` 缓冲导致"整段一次吐出"（首选后端 `X-Accel-Buffering: no` 响应头自声明，或 location 级 `proxy_buffering off`；gzip 必须关）；`proxy_read_timeout` 掐断长回答 → 后端 SSE 注释行 `: ping` 保活（15s 间隔，客户端解析器天然忽略）；代理不可改时降级为一次性 JSON + 本地匀速动画；埋点 TTFT / 总时长 / 中断率分开上报。协议层完整状态机仍指向 AGT-041，未闭合代码块渲染指向 AGT-149，未重复造轮子。

## 09-performance-security.md（新增 PER-201 ~ PER-202，安全缺口）

- **PER-201 SRI 进阶**（静态标签基础见 PER-080）：动态 `createElement('script')` 与 `fetch(url, { integrity })`；ESM 盲区——入口 integrity 只校验入口文件，模块图需 import map 顶层 `integrity` 字段覆盖（Chromium/Safari 已支持，Firefox 落地较晚，建议查 caniuse 并以自托管兜底）；能力边界（只防传输篡改、不防源头投毒）；与 CSP 的正交组合，并点明 `require-sri-for` 未被浏览器广泛实现、方案不要依赖。
- **PER-202 Trusted Types 落地**：`require-trusted-types-for 'script'` 的机制（DOM-XSS sink 只收 TrustedTypes 对象）；2025-2026 支持口径——Chrome/Edge 83 起长期支持，Safari 18.2、Firefox 135（2025，先实验性随后默认开启）跟进，三大引擎齐备；渐进启用三步（report-only 收违规清单 → 显式 policy + default policy 兜底 → 切强制并保留 report-uri）；`default` policy 迁移期清洗放行、稳定后收紧为抛错的演进策略；DOMPurify 自动返回 TrustedHTML、polyfill 不提供真实防护需 CSP 兜底。
- 顺带修正 PER-200 两处「200 题」表述为「全部题目（含 PER-201/202 附录增补）」，避免文件扩容后自述失真。

## 本轮编写纪律

- 浏览器支持口径均以 2025-2026 实际行为核对（容器 style 查询 Firefox 缺位、Trusted Types 三引擎时间线、import map integrity 的引擎差异），不确定的版本号一律以「落地较晚/查 caniuse」表述，未编造具体版本。
- 所有代码块静态推演自洽：SSE 解析的状态转移（分帧、尾帧回填、DONE 提前返回并 `reader.cancel()`）、rAF 缓冲的 flush 与 abort 交错路径、import map 的合法 JSON 结构均已逐步核过。
- 新题编号顺延各文件原最大编号（CSS-200 / SCN-200 / PER-200 之后），未改动既有题目编号与交叉引用；新增题目中的交叉引用（CSS-055/194/201、AGT-041/149、PER-079/080）均指向真实存在的题目。

---

# 第四轮：全量正确性扫描（2026-11-17）

> 审核方式：全新独立第四轮。① 机检脚本基线比对 + 30/29/28/README 非编号文件的题号引用补查（audit.mjs 不覆盖这四个文件）；② 全库 734 个含 `console.log` 的 javascript 代码块用 Node 逐块实跑（提取脚本 + 5s 超时隔离），失败块逐一回原文判定是「教学性报错演示/浏览器 API 环境缺失」还是真 bug；③ 输出题答案与实跑 stdout 逐条比对；④ 高风险事实断言（ES2024/2025、React 19、Vue 3.5、TS 5.x、HTTP/CORS/缓存、性能数字、小程序限额）定向 grep + 精读核实，存疑处联网核对（本次核实了 Vue 3.5 懒水合 API 形态）。
> 本轮共发现 **8 处**问题（7 处技术问题 + 1 处文件损坏），全部修复落地；另有 5 项「疑似」留档未改。

## 一、新发现问题与修复清单

| # | 文件 | 位置 | 问题 | 证据 | 修复方式 |
|---|---|---|---|---|---|
| 1 | 01-web-network-browser.md | WEB-119（约 L3599） | SharedWorker 示例 `port.onmessage` 里引用了**未定义的 `ports`**（只定义了 `port`），照抄运行必 ReferenceError，且「路由中心」转发逻辑无从谈起 | 静态走读：`onconnect` 内只有 `const port`，`ports.forEach` 无来源 | 模块级建 `const ports = []` 连接表，`onconnect` 先登记再转发（排除发送者自身），补 `port.start()` |
| 2 | 02-html5.md | H5-090（约 L3747） | `quickHash` 中段抽样 `Math.floor(file.size / 2) + 2 << 20` **运算符优先级错误**（`+` 高于 `<<`），实际算出 `(中点+2)<<20` 的天文数字，slice 钳制后中段抽样退化为「中点→文件末尾」整段 | `+` 优先级高于 `<<`；对比同行尾块 `file.size - (2 << 20)` 有括号 | 补括号 `+ (2 << 20)` 并加注释 |
| 3 | 04-javascript.md | JS-141（L5186-5218） | **双重错误（本轮最严重）**：① 代码在 `run()` 内部调用 `stolen()`，而 `stolen === inner.run`，构成**无限递归**——非严格模式无限打印 4/5 直到栈溢出（Node 实测复现），严格模式先在 `this.name` 上 TypeError，原声称输出在任何环境都跑不出来；② 原声称输出还漏掉了 `stolen()` 独立调用产生的行 | 实跑复现：非严格 CJS 输出 183KB+ 的 `4 undefined/5 undefined` 循环 | 把 `stolen()` 提到 `run` 外部调用并注明「放 run 内部会无限递归调自己」；按实测更正输出注释为 `1 outer → 2 outer → 4 inner → 5 inner → 6 inner → 4 undefined → 5 undefined → 6 undefined → 3 undefined`，补严格模式 TypeError 追问点 |
| 4 | 06-vue3.md | V3-120（L4936） | 「Vue3.5 的 defineLazyHydration 宏」**API 名称不存在**。联网核实（Vue 官方博客与文档）：Vue 3.5 的懒水合是 `defineAsyncComponent` + `hydrate` 选项（内置 `hydrateOnVisible/hydrateOnIdle/hydrateOnInteraction/hydrateOnMediaQuery` 策略函数）；`defineLazyHydrationComponent` 是 **Nuxt** 的编译宏 | Vue 官方 blog.vuejs.org/posts/vue-3-5 与 vuejs.org Async Components 指南 | 更正为 Vue 官方 API 形态，并指明 Nuxt 宏是对它的上层封装 |
| 5 | 15-algorithms.md | ALG-115（L2534） | `myCall` 用 `defineProperty` 挂临时属性**未声明 `configurable: true`**（默认不可配置），`finally` 里的 `delete` 在严格模式（ESM/class）下直接 TypeError——示例自身即崩溃。Node 实跑复现：打印结果后 `Cannot delete property 'Symbol(fn)'` | 实跑复现 | 补 `configurable: true` 并注释说明这是「defineProperty 默认不可配置」的坑（本身也是考点） |
| 6 | 21-design-patterns.md | DP-027（L1124-1133） | axios 派发层 `{ xhr, http }[name]` 漏掉 **adapter 为函数**的分支，紧接着文档自己给出的「注入 mock」示例第二行就 `TypeError: adapter is not a function`（实测复现）——示例与文字声称（"自定义 adapter 注入 mock"）矛盾 | 实跑复现 | 补 `typeof name === 'function'` 分支，加注释说明两种注入形态 |
| 7 | 21-design-patterns.md | 组合模式题（L1583） | ` ```javascript ` 代码块里使用 **TS 专属语法 `abstract class`**，按 JS 解析直接 SyntaxError（其余 abstract class 均在 typescript fence 中，核对无误） | 实跑复现：`Unexpected token 'class'` | 去掉 `abstract` 关键字，保留基类方法抛错的「模拟抽象约束」写法并加注释 |
| 8 | 30-company-styles.md | 文件尾（原 L793-795） | **文件损坏**：末尾混入 3 行 ZCode shell 包装残留（`__zcode_status=$?` / `pwd -P > /var/folders/...` / `exit ...`），markdown 渲染会露出裸 shell 文本 | tail 查看复现 | 删除残留 3 行，文件恢复为 792 行、以正文收尾 |

## 二、疑似问题（留档未改，附理由）

1. **WEB-191 Redis 广播频道名**：`pub.publish('chat:*', ...)` 把字面量通配符当频道名发布。`psubscribe('chat:*')` 的 glob 恰好能匹配到字面量 `chat:*` 频道，且消息体带 `room` 由订阅端二次过滤，功能可跑通；但与答案「按频道分片」的叙述相悖、生产不应这么写。可运行，属代码品味问题，未改。
2. **反例+正例同 fence 的重复声明**：04（JS-017/064/144）、21（DP-002/003）等多个代码块把「反例 + 正例」写进同一个 fence，整块粘贴会因重复声明 SyntaxError。这是库内一贯的「多文件/多片段演示」风格，前几轮已接受，本轮未改；备考按片段粘贴即可。
3. **27-cross-platform.md L5323 mindmap「心法（贯穿七域）」**：机检启发式对全角括号告警——mermaid 标签内全角括号合法（ASCII 括号才是 shape 语法），确认误报，未改。
4. **23-mock-interviews.md 20 处「缺 **答**」**：机检按题库格式假设对模拟卷报错，试卷本无逐题「**答**」格式，确认误报，未改。
5. **WEB-019 「Range 头属于需预检的非简单头」**：fetch 规范 2022 年起已把单段 `Range`（`bytes=` 形式）纳入 CORS-safelisted 请求头，新版浏览器对简单 Range 不再预检，旧引擎仍预检。原表述在旧引擎下成立、偏保守，不算错误；如追求严格可补一句版本差异，未改。

## 三、机检结果

- `node tools/audit.mjs` 复跑：**4937 题**、题号连续性/引用/围栏平衡全绿；仅存上表「疑似 3/4」两处已知误报（23 的 20 条格式误报、27 的 1 条 mermaid 误报），与基线一致，本轮改动未引入新告警。
- 补充校验（audit 不覆盖的 4 个文件）：30/29/28/README 中全部 `XX-NNN` 题号引用比对题库 registry，**无死链**。
- 734 个含 `console.log` 的 javascript 代码块实跑：除「教学性报错演示」（TDZ/TypeError 演示等）与「浏览器 API/依赖包环境缺失」（document/window/echarts/workbox 等）两类预期失败外，本轮已修复 #1/#3/#5/#6/#7 共 5 个真不可运行块；02-H5-090 属可运行但语义错误，同修。

## 四、本轮统计

- 扫描篇数：33（01~30 全部题库 + README + 23/24 两个专项文件；代码级实跑覆盖全库，事实断言精读覆盖 01/02/03/04/05/06/07/09/10/11/12/13/15/18/20/21/24/28/29/30）。
- 新发现问题：8 处；修复落地：8 处；遗留疑似：5 项（均留档未改）。
- 最严重三处：JS-141 无限递归（任何声称输出都跑不出来）、ALG-115 示例自身崩溃、DP-027 示例第二行崩溃——三者都是「面试现场跑一遍就穿帮」级别，均已用 Node 实测验证修复后输出。

## 第五轮:遗留疑似项处置(2026-11-17,主会话)

第四轮留档 5 条疑似,本轮逐条取证处置:
1. WEB-019「CORS 下 Range 属需预检头」表述偏保守 → **已修**(联网核实 fetch 规范 2022 起单区间 Range 进入 safelist):改为「单区间 Range 不再触发预检;Content-Range 需 Expose-Headers 放行;多区间 Range 仍需预检」,audit 4937 题复跑结论不变;
2. WEB-191 `publish('chat:*')` 字面量通配符频道 → **确认关闭**:实跑可运行且文中有「演示用字面量」语境,不改叙述;
3. 反例+正例同 fence 的重复声明风格 → **确认关闭**:库内一贯约定(刻意展示错误写法),非问题;
4. 27 mindmap 全角括号机检误报 → **确认关闭**:mermaid 全角括号在节点名内合法渲染,属机检规则过严;
5. 23-mock-interviews 20 条「缺 **答**」机检误报 → **确认关闭**:该文件为追问链式排版,与标准问答格式不同,属机检规则未覆盖该体裁。
结论:1 修 4 关,audit 保持全绿(13 项历史误报口径不变)。

## 第九轮(收尾,主会话):audit 误报清零
1. 跨文件重名题 2 组 → 0:PER-009/OPT-009/SCN-012 标题角度化改写(题号不动,内容不变,与 BAS-168/H5-033 的既有角度自然区分);
2. audit.mjs 两处校准:MOCK-P*(模拟卷卷首,非问答条目)跳过「答」结构检查;mermaid 节点文本只拦 ASCII 括号(全角括号合法);
3. 复跑:`node tools/audit.mjs` → **SUMMARY: 0 problem(s)**(此前 13 项全为误报),4937 题与重名检查不变。
