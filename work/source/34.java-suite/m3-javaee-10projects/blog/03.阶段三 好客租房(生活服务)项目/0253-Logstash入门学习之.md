# Logstash 入门学习之合辑：管道三段式、首跑 Hello World、Filebeat 整合与写入 Elasticsearch

## 先给结论

- 四篇内容走完 Logstash 入门一圈：定位与 input、filter、output 三段管道，解压首跑 stdin 到 stdout，接入 Filebeat 监听 5044，output 指向 Elasticsearch 并在 Kibana 出图。
- Logstash 是开源的服务端数据处理管道：input 收数、filter 加工、output 送达；与 Beats 是分工不是二选一，Beats 管采集、Logstash 居中加工、Elasticsearch 存储、Kibana 可视化。
- 部署零门槛：JDK 1.8 以上、tar 解压即用；`-e` 把管道定义直接写在命令行，filter 不是必须段可以整段省略，看到 9600 端口的 API endpoint 才算就绪。
- Filebeat 整合只改两处：采集端 output 段换成 logstash 指向 5044，Logstash 侧加 beats 输入监听 5044；启动先 Logstash 后 Filebeat，顺序反了靠持续重试自动接上。
- 联调期输出先走 stdout 加 rubydebug 在控制台看全字段，确认无误再切 Elasticsearch；加 `--config.reload.automatic` 改配置自动生效，免反复重启。
- 经 Logstash 输出的索引默认按天创建，名字形如 logstash-日期，与 Filebeat 直连时的 filebeat-版本-日期 是两套命名，Kibana 建索引模式时按 `logstash-*` 匹配。
- Kibana 收尾三步：建 logstash-* 索引模式、时间过滤器选 @timestamp、柱形图 Y 轴 Count X 轴 Date Histogram；filter 段的 grok 把整行日志拆成结构化字段，才是加工层真正的价值。

## 第1部分：采集之外的事交给它：Logstash 的定位与 input、filter、output 三段管道

学到这里链路已经能跑通了：Beats 在各台机器上采集，直接写进 Elasticsearch，Kibana 负责看。既然 Filebeat 自己就能直连 ES，Elastic Stack 里为什么还有一个 Logstash？官方介绍里说它也做「数据采集」，和 Beats 的功能是重叠的。重叠是真的，但重叠只是表象，Logstash 的价值在采集之外的那一半：对数据做加工。这一课把它的定位、在整套架构里站的位置、以及「什么时候才需要它」讲清楚，配置怎么写在下一课动手验证。

### 一、一句话定义：事件驱动的数据处理管道

课件里的定义值得逐词拆开读：Logstash 是开源的、事件驱动的数据处理管道，能够同时从多个来源收集数据、转换数据，然后将数据发送到所喜爱的「存储库」中，而这里的存储库当然是 Elasticsearch。

「事件」这个词是理解 Logstash 的入口。一条事件就是一份带结构的数据：日志文件里的一行、Metrics 采集到的一条指标、一条数据库变更记录，进了 Logstash 都会被包装成统一的 JSON 形态，带时间戳、带来源、带原文，之后的每一步加工都作用在这个事件对象上。「管道」则说明它是流动的：数据从 input 进来，流过 filter，从 output 出去，中间不停留、不落库，是实时流转的加工线，不是存储系统。「集中式」点出的是部署位置：它不装在每一台业务机器上，而是部署在少数服务端节点上，各处数据汇到这里集中加工，与单机铺开的 Beats 正好互补。

### 二、在 Elastic Stack 里的位置：承上启下的加工层

把前面几课的组件画到同一张图上，Logstash 的位置就清楚了：

```mermaid
flowchart LR
    A["Filebeat 等采集一切数据"] -->|"Ship 采集"| B["Logstash 高吞吐量数据处理引擎"]
    B -->|"Parse & Transform 解析转换"| C["Elasticsearch 核心存储与检索"]
    C -->|"Visualize 可视化"| D["Kibana 数据可视化"]
    E["各类数据源：日志、指标、数据库"] --> B
```

这张图里每条箭头上都标着动作：Beats 对 Logstash 做 Ship（运送），Logstash 对 Elasticsearch 做 Parse & Transform（解析与转换），Elasticsearch 对 Kibana 提供 Visualize（可视化）。四个组件的角色标注同样能对上号：Beats 是「采集一切数据的」轻量采集器，Logstash 是「高吞吐量数据处理引擎」，Elasticsearch 是「核心存储和检索引擎」，Kibana 是「数据可视化」。课件还给了 Logstash 的去向图：多源数据汇入后可流向分析、归档、监控、告警四个方向，实际项目里绝大多数数据的终点就是 Elasticsearch，进了 ES，后续的图形化展示与告警都顺理成章。

### 三、采集与处理，两个功能两副面孔

Logstash 的功能标牌写着两件事：数据采集、数据处理。处理才是它的招牌。

**采集层面，它和 Beats 重叠，但形态不同。** Logstash 的 input 插件覆盖面很广：文件、stdin、TCP/UDP、Redis、Kafka、JDBC 等都能收，单节点吞吐量高；代价是基于 JVM，内存占用大、启动慢，铺到几百台机器上不现实。Beats 恰好相反：单个 Go 编译的二进制，资源占用以 MB 计，天生为「装到每台机器上」设计。所以采集这一层，实际项目里基本让给了 Beats。

**处理层面，这是 Beats 给不了的。** Beats 自带的处理器能做些轻量动作：加个字段、删个字段、解码 JSON。而日志解析这种正事，比如把一条 Nginx 访问日志按格式拆出 IP、URL、状态码、耗时十几个字段，要用 grok 正则解析；Java 异常栈一行日志跨十几物理行，要合并成一条事件再解析；多来源数据要按规则路由到不同输出，这些都属于 Logstash filter 的日常。生产上它存在的意义就是把杂乱的原文变成结构化数据。

**什么时候需要 Logstash，一张表说清：**

| 场景 | 直连够用吗 | 选择 |
|---|---|---|
| 采集目标单一，原文入库即可 | 够用 | Beats 直写 ES，链路最短 |
| 日志需要解析成结构化字段 | 不够 | 中间加 Logstash 做 filter |
| 多来源汇聚、统一路由 | 不够 | Logstash 居中收口 |
| ES 写入压力大需要缓冲 | 不够 | Logstash 做汇聚与批量写入 |
| 采集点资源极度敏感 | 直连为主 | Beats 采集，Logstash 集中部署 |

一句话总结分工：能轻则轻，Beats 能干的别上 Logstash；需要加工、需要汇聚时，Logstash 上场。两条链路在架构里经常同时存在，按数据是否需要加工来分流。

把三段结构落到配置上，一条典型管道的骨架是这样（示例，按 Logstash 官方语法书写，下一篇动手验证）：

```bash
input {
  beats { port => 5044 }                    # 接收 Filebeat 送来的数据
}
filter {
  grok { match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request}" } }
  mutate { remove_field => ["port", "prospector"] }   # 清理无用字段
}
output {
  elasticsearch {
    hosts => ["192.168.1.7:9200", "192.168.1.7:9201", "192.168.1.7:9202"]
  }
}
```

input 段开 5044 端口等着 Beats 连，filter 段用 grok 把原文拆成结构化字段、顺手删掉噪声字段，output 段写进 ES 集群。三段各占一块、顺序固定，插件名和参数可换，骨架不变。

## 第2部分：Logstash 首跑：解压即用，一行 -e 命令从 stdin 打到 stdout

装新组件最怕环境坑：版本不对、依赖缺失、启动报错堆成山。Logstash 这一步反而简单，它的第一个示例连配置文件都不用写，一条 `-e` 命令把管道定义直接塞给命令行，键盘敲进去什么、屏幕回显什么，跑通它就等于验证了整条管道。动手之前，先把上一课说的三段式流程在图上看一遍，再检查 JDK、解压、启动、敲入第一个 hello。

### 一、先看流程图：Pipeline 三段式

课件里的处理流程把 Logstash 的骨架画得很清楚：左边是数据源，右边是 Elasticsearch，中间那个方框就是 Logstash 的 Pipeline（管道），一条事件从左到右依次流过管道内的三个组件：

```mermaid
flowchart LR
    A["数据源 Data Source"] --> B["input 输入插件"]
    B --> C["filter 过滤插件，可省略"]
    C --> D["output 输出插件"]
    D --> E["Elasticsearch"]
```

三个组件各管一段：input 负责接收数据，事件从这里诞生；filter 负责加工数据，解析、改写、增删字段都在这里；output 负责送出数据，去 ES、去屏幕、去文件由它决定。架构说不上复杂，复杂度都藏在各段插件的配置里。第一个示例刻意把 filter 留空、把 input 和 output 选成最朴素的 stdin 与 stdout，把注意力全部留在「事件怎么流动」上。

### 二、环境检查与解压

检查 JDK 是第一步，Logstash 依赖 Java 运行环境，要求 1.8 以上：

```bash
java -version
# java version "1.8.0_141"
# Java(TM) SE Runtime Environment (build 1.8.0_141-b15)
# Java HotSpot(TM) 64-Bit Server VM (build 25.141-b15, mixed mode)
```

课程环境的 `1.8.0_141` 满足要求。接着把安装包上传到存放 Beats 的同一个目录，然后解压：

```bash
tar -xvf logstash-6.5.4.tar.gz
cd logstash-6.5.4
ll
# bin  config  data  lib  logs  modules  vendor ...
```

解压出来就是一个标准的目录结构，没有编译、没有安装脚本。要说「标准 Java 项目」的味道也确实有：启动脚本在 `bin` 下，配置文件在 `config` 下，`lib` 里全是 jar 包，目录扫一眼就知道东西在哪。版本与前面几课的 Elasticsearch、Kibana、Beats 保持同一梯队（6.5.4），整套栈混用大版本是排障的额外负担，尽量别这么干。

### 三、第一条管道：stdin 进，stdout 出

启动命令一行搞定，`-e` 后面用单引号包住整段管道定义：

```bash
bin/logstash -e 'input { stdin {} } output { stdout {} }'
```

`input { stdin {} }` 声明从标准输入读事件，`output { stdout {} }` 声明把事件打印到标准输出，两个花括号里空着表示全部用默认参数。启动过程要耐心等，JVM 起来、插件加载、管道初始化，十几秒到几十秒都正常，日志刷到最后出现类似这样的内容才算就绪：

```bash
[INFO ][logstash.pipeline        ] Pipeline started {"pipeline.id"=>"main"}
[INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}
```

API 端口 9600 是 Logstash 自身的监控端点，和 ES 的 9200 没有关系，别混。就绪后光标停在等待输入的状态，敲一个 `hello` 回车，屏幕立刻回显：

```json
{
       "@version" => "1",
           "host" => "node01",
         "message" => "hello",
      "@timestamp" => 2019-01-15T15:22:41.020Z
}
```

实际输出的字段顺序以终端为准，上面节选的是重点。`hello` 原封不动进了 `message` 字段，这正是 stdin 的行为：把一行输入包成一条事件；`@timestamp` 是事件生成时刻，`@version` 是格式版本，`host` 是来源主机，这三个字段是 Logstash 自动附加的元信息，不是你输入的内容。stdout 的默认编解码器把整条事件按 Ruby 风格格式化打印，键值一目了然。多敲几行就明白管道在转：每一行输入都是一条独立事件，回显的字段结构完全一致，变的只有 `message` 和时间戳。

### 四、回头看命令：为什么没有 filter

命令里只有 input 和 output 两段，filter 去哪了？答案是：不需要可以不写。filter 在管道里是可选段，不配置它事件就原样通过，不做任何加工。第一个示例里输入 hello、输出还是 hello，没有任何变换，省略 filter 正合适。等下一篇要做日志解析、字段改写时，再往中间插 filter 段，管道结构不变，只是流水线上多了一道工序。

`-e` 这个参数也值得记住：它的意思是 evaluation，管道定义直接跟在命令行里，适合验证和试验。写成配置文件交给 `-f` 加载才是生产做法，配置一多，命令行里塞不下去也不便于管理。`-e` 玩熟了，`-f` 只是换了个放配置的地方，管道语法完全一样。

## 第3部分：Filebeat 采来的 Nginx 日志交给 Logstash：5044 端口上的第一次握手

Filebeat 明明能直连 Elasticsearch，为什么中间还要插一道 Logstash？分工决定的：Filebeat 长在源头轻量采集，Logstash 长在集中加工，日志要解析、要补字段、要按规则路由，就得先把数据从采集端送到加工端。这一课拿 Nginx 的访问日志当素材，把 Filebeat 的 output 从 Elasticsearch 换成 Logstash，在 Logstash 侧开一个 beats 输入，两边联调跑通，为下一篇数据真正写入 ES 铺好路。

动手时最常见的第一跤摔在启动顺序上：Filebeat 一启动就刷 `connection refused`。配置没错，是 5044 端口后面还没人监听。

### 一、链路长什么样，日志源怎么准备

整合后的链路是三段：Nginx 产生日志，Filebeat 盯着日志文件采集，Logstash 在 5044 端口接收并做后续处理。课件里的架构图画得很直白：

```mermaid
flowchart LR
    U["浏览器访问 Nginx"] --> N["Nginx 80 端口"]
    N --> L["/var/log/nginx/access.log 追加一行"]
    L --> F["Filebeat 监控并采集"]
    F -->|"beats 协议发往 5044"| LG["Logstash beats 输入"]
    LG --> O["stdout 打印事件验证"]
```

关键的一条边是 Filebeat 到 Logstash：数据没有直奔 Elasticsearch，而是先交给 Logstash 处理，处理完去哪由 output 段说了算。本课先用 stdout 验证链路，加工逻辑下一篇展开。

日志源用 Nginx 现造。安装并确认服务状态：

```bash
apt install nginx -y
service nginx status            # 确认服务正在运行
service nginx start|stop|restart
```

Nginx 默认监听 80 端口，浏览器直接访问就能看到欢迎页。日志落在 `/var/log/nginx/access.log`，每刷新一次页面就多一行：请求 IP、时间、请求行、状态码、User-Agent 全在这行里。多刷几次看着文件增长，这就是 Filebeat 即将盯住的目标。

### 二、Filebeat 侧：output 换成 logstash

在 Filebeat 目录里把现成的配置复制一份改名为 `haoke-nginx.yml`，输入段指向 Nginx 的访问日志，输出段换成 logstash：

```yaml
# haoke-nginx.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/nginx/access.log
    tags: ["log"]
    fields:
      from: nginx
    fields_under_root: false

output.logstash:
  hosts: ["192.168.1.7:5044"]
```

三个细节值得留意。**第一，`fields` 自定义字段受 `fields_under_root: false` 约束。** `from: nginx` 标记数据来源，这个开关决定它落在事件的 `fields.from` 子对象里而不是根节点，后续按来源过滤路由时用得上。**第二，`tags: ["log"]` 给事件打了标签。** 采集侧打标、加工侧按标签处理，是两端协作的通用做法。**第三，output 里不再有 Elasticsearch 的影子。** `hosts` 指向的 `192.168.1.7:5044` 就是 Logstash 即将监听的地址。

启动 Filebeat：

```bash
./filebeat -e -c haoke-nginx.yml
```

此刻启动必定报 `connection refused`：5044 端口还没有任何进程监听，数据发不出去。Filebeat 不会因此退出，而是按退避节奏不断重试，这是采集器的本分。把进程留着，转去配 Logstash。

### 三、Logstash 侧：beats 输入监听 5044

进入 Logstash 的 `config` 目录创建管道配置 `haoke-pipeline.conf`：

```conf
input {
  beats {
    port => 5044
  }
}

output {
  stdout {
    codec => rubydebug
  }
}
```

input 段的 `beats` 插件是专门接收 Filebeat、Metricbeat 等 Beats 家族数据的入口，`port => 5044` 与 Filebeat 侧的 `hosts` 对上号。output 段先用 `stdout` 加 `codec => rubydebug`，把每条事件按易读格式完整打印，这是联调阶段最快的反馈方式。

启动前先用 `-t` 参数测试配置语法，测试完自动退出：

```bash
bin/logstash -f config/haoke-pipeline.conf -t
# Configuration OK
bin/logstash -f config/haoke-pipeline.conf --config.reload.automatic
```

测试结果 OK 再正式启动。`--config.reload.automatic` 打开配置热加载，之后调整管道只需保存文件，Logstash 自动重新加载，联调时改配置不用反复重启服务。

### 四、联调验证：一条日志的完整旅程

顺序已经就位：Logstash 监听 5044，Filebeat 在重试。此刻回看 Filebeat 的日志，重试报错停止，连接建立。回到浏览器刷新几次 Nginx 页面，`access.log` 每多一行，Logstash 控制台就打出一条事件，形如：

```json
{
       "message" => "192.168.1.20 - - [15/Jan/2019:23:35:10 +0800] \"GET / HTTP/1.1\" 304 0 \"-\" \"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36\"",
        "offset" => 13169,
          "tags" => ["log"],
          "beat" => { "version" => "6.5.4", "name" => "node01", "hostname" => "node01" },
    "prospector" => { "type" => "log" },
        "source" => "/var/log/nginx/access.log",
     "@timestamp" => "2019-01-15T15:35:10.020Z",
        "fields" => { "from" => "nginx" }
}
```

输出为节选，实际字段更多、顺序以终端为准。逐个核对：`message` 是 Nginx 原始日志整行，一字未动；`source` 是来源文件路径，`offset` 是读取偏移；`tags` 与 `fields.from` 正是采集侧配置的两个自定义项，原样跟到了对端；`beat` 带着采集器的主机与版本信息。这些字段一起出现，说明 Filebeat 到 Logstash 这一段完全打通，后面的解析与入库都在这条事件上做文章。

## 第4部分：Logstash 加工完的日志写入 Elasticsearch：logstash 索引入库与 Kibana 出图

上一课把 Filebeat 与 Logstash 打通，事件用 stdout 打印在控制台，看完就没了。控制台只是联调手段，日志链路的终点在 Elasticsearch：只有写入索引，数据才能长期保存、被检索、被画成图。这一课把 `haoke-pipeline.conf` 的 output 段换成 elasticsearch，看索引怎么按天出现，再到 Kibana 里建索引模式、查数据，把 25 条访问日志变成一张柱形图。

### 一、最小改动：output 段指向 Elasticsearch

`haoke-pipeline.conf` 只动 output 段，原来的 stdout 注释掉留作对照：

```conf
output {
  # stdout {
  #   codec => rubydebug
  # }

  elasticsearch {
    hosts => ["192.168.1.7:9200", "192.168.1.7:9201", "192.168.1.7:9202"]
  }
}
```

`hosts` 是数组，三个 ES 节点都列上，写入请求分摊到各节点，某个节点故障时自动切到其余节点，与 Filebeat 直连 ES 时的多节点写法同理。保存后如果开着 `--config.reload.automatic`，配置自动生效；没开的话重启一次 Logstash。

### 二、课件里的完整管道：grok 加工在这一段

课件在「发送到 Elasticsearch」这一页给出了管道全貌，input、filter、output 三段齐备：

```conf
input {
  beats {
    port => "5044"
  }
}

filter {
  grok {
    patterns_dir => "/haoke/logstash-6.5.4/nginx-patterns"
    match => { "message" => "%{NGINX_ACCESS}" }
    remove_tag => ["_grokparsefailure"]
    add_tag => ["nginx_access"]
  }
}

output {
  elasticsearch {
    hosts => ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
  }
}
```

grok 是 Logstash 最常用的解析插件，用预定义的正则模式把整行文本拆成命名字段。`NGINX_ACCESS` 是一条现成模式，能把一条访问日志拆出客户端 IP、时间、请求行、状态码等十几个字段；`patterns_dir` 指向自定义模式目录，内置模式覆盖不了的日志格式就放这里。解析失败的事件会被自动打上 `_grokparsefailure` 标签，`remove_tag` 把它摘掉，`add_tag` 换上 `nginx_access`，避免失败标记一路跟进索引。课堂演示为了让链路最短，先只切了 output，filter 段按这份全貌补齐即可。

### 三、索引怎么出现：logstash-2019.01.15

启动后照旧造数据：浏览器刷新 Nginx 页面，Filebeat 采集，Logstash 转发。打开 elasticsearch-head 的概览页，集群 26 of 26 全绿，索引列表里多出一个 `logstash-2019.01.15`，名字由前缀 `logstash-` 加日期拼成，按天一个。

这个命名值得跟 Filebeat 直连时对比：直连 ES 时索引叫 `filebeat-6.5.4-2019.01.15`，带着 Beat 类型与版本号；经过 Logstash 输出后，索引名由 elasticsearch 输出插件的默认值决定，统一挂 `logstash-` 前缀。同一个数据源，走的路不同，落的索引也不同，看到索引名就能反推数据链路。

数据量验证最直观：head 里盯着 `logstash-2019.01.15` 的文档数，刷新几次页面后从 16 条涨到 25 条；稍等片刻再刷，数字继续涨，说明管道在实时工作。

### 四、Kibana 收尾：索引模式、探索与柱形图

数据进了 ES，Kibana 才是看它的窗口，三步走完。

**第一步，建索引模式。** 在 Kibana 的 Management 里 Create index pattern，填 `logstash-*` 匹配刚出现的索引，时间过滤器字段选 `@timestamp`。Kibana 靠索引模式决定查哪些索引，不建模式，Discover 里永远空白。

**第二步，Discover 探索。** 打开 Discover，选中 `logstash-*` 模式，时间范围调到 Last 4 hours，25 条访问日志列出来，`message`、`fields.from`、`beat.name` 一目了然，与 head 里看到的文档一一对应。继续刷新页面产生新请求，回到 Discover 再刷，新日志按时间排在最上面。

**第三步，画柱形图。** Visualize 里新建柱形图，选 `logstash-*` 索引模式：Y 轴用聚合 Count 统计条数，X 轴选 Date Histogram、字段 `@timestamp`，运行后柱子按时间分桶立起来，一个五分钟桶里 25 条、另一个 20 条，与实际请求节奏对得上。保存命名后在 Visualize 列表随时搜回，颜色可调，饼图、折线图的做法完全类似，多张图拼进 Dashboard 就是给运维看的日志大盘。

整条链路至此闭环：

```mermaid
flowchart LR
    U["浏览器刷新页面"] --> N["Nginx 写 access.log"]
    N --> F["Filebeat 采集"]
    F -->|"5044"| LG["Logstash beats 输入"]
    LG --> G["grok 解析整行日志"]
    G --> ES["Elasticsearch 集群三节点"]
    ES --> I["索引 logstash-当日日期"]
    I --> K1["Kibana Discover 查询"]
    I --> K2["Kibana Visualize 柱形图"]
```

从页面刷新到图上多一根柱子，数据流过了采集、加工、存储、可视化四层，每层都有明确的输入与输出，出了问题沿这条线逐段排查即可。

## 常见误区

- **把 Logstash 当成比 Filebeat 高级的采集器，处处用它替换。** 两者是分工关系，采集层铺 Beats、处理层用 Logstash 是标准架构，全用 Logstash 采集会把它的资源劣势放到最大。
- **认为有了 Logstash 就可以不要 filter。** filter 不写管道也能跑，但那等于花一台服务器的资源做转发，不如直连；上 Logstash 的理由就是 filter 里的加工逻辑。
- **把「存储库」理解成 Logstash 自己存数据。** 管道不落库，数据流过即走，存储由 output 决定，在这个体系里就是 Elasticsearch。
- **觉得它和 Beats 是新旧两代、二选一的关系。** 官方架构图里它们是串联的，Ship 之后接 Parse & Transform，一条链上的两道工序。
- **没查 JDK 就直接启动，报 Java 相关错误。** Logstash 靠 JVM 运行，先 `java -version` 确认 1.8 以上，省掉一轮无头案。
- **把启动慢当成卡死。** JVM 冷启动加插件加载，等几十秒很正常，判断标准是日志里出现 `Pipeline started` 与 9600 端口就绪信息，不是光标闪不闪。
- **以为回显的 JSON 是报错堆栈。** 那是 stdout 插件正常打印的事件内容，`message` 字段里就是你的输入。
- **把 9600 端口当成了 Elasticsearch 的 9200。** 9600 是 Logstash 自身监控 API，管道数据走不走 ES 与它无关。
- **试验阶段用 `-e` 塞大段配置。** `-e` 只适合一行以内的小管道，配置复杂后必须落到文件用 `-f` 加载，别在命令行里堆几十行单引号内容。
- **先起 Filebeat 后起 Logstash，被 connection refused 吓退。** 这只是对端未就绪，Filebeat 会自动重试；把 Logstash 起起来连接自行恢复，不用重启采集端。
- **把 5044 写成 9200。** 9200 是 Elasticsearch 的端口，`output.logstash` 必须指向 beats 插件监听的 5044，端口对不上永远握手失败。
- **以为 `from` 会出现在事件根节点。** `fields_under_root: false` 时它收在 `fields` 子对象里，检索与路由要按 `fields.from` 写；想放根节点就把开关改成 true。
- **跳过 `-t` 直接启动，配置手误让整条管道起不来。** 先测试再启动，几十秒换来一次语法确认，联调效率反而更高。
- **在 Discover 里找不到数据就以为没写进去。** 先确认索引模式建了没、模式名能不能匹配 `logstash-*`、时间范围是否覆盖数据时间，三处任何一处不对，界面都是空白。
- **以为索引还是 `filebeat-6.5.4-日期`。** 数据经 Logstash 输出后默认挂 `logstash-` 前缀按天建索引，拿着错的名字在 head 里找索引当然找不到。
- **grok 解析失败不管不问。** 失败事件带着 `_grokparsefailure` 标签照样入库，脏数据混进索引，检索时才发现字段全是空的；要么按课件摘掉失败标签，要么把失败数据路由到独立索引。
- **注释 stdout 时漏写 Logstash 的注释符。** 配置里的注释用 `#`，漏写或写在行中会直接语法错误，改完先跑一遍 `-t` 再启动。

## 面试可能被问到的问题

1. 面试官追问：「Logstash 和 Filebeat 有什么区别？」
   答：Filebeat 是轻量采集器，单二进制、资源占用小，只管把日志等数据送出去；Logstash 是基于 JVM 的数据处理引擎，input、filter、output 三段管道，能对数据做解析、转换、路由。采集选 Beats，加工选 Logstash，常见架构是两者串联。

2. 面试官追问：「Filebeat 已经能直写 Elasticsearch，为什么还要加一层 Logstash？」
   答：直写适合原文入库的简单场景。当日志需要 grok 解析成结构化字段、多来源需要统一汇聚路由、或者写入压力需要缓冲削峰时，中间加 Logstash 层来做这些事，ES 拿到的就是干净的结构化数据。

3. 面试官追问：「Logstash 的事件指什么？」
   答：一条事件就是一份统一封装的数据对象，JSON 形态，自带时间戳、版本、来源主机等元数据字段，原始内容放在 message 字段里。input 产出事件，filter 改写事件，output 消费事件，整个管道都围绕事件流转。

4. 面试官追问：「input、filter、output 三段各自负责什么？」
   答：input 负责接入，决定数据从哪来，常见有文件、beats 协议、TCP、Kafka；filter 负责加工，可做 grok 正则解析、字段增删改、条件判断、多行合并；output 负责送达，常见去向是 Elasticsearch，也可以是文件或其他消息系统。三段顺序固定，组成一条 Pipeline。

5. 面试官追问：「Logstash 有什么明显的缺点？」
   答：基于 JVM，内存占用高、启动慢，这是它被诟病最多的两点，也是采集职能被 Beats 取代的原因。部署上应该集中少数节点部署，而不是铺到每台业务机器上。

6. 面试官追问：「Logstash 除了把数据发给 Elasticsearch，还能干什么？」
   答：output 可插拔，数据可以归档到文件、转发到消息队列、送往监控告警系统，课件里给的方向就是分析、归档、监控、告警。只是在本技术栈中，它的输出绝大多数指向 ES，供 Kibana 展示。

7. 面试官追问：「Logstash 的 Pipeline 由哪三部分组成，各干什么？」
   答：input、filter、output 三段。input 从数据源接收数据并包装成事件；filter 对事件做解析、改写、条件处理，属于可选段；output 把事件送到目的地，常见是 Elasticsearch。事件按顺序流过三段，一次管道定义决定整条加工线的行为。

8. 面试官追问：「`-e` 和 `-f` 参数有什么区别？」
   答：`-e` 直接在命令行里给管道定义，适合 HelloWorld 级别的快速验证；`-f` 指定配置文件路径，生产环境的标准用法。两者解析的管道语法完全一致，区别只是定义放在哪里。

9. 面试官追问：「第一个示例没有 filter，管道能跑吗？」
   答：能。filter 是可选段，省略时事件原样从 input 直通 output，不做加工。HelloWorld 示例正是利用这一点验证环境；生产上上 Logstash 的主要理由就是 filter 里的加工逻辑，到那时再补这一段。

10. 面试官追问：「输入一行 hello，Logstash 输出了什么？」
   答：输出一条 JSON 事件，输入内容进 `message` 字段，同时自动附上 `@timestamp`（事件时间）、`@version`（事件格式版本）、`host`（来源主机）等元数据字段。这说明 stdin 把每行输入包装成独立事件，stdout 用格式化方式回显。

11. 面试官追问：「Logstash 启动为什么慢？」
   答：它基于 JVM，启动要完成 JVM 初始化、Ruby 插件体系加载、管道创建等多个环节，十几秒到几十秒常见。这也是它的采集职能被轻量的 Beats 取代的原因之一，集中部署的服务端节点对启动速度不敏感，问题不大。

12. 面试官追问：「Logstash 的 9600 端口是干什么的？」
   答：Logstash 自身的监控 API 端点，用于查询节点状态、管道运行情况等指标，默认绑定在本机回环地址。它与 Elasticsearch 的 9200 端口互不相干，一个是采集引擎的管理口，一个是存储引擎的服务口。

13. 面试官追问：「Filebeat 能直连 Elasticsearch，为什么还要经过 Logstash？」
   答：直连适合原文入库即可的场景；当日志需要解析成结构化字段、补富信息或按规则路由时，这些加工是 Logstash filter 的强项。Filebeat 管采集、Logstash 管加工是 Elastic Stack 的标准分工，这一课就是把数据先送到加工端。

14. 面试官追问：「5044 端口是干什么的？」
   答：Logstash beats 输入插件的默认监听端口，专门接收 Filebeat、Metricbeat 等用 beats 协议发来的数据。它与 Elasticsearch 的 9200、Kibana 的 5601 属于不同组件的不同端口，互不通用。

15. 面试官追问：「Filebeat 启动时报 connection refused，怎么排查？」
   答：先看 output 指向的地址与端口，确认对端是否有进程监听，多数情况是 Logstash 还没启动或端口写错。Logstash 就绪后 Filebeat 会自动重连，registry 记录的读取偏移保证数据不丢，不需要重启 Filebeat。

16. 面试官追问：「`--config.reload.automatic` 解决什么问题？」
   答：让 Logstash 周期性检查配置文件变更并自动重新加载管道，改配置不必停服重启。联调阶段频繁调整 filter 时体验明显，生产上也能降低配置变更的操作风险。

17. 面试官追问：「一条 Nginx 访问日志经过这条链路后变成了什么？」
   答：整行原文保留在 `message` 字段，同时事件自动带上来源路径 `source`、读取偏移 `offset`、时间戳 `@timestamp`、采集器信息 `beat`，以及配置的 `tags` 与 `fields.from`。采集侧加的标签和字段会一路带到 Logstash，供后续过滤与路由使用。

18. 面试官追问：「Logstash 输出到 Elasticsearch 的默认索引名是什么规则？」
   答：默认前缀 `logstash-` 加当天日期，例如 `logstash-2019.01.15`，按天创建一个索引。日志类数据按时间窗口切分，过期数据直接删整索引，保留策略好执行。

19. 面试官追问：「和 Filebeat 直连 ES 时的索引名为什么不一样？」
   答：索引名由写入端的默认行为决定。Filebeat 直连时用 Beat 类型、版本、日期拼成 `filebeat-6.5.4-日期`；经 Logstash 输出时走 elasticsearch 输出插件的默认命名 `logstash-日期`。看索引名就能反推这条数据有没有经过加工层。

20. 面试官追问：「Kibana 的索引模式是干什么的？」
   答：它声明 Kibana 要查询哪些索引，用 `logstash-*` 这类通配模式匹配，同时指定 `@timestamp` 之类的时间字段供时间过滤使用。不建索引模式，Discover 与 Visualize 都拿不到数据。

21. 面试官追问：「grok 插件的作用是什么，`_grokparsefailure` 怎么处理？」
   答：grok 用正则模式把非结构化文本拆成命名字段，是日志结构化的主力。解析失败的事件被自动打上 `_grokparsefailure` 标签，常见处理是按课件用 `remove_tag` 摘掉失败标记，或者把失败事件路由到独立索引，避免污染正常数据。

22. 面试官追问：「elasticsearch 输出的 hosts 写三个节点有什么讲究？」
   答：写入请求在节点间分摊做负载均衡，某节点不可用时自动切到其余节点，入库不中断。节点列表与 ES 集群实际部署保持一致，扩缩容时同步维护这份配置。

23. 面试官追问：「日志柱形图的横纵轴怎么配出来的？」
   答：Y 轴是聚合 Count，统计每个时间桶内的文档条数；X 轴是 Date Histogram，按 `@timestamp` 自动分桶，桶的间隔可调。这类时间维度的计数图是日志量监控的基础形态。

## 配套资料

- 课程资料包 `materials/code/03/day16-ElasticStack学习之Beats、Kibana、Logstash/` 解包后未含源码文件，本课为概念课，定位描述与架构图依据课件 5.1、5.2 章节整理，文中配置示例为按本课写法补全并已在下一课动手验证
- 采集侧组件的分工背景可对照同资料包 Beats 相关课件内容（前几课视频已覆盖）
- 课程资料包 `materials/code/03/day16-ElasticStack学习之Beats、Kibana、Logstash/` 解包后未含源码文件，安装命令、`-e` 管道命令与处理流程图依据本课课件 5.2 章节及课堂演示整理；事件输出 JSON 为按本课演示补全的示例并已注明（实际字段顺序以终端输出为准）
- Logstash 的定位与架构背景见同目录上一篇 `0253-Logstash入门学习之简介.md`
- 课程资料包 `materials/code/03/day16-ElasticStack学习之Beats、Kibana、Logstash/` 解包后未含源码文件，`haoke-nginx.yml`、`haoke-pipeline.conf` 与启动命令按本课课件 5.3 章节及课堂演示整理，事件输出 JSON 为演示节选，主机名已统一记作 node01
- 上游铺垫见同目录 `0253-Logstash入门学习之简介.md` 与 `0254-Logstash入门学习之部署安装(HelloWorld).md`，Filebeat 直连 ES 的对照写法见 `0243-Filebeat入门学习之输出到Elasticsearch.md`
- 课程资料包 `materials/code/03/day16-ElasticStack学习之Beats、Kibana、Logstash/` 解包后未含源码文件，output 配置与 grok 管道全貌按本课课件 5.3.5 节整理，文档数变化、索引模式与图表操作步骤依课堂演示整理
- 上一课两边联调见同目录 `0255-Logstash入门学习之Filebeat与Logstash整合.md`，Kibana 索引模式与数据探索的入门操作见 `0251-Kibana入门学习之数据探索.md`
