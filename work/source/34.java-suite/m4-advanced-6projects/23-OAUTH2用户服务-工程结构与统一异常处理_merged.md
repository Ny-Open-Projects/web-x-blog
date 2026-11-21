# 23-OAUTH2用户服务-工程结构与统一异常处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢

去讲解整个工程结构

以及呢统一异常的处理说明

那在这里呢

咱们要改进用户服务

实现用户的登录接口

并且呢要集成OS2的

现权处理功能

我们看一下整个工程结构呢

我们是如何实现的

有划分哪些包

具体的有哪些实现代码

在整个工程结构当中呢

我们可以看到有configure

这里是负责它的整体配置

然后呢有controller

这里呢是提供对应的

用户登录接口

然后下面呢就是

登录接口相关的

数据层操作接口

这个呢就是service

业务处理方法

然后呢就是咱们的启动内

这个整体结构来讲的话呢

大家应该都比较清晰对吧

这个和最初搭建的用户服务呢

就会有较多的差别

之前呢咱们只是简单的

去通过gateway进行一个调用

然后呢返回一个

指定的支付串

非常简单

但是现在的话呢

咱们就开始实现了

用户服务的登录接口

并且呢集成了os2的健全功能

在这里呢

我们还加入了mybatties

diud的读意的数据源

然后呢

以及supreme security os2的集成

好

这个呢是stock user的一个

工程结构说明

那么呢

我们先将这个stock user

服务工程呢

先创建一下

打开咱们的工程

在这里呢

创建一个新的模块

new

model

这个模块呢

我们给它一个名称

叫做buzzstockuser

点击next

好注意了

它是在buzzstock下面

然后点击finish

创建完成之后呢

咱们找到buzzstock user

将它的home-elite呢

先加入进来

完成了基本的配置

它有哪些依赖呢

咱们找到

stock用户服务的home-elite

将这个elite呢

加入进来

然后在这里呢

跟我们之前的认证服务一样

它呢

会有os2认证的相关elite

咱们来看一下

supreme security的

在这里面

os2的健全相关elite

咱们呢

最主要要掌握这一块的

相关elite的添加和配置

这个服务呢

我们先把它停止掉

我们可以看到在这里面呢

它采用supreme cloud start

这里面呢

封装了os2主件

然后呢

security主件

以及呢

autoconfig自动化配置的主件

这些的话呢

都是supreme security os2

健全相关的elite

然后呢

os2的它的load balance的功能相关elite

这个load balance相当于咱们继续访问认证服务的时候呢

如果说一个节点出现问题

对吧

咱们呢

可以就通过它的服务名称去呢

调用其他的同样的认证服务的节点

这样呢

就保证它的一个高回用

最后呢

我们再来看看这个supreme cloud start

这个supreme cloud start

这个supreme cloud start

这个呢

就是份的一个远程调用

然后呢

公用工具的一个配置依赖

公用外部层的依赖

这个呢

是公用实体层的依赖

之前呢

咱们都讲过了

对不对

在空门下面的

抽取出来的公用主件

那么再往上面呢

是supreme boot监控的依赖

还有Nacos服务注册发现依赖

以及我们主要的supreme boot的主件依赖

在这里呢

就是stock user工程的一个POM配置

配置完成之后呢

咱们先将他的包创建一下

这个还没导入对不对

我们让他呢导入生效

对应不报道

这里还没有发生变化

在这里呢

他们可以看到

buzzstock user已经变成灰色了

我们也将他禁止忽略

因为咱们之前已经实现了

在这里的话呢

是给大家做一个讲解

所以呢

重新去创建一遍

那buzzstock user

我们创建他的一个包

这个呢

再刷新一下

对于import

创建完成之后呢

就可以高亮

对不对

识别成为Mainware项目

然后new package

这个包名呢

我们给他定义一下

叫com ID cast

点shared

buzzstock user

然后我们点击OK

接着话呢

咱们再将他对应的纸包呢

创建一下

这个纸包的话呢

有config对吧

Necdir

config

然后呢

还有我们的controller成接口

我们先将包创建好

后面呢

再做具体实现

还有Dio数据产对不对

然后呢

service

MakDir

MakDir

还有Viu相关的对象

这里呢

因为我这边采用命令的方式

创建会比较快一点

大家的手工创建通过这里面的创建也是一样的

可以给你

创建完成之后呢

可以看到对应的纸包

那用户服务呢

这个基本的配置呢

就已经完成

咱们呢

回到讲习当中

然后呢

去看一下我们接下来的统一异常的处理说明

咱们呢

先把周边的这些组件和依赖呢

都创建和实现好

对不对

把这些规范性的这些标准化的组件呢

都先将它实现

接着的话呢

我们才能专注于核心逻辑的一个处理

那我们来看一下统一异常处理这块

该怎么去做呢

为了规范各微服对异常的处理

我们呢

就要统一做一个封装

包括它会有一个统一异常处理的一块

它的错误码的一些定义

如果说各个微服都定义自己的一套异常呢

将来维护起来也是非常麻烦

比如说

如果我们经过一个请求

过程当中呢

有好几个微服节点

每个微服节点呢

有自己的一套异常

那么我们根据这个错误码呢

很难定位出来

到底是哪个异常

哪个服务节点所抛出来的

对不对

那我们来看一下

该怎么去封装呢

在store Common Utils下面呢

我们封装了两类异常

第一个呢

是Compound Exception

这个呢

就是组件异常

使用来讲呢

相对会比较简单一点

这个是什么意思呢

比如说我们像Stream Utils

对不对

对Stream的一些操作

比如出现那些空子人啊

还有我们对那个工具类

比如像那个加密的

或者MD5加密之类的

这些呢

都作为我们的辅助组件

那这些处理的时候

抛出来的异常呢

我们就统称为Compound Exception

另一类呢

是Business Exception

这个呢

是为业务异常

它相比组件异常呢

可以封装

更多的信息

并用我们日子分析排查

那这个就跟逻辑

有比较紧密的关系

比如说咱们要去做一个用户登录

对不对

咱们是不是要判断

这个用户是否存在

那么呢

这个用户不存在

可能呢

就会抛出一个业务异常

要让你呢

去重新输入对应的账号

然后呢

它的密码错误呢

我们可能还会再抛出一个异常

说密码这边的话呢

判断是错误的

然后的话呢

如果是

你的用户的一些那个

权限信息不合法

那么呢

我们也可以呢

去通过这个business acceptance

给它做一个包装和返回

错误码呢

我们来看一下

既然有这两个类的

那个异常错误码

那我们看一下该怎么去封装呢

错误码呢

我们要先统一一下

要实现了

ilcodeanime这个接口

这个呢

是一个Mage

那我们将Mage呢

做了一个抽象

不能随便去定义

applicationilcodeanime呢

它是一个错误码的实现类

那么呢

首先呢

咱们定义一个接口对不对

这个呢

就是application应用服务的

它的一个错误码

比如说将来你还想扩展其他的一些错误码呢

实现对应的ilcodeanime就可以了

好

然后我们可以看一下

在这里面的话呢

它是怎么去做的

里面的主要是包含服务模块

错误编号

消息和错误级别信息

我们呢

把代码来看一下

先给大家看一下整体的一个代码实现

在这里呢

是application

ilcodeanime的具体实现

它是实现了ilcodeanime这个接口

我们可以看一下这个接口里面是定义了些什么内容呢

在这里面呢

我们可以看到它是一个interface

这里主要是定义了一些常量

对吧

这个常量的话呢

我们也可以看到它定义了一个用户服务模块

然后系统模块

如果咱们将来呢

有扩充交易服务模块

在这里面的话呢

咱们接着扩展去定义就可以了

然后呢

去定义了一个内容模块

这个内容模块呢

就是一个公用的接口

这些接口的话呢

有获取自定义的错误码

就是我们的错误编号

然后呢

就是错误码的描述信息

还有我们的错误级别信息

这个错误级别信息就有点类似于咱们log日志里面的info级别

won级别以及的l级别

对不对

根据这个级别的话呢

咱们就一目了然知道呢

它这个错误信息的一个严重程度

这个是它的接口的定义

那下面呢

咱们可以看到它定义了具体的枚举对不对

枚举呢

主要有两个属性

一个是code

另外呢

是message消息

在这里面呢

咱们可以看到

这个消息的话呢

是针对异常的一个具体描述

那么的话呢

错误级别model

在这里面为了便于它的一个实现

咱们也实现了不同的构造方法

可以看到

这个构造方法的话

直接传递code跟message就可以了

对不对

那么它model的话呢

就是采用系统的模块

然后呢

是普通的级别

那么呢

你也可以去指定它具体的model

也可以去指定它的级别

对不对

都是有不同的构造方法

那么这样的话呢

咱们定义错误码起来呢

就非常灵活

可以根据自己的需要去定义了不同类型的

不同需求的错误码

好

然后呢

这些错误编号呢

咱们最好要统一规范一下

对吧

这些错误编号

首先呢

不能确保是冲突的

然后呢

这错误编号呢

咱们建议不同的服务

比如说用户服务

它就一开头了

那么订单服务呢

它就二开头了

这样的话呢

就非常直观

到时候呢

一看到对应的错误码

咱们就知道了

它到底是哪个模块出现了问题

好

这一块呢

是它整个的错误码的一个封装处理

然后其他的话呢

就是这些获取具体的编号

错误详情等等的一些公用型的接口

那么咱们再来从讲义当中回顾一下

在这里面呢

就是服务模块

错误编号

消息和错误级别消息

便用我们规范性的根据错误码

来排查系统的错误信息

有了异常和错误码呢

并非可以任意去使用

为了避免调用一个接口呢

同一个异常在多处抛出

也就是说我们一个异常呢

你不要在DAO里面做了处理抛出

然后又在service里面做了处理抛出

最后在controller层又去做一个处理抛出

这个我们规范一下

在service业务层去统一处理异常

因为你这样在每个地方都去抛出

第一比较混乱

第二你这样维护起来是非常累的

而且的话整个结构层次非常不清晰

那么我们就规范一下

在service业务层的统一处理异常就可以了

比如说你的数据没找到

那么的话你DAO并不去做判断

由service层去做对应判断处理就可以了

service它本来就是负责业务逻辑处理

然后由controller接入层

它就去捕获对应的异常

这里面会负责具体的抛出

然后又去处理抛出

然后由controller层去捕获

你不要在DAO层上面去catch一下

在service层又去catch一下

然后在controller层又去catch一下

这些话是没有递交的

最后咱们封装返回给调用方

好 这个就是咱们统一异常的处理说明

以及整个工程结构的一个基本搭建

还有基本的一些配置

好 这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-user”的用户服务模块的开发与实现教程。课程主要围绕如何改进用户服务，实现用户登录接口，并集成 Spring Security OAuth2 认证功能。讲师通过展示项目结构、依赖配置、异常处理枚举类等核心代码，系统地讲解了服务的构建过程。视频内容覆盖了工程结构设计、依赖管理、统一异常处理等关键环节，旨在帮助开发者理解并实现一个具备完整安全认证能力的用户服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 开场，展示课程大纲，介绍本章主题为“用户服务”的实现。
*   **00:00:05 - 00:00:15**: 展示项目工程结构，重点介绍 `stock-user` 模块下的 `src/main/java` 目录结构，包括 `config`, `controller`, `dao`, `service`, `startup` 等包。
*   **00:00:15 - 00:00:25**: 讲解 `pom.xml` 文件，展示项目依赖，包括 Spring Boot Web、Nacos 服务发现、Spring Boot Actuator、Spring Cloud Security OAuth2 等关键依赖。
*   **00:00:25 - 00:00:35**: 展示 `ApplicationErrorCodeEnum` 枚举类，定义了系统中常见的错误码和消息，如 `USER_NOT_FOUND` (用户不存在) 和 `USER_PWD_ERROR` (用户密码错误)。
*   **00:00:35 - 00:00:45**: 讲解 `ApplicationErrorCodeEnum` 枚举类的实现细节，包括 `getModule()` 和 `getMessage()` 方法，用于获取错误模块和错误信息。
*   **00:00:45 - 00:00:55**: 回顾并总结本章内容，强调了工程结构、依赖配置和统一异常处理的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3. 实现”、“3.1 工程结构”、“3.2 统一异常处理说明”、“3.4 核心类实现说明”。
    *   **核心目标**: “改进用户服务，实现用户登陆接口，集成OAUTH2鉴权功能。”
    *   **工程结构**: 展示了 `stock-user` 项目下的标准 Maven 结构，包括 `controller`, `dao`, `service`, `config` 等包。
    *   **依赖说明**: 在 `pom.xml` 中，明确标注了 `Nacos服务注册发现依赖`、`Spring Boot 监控组件依赖`、`Spring Security OAUTH2 鉴权相关依赖`。

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <!-- Spring Boot Web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Nacos 服务注册发现依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>

        <!-- Spring Boot 监控组件依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <!-- Spring Security OAUTH2 鉴权相关依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-security</artifactId>
            <version>${spring-cloud.version}</version>
        </dependency>
        ```
    *   **`ApplicationErrorCodeEnum` 枚举类**:
        ```java
        public enum ApplicationErrorCodeEnum implements IErrorCodeEnum {
            SUCCESS("200", "成功"),
            FAILURE("300", "系统异常"),
            SYS_ERROR_ENCRYPT_SINGED(ErrorCodeEnum.MODULE_SYSTEM, "00002", "签名加密错误"),
            USER_NOT_FOUND(ErrorCodeEnum.MODULE_USER, "00003", "用户不存在！"),
            USER_PWD_ERROR(ErrorCodeEnum.MODULE_USER, "00004", "用户密码错误！");
        }
        ```
    *   **`ApplicationErrorCodeEnum` 枚举类实现方法**:
        ```java
        @Override
        public String getModule() {
            return IErrorCodeEnum.MODULE_SYSTEM + this.code;
        }

        @Override
        public String getMessage() {
            return this.message;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：工程结构展示** (00:00:05)
    *   **描述**: 讲师在 Typora 文档中滚动展示 `stock-user` 项目的工程结构，重点突出 `controller`, `dao`, `service` 等核心包，说明了模块的分层设计。

*   **场景二：依赖配置演示** (00:00:15)
    *   **描述**: 讲师切换到 IntelliJ IDEA，打开 `bulls-stock-user` 项目的 `pom.xml` 文件，逐行讲解并高亮显示了 Spring Boot Web、Nacos、Actuator 和 Spring Security OAuth2 等关键依赖的配置，强调了这些依赖对实现用户服务和 OAuth2 认证的重要性。

*   **场景三：异常枚举类实现** (00:00:25)
    *   **描述**: 讲师在 IDE 中打开 `ApplicationErrorCodeEnum` 枚举类文件，展示其定义的错误码和消息，如 `USER_NOT_FOUND` 和 `USER_PWD_ERROR`。随后，讲师高亮并讲解了 `getModule()` 和 `getMessage()` 方法的实现，说明了如何通过枚举类统一管理错误信息。

*   **场景四：总结与回顾** (00:00:45)
    *   **描述**: 讲师在 Typora 文档中滚动到“3.4 核心类实现说明”章节，总结了本章的核心内容，即通过工程结构、依赖配置和统一异常处理，成功构建了一个具备 OAuth2 认证能力的用户服务。
