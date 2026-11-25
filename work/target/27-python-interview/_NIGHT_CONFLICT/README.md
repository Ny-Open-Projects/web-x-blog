# 批 27 并发写入隔离区（_NIGHT_CONFLICT）

## 为什么有这个目录

2026-11-25 08:37-09:30，**另一个并发实例**在与批 27 相同的号段（Q5251-5260 / Q5751-5760 / Q6251-6260 /
Q6791-6800 / Q7283-7292 / Q7790-7799）反复写入不同考点的卡，累计 31 个 QID 出现「一号两卡」
（最多时 6 个号同时双卡）。为满足「全库题号零重号」，每个号只保留一张；另一张移入本目录并把后缀改为
`.off` —— 不参与 `find 0* -name "*.md"` 计数，也不会被下游博客流水线误采集。

## 保留判定规则

1. 两张都必须先过机械复核（front-matter 合规 + 代码 3.12.2 实跑）。两套在本次运行中均 100% 通过，故不以此决胜。
2. 用 2~3 个区分性关键词统计**全库其他卡**的命中数（= 该考点已被覆盖的程度），保留「近邻更少、更稀缺」的一张。
3. 接近时优先保留已纳入本班批次台账（`_INDEX.md` 夜 27 行）的那张，避免收口后账实不符。

## 隔离清单（31 张，内容合规、未作废）

| 目录 | 隔离文件（已改 .off） | 该号保留的卡 |
|---|---|---|
| 01-语言核心与底层 | Q5251-slots与property共存及同名冲突.md.off | Q5251-312-sum补偿求和与fsum误差账.md |
| 01-语言核心与底层 | Q5252-enumFlag位标志与boundary边界策略.md.off | Q5252-PEP695别名的惰性求值与缓存成本.md |
| 01-语言核心与底层 | Q5253-sys-monitoring多工具共存与事件禁用协议.md.off | Q5253-inspect生成器状态机观测.md |
| 01-语言核心与底层 | Q5254-realpath与resolve及symlink语义.md.off | Q5254-PEP393三档表示与内存复制账.md |
| 01-语言核心与底层 | Q5255-itertools-batched边界语义与islice差异.md.off | Q5255-dict合并运算符与PEP584语义.md |
| 01-语言核心与底层 | Q5256-math-isclose相对与绝对容差.md.off | Q5256-原子分组与占有量词的语义代价.md |
| 01-语言核心与底层 | Q5257-bisect-key参数与等键稳定性边界.md.off | Q5257-operator取值器家族itemgetter-attrgetter.md |
| 01-语言核心与底层 | Q5258-gc-freeze冻结不是不朽与分代账.md.off | Q5258-struct_time与gmtimelocaltime配对纪律.md |
| 01-语言核心与底层 | Q5259-deepcopy钩子与memo占位.md.off | Q5259-translate表驱动替换与链式replace顺序事故.md |
| 01-语言核心与底层 | Q5260-os-environ视图语义与子进程传递.md.off | Q5260-typing-override运行时零校验边界.md |
| 02-并发与网络工程 | Q5751-asyncio-timeout预算与取消边界.md.off | Q5751-Task命名诊断与get_name日志关联.md |
| 02-并发与网络工程 | Q5752-eager-task-factory顺序副作用与完成态.md.off | Q5752-TLS重协商边界与DoS防线.md |
| 02-并发与网络工程 | Q5753-连接池泄漏画像与借出账本.md.off | Q5753-Semaphore公平切换与计数漂移.md |
| 02-并发与网络工程 | Q5754-create_connection多地址遍历与超时预算.md.off | Q5754-半关闭SHUT-WR与close丢数据边界.md |
| 02-并发与网络工程 | Q5755-TCP_NODELAY与写合并取舍.md.off | Q5755-TCP-NODELAY决策边界与40ms账.md |
| 02-并发与网络工程 | Q5756-应用层心跳与TCPkeepalive分工.md.off | Q5756-getaddrinfo与默认执行器饿死.md |
| 02-并发与网络工程 | Q5757-add_signal_handler执行语义与Unix边界.md.off | Q5757-set-wakeup-fd与self-pipe唤醒.md |
| 02-并发与网络工程 | Q5758-fork与spawn继承事故与macOS默认值.md.off | Q5758-SO_RCVBUF-SNDBUF内核缓冲账.md |
| 02-并发与网络工程 | Q5759-Future-cancel排队与运行中取消语义.md.off | Q5759-StreamReader-limit不是内存保护.md |
| 02-并发与网络工程 | Q5760-contextvars线程池与协程边界.md.off | Q5760-threading-Barrier相位同步与broken传播.md |
| 03-Web后端开发 | Q6251-限流计量维度与配额计费口径.md.off | Q6251-BackgroundTasks失败语义与重试归属.md |
| 03-Web后端开发 | Q6252-hop-by-hop头剥离与透传白名单.md.off | Q6252-Depends请求级缓存与覆盖边界.md |
| 03-Web后端开发 | Q6253-多租户运行时隔离键贯穿.md.off | Q6253-from-attributes与ORM懒加载.md |
| 06-Agent与LLM及系统设计 | Q7792-评测judge注入与内容隔离防线.md.off | Q7792-元数据过滤前置与后置的选择性账.md |
| 06-Agent与LLM及系统设计 | Q7793-长期记忆的写入冲突与版本化.md.off | Q7793-跨语言检索断层与翻译扩展.md |
| 06-Agent与LLM及系统设计 | Q7794-prompt前缀缓存的命中率工程.md.off | Q7794-提示模板条件分支膨胀治理.md |
| 06-Agent与LLM及系统设计 | Q7795-长度感知模型路由与分档成本账.md.off | Q7795-约束解码的失败面与修复回路.md |
| 06-Agent与LLM及系统设计 | Q7796-双judge分歧仲裁与一致率信号.md.off | Q7796-token计数偏差与截断顺序.md |
| 06-Agent与LLM及系统设计 | Q7797-评测集覆盖度矩阵审计.md.off | Q7797-流式响应重试的幂等与半截输出收场.md |
| 06-Agent与LLM及系统设计 | Q7798-评估集回归门禁的显著性与基线漂移.md.off | Q7798-会话任务切换检测与软重置.md |
| 06-Agent与LLM及系统设计 | Q7799-消息编辑重新生成与历史分叉.md.off | Q7799-Agent循环终止的最大步数预算与无进展检测.md |

## 批 28 追加（2026-11-25，01 号段 Q5261-Q5270）

批 28 的 01 号段再次出现并发写同号段：本班 11:31-11:42 写入 10 张，并发实例 11:45-11:55 向同一批 10 个号写入另一套。按上节规则逐号判定：

- **机械复核**：本班 10/10 全绿；并发实例 7/10，Q5262（断言失败）、Q5263（断言失败）、Q5266（`SyntaxError: positional argument follows keyword argument`）。这 3 个号直接保留本班版。
- **稀缺度**（区分性关键词在全库其他卡的命中数，本班 vs 并发）：Q5261 `recursive_repr` 0 vs `enumerate` 216；Q5264 `register_error` 4 vs `divmod/进制转换` 8；Q5265 `lastResort/NullHandler` 1 vs `bytes索引` 67；Q5268 `getattr_static` 0 vs `str.join` 2；Q5270 `sys.exception` 0 vs `from_iterable` 0（平手，本班先到，保留本班）。
- **Q5267 与 Q5269 曾按稀缺度倾向并发实例版**（本班 `_missing_` 命中 15、`memoryview` 27；对方 bytes `%` 3、`zip(*` 3），但并发实例这两张只有难度行、缺 `基线：`，不满足本批正文结构约束（front-matter 合规、难度行、基线行、结论/取舍/实战、追问一二、背诵要点三条、复盘追问两条），故仍保留本班版。
- 结论：并发实例 10 张中 5 张不合规（3 张代码实跑失败 + 2 张缺基线行），01 号段最终 10 张全部为本班版，并发实例 10 张全部隔离。

| 目录 | 隔离文件（已改 .off） | 该号保留的卡 |
|---|---|---|
| 01-语言核心与底层 | Q5261-enumerate的start语义与计数偏移.md.off | Q5261-递归repr守卫与线程隔离.md |
| 01-语言核心与底层 | Q5262-切片负步长区间语义与回文判定.md.off | Q5262-异步生成器终结钩子.md |
| 01-语言核心与底层 | Q5263-any-all短路与生成器副作用.md.off | Q5263-整数十进制转换闸门.md |
| 01-语言核心与底层 | Q5264-divmod与进制位权转换.md.off | Q5264-编解码错误处理器契约.md |
| 01-语言核心与底层 | Q5265-bytes索引返回int与类型分叉.md.off | Q5265-logging兜底lastResort.md |
| 01-语言核心与底层 | Q5266-星号解包赋值收集与展开语义.md.off | Q5266-float精确分数与往返.md |
| 01-语言核心与底层 | Q5267-bytes的percent格式化与轻量打包.md.off | Q5267-Enum别名与missing.md |
| 01-语言核心与底层 | Q5268-str-join类型契约与两遍遍历.md.off | Q5268-静态取属性绕开描述符.md |
| 01-语言核心与底层 | Q5269-zip星号转置与退化边界.md.off | Q5269-memoryview导出计数.md |
| 01-语言核心与底层 | Q5270-chain惰性拼接与from_iterable内存语义.md.off | Q5270-sys.exception当前异常.md |

## 后续处理建议

- 这些卡没有事实或代码问题，只是与保留卡考点重叠：**可换空号段重新入库**（重编号 + 改 `title` 与 `### QID ·` 即可）。
- 若再次出现并发实例写同号段：按同一规则去重并追加到上表，**不要把重号留到收工**。
- 本目录不计入题库实盘（统计口径 `find 0* -name "Q*.md"` 不覆盖下划线目录）。

生成：2026-11-25 批 27 收口
