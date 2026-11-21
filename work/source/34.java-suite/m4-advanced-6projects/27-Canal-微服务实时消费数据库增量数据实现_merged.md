# 27-Canal-微服务实时消费数据库增量数据实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那接着我们就创建这个微服务

实现增量数据的一个消费

好在这一块

这个微服务工程呢

已经搭建好了

我们就不去搭建它了

因为搭建过程也没有什么技术挑战

在这一块要注意

引入了刚才所讲的

Cana对应的一个依赖包就可以了

引入之后呢

我们现在需要做这么几个事情

在BotusJob.yam里面

去配置相关的一些配置信息

那有哪些配置信息呢

我们来简单介绍一下

在这一块

第一个

你要把当前这一块

它的一个服务地址给配置一下

cana.server

第二个是distraction

给配置一下

好把它拷贝一下就可以了

拷贝到当前这个配置文件里面来

到这里

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

拷贝到当前这个配置文件里面来

烤过来之后

这个cana会指向我们刚才那台服务器

这个是street的一个名称

跟这一块是一样的

在这里有一个example

跟这个要保持一致

这是这一块

这一块有了之后

我们接着就要去实现一个相关的监听操作

那么监听操作

右键新建一个类

我们就写skuhandler

因为我们要监听的是sku表的变化

好在这一块注意

写一个comparity

还要写一个叫counter table

它里面你要给一个表的名字

叫tb

sku

还有一个刚才说过

它需要实现一个接口

叫intra handler

这里面写对应表的一个实体

实体并对象

那咱这里就是我们的

sku

就可以了

好这里面有三个方法

delete

update

和我们insert

我们来实现这三个方法

好这三个

那么第一个呢

无疑就是增加数据的监听

第二个呢

这个肯定是

是

修改数据的监听

那么增加数据和修改数据是不一样的

增加数据

它有个sku信息给你了

增加之后的值

而修改呢

有修改前修改后的值

好最后这个是删除数据监听

来我们只做这么一个是

输出就行了

这里呢我们也只做这么一个是

输出就行了

好输出

还有一个是删除

可以了

呃为了

能够看到更好的效果哈

这里

把方法名字也给打印进去

好增加这里呢

把增加的方法名字打印进去

这是这一块

那么这一块一配置之后

紧接着我们这个项目就起来了

它就可以去实现我们增量数据的一个消费工作了

那我们可以创建一个启动类来测试一下

在这一块咱就创建一个启动类实现一次测试

右键新建一个启动类

写个

superboot

application

psvm

superapplication.run

把当前这个对象的直接码给他

class

args

好搞定了

搞定了之后呢

我们可以启动测试一次

看一看效果

好我们启动测试

看现在这一块

能否

实现我们这个数据的一个实时监听

那等他启动一下

程序目前已经启动

这一块在不停的获取消息

我们要设置一下这个日子级别才行

对吧

不然他总是获取这个消息

会感染到我们这一块

我们在这里配置一下

写一个叫做

live

咱写个

root

root下面的日子级别是

咱就不写那个

别的日子级别

咱写个info

可以了好我们重新启动一下

不然一直输出这个消息

这得多麻烦呢

来重新启动一次

好等他启动

那这一块就不像刚才那时输出那么多日子

那就清爽一些了

还在输出

得了咱把日子级别换成 arrow

调调整一下

可以了再来启动一次

我们这个时候呢

就要配套着来

实现我们数据的一个更改了哈

由于日子级别换成了 arrow

所以这这一块就没有输出那么多数据了

我们开始做一下数据的操作

先做一个修改算了

因为这个增加太多了

咱们就不去做增加

这里修改前有两个 a

修改后没有两个 a 保存一次

你看

这个是

修改前的数据

这个是修改后的数据

行这个搞定了

我们再到最后面去做一个删除试一下

好删除

删除了我们看这里打印没有

哎删除有了吧

那增加我就不做了啊

因为增加这个

这个数据咱这么多这么多个列

我去增加一条记录太麻烦了

我就不增加了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `seckill` 的分布式秒杀系统项目，具体讲解了如何使用 **Canal** 技术实现 **MySQL 数据库的增量数据同步**。课程内容从项目结构和依赖配置开始，逐步深入到核心的 Canal 服务端代码实现，包括创建 `EntryHandler` 接口的监听器 `SkuHandler`，并演示了如何通过打印日志来监控数据的增删改操作。最后，通过启动服务并观察数据库表中的数据变化，验证了数据同步功能的有效性。整个过程旨在教授开发者如何在实际项目中集成 Canal，实现数据的实时监听与处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 项目结构与依赖配置。展示 `seckill-canal` 模块的 `pom.xml` 文件，重点介绍了 `canal-spring-boot-autoconfigure` 依赖。
*   **00:16 - 00:30**: Canal 服务配置。在 `bootstrap.yml` 文件中配置了 Canal 的 `destination` 为 `example`，并配置了 Nacos 服务发现地址。
*   **00:31 - 00:45**: 创建监听器类。在 `src/main/java/com/seckill/canal` 包下创建 `SkuHandler.java` 文件。
*   **00:46 - 01:00**: 实现 `EntryHandler` 接口。在 `SkuHandler` 类中，使用 `@Component` 注解，并通过 `@CanalTable(value = "tb_sku")` 指定监听的表。
*   **01:01 - 01:15**: 实现数据监听方法。编写 `insert(Sku sku)`、`update(Sku before, Sku after)` 和 `delete(Sku sku)` 方法，并在其中添加 `System.out.println` 语句用于打印日志。
*   **01:16 - 01:30**: 启动 Canal 服务。在 `CanalApplication.java` 中，使用 `SpringApplication.run` 方法启动服务。
*   **01:31 - 01:45**: 服务启动与日志观察。在控制台中观察服务启动日志，并在数据库中执行 `INSERT` 操作，验证监听器是否生效。
*   **01:46 - 02:00**: 数据库操作与结果验证。在 Navicat 数据库客户端中，执行 `INSERT` 语句向 `tb_sku` 表插入数据，并观察 `SkuHandler` 的日志输出，确认数据同步成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲中明确列出了“5.3 Canal服务”、“6 同步数据”、“6.1 索引库同步”、“6.2 静态页同步”等章节。
    *   在 `bootstrap.yml` 配置文件中，展示了 Canal 的配置项，如 `destination: example` 和 Nacos 的配置。
*   **代码关键内容**:
    *   **`pom.xml` 依赖**:
        ```xml
        <dependency>
            <groupId>top.javatool</groupId>
            <artifactId>canal-spring-boot-autoconfigure</artifactId>
            <version>1.2.1-RELEASE</version>
        </dependency>
        ```
    *   **`bootstrap.yml` 配置**:
        ```yaml
        server:
          port: 18088
        spring:
          application:
            name: seckill-canal
        cloud:
          nacos:
            config:
              file-extension: yaml
              server-addr: nacos-server:8848
            discovery:
              server-addr: nacos-server:8848
        # 超时配置
        ribbon:
          ReadTimeout: 3000000
        # Canal配置
        canal:
          server: canal-server:11111
          destination: example
        # 日志
        logging:
          level:
            root: error
        ```
    *   **`SkuHandler.java` 代码**:
        ```java
        package com.seckill.canal;

        import com.seckill.goods.pojo.Sku;
        import org.springframework.stereotype.Component;
        import top.javatool.canal.client.annotation.CanalTable;
        import top.javatool.canal.client.handler.EntryHandler;

        @Component
        @CanalTable(value = "tb_sku")
        public class SkuHandler implements EntryHandler<Sku> {

            @Override
            public void insert(Sku sku) {
                System.out.println("============insert:" + sku);
            }

            @Override
            public void update(Sku before, Sku after) {
                System.out.println("============update-before:" + before);
                System.out.println("============update-after:" + after);
            }

            @Override
            public void delete(Sku sku) {
                System.out.println("============delete:" + sku);
            }
        }
        ```
    *   **`CanalApplication.java` 启动类**:
        ```java
        package com.seckill;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;

        @SpringBootApplication
        public class CanalApplication {
            public static void main(String[] args) {
                SpringApplication.run(CanalApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**。讲师首先展示了 `seckill-canal` 模块的项目结构，并在 `pom.xml` 中添加了 `canal-spring-boot-autoconfigure` 依赖，为后续的 Canal 集成做好准备。
*   **场景二：配置文件编写**。讲师在 `bootstrap.yml` 文件中配置了 Canal 的 `destination` 为 `example`，并配置了 Nacos 服务发现地址，确保服务能够正常注册和发现。
*   **场景三：监听器开发**。讲师在 `src/main/java/com/seckill/canal` 包下创建了 `SkuHandler.java` 文件，并实现了 `EntryHandler<Sku>` 接口，通过 `@CanalTable(value = "tb_sku")` 注解指定监听 `tb_sku` 表。
*   **场景四：监听方法实现**。讲师在 `SkuHandler` 类中分别实现了 `insert`、`update` 和 `delete` 方法，并在每个方法中添加了 `System.out.println` 语句，用于打印监听到的数据变化。
*   **场景五：服务启动与数据验证**。讲师在 `CanalApplication.java` 中启动服务，并在 Navicat 数据库客户端中执行 `INSERT` 语句向 `tb_sku` 表插入数据。随后，讲师在控制台中观察到 `SkuHandler` 的日志输出，成功验证了数据同步功能。

---
