# ES 课程素材 · 机翻/语音转写术语还原表

> 素材是**课程音频转写 + 机器翻译**的双重噪音产物。
> 写博客前先对照本表还原术语，否则会把 `shard` 写成「分辨」这种笑话写进正式博客。
> **处理新素材时发现的新的错译，追加到表尾，别@localhost 里攒着。**

## 一、高频错译（出现频率最高，先看这组）

| 转写/机翻出来的 | 正确术语 | 说明 |
| --- | --- | --- |
| `yes` / `insearch` / `elecsticsearch` / `yess` / `ES思` | **Elasticsearch（ES）** | 语音转写把 `ES` 听成 `yes` 是最高频错误 |
| `分辨` / `主分辨` / `主分辨数` | **shard / primary shard** | `shard` → 「分辨」 |
| `副本分辨` | replica shard | |
| `主体` / `体` / `routine` / `root` / `rout` | **routing** | 出现过至少 5 种错法 |
| `档` / `蛋` / `selest段` / `select段` / `淡文件` | **segment** | `segment` → 「档」 |
| `氮合并` / `但合并` / `断合并` / `规并` / `淡合并` | **segment merge** | |
| `bug` / `buk` / `八k` / `八个` / `八x` / `bubut` | **bulk** | 批量写 API |
| `fresh` / `ffresh` / `refres` / `刷新` | **refresh** | |
| `transfor` / `trlorefresh` / `translaer` / `trlog` | **translog** | |
| `OScatch` / `oscach` / `oscache` | **OS cache** | 操作系统页缓存 |
| `indexbuffer` / `inmemorybuffer` / `insbuffer` / `induspatfer` / `indexspark` | **index buffer** | |

## 二、参数 / API 名还原

| 转写错法 | 正确参数 |
| --- | --- |
| `waitforactive下子` / `waitforIQ下下来` / `waitforacq下载` | `wait_for_active_shards` |
| `maxcontendance` / `玻璃的限制` | `http.max_content_length`（默认 100MB） |
| `ffreshinterval` / `refresh之同` / `副fresh之同` | `index.refresh_interval`（可动态改；设 `-1` 关掉） |
| `duryability` / `sumfliability` | `translog.durability` |
| `bliity` / `ASINC` / `asinc` | `translog.durability=async` / **async** |
| `translog 达到 EGB 强制刷盘` | `translog.flush_threshold_size` |
| `flowsegment` / `flow_segment` | `index.merge.flow_segment`（默认 2MB） |
| `maskmergeadvance` / `maskmerge` / `marmerge` | `index.merge.merge_at_once`（默认一次 10 个段） |
| `max_merge_segment` / `maxmerge` | `index.merge.max_merge_segment`（默认 5GB，超过不参与合并） |
| `firstmerge` / `firstmermergePI` / `firstmerge中API` | **`forcemerge` API** |
| `only_expunge_deletes` | `?only_expunge_deletes=true`（只清删除文档，压力小） |
| `VMsswiplist` / `VMsweptlist` / `swaplist` / `swaftlist` | `vm.swappiness` |
| `wortscrap点memorylook` / `pootscrat点memorylock` | `bootstrap.memory_lock: true` |
| `preference=下划线logo` | `preference=_local` |
| `waitforactive下子` 数量含主分片 | 注意：设 2 = 1 主 + 1 副本 |

## 三、架构名词还原

| 转写错法 | 正确 |
| --- | --- |
| `logoDB` / `梦goDB` / `猫goDB` / `某购DB` / `从某购` | **MongoDB**（课程用它存不参与检索的冷字段） |
| `极限网关` | 第三方支持「写请求直发分片」的网关，**术语存疑，正文保留原词并加注** |
| `解集群` / `集储数据` / `写入集群` | 承接写请求的**写集群**（与读集群分离） |
| `读集群` | 存量只读集群 |
| `半读写分级` | 读写分级架构 |
| `文档合并服务` | 同 `_id` 多操作合并后批量写入的服务 |
| `垂直搜索` | 垂直搜索业务（如电商、招聘） |
| `六点三` / `六点s` | `6.3` / `6.x` |
| `企业请求` / `写请求` | 泛指 HTTP 请求 |
| `孔令性` | 语义存疑（上下文为「可靠性」），**不确定就按上下文取义，别硬译** |
| `步单` | 「开销/波动」语义存疑 |
| `九 十 兆` / `一百兆` | 数值按 100MB 上限处理 |

## 三·补、esrally / 压测专题新增错译（10.13 / 10.14 补充）

| 转写错法 | 正确术语 |
| --- | --- |
| `ESral` / `ESrail` / `railally` / `ESrailly` / `ESrally` / `yesrunning` / `yesrrning` / `yesrrunning` / `ESrunning` / `ESrally` / `ES里realrise` | **esrally（Rally）** |
| `electsearch` / `electsticsearch` / `electtest` | Elasticsearch |
| `PD级` / `PB级` 混用 | **PB 级** |
| `force` / `缩s` / `soues` / `source` / `原文` | **`_source`** |
| `bestcompression` | `index.codec: best_compression`（改前需 close 索引） |
| `targethorsts` / `targethost` / `popmail`（指目标地址时） | `--target-hosts` |
| `pipeline` / `压测流程` | `--pipeline`（`benchmark-only` = 只当负载发生器） |
| `checkackpelons` | **术语存疑**，上下文为「覆盖默认压测参数」，疑似 `--challenge` / `track-params` |
| `usertag` | `--user-tag` |
| `clientoptions` | `--client-options`（`useSSL` / `verifyCerts` / `basicAuthUser`） |
| `createtrack` / `刚刚track` | `esrally create-track` / `--track` |
| `trackpass` | `--track-path` |
| `riseID` / `rseID` | **race id**（`esrally list races` 取） |
| `compile`（对比语境） | `esrally compare --baseline --contender` |
| `schedule` / `压缩任务` | track.json 里的 **`schedule` 任务列表** / 压测任务 |
| `rorrate` | **error rate（错误率）** |
| `积分` / `积c` | **GC**（GC 时间、GC 次数） |
| `jason` / `接省` / `杰森` / `接层` | **json** |
| `jmater` / `ABWRK` | **JMeter** / **ab、wrk** |
| `sendOS` | **CentOS** |
| `get` / `gate` / `gethome` | **git** / `GIT_HOME` |
| `JDC` / `JDKget` | **JDK** |
| `PIP` / `PIP三` | **pip / pip3** |
| `yesrallynestpipeline` | `esrally list pipelines` |
| `快remail零一点CSV` / `querymail01` | `querymail01.csv`（`--report-file` 产物） |

## 三·补二、10.4~10.9 大文本优化专题新增错译（2026-10-02 追加）

| 转写错法 | 正确术语 |
| --- | --- |
| `hlp` | **HanLP**（开源 NLP 工具包，课程用它做摘要抽取；`hlp` 出现在 10.4） |
| `拖曼` / `拖慢的查询速度` | 拖慢 |
| `索以` / `缩引` / `缩影` | **索引** |
| `全量机器人` / `全量机器` | 全量集群 |
| `喜负感` / `额外的喜负感` | **额外负载** |
| `学入请求` / `写入请求` | 写请求（注意别误读成"学入"） |
| `mango` / `芒果` / `梦goDB`（存搜索记录语境） | **MongoDB**（10.5 用它存用户搜索记录） |
| `主件` / `主键id` | 主键 |
| `热机系统` / `热级群` / `弱用户` | 热集群 / **热用户**（"弱用户"是"热用户"的错听） |
| `sous` / `sours` / `sauce` / `sce` / `ssource` | **`_source`** |
| `措词` / `开启措词` | 开启 `_source` |
| `列存储` | 课程口语用法 = **字段原始值存储**（`_source` / `store`），不是列式数据库那个含义 |
| `source和store` | `_source` 与 `store` 两个 mapping 开关 |
| `helpdump` / `hipdump` / `djVMhelpdumppass` | **heap dump** / JVM 参数 `-XX:HeapDumpPath` |
| `JVM点options` | `jvm.options` 配置文件 |
| `xpkMLNable` | `xpack.ml.enabled: false` |
| `transport点TCB一点comrix` | `transport.tcp.compress: true` |
| `bootstrap的点memorylock` / `pootscrat点memorylock` | `bootstrap.memory_lock: true` |
| `load点processors` / `loadprocessor` | `node.processors` |
| `黑布` / `黑p` / `GAM里面配置的黑布大小` | **heap size**（JVM 堆大小） |
| `fiace` / `face` / `fix` / `ace的face类型` | **fixed 线程池类型** |
| `scalalling` / `scaling` | scaling 线程池类型 |
| `fixedautoqueensize` | `fixed_auto_queue_size`（ES 8 起废弃） |
| `queensize` / `企业请求队列` | `queue_size` / 请求队列 |
| `right的线程池` / `write线程池` | **write 线程池**（`write` 被听成 `right`） |
| `四二九` | **HTTP 429** |
| `ffreshinterval` / `mrefreshintervl` / `副fresh之同` | `index.refresh_interval` |
| `copytwo` / `QBQ属性` | **`copy_to`** |
| `matchfreeze` | **`match_phrase`** |
| `sits` / `大文本的sits` | `_source` |
| `托管的数量` / `分出来的托管` | **token 数量** |
| `细力度` / `力度` | 粒度（分词粒度） |
| `figmmerge` / `firstmerge` | `forcemerge` / 段合并（merge） |
| `一百二十g` | 节点内存 **120GB**（10.8 的内存分配建议，按原话保留） |

## 三·补三、11.x 面试专题新增错译（2026-10-02 追加）

| 转写错法 | 正确术语 |
| --- | --- |
| `blowKDtree` / `KD树` / `树形结构`（数值字段语境） | **BKD tree**（数值/地理/日期字段的底层结构） |
| `k文类型` / `k位类型` / `kone类型` / `KM类型` | **keyword 类型** |
| `tom查询` / `特目个例` / `特目查询` | **term 查询** |
| `tomindex` / `倒排` | **term index**（term dictionary 的索引） |
| `beatset` / `bitset` | **bitset**（ES filter 缓存的文档位图，实际是 Roaring Bitmap） |
| `全局序数` / `globalaudiences` | **global ordinals / `eager_global_ordinals`**（转写把 ordinals 听成 audiences） |
| `exclusion汉译词` | **`execution_hint`**（terms 聚合参数，可设 `map` / `global_ordinals`） |
| `低技素` / `低基数` / `维值比例` | **低基数 / 高基数**（cardinality） |
| `sermap` / `schem`（mapping 语境） | **mapping / schema** |
| `预排序序段` / `预排序字段` | **`index.sort.field`**（索引级预排序配置） |
| `m体` / `msearch` | **`_msearch`**（拆分聚合用） |
| `copyu` / `copytwo` | **`copy_to`** |
| `joinnested` / `join` | **join / nested / parent-child** |
| `GA提问法` | **GA 提问法**（典型事件评估法，课程原话保留） |
| `start提问法` / `star提问法` | **STAR 提问法**（S/T/A/R） |
| `五w加EH` / `五w分析法` | **5W1H 分析法** |
| `冰山模型` | 冰山模型（六层：知识 / 技能 / 价值观 / 自我认知 / 个性 / 动机） |
| `note二` / `dot二` | **node2**（示例节点名） |
| `主分辨数` / `分辨数` | **主分片数**（routing 取余的分母） |
| `roorooid` / `rooes` / `root` / `物体` / `自定义体` | **routing / 文档 id** |
| `哈欠` | **哈希**（"哈希后取余"被听成"哈欠"） |
| `八k` / `八k型`（超大集群语境） | **bulk** |
| `webug` | **bulk** |
| `note二承担协调节点` | 协调节点（coordinating node） |
| `同步副本集` | **in-sync replica set** |
| `同步副本集已处理所有索引和删除操作` | 主节点维护的同步副本列表 |
| `firstmerge` / `firstmerge的API` | **`_forcemerge` API** |
| `onlyexpertdeletes` | **`only_expunge_deletes=true`** |
| `indexbuver` / `inlexbuffer` / `indexbuark` | **index buffer** |
| `transloer` / `transword` / `translog` | **translog** |
| `OScat` / `OS开始` / `OScatch` | **OS cache** |
| `hoetpoint` / `检查点` | **commit point** |
| `flat` / `flash`（落盘语境） | **flush** |
| `merch` / `档合并` / `办合同` | **merge（段合并）** |
| `sugman` / `selest段` | **segment** |
| `连delete文件` / `.del` | **`.del` 文件**（记录已删除文档 id） |
| `四二九` / `四二九状态码` | **HTTP 429**（写入拒绝） |
| `写入句体` / `写入拒绝` / `reject` | **写入拒绝 / rejected** |
| `键盘值` / `线程池` | **线程池**（get / search / bulk 各自独立） |
| `六点三版本` | **6.3 版本**（realtime GET 相关，实现依赖 translog） |
| `preference参数` / `用户的UID` | **`preference` 参数**（可用 uid / sessionId，固定分片 + 提升缓存命中） |

## 四、文件名噪音（清洗规则，脚本已实现）

文件名统一形如：
`{编号} {标题}【海量资源：ubkz.com】[16]-迅捷文字转语音-{13位时间戳}zh.txt`

清洗掉的部分（**绝不进正文**）：
- `【海量资源：ubkz.com】` —— 课程推广，属提示词明令删除项
- `[16]` 之类的方括号编号残留
- `-迅捷文字转语音-{时间戳}zh` —— 转写工具尾巴
- 标题尾部的 `(一)` `(二)` `（一）`（相似标题靠这个分组）

编号前缀形态混乱，有三种：`11-2` / `[10.10]--10-10` / `[10.4]`，脚本循环最多吃 3 轮。

## 三·补四、11.5~11.9 面试专题新增错译（2026-10-02 第 4 轮追加）

| 转写错法 | 正确术语 |
| --- | --- |
| `GOM` / `GAM` / `GOM堆内存` / `多内存` | **JVM 堆内存（heap）** |
| `压缩指针` / `GOM压缩指针在三十二g以下才开启` | **compressed oops（压缩指针）**，堆 > 32GB 失效，惯例设 31GB |
| `loadprocessor` / `load点processors` | **`node.processors`**（单机多实例设为物理核数的一半） |
| `clsterrouting和location剩下的host` | **`cluster.routing.allocation.same_shard.host: true`**（避免主副同机） |
| `bootscrapDMmemorylock` / `sccopememorylook` | **`bootstrap.memory_lock: true`** |
| `scwap` / `scwap分区` | **swap**（关闭 swap + `vm.swappiness`） |
| `dataclientdata获得datawarm和datacode` | **`data_content` / `data_hot` / `data_warm` / `data_cold`** |
| `read或者是优留状态` | **red / yellow 状态** |
| `盖inss的任务` / `inss` | **ingest（预处理）任务** |
| `索引的生命周期MA二` / `MR策略` / `IML策略` | **ILM（Index Lifecycle Management）** |
| `allocationexplain` / `_cluster/allocation/explain` | 同左；看 `assigned` 与 `decide.explanation` |
| `assigned付和和inreason` | **`assigned` 字段 + `unassigned.reason`** |
| `assigneddetail` / `assignedreason` | **`unassigned.details` / `unassigned.reason`** |
| `ptinctthis` / `开at架子` | **`GET /_cat/indices?health=red` / `_cat/shards`** |
| `暗散的分片` / `暗散的` | **未分配的分片（unassigned）** |
| `class的reroot` / `reroot` | **`POST /_cluster/reroute`** |
| `retrireevod` | **`?retry_failed=true`** |
| `accept带动nose` / `fdatedateloss` | **`accept_data_loss: true`** |
| `hellocalatingstyleprimary` / `allocate_stale_primary` | **`allocate_stale_primary`**（提升旧副本为主分片） |
| `allocate_empty_primary` | 同左（放弃损坏分片，剔除元数据） |
| `classroutingallocationstemshothost` | **`cluster.routing.allocation.same_shard.host`** |
| `rockID` / `rack_id` | **`node.attr.rack_id` + allocation awareness** |
| `lass的reroot` / `classreroot` | **`_cluster/reroute`** |
| `thislocationenable` / `locationenable` | **`cluster.routing.allocation.enable`**（`primaries` / `all` / `null`；**不能设 `none`**） |
| `flash` / `执行flash` | **`POST /_flush`** |
| `classhouse` / `classhealth` | **`GET /_cat/health`** |
| `threadpool` / `线程池池的大` | **`GET /_cat/thread_pool`** |
| `lose` / `hot_threads` / `热点线程` | **`GET /_nodes/hot_threads`** |
| `ricopenpending` / `pending任务` | **`GET /_cluster/pending_tasks`** |
| `划线alcode` / `allocation.exclude` | **`cluster.routing.allocation.exclude._ip`** |
| `firstmerch` / `facemerge` / `firstmatch` / `facematch` | **`forcemerge`** |
| `奥inexmerge` / `only_expunge_deletes` | **`?only_expunge_deletes=true`** |
| `ttask` / `txas` / `taskdetail` | **`GET /_tasks` / `POST /_tasks/{id}/_cancel`** |
| `插的pmonitor` / `collectionenable` | **`xpack.monitoring.collection.enabled: false`** |
| `mteropenschoolcontext` | **`search.max_open_scroll_context`** |
| `reininx` / `reindex` + `process` | **`conflicts: proceed`** |
| `OPtype` / `op_type` | **`op_type: create`** |
| `datarom` / `dataHODD` / `dataworm` / `dataAOD` | **`data_hot` / `data_warm` / `data_cold`** |
| `taylorpreference` / `include` | **`index.routing.allocation.include.<attr>`** |
| `分辨总数` / `每节点分片个数` | **`index.routing.allocation.total_shards_per_node`** |
| `indexlifeirql点name` | **`index.lifecycle.name`** |
| `bestcomression` / `bestcompression` | **`index.codec: best_compression`**（改前需 close） |
| `并发恢复的分辨数量` | **`cluster.routing.allocation.node_concurrent_recoveries`** |
| `每秒恢复数据大小` | **`indices.recovery.max_bytes_per_sec`**（单机多节点需减半） |
| `开recover` | **`GET /_cat/recovery/idx?v`** |
| `信号去删除` / `通费服务删除` | **`action.destructive_requires_name: true`** |
| `节点总分辨限制一千` | **`cluster.max_shards_per_node`**（7.x 起默认 1000） |
| `索引止读状态` / `禁读` | **`index.blocks.read_only_allow_delete` / `index.blocks.read`** |
| `losen` / `lucene实例` | **Lucene**（每个分片 = 一个 Lucene 实例） |
| `档合并` / `氮合并` / `蛋合并` / `蛋壳病` / `淡合并` | **段合并（segment merge）** |
| `sergomen` / `sugman` / `蛋` / `档` | **segment（段）** |
| `intsuffer` | **index buffer** |
| `marchmergecount` / `maximagecount` | **`maxMergeCount`**（超过则激活限流 throttle） |
| `masternumbersetcments` | **`max_num_segments`**（forcemerge 目标段数） |
| `mmergemiddle` / `mergeMiddle` | **`mergeMiddle` 阶段**（按结构分别合并） |
| `cromitmerge` / `commitMerge` | **`commitMerge` 阶段**（删旧段与物理文件） |
| `aftermerch` / `afterMerge` | **`afterMerge` 阶段**（重新评估限流） |
| `劣势存储` / `系列化的劣势存储` | **列式存储（doc values）** |
| `建值类` | **键值对（stored field）** |
| `报排列表` / `大排列表` / `postneist` / `postingunist` | **倒排列表（posting list）** |
| `倒瓣相` | **倒排项** |
| `postingnest` / `postinglist` | **posting list** |
| `max查询` / `nec查询` | **`LIKE` 查询** |
| `照白索引` / `倒排摄影` / `倒排索影` | **倒排索引** |
| `termdictionary` / `单词词典` | **term dictionary（`.tim` 文件）** |
| `termunist` / `tomindex` / `termundex` / `单词索引` | **term index** |
| `obsets` / `offsets` / `起始和结尾字符偏移量` | **`offsets`**（`index_options` 第四档，支持高亮） |
| `uniiteopenations` / `indexoptions` / `mainnexopence` | **`index_options`**（`docs` / `freqs` / `positions` / `offsets`） |
| `matchfreease` / `matchfriase` | **`match_phrase`** |
| `action分析` / 分词处理 | **analyzer 分词分析** |
| `block` / `objects` / `offset` | **词典 block / offset** |

## 三·补五、2.x Go 工程化专题新增错译（2026-10-02 第 5 轮追加）

| 转写错法 | 正确术语 |
| --- | --- |
| `勾` / `构` / `够` / `购物` / `高帽` / `勾浪` / `购line` / `goline` | **Go / Go 语言**（最高频，几乎每句都有） |
| `PK机` / `PKGPKG` / `PKGB` | **`pkg`** 目录 / 包 |
| `PKCC` / `PCC` | **`$GOPATH/pkg`**（放编译文件，加快后续编译） |
| `gopass` / `gopath` / `高pass` | **GOPATH**（`src` / `bin` / `pkg` 三个子目录） |
| `goget` / `高get` / `gate` / `getup` / `gethome` | **`go get` / git / GitHub** |
| `gthub` / `gate平台` / `gatee一` / `get一` | **GitHub / Gitee**（按上下文取；`gate` 系列基本都是 git） |
| `gorender` / `gomoderender` / `render` / `radder` / `rendow` / `radow` | **`go mod vendor` / `vendor` 目录** |
| `gomode` / `gomodel` / `高帽的` / `勾目的` / `勾帽的` / `gomodedemo` | **go module / go mod**（demo 工程名 `gomodedemo`） |
| `gomodeNIT` / `go的monIT` / `构modeNIT` | **`go mod init`** |
| `gomode开底` / `go的猜底` / `勾目的tidy` / `勾目的的胎比` / `勾目的拍` | **`go mod tidy`** |
| `gorun` / `gorn` / `goramin` / `goran` | **`go run`** |
| `gobill` / `gobd` / `go乱` / `gobd的` | **`go build`** |
| `构点mode` / `勾点mode` / `gomode的文件` | **`go.mod` 文件** |
| `构点sum` / `勾点sum` | **`go.sum` 文件** |
| `moreplace` / `replac` / `replace` | **`replace` 语法** |
| `exclude` / `requirerequire` | **`exclude` / `require`** |
| `goprivate` / `gopropersy` / `goproperate` / `goproxy` | **`GOPRIVATE` / `GOPROXY`** |
| `logRUS` / `logIUS` / `logREVS` | **logrus**（`github.com/sirupsen/logrus`） |
| `record` / `radk` / `redas` | **Redis** |
| `GRPC` / `gRPC` | gRPC |
| `yamoo` / `yamo` / `yumo` | **yaml** |
| `waper` / `whiper` / `微per` / `whapper` / `weaper` | **viper**（配置读取库） |
| `imadule` / `imagil` / `imagile` | **`viper.Unmarshal`** |
| `setconfigfile` / `点点waisetconfigfile` | **`viper.SetConfigFile`** |
| `readinconfig` / `微per点read` | **`viper.ReadInConfig`** |
| `watchconfig` / `握取` / `wichconfig` | **`viper.WatchConfig`** |
| `onconfigchange` / `conconfig陷阱` / `config陷阱` | **`viper.OnConfigChange`** |
| `FSnotify` / `FSnotifyevent` | **`fsnotify.Event`** |
| `单飞` / `够单飞` / `singlfight` | **singleflight**（`golang.org/x/sync/singleflight`） |
| `middlewell` / `middleware` / `bos的中间件` | **中间件 / middleware** |
| `root` / `route` / `router` | **路由 router** |
| `INI` / `NIT的方法` / `INIT` | **`init` 方法** |
| `CMD` / `CND` / `CMDdemo` | **`cmd` 目录 / `cmd/demo`** |
| `interneal` / `internal` / `特intert` | **`internal` 目录** |
| `PKGB函数` / `bservice` | demo 里的 `pkgb` / `bizService` 函数 |
| `frontent` / `prompt` / `baton` / `backattheorder` | demo 里的 `frontend` / `backend` 目录 |
| `restful` / `reststful` / `rerestful` / `restfor` / `reansforful` / `rsfful` | **RESTful** |
| `密冷性` / `密等性` / `幂等` | **幂等性** |
| `安全` / `安全性` | 安全性（只读） |
| `pose` / `破` / `put` / `delete` | **POST / PUT / DELETE** |
| `玻璃` / `玻璃当中` | **body / 请求体** |
| `UI` / `UII` / `URI` / `URL` | **URI / URL** |
| `中红线` / `中横线` | **中横线（hyphen `-`）** |
| `两百` / `四零一` / `四零三` / `四零四` / `五百` / `五零三` | **200 / 401 / 403 / 404 / 500 / 503** |
| `零六幺零零三二五` / `零六号项目组` | **错误码 06100325**（项目组+服务+模块+枚举） |
| `动境变量` / `环境变量` | **环境变量** |
| `ETCD` / `etcd` | **etcd** |
| `timeout` / `HTTPrequesttimeoutseconds` | `http_request_timeout_seconds`（命名带单位的示例） |
| `AKSK` / `健全` / `AK` / `SK` | **AK/SK 鉴权**（`健全` = 鉴权） |
| `sort` / `sorted` | sort（排序） |
| `maffile` / `makefile` | **Makefile** |
| `dockerfile` / `thefile` | **Dockerfile** |
| `composer` / `docker-compose` | **docker-compose** |
| `supervisord` / `systemd` | **supervisord / systemd** |
| `swagger` / `protobuff` / `protoal` | **Swagger / protobuf / .proto** |
| `DDD` / `createtive` / `kitex`语境 | **DDD 设计思想**（`createtive` 疑似某框架名，**存疑**） |
| `MVC` | MVC |
| `SEO` | SEO |
| `CICD` / `CI/CD` | CI/CD |
| `SDK` / `解码的SDK` | SDK |
| `九零九零` / `端口九零九零` | **端口 9090** |
| `六十` / `excel是六十` | 配置项取值，**语义存疑**（疑似某个超时/限流配置），不臆造 |
