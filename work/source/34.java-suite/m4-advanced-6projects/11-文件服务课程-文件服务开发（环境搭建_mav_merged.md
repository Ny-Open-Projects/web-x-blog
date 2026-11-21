# 11-文件服务课程-文件服务开发（环境搭建_mav — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,继续来看咱们Maven工程的环境搭建,刚才呢,我们是把这个PTFile Entity,也就是我们文件服务啊,相关的这个实体模块,对吧,把它已经创建好,并且呢,是直接啊,把我们封装好的这些实体类DTO Domain这些类呢,把它考到我们这个项目里面来了,因为对于这些基础啊,基础模块,我们这些实体类DTO,这些呢,我们就没有必要在课上自己去写了啊,

那么直接把它考进来,到时候我们直接拿过来用就可以了,好,那么再往下呢,我们就需要来创建什么呢,我们PTFile它相关的这个文件服务模块,也就是PTFile Server,好,同样还是在我们PTFile下边来创建模块,好,选中它右键,对吧,然后呢,指定一下这个项目的名称,好,同样的是放在PTFile这层目录下边,好,然后呢,直接完成,

然后呢,我们可以看一下在我们这个PTFile下边,它这个POM文件,你看,它现在是不是已经聚合进来了两个,对吧,刚才看到的只有这个PTFile Entity,现在呢,能看到这个PTFile Server,好,这是我们这个文件服务这个模块,好,到时候我们启动呢,就启动这个模块就可以了,同时呢,我们当前这个模块呢,它是不是还继承了我们PTFile这个复工程,对吧,复工程,好,那么这个POM文件呢,咱们是不是接下来需要来配置一下,

这里边呢,要导入的这个配置呢,就比较多了,我们可以先来复制一下,然后呢,再带着大家呢,一块来看一下我们导入的这些内容,直接复制到Build这个地方,好,因为它这是一个服务模块啊,所以这里边呢,所依赖的这个Main文坐标呢,就比较多了,好,咱们来看,这个是文件服务启动模块,对吧,然后呢,它是依赖的什么呢,PTOS API,这个是谁呢,

其实是PTOS API,

这个是在我们这个PTOS API,这个模块,对吧,然后呢,还有这个什么呢,就是关于我们这个Spring Cloud的OpenFane,对吧,因为我们接口调用呢,需要使用它,然后呢,还有什么呢,PT Tools Log,这是我们这个小水价工程里面自带的这个模块,对吧,PT Tools Log,这个是跟日志相关的模块,还有Swagger,对吧,这是我们接口文档展示的模块,还有呢,PT Tools Validator,这是进行我们表单数据校验的模块,还有XSS,对吧,

这个呢,是对我们页面输入的信息啊,进行清理,防止攻击,这个模块,然后呢,这个接下来又是这个Spring Cloud的阿里巴巴,对吧,阿里巴巴提供的这个Discovery,因为我们这儿呢,要使用到我们的这个Nucleus,对吧,所以需要把它引入进来,然后呢,这个呢,是进行这个熔断的,对吧,Netflix的Hastrix,熔断的模块,然后呢,这个是ASM模块,接下来呢,这个呢,是我们的这个Starter,Spring Boot,Starter,

Starter,

Starter,

然后呢,

然后呢,

然后呢,

然后呢,

然后呢,

接下来,

这是一些云存储的,像什么阿里云呢,

七牛云呢,

还有Fast DFS啊,

等等,

这些,

对吧,

然后这是Storm Boot给我们提供的这个Config Processor,

处理器,

OK,

那么下面这些就是一些常规配置了,

这是我们整个PDFile这个模块里边啊,

所涉及到的这些什么呢,

POM文件配置,

那么整体来说呢,

还是比较多的啊,

因为我们这是一个服务启动模块,

所以它依赖的这些,

这些架包呢,

是比较多的,

好,

然后接下来呢,

我们把POM文件搞定之后啊,

再往下呢,

是不是就是我们需要来导入什么呢,

我们这个服务啊,

文件服务相关的一些配置文件,

而这些配置文件呢,

也是比较多的啊,

那么我们这个课程呢,

重点还是来开发我们文件服务相关的这些文件上传下来,

对吧,

分片,

合并等等,

这些跟文件服务密切相关的这些业务代码,

所以说,

对于这些常规的一些配置呢,

我们就不再课上啊,

去手写了,

而实际开发当中啊,

其实也都是这样的,

基本上也都是直接导入,

拿过来来修改一下就可以用了,

所以我们可以看一下,

我们这个地方的这些配置文件呢,

我提前都已经整理好了,

咱们呢,

直接拷进来,

拿过来用就可以,

那么我们导入的这些配置文件呢,

咱们来分一下类啊,

可以看一下,

一个是dozer,

对吧,

dozer呢,

它其实是一个什么呢,

是一个进行对象之间,

进行这个转换的,

比如我把A对象,

把它转成B对象,

它们这里边有一些属性呢,

是相同的,

对吧,

当然也可以不相同,

我们通过这个映射文件,

可以进行映射,

然后呢,

就可以直接啊,

把这个对象呢,

进行一个映射,

它底层其实是基于我们的binutils啊,

来实现的,

啊,

然后还有mapperfile,

这其实就是我们这个mybatties,

它的映射文件了,

对吧,

配置文件,

啊,

然后呢,

还有bootstrap,

这是我们sprintboot启动的时候,

首先是不是要加载这个配置文件,

好,

然后还有一个lobac-spring,

这是日志的文件,

然后呢,

spwire,

这个是进行这个,

我们这个数据源的,

也就是说我们需要在我们的控制台,

来输出我们执行的circle语句,

哎,

所以说呢,

需要准备这么一个配置文件,

好,

那么这些配置文件呢,

在我们资料文件服务相关配置文件呢,

在这个目录下面,

我们都已经整理好了,

好,

就是这个文件服务相关配置文件,

咱们整个啊,

把它,

把它来复制一下,

然后呢,

直接把它粘贴到我们这个pdfile server,

这个下面,

好,

放在这个resources下面,

好,

直接在这儿来粘贴一下就可以了,

OK,

那么我们一次性呢,

是导入了这么多的配置,

大家来看一下,

一个是这个,

这个dozer下面呢,

我们是配置,

导入了这么两个文件,

对吧,

一个是globaldozer,

这个是全局的,

目前没有用到,

所以就空着,

然后呢,

还有biz,

对吧,

bizdozer,

这是跟我们业务相关的,

你看,

这个地方呢,

我们给了这么一个示例,

对吧,

然后呢,

这是class a,

class b,

这是这么两个类,

这两个类呢,

我想把这个类,

把它转成这个类的一个对象,

那么我们就需要让这两个类来做一个映射,

来做一个映射,

然后以及什么呢,

这两个类里边,

它们的属性,

对吧,

哪个属性对应哪个属性,

比如说在我们这个a类,

上面这个代表的就是a类啊,

它这里边是不是有个属性叫做type,

来看,

是不是叫type,

然后呢,

在我们这个b类,

就是下边这个类里边,

是不是有一个属性叫做context type,

那么现在呢,

我需要把这个a对象映射成b对象,

那么它这两个属性是不是不一样,

那么在这个地方呢,

就需要来映射一下,

对应一下,

这样的话呢,

我就知道,

把a类的这个type属性值,

复制给什么呢,

b类的context type这个属性值,

有人说,

那这里边我们看到有这么多属性,

为什么只映射这个呢,

是因为它们,

这两个属性名是不是不一样,

那么如果属性名一样的话,

比方说md5,

size,

name,

然后呢,

你看这边是不是也有,

md5,

对吧,

然后呢,

size,

name,

属性名如果完全一样呢,

其实就不用映射了,

只有属性名不一样的时候,

才进行映射,

OK,

所以说呢,

我们这个地方呢,

直接拷过来就可以,

这个地方呢,

我们好像不小心放错位置了,

我这个src的话,

应该是这个src,

对吧,

我们刚才这个,

这个,

这个配置文件呢,

应该是放错位置了,

因为它这个层次呢,

比较深,

刚才我们看啊,

我刚才是不小心放在这个位置了,

这个呢,

我对应的这个位置,

其实应该是我们这个ptf,

对吧,

是这个复工程,

咱们呢,

把它,

重新来这个复制一下,

复制,

应该是上面这个位置,

对吧,

刚才是放错位置了,

应该是这个位置,

好,

然后呢,

我们直接把它粘贴到这个地方,

OK,

好,

那么粘到这边来,

之后呢,

咱们这个地方,

这个就不要了,

因为它这个层次呢,

稍微有一点点乱,

好,

然后呢,

我们到这边来看,

刚才呢,

是已经看到,

看过了这两个配置文件了,

对吧,

这是dozer的,

然后呢,

这个,

这个myprofile呢,

这就是我们mybattis,

它的这个应设文件,

好,

你看这个是attachment,

有人说,

那这个地方为什么分成了两个啊,

一个是base,

一个是ext,

base下边啊,

这个文件呢,

这两个文件,

它其实啊,

这里边并没有circle语句,

而是什么呢,

而是我们这个表里边的一些什么呢,

一些这个基本的字段,

跟类里边的一些属性的映射,

你看通过result map是不是进行映射,

以及什么呢,

所有的这个表里面字段呢,

统一进行抽取,

在这统一进行抽取,

然后呢,

我们在真正circle语句的地方呢,

可能就会用到我们这个result map,

也可能会用到我们这个,

这些这个字段,

对吧,

那么我们就可以通过include,

直接引用它就可以,

引用这些字段,

所以你看真正circle语句呢,

其实对应的是在ext下边这个映射文件里边,

你看,

对吧,

select的语句,

对吧,

select的语句,

然后呢,

我select的,

然后字段,

这些字段呢,

我就不用写了,

我直接include reference id,

叫做base column list,

而这个base column list在哪呢,

是不是应该就在我们这个地方,

对吧,

这样的话就相当于把我们这些字段给拿过去了,

放在了这个位置,

好,

实际上这两个文件呢,

你完全可以合并到一块啊,

也就是整到一个文件里面也是可以的,

只不过我们在这呢,

就是把所有的circle语句写到这个ext,

这个目录下边,

然后呢,

把我们这个抽取的这些东西呢,

放在这个base下边,

进行了这么一个分割,

然后呢,

这个file mapper其实也是这个道理啊,

也是这个道理,

你看,

然后具体的circle语句呢,

全都在下面这个里边,

好,

这circle都在这儿了,

当然,

现在呢,

我们先不具体来看这些circle语句了,

到时候呢,

我们用到了之后呢,

再来打开它看一下,

好,

整个这里边呢,

对应的就是我们mybatties plus相关的这些,

mybatties相关的配置,

对吧,

然后呢,

这个呢,

就是非常非常重要的,

就是我们sprint boot启动的时候要加载的这个bootstrap,

这个默认的配置,

好,

然后大家可以看到,

我们在这呢,

自定义了这么一些属性,

对吧,

这么一些属性,

品达,

对吧,

然后呢,

local IP,

而这个IP的话具体在什么位置,

你看我们在这儿呢,

并没有去这个写死,

对吧,

而是什么呢,

我们在docker部署的时候呢,

需要去指定,

需要去指定,

然后呢,

包括下边这块,

Nucleus IP,

然后IP的话呢,

它首先从我们环境变量去获取,

如果获取不到呢,

就会从我们POM文件去获取,

咱们前面是不是刚刚完成了这个配置,

在POM文件里边,

你看我们有一个小的技巧,

可以按着control来点,

一点击,

它就能找到我们这个PD APPs,

对吧,

然后呢,

从这儿取的值,

它其实相当于就是把我们这段给取过来了,

当然了,

我们也可以直接把这个IP地址写在这儿,

那么我们现在相当于把这个源头呢,

把它配置在这个地方,

然后其他地方如果想用,

用这种方式呢,

来获取一下,

就两个at符号,

中间加的是什么,

pom.nexus.ip,

其实就是这个标签的名称,

对吧,

这个标签的名称,

通过这种方式呢,

就可以从我们POM文件来把IP地址给取回,

同理呢,

我们这个端口号是不是也是这样来取,

你看取的就是这个8848,

然后呢,

这是我们那个namespace,

对吧,

然后呢,

它是也是取的这个地方,

这样的话就可以把这个内容给取到了,

那么取到之后呢,

我们后边呢,

就可以直接从我们这个自定义的这些变量里边是不是来获取这些值,

那么下边这些配置呢,

你看Spring这个application name,

然后呢,

这个name从哪取的值呢,

也是从POM文件,

其实取的就是PDFile server,

全都是取值,

然后呢,

Active我们当前使用的是哪个环境啊,

点过来是不是第一V这个环境,

所以大家一定要熟悉我们这种用法,

要不然的话,

你不会看的话呢,

这个地方呢,

它全都是引用,

对不对,

你根本就看不到具体的值,

那么它其实具体的值都是从这儿,

相当于这是源头,

在POM文件里面配置的,

这是源头,

然后接下来呢,

是Spring Cloud,

是吧,

NUCLS,

这是配置,

对吧,

我们的配置信息,

然后SERVER ADDRESS,

因为呢,

它要加载我们的配置文件,

而我们的配置文件呢,

都在我们NUCLS配置中心,

而这个配置中心呢,

它要去连,

那么我们需要告诉它我们这个服务的地址,

对吧,

也就是配置中心的地址以及端口号,

而这个地址的话呢,

你看这个地方还是没有写具体的值,

而是什么呢,

品达NUCLS IP,

其实它就是从我们这个地方,

品达NUCLS IP,

其实就是取得它的值,

而它的值呢,

又是取得谁呢,

又是取得我们这个POM文件里面这个值,

刚才已经提到过了,

好,

那么这个是IP地址,

然后冒号,

后边跟上这个端口号,

对吧,

然后呢,

File Extension,

这个呢,

就是我们配置中心里边,

这些这个配置文件,

它的后缀呢,

都是这种YML的,

前面我们也都看到了,

你看,

在这儿,

咱们这些是不是全都是这种YML,

这种扩展名的,

好,

然后呢,

Namespace,

从哪个命名空间去,

这个获取我们的一些配置文件呢,

那么这个地方,

品达NUCLS Namespace,

其实就是取到了这个地方,

对吧,

好,

这个地方刚才我们也看了,

它是从这儿取得值,

这就是一层一层引用,

对吧,

最终呢,

是引用到我们这个POM文件这儿,

然后呢,

还要Share,

这个就是共享的一些配置,

也就是说,

每一个这个服务啊,

不管是我们当前这个文件服务,

还是我们这个,

脚手架里面自带的这些网关服务,

还有权限服务,

都会加载到这几个配置,

Common,

Redis,

还有MySQL,

你看这里边Common,

MySQL,

Redis,

也就是这三个配置文件呢,

是作为公共的配置文件,

那么我们这些应用呢,

全都可以要加载到,

然后Refresh,

就是这个Common呢,

如果发生变动呢,

它是会自动通知到我们这些服务,

对吧,

它就自动刷新,

Enable True,

表示我们当前这个配置中心呢,

是启用状态,

OK,

那么也就是说,

我们对于当前咱们这个文件服务之外来说,

对于我们这个PTFEL Server这个文件服务来说呢,

它可以加载到这三个配置文件,

然后另外呢,

还有两个是这个服务特有的,

一个是什么呢,

PTFEL Server,

对吧,

还有一个是PTFEL Server DEV,

这两个文件,

所以说呢,

这些,

这两个是它特有的,

然后另外三个呢,

是公共的,

所以它一共呢,

应该是能够加载到这五个文件,

五个文件,

然后接下来呢,

是Discovery,

对吧,

这是我们这个发现,

也就是说我们NUCLS,

我们大家都知道,

它除了可以作为配置中心呢,

还可以作为注册中心,

对吧,

所以说呢,

我们可以从这个注册中心去查找服务,

所以说呢,

还是通过配置这个什么呢,

SERVER ADDRESS,

NAME SPACE,

对吧,

然后这些来进行配置,

然后下面这些是关于日志的,

这是关于我们这个bootstrap这个配置文件,

来看一下,

再往下呢,

这是关于我们这个loadback,

对吧,

loadback来进行这个什么呢,

进行记录日志,

然后这个呢,

这是我们的一个配置文件啊,

叫做什么呢,

P6SPY,

对吧,

P6SPY,

这个配置呢,

相关的,

其实是在这个里面配置的,

是PTFEL SERVER DEV,

大家可以来看一下,

你看这里边我们是不是配置了这么一个数据源,

对吧,

然后呢,

叫什么P6SPY,

什么DRIVER,

这个,

这个数据源呢,

它的作用是什么呢,

就是可以将我们执行的circle语句呢,

把它输出在控制台,

并且呢,

这个circle语句执行的时间呢,

也可以输出在控制台,

相当于是circle的一个分析,

对吧,

这么一个小的插件,

好,

但这个呢,

仅限于在我们这个开放环境下面来使用,

生产环境下面呢,

是不建议使用的,

因为它是有性能消耗的,

性能损耗的,

好,

这是关于我们这个PTFEL相关的这些配置文件呢,

我们统一导进来,

然后呢,

带着大家,

来整体来熟悉一下,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析报告。

---

### 1) 视频摘要

本视频为一个关于“文件服务”模块开发的技术课程，主要演示了如何在 Spring Cloud 微服务架构下，从零开始搭建一个文件上传与下载服务。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目初始化、Maven 依赖管理、数据库映射配置、Nacos 配置中心集成以及日志配置等核心环节。整个过程围绕 `pd-file-server` 子模块展开，旨在构建一个可扩展、可配置的文件服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目总览 PPT，介绍本节内容为“文件服务开发”。
*   **00:05 - 00:15**: 进入“5.1 环境搭建”章节，讲师在 IDEA 中打开项目结构，准备创建 `pd-file-server` 模块。
*   **00:15 - 00:30**: 演示如何在 `pd-file` 项目中创建 `pd-file-server` 子模块，并配置其 `pom.xml` 文件。
*   **00:30 - 00:50**: 编辑 `pom.xml`，添加父项目依赖和核心 Spring Boot 依赖。
*   **00:50 - 01:10**: 继续编辑 `pom.xml`，添加 `spring-cloud-context`、`mybatis-plus-boot-starter`、`aliyun-sdk-oss`、`qiniu-java-sdk` 等依赖。
*   **01:10 - 01:25**: 展示 `pom.xml` 中的 `exclusions` 配置，用于排除 `spring-boot-starter-web` 中的 Tomcat 依赖。
*   **01:25 - 01:40**: 展示 `pom.xml` 中的 `dependencies` 配置，添加 `pd-file-entity` 和 `pd-tools-databases` 等模块依赖。
*   **01:40 - 02:00**: 切换到 `src/main/resources/mapper` 目录，展示 `AttachmentMapper.xml` 文件。
*   **02:00 - 02:20**: 在 `AttachmentMapper.xml` 中配置 `resultMap` 和 `select` 语句，用于查询附件信息。
*   **02:20 - 02:40**: 展示 `src/main/resources/bootstrap.yml` 文件，配置 Nacos 服务发现和配置中心。
*   **02:40 - 03:00**: 在 `bootstrap.yml` 中配置 Nacos 的 `server-addr`、`namespace`、`file-extension` 等参数。
*   **03:00 - 03:20**: 继续编辑 `bootstrap.yml`，配置 `logging` 日志文件路径和名称。
*   **03:20 - 03:40**: 展示 `src/main/resources/logback-spring.xml` 文件，配置不同环境（test, docker, prod）的日志级别和输出。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲：`文件服务开发` -> `5.1 环境搭建` -> `5.1.1 数据库环境搭建`、`5.1.2 Nacos环境搭建`、`5.1.3 Nginx环境搭建`、`5.1.4 maven工程环境搭建`。
    *   注释：`文件服务相关实体类位置`、`文件服务/资料/文件服务相关实体类`。

*   **代码关键内容**:
    *   **`pom.xml` (父模块)**:
        ```xml
        <parent>
            <artifactId>pd-file</artifactId>
            <groupId>com.ithema</groupId>
            <version>1.0.0</version>
        </parent>
        ```
    *   **`pom.xml` (子模块 `pd-file-server`)**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.apache.tomcat.embed</groupId>
                    <artifactId>tomcat-embed-websocket</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-tomcat</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        ```
        ```xml
        <dependency>
            <groupId>com.ithema</groupId>
            <artifactId>pd-file-entity</artifactId>
            <version>1.0.0</version>
        </dependency>
        ```
        ```xml
        <dependency>
            <groupId>com.ithema</groupId>
            <artifactId>pd-tools-databases</artifactId>
            <version>1.0.0</version>
        </dependency>
        ```
    *   **`AttachmentMapper.xml`**:
        ```xml
        <resultMap id="Base_Column_List" type="com.ithema.pinda.file.dto.AttachmentDTO">
            <id column="biz_id" property="bizId" />
            <result column="biz_type" property="bizType" />
            <result column="file_name" property="fileName" />
            <result column="file_size" property="fileSize" />
            <result column="file_url" property="fileUrl" />
            <result column="create_time" property="createTime" />
        </resultMap>
        ```
        ```xml
        <select id="selectByBizIdAndBizType" parameterType="java.util.Map" resultType="com.ithema.pinda.file.dto.AttachmentDTO">
            SELECT * FROM pd_attachment
            WHERE a.biz_id = #{bizId} AND a.biz_type = #{bizType}
            ORDER BY a.create_time DESC
        </select>
        ```
    *   **`bootstrap.yml`**:
        ```yaml
        spring:
          cloud:
            nacos:
              config:
                server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
                file-extension: yaml
                namespace: ${pinda.nacos.namespace}
                shared-dataids: common.yaml,redis.yaml,mysql.yaml
                refreshable-dataids: common.yaml
                enabled: true
              discovery:
                server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
                namespace: ${pinda.nacos.namespace}
                metadata:
                  management.context-path: ${server.servlet.context-path}:${spring.mvc.servlet-path}
        ```
    *   **`logback-spring.xml`**:
        ```xml
        <springProfile name="test,docker,prod">
            <logger name="com.ithema.pinda.file.controller" additivity="true" level="INFO">
                <appender-ref ref="ASYNC_CONTROLLER_APPENDER" />
            </logger>
            <logger name="com.ithema.pinda.file.service" additivity="true" level="INFO">
                <appender-ref ref="ASYNC_SERVICE_APPENDER" />
            </logger>
            <logger name="com.ithema.pinda.file.dao" additivity="false" level="DEBUG">
                <appender-ref ref="ASYNC_DAO_APPENDER" />
            </logger>
        </springProfile>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与模块创建** (00:05-00:15)
    *   讲师在 IDEA 中打开项目，点击“新建模块”，创建名为 `pd-file-server` 的子模块。
    *   在 `pom.xml` 中，将父模块设置为 `pd-file`，并配置了 `groupId` 和 `version`。

*   **场景二：Maven 依赖管理** (00:30-01:40)
    *   讲师在 `pom.xml` 中添加了 `spring-boot-starter-web` 依赖，并通过 `exclusions` 排除了内置的 Tomcat。
    *   添加了 `spring-cloud-context` 用于服务发现和配置。
    *   添加了 `mybatis-plus-boot-starter`、`aliyun-sdk-oss`、`qiniu-java-sdk` 等第三方库。
    *   添加了 `pd-file-entity` 和 `pd-tools-databases` 依赖，用于引入实体类和数据库工具。

*   **场景三：MyBatis Mapper 配置** (01:40-02:00)
    *   讲师在 `src/main/resources/mapper` 目录下创建了 `AttachmentMapper.xml` 文件。
    *   在文件中定义了 `resultMap`，用于映射数据库字段到 Java 对象。
    *   定义了 `select` 语句，用于根据 `bizId` 和 `bizType` 查询附件信息。

*   **场景四：Nacos 配置中心集成** (02:20-0
