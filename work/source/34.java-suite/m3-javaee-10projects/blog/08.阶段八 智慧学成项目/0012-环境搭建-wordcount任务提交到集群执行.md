# WordCount 上集群：打包、上传与 spark-submit 提交全流程

IDEA 里跑通只能说明代码逻辑对，运行环境仍然是本机。课程环境的真身是 Docker 编排的 CDH 集群，Spark 任务最终要交给集群跑。这一步新手最容易栽在三个地方：打包完用 java -jar 直接跑报错，提交了任务 Web UI 上却找不到，或者集群上跑的结果和本地对不上。按打包、上传、提交、观察四步走，一次理顺。

## 先给结论

- 打包前先把 `application.properties` 的 `useingCluster` 改为 true，让代码走集群分支，然后在 Maven 视图选中父工程 xc-analysis，Lifecycle 里执行 package。
- 要用的是 target 下带依赖的 `xc-service-offline-jar-with-dependencies.jar`，改名成 wordcount.jar；这个包不能用 java -jar 直接运行，只能交给 spark-submit。
- 上传分两跳：WinSCP 把 jar 传到宿主机 `/opt/jars` 目录，再用 `docker cp` 复制进 xc-online-spark 容器的 `/opt` 目录。
- 提交命令是 `spark-submit --class com.study.xc.first.WordCount --master spark://xc-online-spark:7077 wordcount.jar`，任务约 6 秒跑完，结果与本地一致。
- 观察入口：Spark Master 管理页在 8080 端口，Running Applications 里能看到 WordCount；任务 stdout 日志把页面地址里的容器主机名换成 hosts 域名，就能在外部浏览器打开。

## 打包：要的是带依赖的 jar

第一件事是改配置文件，把 local 开关切到集群模式：

```properties
# 是否使用集群模式：true 为集群模式，false 或不配置默认 local 模式
useingCluster=true
```

然后在 IDEA 的 Maven 视图里选中父工程 xc-analysis，展开 Lifecycle 双击 package。打包要把全部依赖一起打进 jar，时间比单纯编译长不少，控制台构建日志滚完后，target 目录里会生成两个包：一个是不带依赖的普通 jar，体积小；另一个是 `xc-service-offline-jar-with-dependencies.jar`，把 Spark 之外的所有依赖都装了进去。运行用的是后者，按文档改名为 wordcount.jar，后续命令都认这个名字。

讲义配图里用红字标了一句话：打包后，不能直接运行。这句话值得单独解释。带依赖的 jar 依然是普通的 Java 归档，里面没有集群运行所需的上下文，用 java -jar 跑起来连不上任何集群。启动 driver、向集群注册、申请资源这些动作全由 spark-submit 负责，它才是集群任务的入口。

## 上传：宿主机转手一次进容器

jar 在开发机上，Spark 容器在服务器上，中间要转一次手。用 WinSCP 把 wordcount.jar 上传到服务器 `/opt/jars` 目录（目录不存在就新建一个），然后在服务器终端把包复制进 Spark 容器：

```bash
# 把 jar 从宿主机复制进 Spark 容器的 /opt 目录
docker cp wordcount.jar xc-online-spark:/opt
# 登录 Spark 容器
docker exec -it xc-online-spark bash
```

容器里 ls 确认 wordcount.jar 已经在了，接下来就是提交。

## 提交与观察：Web UI 上看到任务才算数

提交命令一行：

```bash
spark-submit --class com.study.xc.first.WordCount --master spark://xc-online-spark:7077 wordcount.jar
```

三个参数各管一段：

- `--class`：程序主类的全限定名，也就是 IDEA 里那个 object 的包名加类名，在编辑器里对类名右键 Copy Reference 可以直接复制，避免手写漏掉包名。
- `--master`：Spark 集群地址，`spark://xc-online-spark:7077` 指向 Standalone 模式的 Master，任务由它调度到 Worker 上执行。
- `wordcount.jar`：程序本体。如果依赖没有打进包里，还要加 `--jars` 逐个指定依赖文件；用了带依赖的 jar 就不需要。

这条命令在课程后续章节里会反复出现：调度脚本里的写法是把 spark-submit 的完整路径写死为 `/opt/spark/bin/spark-submit`，jar 固定放在 `/opt/run/jars/` 目录，主类与日期参数按任务替换，骨架与这里的命令完全一致。

命令敲下去终端开始刷日志，此时浏览器打开 `xc-online:8080` 的 Spark Master 页，Running Applications 里已经出现 WordCount，整个任务大约 6 秒跑完进入完成状态。点进任务详情可以看到 executor 分配与各 Stage 的进度；stdout 日志页默认用容器内部地址，把地址里的主机名换成 hosts 里映射的域名即可在外部浏览器直接打开。终端里同步输出统计结果：java 3 次，scala 2 次，与 IDEA 本地测试完全一致。整条链路串起来是这样：

```mermaid
flowchart LR
    A["Maven package 打出带依赖 jar"] --> B["改名 wordcount.jar"]
    B --> C["WinSCP 上传到宿主机 opt jars"]
    C --> D["docker cp 复制进 Spark 容器"]
    D --> E["spark-submit 指定主类与 master"]
    E --> F["Master 调度 Worker 拉起 executor"]
    F --> G["executor 从 HDFS 读 word.txt 计算"]
    G --> H["结果回 driver 输出并可在 Web UI 查看"]
```

## 集群模式背后发生了什么

回看 EtlEnvironment 的集群分支就明白配置开关的意义：`useingCluster=true` 时只 setAppName 不设置 master，SparkConf 里没有集群地址，这时硬在 IDEA 里 Run 会直接报 master 缺失；换成 spark-submit 提交，`--master` 参数把地址补上，两种环境共用同一份代码。

spark-submit 在背后做的事可以按顺序捋一遍：先在容器内启动 driver 进程执行主类；driver 拿着 `--master` 的地址向 Standalone Master 注册应用；Master 在空闲 Worker 上分配内存并拉起 executor；executor 反向注册到 driver 后开始领取任务；任务调度时结合数据本地性，把计算尽量派到存有对应 HDFS 数据块的节点附近执行。这也是为什么数据必须放在 HDFS：executor 分散在各个容器里，只有 HDFS 这个统一入口能让每个 executor 都读到同一份输入。

## 常见误区

- **忘记把 useingCluster 改成 true 就打包。** 错例：SparkConf 已被 setMaster 写死为 local，提交到集群后任务只跑在 driver 进程内部，Web UI 上看不到真正的集群计算。正解：改配置和打包是绑定动作，先改配置再 package。
- **用不带依赖的 jar 提交。** 错例：拿了体积小的那个包提交，运行时报类找不到。正解：认准 `-jar-with-dependencies` 结尾的包，或者用 `--jars` 把依赖补齐。
- **--class 只写类名不写包名。** 错例：`--class WordCount`，直接报主类不存在。正解：用 Copy Reference 拿全限定名 `com.study.xc.first.WordCount`。
- **word.txt 没传或路径写错。** 错例：集群日志报 Input path does not exist。正解：先在 HDFS 管理页确认文件在根目录，代码里的路径与实际存放位置保持一致。

## 面试可能被问到的问题

1. 面试官追问：「spark-submit 提交任务后，集群里发生了什么？」
   答：spark-submit 首先启动 driver 进程运行用户主类，driver 根据 master 参数向 Standalone Master 注册应用，Master 在满足条件的 Worker 上拉起 executor，executor 反向注册到 driver。之后 driver 把作业切分成 Stage 和 Task 下发，executor 领取任务执行并汇报状态，任务全部结束后资源释放。
2. 面试官追问：「fat jar 和 --jars 指定依赖两种方式怎么选？」
   答：fat jar 把依赖全部打进一个包，提交命令简单，离线环境友好，代价是包大、依赖变更要重新打包；--jars 保持业务包瘦小，多任务可共享依赖文件，但要维护依赖清单。课程工程任务统一、版本固定，选 fat jar，命名统一后调度脚本也更好写。
3. 面试官追问：「为什么提交到集群的程序必须读 HDFS？」
   答：executor 分布在不同容器甚至不同节点上，本地路径只对 driver 所在机器有意义。HDFS 是全集群统一的文件入口，任何 executor 都能按同一个路径读到数据，调度时还能利用数据本地性把计算挪到数据所在节点，减少网络传输。
4. 面试官追问：「master 参数里的 spark://xc-online-spark:7077 是什么？」
   答：这是 Spark Standalone 模式下 Master 的 RPC 地址，7077 是默认端口，spark-submit 与 driver 都通过它向 Master 注册和申请资源。写成 local 则整个任务收在 driver 进程里跑，集群地址与 local 的差别就在这里。
5. 面试官追问：「本地测试通过，上集群结果却不一样，你会先查什么？」
   答：先查数据源是否同一个，本地读的文件与集群 HDFS 上的文件内容是否一致；再查配置开关，确认打包时集群模式已生效而不是 local；然后看 driver 日志与 Web UI 上各 Stage 的输入记录数，确认读到的数据量符合预期；最后核对客户端依赖与集群组件版本是否一致。

## 配套资料

- 讲义：`materials/docs/08/智慧学成-第1章-环境搭建v1.0.md`，2.4.2 提交 Spark 任务到集群，打包步骤、docker cp 与 spark-submit 命令的出处。
- 调度脚本：`materials/code/08/_散落资料/`，后续章节真实 spark-submit 调度脚本与 docker-compose 编排文件所在目录，master 地址与 jar 路径的写法即出自这批脚本；目录内文件原始名带站点后缀，属元信息，不进正文。
- 说明：Scala 源码工程未随归档解压，WordCount 与 EtlEnvironment 的完整代码见上一篇，包名已按 `com.study.xc` 系改写；打包与提交日志按课程画面线摘录。
