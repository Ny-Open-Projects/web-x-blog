# 79-规则引擎Drools-Drools实战（信用卡申请_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才咱们是对我们信用卡申请

这个场景下面所涉及到的规则

做了一个说明

接下来我们就具体来实现

实现步骤我这已经列好了

需要说明的是我们当前这个案例

还是基于咱们Spring Boot

跟我们D-Rose整合

这个技术架构来实现

接下来我们就来创建一个

Mainware工程

第一步工程的名字就叫

Credit Card Apply

这个翻译过来就叫信用卡申请

咱们来创建这么一个工程

那么先把我们这个包来指定一下

看我们IT黑码

这是坐标

然后这个Mocker ID

来指定一下

这个位置都不用动了

直接完成

这样我们这个工程已经创建好了

接下来咱们来配置一下

这个POM文件

配置的这些坐标

我们都已经提供

好了

跟咱们其实第一个

这个个人所得税的

这个坐标都是一样的

首先我们需要

因为它是一个Spring Boot工程

所以我们需要来继承一下

通过Parent

这样来继承Spring Boot Starter

然后接下来我们来导入相关的坐标

通过这个Dependency

整个都考过来

后边还有一个Build

这个标签一直考到这

直接贴到这

好

这样的话

我们这个POM文件就已经配置好了

关于这些坐标

我就不再过多解释了

前面我们都已经导过一遍了

好

然后再往下

我们POM文件配置好之后

是不是就是我们Spring Boot工程

所涉及到的核心配置文件

通常叫做application.yml

但是也有用property属性的

那种格式的配置文件

咱们这用的是这种yml

这种格式

好

这里面的配置

其实还是比较简单的

因为没有涉及到一些数据库的配置

也没有其他的第三方的一些插件的配置

主要就是一个Tamk的服务器的端口

还有我们的应用的名称

所以配置起来比较简单

好

这一步就已经搞定了

再往下就是关于我们配置类

对吧

配置类的话

前面也已经用过了

咱们先把配置类所在的包

来创建一下

在config.com里面

我们先把配置类的配置类

放在这个包下边

然后这个类名就叫什么

就叫deroseconfig

它其实就是起到一个配置文件的作用

只不过是在我们Spring Boot工程里面

是通过一个类来表示的

然后需要给这个类是不是来加一个注解

就叫configuration

它代表的就是规则引擎的配置类

咱们整个就来考一下就可以了

然后这个配置类的话

我们其实前面也已经用过了

直接贴到这儿

这里面呢重点

是谁呢

就是这个

KE base

因为什么呢

因为我们是在咱们这个项目当中

直接把这个KE base是不是注给我们的service

然后有了base之后

我是不是就可以来获得一个KE session

从而通过这个session

就可以来操作我们规则引擎

对吧

比如说来触发规则

或者设置一些给它添加一些facts的对象

到我们的工作内存等等

所以说这个KE base呢

是我们直接会用到的

当然了你要想获得KE base呢

它需要有KE的container

因为它是从container里边来获得的base

而这个container从哪来的呢

它是不是需要从我们的这个repository这边来获得

所以它其实是一层套一层的

只不过我们直接接触的是这个KE base

这是关于这个配置类呢

我们直接考过来就可以了

需要注意的就是什么呢

就是这块

我们指定的这个rules path

就是你的规则文件放在哪

在这需要看准了

这是不是意味着我们需要来创建一个什么呢

来创建一个rules目录对吧

在这个resources下面来创建一个目录

一会儿呢我们的规则文件是不是就需要

放在这个目录下面

否则它是找不着的

但是在这的话呢

我们需要来创建一个实体类

创建一个实体类

这个实体类里面你看封装的信息呢

其实就是咱们信用卡申请的一些信息

比如说有这个申请人的一些基本信息

包括什么姓名啊

性别年龄啊这些对吧

然后呢这个呢是学历对吧

然后呢还有手机号

还有月收入

还有住址

还有是否有房

是否有车

还有现在持有信用卡的数量

也就是说前面这些啊

是需要我们是不是再通过

我们刚才看到那个表单页面啊

来录入的信息呢

就是这个一些信息

而下边这两个呢

是我们经过规则匹配之后啊

产生的结果

一个是check result

对吧

就是审核是否通过

还一个是什么呢

额度

还一个是额度

那接下来呢

咱们把这个实体类呢

来考过来

先来创建一下

先把这个entity这个包

创建出来

我就在这直接来创建一个package

然后呢在entity下面来创建这么一个

叫做credit card apply info

封装的呢就是咱们

表单页面上这些信息

这块呢我就不带手锹了

直接来复制了

包括它的这个get set方法

比较多啊

直接复制到这

咱们来看一下这我们是不是重写了一下

它的tostring方法对吧

在这个tostring方法这儿呢你看

我们判断了一下这个check result

check result刚才也看到了

它其实就是上面的这个result

那么这个boole类型的

这儿还考多了对吧

把这个去掉

那么我们来看一下

在这儿呢是不是有这么一个叫做check result

审核是否通过

如果是true的话表示审核通过

false的话表示审核不通过

然后呢这个是额度对吧

这个额度的话当然

它必须得是

你审核通过之后才有效对吧

如果审核都不通过

那这个额度根本谈不上

所以你看在我们这个tostring方法这儿呢

我们来判断一下

如果它等于true的话呢

输出这么一句话

就返回这么一句话

审核通过

信用卡额度为

然后把这个额度是不是给追加上

否则的话呢审核不通过就直接返回

审核不通过了

这是把这个tostring方法我们重写了一下

这个呢是关于咱们这个实体类

那么再往下呢是不是就需要来编写我们的规则文件了

但是这个规则文件编写起来呢

可能需要花费一段时间

所以说我们暂时先进行到第四步

现在呢我们来看一下我们完成的是什么呢

一个是创建了一个工程

再一个呢导入了一些这个坐标对吧

这些坐标

然后呢就是创建了咱们这个yam文件

还有呢就是创建了两个类

一个是实体类

刚刚创建的

还有一个呢就是咱们这个配置类

都是关于D-Rose的一些配置项

这段呢我们先到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于在 Spring Boot 项目中集成 DRL（Drools Rule Language）规则引擎的实战教程。讲师通过一个“信用卡申请”业务场景，演示了如何从零开始搭建项目结构、配置 Maven 依赖、编写配置类初始化 Drools 环境、创建业务实体类，并最终为业务规则（如根据收入和资产决定信用额度）做好准备。视频内容聚焦于项目初始化和核心配置，为后续编写规则文件和进行规则测试打下基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **课程介绍与项目背景**。讲师介绍了本节内容是“Drools 实战”系列中的“信用卡申请”模块，并展示了课程大纲，明确指出本节将讲解“9.2.2 实现步骤”。
*   **00:05 - 00:15**: **第一步：创建 Maven 工程并配置 pom.xml**。画面展示了如何在 IntelliJ IDEA 中创建一个名为 `creditCardApply` 的 Spring Boot 项目，并在 `pom.xml` 文件中添加必要的依赖，包括 `spring-boot-starter-web` 和 `drools-spring`。
*   **00:15 - 00:25**: **第二步：创建配置文件 application.yml**。讲师指导创建 `src/main/resources/application.yml` 文件，并配置服务器端口为 `8080`。
*   **00:25 - 00:35**: **第三步：编写配置类 DroolsConfig**。讲师在 `src/main/java/com/itheima/drools/config` 包下创建 `DroolsConfig.java` 文件，并导入必要的 Drools API。
*   **00:35 - 00:45**: **第四步：在 DroolsConfig 中配置 KieContainer 和 KieBase**。讲师在 `DroolsConfig` 类中编写了 `@Bean` 方法，用于初始化 `KieContainer` 和 `KieBase`，这是 Drools 规则引擎的核心组件。
*   **00:45 - 00:55**: **第五步：创建业务实体类 CreditCardApplyInfo**。讲师在 `src/main/java/com/itheima/drools/entity` 包下创建 `CreditCardApplyInfo.java` 文件，定义了申请人的基本信息，如姓名、月收入、是否有房、是否有车等属性。
*   **00:55 - 01:05**: **第六步：在配置类中加载规则文件**。讲师在 `DroolsConfig` 类中添加了加载规则文件的代码，将 `src/main/resources/rules` 目录下的 `.drl` 文件加载到 `KieBase` 中。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档大纲**：
    *   展示了课程的详细目录，包括“9.1 个人所得税计算器”、“9.2 信用卡申请”、“9.3 保险产品准入规则”等。
    *   在“9.2 信用卡申请”章节下，明确列出了“9.2.2 实现步骤”，并标注了“第一步”、“第二步”、“第三步”等。

*   **代码**：
    *   **Maven 依赖 (pom.xml)**：
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
        </dependency>
        <dependency>
            <groupId>org.kie</groupId>
            <artifactId>kie-spring</artifactId>
            <version>7.54.0.Final</version> <!-- 注意：实际版本可能不同 -->
        </dependency>
        ```
    *   **配置文件 (application.yml)**：
        ```yaml
        server:
          port: 8080
        spring:
          application:
            name: creditCardApply
        ```
    *   **配置类 (DroolsConfig.java)**：
        ```java
        @Configuration
        public class DroolsConfig {
            @Bean
            @ConditionalOnMissingBean
            public KieContainer kieContainer() throws IOException {
                KieServices kieServices = KieServices.Factory.get();
                KieRepository kieRepository = kieServices.getRepository();
                kieRepository.addKModule(kieRepository.getDefaultReleaseId());
                KieBuilder kieBuilder = kieServices.newKieBuilder(kieRepository);
                kieBuilder.buildAll();
                return kieServices.newKieContainer(kieRepository.getDefaultReleaseId());
            }

            @Bean
            @ConditionalOnMissingBean
            public KieBase kieBase() throws IOException {
                return kieContainer().getKieBase();
            }

            @Bean
            public KModuleBuilderFactoryPostProcessor kiePostProcessor() {
                return new KModuleBuilderFactoryPostProcessor();
            }
        }
        ```
    *   **实体类 (CreditCardApplyInfo.java)**：
        ```java
        public class CreditCardApplyInfo {
            private String name;
            private double monthlyIncome;
            private String address;
            private boolean hasHouse;
            private boolean hasCar;
            private int hasCreditCardCount;
            private boolean checkResult = true; // 核查是否通过
            private double quota = 0; // 额度
            // getter and setter methods
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**。
    *   讲师在 IntelliJ IDEA 中创建了一个名为 `creditCardApply` 的 Spring Boot 项目。
    *   通过编辑 `pom.xml` 文件，添加了 `spring-boot-starter-web` 和 `kie-spring` 依赖，为后续的 Web 服务和规则引擎集成做准备。

*   **场景二：配置文件与核心配置类编写**。
    *   讲师创建了 `application.yml` 文件，并配置了服务器端口。
    *   讲师在 `config` 包下创建了 `DroolsConfig.java` 文件，并编写了初始化 `KieContainer` 和 `KieBase` 的代码。这一步是 Drools 规则引擎在 Spring Boot 项目中运行的核心。

*   **场景三：业务实体类创建**。
    *   讲师在 `entity` 包下创建了 `CreditCardApplyInfo` 类，定义了申请人姓名、月收入、地址、是否有房、是否有车、是否通过审核和额度等属性。这些实体类将作为规则引擎的输入数据。

*   **场景四：规则文件加载**。
    *   讲师在 `DroolsConfig` 类中添加了加载规则文件的代码，将 `src/main/resources/rules` 目录下的 `.drl` 文件加载到 `KieBase` 中，为后续编写和测试规则做好了准备。

---

以上是根据视频画面内容整理出的技术课程结构化分析。
