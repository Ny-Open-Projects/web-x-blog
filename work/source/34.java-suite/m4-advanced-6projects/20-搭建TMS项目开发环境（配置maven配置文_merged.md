# 20-搭建TMS项目开发环境（配置maven配置文 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么接下来呢

来看我们项目第一章的最后一个小节了

这个小节呢

就是配置Maven的配置文件

咱们前面呢

使用Maven呢

应该用的也比较多

对吧

那么我们知道啊

Maven安装完之后呢

其实有一个非常重要的核心的配置文件

就是那个settings.tmr

咱们呢

可以一块来看一下

我当前

我自己的Maven

然后呢

我现在使用的Maven呢

是在这个地方

libs

然后呢

在这有一个Maven 3.5.4

好

然后呢

这是我本地安装的Maven

对吧

然后呢

在这个config下边

是不是有一个叫做settings.tmr

好

然后这里边呢

我们通常会配置什么呢

我们配置最多的呢

其实就是这个

就是指定一下我们

当前呢

使用的这个Maven本地的仓库

对吧

在什么位置

本地仓库在什么位置

对吧

这个用的是最多的

然后呢

我们如果要使用到一些私服

的话呢

还需要在这个settings文件里面

来配置一些私服

配置私服

而我们现在呢

就需要来修改一下这个文件

那么

为什么要使用到私服呢

我们在这来说明一下

就是我们导入的这个初始工程当中

其实引入了两个架包

这两个架包的话呢

并没有在我们Maven的中央仓库里面去

那么这两个架包它是什么呢

它是由我们这个通用权限系统提供的

提供的

你看一个叫做PDM2

一个叫做PDM2

还有一个叫做PDOS Entity

还有一个叫做PDOS API

好

那么这两个架包的话呢

我们已经把它部署到私服上去了

所以大家呢

需要去在你本地的这个Maven的

settings文件里边

来配置上这个私服

这样的话呢

才能够从我们提供的这个私服上

去下载到我们所对应的这两个架包

否则的话

你本地的Maven工程是无法

这个连编译都通过不了的

具体是在哪儿

这个引入的这两个坐标呢

大家来看一下

是我们这个PDU

在这里边

大家来看

有个POM文件对吧

然后POM文件里边

你看我们其实是引入了

来找一下

当前呢

我们应该是已经给它删掉了

为了防止这个报错对吧

为了防止报错

所以说呢

我们需要注意是什么呢

就是咱们呢

需要先把我们这个私服

先把私服呢来配置好

这个私服具体怎么配置呢

大家可以来参考一下

我今天这个资料里边

你看还是在我们初始工程里边

有一个settings文件

然后呢

参照这个settings文件就可以

其实我本地的这个文件呢

其实也已经改好了

所以说我们直接看这个文件就可以了

因为目前来说

这两个文件是完全一致的

你看在这呢

我们是不是配置了两个server对吧

然后呢

ID username password

其实用的是一个

用的是一样的

一个是release

一个是snapshots对吧

release呢

代表的就是发布版对吧

这个就是快照版

然后用户名密码

那么这个不要写错了

不要写错了

然后接下来呢

我们是不是配置这个镜像对吧

配置这个镜像

然后这是镜像的地址

这个私服呢

我们其实使用的是什么呢

使用的是阿里云

阿里云给我们提供的云效服务

用到他的云效服务

来搭建了我们这个Maven私服

但这块大家不用关心

你就按照我们这个配置

配置上之后呢

那么就能够成功的下载到

我们这两个夹包了

好

咱们来看一下

具体配置啊

你看上面要配置镜像

然后呢

下面呢就要配置这个私服了

通过profile对吧

这个标签

然后配置有central对吧

central你看

它其实是Maven的阿里云

这个地址对吧

然后呢

还有snapshots

还有这个什么呢

release

还有这个snapshots

然后呢

这是插件的仓库

插件的仓库

上面写法是一样的

把这堆配置上

然后最后呢

需要激活对吧

激活这个私服

通过activeprofiles

然后呢

激活我们上面这个nexus

这个nexus呢

对应的其实就是我们上面这个ID

所以大家呢

这些配置

大家不要自己去手敲啊

没有什么意义

所以说呢

你就直接把我们这个配置

原封不动的复制到你本地的那个Maven

这个settings文件里面去

这个配置文件当中去

就可以用了

配置完了之后啊

配置完了之后呢

我们再把这两个坐标

怎么做呢

再把这两个坐标复制一下

复制

然后呢

复制到比如说我当前这个PDU的

我PDU的这个微服务里边呢

后边会用到这两个坐标

对吧

然后呢

我就把它直接粘贴在这个位置就可以了

保存一下

你看这的话稍等一下

他其实是正在下载的吧

然后呢

我们可以去看一下

看看他能不能这个下载成功啊

能不能下载成功

咱们可以在这啊

手动的让他刷新一下

强制让他来看看能不能下载

好

从这边来刷新一下

然后呢

找到我们这个PDU的

你看他现在是报错

对吧

现在是报错

稍等一下

现在呢

应该是这个版本没有找到

对吧

他不知道版本号

然后呢

我们来看一下这个版本号

好像是没有锁定的吧

没有指定

没有指定的话呢

我们可以在这来指定一下

Version应该是1.0.0

同理

下面这个也是啊

需要来指定一下这个版本

然后呢

我们可以把这个讲义呢

来简单修改一下

再加上版本号

这样就没有问题了

然后呢

我回到ID这边来看

重新刷新一下

稍等一下

你看现在他是不是就已经这个下载成功了啊

下载成功了

然后呢

他会下载的什么位置呢

肯定是下载我本地的Maven仓库啊

好

这样他就已经下载好了

这个地方呢

他之所以能够下载成功

就是因为什么呢

就是因为我在这个

我这个Settings文件里边呢

提前已经

提前已经配置好这个私服了

如果说你没有配置这个私服的话呢

他肯定是无法下载成功的

因为没有这个私服的话呢

他只能到Maven的中央仓库去下载

而中央仓库里面是不可能有这个架包的

对吧

这是我们通用权益系统里边的两个架包

所以我们在这呢

就需要这样来配置一下就可以了

配置完之后呢

他就可以正常的把我们这两个坐标给下载到了

好

这是我们最后这一步啊

大家按照我们这个讲义呢

来操作一下就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”的技术课程，主要讲解如何为项目中的 `pd-user` 模块配置 Maven 依赖。讲师首先介绍了项目整体架构，然后重点演示了如何在 `pom.xml` 文件中添加自定义的、非标准的 Maven 依赖（如 `pd-auth-entity` 和 `pd-auth-api`），并说明了由于这些依赖未在中央仓库中，需要通过修改本地 Maven 的 `settings.xml` 文件来配置私有仓库，以确保项目能够成功构建。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示项目整体架构图，包含 `pd-user`, `pd-base`, `pd-work` 等多个服务模块。
*   **00:00:05 - 00:00:15**: 讲师切换到 `pom.xml` 文件，开始讲解 `pd-user` 模块的依赖配置。
*   **00:00:15 - 00:00:30**: 讲师在 `pom.xml` 中添加了 `pd-auth-entity` 和 `pd-auth-api` 两个依赖项。
*   **00:00:30 - 00:00:45**: 讲师解释，这两个依赖项没有在 Maven 中央仓库，需要配置私有仓库。
*   **00:00:45 - 00:01:00**: 讲师切换到 `settings.xml` 文件，演示如何配置私有仓库的镜像和 profile。
*   **00:01:00 - 00:01:15**: 讲师在 `settings.xml` 中配置了 `rd` 和 `rdd` 两个仓库的镜像地址。
*   **00:01:15 - 00:01:30**: 讲师在 `settings.xml` 中配置了 `activeProfiles`，确保在构建时使用私有仓库。
*   **00:01:30 - 00:01:45**: 讲师回到 `pom.xml`，展示最终的依赖配置，并强调了版本号的管理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   项目架构图：展示了 `pd-user`, `pd-base`, `pd-work`, `pd-druid`, `pd-redis`, `pd-aggregation` 等模块。
    *   课程大纲：列出了“第1章 项目概述和环境搭建”、“第5章 搭建TMS项目开发环境”等章节。
    *   文档路径：`我的电脑 > LENOVO (D:) > work > libs > apache-maven-3.5.4 > conf`。

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>com.iteima</groupId>
            <artifactId>pd-auth-entity</artifactId>
            <version>1.0.0</version>
        </dependency>
        <dependency>
            <groupId>com.iteima</groupId>
            <artifactId>pd-auth-api</artifactId>
            <version>1.0.0</version>
        </dependency>
        ```
    *   **`settings.xml` 配置**:
        ```xml
        <localRepository>D:/repository_boot/localRepository</localRepository>
        <mirror>
            <id>aliyun</id>
            <mirrorOf>central</mirrorOf>
            <name>阿里云公共仓库</name>
            <url>https://maven.aliyun.com/repository/public</url>
        </mirror>
        <profile>
            <id>rd</id>
            <repositories>
                <repository>
                    <id>central</id>
                    <name>阿里云公共仓库</name>
                    <url>https://maven.aliyun.com/repository/public</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                    </snapshots>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>rd-releases</id>
                    <url>https://maven.aliyun.com/repository/330518-release</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>false</enabled>
                    </snapshots>
                </pluginRepository>
                <pluginRepository>
                    <id>rd-snapshots</id>
                    <url>https://maven.aliyun.com/repository/330518-snapshot</url>
                    <releases>
                        <enabled>false</enabled>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                    </snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
        <activeProfiles>
            <activeProfile>rd</activeProfile>
        </activeProfiles>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目架构展示 (00:00:00-00:00:05)**:
    *   讲师在屏幕上展示了项目架构图，图中清晰地列出了 `pd-user`, `pd-base`, `pd-work`, `pd-druid`, `pd-redis`, `pd-aggregation` 等服务模块，帮助观众理解项目的整体结构。

*   **场景二：依赖配置演示 (00:00:15-00:00:30)**:
    *   讲师在 IntelliJ IDEA 中打开 `pd-user` 模块的 `pom.xml` 文件。
    *   讲师在 `<dependencies>` 标签内，依次添加了 `pd-auth-entity` 和 `pd-auth-api` 两个依赖项，并设置了版本号 `1.0.0`。
    *   讲师强调，这些依赖项是项目自定义的，需要特殊配置才能被 Maven 正确解析。

*   **场景三：私有仓库配置 (00:00:45-00:01:15)**:
    *   讲师切换到 `settings.xml` 文件，演示如何配置私有仓库。
    *   讲师在 `<mirrors>` 部分添加了阿里云的镜像配置，以加速依赖下载。
    *   讲师在 `<profiles>` 部分创建了一个名为 `rd` 的 profile，并配置了 `central`、`releases` 和 `snapshots` 仓库的地址。
    *   讲师在 `<activeProfiles>` 部分激活了 `rd` profile，确保在构建时使用私有仓库。

*   **场景四：最终配置与总结 (00:01:30-00:01:45)**:
    *   讲师回到 `pom.xml`，展示最终的依赖配置。
    *   讲师总结了整个配置过程，强调了通过配置 `settings.xml` 文件，可以成功管理非标准的 Maven 依赖，从而确保项目的顺利构建。
