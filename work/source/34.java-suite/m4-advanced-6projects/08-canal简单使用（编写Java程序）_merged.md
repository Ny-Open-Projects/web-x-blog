# 08-canal简单使用（编写Java程序） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面咱们这个canner已经安装完了,并且进行了相应的配置。

那接下来咱们来看下一个小节,就是简单使用。

所谓简单使用其实就是什么呢?

我们来创建一个Mainware工程,然后通过这个Mainware工程能够连接到我们这个canner服务,也就是canner server上面。

而我们这个canner它是不是相当于把自己伪装成了一个slave,一个重解点。

一旦我们这个MySQL服务器里边的数据发生变化,那么这个canner就能够获取到,就能够通过日志的方式获取到。

而现在我们就是希望我们客户端再写一个程序,写一个Java工程,然后连接到我们这个canner server,然后来监控我们这个canner它获得到的日志。

然后在我们的Java程序当中就可以通过解析日志,能够知道MySQL数据。

然后我们就来看看这个MySQL数据那边执行的到底是一个什么样的Circle,对吧?

它执行前的数据是什么样子的,执行后的数据是什么样子的,等等。

所以说我们这个地方就是来看一下简单应用,就是来做这个事。

首先我们需要在咱们这个MySQL数据库当中,在MySQL服务当中来创建一个数据库,然后在数据库里面来创建这么一张表。

一会儿我们就操作这么一张表。

首先我们在这儿把这个数据库来创建一下。

咱们前面是不是已经启动了我们这个MySQL?

我们已经在这里创建了我们的MySQL容器,对吧?

那么并且我们在这儿已经连上来了。

咱们在这个地方来创建,新建一个新的数据库。

就叫做Counter-Test就可以了。

然后这个字符集我们来指定一下,使用这个UTF-8 MB4这种方式。

这个就使用这个就可以,点确定。

这样的话我们这个库就已经创建出来了,对吧?

好,创建好了之后我们来创建这么一个Student,这么一张表。

非常简单,就这么几个字。

字段,ID,NAME,AGE,SEX,CITY。

好,咱们把这个键表语句复制一下。

然后我们在这儿来创建一下。

好,在这儿执行一下这个SQL。

这样的话我们到这边来刷新一下。

好,稍等一下,刷新一下。

好,那么这样的话能够看到咱们这张表就已经创建出来了。

然后接下来我们来创建一个Mainframe工程,对吧?

然后作为这个什么呢?

作为看着的客户端。

我们连接到咱们这个看着。

现在再来回过头来再来看一下它这个地方。

看一下这个图。

你看我们上面这个呢其实是咱们这个看着服务,对吧?

看着服务,看着Server。

好,并且呢我们现在已经启动完了。

通过Docker这种方式已经跑起来了,对吧?

然后呢我们现在要编写的这个Java工程啊,

它其实是作为一个看着的客户端。

然后来连接到什么呢?

我们这个看着Server,对吧?

然后呢一旦它这边能够从MySQL那边,

就会去到日志,对吧?

会去到这个Binary Log,

那么在我们客户端呢,

我就能通过这个监听的方式,

通过消息订阅的方式来订阅这个日志。

然后呢我们在这个地方呢来进行一个解析。

这样的话呢我们就知道在MySQL那边发生了什么事情,对吧?

具体它操作的数据是什么样子的,

都能够解析出来。

好,所以现在呢我们就需要来创建这个Mainframe工程。

咱们这个就叫什么呢?

看到-demo就可以。

好。

把这个工程名我们来复制一下。

然后呢我们来创建一下。

好,在这儿来create new project。

好,next。

来指定一下咱们这个坐标,cam-it-hema-candle-demo。

这个,然后直接点完成。

咱们需要注意的是什么呢?

我们需要在这个POM文件当中来导入一个坐标。

这个坐标的话呢,

大家来看叫做candle.client,对吧?

这是它的模块ID。

这一看,

是不是就是作为我们这个candle客户端来使用的。

所以我们要在当前我们创建的这个Mainframe工程当中,

能够连接到candle server,

就必须要来导入它这个坐标。

好,直接把它拷到这儿来就可以了。

你看cam的alibaba叫altar,对吧?

这个包下边给我们提供的这么一个坐标。

好,这样的话我们这个坐标呢就已经导好了。

那接下来呢,我们需要来编写一段Java代码,对吧?

这段Java代码呢就是什么呢?

哎,通过,

就有点类似于我们以前最早讲的JDBC,对吧?

连接到MySQL数据库。

只不过我们这段代码呢,

是连接到什么呢?

连接到我们这个candle server,

然后呢来订阅它,来订阅它的消息,对吧?

一旦我们这个MySQL数据那边,

MySQL,比如说咱们这个student吧,

比如说咱们student这个表发生变化,对吧?

candle呢是不是就能监控到。

那这个时候呢,我们连接到candle,

连接到candle,

然后呢,通过订阅这种方式呢来解析它,

最终呢就能知道什么呢,

咱们刚才操作那个student,对吧?

你到底执行的是个insert操作,

还是个delete操作,

还是个update操作,

以及什么呢?

这个执行前后,

那么它具体的数据都是什么样子的。

比如说我执行一个update操作,对吧?

那么执行前的数据是什么样子的?

执行后的数据是什么样子的?

我们其实都能够解析出来。

当然这段Java代码的话呢,

不需要我们自己去写,

因为呢,我们这个地方呢,

咱们今天其实重点讲的是alt它的使用,

那么它这个使用起来,

是通过这个页面配置的方式来使用。

而这个canner呢,

是它的底层原理,对吧?

它其实基于canner来实现的。

所以说呢,这段代码呢,

我们不要求自己大家能够手写出来,

只要大概能读懂,

它是在做什么事情就可以了。

好,咱们呢,把整个代码复制过来,

然后呢,大概来读一下就可以了。

先把这个类创建出来,

叫做canner test。

在这下边来创建这个类。

连同包一块来创建一下。

comit黑码。

好,

然后呢,叫做canner。

好。

然后呢,我们整个把这个代码拷过来。

你看这个代码写起来,

其实还是挺繁琐。

Ctrl-C。

然后呢,拷过来。

好,咱们来看一下。

这个代码拷过来之后呢,

你像这个IP地址肯定是需要进行相应修改的,对吧?

这个IP指的是什么呢?

指的是我们这个canner server的IP。

所以在这来写一下。

这个指定什么呢?

指定我们这个,

我们这个canner server它的这个IP。

好。

但这个地址呢,需要改。

你看咱们当前使用的这个canner是什么呢?

是68.79.63.42,对吧?

指定的是这个地址。

这是我们当前这个canner它这个服务的地址。

然后呢,这个destination对应的这个example,

这个呢,应该叫做目标。

这个呢,应该叫做目标。

对吧?

这个地方呢,大家来看啊。

这个地方你就不要改了。

大家还记得吧,我们前面在进行这个canner配置的时候呢,

咱们来看一下。

我们当时是不是修改了这么一个配置文件,对吧?

这个配置文件呢,是在这个example下边,对吧?

example下边。

相当于呢,我们当前这个目标就是它。

好。

所以这一段Java代码就不要改了。

好。

然后接下来呢,咱们是不是创建一个连接对象啊?

叫做什么呢?

叫做canner connector,对吧?

然后呢,指定IP。

好。

这个IP呢,改对。

然后接下来呢,就是端口,对吧?

端口。

大家还记得吧,我们当时启动canner的时候呢,

是不是使用的就是这个5个1,这个端口。

然后呢,在这儿来指定destination。

这个地方就不用改了。

然后接下来呢,调用这个connect对象,它的connect方法,对吧?

这样进行连接。

这就相当于什么呢?

相当于我们这个客户端就连接上了什么呢?

连接上了我们这个canner服务,对吧?

你看,这是一个canner client。

这是我们canner服务。

然后呢,建立一个连接。

好。

就是这个connect的这连接。

连接完之后呢,我们进行这个订阅。

你看,调用connect.subscribe,对吧?

进行订阅。

其实就是订阅谁呢?

订阅我们这个canner server它这边的消息。

因为我们不知道它什么时候有消息,对吧?

所以呢,你看这个地方呢,我们是写了一个vile true。

相当于一个死云环,对吧?

不断地去获取canner的消息。

不断地去获取。

咱们调用这个方法,get without ack,对吧?

调用这个方法。

调用这个方法来获取。

那么获取到的消息呢,它是封装成了这么一个message对象,对吧?

这么一个message对象。

然后在这个类里面呢,你看有消息的ID,对吧?

还有具体的消息的内容呢,它是封装在这个list的集合里面了。

封装在这个集合里面了,entries。

所以说一旦有消息的话呢,它就会获取到。

然后呢,获得消息的ID。

还有什么呢?

这个entries叫size。

这其实就是什么呢?

就是消息的数量,对吧?

消息的数量。

如果这个size等于0,或者ID等于-1,对吧?

说明没有获取到数据。

没有获取到数据呢,那我们就sleep。

重点看else这个分支,这说明有数据,对吧?

有数据的话呢,我们是不是就要进行数据的解析。

进行数据的解析。

好,通过这个message消息对象,getEntries,对吧?

然后呢,我们具体的数据呢,都是封装到这个list的集合里面去了。

所以接下来呢,需要来便利它,对吧?

便利它。

然后把每一个entry获取出来。

然后呢,这个entry里边呢,就可以通过entry.get什么?

entryType,对吧?

getEntryType。

这就是获得我们条目的类型。

然后接下来呢,再通过entry.getEntryType。

它如果等于什么呢?

RowData。

等于RowData。

说明什么呢?

我们获取的是这个,这次操作它是一个原始的数据操作。

说白了就是执行的我们增伤改查这一类的搜索,对吧?

那这个时候呢,我们就需要来获取它具体存储的内容。

怎么获取呢?

通过entry.getStoreValue。

它这个对象封装得非常深,对吧?

你看在entry里边,getStoreValue。

然后呢,通过我们这个rowData,

然后呢,通过我们这个rowChange,

然后调用它这个静态方法来进行解析,对吧?

这不是passFrom吗?

然后呢,解析。

解析完之后呢,通过这个rowChange.get什么?

EventType。

这是不是叫做事件类型,对吧?

那么就能知道我们刚才执行的这个日志,

它记录的这个事件类型是哪一种,

到底是insert还是delete还是update。

这是事件的类型。

那么这样就一步一步能够解析出来了。

然后光知道事件类型还不行。

我还想知道,

你操作的数据,对吧?

你操作的数据,

比方说你insert了一条数据,

那你插入的这条数据具体是什么,对吧?

具体值是什么?

那么就需要通过这个什么呢?

还是通过这个rowChange,对吧?

getRowDataAsList。

然后呢,它就,

其实得到的是一个集合,

然后呢,我们便利这个集合。

你看,它这个返回值其实是一个集合。

然后呢,我们在这来便利它,

就是放运环,便利。

然后rowData。

那么有一些数据呢,

它是有改变前的,

有改变后的。

比如说我们执行的是update,对吧?

那你update之前的数据是什么样子的?

update之后的数据是什么样子的?

我都可以获取到。

你看,这不是getBeforeColumnList,对吧?

然后呢,这个是getAfterColumnList。

这是改变后的,改变前的,

都能够获取到。

所以你可以看到,

咱们这个代码呢,

写起来比较繁琐,

但是呢,都能够一步一步解析,对吧?

从最原始的这个message这个地方,

是不是获取信息,对吧?

消息。

然后呢,

从这个消息,

对象一步一步解析。

最终呢,就能把我们真正执行circle,对吧?

改变前的数据,改变后的数据呢,

都能够解析出来。

最终呢,我们调用这个ack这个方法。

这表示什么呢?

消息确认,对吧?

其实就是我们这个作为客户端,

我们发一个消息,

就是告诉我们这个counter server,

就是这条消息呢,

我已经成功地接收了,对吧?

这是一个消息确认机制。

以前我们使用这个什么呢?

使用相应的这个,

比如说消息队列,对吧?

经常会有这样的,

经常会有这样的,

就是我们消费完这个消息之后,

可以手动去应答一下。

好,这是咱们把这个代码呢,

大概读一下。

一会儿呢,我们来执行一下这个man法,

咱们来测试一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **Canal** 数据库增量同步工具的入门教程。讲师通过一个具体的 Java 项目 `canal-demo`，演示了如何在 MySQL 数据库中创建测试表，如何在 IntelliJ IDEA 中配置并编写 Java 代码，使用 Canal 客户端库来监听并获取数据库的 Binlog 信息。核心内容包括：创建数据库和表、添加 Canal 依赖、编写监听程序、解析 Binlog 事件并打印变更数据。整个过程旨在帮助开发者快速上手 Canal 的基本使用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程开始，讲师在 Typora 文档中展示课程大纲，当前章节为 “1.6 简单使用”。
*   **00:00:05 - 00:00:15**：讲师在文档中展示需要在数据库中创建的表结构 `student`。
*   **00:00:15 - 00:00:25**：讲师展示在 Maven 项目的 `pom.xml` 文件中需要添加的 Canal 客户端依赖。
*   **00:00:25 - 00:00:35**：讲师切换到 IntelliJ IDEA，演示如何新建或打开项目 `canal-demo`。
*   **00:00:35 - 00:00:45**：讲师在 IDEA 中打开项目，并展示 `CanalTest.java` 文件的初始代码结构。
*   **00:00:45 - 00:01:00**：讲师逐步讲解并编写 Java 代码，包括创建 `CanalConnector` 对象、连接、订阅和循环获取 Binlog 消息。
*   **00:01:00 - 00:01:20**：讲师讲解如何判断获取到的消息是否为空，并在无数据时进行等待。
*   **00:01:20 - 00:01:40**：讲师讲解如何解析 Binlog 消息，获取事件类型（`EntryType`）并打印。
*   **00:01:40 - 00:02:00**：讲师讲解如何处理 `ROWDATA` 类型的事件，解析并打印变更前后的数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：显示了本章的结构，包括“1.6 简单使用”、“2. Otter概述”、“3. Otter安装配置”等。
*   **数据库建表语句**：
    ```sql
    CREATE TABLE `student` (
        `id` varchar(20) NOT NULL,
        `name` varchar(50) DEFAULT NULL,
        `age` int(11) DEFAULT NULL,
        `sex` varchar(5) DEFAULT NULL,
        `city` varchar(20) DEFAULT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```

#### 代码内容

*   **Maven 依赖**：
    ```xml
    <dependency>
        <groupId>com.alibaba.otter</groupId>
        <artifactId>canal.client</artifactId>
        <version>1.1.4</version>
    </dependency>
    ```

*   **Java 代码 `CanalTest.java`**：
    ```java
    import com.alibaba.otter.canal.client.CanalConnector;
    import com.alibaba.otter.canal.client.CanalConnectors;
    import com.alibaba.otter.canal.protocol.CanalEntry;
    import java.net.InetSocketAddress;
    import java.util.List;
    import java.util.concurrent.TimeUnit;

    public class CanalTest {
        public static void main(String[] args) {
            String ip = "39.98.107.235"; // 指定canal server的ip
            String destination = "example";
            // 创建连接对象
            CanalConnector canalConnector = CanalConnectors.newSingleConnector(
                    new InetSocketAddress(ip, 11111), destination, "", "");
            // 进行连接
            canalConnector.connect();
            // 进行订阅
            canalConnector.subscribe();
            int batchSize = 5 * 1024;
            // 使用死循环不断的获取canal信息
            while (true) {
                // 获取Message对象
                Message message = canalConnector.getWithoutAck(batchSize);
                long id = message.getId();
                int size = message.getEntries().size();
                System.out.println("当前监控到的binlog消息数量是：" + size);
                // 判断是否有数据
                if (id == -1 || size == 0) {
                    // 如果没有数据，等待1秒
                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } else {
                    // 如果有数据，进行数据解析
                    List<Entry> entries = message.getEntries();
                    // 遍历获取到的Entry集合
                    for (Entry entry : entries) {
                        System.out.println("当前的二进制日志的条目（entry）类型是：" + entry.getEntryType());
                        // 如果属于原始数据ROWDATA，进行打印内容
                        if (entry.getEntryType() == CanalEntry.EntryType.ROWDATA) {
                            try {
                                // 获取存储的内容
                                RowChange rowChange = RowChange.parseFrom(entry.getStoreValue());
                                // 打印事件的类型，增删改哪种 eventType
                                System.out.println("事件类型是：" + rowChange.getEventType());
                                // 打印改变的内容（增量数据）
                                for (RowChange.RowData rowData : rowChange.getRowDatasList()) {
                                    System.out.println("改变后的数据：" + rowData.getAfterColumnsList());
                                }
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                        }
                    }
                    // 消息确认已经处理了
                    canalConnector.ack(id);
                }
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与依赖配置**
    *   讲师首先在 Typora 文档中展示了课程大纲，明确了本节内容。
    *   接着，讲师在文档中展示了一个用于测试的 MySQL 表结构 `student`，并强调需要在数据库中创建该表。
    *   随后，讲师在 IDEA 中打开项目，并在 `pom.xml` 文件中添加了 Canal 客户端的 Maven 依赖，版本号为 `1.1.4`。

*   **场景二：编写监听程序**
    *   讲师在 IDEA 中打开 `CanalTest.java` 文件，开始编写 Java 代码。
    *   讲师首先定义了连接 Canal Server 的 IP 地址和 destination 名称。
    *   讲师使用 `CanalConnectors.newSingleConnector()` 方法创建了 `CanalConnector` 对象，并调用 `connect()` 和 `subscribe()` 方法建立连接和订阅。
    *   讲师设置了一个 `batchSize` 变量，用于控制每次获取 Binlog 消息的大小。
    *   讲师使用 `while (true)` 循环，通过 `getWithoutAck(batchSize)` 方法持续获取 Binlog 消息。

*   **场景三：解析与处理 Binlog 事件**
    *   讲师通过 `message.getId()` 和 `message.getEntries().size()` 获取消息的 ID 和包含的条目数量。
    *   讲师编写了判断逻辑：如果 ID 为 -1 或者 size 为 0，表示没有数据，程序会调用 `TimeUnit.SECONDS.sleep(1)` 等待 1 秒。
    *   如果有数据，讲师通过 `message.getEntries()` 获取 `Entry` 对象的列表。
    *   讲师遍历 `Entry` 列表，打印每个条目的类型。
    *   讲师使用 `if (entry.getEntryType() == CanalEntry.EntryType.ROWDATA)` 判断是否为数据变更事件。
    *   在 `ROWDATA` 事件中，讲师使用 `RowChange.parseFrom(entry.getStoreValue())` 解析存储的值，并打印事件类型和变更后的数据。
    *   最后，讲师调用 `canalConnector.ack(id)` 方法确认消息已处理，以便 Canal Server 可以继续推送新的数据。

整个演示过程逻辑清晰，步骤完整，通过实际代码展示了 Canal 的基本使用方法。
