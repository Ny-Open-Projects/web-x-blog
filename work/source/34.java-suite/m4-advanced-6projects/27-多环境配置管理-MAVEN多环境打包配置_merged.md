# 27-多环境配置管理-MAVEN多环境打包配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就来实现多环境的版本打包配置

咱们首先要去修改POM文件

增加下面的配置信息

以及打包的插件配置信息

那么咱们先将本地配置的多环境版本信息加入进去

放到咱们的POM文件下面

这个放在Depensys标签下面

注意它的顺序

它的意思是什么呢

在这里面这个是多环境的配置标签

那么我们可以看到它有多个版本的环境配置

像DEV的话有DEV的配置信息

BlockDuck有BlockDuck的配置信息

那么咱们可以看到它下面有个ID

然后有个Activation

Activation它是指激活的配置

这个我们可以看到

Modern的激活配置就是采用DEV的配置版本

然后下面呢

是它的属性配置

这个属性配置我们可以看到它对应的是什么呢

对应的就是咱们在Modern的配置文件当中

所采用的环境变量

这个呢和咱们Mave里面是对应的

那么通过Mave打包的时候呢

它就可以知道DEV下面呢

它要读取的指定版本呢

就是DEV

然后呢UAT也是同样的

进入到UAT的打包配置的时候呢

如果它的Profile配置的是UAT呢

那么它就会读取的配置版本呢

那么它就会读取的配置版本呢

那么它就会读取的配置版本呢

那么它就会读取的配置版本呢

那么它就会读取UAT的配置

这个呢是Profile标签的一个作用

多环境的版本配置管理

实现完多环境版本配置管理之后呢

咱们还加上U的构建的配置信息

我们呢先将它拷贝进来

那我们看一下它是如何去构建配置呢

在这里呢是Final Name

打包之后的名称

然后呢是它的插件

下面的话呢

是一些具体的配置

比如像你这边的CoffeeResource

将Resource里面的静态资源呢

打包进去

然后的话呢

像Java里面它的Xmail的配置

这个的话呢

也要打包进去

好我们看下它的打包插件

采用了ServinBoot Maven的插件

这个呢一定要加上

这样呢它才能实现ServinBoot多环境版本

打包的功能

好这个呢就是Build它整个的一个构建配置

我们加上注释

ServinBoot多环境

打包构建配置

接下来呢咱们就看一下如何去实现打包呢

打包之后它会在Touch的下面呢

生成可执行价

这个价的话呢目前没有对不对

那么呢咱们就来做一个配置实现

打开Maven师徒窗口

然后呢找到咱们的用户服务工程

在下面呢我们点击右键

在Live Circle下面点击右键

然后呢Create FastTalk User

点击这个命令

好

那咱们可以看到Command Line下面呢

可以去输入自己定义的命令对不对

我们呢就先以打包一个UAD环境来做测试

命令的话呢是Clean

Install

然后呢这个P就是指定你Profile的版本

这个话我们指定为UAT

这个Profile呢就是咱们在这里面所定义的对不对

如果说你指定的是UAT呢

那么它就会读取这里面的配置

那么咱们呢就来运行一下

找到刚才所创建的命令

在Run Configurations下面

我们右键Run运行

好

大家注意观察呢

它举的目录下面

好

正在打包执行过程当中

我们可以看到

它举的目录下面呢

已经生成了咱们打包之后的可执行价

对不对

这个价的话呢

跟咱们在这里所配置指定的环境版本呢

是一致的

是Talker User UAT

这个呢也是UAT环境

这个环境配置呢

它到底有没有读取成功呢

那么咱们可以从架包里面呢

去查看一下

我们点击Boot INF目录

然后我们找到了

默认了配置文件

看一下呢

它的值到底是指向的DV还是UAT

点击查看文件

它的值呢

是指向的UAT对不对

跟咱们呢

刚才打包配置的版本呢

是一致的

那么咱们还可以再测试一下

看一下DV的话呢

能否打包成功呢

这个话呢

就是对多版本呢

全面的一个验证

那咱们呢

再按刚才的方法

重新给大家演示一遍

加上呢

对整体的运用和理解

那在这里呢

输入Clean Install-P

指定环境版本

我们呢

这时候就指定为DV

OK

好

好呢

可以看到

在这里呢

又生成了一个可以执行的命令

好

打包呢

已经成功

咱们看一下它举的目录下面

可以看到

它举的目录下面呢

就已经生成了一个Stalk User

DV的可执行加包

这个呢

跟咱们命令当中所配置的版本呢

是一致的

对不对

我们呢

继续来验证一下

我们查看它的默认配置文件

看它指向的到底是哪个环境版本

好

可以看到

这个时候呢

它的环境版本就指向的是DV

对不对

这样呢

咱们就通过Maven的命令呢

去实现了多环境版本的打包配置

好

最后呢

咱们再来看一下

如果是在咱们打包的过程当中呢

出现打包失败的情况呢

我们要根据Maven的错误提示

检查所有的依赖组件呢

它是否已经执行Clean Instal

要确保这些依赖组件呢

是最新的

没有依赖方面的问题

在打包之前呢

最好就是将所有的模块都编译打包一遍

那么怎么去打包呢

就在咱们Bus Talk

最上面的根据目录

最上面的复制工程当中

然后呢

去选中Clean和Install

进行一个打包

好

这样呢

就是确保咱们所依赖的组件呢

都是最新的

避免呢

在编译过程当中

出现组件依赖

或者冲突等方面问题

好

在这里呢

咱们就实现了

多环境的Maven打包的一个管理配置

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于 **Spring Boot 多环境打包配置**。讲师通过实际操作演示了如何在 Maven 项目中配置多环境（如开发 `dev`、用户验收测试 `uat`、生产 `prd`）的打包策略。核心内容包括：
*   **在 `pom.xml` 中定义 Maven Profiles**：为不同环境设置激活条件和自定义属性。
*   **配置 `bootstrap.yml` 文件**：通过 `spring.profiles.active` 属性指定当前激活的环境。
*   **使用 Maven 插件实现环境特定的打包**：通过 `maven-resources-plugin` 和 `spring-boot-maven-plugin`，在打包时根据激活的环境变量（如 `${package.environment}`）动态修改最终的 JAR 文件名和资源文件内容。
*   **演示打包流程**：通过修改配置文件激活不同环境，然后执行 Maven `clean install` 命令，最终生成对应环境的 JAR 包（如 `stock-user-dev.jar`）。

整个过程旨在解决在不同部署环境中，如何让应用自动加载对应配置并生成相应包的问题，避免了手动修改和部署的繁琐。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，讲师在 Typora 中展示课程大纲，明确本节主题为“3.4 多环境打包配置”。
*   **00:05 - 00:15**: 讲师在 IDE 中打开 `pom.xml` 文件，开始讲解如何通过 Maven Profiles 来管理不同环境。
*   **00:15 - 00:30**: 讲师在 `pom.xml` 中添加 `profiles` 配置，定义 `dev` 和 `uat` 两个环境，并设置 `activeByDefault` 为 `true`，使 `dev` 环境默认激活。
*   **00:30 - 00:45**: 讲师切换到 `bootstrap.yml` 文件，演示如何通过 `spring.profiles.active: dev` 来激活 `dev` 环境。
*   **00:45 - 01:00**: 讲师在 `pom.xml` 中配置 `spring-boot-maven-plugin` 插件，设置 `finalName` 为 `${package.environment}`，以便打包时自动生成带环境标识的 JAR 文件名。
*   **01:00 - 01:15**: 讲师在 `pom.xml` 中配置 `maven-resources-plugin` 插件，设置 `filtering` 为 `true`，以便在打包时根据激活的环境变量替换资源文件中的占位符。
*   **01:15 - 01:30**: 讲师在 `bootstrap-dev.yml` 和 `bootstrap-uat.yml` 文件中分别配置了 `dev` 和 `uat` 环境的特定属性（如 `server.addr`）。
*   **01:30 - 01:45**: 讲师在 IDE 中创建并配置了 Maven 的 `clean install` 任务，用于执行打包。
*   **01:45 - 02:00**: 讲师执行 `clean install` 命令，IDE 控制台显示打包成功，并在 `target` 目录下生成了 `stock-user-dev.jar` 文件。
*   **02:00 - 02:15**: 讲师在 Typora 中总结，强调了多环境打包配置的核心思想和操作步骤。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.4 多环境打包配置”。
    *   **总结页**: “如果打包失败，根据 maven 错误提示，检查所有依赖的组件是否已执行 clean install，在打包之前，最好将所有模块都编译打包一遍，在顶级工程下面，执行 clean install 命令进行打包，避免编译过程中，出现的组件依赖问题。”

*   **代码关键内容**:

    *   **`pom.xml` 中的 Maven Profiles 配置**:
        ```xml
        <profiles>
            <profile>
                <id>dev</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
                <properties>
                    <package.environment>dev</package.environment>
                </properties>
            </profile>
            <profile>
                <id>uat</id>
                <properties>
                    <package.environment>uat</package.environment>
                </properties>
            </profile>
        </profiles>
        ```

    *   **`bootstrap.yml` 中的环境激活配置**:
        ```yaml
        spring:
          profiles:
            active: dev
        ```

    *   **`pom.xml` 中的 `spring-boot-maven-plugin` 配置**:
        ```xml
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <mainClass>com.icitcast.bulls.stock.user.StockUserApplication</mainClass>
                <jvmArguments>
                    <jvmArgument>-Dspring.profiles.active=${package.environment}</jvmArgument>
                </jvmArguments>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        ```

    *   **`pom.xml` 中的 `maven-resources-plugin` 配置**:
        ```xml
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-resources-plugin</artifactId>
            <version>${maven-resources-plugin.version}</version>
            <configuration>
                <encoding>UTF-8</encoding>
                <useDefaultDelimiters>true</useDefaultDelimiters>
                <filtering>true</filtering>
            </configuration>
            <executions>
                <execution>
                    <phase>process-resources</phase>
                    <goals>
                        <goal>resources</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        ```

    *   **`bootstrap-dev.yml` 和 `bootstrap-uat.yml` 中的环境配置**:
        ```yaml
        # bootstrap-dev.yml
        server:
          addr: 127.0.0.1:8080

        # bootstrap-uat.yml
        server:
          addr: 192.168.11.1:8080
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置 Maven Profiles** (00:15 - 00:30)
    *   讲师在 IntelliJ IDEA 中打开 `pom.xml` 文件。
    *   通过鼠标选中并编辑 XML 代码，添加了 `profiles` 标签，并在其中定义了 `dev` 和 `uat` 两个 profile。
    *   在 `dev` profile 中，设置了 `activeByDefault` 为 `true`，确保项目默认使用开发环境。
    *   在每个 profile 的 `properties` 标签内，定义了名为 `package.environment` 的属性，并分别赋值为 `dev` 和 `uat`。

*   **场景二：配置 `bootstrap.yml`** (00:30 - 00:45)
    *   讲师切换到 `bootstrap.yml` 文件。
    *   在文件中添加了 `spring.profiles.active: dev` 行，用于激活 `dev` 环境。
    *   讲师在 `bootstrap-dev.yml` 和 `bootstrap-uat.yml` 文件中分别配置了 `dev` 和 `uat` 环境的特定属性（如 `server.addr`）。

*   **场景三：配置 Maven 插件** (00:45 - 01:15)
    *   讲师在 `pom.xml` 中添加了 `spring-boot-maven-plugin` 插件配置。
    *   在 `<configuration>` 标签内，设置了 `mainClass` 为应用的主类，并通过 `<jvmArguments>` 标签添加了 `-Dspring.profiles.active=${package.environment}` 参数，确保启动时加载正确的配置。
    *   讲师还添加了 `maven-resources-plugin` 插件配置，设置 `filtering` 为 `true`，以便在打包时根据激活的环境变量替换资源文件中的占位符。

*   **场景四：执行打包并验证** (01:30 - 02:00)
    *   讲师在 IDE 中创建并配置了 Maven 的 `clean install` 任务。
    *   讲师执行 `clean install` 命令，IDE 控制台显示打包成功。
    *   讲师在 `target` 目录下找到了生成的 `stock-user-dev.jar` 文件，证明打包过程成功完成。

*   **场景五：总结与最佳实践** (02:00 - 02
