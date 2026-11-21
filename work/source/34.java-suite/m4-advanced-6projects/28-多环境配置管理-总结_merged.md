# 28-多环境配置管理-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们再对第三章内容做一个回顾和总结

我们首先要了解和掌握第三章的学习目标

在这里我们要去掌握SplitBoot多环境的打包配置

如何去实现Maven的打包和发布

我们来回顾一下整体的讲解内容有哪些

首先咱们对SplitBoot多环境配置做了一个简要介绍

为什么会采用SplitBoot多环境版本配置

它的一个主要作用

然后咱们通过本章的学习

可以去加深多环境配置的理解和运用

后续可以通过配置中心方式

去实现了生产级的统一配置集成实现方案

再往下面咱们就讲解了SplitBoot本地化多环境配置的具体规则

如何去管理不同环境之间怎么去配置和使用

在这里可以通过默认的

配置文件形式去指定具体的环境版本

也可以通过参数变量的形式去指定

接着咱们就通过本地的开发环境做了一个配置和使用

然后去启动了用户服务

给大家做了一个测试和验证

最后咱们就通过Maven实现了多环境的打包配置

在这里该怎么去配置

Profile的一个主要的作用

这些大家要理解清楚

然后是Builder的一个构建配置

好

最后呢

咱们再来通过Maven构建的时候

要注意整个运行的过程

不要包出错误

如果是有Maven的错误提示

最好在顶级工程下面

将所有的模块进行一个重新打包

避免编译过程当中出现了有些依赖问题

最后咱们再来总结一下

如果要打包生产环境的运行包

按照上面的配置

我们再建立一个名为ProDuck的配置文件就可以了

再创建一个顶级工程

再一个名为PRD的Profile配置

以及对应的Bootstrap ProDuck的YAM配置文件

通过Maven执行命令

就可以实现了生产环境的打包配置

通过这种方式开发完成后

我们不再需要去反复修改配置文件

对不对

每个环境可以去独立维护一套自身的配置文件

不会因为交叉产生的冲突或者是配置修改错误的问题

便于咱们开发的管理

在实际项目当中往往是多人协作

对不对

负责不同的模块进行开发

在打包发布的时候

我们最好要加上一个什么

Deploy命令

因为我们在项目实际运动当中

往往都会有一个统一的中央仓库

对吧

那么每个人负责了不同模块

可能每个人本地的代码并不是最新的

所以我们在打包更新的时候

要将生成后的架包发布到中央仓库当中

这个命令

如何编写呢

就通过clean install deploy-p uat

最主要的就加上deploy这个命令就可以了

这个命令的主要作用

是不仅会安装到本地的卖尾仓库当中

我们还会发布到远程的中央统一卖尾仓库当中

保证每个人生成的都是最新的包

集成和使用了最新的版本功能

如果说你仅仅只是通过clean install

你只会将本地的仓库进行分析

并不会将远程仓库分析

那么别人要进行打包的时候

可能拿到的还是你之前的版本

所以这点大家要注意一下

好

大家有时间的话

可以再去扩展一下生产环境版本的配置实现

以及通过deploy命令去实现了Maven的打包和发布

那在这里呢

就是对第三章内容的回顾与总结

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频课程讲解了 **Spring Boot 多环境配置与打包发布** 的完整流程。讲师通过一个名为 `stock-user` 的项目，演示了如何为开发（dev）、测试集成（uat）和生产（prd）三个环境分别配置独立的配置文件，并通过 Maven 的 Profile 机制实现环境切换和打包。核心内容包括：多环境配置文件的命名规则、`bootstrap.yml` 中通过 Maven 变量动态指定激活环境、在 `pom.xml` 中定义 Maven Profile 以控制打包产物名称和构建过程、以及如何执行打包命令并验证成功。最后，讲师总结了该方案在实际项目中的优势，即环境隔离、配置独立、便于团队协作和发布。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，明确本章主题为“第3章 Spring Boot 多环境配置与打包发布”。
*   **00:00:05 - 00:00:15**：讲解“目标”，即掌握 Spring Boot 多环境配置与打包发布。
*   **00:00:15 - 00:00:30**：讲解“步骤”，包括多环境配置介绍、配置规则、本地开发环境使用和打包配置实现。
*   **00:00:30 - 00:00:45**：进入“实现”部分，首先讲解“3.1 Spring Boot 多环境配置介绍”，说明项目中不同环境（如 dev, uat, prd）需要不同的配置。
*   **00:00:45 - 00:01:00**：讲解“3.2 Spring Boot 多配置规则”，介绍配置文件的命名规范（`application-{profile}.properties`）和默认配置文件 `application.properties` 的作用。
*   **00:01:00 - 00:01:15**：讲解“3.3 本地的开发环境配置使用”，展示项目目录结构，说明 `bootstrap.yml` 中通过 `${package.environment}` 变量动态指定激活的环境。
*   **00:01:15 - 00:01:30**：讲解“3.4 多环境打包配置”，演示如何在 `pom.xml` 中定义 Maven Profile，为不同环境设置不同的打包名称。
*   **00:01:30 - 00:01:45**：演示如何执行 Maven 打包命令，通过右键菜单选择 `Create 'stock-user' [clean]...`。
*   **00:01:45 - 00:02:00**：展示打包成功后的结果，包括生成的 `target` 目录和 `stock-user-xxx.jar` 文件。
*   **00:02:00 - 00:02:15**：进入“4. 总结”部分，总结整个方案的优势，并给出在多人协作项目中常用的发布命令 `clean install deploy -P uat`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`第3章 Spring Boot 多环境配置与打包发布`。
    *   **目标**：`掌握Spring Boot 多环境配置与打包发布`。
    *   **步骤**：`Spring Boot 多环境配置介绍`、`Spring Boot 多环境配置规则`、`本地的开发环境配置使用`、`多环境打包配置实现`。
    *   **总结**：`如果要打包生产环境的运行包，按照上面配置，再建立一个名为prd的Profile 和对应的bootstrap-prd.yml配置文件，通过maven执行命令即可。通过这种方式，开发完成后，不再需要反复修改配置文件，每个环境维护独立一套配置文件，不会产生冲突错误，便于开发管理。`

*   **代码示例**：
    *   **`bootstrap.yml` 配置**：
        ```yaml
        spring:
          profiles:
            active: ${package.environment}
        ```
    *   **`pom.xml` 中的 Maven Profile 配置**：
        ```xml
        <profiles>
            <profile>
                <id>dev</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
            </profile>
            <profile>
                <id>prd</id>
                <properties>
                    <package.environment>prd</package.environment>
                </properties>
            </profile>
        </build>
        <finalName>stock-user-${package.environment}</finalName>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境配置介绍** (00:00:30)
    *   讲师在文档中指出，在项目开发中，不同环境（如 dev, uat, prd）需要不同的配置，如 Redis 地址、数据库连接等。
    *   为了解决这个问题，Spring Boot 提供了多环境配置功能，通过 `application-{profile}.properties` 文件来区分不同环境的配置。

*   **场景二：配置文件命名规则** (00:00:45)
    *   讲师在文档中列出 Spring Boot 支持的配置文件类型，如 `application.yml`、`application.properties`、`bootstrap.yml` 和 `bootstrap.properties`。
    *   强调多环境配置文件的命名必须符合 `application-{profile}.properties` 的格式，其中 `{profile}` 是环境标识，例如 `application-dev.properties` 代表开发环境。

*   **场景三：本地开发环境配置** (00:01:00)
    *   讲师展示项目目录结构，其中包含 `bootstrap.yml`、`bootstrap-dev.yml`、`bootstrap-uat.yml` 等文件。
    *   在 `bootstrap.yml` 中，通过 `spring.profiles.active: ${package.environment}` 设置默认激活的环境，其中 `${package.environment}` 是一个 Maven 变量。
    *   讲师指出，最新版的 IntelliJ IDEA 可以识别这个变量，但老版本可能无法识别，需要手动处理。

*   **场景四：多环境打包配置** (00:01:30)
    *   讲师在 `pom.xml` 中添加了 Maven Profile 配置。
    *   为 `dev` 环境定义了一个默认激活的 Profile。
    *   为 `prd` 环境定义了一个 Profile，并设置了 `package.environment` 属性为 `prd`。
    *   在 `<build>` 部分，通过 `<finalName>stock-user-${package.environment}</finalName>` 使打包后的文件名包含环境标识。

*   **场景五：执行打包命令** (00:01:45)
    *   讲师在 IDE 中右键点击项目 `stock-user`，选择 `Run Maven Build` 下的 `Create 'stock-user' [clean]...`。
    *   在弹出的对话框中，选择 `clean install -P uat` 命令进行打包。
    *   打包成功后，IDE 的项目视图中显示 `target` 目录，其中包含生成的 `stock-user-uat.jar` 文件。

*   **场景六：总结与发布命令** (00:02:00)
    *   讲师在文档中总结了本章内容，强调了该方案的优势：环境隔离、配置独立、便于团队协作。
    *   讲师给出一个在多人协作项目中常用的发布命令：`clean install deploy -P uat`。
    *   解释该命令的作用：不仅安装到本地 Maven 仓库，还会发布到远程 Maven 仓库，确保每个人生成的都是最新的包，集成的是最新版本功能。
