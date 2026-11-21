# Superset 管理端走读：六大功能区与 Druid 数据源接入

> 🔒 安全提示：文中示例的口令/密钥均为课程教学环境演示口径，生产环境的安全要求见《安全与合规须知》。

装好 Superset，admin 登录进去，第一眼是顶部一排菜单：安全、管理、数据源、SQL 工具箱、Charts、看板。六个入口对应六类工作，不知道每个页签管什么，排查问题时就会迷路。平台要接的两种库也在这里配置：MySQL 走 SQLAlchemy URI，Druid 集群另有独立入口，端口与协议都不一样。

## 先给结论

- 管理端六大功能区：安全、管理、数据源、SQL 工具箱、看板、Charts，功能架构可以画成一张以 Superset 为中心的地图。
- 安全是权限体系入口：用户列表、角色列表、用户统计、基本权限、视图和菜单、操作日志；admin 拥有全部权限，public、alpha、gamma 各管一段。
- 数据源是日常重点：先加数据库连接（核心填 SQLAlchemy URI），再建数据表（数据集）；Druid 集群单独一个菜单，支持扫描与刷新 Druid 数据源。
- SQL 工具箱等价于一个网页版 SQL 客户端：数据源配好后直接写 SQL 查询，关系型与非关系型通吃。
- 课程环境已接入两个 MySQL 连接，示例表 users、cold_meter、cold_message_realtime；Druid 侧数据来源 all_device_message 由扫描刷新进来。

## 一、六大功能一张图

课件给的功能架构图以 Superset 为中心分出六个分支，先把结构看全：

```mermaid
flowchart TB
    SUP["Superset"] --> SEC["安全"]
    SUP --> ADM["管理"]
    SUP --> SRC["数据源"]
    SUP --> LAB["SQL 工具箱"]
    SUP --> DASH["看板"]
    SUP --> CHA["Charts"]
    SEC --> S1["用户统计"]
    SEC --> S2["基本权限"]
    SEC --> S3["权限与菜单"]
    SEC --> S4["操作日志"]
    ADM --> A1["导入表单"]
    ADM --> A2["CSS 模板"]
    ADM --> A3["查询与注释"]
    SRC --> R1["数据库"]
    SRC --> R2["数据表与上传 CSV"]
    SRC --> R3["Druid 数据源：扫描与删除"]
    LAB --> Q1["SQL 编辑器"]
    LAB --> Q2["查询历史与已保存查询"]
```

六个分支的分工一句话讲完：安全管账号与权限，管理区放看板周边的辅助功能，数据源管一切取数的入口，SQL 工具箱管手工查询，Charts 管图表制作，看板管图表编排。日常使用频率最高的是数据源、SQL 工具箱、Charts 与看板四个，安全配置一次就少动。

## 二、安全页签：权限体系的家底

用户列表负责添加 Superset 的用户名与密码，并控制账号是否激活。角色列表挂着系统默认的几个角色：admin 拥有全部权限；public 是基础底座；alpha 与 gamma 各对应一档可见范围。权限从角色来，不直接挂在用户上，收权放权都改角色。用户统计记录登录状态与登录时间等日志信息。

基本权限页是系统默认权限的清单，`can_this_form_post`、`can_this_form_get`、`can_edit`、`can_add`、`can_delete`、`can_download` 这类条目，粒度细到单个表单动作，这些是平台预设的，页面上不做增删改。视图和菜单列出系统默认开放的功能入口，同属只读。操作日志记录哪个用户在什么时候执行了 explore、log、explore_json 之类的动作，排查「谁动了图表」时先翻这里。

## 三、数据源页签：数据库与数据集两级

数据源下分两层。**上层是数据库连接。** 数据库列表每行一个连接，课程环境已有两个 MySQL 连接，Backend 标记为 mysql，每行还带允许同步运行、允许异步运行、允许 DML 等开关。点加号新建连接，表单的核心字段是 SQLAlchemy URI，具体格式可到 SQLAlchemy 官方文档的 Database URLs 页面核对，课堂演示就是打开这个页面对照着填：

```bash
# MySQL 连接：协议、账号密码、主机、端口、库名加字符集
mysql://root:123456@mysql.example.com:3306/coldchain?charset=utf8
# Druid 集群连接：走 Broker 服务的 8082 端口
druid://druid.example.com:8082/druid/v2/
```

MySQL 那行好理解。Druid 那行要单独解释：Superset 连 Druid 集群走 Broker 的 8082 端口；而 Java 程序查 Druid 用的是 Avatica SQL 网关的 8888 端口，cold-druid 工程 `DruidHelper` 的连接串指向的就是 8888。两个入口服务不同使用方，端口不要混用。密码按课程环境如实填写，示例里 123456 这类弱密码只属于实验环境。

**下层是数据表（数据集）。** 数据库下面挂表，表清单里能看到用户示例表 `users`、设备表 `cold_meter` 与实时消息表 `cold_message_realtime`（表名按项目口径改写），在这里新增、修改表并定义字段口径。新版 Superset 把这两层收进 Data 一级菜单下的 Databases 与 Datasets 两个子项，名称不同，层级关系一样。

Druid 集群在数据源区还有独立菜单：连接 Druid 集群与数据源、扫描新的 Druid 数据源、刷新与删除已有数据源。设备消息持续写进 Druid，新数据源出现后执行一次扫描刷新，它就会出现在数据清单里，再从清单建成数据集。

## 四、SQL 工具箱、Charts 与看板

SQL 工具箱（SQL Lab）是一个网页版 SQL 客户端：选数据库，写 SQL，点运行出结果。只要数据源里配好了，关系型与非关系型这里都能查，验证口径最顺手（示例按本课写法补全）：

```sql
SELECT housename,
       MAX(tem) AS max_tem,
       AVG(hum) AS avg_hum
FROM all_device_message
WHERE __time >= CURRENT_TIMESTAMP - INTERVAL '1' DAY
GROUP BY housename
```

数字对得上，再把同一条口径转成图表：Charts 页添加新图表，选数据源、选可视化类型（如 Line Chart）、配维度与指标，生成一张 chart；看板页编辑看板，把做好的图表编排进去。管理区的 CSS 模板可以编写样式并在看板中显示，导入表单负责把外部图表导入看板；查询与注释两个功能用得较少，知道入口即可。

## 常见误区

- **把数据库连接当数据集。** 错例：加了数据库连接就直接建图表。正解：连接只解决连得上，字段口径在数据表（数据集）层定义，两层都配好图表才有数。
- **Druid 连接串套 JDBC 习惯。** 错例：把 `jdbc:avatica:remote:url=...:8888` 填进 Superset 的 SQLAlchemy URI。正解：Java 程序走 8888 的 Avatica 网关，Superset 连 Druid 集群走 Broker 8082 的 `druid://` URI，两个入口别混。
- **权限角色随手给。** 错例：图省事把业务同学全加进 admin。正解：admin 是全部权限，日常分析给 gamma 一类受限角色，数据源与看板的可见性按角色收敛。
- **把操作日志当审计合规日志。** 错例：拿操作日志页满足安全审计要求。正解：它记录的是页面动作且粒度有限，敏感操作审计要靠库层与网关层日志补位。

## 面试可能被问到的问题

1. 面试官追问：「Superset 管理端有哪些核心功能区？」
   答：安全、管理、数据源、SQL 工具箱、看板、Charts 六大块。安全管用户角色与权限日志，数据源管数据库连接与数据集，SQL 工具箱做手工查询，Charts 做图表，看板做编排，管理区放 CSS 模板与导入等辅助功能。
2. 面试官追问：「在 Superset 里接入一个新 MySQL 库要几步？」
   答：数据源页新建数据库，核心是填对 SQLAlchemy URI；再到数据表层把要分析的表建成数据集并定义维度指标口径；最后用 SQL 工具箱跑一条 SQL 验证连通与口径，三步缺一不可。
3. 面试官追问：「Superset 连 Druid 和 Java 程序连 Druid 有什么区别？」
   答：Superset 走 Druid 集群 Broker 端口 8082，URI 形如 druid://host:8082/druid/v2/；Java 程序走 Avatica SQL 网关 8888，连接串 jdbc:avatica:remote:url 指向 /druid/v2/sql/avatica/。协议与端点都不同，按使用方选择。
4. 面试官追问：「alpha、gamma、public 这些角色是什么关系？」
   答：系统默认角色，admin 全权限；public 是基础底座；alpha 可见全部数据源做分析，gamma 只能看被授权的数据源与看板。用户通过角色拿权限，基本权限清单里还有 can_edit、can_add 这类细粒度条目。
5. 面试官追问：「Druid 里新出现了数据源，Superset 怎么感知？」
   答：在 Druid 集群菜单执行扫描刷新，把集群里已有的数据源同步进清单，再在数据集层建表定义口径，图表即可取数；持续写入的场景每隔一段时间补一次扫描。

## 配套资料

- 代码：`materials/code/06/day8 数据可视化/`，本课无配套源码包，SQLAlchemy URI 与 SQL 示例为按本课写法补全。
- 代码：`materials/code/06/day7 统计分析/`，cold-druid 真实工程，`DruidHelper` 的 8888 Avatica 连接串与数据来源 all_device_message 以该工程为准。
- 说明：表名与包名按 com.study.coldchain 口径改写；主机地址以 example.com 占位；引用路径截至 day 目录层级。
