# 审稿 B9-P8：08.第八期（19 篇）专家复核报告

- 审稿对象：`work/target/25-lowcode/posts/08.第八期/`（28-4~28-9、29-1~29-3、30-1~30-6、31-1~31-4，共 19 篇；JMeter 压测全流程 + Redis 缓存优化 + 简历/面试收尾）
- 真源对照（SRC）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`——本批重点核对 `packages/server/src/main.ts`（端口 3000）、`src/low-code/low-code.controller.ts`（low_code 路由/@Public/page_id）、`src/utils/modules/redis.module.ts`（getCachedData）、`src/user/dto/login.dto.ts`（PasswordLoginDto=phone+password）、`src/common/{ResponseIntercept,AbnormalFilter}.ts`（{code,data,msg} / code=-1）、`docker-compose.yml`、`packages/share/src/utils/componentExport.ts`、`packages/client/src/hooks/`、`nginx/server.nginx.conf`
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`（重点 A1/A2）、`reports/review-eng-b.md`（表述风险清单）、`reports/review-b5-p4.md` / `review-b6-p5.md`（判例：标题以文件名引用名为准改偏离方；API/类型/字段名一律以 SRC 为准；命名别名首次括注）
- 外部核实（JMeter 行为类断言）：jmeter-server 属**从节点/压力机**脚本、**监听器会随 .jmx 保存**（只不保存采样结果数据）、Open Model Thread Group 为 JMeter 5.5+ 内置（本批说法正确）、`bin/templates/simple-http-request-test-plan.jmx` 真实存在。来源：[Apache JMeter 用户手册](https://jmeter.apache.org/usermanual/component_reference.html)、[JMeter 分布式压测官方分步指南](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf)、[Baeldung: JMeter Distributed Testing](https://www.baeldung.com/jmeter-distributed-testing)、[JMeter 监听器中文文档](https://jmeter.xiniushu.com/listeners)、[CNBlogs: Open Model Thread Group](https://www.cnblogs.com/jiushao-ing/p/17647366.html)
- 审查维度：技术硬伤（JMeter 组件/线程组/断言/聚合报告数字口径、Redis getCachedData 命名与 TTL 600s 口径、QPS 与 30-6 已修限定一致性）· 代码/命令块可执行性 · 六段结构与互链真实 · 去 AI 味
- 结论口径：【合格】= 无 P0/P1（可附 P2 建议）；【需修】= 存在 P0/P1。只出报告，未改任何文件。

---

## 〇、残留复查（对齐 scan6 / review-eng-b 已修点）

| 检查项 | 结果 |
|---|---|
| A2-1/A2-2 30-6 `getCachedData` 命名 + `{ ttl: 60 * 10 }`（600s） | 无回潮：L11 导语、L37/L42 代码块、L118 小结全部正确；「注释态/未合入主线」限定说明在 L11 与 L88 都有 |
| A2-3 30-6 伪代码（删 del、set 带 'EX'） | 主体无回潮；连带发现 1 处小瑕疵（`this.set` 四参与 SRC `set(key,value,time?)` 三参封装不符），见 30-6 条目 2，判 P2、非回潮 |
| A2-4/A2-5 30-6 force 口径 + 推广段限定 | L48/L118「并非显式 del」正确；**L119 小结残留「清空旧缓存」旧口径**，与 L48/L118 自相矛盾，本次上报（30-6 条目 1，P2） |
| A1 RBAC→接口权限守卫 | 本批 0 处 RBAC 表述 |
| `/local/...` 旧路由（b6 簇一） | 本批 0 处；但发现**新变体 `/api/local_code/release`**（应为 `low_code`）2 处，见簇二 |
| 20-8 / 19-4 等 b6 清单外残留 | 均在 05.第五期，不在本批范围 |
| review-eng-b 风险 #2/#19（防刷体系、防重提交） | 本批技术篇（30-4/30-5）未写「完整防刷体系」，仅 31-4 简历亮点写「原子性防重提交」超出现状，P1 上报 |

六段结构：19 篇均为「H1 + 导语（blockquote）+ 前置知识 + 正文 + 小结 + 下一步」，无缺段。互链：本批出链 49 处书名号引用全部指向真实篇目（含 00 期 1-1、01 期 2-5/2-6/2-9、02 期 8-1、06 期 22-4、07 期 28-3 跨期引用），无死链；入链（07 期 28-3 →《多环境快速安装Jmeter5》）与文件名口径一致。

---

## 一、共性簇（跨篇问题，逐篇条目只留指针）

### 簇一：标题/H1 与文件名（= 全批引用名）不一致（14 篇，31-4 判 P1，余 P2）

系列口径（b5-p4 簇一、b6-p5 簇三）：引用名按文件名标题书写，**改偏离方的 title/H1，引用方不动**。29-1/29-2/30-6 与引用名仅「JMeter/Jmeter」大小写差异，不算断链（可顺手统一）：

| 篇 | 实际 title/H1 | 引用名（引用方） | 建议 | 严重度 |
|---|---|---|---|---|
| 28-4 | 多环境快速安装 JMeter 5.x | 《多环境快速安装Jmeter5》（28-5 L15、28-6 L46、07期 28-3 ×2） | title/H1 改为引用名 | P2 |
| 28-5 | JMeter 5.x 基础功能组件：线程组与取样器 | 《Jmeter5.X基础功能组件+线程组和取样器》（28-4 L98、28-6 L15） | 改为引用名 | P2 |
| 28-6 | JMeter 5.x 查看测试结果：结果树与聚合报告 | 《Jmeter5.X查看测试结果结果树+聚合报告》（28-5 L86、28-7 L15、30-5 L15） | 改为引用名 | P2 |
| 28-7 | 低代码发布页面获取组件接口的 JMeter 性能测试实战 | 《低代码发布页面获取组件的Jmeter性能测试》（28-6 L73、28-8 L15、30-6 L15） | 改为引用名 | P2 |
| 28-8 | 特殊线程组 setUp/tearDown 与调度器实战 | 《特殊的线程组setUP-tearDown和调度器实战》（28-7 L59） | 改为引用名 | P2 |
| 28-9 | HTTP 取样器复用与 HTTP 请求头管理实战 | 《Http取样器复用和Http请求头管理实战》（28-8 L76、29-1 L15、30-5 L16） | 改为引用名 | P2 |
| 29-3 | 高并发业务下 JMeter 集合点（同步定时器）应用实战 | 《高并发业务下Jmeter集合点应用实战》（29-2 L78、30-1 L15） | 删「（同步定时器）」或整体改为引用名 | P2 |
| 30-1 | JMeter 压测接口实战：用户登录接口 | 《Jmeter 压测接口—用户登录接口》（29-3 L60、30-2 L15/L53、30-3 L36） | 改为引用名 | P2 |
| 30-2 | JMeter 压测接口实战：获取问卷组件接口 | 《Jmeter 压测接口—获取问卷组件接口》（30-1 L53、30-3 L15） | 改为引用名 | P2 |
| 30-3 | JMeter 压测接口实战：获取问卷数据接口 | 《Jmeter 压测接口—获取问卷数据接口》（30-2 L65、30-4 L15） | 改为引用名 | P2 |
| 30-4 | JMeter 压测接口实战：用户提交问卷接口 | 《Jmeter 压测接口—用户提交问卷接口测试》（30-3 L48） | 改为引用名（勿丢「测试」二字） | P2 |
| 30-5 | JMeter 压测接口：发布页面是否提交过问卷接口 | 《Jmeter 压测接口—发布页面是否提交过问卷接口》（30-4 L56、30-6 L15） | 「：」改「—」 | P2 |
| 31-2 | 大厂面试官角度告诉你：项目经验需要注意的事情 | 《大厂面试官角度告诉你-项目经验需要注意的事情》（31-1 L68、31-3 L15、31-4 L15） | 「：」改「-」 | P2 |
| 31-3 | 全栈高级工程师简历—小滴官网全栈项目 + 低代码项目模板与技术栈讲解 | 《全栈高级工程师简历—小滴官网全栈项目+低代码项目简历模板和技术栈讲解》（31-1 L68、31-2 L70、31-4 L16） | 改为引用名（现题漏「简历」二字） | P2 |
| **31-4** | **简历实战：把低代码平台项目写进全栈高级工程师简历** | 《全栈高级工程师简历—低代码项目大课项目讲解》（31-1 L68、31-2 L70、31-3 L78，共 3 处） | title/H1 改为引用名 | **P1** |

（29-1、29-2、30-6、31-1 标题与引用名一致或仅大小写差。）

### 簇二：`/api/local_code/release` 路由不存在（2 处，P1）

SRC 为 `@Controller('low_code')` + 全局前缀 `api`，C 端公开接口是 `GET /api/low_code/release?id=`（low-code.controller.ts L33-36，`@Public()`）。`local_code` 在 SRC 与全库中均不存在，读者照抄会 404：

| 篇 | 位置 | 现状 | 应为 |
|---|---|---|---|
| 28-5 | L62 | 路径填 `/api/local_code/release` | `/api/low_code/release?id=3` |
| 28-7 | L15 | `HTTP GET /api/local_code/release` | `HTTP GET /api/low_code/release?id=3` |

### 簇三：统一响应字段口径 `{code, data, msg}`（P2）

SRC `ResponseIntercept` 成功返回 `{code: 0, data}`（或含 `msg`），`AbnormalFilter` 失败返回 `{code: -1, data: null, msg}`：

- 28-9 L69：「`code = 0`、`message = 登录成功`」→ 字段是 `msg`（passwordLogin 返回 `{data: token, msg: '登录成功'}`）。
- 29-2 L23：示例 `{"code":1,"message":"密码错误"}` → 实际是 `{code: -1, data: null, msg: '密码错误'}`（字段与 code 值都不对）。

### 簇四：配套资料路径在协作工作区不存在（P2，沿 b6 簇四判例）

- 30-5 L50、30-6 L112：「`安装包（已8期）/安装包（已8期）/apache-jmeter-5.6.3/apache-jmeter-5.6.3/backups/`」——嵌套重复疑似转写残留，且路径在工作区不存在。
- 30-6 L50/L90：「`代码（已8期）/30-6/lowcode`」「`代码（已8期）/30-6/lowcode/docker-compose.yml`」。
- 31-1 L56、31-2 L15、31-4 L17：「`简历/简历/高级前端开发工程师简历【前端大课+低代码】.docx / .pdf`」。

建议统一改「课程配套资料/简历模板」泛指，或删除具体路径。

### 簇五：「release 控制器 / 无参数」表述（P2）

28-5 L53/L60 与 28-6 L15 把压测目标说成「`release` 模块/控制器、GET、免登录、无参数」。SRC 里 release 是 **low-code 模块 `LowCodeController` 的方法**，端口 3000 来自 `src/main.ts` 的 `app.listen(3000)`（无 `src/version.ts`），且接口带 `?id=` 查询参数（不带 id 时 TypeORM 空条件返回表中第一条，review-eng-b P2#2）。建议表述为「low_code 控制器的 release 方法，GET、免登录、仅需 `?id=` 页面参数」。

---

## 二、逐篇明细

### 28-4.多环境快速安装Jmeter5 — 需修

1. 【P1】L54 分布式脚本角色写反：原句「分布式压测主节点：启动 `jmeter-server`（Windows 下为 `jmeter-server.bat`）。这是后续做分布式压测时才用到的」→ `jmeter-server` 是在**各台压力机（从节点）**上启动 RMI 引擎的脚本；主节点（控制机）仍用 `jmeter`/`jmeter.bat`，通过 `remote_hosts` 或 `-R` 远程调度压力机。建议改为「分布式压测的各台压力机（从节点）：启动 `jmeter-server`……主节点用 `jmeter` 并远程启动它们」。照原文搭分布式会把主从角色装反。
2. 【P2】L2/L9 title/H1「多环境快速安装 JMeter 5.x」→ 引用名《多环境快速安装Jmeter5》（簇一）。
3. 【P2】L63-65 macOS 启动方式：原句「双击 `bin/jmeter` 脚本，系统会自动拉起一个终端窗口执行启动逻辑」→ macOS 双击无扩展名脚本默认不会执行（一般以编辑器打开），建议改「终端内执行 `sh jmeter`（或 `chmod +x` 后 `./jmeter`）」；Windows 保持「双击 jmeter.bat」。

（JDK 8 要求、5.6.3 版本、`language=zh_CN` 汉化法、目录说明均无问题。）

### 28-5.Jmeter5.X基础功能组件+线程组和取样器 — 需修

1. 【P1】L62 路径不存在（簇二）：`/api/local_code/release` → `/api/low_code/release?id=3`。顺带把 L53「不需要登录、GET 方式、无参数」的「无参数」改为「仅需 `?id=` 页面参数」——该接口带 id 查询参数（28-6/28-7 的演示数字也以同接口为前提）。
2. 【P2】title/H1 断链（簇一）。
3. 【P2】L60：「端口号 3000（后端默认端口，来源于 `src/version.ts` 或启动配置）」→ SRC 无 version.ts，端口来自 `src/main.ts` 的 `await app.listen(3000)`，建议改「来源于 `main.ts` 的启动配置」。
4. 【P2】L53：「（对应代码 `packages/server/src` 中端口 3000 的 release 模块）」→ 应为 low-code 模块（`low-code.controller.ts` 的 `getReleaseData` 方法），见簇五。

（线程组三参数与算例、取样器、`开放模型线程组` 为 JMeter 5.5+ 内置组件的说法均经核实正确。）

### 28-6.Jmeter5.X查看测试结果结果树+聚合报告 — 需修

1. 【P1】L53/L59 监听器保存说法与 JMeter 实际行为相反：原句「**监听器（查看结果树、聚合报告）本身不会被保存到 `.jmx` 文件里**……打开后需**手动重新添加**查看结果树与聚合报告」→ .jmx 会把测试计划树里的全部组件（含监听器 `ResultCollector`）一并序列化保存；**不会保存的只是采样结果数据**，重开脚本后监听器仍在、只是空列表。建议改写为「.jmx 会保存监听器本体，不会保存运行产生的结果数据；重开脚本监听器还在但为空。正式压测建议删掉/禁用 GUI 监听器，用命令行 `-l` 写结果文件」。按原文操作会把「每次手动重加监听器」当成必需步骤。
2. 【P2】title/H1 断链（簇一）。
3. 【P2】L15：「课程后端 `release` 控制器（GET、免登录、无参数）」→ 簇五改法。

（监听器作用域三档、90% Line 误读纠正、`sampleresult.default.encoding` 修复法、平均值 74ms 等数字均无问题。）

### 28-7.低代码发布页面获取组件的Jmeter性能测试 — 需修

1. 【P1】L15 路径不存在（簇二）：`HTTP GET /api/local_code/release` → `HTTP GET /api/low_code/release?id=3`。
2. 【P2】title/H1 断链（簇一）。

（清空按钮、样本 10/平均 74ms/吞吐量口径与 28-6 自洽，90% Line 纠偏无问题。）

### 28-8.特殊的线程组setUP-tearDown和调度器实战 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）：改《特殊的线程组setUP-tearDown和调度器实战》。

（三类线程组执行顺序、职责划分、监听器作用域回顾、调度器「持续时间/启动延迟」、须配「永远」循环的说法均成立——有限循环次数下持续时间只作为上限、不会延长运行，原文口径可保留；「约 13 秒」= 3s 延迟 + 10s 持续，自洽。）

### 28-9.Http取样器复用和Http请求头管理实战 — 需修

1. 【P1】L45-50 登录请求体字段名错误：原句 JSON `{"account": "你的账号", "password": "你的密码"}` → SRC `PasswordLoginDto` 只有 `phone` + `password` 两个 `@IsNotEmpty` 字段（user.service.ts L141 `passwordLogin({ phone, password })`）。按 `account` 发送 DTO 校验直接 400，后文「加上 Content-Type 后返回登录成功」的场景就复现不出来。改为 `{"phone": "你的手机号", "password": "你的密码"}`。
2. 【P2】title/H1 断链（簇一）。
3. 【P2】L69：「`code = 0`、`message = 登录成功`」→ `msg` 字段（簇三）；完整响应为 `{code: 0, msg: '登录成功', data: token}`。

（Request Defaults/Header Manager 作用域、JMeter 默认 `Content-Type: text/plain` 的坑、L71 模板路径 `bin/templates/simple-http-request-test-plan.jmx` 真实存在，均无问题。）

### 29-1.Jmeter实战之压测结果聚合报告分析 — 合格（无 P0/P1）

数字自洽性核过：500 线程持续 20s 得 2174 样本、平均 RT 约 4s、吞吐 95.1/s——2174/95.1 ≈ 22.9s（调度 20s + 长 RT 尾部收尾），500 并发 × 4s RT 的理论上限约 125/s，与 95.1/s 吻合；与 30-1「1 样本 / 55ms / 18/s」（1/0.055≈18.2）同口径。聚合报告列名（Median/90%/95%/99% Line/Error%/Throughput/收发 KB/sec）与 JMeter 5.6 实际一致，90% Line 口径与 28-6/28-7 一致。

1. 【P2·可选】L21-25 TPS「侧重增删改」、QPS「侧重查询」为课程简化口径（严格定义上 TPS/QPS 不按读写划分），文中已有「日常口语常混用」的注解兜底，可不改。

### 29-2.Jmeter实战压测结果之响应断言 — 合格（附 P2 建议）

1. 【P2】L23：示例响应 `{"code":1,"message":"密码错误"}` → SRC AbnormalFilter 实际返回 `{code: -1, data: null, msg: '密码错误'}`（簇三）。该例是「假成功」的示意，读者也可能照此写断言模式，建议按实名改。
2. 【P2】title 与引用名仅 JMeter/Jmeter 大小写差异，顺手统一即可。

（「打勾=仅看 HTTP 状态」、断言作用域、字段/匹配规则清单（Contains/Matches/Equals/Substring/Not/Or）、Matches 正则开销提醒均正确。）

### 29-3.高并发业务下Jmeter集合点应用实战 — 合格（附 P2 建议）

1. 【P2】L46 转写残留：「并发量 **smaller**，QPS 反而更高」→ 中英文混排残留，改「并发量更小」。
2. 【P2】L44/L46 数字与叙事张力：两场景都宣称「线程凑齐后**同一刻打出**」，但按齐发口径算，100 并发（avg RT 255ms）应在约 2s 内收尾、吞吐约 40~60/s；实测 5.5/s（elapsed≈18s）与 50 并发的 48.9/s（elapsed≈1s）都表明请求是线程陆续启动后**分批快速放行**的（10ms 超时下未凑满也放行）。建议把叙事改为「受线程启动速度影响，实际是快速分批放行」，或补一句两场景的 Ramp-Up 设置，避免「严格瞬时 100 并发」的过度宣称；结论「并发越高吞吐越低、延迟越高」不受影响。
3. 【P2】title/H1 断链（簇一）。

（Synchronizing Timer 两参数英文名、超时 0=无限等待、组数≤线程数且最好整除、>0 超时防卡死等均正确。）

### 30-1._Jmeter_压测接口—用户登录接口 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）：30-x 系列引用名统一为《Jmeter 压测接口—××》。
2. 【P2】L42：「登录接口涉及**写库**/查库与 token 生成」→ `passwordLogin` 只查库（findOneBy）+ 比对 + 签发 JWT，无写库；改「涉及查库与 token 生成」。

（「三个 1」跑通、默认值/Header Manager 全局复用、逐步加压法回链、1 样本 55ms→18/s 均无问题。）

### 30-2.Jmeter_压测接口—获取问卷组件接口 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）。
2. 【P2】L33-34：全文未给出实名路径（「对照 Postman 里……把路径粘贴进来」），建议补 `GET /api/low_code/question_components`——SRC 该接口无查询参数、需登录，与文中「GET 且无参」的说法正好一致，补上即可完全落地。

（Bearer 空格提醒、信息头多条目共存、正则/JSON 提取器展望、1 样本 51ms→19.6/s 均无问题。）

### 30-3.Jmeter_压测接口—获取问卷数据接口 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）。
2. 【P2】L27：同 30-2，建议补实名 `GET /api/low_code/question_data`（SRC 按登录用户 id 查、无查询参数）。

（GET+鉴权+无请求体、线程组内自动继承默认值/鉴权头、QPS/TPS 混用口径均无问题。）

### 30-4.Jmeter_压测接口—用户提交问卷接口测试 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一，注意保留「测试」二字）。
2. 【P2】L36：「路径中含 **questionnaire**/question 相关数据标识」→ SRC 无 questionnaire 字样，实名是 `POST /api/low_code/question_data`（`@Public()`，body 为 `{page_id, props}`）。建议删除含混括注、直接写实名路径，读者才能落地。
3. 【P2】L42/L51：成功文案「提交成功，感谢您的参与」→ SRC 为「提交成功！感谢您的参与！」（postQuestionData 返回 msg），顺手对齐标点。

（抓包取真实入参再转 JSON 的做法、写库接口加压注意项均无问题。）

### 30-5.Jmeter_压测接口—发布页面是否提交过问卷接口 — 需修

1. 【P1】L26/L33/L55 查询参数名错误：`pageId`（且解释为「配置 ID」）→ SRC `@Query() { page_id }`（low-code.controller.ts L41-45），参数名是 **`page_id`**、语义是**发布页面 ID**。照 `pageId` 传参后端取不到，`page_id` 为 undefined 会被 TypeORM 忽略、退化为仅按 user key 匹配任意页面，「是否提交过」的结果失真。表格（L30-33）与小结三处同步改，并去掉「配置 ID」表述（b6-p5 对 20-3 `configId→page_id` 同判例）。
2. 【P2】title/H1 断链（簇一）。
3. 【P2】L39：「接口返回『提交过问卷』」→ 接口实际返回 `data: true/false`（`!!isExist`）；「您已提交过问卷……」是前端 ComponentRender 的展示文案，建议区分「接口返回布尔 / 前端文案」。
4. 【P2】L50 资料路径嵌套重复且不存在（簇四）：「安装包（已8期）/安装包（已8期）/apache-jmeter-5.6.3/apache-jmeter-5.6.3/backups/」→ 改「课程配套资料的 apache-jmeter-5.6.3/backups 目录」泛指。

（禁用其它线程组、清空历史结果、18ms→55/s 的单样本口径自洽，均无问题。）

### 30-6.Jmeter_压测接口—优化获取低代码组件接口性能 — 合格（附 P2 建议；A2 已修点无回潮）

残留复查结论：`getCachedData` 命名、`{ ttl: 60 * 10, force: false }`（600s）、伪代码无 `del`、force「并非显式 del」、注释态/未合入主线限定说明（L11/L88）、QPS「428~440 vs 410、样本仅 800 个」的诚实口径——全部在位且与 scan6 A2 修法一致；L92-110 的 docker-compose YAML 与 SRC 逐字一致（省略 restart/extra_hosts 属合理摘录）。以下为本次新发现：

1. 【P2】L119 小结残留旧口径：「`force` 用于强制刷新、**清空旧缓存**」与 L48/L118「并非显式 del」自相矛盾（A2-1 修的就是这句的正文版）。建议改「`force` 用于强制刷新（跳过缓存、回源覆盖写回）」。
2. 【P2】L57-67 伪代码调用签名瑕疵（scan6 A2-3 修法的连带，非回潮）：块内 `this.set(key, JSON.stringify(data), 'EX', options.ttl)` —— SRC 的 `RedisModule.set(key, value, time?)` 是**三参**封装，四参 `'EX'` 形态出现在 `getCachedData` 里直接调 ioredis 原生 `this.redis.set(key, JSON.stringify(data), 'EX', options?.ttl ?? 3600)`。若读者照伪代码在本模块内写 `this.set(..., 'EX', ttl)`，`'EX'` 会落进 `time` 位导致 TTL 丢失。建议把块内调用改为 `this.redis.set(...)`，或旁注「此处为 ioredis 原生 set，非本模块的 set 封装」。
3. 【P2】L50/L90/L112 资料路径（簇四）。

### 31-1.全栈高级工程师简历编写实战—个人技术栈模块 — 合格（附 P2 建议）

1. 【P2】L56 资料路径（簇四）：`简历/简历/高级前端开发工程师简历【前端大课+低代码】.docx / .pdf` → 泛指。
2. 【核实无问题】L15 四篇跨期引用（1-1、2-9、2-5、2-6）真实存在；「不写精通」「有横有纵」「四个注意点」为方法论内容，与 SRC 无冲突；L52 把 JMeter 压测与云效 DevOps 挂到「可写进简历」与本系列 28-30 篇内容自洽。

### 31-2.大厂面试官角度告诉你-项目经验需要注意的事情 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）：「：」改「-」。
2. 【P2】L15 资料路径（簇四）。
3. 【核实无问题】《Jmeter性能压测—基本介绍和使场景》引用名与 07期 28-3 实际标题一致（「使场景」是 07期标题自带的笔误，非本批之错）；L50「对部分性能较差的接口，还做了 Redis 缓存或代码层面的优化」与 30-6 限定说明不冲突（课堂演示确实完成，未合入主线不影响面试口径）。

### 31-3.全栈高级工程师简历—小滴官网全栈项目+低代码项目简历模板和技术栈讲解 — 合格（附 P2 建议）

1. 【P2】title/H1 断链（簇一）：现题漏「简历」二字且「+」两侧多空格。
2. 【P2】L58/L72：「前端大课走 **GitGo** 类工具」→ 工作区与 SRC 均查无此工具名，疑为转写噪声（Gogs/Gitea 类自建 Git 服务？）。建议泛写「自建 Git 服务 + CI/CD」或核实后修正（两处同步）。
3. 【P2】L53：「Redis 缓存：自定义 key、**发布订阅**」→ 本大课 SRC 的 RedisModule 只有 set/get/del/exists/getCachedData，无发布订阅；若该条来自前端大课或其他项目，建议括注来源或删掉「发布订阅」，避免按此写简历被追问（与本篇自己「按掌握程度删减」的原则一致）。

### 31-4.全栈高级工程师简历—低代码项目大课项目讲解 — 需修

1. 【P1】title/H1 完全断链（簇一末行）：现题《简历实战：把低代码平台项目写进全栈高级工程师简历》与 3 处引用名《全栈高级工程师简历—低代码项目大课项目讲解》完全不同（b5 对 14-9/15-6/16-4、b6 对 18-6 同型问题判 P1）。
2. 【P1】L63 简历亮点「原子性防重提交」超出现状：SRC `postQuestionData` 是先 `findOneBy` 再 `save` 的 check-then-insert，无事务/行锁/唯一索引（review-eng-b P1-13、P0-3；b6 簇六口径——换 UA 即绕过、并发可重复插入）。「原子性」是源码不具备的属性，写进简历必被追问翻车，与 31-2 自己教的「经不起追问的不写」相悖。建议改「图形验证码 + 短信验证码防刷、基于 MD5(ip+ua) 匿名标识的防重复提交」，并可在讲解段补一句现状注：「并发防重需唯一约束或分布式锁才算闭环，可作为面试改进项来讲」。
3. 【P2】L45：「（代码在 `client/src/components/hooks`）」→ 实为 `packages/client/src/hooks`（useStoreComponents/useComponentKeypress/useStoreAuth 等都在这里，SRC 无 components/hooks 目录）。
4. 【P2】L45：「键盘**排序**」→ 快捷键是复制/粘贴/删除/撤销重做，无排序；改「键盘快捷键操作」。
5. 【P2】L51：「`componentExpose` 做统一导出」→ SRC 是 `share/src/utils/componentExport.ts`（导出 `componentList` 组件映射表），无 componentExpose。
6. 【P2】L52：「Nginx 反向代理、负载均衡与**缓存压缩**」→ SRC nginx conf 未配 gzip/缓存（review-eng-b P1-14），建议删「缓存压缩」或括注为生产待补项。
7. 【P2】L17 资料路径（簇四）。

（其余核对：`client/src/hooks` 之外的 pnpm workspace / share 复用 / OSS 部署 React 编辑端 / Next.js+NestJS 上服务器 / TypeORM 笔误提醒 / Next.js≠Nest 名词纠正，均与 SRC 一致。）

---

## 三、统计

| 项 | 数量 |
|---|---|
| 总篇数 | 19 |
| 合格（含附 P2 建议 11 篇：28-8、29-1、29-2、29-3、30-1、30-2、30-3、30-4、30-6、31-1、31-2、31-3） | **12** |
| 需修 | **7**（28-4、28-5、28-6、28-7、28-9、30-5、31-4） |
| P0 | 0 |
| P1 | **8**（簇二 `local_code` 路由 2 处 1 簇；28-4 jmeter-server 主从角色写反；28-6 监听器保存说法与 JMeter 实际相反；28-9 登录体 `account`→`phone`（照抄即 400）；30-5 `pageId`→`page_id`（照抄即失真）；31-4 标题整体断链；31-4 简历「原子性防重提交」超出现状） |
| P2 | **约 41**（标题/H1 断链 14、簇三响应字段口径 2、簇四资料路径 6 处 6 篇、簇五 release 控制器/无参数/version.ts 3、30-6 残留 2（L119 口径 + this.set 签名）、29-3 转写残留与数字叙事 2、31-3 GitGo/发布订阅 2、31-4 hooks 路径/键盘排序/componentExpose/缓存压缩 4、30-1 写库/30-2~30-4 补实名路径与文案 6、28-4 macOS 启动 1、其余随手项） |

需修优先级建议：

1. **先修簇二 + 两个「照抄即错」字段**（28-5 L62、28-7 L15 的 `/api/local_code/release`→`/api/low_code/release?id=`；28-9 `account`→`phone`；30-5 `pageId`→`page_id`）——这四处读者照着做必失败或结果失真，且均为一词替换。
2. **再修两处 JMeter 行为误述**（28-4 jmeter-server 角色一句改写；28-6 监听器保存说法整段改写并保留实践建议）。
3. **31-4 两处 P1**（title 改回引用名一处修复三条引用；「原子性」降格 + 现状注）。
4. **簇一 14 篇 title/H1 与簇三/簇四/簇五批量卫生项**可一次批量处理；29-3 L46「smaller」、30-6 L119「清空旧缓存」为单点微调。
5. 简历篇口径（31-3 GitGo/发布订阅、31-4 缓存压缩）建议与「按掌握程度删减」的原则统一收紧，防止读者把经不起追问的名词带进真实简历。
