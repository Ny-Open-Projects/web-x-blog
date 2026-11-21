# 04-基础数据微服务开发准备（SpringBoot配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

刚才呢

我们已经把这个基础数据微服务啊

所涉及到的这些数据模型

对吧

所要操作的这些表

一共是14个表啊

整个过了一遍

好

然后接下来呢

我们来看下一个小节呢

就是关于我们基础数据微服务啊

开发之前的一些准备工作

开发准备

那么因为后边呢

我们马上就要开发这个货物类型管理

对吧

相关的这些接口开发了

那么在开发之前呢

有一些环境啊

需要提前准备好

比如说我们配置文件

对吧

先配置好

然后呢

服务的启动类

还有配置类等等

这些呢

需要都准备好

然后才能进入我们真正的业务开发

好

那么首先呢

我们来看啊

第一个呢

是Spring Boot的配置文件

好

这个配置文件呢

其实在我们导入的这个初始工程里边呢

我们其实提前都已经准备好了

所以我们这一步呢

其实是可以略过去的

比如说我们导入的初始工程里边

这些配置呢

其实都已经有了

咱们大概来浏览一下就可以了

看看都是配置的

哪些项啊

首先呢

我们项目启动的时候呢

首先要加载的是这个

bootstrap.yml

对吧

这是根据规则来指定的

那么它会加载这个文件

然后这里面呢

配置的是我们server

他们开的对吧

配置了他们开的这些参数

以及这个端口号

对吧

服务的端口号

但是这个呢

废弃了

你看是不是有一个横线呢

所以这个的话呢

你给它去掉也可以啊

然后呢

接下来配置的

Spring Application.name

这个是配置的是我们当前这个服务

它的应用名

对吧

每一个服务呢

都有一个应用名称

那么就是由这儿来指定的

后边呢

这是指定我们当前所处的环境

对吧

环境的话呢

通常呢

会有这么几种环境啊

什么dev啊

test啊

prod啊

对吧

dev就是development

其实就是开发环境

对吧

然后test呢

就是测试环境

然后prod呢

其实就是product

也就是生产环境

当前的是dev

这就意味着什么呢

我们除了要加载这个配置文件之外

它是不是还要加载

一个

这个什么

bootstrap-dev.yml

因为我们现在配置的是这个

所以根据规则呢

它还会加载这个文件

然后呢

在这个文件里边呢

咱们是不是配置的什么呢

springcloud-nucleus

对吧

那么配置的这些参数

然后再往下呢

是不是有jackson

有什么server-late

等等这些

然后呢

我们现在重点来看一下什么呢

就是这些地方

大家可以来看一下

这些地方

你看我们是不是写了一个

dollar花块号

对吧

这个呢

其实就是

我们并没有把具体

所设置的值

是不是写在这儿

而是通过这么一种语法

对吧

类似于一儿表达师的一种写法

它其实就是动态的来取值

对吧

那么它动态的从哪去取值呢

那么很明显

它肯定是从哪呢

从我们这个NUCLEUS配置中心

是不是需要去取值

所以说呢

我们现在来看一下

因为我们前面在第一章当中

已经完成了什么呢

把咱们这个NUCLEUS

是不是已经搭建好

并且呢

把我们那些配置文件呢

是不是已经

倒进来了

所以现在呢

我们来看一下

好

这儿呢

因为前面已经登录过了

所以它是有缓存的

那么如果说你时间长了

不登录的话呢

那么它可能需要你重新登录一下

好

然后呢

我们进来

进来之后呢

进到我们当前这个

Namespace

对吧

这个命名空间

下边呢

就有我们这些配置文件

那么具体到我们当前

这个什么呢

PD-Base

咱们这个微服务的话

它会加在哪个配置文件呢

那么很明显

它是有

有我们这个Application Name

对吧

应用名

以及我们这个

这个地方

这个环境

是不是加一块

来构成我们要读取的

那个配置文件的名称

那是不是应该就是

PD-Base-DV.yml

因为我们在这个地方

是配置的

咱们这个要读取文件的后缀

对吧

是这种形式的

所以说呢

它就会读取到

这个

PD-Base-DV

对吧

那么它就会读取到这个文件

然后在这个文件里边

大家来看一下

我们来看一下

比如说我们就拿刚才这个地方来说

我这个Jackson TimeZone

对吧

这是Jackson它的一个时区

对吧

设置成时区

时间格式化的时候会用到

然后呢

具体这个值

它会从我们Nux的这个配置里边

去取

取哪个呢

Spring.Jackson.TimeZone

你看啊

这里面肯定也有

Spring.Jackson.TimeZone

那这样的话呢

它其实就会把这个值取到

对吧

然后呢

对应的相当于就放在这个位置了

只不过这个过程呢

是一个动态的过程

它需要先从这边

是不是来取这个值

然后呢

把它设置给我们这个属性

设置给这个属性

那么同理

其他的也都是类似的

也都是这种玩法

比如说还有这儿

是不是还有一个

Spring.Jackson.DataFormat

你看Spring.Jackson.DataFormat

具体的这个值

是不是就是这种

它其实就是把这个值取到

读取到

然后呢

付给我们当前这个属性

因为我们说

虽然说表面上来

看的话

这些其实是在配置文件里面

配置的一些项

最终呢

它其实都会什么呢

都会封装成相应的一些

这个配置属性类

其实就是把这个值

付给这个属性了

付给这个属性

最终呢

把我们读取到的这个值呢

把它封装成这么一个对象

叫做什么呢

Jackson Properties

对吧

由这个对象来封装

所以最终呢

其实都是一些Java代码

那么其他的也都是类似的

也都是类似的

然后下边是不是配置的是

一些数据源呢

对吧

是一些数据源的这些配置

像type啊

什么driver class name

URL

username等等

好

密码等等这些

当然这些呢

也都是动态来取值

同样的也是从我们下边

这些地方是不是来取的值

大家可以看到

username password

然后这些

那么都是在这配置的

最终呢

都是读取过来

然后付给相应的这些属性

就可以了

整个呢

这都是关于数据源的配置

那么数据源的配置比较多

对吧

一直有这么多

下面这块呢

就是我们

这个mybattiesplus的一些配置

比如说我配置这个myperlocation

对吧

来指定我们这个myper应设文件

对吧

它的位置

那么具体在什么位置呢

你看它也是取值

mybattiesplus.myperlocations

那么来看一下

我们这边是怎么配置的

myperlocations

配置的是这个

classpass星

对吧

下面myper

也就是说我们后边

这个配置文件呢

都会放在这个myper目录下边

对吧

然后当下边呢

也可能会细分其他的目录

最后呢

是以这个文件名呢

是以这个chaml这种形式的

也就是说我们这些配置文件呢

应设文件都会放在这个myper下边

mypattern的应设文件都会放在myper

这个目录下边

然后呢

这个是不是进行这个扫描

对吧

扫描完之后呢

扫描实体

最终呢

生成我们的这个什么呢

生成我们的这个

应该叫做别名

对吧

alias

然后globalconfig

dbconfig等等

整个这块呢

这属于我们

mybattiesplus的配置

大概就是这些

你看

这是咱们这个配置

大概读一遍啊

就可以了

也说我们这个项目

它开发的特点是什么呢

就是啊

在我们这个项目内部

这个配置文件

绝大部分的配置项

全都是使用这种什么的

动态读取的方式

对吧

那么具体我们要修改

某个值的时候呢

我们应该修改的

就是咱们这个什么呢

配置中间的

这些配置项

那么这个有什么好处呢

因为我们这个改完之后啊

你直接重新点发布就可以了

对吧

重新发布就可以了

我们这个代码呢

是不用做任何修改的

这样的话呢

我们这个代码相当于

它的这个可维护性会更强

对吧

那么我们直接改的是

配置中心的

这些配置

具体这些配置项呢

全都是从我们配置中心

动态读取

这是关于咱们第一部分啊

配置文件

因为我们这些配置项呢

我们都用了

我们的配置中心

我们的配置项呢

我们的配置项呢

我们的配置项呢

这个导入的初始工程里边呢

都已经提供好了

所以我们整个啊

就大概过一下

看看它都配置了

哪些内容就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”第二章“基础数据微服务开发”的技术讲解，主要聚焦于 Spring Boot 项目的配置文件（`bootstrap.yml` 和 `bootstrap-dev.yml`）的编写与管理，以及如何通过 Nacos 配置中心进行动态配置管理。讲师通过 IntelliJ IDEA 编辑器展示代码，并在 Nacos 控制台演示如何创建和发布配置，旨在为后续服务的启动和运行打下基础。课程内容涵盖了服务器参数、应用名称、环境配置、数据源配置、MyBatis-Plus 配置等多个方面，强调了配置文件的分层管理和动态化。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 课程开场，展示项目结构和当前章节“2.1 SpringBoot配置文件”。
*   **00:03 - 00:08**: 讲解 `bootstrap.yml` 文件，重点是 `server` 和 `spring.application.name` 配置。
*   **00:08 - 00:12**: 展示 `bootstrap-dev.yml` 文件，介绍其用于开发环境的配置，包含 Nacos 的 `discovery` 和 `config` 配置。
*   **00:12 - 00:16**: 在 IntelliJ IDEA 中编辑 `bootstrap-dev.yml`，展示 `spring.cloud.nacos` 配置块。
*   **00:16 - 00:20**: 讲解 `bootstrap-dev.yml` 中的 `jackson` 和 `servlet` 配置项。
*   **00:20 - 00:24**: 展示 `datasource` 配置块，重点是 `druid` 数据源的配置。
*   **00:24 - 00:28**: 继续展示 `druid` 数据源的详细配置项，如 `max-active`, `min-idle` 等。
*   **00:28 - 00:32**: 展示 `mybatis-plus` 配置块，包括 `mapper-locations` 和 `typeAliasesPackage`。
*   **00:32 - 00:36**: 展示 `mybatis-plus` 的 `global-config` 和 `configuration` 配置项。
*   **00:36 - 00:40**: 切换到 PPT，展示章节“2.2 服务启动类”，并展示对应的 Java 代码。
*   **00:40 - 00:44**: 在 Nacos 控制台创建配置，展示 `Data ID` 和 `Group` 的设置。
*   **00:44 - 00:48**: 在 Nacos 控制台编辑配置，展示 `bootstrap-dev.yml` 的内容，并进行发布。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **章节标题**: “2. 基础数据微服务开发准备” -> “2.1 SpringBoot配置文件”。
*   **章节标题**: “2.2 服务启动类”。
*   **PPT 文字**: “海量一手资源：666java.com”。

#### 代码内容

*   **`bootstrap.yml` 关键配置**:
    ```yaml
    server:
      # 服务器相关配置
      uri-encoding: UTF-8
      max-threads: 1000
      min-spare-threads: 30
      port: 8185
      connection-timeout: 50000ms
      # servlet:
      #   context-path: /pd-base

    spring:
      application:
        name: pd-base
        # 环境 dev/test/prod
        profiles:
          active: dev
        main:
          allow-bean-definition-overriding: true
    ```

*   **`bootstrap-dev.yml` 关键配置**:
    ```yaml
    spring:
      cloud:
        nacos:
          discovery:
            server-addr: 111.231.76.210:58848
            group: pinda-tms
            namespace: c035ed13-9d51-4a81-9573-9162320515cc
          config:
            server-addr: 111.231.76.210:58848
            file-extension: yaml
            group: pinda-tms
            namespace: c035ed13-9d51-4a81-9573-9162320515cc

    # Jackson时间格式化
    jackson:
      time-zone: ${spring.jackson.time-zone}
      date-format: ${spring.jackson.date-format}

    servlet:
      multipart:
        max-file-size: ${spring.servlet.multipart.max-file-size}
        max-request-size: ${spring.servlet.multipart.max-request-size}
        enabled: ${spring.servlet.multipart.enabled}

    datasource:
      type: ${spring.datasource.druid.type}
      driver-class-name: ${spring.datasource.druid.driver-class-name}
      url: ${spring.datasource.druid.url}
      username: ${spring.datasource.druid.username}
      password: ${spring.datasource.druid.password}
      initial-size: ${spring.datasource.druid.initial-size}
      max-active: ${spring.datasource.druid.max-active}
      min-idle: ${spring.datasource.druid.min-idle}
      max-wait: ${spring.datasource.druid.max-wait}
      pool-prepared-statements: ${spring.datasource.druid.pool-prepared-statements}
      max-pool-prepared-statement-per-connection-size: ${spring.datasource.druid.max-pool-prepared-statement-per-connection-size}
      time-between-eviction-runs-millis: ${spring.datasource.druid.time-between-eviction-runs-millis}
      min-evictable-idle-time-millis: ${spring.datasource.druid.min-evictable-idle-time-millis}
      test-while-borrow: ${spring.datasource.druid.test-while-borrow}
      test-on-borrow: ${spring.datasource.druid.test-on-borrow}
      test-on-return: ${spring.datasource.druid.test-on-return}

    mybatis-plus:
      mapper-locations: ${mybatis-plus.mapper-locations}
      typeAliasesPackage: ${mybatis-plus.typeAliasesPackage}
      global-config:
        db-config:
          # 主键类型 AUTO:"数据库ID自增", INPUT:"用户输入ID", ID_WORKER:"全局唯一ID (数字类型唯一ID)", UUID:"全局唯一ID UUID"
          id-type: ${mybatis-plus.global-config.db-config.id-type}
          field-strategy: ${mybatis-plus.global-config.db-config.field-strategy}
          column-underline: ${mybatis-plus.global-config.db-config.column-underline}
          logic-delete-value: ${mybatis-plus.global-config.db-config.logic-delete-value}
          logic-not-delete-value: ${mybatis-plus.global-config.db-config.logic-not-delete-value}
          banner: ${mybatis-plus.global-config.banner}
      configuration:
        map-underscore-to-camel-case: ${mybatis-plus.configuration.map-underscore-to-camel-case}
        cache-enabled: ${mybatis-plus.configuration.cache-enabled}
        call-setters-on-nulls: ${mybatis-plus.configuration.call-setters-on-nulls}
        jdbc-type-for-null: ${mybatis-plus.configuration.jdbc-type-for-null}
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
    ```

#### 图表/界面

*   **Nacos 配置管理界面**: 展示了 Nacos 控制台的“配置管理”页面，用于创建和管理配置。
*   **Nacos 配置编辑界面**: 展示了 Nacos 控制台的配置编辑页面，用于编辑 `bootstrap-dev.yml` 文件内容。

---

### 4) 关键场景与演示描述

1.  **场景一：配置文件结构与内容展示** (00:00 - 00:08)
    *   讲师在 IntelliJ IDEA 中打开 `bootstrap.yml` 文件，高亮显示 `spring.application.name` 和 `profiles.active` 配置项，解释其作用。
    *   随后，讲师切换到 `bootstrap-dev.yml` 文件，展示其用于开发环境的配置，包括 Nacos 的服务发现和配置管理相关设置。

2.  **场景二：Nacos 配置中心操作** (00:40 - 00:48)
    *   讲师在浏览器中打开 Nacos 控制台，进入“配置管理”页面。
    *   讲师点击“+”号，创建一个新的配置，设置 `Data ID` 为 `bootstrap-dev.yml`，`Group` 为 `pinda-tms`。
    *   讲师在编辑页面粘贴 `bootstrap-dev.yml` 的内容，并点击“发布”按钮，完成配置的上传。

3.  **场景三：MyBatis-Plus 配置详解** (00:28 - 00:36)
    *   讲师在 `bootstrap-dev.yml` 文件中滚动到 `mybatis-plus`
