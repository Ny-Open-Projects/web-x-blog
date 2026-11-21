# 29-网关服务-Druid参数说明 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解德鲁伊的简要说明

那上面咱们是演示了如何去使用德鲁伊的数据盘

大家应该会有一个大概的了解和印象

这里咱们就再具体去扩展一下

了解它所具备的所有功能

以及监控台的使用

德鲁伊它是一个非常优秀的数据库连接池

也是阿里推出的一个开源组件

在功能性能和扩展性方面

都超过了其他数据库连接池

这个是它的一些优势

包括像目前市面上比较知名的一些开源连接池组件

像DBCP,C3PO,BONCP,PLATO,JBOX,DXS等等

并且德鲁伊在阿里巴巴部署了超过600个营用

也是经过了严苛的一个生产环境检验

具备了较强的可靠性

大家在生产环境当中可以去放心使用监控数据

当然大家一定要选择一个稳利的版本

德鲁伊监控台它包含数据员的配置信息

还有社口的监控

防火墙信息

URI监控

Session监控

以及视频一键监控

算是比较全面的一个监控台

最主要咱们是关注社口监控

对不对

它的数据员的一些配置信息

这个是我们最主要使用监控台的一个作用

当然大家如果有其他需要

使用其他的一些监控功能的话

能够起到帮助

这个也是可以的

好

再往下面咱们来看一下

德鲁伊监控参数

它具体有哪些配置

包括哪些功能

我们来了解一下

NIM

在这里面

我们重新看一下

NIM它是什么

它是数据员的一个名称

配置这个属性的意义是在于

如果说存在多个数据员

监控的时候

咱们就可以通过名字来区分

对不对

如果没有配置

它将会生成一个默认的格式

是以Data Source

然后以一个横杠

后面再根据System这样一个Hash Code

生成一个Hash的一个值

然后作为整个的名称

另外配置这个属性至少需要在1.0.5以上版本

才能起到作用

强行设置NIM

它会已经出错了

这个是NIM的一个作用

下面是URL

这个就不用做过多对数

对不对

因为连接数据库的URL

不管你哪个监控数据员

这个都必须要做对应的配置

下面就是连接数据库的用户名

对吧

还有它的密码

那么Job Class NIM

就是根据咱们连接的不同数据库

要采用了不同的驱动毛

在这里我们可以去做

就是对应的一个配置

这一项的话

我们可配可不配

如果说不配置

格鲁伊他会根据UI去自动识别DbType

然后去选择相应的Job Class NIM

咱们来看一下

这里面的话

有一套监控数据员的配置

对不对

Job Class NIM

如果说没有一些特殊要求的话

你不配置

他可以从这里面去识别出来

他可以看到是MySQL的

对不对

好

那么建议大家的话

还是按照我们的一个要求

叫他们配置一下

以防止自动识别

可能导致的一些监控性方面的问题

再往下面

咱们可以看一下

有Initial size

这个就是初始化建立的物理连接个数

初始化是发生显示调用init方法

然后或者是第一次get connection的时候

会进行了一个连接数的这种初始设定

Max active是最大的连接次数量

Max idea在这里面的话

它已经不再使用了

配置也没有具体的效果

Main idea是最小的连接次数量

有最大

对应也会有一个最小

对不对

那么Max wait是获取连接时的最大等待时间

比如说咱们要连接通讯

对不对

如果是由于网络阻塞

不可能一直等待在其中

所以要一个最大的等待时间

那么Pull prepared statements

在这里面它默认着是force

是否去缓存repealed statement

也就是说我们的ps的缓存

ps cache它对支持游标的数据库性能

会有提升巨大

比如说

我们的ps cache是否会被连接到

但是在买sql下面可以建议完毕

因为咱们一般不会去频繁对游标进行相应的操作

对不对

如果是在olig的连接当中

咱们可以将它去开启

Max pull for connection size

这个是要启用ps cache

我们再回到刚才

它是要启用ps cache

必须配置大于0

当大于0的时候

Pull prepared statements

是什么

就是说我们的ps cache

会自动触发并修改为chew

在diuid当中

不会存在olig下面ps cache

占用内存过多的问题

可以把这个数值配大一些

比如说设定为1

这些要根据实际需要去设定不同的参数值

那么validation query

这个是用来检测连接是否有效的circle

比如说咱们数据库有初始化10个连接

对不对

这些连接是不是可靠可用的

那就通过validation query的验证语句

去做一个调验

好

再往下面的话

是validation query timeout

但是timeout是什么意思

就是说我的验证查询的circle

它的最长的超时等待时间

对不对

如果因为网络阻塞

我不可能一直等待在这里

所以会有个超时时间的上限设定

那么test on borrow

这个是什么

申请连接时

执行validation query

检测连接是否有效

做了这个配置

它会降低性能

也就是说在你要去获取连接的时候

要去做一个follow

对不对

做获取连接的时候

它就要去做检测

检测是否有效

那么test on return

就在归还的时候

要去做这样一个连接验证

那么test the while idle

这个意思就是说

我们建议是配置为to

它的意思是在申请连接的时候

去做一个检测

如果说空闲时间大于time between

division

long time

long miles

在这里面的话

执行validation query

检测连接是否有效

也就是说你的空闲时间

比如说是设的是10秒

对不对

大于这个值的话

这个值如果是5毫秒

一个是10秒

一个是5秒

那么执行validation

检测连接

它就会去做对应的判断

那么下面的话

是time between

这个time between

它有两个含义

哪两个含义

第一个就是在destroy现成的时候

它会去检测这个连接

的时间间隔

如果连接空闲时间大于等于min

everytable

time miles

这个是关闭物理连接

test where idle

它的判断依据

详细的话

我们可以看test where idle

属性的说明

也在这里面

结合这个属性去做一个理解

再往下面的话

是num test for application

long

这个是不再使用了

在1.0.1.14以上的一个盘本的话

就不再推荐去使用

那么min everyable time miles

这个是连接保持空闲

而不被驱除的最长时间

connection initial circle是物理连接

初始化时候执行的circle

这些都是一些比较细节的阐述

在这里面的话

咱们可以采用它的默认词

然后exception的话

sort根据dbtype去自动识别

当数据库抛出一些不可恢复的异常时

就抛弃这个连接

filter它的是属性

内心的字符串

通过别名的方式

配置扩展插件

它这些插件的话

比如说监控统计用的

field state

日日用的

filter log4g

然后防社会注入的

这个

filter war

在这里面的话

我们也看到有对应的

filter

在这里面有多个的话

通过逗号拼接起来

那么proxy filter是什么意思

它的内心是一个list

如果是同时配置的filter

proxy filter

它就是一个组合关系

系统关系

也在这里面的话

配置起来

大家都可以去生效

那么咱们可以看到

在我们的数据库连接

配置当中

都会有一个详细的注解和说明

咱们也可以结合表格

参数的配置说明

去做一个详细的理解

在这一块就是对德鲁伊

它整个监控参数的一个配置的详细说明

以及德鲁伊监控注意员的进行介绍

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于 **Druid 数据库连接池** 的深入讲解，主要聚焦于其 **监控参数配置**。讲师首先回顾了 Druid 的基本概念和优势，随后详细介绍了其核心配置项，包括连接池的基本参数（如 `initialSize`, `maxActive`, `minIdle`）、连接有效性检测（`validationQuery`, `testOnBorrow`, `testOnReturn`, `testWhileIdle`）、连接回收策略（`timeBetweenEvictionRunsMillis`, `numTestsPerEvictionRun`, `minEvictableIdleTimeMillis`）以及监控和安全相关的配置（`filters`, `proxyFilters`, `connectionProperties`）。课程通过在 IntelliJ IDEA 中展示 `bootstrap.yml` 配置文件，将理论知识与实际应用相结合，旨在帮助开发者掌握如何正确、高效地配置和监控 Druid 连接池，以提升应用的性能和稳定性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，讲师在 Typora 中展示文档大纲，引出本节内容为“3. 实现”下的“3.1 Druid简介说明”。
*   **00:15 - 00:40**: 讲解 Druid 的基本概念，强调其在功能、性能和扩展性方面的优势，并提及它在阿里巴巴的广泛应用和高可靠性。
*   **00:40 - 01:10**: 进入“3.2 Druid监控参数配置说明”章节，开始详细介绍配置项。首先展示 `name`, `url`, `username`, `password`, `driverClassName` 等基础连接信息配置。
*   **01:10 - 01:40**: 继续讲解连接池的核心参数，如 `initialSize`, `maxActive`, `minIdle`, `maxWait`，并解释其作用。
*   **01:40 - 02:10**: 讲解与连接池性能和安全相关的配置，如 `poolPreparedStatements`, `maxPoolPreparedStatementPerConnectionSize`, `validationQuery`, `validationQueryTimeout`。
*   **02:10 - 02:40**: 重点讲解连接回收和检测相关的配置，包括 `testOnBorrow`, `testOnReturn`, `testWhileIdle`, `timeBetweenEvictionRunsMillis`, `numTestsPerEvictionRun`, `minEvictableIdleTimeMillis`，并解释其工作原理和最佳实践。
*   **02:40 - 03:00**: 讲解监控和安全过滤器配置，如 `filters` 和 `proxyFilters`，并说明其作用。
*   **03:00 - 03:20**: 展示 IntelliJ IDEA 中的 `bootstrap.yml` 配置文件，将前面讲解的配置项应用到实际项目中，包括 `minEvictableIdleTimeMillis`, `validationQuery`, `testWhileIdle`, `filters` 等。
*   **03:20 - 03:30**: 课程结束，讲师总结了本节内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3. 实现”、“3.1 Druid简介说明”、“3.2 Druid监控参数配置说明”。
    *   **Druid 优势**: “在功能、性能、扩展性方面，都超过其他数据库连接池，包括 DBCP、C3PO、BoneCP、Proxool、jBoss DataSource”。
    *   **Druid 监控台**: “包含数据源配置信息、SQL监控、防火墙信息、URI监控、Session监控和Spring 监控等”。
    *   **配置项表格**: 详细列出了 Druid 的各项配置参数，包括 `name`, `url`, `username`, `password`, `driverClassName`, `initialSize`, `maxActive`, `minIdle`, `maxWait`, `poolPreparedStatements`, `maxPoolPreparedStatementPerConnectionSize`, `validationQuery`, `validationQueryTimeout`, `testOnBorrow`, `testOnReturn`, `testWhileIdle`, `timeBetweenEvictionRunsMillis`, `numTestsPerEvictionRun`, `minEvictableIdleTimeMillis`, `connectionInitSqls`, `exceptionSorter`, `filters`, `proxyFilters` 等，并附有其默认值和详细说明。

*   **代码 (配置文件)**:
    *   **文件路径**: `bulls-stock / bulls-stock-user / main / resources / bootstrap.yml`
    *   **关键配置内容**:
        ```yaml
        # Druid连接池配置
        druid:
          # 最小空闲连接数
          minEvictableIdleTimeMillis: 300000
          # 验证SQL
          validationQuery: SELECT 1 FROM DUAL
          # 从连接池中获取连接时检测连接有效性
          testWhileIdle: true
          # 从连接池中归还连接时检测连接有效性
          testOnBorrow: false
          # 归还连接时检测连接有效性
          testOnReturn: false
          # 是否缓存PreparedStatement
          poolPreparedStatements: true
          # 每个连接缓存PreparedStatement的最大数量
          maxPoolPreparedStatementPerConnectionSize: 20
          # 连接池监控过滤器
          filters: stat, wall, log4j
          # 连接池属性
          connectionProperties: druid.stat.mergeSql=true;druid.stat.slowSqlMillis=5000
          # Web监控过滤器
          web-stat-filter:
            enabled: true
            url-pattern: /*
            exclusions: "*.js,*.gif,*.jpg,*.bmp,*.png,*.css,*.ico,/druid/*"
          # 配置Druid的StatViewServlet
          stat-view-servlet:
            enabled: true
            # 配置监控页面访问权限
            # url-pattern: /druid/*
            # # 配置监控页面访问权限
            # # auth-interceptor: com.bulls.stock.user.config.DruidAuthInterceptor
        ```

---

### 4) 关键场景与演示描述

*   **场景一：Druid 简介与监控台介绍 (00:00-00:40)**
    *   讲师在 Typora 中展示文档大纲，鼠标悬停在“3.1 Druid简介说明”上。
    *   讲师朗读文档内容，介绍 Druid 是一个非常优秀的数据库连接池，功能、性能和扩展性都超过其他连接池，并强调其在阿里巴巴的广泛应用和高可靠性。
    *   讲师提到 Druid 监控台包含多种监控信息，为后续配置做铺垫。

*   **场景二：Druid 监控参数配置详解 (00:40-03:20)**
    *   讲师在 Typora 中滚动查看“3.2 Druid监控参数配置说明”章节。
    *   讲师逐行讲解配置项，如 `name`、`url`、`username`、`password` 等，并解释其作用和默认值。
    *   讲师重点讲解了连接池的核心参数，如 `initialSize`、`maxActive`、`minIdle`、`maxWait`，并解释了它们对连接池性能的影响。
    *   讲师讲解了连接有效性检测相关的配置，如 `testOnBorrow`、`testOnReturn`、`testWhileIdle`，并解释了它们的含义和最佳实践。
    *   讲师讲解了连接回收和检测相关的配置，如 `timeBetweenEvictionRunsMillis`、`numTestsPerEvictionRun`、`minEvictableIdleTimeMillis`，并解释了它们的工作原理。
    *   讲师讲解了监控和安全过滤器配置，如 `filters` 和 `proxyFilters`，并说明了它们的作用。
    *   讲师在 IntelliJ IDEA 中打开 `bootstrap.yml` 文件，将前面讲解的配置项应用到实际项目中，并高亮显示了关键配置。

*   **场景三：配置文件演示 (03:00-03:20)**
    *   讲师在 IntelliJ IDEA 中展示 `bootstrap.yml` 文件。
    *   讲师高亮显示了 `minEvictableIdleTimeMillis`, `validationQuery`, `testWhileIdle`, `filters` 等配置项，并解释了它们的作用。
    *   讲师解释了 `filters: stat, wall, log4j` 的含义，其中 `stat` 用于监控统计，`wall` 用于防火墙，`log4j` 用于日志记录。
    *   讲师解释了 `connectionProperties` 的作用，如 `druid.stat.mergeSql=true` 用于合并 SQL 语句，`druid.stat.slowSqlMillis=5000` 用于设置慢 SQL 的阈值。
    *   讲师解释了 `web-stat-filter` 和 `stat-view-servlet` 的作用，用于开启 Web 监控功能。
