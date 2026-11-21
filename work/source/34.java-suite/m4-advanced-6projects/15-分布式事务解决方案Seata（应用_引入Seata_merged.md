# 15-分布式事务解决方案Seata（应用_引入Seata — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢继续来看我们Sita的应用

前面呢我们是已经完成了咱们Sita Server的启动对吧

那么我们是基于Docker镜像这种方式把它跑起来的

同时呢我们也提供了两个配置文件对吧

一个就是我们这个registry.config

还有一个是file.config

然后这两个文件呢全都是拷到了哪呢

拷到了我们这个Docker容器当中对吧

好并且呢重启服务

我们也可以看到服务启动之后呢

它已经注册到我们这个Nux

这个服务列表里面来了

好那接下来呢我们就可以来看啊

就是什么呢

这是服务端已经搞定了

剩下的就是在我们的程序当中如何来配置Sita

相当于什么呢

我们的程序呢需要作为Sita的客户端

跟咱们Sita Server呢来进行交互啊

好那么这样的话呢

我们就需要在咱们这个POM文件当中

来引入Sita的这个应用

就是这个坐标

那么因为我们当前这个项目里边呢

有很多微服务呢都会使用到Sita对吧

那如果说每一个微服务呢都去演一份的话呢

这样就太麻烦了

也不好统一管理这个版本

那怎么办呢

我们是在这个最最上层对吧

这个副工程这个地方

你看就是我们品达TMS Java这个下面呢

咱们来统一锁定Sita的版本

来看一下

是在这个地方对吧

在这个地方来锁定Sita的版本

注意啊

我们现在这个配置呢

是不是配置在Dependency Management的这个标签里边

相当于是什么呢

这个架包呢

其实不会被我们这些微服务是不是去继承

也就是说它只是锁定了版本

具体哪个微服务会使用呢

咱们刚才也提到了

那么我们下边可能好多微服务都会使用到

那怎么做呢

我们又在这个Common里边

因为其他的模块呢

都依赖这个Common对吧

所以我们在这个Common里边呢

再次引入一下Sita

而这次引入的话呢

就不用指定什么呢

版本号了

就是因为我们在它的上一层

这个品达TMS Java这里边

已经锁定了这个版本号是1.2对吧

然后呢

这个地方呢

我们直接来通过Group ID

还有Artifact ID就可以了

好

这样把它锁定

你看在我们这个Common里边

是不是来指定

但是还用到了一个什么呢

Open Faint

就是这个

因为我们后边呢

会使用到这个加包啊

所以说呢

我们提前把它引进来

你看在我们这个地方呢

也有Open Faint

然后呢

还需要注意是什么呢

因为我们引入了这个Sita

这个加包

那这样的话呢

如果我们某一个微服务啊

如果它没有使用到这个Sita的话呢

我们还需要给它排除掉

那么咱们这个地方

有这么多的微服务

对吧

那么具体哪个没有使用到呢

其实就是这个

就是我们这个Droid的这个服务

没有使用到Sita

因为它这里面的操作呢

所有的都是这种查询操作

对吧

所以说呢

它是不需要使用Sita的

所以说呢

我们需要干什么呢

就是在我们这个Droid的

PDD的

这个微服务的POM文件当中

然后呢

通过Exclusions这个标签呢

来排除Sita

就是我用不着它

我就必须要给它排除掉

因为什么呢

如果你不排除的话呢

它在启动的时候呢

就会去连接我们Sita Server

而我们当前呢

并没有给它去

在它配置文件里面

并没有去配置Sita相关的配置

那这样的话呢

它就会报错

所以说呢

我们这个架包呢

不能随便引

就是什么呢

你用到的时候

把它引进来

如果没有使用到的话

就必须把它排除掉

而我刚才已经说清楚了

我们这里边呢

只有这个Droid的

没有使用到Sita

其他的都使用到了

所以说呢

我们单独把它给排除一下

就可以了

就是这个地方

你看

因为我们这个Droid的

你看它是不是

依赖了我们这个Common

PD Common

然后呢

我们Sita不想要

对吧

然后呢

再通过Exclusions

把它排除掉

就可以了

所以这个地方呢

我们也要注意一下

就是说有一些这个架包呢

它其实都是一个这样的特点

即使你不用它

对吧

你如果不用它的话

就必须要把它排掉

否则的话呢

它会报错

比如说我们上面这个

Spring Cloud

什么Starter

Nexus

什么Config等等这些

如果你用不着的话呢

也一定给它排除掉

因为什么呢

如果你不排除的话呢

它就需要去连接

什么呢

我们这个Nexus等等

所以说呢

它可能就会报错

那这样的话

我们把它排除掉就可以了

好

这是这一步啊

这是引入我们这个Sita的依赖

我们就先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第11章“分布式事务解决方案Seata”的教学内容，主要讲解如何在项目中集成和配置分布式事务框架Seata。讲师通过演示在 IntelliJ IDEA 中编辑 `pom.xml` 文件，逐步添加 Seata 和 OpenFeign 的依赖，并对 `pd-druid` 模块进行依赖排除，以避免与 Seata 冲突。同时，视频也展示了如何通过 Docker 复制配置文件到容器中，并重启服务以验证服务注册成功。整个过程旨在为后续的分布式事务功能开发打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，明确当前章节为“第11章 分布式事务解决方案Seata”。
*   **00:00:05 - 00:00:15**: 讲师在 Typora 中切换到“6. 引入seata依赖”部分，开始讲解如何在项目中引入 Seata。
*   **00:00:15 - 00:00:30**: 讲师切换到 IntelliJ IDEA，展示 `pinda-tms-java/pom.xml` 文件，重点讲解在 `<dependencyManagement>` 部分添加 Seata 的依赖坐标。
*   **00:00:30 - 00:00:45**: 讲师切换到 `pd-common/pom.xml` 文件，演示如何在该模块中引入 Seata 和 OpenFeign 的依赖。
*   **00:00:45 - 00:01:00**: 讲师在 `pd-druid/pom.xml` 文件中，演示如何为 `pd-druid` 模块添加依赖排除（exclusions），以排除其内部对 Seata 的依赖，避免冲突。
*   **00:01:00 - 00:01:15**: 讲师在 Typora 中切换到“7. 增加Seata配置”部分，准备讲解如何在各个项目中配置 Seata。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: “品达物流TMS项目” -> “第11章 TMS司机端、快递员端开发” -> “2. 分布式事务概述” -> “3. 分布式事务解决方案Seata” -> “3.4 应用” -> “6. 引入seata依赖”、“7. 增加Seata配置”。
    *   **关键说明**: “由于pd-druid不需要seata，所以需要排除掉”。
    *   **配置说明**: 在 `seata` 配置中，`application-id` 的值需要与 `vgroup-mapping` 下的参数保持一致。

*   **代码关键内容**:

    *   **在 `pinda-tms-java/pom.xml` 中添加 Seata 依赖**:
        ```xml
        <!-- 在 <dependencyManagement> 标签中配置 -->
        <dependency>
            <groupId>io.seata</groupId>
            <artifactId>seata-spring-boot-starter</artifactId>
            <version>1.2.0</version>
        </dependency>
        ```

    *   **在 `pd-common/pom.xml` 中引入 Seata 和 OpenFeign 依赖**:
        ```xml
        <dependency>
            <groupId>io.seata</groupId>
            <artifactId>seata-spring-boot-starter</artifactId>
            <version>1.2.0</version>
        </dependency>
        <dependency>
            <groupId>io.github.openfeign</groupId>
            <artifactId>feign-core</artifactId>
        </dependency>
        ```

    *   **在 `pd-druid/pom.xml` 中为 `pd-druid` 模块添加依赖排除**:
        ```xml
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
            <version>${spring-cloud-alibaba-version}</version>
        </dependency>
        <!-- 排除 seata -->
        <exclusion>
            <groupId>io.seata</groupId>
            <artifactId>seata-spring-boot-starter</artifactId>
        </exclusion>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：引入 Seata 依赖**
    *   **描述**: 讲师首先在 Typora 文档中定位到“6. 引入seata依赖”部分。随后，他切换到 IntelliJ IDEA，打开 `pinda-tms-java` 项目的 `pom.xml` 文件。他通过鼠标选中并高亮显示了在 `<dependencyManagement>` 标签内添加的 Seata 依赖坐标，并解释了其作用是为项目中的其他模块提供统一的依赖版本管理。

*   **场景二：在 `pd-common` 模块中引入依赖**
    *   **描述**: 讲师接着导航到 `pd-common` 模块的 `pom.xml` 文件。他高亮显示了在 `<dependencies>` 标签内添加的 Seata 和 OpenFeign 依赖。他解释了 `pd-common` 是一个公共模块，需要引入这些依赖以便其他服务模块可以正常使用。

*   **场景三：为 `pd-druid` 模块排除 Seata 依赖**
    *   **描述**: 讲师切换到 `pd-druid` 模块的 `pom.xml` 文件。他高亮显示了 `<exclusions>` 标签，并在其中添加了对 `io.seata:seata-spring-boot-starter` 的排除。他解释了 `pd-druid` 模块本身不使用 Seata，因此需要排除其内部可能引入的 Seata 依赖，以避免项目中出现依赖冲突。

*   **场景四：准备配置 Seata**
    *   **描述**: 讲师在 Typora 文档中切换到“7. 增加Seata配置”部分。他高亮显示了即将要配置的 Seata 配置项，包括 `enabled`, `application-id`, `tx-service-group`, `registry`, `file`, `name` 等参数，并强调了 `application-id` 的命名规范。这为接下来的配置步骤做好了准备。
