# 30-代码生成器-通过MAVEN插件生成 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们就来学习

如何通过Maven插件的形式

来生成对应的代码

除了上面的生成方式

咱们还可以通过Maven插件来生成

大家想想

在我们实际工作当中

经常要通过Maven这个命令

去进行工程的打包和配置

对不对

这样如果说我们每次

都通过启动内去生成

必须依赖于这个代码

然后去做对应的运行和配置

所以我们要更简便起见

可以通过Maven插件

来帮助我们去实现代码生成

那么怎么去做呢

这个要在Home插秒下面

增加以下的插件配置

好

这些插件配置咱们可以看一下

在MyBedisGenerator

Home下面

找到Build标签

在这里的话是要增加

MyBedisGenerator

Maven的一个插件

还有MyCircle的一个连接插件

以及MyBedisGenerator的

插件

然后再加一个Maven的一个插件

它的核心代码包

我们可以看到

这个代码包的话

为什么会去依赖到我们本地的工程呢

因为在这里面的话

我们是不是要添加它对应的相关的依赖

在这里面它有MyBedisGenerator的代码生成器

还有MyBedis

在这里面的话

指向它的一个依赖作用

它才能关联找到它所对应的这些依赖

如果说咱们不加上

在这里面的话

这些依赖它是不加上的

它是不能够自动关联和找到的

这一点大家要注意一下

好

那这个插件配置完成之后

咱们来看一下该怎么去使用

我们还记得之前

就上个章节

我们对这一块做了讲解和说明

对不对

如果是通过Maven Plugin的方式去生成的话

我们是不需要追加到它的工程名称的

它会自动找到对应的工程目录

然后以相对入境的方式

在下面去生成对应的代码

那我们在通过Maven插件生成之前

先将对应的这个Plugin的Project目录

做个调整和修改

我们做一个搜索提换

就全部将它替换一下

这样就已经替换完成

那我们将Output目录清空

Output目录也已经清空完成

这个时候我们就可以开始执行Maven

去生成对应代码

我们打开Maven视图

在这里面的话

我们找到MyBase捐给率

这个工程

然后注意在是在Plugin下面

下面找到MyBaseGenerator这个插件

看到下面有个Generator的命令

对不对

咱们去执行一下

让Maven Build

这个时候它就会去扫描

然后去做对应的代码生成

大家可以看到这里面报错了

对不对

因为它要去找到我们制定的注释实现器

也就是这个类

但是它的插件并没有找到

在这里面的话

它为什么没找到呢

我们要将它的代码重新打包一下

Maven

这样它就能够沿用我们最新的代码

让我们再重新执行一下刚才的插件

这个时候是不是看到执行成功了

对不对

我们看一下有没有输出我们所期望的内容

也可以看到一个JST

在这里面的话

它都生成了对应代码

让我们检查一下

在对应的目录里

确实是按照我们的预期

实际当中的配置生成了对应的代码

实体还有MAP

已经是我们的MAP文件

那通过Maven插件的方式

我们已经成功生成对应的代码

好

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程讲解了如何使用 MyBatis Generator 工具，通过 Maven 插件的形式，自动生成 Java 实体类（Entity）、数据访问对象（DAO）和映射文件（Mapper）。课程首先介绍了在 `pom.xml` 中配置 Maven 插件和依赖项，然后演示了如何编写配置文件 `generatorConfig.xml` 来定义生成规则，最后通过执行 Maven 的 `generate` 目标来完成代码的自动生成。课程还展示了生成过程中可能出现的错误（如自定义注解器无法实例化）以及如何解决。最终，课程总结了 MyBatis Generator 的价值，即通过自动化减少重复性开发工作，让开发者能更专注于核心业务逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程开始，展示当前正在讲解的章节“3.4 通过MAVEN插件形式生成”。
*   **00:00:05 - 00:00:15**：讲解在 `pom.xml` 中配置 Maven 插件和依赖项。
*   **00:00:15 - 00:00:30**：展示 `pom.xml` 中的插件配置和 MySQL 数据库驱动依赖。
*   **00:00:30 - 00:00:45**：展示自定义的 MyBatis Generator 插件依赖。
*   **00:00:45 - 00:01:00**：讲解 `generatorConfig.xml` 配置文件，定义目标包名、数据库表名和生成策略。
*   **00:01:00 - 00:01:15**：演示在 IntelliJ IDEA 中执行 Maven `generate` 命令。
*   **00:01:15 - 00:01:30**：展示生成过程中的错误信息（自定义注解器无法实例化）。
*   **00:01:30 - 00:01:45**：演示如何修复错误并成功执行生成。
*   **00:01:45 - 00:02:00**：展示生成成功的日志和生成的 Java 文件。
*   **00:02:00 - 00:02:15**：总结 MyBatis Generator 的优势和自定义能力。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.4 通过MAVEN插件形式生成`。
    *   **总结部分**：
        *   “在工作当中，经常会碰到CRUD的功能操作，掌握MyBatis Generator代码生成器使用，能够简化开发工作量，把更多的精力放在核心业务实现上。”
        *   “MyBatis Generator支持很多自定义配置，如果默认的模板不能够满足要求，可以参照自定义注释功能，实现不同需求，甚至可以修改源码，做成个性化的项目代码生成器。”

*   **代码关键内容**：

    *   **Maven 插件配置 (`pom.xml`)**：
        ```xml
        <build>
            <plugins>
                <plugin>
                    <groupId>org.mybatis.generator</groupId>
                    <artifactId>mybatis-generator-maven-plugin</artifactId>
                    <version>1.3.7</version>
                    <configuration>
                        <verbose>true</verbose>
                        <overwrite>true</overwrite>
                    </configuration>
                </plugin>
            </plugins>
        </build>
        ```

    *   **依赖项配置 (`pom.xml`)**：
        ```xml
        <dependencies>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>8.0.14</version>
            </dependency>
            <dependency>
                <groupId>com.icast.trade</groupId>
                <artifactId>mybatis-generator</artifactId>
                <version>1.0-SNAPSHOT</version>
            </dependency>
        </dependencies>
        ```

    *   **生成配置文件 (`generatorConfig.xml`)**：
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE generatorConfiguration
                PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
                "http://mybatis.org/dtd/mybatis-generator-config_1.0.dtd">

        <generatorConfiguration>
            <context id="DB2Tables" targetRuntime="MyBatis3">
                <jdbcConnection connectionURL="jdbc:mysql://localhost:3306/trade_stock"
                                driverClass="com.mysql.cj.jdbc.Driver"
                                userId="root"
                                password="123456">
                </jdbcConnection>

                <javaTypeResolver>
                    <property name="forceBigDecimals" value="false"/>
                </javaTypeResolver>

                <javaModelGenerator targetPackage="com.icast.trade.stock.entity"
                                    targetProject="output">
                    <property name="enableSubPackages" value="true"/>
                </javaModelGenerator>

                <sqlMapGenerator targetPackage="com.icast.trade.stock.mapper"
                                 targetProject="output">
                    <property name="enableSubPackages" value="true"/>
                </sqlMapGenerator>

                <javaClientGenerator type="XMLMAPPER"
                                    targetPackage="com.icast.trade.stock.dao"
                                    targetProject="output">
                    <property name="enableSubPackages" value="true"/>
                </javaClientGenerator>

                <table schema="trade_stock" tableName="t_trade_account">
                    <property name="useActualColumnNames" value="true"/>
                    <generatedKey column="ID" sqlStatement="MySql" identity="true"/>
                    <columnOverride column="DATE_FIELD" property="startDate"/>
                    <columnOverride column="LONG_VARCHAR_FIELD" jdbcType="VARCHAR"/>
                    <columnOverride column="FRED" />
                </table>
            </context>
        </generatorConfiguration>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置 Maven 插件**：讲师在 IDE 中打开 `pom.xml` 文件，通过鼠标选中并高亮显示了用于配置 MyBatis Generator Maven 插件的 XML 代码块，包括插件的 `groupId`、`artifactId` 和 `version`，以及 `configuration` 中的 `verbose` 和 `overwrite` 属性。

*   **场景二：配置数据库依赖**：讲师在 `pom.xml` 中添加了 MySQL 数据库驱动的依赖项，并高亮显示了 `groupId`、`artifactId` 和 `version`。

*   **场景三：配置自定义插件**：讲师添加了一个自定义的 MyBatis Generator 插件依赖，并高亮显示了其 `groupId`、`artifactId` 和 `version`。

*   **场景四：编写生成配置文件**：讲师在 `resources` 目录下创建并编辑 `generatorConfig.xml` 文件，高亮显示了 `context`、`jdbcConnection`、`javaModelGenerator`、`sqlMapGenerator`、`javaClientGenerator` 和 `table` 等关键配置元素，并展示了如何为特定表（如 `t_trade_account`）配置列的映射规则。

*   **场景五：执行生成命令**：讲师在 IntelliJ IDEA 的 Maven 插件面板中，右键点击 `mybatis-generator:generate` 目标，执行了生成操作。终端窗口显示了生成过程的日志，包括成功和错误信息。

*   **场景六：处理错误**：在执行生成时，终端显示了错误信息，指出自定义注解器 `CustomCommentGenerator` 无法实例化。讲师演示了如何修复此错误。

*   **场景七：查看生成结果**：讲师在 IDE 中打开了生成的 Java 文件（如 `TTradeAccount.java` 和 `TTradeAccountMapper.xml`），并高亮显示了文件中的注释和自动生成的代码，证明生成成功。

*   **场景八：课程总结**：讲师切换到 PPT 页面，高亮显示了课程的总结部分，强调了 MyBatis Generator 的价值和自定义能力。
