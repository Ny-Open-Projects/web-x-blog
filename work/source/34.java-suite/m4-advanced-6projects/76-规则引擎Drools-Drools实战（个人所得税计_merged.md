# 76-规则引擎Drools-Drools实战（个人所得税计 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢咱们这个规则文件呢已经写完了

这里边呢一共涉及到了是9个规则

对吧 这个都已经计算完了

再往下呢我们就需要来创建一个

Ruler Service这么一个类啊

我们通过这个类呢

跟咱们的规则引擎来进行交互

好 接下来我们来创建出来

它在哪个包下面呢

就在我们这个D-Rose.service啊

这个包下面

来 先来创建这么一个package

然后呢我们来创建这么一个类啊

就叫Ruler Service

Ruler Service

好

别忘了加一个注解

对吧 加一个service注解

然后呢在这里边咱们是不是需要来注入一下

注入一个什么对象呢

还是我们的KBase对象

好

Private

叫KBase

把它注进来

通过一个什么呢

AutoWare的是不是来注入一下

好

这是先把KBase对象

是KIE Base啊

不是KBase

好

这个别写错了

应该是KIE Base

那么把它注进来

那这个KIE Base从哪能注进来呢

为什么能注进来呢

就是因为在我们这个Config配置类里边

咱们是不是已经配置了

通过这个方法是不是帮我们来

这个返回一个KIE Base对象

并且呢它也是

你看我们加了bin标签对吧

这其实就相当于我们的配置文件啊

由Spring工厂来负责处置化

这样的话呢

我们把这个KIE Base呢

就已经注进来了

注进来之后呢

咱们在这儿呢

来提供一个方法

这个是调用什么呢

调用我们D-Rose规则引擎

来干什么呢

实现我们这个个人所得税啊

计算

这么一个方法

那这个方法呢

返回值返回个什么东西呢

咱们让它来返回我们这个实体类啊

这种类型

因为一会儿呢

我们要来编写一个Controller

所以Controller会调用我们的service

那么它调用service这个方法之后呢

就会把我们计算之后的这个结果返回

而这个结果呢

咱们就使用这种类型来返回就可以

这个方法名呢就叫calculate吧

calculate

这是计算的意思

那计算的话呢

你需要

你需要给我传一个对象进来

传一个什么对象呢

也传一个这样的对象进来

这样的对象进来

calculation

这个方法呢叫calculate

其实是动词对吧

这个是名词

然后这个计算的过程呢

我们就需要来调用规则引擎来计算了

规则刚才咱们都已经写完了对吧

并且呢我们的KAE base也已经

这个给注进来了

注进来之后呢我们直接通过它呢

来new一个session对吧

来获得一个KAE session

有了session之后呢

咱们是不是就可以啊

将我们这个对象啊

给它加入到我们的工作内存里面去

所以通过session点什么呢

insert一下

把这个对象

fag的对象加入到工作内存

并且呢来触发一下

大家还记得吧

fail all rulers

然后呢

别忘了把这个session是不是给关闭一下

dispose

然后执行完之后呢

我们还是把这个对象来返回

大家来看这个代码

那这个时候呢

我们返回的这个对象可就不一样了

因为呢

我们是已经insert了这个对象了

对吧

把它加入到我们的工作内存里面去了

这样呢

会导致我们的规则触发

触发的时候呢

在规则文件里面

咱们是不是对传进来的这个对象

然后进行了修改啊

进行了修改

而这些修改的话呢

我们通过这个Java代码的方式呢

其实是能够感知到的

因为它其实是同一个对象

它本质上就是同一个对象

所以说呢

你传进去的时候呢

传进去的时候

只是设置了这个税前工资

其他的这些我们都没有设置

因为这些呢

是需要我们去计算的

对不对

而我们计算完之后

这个时候再返回的时候

这个对象呢

就已经设置完值了

在规则文件上

咱们是不是都已经各种设置了

都已经设置完了

所以说呢

返回的这个对象里边的属性呢

就已经是经过计算之后

设置成功的属性了

所以我们返回的

其实还是这个对象

好

这样的话呢

我们这个service也就已经写好了

那么再往下呢

咱们来编写一个controller

对吧

你看这是我们的service

就已经写好了

然后再往下呢

我们就需要来

我们就需要来

创建一个controller

这个controller包呢

我们先来创建一下

在controller里边呢

我们来调用service就可以

先把这个包来创建一下

这个类名呢

也叫啊

比如说也叫

ruler controller

好

然后呢

注解我们来加一下

先来加一个rest controller

然后再来加一个request mapping

这个就叫ruler吧

然后这里边呢

我们来提供一个计算的方法

这个方法呢

我就不写了

包括我们这个service也是需要注进来的

直接拷过来

咱们大概把这个代码读一下就可以了

都是比较简单的代码

注入这个service

然后呢

我们提供了这么一个方法叫calculate

对吧

这个方法呢

可以通过这个路径访问到

这个方法呢

需要页面给我传过来一个参数

而这个参数呢

是不是代表的就是我们的这个

税前的这个月收入

对吧

然后呢

我们把它Nu出来

Nu出来之后呢

只是设置这个值

然后呢

给到service

里面去

而在service里边

咱们是不是调用了我们规则引擎

在规则引擎内部呢

就会为我们去计算相应的其他的值

对吧

完事之后呢

把这个对象是不是就给我返回回来

返回来之后呢

我们可以在这先输出一下

输出之后呢

然后再返回

把这个对象呢

转成JSON

然后返回给我们的页面

好

那这一步呢

我们也就做完了

还是比较简单的

好

那这个control写完之后呢

接下来咱们需要来编写一个

起动性的页面

还有呢

就是我们的静态资源文件

也就是我们的页面

好

先把这个启动类来创建一下

就叫derose application吧

放在哪呢

还是放在我们derose

这层目录里边

这里边呢

就有一个启动的方法

对吧

一个main方法

然后呢

还有一个注解

把main方法拷过来

把注解呢

我们来加一下

sprintboot application

好

这个没什么好说的

直接这样来编写一下就可以了

好

最后呢

就是我们的页面了

对吧

因为我们需要让页面呢

跟咱们这个control来进行交互

页面呢

我提前已经准备好了

咱们直接考过来就可以

在这呢

有个static

在我们今天资料里边

有一个static

static里边呢

有一个calculation.html

这是咱们的html页面

然后呢

这个页面上呢

用到了两个gs文件

一块呢

把它考过来

咱们整个把static

注意

static是不是代表的是静态的

我们复制一下

然后放到

resources

下面

这是在咱们

sprint boot的工程里边

咱们的静态的资源文件呢

可以放在static

这么一个目录下边

这样呢

我们就可以访问到的

好

那么到目前为止啊

咱们的案例的代码编写部分呢

就都已经完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于在 Spring Boot 项目中集成 Drools 规则引擎的实战教学。讲师通过一个“个人所得税计算器”的示例，逐步演示了如何创建项目结构、配置 Drools、编写 Java 实体类、编写服务层代码以调用规则引擎、以及创建 RESTful 控制器来暴露服务接口。整个过程旨在展示如何将业务规则（如税率计算）从业务逻辑中解耦，通过规则引擎进行动态管理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中精确获取视频时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **第 1 节：项目初始化与服务层创建 (00:00 - 00:15)**
    *   展示了项目结构，包括 `src/main/java` 和 `src/main/resources`。
    *   创建了 `RuleService` 服务类，用于调用 Drools 引擎。

*   **第 2 节：Drools 配置类 (00:15 - 00:30)**
    *   创建了 `DroolsConfig` 配置类。
    *   代码中使用了 `@ConditionalOnMissingBean` 注解，并通过 `KieServices` 创建 `KieContainer` 和 `KieBase`。

*   **第 3 节：实体类与服务层完善 (00:30 - 00:45)**
    *   创建了 `Calculation` 实体类，包含 `wage` (税前工资)、`wagemore` (应纳税所得额)、`cess` (税率)、`preminus` (速算扣除数)、`wageminus` (扣除额) 和 `actualwage` (税后工资) 等属性。
    *   在 `RuleService` 中，完善了 `calculate` 方法，调用 `session.fireAllRules()` 来触发规则。

*   **第 4 节：控制器层创建 (00:45 - 00:55)**
    *   创建了 `RuleController` 控制器类。
    *   使用 `@RestController` 和 `@RequestMapping` 注解，定义了 `/calculate` 接口，接收 `wage` 参数并调用 `RuleService`。

*   **第 5 节：启动类与项目整合 (00:55 - 01:05)**
    *   创建了 `DroolsApplication` 启动类。
    *   使用 `@SpringBootApplication` 注解，通过 `SpringApplication.run()` 启动 Spring Boot 应用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容：**
    *   **大纲：** 显示了课程的目录结构，包括“7.3 Spring Boot整合Drools”、“8. WorkBench”、“9. Drools实战”等章节。
    *   **关键步骤：** 明确列出了“第六步：创建RuleService”、“第八步：创建启动类DroolsApplication”、“第九步：导入静态资源文件到resources/static目录下”等步骤。

*   **代码关键内容：**

    *   **`RuleService.java` (服务层)**
        ```java
        package com.itheima.drools.service;

        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.stereotype.Service;
        import org.kie.api.KieBase;
        import org.kie.api.runtime.KieSession;

        @Service
        public class RuleService {
            @Autowired
            private KieBase kieBase;

            // 调用Drools规则引擎实现个人所得税计算
            public Calculation calculate(Calculation calculation) {
                KieSession session = kieBase.newKieSession();
                session.insert(calculation);
                session.fireAllRules();
                session.dispose();
                return calculation;
            }
        }
        ```

    *   **`Calculation.java` (实体类)**
        ```java
        package com.itheima.drools.entity;

        public class Calculation {
            private double wage; // 税前工资
            private double wagemore; // 应纳税所得额
            private double cess; // 税率
            private double preminus; // 速算扣除数
            private double wageminus; // 扣除额
            private double actualwage; // 税后工资

            public double getWage() {
                return wage;
            }

            public void setWage(double wage) {
                this.wage = wage;
            }

            public double getActualWage() {
                return actualwage;
            }
        }
        ```

    *   **`DroolsConfig.java` (配置类)**
        ```java
        @Configuration
        @ConditionalOnMissingBean
        public KieContainer kieContainer() throws IOException {
            KieRepository kieRepository = kieServices.getRepository();
            kieRepository.addKieModule(kieRepository.getDefaultReleaseId());
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
        @ConditionalOnMissingBean
        public KModuleBeanFactoryPostProcessor kiePostProcessor() {
            return new KModuleBeanFactoryPostProcessor();
        }
        ```

    *   **`RuleController.java` (控制器层)**
        ```java
        package com.itheima.drools.controller;

        import org.springframework.web.bind.annotation.RestController;
        import org.springframework.web.bind.annotation.RequestMapping;

        @RestController
        @RequestMapping("/rule")
        public class RuleController {
            @Autowired
            private RuleService ruleService;

            @RequestMapping("/calculate")
            public Calculation calculate(double wage) {
                Calculation calculation = new Calculation();
                calculation.setWage(wage);
                calculation = ruleService.calculate(calculation);
                System.out.println(calculation);
                return calculation;
            }
        }
        ```

    *   **`DroolsApplication.java` (启动类)**
        ```java
        package com.itheima.drools;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;

        @SpringBootApplication
        public class DroolsApplication {
            public static void main(String[] args) {
                SpringApplication.run(DroolsApplication.class);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建服务层 `RuleService`**
    *   讲师在 IntelliJ IDEA 中创建了 `RuleService` 类。
    *   通过 `@Autowired` 注解注入 `KieBase` 实例。
    *   在 `calculate` 方法中，创建 `KieSession`，调用 `insert` 方法将 `Calculation` 对象插入会话，然后调用 `fireAllRules()` 触发规则，最后调用 `dispose()` 关闭会话。

*   **场景二：配置 `DroolsConfig`**
    *   讲师创建了 `DroolsConfig` 配置类。
    *   使用 `@Configuration` 和 `@ConditionalOnMissingBean` 注解，定义了 `kieContainer`、`kieBase` 和 `kiePostProcessor` 三个 Bean。
    *   通过 `KieServices` 获取 `KieRepository`，并构建 `KieContainer` 和 `KieBase`。

*   **场景三：创建实体类 `Calculation`**
    *   讲师创建了 `Calculation` 实体类，定义了多个属性，如 `wage`、`wagemore`、`cess`、`preminus`、`wageminus` 和 `actualwage`。
    *   为这些属性提供了 getter 和 setter 方法。

*   **场景四：创建控制器 `RuleController`**
    *   讲师创建了 `RuleController` 类。
    *   使用 `@RestController` 和 `@RequestMapping("/rule")` 注解。
    *   在 `calculate` 方法中，接收 `wage` 参数，创建 `Calculation` 对象，调用 `ruleService.calculate()` 方法进行计算，并返回结果。

*   **场景五：创建启动类 `DroolsApplication`**
    *   讲师创建了 `DroolsApplication` 启动类。
    *   使用 `@SpringBootApplication` 注解，通过 `SpringApplication.run()` 方法启动 Spring Boot 应用。

*   **场景六：演示规则引擎工作流程**
    *   讲师在 `RuleService` 中逐步完善代码，从 `insert` 到 `fireAllRules`，演示了规则引擎的完整调用流程。
    *   在 `RuleController` 中，通过 `@RequestMapping("/calculate")` 暴露接口，演示了如何通过 HTTP 请求触发规则计算。
