# 面试卡串行生产 · 总进度表

> 用途：单条串行自动化按此表**从上往下取第一个 `pending` 单元**，每次只处理**一个**单元（禁止并发、禁止派子 agent，防 429）。
> 顺序：**先 MySQL 全部完成（03→10），再 Python（03→10）**。串行，不跳序。
> 更新规则：每完成一个单元，把该行 `pending` 改为 `done`，并在「产出」列填入卡号区间与张数。

---

## 一、MySQL 面试指南（`work/mysql-interview/`）

- 源：`mysql-interview/source/NN-*.txt`（单章单文件）
- 卡目录：`mysql-interview/target/`
- 门禁：`cd mysql-interview && python3 _pipeline/validate.py`（须 0 error）
- 已校准样板：`target/001-*.md` ~ `target/018-*.md`（第2章，18 张，0 error 0 warn）

| 状态 | 单元 | 源文件 | 字节 | 卡号 | 产出 |
|---|---|---|---|---|---|
| done | 02 版本类 | source/02-version.txt | 54K | 001–018 | 18 张 |
| done | 03 用户管理 | source/03-user-management.txt | 33K | 019–034 | 16 张 |
| done | 04 服务器配置 | source/04-server-config.txt | 55K | 035–060 | 26 张（035–052 首轮 18 张 + 053–060 续 8 张；buffer_pool_instances 已并入 052，不单出） |
| done | 05 日志类 | source/05-logs.txt | 74K | 061–079 | 19 张（061–072 前两轮 12 张 + 073–079 续 7 张：row_image / rows_query_log_events / log_slave_updates / DDL 记语句 / binlog 清理 / 日志轮转 / 慢查分析工具） |
| done | 06 存储引擎 | source/06-storage-engine.txt | 70K | 080–094 | 15 张（080–089 首三轮 10 张 + 090–094 续 5 张：读不阻塞写 / MVCC 版本链+隐藏列 / 共享锁排他锁兼容矩阵 / 快照读vs当前读 / RC-RR 的 ReadView 时机） |
| done | 07 架构类 | source/07-architecture.txt | 152K | 095–115 | 21 张（095–105 前四轮 11 张 + 106–115 续 10 张：异步复制主库侧搭建 / 复制账号与认证插件 / 从库是否开 binlog / CHANGE MASTER TO 与 START SLAVE / 半同步插件安装启用 / 半同步超时对写入影响 / GTID 前置参数 / MGR 前置变量 / MGR 节点加入与监控 / MGR 限制与常见问题） |
| done | 08 备份恢复 | source/08-backup-recovery.txt | 67K | 116–125 | 10 张（逻辑 vs 物理备份 / 全量-增量-差异 / 三款工具选型 / mysqldump 参数 / dump 恢复 GTID 报错 / mysqlpump 并行压缩 / XtraBackup 原理与全备恢复 / XtraBackup 增量恢复 / binlog 增量与时间点恢复 / binlog 备份策略） |
| done | 09 管理及监控 | source/09-monitoring.txt | 39K | 126–132 | 7 张（QPS 计算 / TPS 口径 / 并发数与连接数 / 缓冲池命中率 / 可用性探活 / 阻塞定位与 KILL / 死锁 vs 阻塞与慢查询监控） |
| done | 10 异常处理 | source/10-exception-handling.txt | 27K | 133–146 | 14 张（CPU 冲高伴 QPS 下降判读 / CPU 高四类根因与工具矩阵 / 磁盘 IO 打满三类成因 / lsof+计数器坐实临时表风暴 / 磁盘临时表治理 / 主从无延迟却不一致三类成因 / read_only 与 super_read_only / statement→ROW 消除差异 / 校验与 pt 同步修复 / IO 线程 Connecting 四步排查 / 复制账号权限 / 1062 主键冲突成因 / 处置优先级 / GTID 注入空事务） |

## 二、Python 服务端工程师指导面试教程（`work/py-interview/`）

- 源：`py-interview/source/第N章 .../`（软链到 `source/13.Python服务端工程师指导面试教程`）
- 卡目录：`py-interview/target/`
- 门禁：`cd py-interview && python3 _pipeline/validate.py`（须 0 error）
- 分诊：`py-interview/_pipeline/TRIAGE.md`（**第1/2/11/12 章为导学·面试流程·经验·总结，R1/R4 剔除，不出卡**）
- 已有样卡：`301-python-dynamic-strong-typing.md`、`303-monkey-patch(.deep).md` → **下一批从 302 起编号，避免撞号**

| 状态 | 单元 | 源目录 | 备注 |
|---|---|---|---|
| done | 第3章 语言基础 | source/第3章 Python语言基础考察点 | 93K，分 3 批完成，**共 47 张**：302、304–320（18 张，3-1/3-2：后端选型 / 鸭子类型 / 自省 / is 与 == / 列表字典推导 / 生成器推导 / print 函数化 / bytes 与 str / 真除法与整除 / 类型注解 / super 与星号解包 / 限定关键字参数 / 异常链 / 全面迭代器化 / Python3 新增 / 2-3 兼容工具 / __pycache__ / Python 之禅）+ 321–328（8 张，3-3 函数传参：共享传参 / 可变与不可变类型 / 可变默认参数 / args 打包 / kwargs 打包 / 调用处解包 / 形参五段顺序 / 防御性拷贝）+ 329–340（12 张，3-4 异常 + 3-5 GIL 与性能：异常vs错误码 / 异常继承体系 / try-except-else-finally / 自定义业务异常 / GIL 是什么 / CPU-IO 密集差异 / 切换间隔 / += 非原子 / dis 判原子 / 绕开 GIL 选型 / 性能剖析工具 / Web 后端优化四层）+ 341–349（9 张，3-6~3-8：yield 生成器 / 生成器协程 send / @coroutine 装饰器 / 原生协程三者区分 / 单元测试意义 / 用例设计三类 / mock 与 coverage / 深浅拷贝 / 二维数组初始化坑）。**3-1~3-8 全部覆盖** |
| done | 第4章 算法与数据结构 | source/第4章 Python算法与数据结构考察点 | 168K/10 个源文件。**共 49 张**（350–398）。已产出 **350–365，16 张**（4-1 + 4-2 全覆盖：内置结构全景分类 / tuple 引用不可变 / 可哈希与字典 key / namedtuple / deque 栈队列 / Counter / OrderedDict / defaultdict / dict 哈希表与冲突 / 哈希表扩容 / set 与 frozenset / 缓存淘汰策略 LRU-LFU-FIFO / OrderedDict 手写 LRUCache / functools.lru_cache / 排序查找考纲 / sorted-bisect-heapq）。续产出 **366–376，11 张**（4-3 覆盖：链表三种结构与表示 / 迭代反转单链表 / deque 封装队列 / list 当队列的代价 / deque 实现栈 / 两栈实现队列 / 最小栈 / 哈希冲突链地址法vs开放寻址 / 二叉树表示与三种遍历 / 堆性质与数组存储 / TopK 小顶堆）。续产出 **377–380，4 张**（4-4 白板编程方法论 + 4-5 两道链表题：只给定待删节点如何删除（复制后继法）/ 合并两个有序链表（哑节点+归并）/ 白板编程准备方法 / 现场没思路的应对策略）。续产出 **381–398，18 张**（4-6 二叉树 5 张：反转二叉树镜像 / 层序遍历双列表 / 空树边界 NoneType / 左右视图 / 遍历全景 DFS-BFS；4-7 栈队列 4 张：手写 Stack 类四接口 / 单栈无法做队列 / peek 与 empty / 栈队列是图遍历底层；4-8 堆 4 张：合并 K 个有序链表最小堆三步法 / heapq 三板斧 / 两两归并vs堆vs分治 / 空输入三重坑 []-[[]]-空堆；4-9 字符串 5 张：原地反转字符串 / reverse-vs-reversed / 回文数字符串双指针 / 回文数数值解反转一半 / 对撞指针套路）。**4-10 为章末总结与作业（反转链表，367 已含迭代+递归），无新考点，不出卡。4-1~4-10 全部覆盖，本单元完结** |
| done | 第5章 编程范式 | source/第5章 编程范式考察点 | 61K/6 文件。**共 46 张（399–444）**：5-1 面向对象 11 张（399–409）；5-2 装饰器 7 张（410–416）；5-3 创建型 9 张（417–425）；5-4 结构型 7 张（426–432）；5-5 行为型 6 张（433–438）；5-6 函数式 6 张（439–444）。**第5章完结** |
| done | 第6章 操作系统·6-1 Linux命令 | source/第6章 操作系统考察点/6-1*.txt | 4 文件：6-1 12824B/6-2 14350B/6-3 23660B/6-4 2182B。**7 张（445–451）**：445 Linux为什么学+命令查找 / 446 软硬链接 / 447 文件权限命令 / 448 find-locate-grep / 449 进程命令 / 450 网络命令 / 451 free内存-users-crontab |
| done | 第6章 操作系统·6-2 进程线程 | source/第6章 操作系统考察点/6-2*.txt | 14350B。**9 张（452–460）**：452 进程vs线程本质 / 453 并发vs并行(GIL) / 454 线程安全+i+=1陷阱 / 455 锁(mutex) / 456 信号量 / 457 事件+三者对比 / 458 IPC全景(Ctrl+C=SIGINT, RPC≠IPC) / 459 Python多线程threading / 460 Python多进程multiprocessing(master-slave) |
| done | 第6章 操作系统·6-3 内存管理+GC | source/第6章 操作系统考察点/6-3*.txt | 23660B。**10 文件（461–468 主卡 + 467/468 两张 .deep）**：461 分页 / 462 分段 / 463 虚拟内存+局部性 / 464 内存抖动+置换策略(LRU/LFU/FIFO,Redis) / 465 Python GC总览 / 466 引用计数(del/getrefcount/小整数池) / 467 循环引用+标记清除(L3) / 468 分代回收(L3,get_threshold 700/10/10)。**第6章完结（6-4 为 R4 元内容剔除）** |
| pending | 第6章 操作系统·6-4 章末总结 | source/第6章 操作系统考察点/6-4*.txt | R4 元内容（作业/总结），按 TRIAGE 剔除不出卡 |
| done | 第7章 网络编程·7-1 网络基础 | source/第7章 网络编程考察点/7-1*.txt | 19446B。**4 张（469–472）**：469 URL输入到返回全流程(DNS→TCP→Nginx→WSGI→web应用) / 470 TCP三次握手 / 471 TCP四次挥手 / 472 TCP vs UDP |
| done | 第7章 网络编程·7-2 HTTP协议 | source/第7章 网络编程考察点/7-2*.txt | 24796B。**6 张（473–478）**：473 HTTP报文结构(请求/响应) / 474 状态码五大类(301vs302,304) / 475 方法GET/POST/PUT/DELETE+RESTful / 476 幂等性与安全性 / 477 长连接keep-alive(Content-Length/chunked) / 478 Cookie与Session |
| done | 第7章 网络编程·7-3 Socket编程 | source/第7章 网络编程考察点/7-3*.txt | 12608B。**3 张（479–481）**：479 TCP服务端 socket(bind→listen→accept) / 480 TCP客户端 socket 与 bytes(encode/decode) / 481 手工拼 HTTP 请求(socket+请求行+Host+\r\n\r\n) |
| done | 第7章 网络编程·7-4 IO多路复用 | source/第7章 网络编程考察点/7-4*.txt | 11375B。**3 张（482–484）**：482 阻塞IO vs IO多路复用(事件循环/C10K瓶颈) / 483 select·poll·epoll 区别与时间复杂度(O(N)/O(N)/O(1),FD_SETSIZE,LT/ET) / 484 Python selectors 模块(DefaultSelector+register+事件循环+回调,协程解回调地狱) |
| done | 第7章 网络编程·7-5 并发网络库 | source/第7章 网络编程考察点/7-5*.txt | 13700B。**4 张（485–488）**：485 三大库总览(底层共性=IO多路复用) / 486 Tornado(FriendFeed, IOLoop+非阻塞socket+协程, monkey patch 纠偏) / 487 gevent(greenlet+monkey patch+libev, 常配 gunicorn) / 488 asyncio与aiohttp(原生协程+事件循环, 生态成熟度版本翻转) |
| 排除 | 第7章 网络编程·7-6 章末总结 | source/第7章 网络编程考察点/7-6*.txt | 2332B，**R4 元内容（本章回顾 + 异步爬虫作业）**，无新考点，按 TRIAGE 剔除不出卡 |
| done | 第8章 数据库·8-1 MySQL基础 | source/第8章 数据库考察点/8-1*.txt | 17981B。**7 张（489–495）**：489 事务与ACID(undo/redo/锁+MVCC) / 490 并发异常(脏读/不可重复读/幻读/丢失更新, InnoDB RR防幻读) / 491 隔离级别(RU-RC-RR-Serializable, MySQL默认RR, PG/Oracle默认RC) / 492 乐观锁vs悲观锁(SELECT FOR UPDATE/版本号/CAS=Check-And-Set) / 493 并发插入去重(唯一索引/队列/Redis锁) / 494 数据类型(CHAR/VARCHAR/TEXT, INT(n)显示宽度误区, DATETIME/TIMESTAMP-Y2038, 金额用DECIMAL) / 495 InnoDB vs MyISAM(5.6+ InnoDB全文索引翻转, 崩溃恢复) |
| done | 第8章 数据库·8-2 MySQL索引 | source/第8章 数据库考察点/8-2*.txt | 32084B。**8 张（496–503）**：496 什么是索引与查找结构进化史(线性→二分→哈希→BST→AVL→B树→B+树) / 497 B树 vs B+树(非叶不存数据→更矮, 叶子双向指针→范围查, 阶由磁盘页定, L3) / 498 MySQL索引类型(普通/唯一/联合/主键/全文, InnoDB 5.6+ 全文索引翻转) / 499 联合索引与最左前缀(B+树 key 多列拼接, 从左比较, 范围截断 L3) / 500 创建索引最佳实践(非空字段/高区分度/短长度, 回扣B+树key比较) / 501 索引失效三口诀(模糊匹配/类型隐转/最左匹配, 统一根因=B+树key无法直接比较) / 502 聚集索引与非聚集索引(InnoDB主键=聚集叶存整行, 辅助索引叶存主键→回表; MyISAM非聚集两文件) / 503 慢查询排查(慢日志/EXPLAIN/代码层类型匹配与分页) |
| done | 第8章 数据库·8-3 SQL 连接查询 | source/第8章 数据库考察点/8-3*.txt | 6854B。**3 张（504–506）**：504 SQL 编写重点与连接查询总览(复杂SQL高并发差→逻辑下沉代码层, 阿里禁3表join) / 505 内连接 INNER JOIN(两表匹配才返回, 类似交集, a/b表示例手算+终端验证) / 506 外连接 LEFT/RIGHT JOIN(保左/保右全部+NULL填充, MySQL不支持原生FULL OUTER JOIN→LEFT UNION RIGHT模拟) |
| done | 第8章 数据库·8-4 Redis 缓存 | source/第8章 数据库考察点/8-4*.txt | 29877B。**12 张（507–518）**：507 为什么用缓存(缓解DB压力/降延迟μs vs ms/提吞吐) / 508 Redis vs Memcached(类型/单线程IO多路复用/持久化, 6.0多线程化) / 509 五数据类型(string/list/hash/set/zset) / 510 底层编码(SDS/ziplist/intset/skiplist, 7.0 listpack) / 511 跳跃表(多层索引+二分, 为何不用平衡树) / 512 持久化 RDB vs AOF(混合持久化) / 513 Redis事务 MULTI-EXEC-WATCH 与 ACID(无回滚/单线程隔离) / 514 分布式锁(SETNX+expire+随机值, SET NX EX 原子) / 515 Cache Aside(先更DB再删缓存) / 516 缓存穿透(空值+布隆) / 517 缓存击穿(分布式锁/后台刷新) / 518 缓存雪崩(随机TTL/多级/可用性) |
| done | 第8章 数据库·8-5 章末回顾 | source/第8章 数据库考察点/8-5*.txt | 3002B，**R4 元内容（章末回顾+思考题）**，仅提取 1 个新考点。**1 张（519）**：519 数据库主键设计(自增INT vs UUID 的 B+树代价) + 分布式 ID 生成(Snowflake/号段/Redis/Leaf)；其余 MySQL/Redis 回顾均已覆盖，按 TRIAGE 不注水 |
| done | 第9章 Web 框架·9-1 Web 框架概览 | source/第9章 Python Web 框架考察点/9-1*.txt | 16831B。**4 张（520–523）**：520 WSGI 规范(PEP 3333, 应用/服务器双端契约, wsgiref 启动) / 521 Web 框架对比(Django全栈/Flask轻量/Tornado异步/Pyramid/web.py/Bottle) / 522 MVC 模式(控制-模型-视图, Django MTV 纠偏) / 523 ORM 对象关系映射(去 SQL 化, 抽象层, 性能权衡) |
| done | 第9章 Web 框架·9-2 Web 安全 | source/第9章 Python Web 框架考察点/9-2*.txt | 14140B。**2 张（524–525）**：524 SQL 注入(拼接+无过滤根因, 参数化根治, OR/LIKE/ORDER BY 盲区) / 525 XSS 跨站脚本(存储/反射型, 转义+CSP+HttpOnly, 与 CSRF 对比)；源仅提名 CSRF 未展开，未单出卡 |
| done | 第9章 Web 框架·9-3 前后端分离与 RESTful | source/第9章 Python Web 框架考察点/9-3*.txt | 11181B。**2 张（526–527）**：526 前后端分离(传统 MVC 痛点/定义/四大优势/SEO 劣势+SSR 补救) / 527 RESTful(三要素/设计准则/动词映射 CRUD/名词复数 URI/幂等性+Tornado 代码示例) |
| 排除 | 第9章 Web 框架·9-4 章末 | source/第9章 Python Web 框架考察点/9-4*.txt | 2447B，**R4 元内容（章末回顾 + HTTPS 练习题）**：仅回顾 WSGI/三框架/SQL注入/XSS/CSRF/前后端分离/RESTful（均已覆盖于 520–527）；HTTPS 仅作"练习题"点名、源未展开讲解，按"以源为准、不注水"剔除不出卡。第9章完结 |
| done | 第10章 系统设计·10-1 方法论 | source/第10章 系统设计考察点/10-1*.txt | 14213B。**2 张（528–529）**：528 系统设计概述与难点(定义/三大难点/微服务催生/常见考题/DRY原则) / 529 回答框架三大要素(场景限制+QPS估算 / 数据存储选型+索引缓存 / 算法模块接口+时空权衡；延伸扩展与容错) |
| done | 第10章 系统设计·10-2 短网址实战 | source/第10章 系统设计考察点/10-2*.txt | 28451B。**3 张（530–532）**：530 短网址系统设计(需求两接口/约束≤7位62字符集/bitly QPS估算/MySQL四字段+token索引) / 531 短码算法(MD5截断冲突 vs 自增ID base62/divmod取余倒序/num=0边界/Redis INCR) / 532 Flask+Redis+MySQL 落地(视图函数/参数化防注入/白纸分区图文并茂) |
| 排除 | 第10章 系统设计·10-3 章末 | source/第10章 系统设计考察点/10-3*.txt | 2483B，**R4 元内容（章末回顾 + 秒杀系统思考题）**：仅回顾三要素+短网址实战（已覆盖于 528–532）；秒杀系统仅作"思考题"点名（消息队列削峰、Redis 削减库存两句提示），源未展开讲解，按"以源为准、不注水"剔除不出卡。**第10章完结，Python 全册完成** |

## 三、通用规则（每次执行必读）

1. **一次只处理一个 pending 单元**，不派子 agent、不并行（历史实测：并行 3 会全线 429）。
2. 单元结束立即 `validate.py`，**有 error 必须修完再收尾**；修不完就保持 `pending` 并写明阻塞原因。
3. 卡号**连续不撞号**：MySQL 从 019 续，Python 从 302 续（跳过已存在的 301/303）。
4. 单元超大（>80KB）时**允许只完成一部分**：把已产出的卡号区间写入「产出」列、状态改 `partial`，下次从剩余部分续；**不要**为了一次做完而压缩质量。
5. 完成后追加日志到 `/Users/Wang/Code/github/web-x-blog/.workbuddy/memory/YYYY-MM-DD.md`。
6. **不要 git commit / push**（等用户指令）。

## 四、收尾条件

两表全部 `done`/`partial=0` 后，跑全量 `validate.py` 双目录 + 统计总张数 + 生成背诵清单，汇报「全部完成」。
