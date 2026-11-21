# 31-代码生成器-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对第五章MyBattis Generate代码生成器的使用做个回顾与总结

同样的咱们看一下第五章的学习目标有哪些呢

第一我们要掌握MyBattis Generate代码生成器的配置及其它的使用方法

接着我们要掌握自定义注视扩展功能的实现

在这里我们通过一个自定义的注视生成器

然后实现了自定义的一个注视要求

如果是大家的话呢

有兴趣可以再去实现它的其他的扩展功能

比如还有我们自定义的一些Circle

自定义的一些方法

这些都可以按要求去做一个自定和实现

这样就可以实现一个自己去定义的代码生成器

最后咱们要掌握通过Maven插件形式去生成对应的代码

这样我们就使用起来会更加灵活

我们回顾一下整体的

讲解分析步骤是怎样的

首先咱们对MyBattis Generate做了一个简要的说明

它是一个怎样的工具

它能够发挥怎样的功能

帮助我们去简化代码的一个实现

接着的话咱们要创建对应的MyBattis Generate的工程

然后针对于它的一个集成配置做了一个使用说明

以及我们如何去通过Maven插件的形式生成对应的代码

那么插件形式生成跟我们正常的这种方式生成会有些不一样

大家要注意它的一个插件依赖关系一定要配置正确

同时的话在我们代码实现当中

我们配置一定要注意它的一个路径

这个路径的话它就叫Project

在这里我们也做了一个说明和讲解

那就在问读者下面的话

我们要注意这个目录它的相对路径该怎么去定义

不同的使用方法

它的目录的方法应该怎么去定义

这种路径写法是不一样的

这点大家要仔细的注意

最后咱们再来总结一下

在工作当中

我们经常会碰到CRUD的增长改达功能

掌握MyBattis Generate代码生成器的使用

就能够简化我们的开发工作量

能够把更多的精力放在核心业务的实现上面

如果说我们经常碰到这种增长改达的操作

我们就可以采用这个

MyBattis Generate代码生成器

像这种实体的编写

这种属性的定义

就能节省我们很多的时间

我们可以把更多的精力放在核心业务当中

MyBattis Generate它支持很多的自定义配置

如果说默论的模板它不能满足要求

就可以参照我们自定义注释的一个功能

在这里只是简要的抛砖引玉

大家有兴趣

有时间经历的话

可以再多去研究和扩展

实现了不同的功能

甚至我们就可以修改它的源码

做成一个个性化的代码生成器

这样的话

就可以根据你的实际需要

生成了你所想要的代码

好

这一讲就是MyBattis Generate代码生成器的一个使用讲解

这讲我们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频课程为“第5章 MyBatis Generator代码生成器”，旨在教授学员如何使用 MyBatis Generator 工具来自动化生成数据库对应的 Java 实体类、Mapper 接口及 XML 映射文件，从而简化 CRUD 操作的开发工作。课程内容涵盖了工具的基本介绍、通过 Maven 项目配置文件（`pom.xml`）进行配置、以及通过 Maven 插件形式进行代码生成的两种主要方法。视频通过 PPT 讲解和实际代码演示相结合的方式，详细说明了配置文件的结构、依赖项的添加、以及生成过程中的注意事项和自定义扩展功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，明确本章主题为“第5章 MyBatis Generator代码生成器”。
*   **00:05 - 00:15**: 讲解本章“目标”，即掌握 MyBatis Generator 的配置、自定义扩展及 Maven 插件形式的使用。
*   **00:15 - 00:30**: 讲解“步骤”，包括 MyBatis Generator 说明、创建专用工程、配置使用和插件使用。
*   **00:30 - 00:45**: 进入“实现”部分，首先介绍 MyBatis Generator 是一个自动代码生成工具，能自动生成实体、Mapper 接口和 XML 文件。
*   **00:45 - 01:00**: 讲解“3.2 创建工程”，展示项目结构，包括 `java`、`resources` 和 `test` 目录。
*   **01:00 - 01:15**: 讲解“3.3 使用说明”，展示 `pom.xml` 文件中需要添加的依赖项，包括 MySQL 驱动和 MyBatis Generator 依赖。
*   **01:15 - 01:30**: 讲解“3.4 通过MAVEN插件形式生成”，展示在 `pom.xml` 中配置 Maven 插件的代码。
*   **01:30 - 01:45**: 展示 `generatorConfig.xml` 配置文件，说明如何通过该文件配置生成规则，如目标包名、数据库表名、是否生成 `@TableId` 等。
*   **01:45 - 02:00**: 演示运行 `GeneratorApplication` 类，展示生成的实体类和 Mapper 接口文件，以及控制台输出的警告信息。
*   **02:00 - 02:15**: 总结本章内容，强调 MyBatis Generator 的强大自定义能力，可以修改源码以满足个性化需求。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “第5章 MyBatis Generator代码生成器”。
    *   **目标**: 掌握配置、自定义扩展、Maven 插件形式生成。
    *   **步骤**: MyBatis Generator 说明、创建工程、配置使用、插件使用。
    *   **实现**: 说明、创建工程、使用说明、通过 Maven 插件形式生成。
    *   **总结**: 简化开发工作，支持自定义配置，可修改源码。

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependencies>
            <!-- Mysql数据库驱动包 -->
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>8.0.14</version>
            </dependency>
            <dependency>
                <groupId>com.itcast.trade</groupId>
                <artifactId>mybatis-generator</artifactId>
                <version>1.0-SNAPSHOT</version>
            </dependency>
        </dependencies>
        ```
    *   **`pom.xml` Maven 插件配置**:
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
                    <dependencies>
                        <dependency>
                            <groupId>mysql</groupId>
                            <artifactId>mysql-connector-java</artifactId>
                            <version>8.0.14</version>
                        </dependency>
                        <dependency>
                            <groupId>com.itcast.trade</groupId>
                            <artifactId>mybatis-generator</artifactId>
                            <version>1.0-SNAPSHOT</version>
                        </dependency>
                    </dependencies>
                </plugin>
            </plugins>
        </build>
        ```
    *   **`generatorConfig.xml` 配置文件**:
        ```xml
        <generatorConfiguration>
            <context id="DB2Tables" targetRuntime="MyBatis3">
                <jdbcConnection connectionURL="jdbc:mysql://localhost:3306/your_database" driverClass="com.mysql.cj.jdbc.Driver" userId="your_username" password="your_password"/>
                <javaTypeResolver>
                    <property name="forceBigDecimals" value="false"/>
                </javaTypeResolver>
                <javaModelGenerator targetPackage="com.itcast.trade.entity" targetProject="src/main/java">
                    <property name="enableSubPackages" value="true"/>
                </javaModelGenerator>
                <sqlMapGenerator targetPackage="com.itcast.trade.mapper" targetProject="src/main/resources">
                    <property name="enableSubPackages" value="true"/>
                </sqlMapGenerator>
                <javaClientGenerator type="XMLMAPPER" targetPackage="com.itcast.trade.dao" targetProject="output">
                    <property name="enableSubPackages" value="true"/>
                </javaClientGenerator>
                <table tableName="t_trade_user" enableCountByExample="false" enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false" useActualColumnNames="true">
                    <generatedKey column="id" sqlStatement="JDBC" identity="true"/>
                </table>
            </context>
        </generatorConfiguration>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (00:45)
    *   **描述**: 展示一个名为 `mybatis-generator` 的 Maven 项目结构，包含 `src/main/java`、`src/main/resources` 和 `test` 目录。重点突出 `resources` 目录下的 `generatorConfig.xml` 文件，这是配置生成规则的核心文件。

*   **场景二：`pom.xml` 依赖配置演示** (01:00)
    *   **描述**: 在 `pom.xml` 文件中，演示如何添加 MySQL 数据库驱动和自定义的 MyBatis Generator 依赖。通过高亮显示代码，强调 `groupId`、`artifactId` 和 `version` 的重要性。

*   **场景三：Maven 插件配置演示** (01:15)
    *   **描述**: 在 `pom.xml` 的 `<build>` 标签内，演示如何配置 `mybatis-generator-maven-plugin` 插件。通过代码高亮，展示插件的 `<groupId>`、`<artifactId>`、`<version>` 以及 `<configuration>` 中的 `<verbose>` 和 `<overwrite>` 属性。

*   **场景四：`generatorConfig.xml` 配置文件演示** (01:30)
    *   **描述**: 展示 `generatorConfig.xml` 文件的内容，详细讲解其中的 `<context>`、`<jdbcConnection>`、`<javaModelGenerator>`、`<sqlMapGenerator>` 和 `<javaClientGenerator>` 等标签的含义。通过高亮显示 `targetPackage` 和 `targetProject` 属性，说明生成文件的存放位置。

*   **场景五：代码生成运行演示** (01:45)
    *   **描述**: 在 IntelliJ IDEA 中，运行 `GeneratorApplication` 类。演示程序成功执行后，控制台输出的警告信息，如“Column LOW_VARCHAR_FIELD... does not exist in the table”和“Existing file... was overwritten”。同时，展示生成的实体类文件（如 `TradeUser.java`）和 Mapper 接口文件（如 `TradeUserMapper.java`）已成功创建在 `target` 目录下。

*   **场景六：总结与展望** (02:00)
    *   **描述**: 课程最后，总结 MyBatis Generator 的核心价值：简化开发、支持自定义配置、可修改源码。强调其在实际项目中的应用，鼓励学员动手实践，掌握其强大功能。
