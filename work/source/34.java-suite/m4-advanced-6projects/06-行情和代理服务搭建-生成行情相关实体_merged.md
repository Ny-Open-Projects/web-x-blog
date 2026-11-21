# 06-行情和代理服务搭建-生成行情相关实体 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始生成行情服务相关的实体

咱们之前讲解过MyBattis Generator代码生成工程的使用

接着咱们就通过代码生成工程去创建了行情服务的实体

之前咱们讲解如何去连接MySQL MereDB数据库去生成实体

那么针对于Post回式口该如何去配置呢

那咱们来看一下

在这里咱们先将代码拷贝过去

将它的配置文件与source目标下面针对于PG Circle的配置

咱们先放在工程代码当中

打到MyBattis Generator

为了不跟之前的配置文件产生冲突

因为之前这一块是连接MereDB的

所以在这里咱们新建了一个配置文件

专门针对PG Circle去做的一个配置文件

那咱们具体来看一下

配置文件里面的配置内容

这个呢跟之前的配置呢没有太大的差别

针对JDBC的Connection连接配置信息呢

咱们要做相应的调整

因为在这里呢是要指向PG Circle

然后是它的用户名和密码信息

这个是它的驱动包

也要做相应的调整

那下面呢咱们就要去配置针对于行情的数据表

这一块呢是它的实体配置

然后这个是DAO的配置

这个呢是DAO Map文件

就是MyBatties主要使用到的XML的配置文件

下面呢就是具体的表映射配置

主要有三个表

一个呢是StoreKeylineK线数据表

一个是实时行情数据表

最后一个呢就是行情概要信息表

配置文件配置完成之后

咱们要加入PG Circle的驱动包

那从讲义当中

Copy进来

放在下面

这个版本呢咱们也要定义一下

相属性Copy

在复集工程当中

Properties标签下面

版本呢采用42.2.5

配置完成之后

让它导入生效

接着咱们再看一下

这个包呢就能正常找到

那下面呢我们就要去修改它的启动运行内

要指定了PG Circle的配置文件

这样呢它才会去读取咱们的PG Circle

配置生成相应的代码

原来的处理逻辑呢

不需要做过多调整

咱们只需要去修改它的配置文件

在大码当中呢

将启动内的配置文件路径

咱们要做一个调整

之前呢是指向的Generate

放这个配置文件

咱们要将它调整为PG Circle的配置文件

好

调整完成之后呢

咱们就可以进行一个运行测试

将AutoBoot下面的目录呢

先全部清除掉

那么右键让运行

查看一下它的运行结果

好

服务运行完成

咱们来看一下AutoBoot的输出目录

咱们可以发现

它已经生成了相关的DAO

以及呢实体代码文件

生成的代码呢

并非立即能够使用

咱们还要做相应的一个调整

然后呢再将它放到

Stock Nt的公用的实体工程下面

这些实体

细节方面的调整呢

在这里就不做过多的赘述

咱们将代码呢直接copy进来

这三个实体

一个是K线

实时行情

以及呢行情概要信息表

我们将它放到Stock Nt下面

在这里面我们创建一个BOW

Bow的行情

专门存放行情相关的实体

让它粘贴进去

创建完成之后呢

咱们要检查一下它的BOW路径是否正确

Com ID Cast Bar

Stock Nt

或者好

要确保这些实体所映射的表名称是正确的

以及呢相关的注解要加入进去

要检查一下

看这些属性是否跟咱们Circle里面的属性是一致的

将这些实体创建配置完成之后呢

咱们后面行情服务功能实现的时候还需要去使用到

在这里呢

咱们将必要的实体呢

先创建和配置好

那回到讲义当中

这一节呢

咱们对行情服务的相关信息表明呢

就是说我们的实体通过代码服务工程进行了配置和创建

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“交易平台 - Day 12”的一部分，主要讲解如何使用 MyBatis-Generator 工具为 PostgreSQL 数据库自动生成实体类和 Mapper 接口。课程内容聚焦于“生成行情服务的实体”这一子模块，通过配置文件 `generatorConfig_pgsql.xml` 来指定目标数据库、表名、包路径等参数，并演示了如何运行生成器程序 `GeneratorApplication` 来执行代码生成。视频中还展示了生成后的 Java 文件内容，并指出了因数据库表结构与配置不匹配而产生的警告信息。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程标题页，显示“交易平台 - Day 12”和“学习目标”。
*   **00:00:05 - 00:00:15**：进入“第2章 第三方行情接入”下的“3.4 生成行情服务的实体”章节，介绍本节目标。
*   **00:00:15 - 00:00:30**：展示项目结构，重点介绍 `mybatis-generator` 模块及其内部的 `generatorConfig.xml` 和 `generatorConfig_pgsql.xml` 配置文件。
*   **00:00:30 - 00:00:45**：在 `generatorConfig_pgsql.xml` 中，配置数据库连接信息（`<jdbcConnection>`）和 Java 类型解析器（`<javaTypeResolver>`）。
*   **00:00:45 - 00:01:00**：配置生成的 Java Model、SQL Map 和 Java Client 的目标包路径（`<javaModelGenerator>`, `<sqlMapGenerator>`, `<javaClientGenerator>`）。
*   **00:01:00 - 00:01:15**：配置具体的数据库表信息，包括 `table` 标签，指定 `schema` 和 `tableName`，并设置 `enableSelectByExample` 等属性。
*   **00:01:15 - 00:01:30**：展示 `pom.xml` 文件，确认项目依赖和模块结构。
*   **00:01:30 - 00:01:45**：展示 `GeneratorApplication.java` 的核心代码，包括配置解析器、生成器实例化和执行方法。
*   **00:01:45 - 00:02:00**：演示运行 `GeneratorApplication`，在控制台输出生成结果和警告信息。
*   **00:02:00 - 00:02:15**：展示生成的 Java 文件 `TradestockquotelastMapper.java`，并指出其中的警告信息（如 `DATE_FIELD`、`FRED`、`LONG_VARCHAR_FIELD` 等列在数据库中不存在）。
*   **00:02:15 - 00:02:30**：总结本节内容，强调配置文件 `generatorConfig_pgsql.xml` 的作用和注意事项。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   课程大纲：`第2章 第三方行情接入` -> `3.4 生成行情服务的实体`。
    *   学习目标：明确本节要实现的功能。
    *   项目结构图：展示了 `mybatis-generator` 模块下的 `src/main/java` 和 `src/main/resources` 目录结构。
    *   配置文件说明：强调 `generatorConfig_pgsql.xml` 与 `generatorConfig.xml` 的区别，以及需要调整的 `jdbcConnection` 和 `table` 标签信息。

*   **关键代码**：

    *   **`generatorConfig_pgsql.xml` 配置文件**：
        ```xml
        <jdbcConnection>
            <driverClass>org.postgresql.Driver</driverClass>
            <connectionURL>jdbc:postgresql://localhost:5432/office</connectionURL>
            <userId>postgres</userId>
            <password>123456</password>
        </jdbcConnection>

        <javaTypeResolver>
            <property name="forceBigDecimals" value="false" />
        </javaTypeResolver>

        <javaModelGenerator targetPackage="com.itcast.bulls.stock.entity" targetProject="mybatis-generator">
            <property name="enableSubPackages" value="true" />
            <property name="trimStrings" value="true" />
        </javaModelGenerator>

        <sqlMapGenerator targetPackage="com.itcast.bulls.stock.dao" targetProject="mybatis-generator">
            <property name="enableSubPackages" value="true" />
        </sqlMapGenerator>

        <javaClientGenerator type="XMLMAPPER" targetPackage="com.itcast.bulls.stock.dao" targetProject="mybatis-generator">
            <property name="enableSubPackages" value="true" />
        </javaClientGenerator>

        <table schema="office" tableName="t_trade_stock_quote_last" enableCountByExample="false">
            <property name="useActualColumnNames" value="true" />
            <generatedKey column="ID" sqlStatement="MySql" identity="true" />
            <dominantObjectRenamingRule searchString="T(*)" replaceString="$1" />
            <ignoreColumn column="DATE_FIELD" />
            <columnOverride column="LONG_VARCHAR_FIELD" jdbcType="VARCHAR" />
        </table>
        ```

    *   **`GeneratorApplication.java` 核心代码**：
        ```java
        public class GeneratorApplication {
            public static void main(String[] args) {
                // 记录生成过程中的警告信息
                List<String> warnings = new ArrayList<>();

                // 配置转换器
                ConfigurationParser cp = new ConfigurationParser(warnings);

                // 获取具体的代码生成配置
                Configuration config = cp.parseConfiguration(GeneratorApplication.class.getClassLoader().getResourceAsStream("generatorConfig_pgsql.xml"));

                // 回调方法
                DefaultShellCallback callback = new DefaultShellCallback(true);

                // 创建 MyBatis 生成器
                MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config, callback, warnings);

                try {
                    // 执行代码生成
                    myBatisGenerator.generate(null);

                    // 打印生成的警告信息
                    if (warnings.size() > 0) {
                        System.out.println("Warning Msg :");
                        for (String warn : warnings) {
                            System.out.println(warn);
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置文件定位** (00:00:15)
    *   **描述**：讲师在 IntelliJ IDEA 中打开项目，展示 `mybatis-generator` 模块的目录结构。重点指向 `src/main/resources` 目录下的 `generatorConfig.xml` 和 `generatorConfig_pgsql.xml` 文件，说明后者是为 PostgreSQL 数据库定制的配置文件。

*   **场景二：配置文件内容详解** (00:00:30 - 00:01:15)
    *   **描述**：讲师逐行讲解 `generatorConfig_pgsql.xml` 的内容。首先配置了 PostgreSQL 数据库的连接信息（`<jdbcConnection>`），然后配置了 Java 类型解析器（`<javaTypeResolver>`），接着配置了生成的 Java Model、SQL Map 和 Java Client 的包路径（`<javaModelGenerator>`, `<sqlMapGenerator>`, `<javaClientGenerator>`）。最后，通过 `<table>` 标签配置了具体的数据库表 `t_trade_stock_quote_last`，并设置了 `enableCountByExample`、`useActualColumnNames`、`generatedKey`、`dominantObjectRenamingRule`、`ignoreColumn` 和 `columnOverride` 等属性。

*   **场景三：运行生成器并查看结果** (00:01:45 - 00:02:15)
    *   **描述**：讲师在 IntelliJ IDEA 中运行 `GeneratorApplication` 类。程序执行后，在控制台输出了生成成功的提示和一系列警告信息。这些警告信息指出，配置文件中指定的 `DATE_FIELD`、`FRED`、`LONG_VARCHAR_FIELD` 等列在实际的数据库表中不存在，这表明配置与数据库结构存在不一致。讲师随后展示了生成的 Java 文件 `TradestockquotelastMapper.java`，并解释了这些警告信息的含义。

*   **场景四：总结与注意事项** (00:02:15)
    *   **描述**：讲师总结本节内容，强调 `generatorConfig_pgsql.xml` 文件的重要性。他提醒学员，在使用该配置文件时，必须确保其中的 `jdbcConnection` 和 `table` 标签中的信息与实际的数据库环境和表结构保持一致，否则会生成失败或产生警告。
