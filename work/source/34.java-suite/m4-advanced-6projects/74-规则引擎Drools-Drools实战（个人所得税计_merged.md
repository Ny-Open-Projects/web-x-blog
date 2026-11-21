# 74-规则引擎Drools-Drools实战（个人所得税计 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续啊,刚才呢我们是对计算的规则呢,说了一个说明,对吧,并且套用了一个实际的例子,假设我们这个税前工资是1万块钱,对吧,最终呢我们怎么通过这个规则一步一步啊,把我们需要的扣税额还有税后工资给计算出来。

哎,这是我们规则呢,需要先明确,你必须得会计算,啊,然后接下来呢,我们就实际来操作一下,看看我们这个案例啊,具体如何实现。

首先呢,我们还是来创建工程,而我们这个案例呢,是基于Spring Boot啊,整合我们D-Rose这种方式来实现的,这也是目前比较主流的啊,就是在我们项目开发当中啊,一般都是基于Spring Boot啊,这个平台来开发,啊,这样的话可以大大简化我们的开发量,对吧。

好,那接下来呢,我们就从创建项目开始。

先创建一个Mainware工程,然后呢,这个工程的名字呢,就叫Calculation,对吧。

这就是计算的意思。

好,咱们在这呢,直接创建一个新的Mainware工程。

因为是一个Spring Boot的工程啊,所以这儿呢,这个股价就不用选择了,直接在这儿来指定一下它的这个坐标就可以。

好,把这个工程名写到这儿,然后Next。

这些地方呢,都不用改了。

好,这样的话,我们这个工程呢,就已经创建好了。

呃,创建好之后呢,咱们是不是需要第一步呢,肯定是配置这个POM文件了,对吧。

好,那么我们来配置一下这个POM.XML文件。

在这里边呢,首先我们需要来干什么呢?

呃,继承这个Spring Boot Stutters,对吧。

咱们使用Spring Boot的工程啊,肯定都是这样的,继承它的这么一个副工程,Spring Boot Stutters,这是官方给的。

版本呢,是2.0这个版本。

然后接下来呢,我们来看啊,要导入的这个Dependency。

也就是说,我们要导入这个Dependency。

这是我们的Main文坐标,对吧。

好,把它来烤一下。

呃,这些坐标的话,我们其实前面都已经讲过了。

咱们前面在讲整合的时候,Spring Boot整合D-Rose的时候呢,都已经说过了。

所以我们在这儿呢,就直接烤过来用啊,就可以了。

接下来拿过来。

跟当时导的坐标是完全一样的。

没有做任何修改。

好,这是关于POM文件呢,就已经整理好了。

好,把它关上就可以了。

呃,这一步搞定之后呢,接下来咱们是不是需要来创建我们的,呃,YAM文件,对吧。

就是作为Spring Boot的工程啊,它的核心的配置文件。

那么这个配置文件名呢,我们还是使用默认的,application.yml。

这个位置呢,肯定是在我们的resources下边来创建。

呃,这里边要配置的东西其实非常少。

因为我们当前这个案例呢,没有涉及到相关的一些数据库的操作啊。

所以关于那些什么数据源。

那些什么CNN的呀,mybatties的,很多配置就没有了。

呃,所以说这块配置的很少。

一个是我们的端口号,还有一个就是我们的应用名。

好,这个直接抄过来就可以了。

然后把它关上,这一步也就搞定了。

然后再往下呢,是不是就是关于我们这个配置类啊。

这个配置类的话放在哪呢?

放在这个config目录下。

所以我们先把这个package来创建一下。

然后这个config这个类的话,咱们前面其实也都讲过了。

再做我们这个Spring Boot。

等和Droso的时候,是不是也讲过了。

呃,只不过呢,这一块的话,呃,有一句不一样。

就在原先的基础之上加入了这么一句。

而这一句的话,咱们前面也已经建过了。

就是system.setProperty。

那这个地方大家还记得是什么意思吗?

是不是我们在规则文件中啊,如果使用到了我们的一些日期的格式,对吧?

并且呢,你使用的还不是人家默认的格式。

那这个时候呢,我们就需要来设置一下。

否则的话,它是不是在进行。

这个启动的时候,预发检查的时候就会报错。

因为我们一会儿呢,在规则文件里面会使用到日期。

这个日期呢,我用的是这种年月日这种格式啊。

所以说我们在这需要来设置一下。

其他的地方呢,跟原先都是一样的,没有做任何修改。

咱们直接把这个配置类呢,来创建出来。

就叫DrosConfig。

在这儿来创建一下。

DrosConfig。

刚才我就整个啊,整个考吧。

把整个文件内容全都考过来。

直接放在这儿。

好。

这是我们的配置类啊,就已经考过来了。

需要注意的还是什么呢?

就是这个Rules.

Rules Path,对吧?

也就是我们的规则文件放在什么位置,需要跟它对应上。

那么一会儿呢,我们是不是就需要来创建规则文件。

那这个规则文件放在哪呢?

就要放在Rules目录下。

这个Rules指的是从Resource下面找的。

所以咱们现在呢,可以先给它创建出来。

Rules目录。

一会儿呢,我们的规则文件就会放在这下边。

这样的话呢,我们项目加载的时候呢,就会从这个下边,是不是找到我们这个规则文件了。

好。

这是配置类呢,咱们就已经搞定了。

然后接下来再往下呢,我们需要来编写一个实体类。

因为一会儿我们要进行规则的计算,对吧?

规则的计算呢,会涉及到很多参数。

包括我们的税前工资啊,应纳税所得额啊,税率啊,还有什么扣税额。

等等一大堆。

那这个时候呢,我们会封装一个实体类啊。

把这些属性呢,全都封装在这个类里面去。

好。

这个实体类呢,我们就放在这个Entity啊,这个包下面来。

所以接下来呢,我先把这个包来创建一下。

先创建一个Package。

好,这包有了。

然后呢,把这个类啊,卡过来。

叫Calculation。

然后呢,我们把它的这个属性,对吧?

以及对应的Guideset方法。

然后呢,还有一个ToString的方法。

把这块儿卡过来。

这些代码呢,我们就不再刻上去敲了啊。

好,大家可以看到。

这些呢,我都已经卡过来了。

然后呢,这里边有税前工资,对吧?

还有我们的应纳税所得额,还有税率,还有素算扣除数。

这个呢,是扣税额,这个是税后工资。

恰好跟我们这个页面上,大家看一下。

我们页面上设计的这些啊,来往上翻一下。

这些是不是能对应上?

税前月收入,对吧?

然后呢,应纳税所得额,税率,素算扣除数,还有扣税额,还有扣税工资。

这些呢,都是一一对应的。

好。

这是关于我们这个实体类。

然后再往下呢,是不是就是我们的规则文件的编写。

好,那么因为这个案例呢,我们要编写规则文件的时候呢,可能花费的时间会长一些。

所以呢,我们一会儿呢,再来专门编写我们的规则文件。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是关于“Spring Boot整合Drools”技术实战的教程，具体演示了如何开发一个“个人所得税计算器”。课程从创建一个名为 `calculation` 的 Maven Spring Boot 项目开始，逐步配置项目依赖、应用配置文件、编写核心的 DRL 规则文件、以及定义用于计算的实体类 `Calculation`。整个过程旨在展示如何在现代 Java 开发环境中集成 Drools 规则引擎，实现业务逻辑的规则化管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**：视频开头，展示课程的 PPT 大纲，定位到“9.1.3 实现步骤”。
*   **00:00:03 - 00:00:07**：演示在 IntelliJ IDEA 中创建新项目，选择 `calculation` 作为项目名。
*   **00:00:07 - 00:00:12**：在 IDEA 中打开 `pom.xml` 文件，展示父工程的配置，包括 `spring-boot-starter-parent` 和 `2.0.6.RELEASE` 版本。
*   **00:00:12 - 00:00:16**：展示 `pom.xml` 中的 `<build>` 部分，配置了 `maven-compiler-plugin`，将 Java 编译版本设置为 1.8。
*   **00:00:16 - 00:00:20**：切换到 `application.yml` 文件，配置服务器端口为 8080 和应用名称为 `calculation`。
*   **00:00:20 - 00:00:24**：开始编写配置类 `DroolsConfig`，用于初始化 Drools 的 `KieFileSystem` 和 `KieContainer`。
*   **00:00:24 - 00:00:28**：编写实体类 `Calculation`，定义了 `wage`（税前工资）、`wageMore`（应纳税所得额）、`cess`（税率）、`preminus`（速算扣除数）、`wageminus`（扣税额）和 `actualWage`（税后工资）等属性。
*   **00:00:28 - 00:00:32**：在 `Calculation` 类中添加了 `getActualWage()` 方法，用于计算税后工资。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`9.1.3 实现步骤`。
    *   **第一步**：创建 Maven 工程 `calculation` 并配置 `pom.xml` 文件。
    *   **第二步**：创建 `/resources/application.yml` 文件。
    *   **第三步**：编写配置类 `DroolsConfig`。
    *   **第四步**：编写实体类 `Calculation`。

*   **代码关键内容**：

    *   **`pom.xml` (父工程配置)**：
        ```xml
        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.0.6.RELEASE</version>
        </parent>
        ```

    *   **`pom.xml` (编译插件配置)**：
        ```xml
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>2.3.2</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
        ```

    *   **`application.yml` (应用配置)**：
        ```yaml
        server:
          port: 8080
        spring:
          application:
            name: calculation
        ```

    *   **`DroolsConfig.java` (配置类)**：
        ```java
        public KieFileSystem kieFileSystem() throws IOException {
            System.setProperty("drools.dateformat", "yyyy-MM-dd");
            KieFileSystem kieFileSystem = kieServices.newKieFileSystem();
            ResourcePatternResolver resourcePatternResolver =
                    new PathMatchingResourcePatternResolver();
            Resource[] files =
                    resourcePatternResolver.getResources("classpath*:" + RULES_PATH + "/*.drl");
            String path = null;
            for (Resource file : files) {
                path = RULES_PATH + file.getFilename();
                kieFileSystem.write(ResourceFactory.newClassPathResource(path, UTF_8));
            }
            return kieFileSystem;
        }

        @Bean
        @ConditionalOnMissingBean
        public KieContainer kieContainer() throws IOException {
            KieRepository kieRepository = kieServices.getRepository();
            KieBuilder kieBuilder = kieServices.newKieBuilder(kieFileSystem());
            kieBuilder.buildAll();
            return kieServices.newKieContainer(kieRepository.getDefaultReleaseId());
        }
        ```

    *   **`Calculation.java` (实体类)**：
        ```java
        package com.itheima.drools.entity;

        public class Calculation {
            private double wage; // 税前工资
            private double wageMore; // 应纳税所得额
            private double cess; // 税率
            private double preminus; // 速算扣除数
            private double wageminus; // 扣税额
            private double actualWage; // 税后工资

            public double getWage() {
                return wage;
            }

            public void setWage(double wage) {
                this.wage = wage;
            }

            public double getActualWage() {
                return actualWage;
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化**：
    *   讲师在 IntelliJ IDEA 中创建了一个名为 `calculation` 的新项目。
    *   展示了项目结构，包括 `src/main/java` 和 `src/main/resources` 目录。

*   **场景二：配置文件编写**：
    *   讲师在 `pom.xml` 中配置了 Spring Boot 的父工程和编译插件。
    *   在 `application.yml` 中设置了服务器端口和应用名称。

*   **场景三：Drools 配置类开发**：
    *   讲师编写了 `DroolsConfig` 类，其中包含了初始化 `KieFileSystem` 和 `KieContainer` 的方法。
    *   通过 `ResourcePatternResolver` 读取 `classpath` 下的 `.drl` 规则文件。

*   **场景四：实体类开发**：
    *   讲师创建了 `Calculation` 实体类，定义了用于计算个人所得税的各个属性。
    *   展示了 `getActualWage()` 方法，该方法将用于在规则中调用，以计算最终的税后工资。

*   **场景五：多窗口操作**：
    *   讲师在 IDEA 中打开了多个窗口，包括 `Calculation.java`、`application.yml` 和 `pom.xml`，以便于同时查看和编辑相关文件。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解视频内容的技术要点和实现步骤。
