# 88-规则引擎Drools-Drools实战（保险产品准入 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是把我们这个实战案例啊,它的业务规则呢,介绍了一下,那接下来呢,我们就具体来实现一下,咱们这个案例呢,还是基于Supreme Boot整合DROCE这个架构呢,来实现,那首先我们肯定先是创建一个美文工程啊,这个工程呢,叫做Insurance InfoCheck,Inference呢,其实翻译过来就是保险的意思,对吧,这个叫做保险信息检查,大概是这么一个意思啊,

我们就按照这个名字来创建,咱们来创建一个新的Project,然后Next,这个位置不用改,直接完成,直接在当前这个窗口打开就可以啊,打开之后呢,咱们来导入相关的美文坐标,因为它是一个Supreme Boot的工程,所以肯定还是要继承啊,这个地方,通过Parent标签来继承这么一个Supreme Boot Stutters,

好,然后接下来我们看具体导入哪些坐标,我先复制过来啊,咱们来整体来看一下,一直到Build这儿,好,前面这些呢就不用看了,我们都已经说过了,对吧,然后这里边重点我们还是看哪个呢,重点看的是这个,是DROCE-KIE-Supreme,这是不是跟我们的Supreme来进行整合的,

但是你仔细看的话,你会发现,好像我们并没有去导入这个Supreme Boot Stutters,

我们已经导入那个DROCE-DecisionTables,就是那个决策表相关的那个架标,对不对,并没有导那个,为什么呢,因为我们现在啊,已经导入这个KIE-Supreme,那么你在导入它的时候呢,它其实就会把我们那个决策表的那个坐标呢,给传递过来,咱们可以看一下,

但是你显示的给它写上,给它导进来也是没问题的,咱们可以来看一下,重点看的是什么呢,

跟我们这个Supreme整合的这个,就是KIE-Supreme,对吧,就是这个,然后呢,我们打开来看一下,你看这里边呢,它其实就已经把这个DROCE-DecisionTables,就是决策表所对应的这个,已经给我们传递过来了,好,所以我们就不用显示的再来导一遍了,OK,这是咱们这个POP文件呢,也就已经搞定了,然后再往下呢,我们就需要来创建咱们这个VML文件啊,这个都是常规的,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们的VML文件,这个就是我们

常规的做法,我们在这儿来创建出来这个文件,并且呢,这个文件呢,我们还是最简单的,设置的一个是什么呢,一个是我们他们开的端口号,对吧,然后还有一个呢,就是咱们这个应用名称,好,跟咱们当前这个项目名呢,保持一致就可以了,好,这个也没什么好说的,然后再往下呢,我们就来创建一个实体类,这个实体类呢,就是跟我们这个保险信息相关的封装的保险信息相关的封装的保险信息相关的封装的保险信息相关的封装的保险信息相关的封装的保险信息相关的封装的保险信

相关的,因为一会儿我们的业务规则当中呢,也会使用到它,所以我们先把它创建出来,先把它的包呢,咱们来创建一下,然后呢,把这个类创建出来,这个类里边的属性呢,还是比较多的,你看我们是从parameter1一直到24,一共设计到了24个属性啊,分别都是什么含义呢,你看后边我们都有注释啊,

如果没有注释的话,因为咱们起的这个名字呢,其实用这个编号来起的,所以说它的可读性还是比较差的,所以呢,我们这个注释呢,就显得非常重要了,第一个参数呢,代表的是什么呢,是这个第一个属性代表的是保险公司,然后呢,方案代码,什么渠道号,销售区域,投保年龄等等这些啊,还有保险期间,交费期间,交费方式,保险类型,等待期,犹豫期等等啊,这些呢,全都是跟保险相关的,全都是跟保险相关的,

好,get set呢,我们就这就省略了,咱们考进来,整个考进来,把这替换一下,但是这里边的话,我们的get set就不能省略了,咱们可以来创建一下,把get get set都给它加上,好,这样的话,我们这个实体类呢,就已经搞定了,它封装的就是我们的保险信息,好,这个实体类放这儿,

好,

然后再往下的话呢,我们就需要来创建咱们这个决策表文件了,其实呢,我们这个决策表文件才是咱们这个案例里边最最重要的,或者说我们的业务规则呢,是不是都在决策表里边,主要的业务逻辑全在这里边呢,这个文件的话呢,因为如果我们现场去写的话,自己去设计的话,可能这个文件呢,光这一个文件就要搞一个小时,甚至时间会更长,所以说呢,我们在这呢,提前已经准备好了,

咱们呢,直接拿过来啊,先来读一下这个文件,然后呢,我们就直接用它就可以了,在我们这个实战资料里边啊,在我们今天实战资料里边已经提供好了,就是这个insurance info check,这个excel文件,然后我们直接打开它,打开它之后呢,我们直接看第一个,后边这些呢,这是你看这是字段说明,对吧,跟我们刚才看到那个实体类里面那个是一致的,然后呢,这是事例,事例就不用管了,然后呢,我们直接看第一个,

而且呢,我们使用这个D-Rose啊,来解析咱们这个,来解析我们的这个表格的时候呢,它默认呢,也只是解析第一个标签页的,所以要把我们这个真正有用的啊,或者你想让它解析的,放在第一个这个标签页里边,好,然后呢,咱们一块可以来读一下,大概读一下,ruler set,这是不是对应的,就是我们的那个什么,相当于我们的package,对不对,后边呢,我写的ruler,它这个值你写什么都可以,

啊,甚至你也可以,

不写,

这个值,这个ruler我可以不写,

不写的话呢,它就会使用默认的,

然后variables呢,

这是定义全局变量,我们在这呢,依然也是定义了一个全局变量,是list类型的,

名字呢,叫做list rulers,

然后呢,这个还是

这个排序的这个,对吧,然后呢,

import,咱们在这呢,一共引入了

三个吧,引入了三个,

一个是我们这个

insurance

info,对吧,就是刚才我们

创建的这个实体类,

一会儿需要把它传进去,

还有呢,一个是list的,还有一个arealist的,

一共引入了这么三个类,

然后再往下呢,

在这个地方有一个空行,

其实这个空行有没有都可以,有没有都可以啊,

然后再往下看,

就是ruler table,对吧,

ruler table呢,我们

前面已经提到过了,

再往下呢,是不是就是我们的条件,

条件完了之后呢,是不是就是

有一行是类似于注释的,

再往下呢,是不是就是我们一行

代表的就是一条规则,

ruler table呢,给的名字叫

insurance-ruler

再往下就是我们的condition,

这是关键字了,对吧,condition关键字,

咱们这个condition呢,定义的比较多啊,

你看整体我们缩小来看一下,

比较多,

但是这么小大家应该看不清楚了,

我们主要还是看一下它的结构,

因为这个表格呢,

设计的是相对来说

比较复杂的,比较复杂的,

因为它的条件的维度,

一共有多少个维度呢,

一共有11个维度,

所以说呢,这个条件一共有11个condition,

非常多,

然后呢,我们来看

下面呢,是不是就是我们的这个

匹配,对吧,

首先呢,是类型匹配,

要求从这个工作内存里面要查找

叫insurance-info,就是咱们这个实体类,

对吧,然后呢,再往下呢,

就是这一行

对应的就是我们的这个什么呢,

属性约束了,你看parameter1

不等于什么,

parameter1对应的是谁呢,

parameter1对应的是保险公司,

对吧,咱们不是说嘛,

必须是PICC的,所以你看啊,

它写的是parameter1不等于,

然后这个地方是$1,

$1将来它是不是会从我们这个

这个地方来取值,

这个地方来取值,

相当于就是parameter1不等于PICC,

好,

如果这条成立了,

那就说明保险公司不对,对吧,

那这个时候呢,准入就失败了,

以此类推啊,其他的这是

第二个条件,这是销售区域,

你看,parameter4不等于什么,

$1,然后呢,同时parameter4

不等于$2,这个地方

我们给的值,你看是北京,天津,

对吧,因为我们的销售区域,

刚才我们也看了那个规则了,

它是不是要求是北京,天津,这两个区域,

还有年龄,对吧,是0到17岁,

保险期间是不是三个,

20,25,30,还有这个

交费期间是这些,

整个,

这是那个交费方式,对吧,

一个是短交,还有一个是年交,

好,这是对这个要求,

这是我们这些条件啊,

条件完了之后呢,我们看,

再往后呢,是有一个agenda group,

这跟咱们这个room

案例是一样的,对吧,这些规则呢,

这一共11个规则啊,全都

归到了一个组里面,都叫sign,

这个组,再往后面

是不是就是我们的action,就是具体的

动作,对吧,相当于就是

我们的zend那一部分,

这一部分呢,

我们主要就是像这个

全局变量里面,是不是来添加

我们的这个信息,

对吧,比如说这条成立了,

就说明保险公司不对,那么他就会

添加进去这么一个信息,保险公司

不正确,如果第二条规则呢,

如果这是销售区域的,

对不对,所以他就会添加

这么一个进去,销售区域不正确,

仅支持北京和天津,

这是年龄的,所以

后边呢,都是类似的,都是类似的,

然后我们再可以

缩小一下,你看,从这一行

开始,对吧,从我们这一行

开始,然后呢,下边

这些,这都是

每一行就是一个

规则,每一行就是一个规则,

好,这是关于咱们这个

决策表,对吧,决策表,

它本质上呢,就是这么一个Excel

文件,咱们的规则呢,全都写到

这里面来了,OK,决策表呢,

我们先看到这儿,咱们呢,

可以直接拿过来用就可以了,

我们可以把它放到

我们某一个盘复下面,一会儿呢,

到下面去读取它,就可以了,

好,那么这是咱们

这个入门案例呢,我们先说到这儿,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告：

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 项目中集成 Drools 规则引擎的实战教程。讲师通过一个“保险产品准入规则”的案例，演示了从零开始构建项目、定义实体类、创建规则表、编写规则文件、并最终封装工具类的完整流程。核心思想是利用 Excel 表格作为规则模板，通过 Drools 的规则引擎进行动态校验，从而实现业务规则的灵活配置和管理。视频重点在于展示如何将业务规则从 Excel 文件中读取并应用到 Java 应用程序中，强调了规则与代码分离的优势。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：开场，介绍本节内容为“Drools 实战”中的“保险产品准入规则”部分。
*   **00:00:05 - 00:00:15**：讲解本案例的业务背景，即通过 Excel 文件定义规则，业务人员可直接修改，系统无需改动。
*   **00:00:15 - 00:00:30**：第一步，创建 Maven 工程 `insuranceInfoCheck` 并配置 `pom.xml` 文件，引入 Spring Boot 和 Drools 相关依赖。
*   **00:00:30 - 00:00:45**：第二步，创建 `application.yml` 配置文件，设置服务端口和应用名称。
*   **00:00:45 - 00:01:00**：第三步，创建实体类 `InsuranceInfo`，用于封装保险产品的各项参数。
*   **00:01:00 - 00:01:15**：第四步，创建决策表文件（Excel），用于定义具体的业务规则。
*   **00:01:15 - 00:01:30**：第五步，封装工具类 `KieSessionUtils`，用于加载规则并执行校验。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **规则列表**：展示了规则9、10、11的具体内容，例如“投保年龄+保险期间不得大于40周岁”、“保险金额规则”等。
    *   **章节大纲**：清晰地列出了“9.3.3 实现步骤”下的各个子步骤。
    *   **Excel 规则表**：展示了规则表的结构，包含“CONDITION”和“ACTION”列，以及具体的规则条件和动作。

*   **代码关键内容**：
    *   **`pom.xml` 依赖配置**：
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>2.0.6.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>2.0.6.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
            <version>2.0.6.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
            <version>2.0.6.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-compiler</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-templates</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        <dependency>
            <groupId>org.kie</groupId>
            <artifactId>kie-api</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        <dependency>
            <groupId>org.kie</groupId>
            <artifactId>kie-spring</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        ```
    *   **`application.yml` 配置**：
        ```yaml
        server:
          port: 8080
        spring:
          application:
            name: insuranceInfoCheck
        ```
    *   **`InsuranceInfo` 实体类**：
        ```java
        package com.ithema.drools.entity;

        /**
         * 保险信息
         */
        public class InsuranceInfo {
            private String param1; // 保险公司
            private String param2; // 方案代码
            private String param3; // 渠道号
            private String param4; // 销售区域
            private String param5; // 投保年龄
            private String param6; // 保险期间
            private String param7; // 缴费期间
            private String param8; // 缴费方式
            private String param9; // 保障类型
            private String param10; // 等待期
            private String param11; // 犹豫期
            private String param12; // 职业类型
            private String param13; // 保额限制
            private String param14; // 免赔额
            private String param15; // 土险保费
            private String param16; // 附加险保费
            private String param17; // 与投保人关系
            private String param18; // 与被保人关系
            private String param19; // 性别
            private String param20; // 证件
            private String param21; // 保额
            private String param22; // 保费
            private String param23; // 保额
            private String param24; // 保费
        }
        ```

*   **图表 / 规则表内容**：
    *   **规则表结构**：包含“CONDITION”和“ACTION”列，用于定义规则条件和动作。
    *   **规则示例**：
        ```
        param1 = $1
        param1 = $1, param4 = $2
        Integer.parseInt(param5) < 1
        Integer.parseInt(param5) = 2
        param7 = $1, param7 = $2
        param7 = $1, param7 = $3
        param7 = $1, param7 = $4, param7 = $5, param7 = $6
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   **描述**：讲师在 IntelliJ IDEA 中创建了一个名为 `insuranceInfoCheck` 的 Spring Boot 项目，并在 `pom.xml` 文件中添加了必要的依赖，包括 Spring Boot 的 Web、Test、AOP 启动器，以及 Drools 的核心库（如 `drools-compiler`, `kie-api` 等）。
    *   **演示**：通过鼠标点击和滚动，展示了 `pom.xml` 文件中依赖的添加过程，并高亮了关键的依赖项。

*   **场景二：配置文件与实体类创建**
    *   **描述**：讲师创建了 `application.yml` 文件，配置了服务端口为 8080 和应用名称。随后，创建了 `InsuranceInfo` 实体类，用于封装保险产品的各项参数。
    *   **演示**：在 IDEA 中展示了 `application.yml` 文件的内容，并在 `src/main/java/com/ithema/drools/entity` 包下创建并编辑了 `InsuranceInfo.java` 文件，定义了 24 个私有字符串属性。

*   **场景三：规则表设计与 Excel 操作**
    *   **描述**：讲师切换到 Microsoft Excel，展示了规则表的结构。规则表包含“CONDITION”和“ACTION”列，用于定义规则条件和动作。
    *   **演示**：在 Excel 中，讲师通过鼠标操作，展示了如何在规则表中输入条件，例如 `param1 = $1` 和 `Integer.parseInt(param5) < 1`，并解释了这些条件的含义。

*   **场景四：工具类封装**
    *   **描述**：讲师开始编写 `KieSessionUtils` 工具类，用于加载规则并执行校验。
    *   **演示**：在 IDEA 中，讲师在 `src/main/java/com/ithema/drools/utils` 包下创建了 `KieSessionUtils.java` 文件，并导入了 `InsuranceInfo` 和 `PersonInfoEntity` 等实体类，以及 `KieServices` 和 `KieContainer` 等 Drools 相关类。

---

以上是根据视频画面进行的结构化分析报告。
