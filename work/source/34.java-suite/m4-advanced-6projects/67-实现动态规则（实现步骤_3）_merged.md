# 67-实现动态规则（实现步骤_3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们是把这个reload啊

deroads ruler service这个类呢已经写完了

那么主要呢其实主要的代码量呢是在这儿对吧

就是把我们传进了这个list结合

然后呢把它进行便利对吧

然后呢进行这个读取

读取完之后呢通过这个file system这个对象呢来进行写

把这些内容呢把它写到我们这个磁盘下面

要注意啊这个地方我们是不是少了一个斜线对吧

resources然后呢应该是少了个斜线

然后后边这是不是我们的一个文件名

前面呢这是路径对吧

最终呢拼到一块

把这个文件把它写到这儿

然后呢基于我们这个文件系统

然后呢构建啊构建这个一个新的这个container对象

然后呢把它返回

这样的话呢我们就可以把这个重新构建的这个对象呢

把它复制给咱们这个全局的

这静态的这个container对象

然后呢我们后边再来创建session的时候呢

就直接基于这个container来创建

因为呢这个你可以倒着来来返回对吧

那么

那通过这个这个container对象怎么来的呢

它是不是就是通过我们这个重新查询数据库构建出来的

这样的话相当于我们这个规则呢就变成动态了

好

这是这个类呢就已经搞定了

然后接下来呢我们下一步呢就需要来提供这么一个叫做command line

renderimpl

但是这个类名叫什么无所谓

它起的作用就是什么呢

我希望在项目启动的时候

在项目启动的时候呢

它就会触发一下这个方法

就执行我们这个reload的方法

然后呢

把我们数据库里面最新的规则重新查一遍

对吧

然后呢把这个container对象给我重新创建一遍

那么我们如何能做到在项目启动的时候就会调用到这个方法呢

在这呢我们就需要通过这么一种方式

就是什么呢

实现这么一个接口

这是Spring Boot给我们提供的这个接口

叫做什么呢

command line render

可能有的同学前面已经用过了啊

有些人可能没有用过

那么它起的作用就是当我们只要让我们的类呢

实现这个接口对吧

实现这个接口

这样的话呢

在项目启动的时候呢

会就会有Spring Boot框架帮我们去调我们这个类相关的方法

咱们的可以先来看一下

command line render

我们可以来搜一下

找到这个接口

就这个command line render

你看他是在我们这个Spring Framework Boot的这个包下边提供的这么一个接口

而这个接口里边呢

只声明了一个方法

就是这个run这个方法

啊

所以说呢

它相当于是一个生命周期的方法

当我们这个项目启动的时候呢

就会由框架帮我们去调这个run方法

那么我们要做的呢

就是按照它的规则对吧

去提供一个类

实现这个接口

把我们具体想做的事呢

写到这个run方法内部就可以

你看我们这个run方法内部呢

就写一句话

就是什么呢

调用我们这个service的reload方法就可以了

好

那接下来呢

我们把这个类呢

来创建一下

咱们呢

也是放在咱们这个IMPL这个包下边去

在这边就可以了

在这来创建

然后呢

implement

给他们看是不是叫做command line render

command line render

这个

然后实现这个run方法

对吧

然后呢

这个地方呢

我们来给它加一个注解

来加一个注解

它其实就是一个service

对吧

其实你加service也行

或者加其他的注解

比如说我们这个讲义上写的是什么

component

咱们学过Spring应该都知道

这些注解其实本质上没什么区别

那么

起的

作用都是一样的

然后呢

这个日志这个加不加都可以

也可以给它加一下

好

然后接下来呢

我们就需要在这里边来注入什么呢

注入我们刚才编写的这个service

就是reload deroads ruler service

对吧

把它注入一下

reload deroads service

好

然后呢

通过Altware的把它注进来

然后在我们这个run方法里边呢

咱们直接调用这个service的什么呢

reload的方法

是不是

就可以啊

一定要这个方法

它是不是就执行我们这个reload的方法

然后在这呢

重新是不是查数据库

然后呢

重新创建考猜者

这样呢

当我们项目启动的时候呢

它就会执行一遍这个代码

大家注意啊

我们现在呢

这个包的话跟我们讲义不太一致

我把它改一致了

这块好

放在我们这个service的IMPL包下边

那么这一步呢

我们就已经搞定了

那么它起的作用是什么呢?

我们来写一个注释

这个就是什么呢

项目启动时

是不是来执行什么呢

当前类中的run方法

好

这个呢

就是我们必须要实现这个接口

实现这个接口

这个呢

是一个固定的用法

那么大家呢

直接按照这个用法来使用就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程讲解了如何在 Spring Boot 项目中实现 DRL（Drools 规则语言）规则的动态加载与热更新。核心内容是通过 `CommandLineRunner` 接口，在项目启动时自动调用 `ReloadDroolsRulesService` 服务，该服务会从数据库中查询最新的规则，将其转换为 DRL 文件并加载到 Drools 的 `KieContainer` 中，从而实现规则的动态生效。整个过程结合了 Spring 的依赖注入、Drools 的规则引擎 API 以及项目启动时的生命周期管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示项目结构和 `ReloadDroolsRulesService` 服务类的代码。
*   **00:00:05 - 00:00:15**: 讲解 `loadRules()` 方法，用于从数据库查询规则列表。
*   **00:00:15 - 00:00:30**: 讲解 `reload()` 方法，该方法会调用 `loadContainerFromString` 来重新加载规则。
*   **00:00:30 - 00:00:45**: 重点讲解 `loadContainerFromString(List<Rule> ruleList)` 方法，展示如何将规则内容写入文件系统并构建 `KieContainer`。
*   **00:00:45 - 00:01:00**: 讲解如何在 `CommandLineRunner` 中调用 `reload()` 方法，实现项目启动时自动加载规则。
*   **00:01:00 - 00:01:15**: 展示 `CommandLineRunnerImpl` 类的完整代码，包括 `@Component`、`@Autowired` 注解和 `run()` 方法的实现。
*   **00:01:15 - 00:01:30**: 讲解 `RulesReloadController` 的创建，用于提供 HTTP 接口来手动触发规则重载。
*   **00:01:30 - 00:01:45**: 展示 `RulesReloadController` 的代码，包含一个 `@PostMapping` 接口，用于触发 `reload()` 方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **标题**: “第五步：创建 CommandLineRunnerImpl，在项目启动时加载数据库中最新规则”。
    *   **标题**: “第六步：创建 RulesReloadController”。
    *   **大纲**: 展示了课程的目录结构，包括“8.2 实现步骤”下的“8.2.1 实现思路”和“8.2.2 实现步骤”。

*   **代码关键内容**:
    *   **`ReloadDroolsRulesService.java`**:
        ```java
        @Service
        public class ReloadDroolsRulesService {
            @Autowired
            private RuleMapper ruleMapper;

            public static KieContainer kieContainer; // 全局唯一容器

            public List<Rule> loadRules() {
                return ruleMapper.selectList(queryWrapper: null);
            }

            public void reload() {
                KieContainer kieContainer = this.loadContainerFromString(loadRules());
                this.kieContainer = kieContainer;
            }

            public KieContainer loadContainerFromString(List<Rule> ruleList) {
                KieServices ks = KieServices.Factory.get();
                KieRepository kr = ks.getRepository();
                KieFileSystem kfs = ks.newKieFileSystem();

                for (Rule rule : ruleList) {
                    String drl = rule.getContent();
                    kfs.write("/src/main/resources/" + drl.hashCode() + ".drl", drl);
                }

                KieBuilder kb = ks.newKieBuilder(kfs);
                kb.buildAll();

                KieContainer kieContainer = ks.newKieContainer(kr.getDefaultReleaseId());
                return kieContainer;
            }
        }
        ```
    *   **`CommandLineRunnerImpl.java`**:
        ```java
        @Component
        @Slf4j
        public class CommandLineRunnerImpl implements CommandLineRunner {
            @Autowired
            private ReloadDroolsRulesService reloadDroolsRulesService;

            @Override
            public void run(String... args) throws Exception {
                reloadDroolsRulesService.reload();
            }
        }
        ```
    *   **`RulesReloadController.java`**:
        ```java
        @RestController
        @RequestMapping("/rules")
        public class RulesReloadController {
            @Autowired
            private ReloadDroolsRulesService reloadDroolsRulesService;

            @PostMapping("/reload")
            public String reloadRules() {
                reloadDroolsRulesService.reload();
                return "Rules reloaded successfully.";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务类初始化与规则加载**
    *   **描述**: 讲师在 IntelliJ IDEA 中展示 `ReloadDroolsRulesService` 类。他首先解释了 `loadRules()` 方法的作用是查询数据库中的规则列表。接着，他演示了 `reload()` 方法，该方法会调用 `loadContainerFromString` 来创建一个新的 `KieContainer`，并将它赋值给类的静态变量 `kieContainer`，从而实现规则的热更新。

*   **场景二：动态加载规则的实现**
    *   **描述**: 讲师聚焦于 `loadContainerFromString` 方法。他详细解释了如何使用 `KieServices` 和 `KieFileSystem` 将规则内容写入到 `src/main/resources` 目录下，并通过 `KieBuilder` 构建规则。最后，他展示了如何使用 `KieContainer` 来加载这些规则。

*   **场景三：项目启动时自动加载规则**
    *   **描述**: 讲师在 Typora 中展示 `CommandLineRunnerImpl` 的代码。他解释了 `CommandLineRunner` 是 Spring Boot 提供的接口，用于在项目启动时执行特定的逻辑。他演示了如何在 `run()` 方法中调用 `reloadDroolsRulesService.reload()`，从而在项目启动时自动加载最新的规则。

*   **场景四：提供 HTTP 接口手动触发重载**
    *   **描述**: 讲师展示了 `RulesReloadController` 的代码。他解释了如何通过 `@PostMapping("/reload")` 注解创建一个 HTTP 接口，当用户访问该接口时，会触发 `reload()` 方法，从而手动更新规则。

*   **场景五：多窗口演示**
    *   **描述**: 在视频的最后，讲师切换到一个包含多个窗口的视图，展示了项目结构、IDEA 编辑器、Swagger UI 和 Navigat Premium 等工具。这表明整个系统是集成的，可以通过多种方式与规则引擎进行交互。
