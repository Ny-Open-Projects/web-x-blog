# 66-实现动态规则（实现步骤_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们实现动态规则,实现步骤

刚才我们是已经完成了第三步,对吧

就是把这个接口,如了Mapper接口已经创建好了

那接下来我们来看第四步

第四步就是需要来创建一个service

这个service它的作用就是用来重新加载我们数据库中的规则,对吧

并且根据我们加载出来的规则

重新把我们的KE container等等这些对象把它创建出来

好,那么接下来我们先来把这个类创建一下

就放在我们service.impl这个包下边

在这个下边来创建

然后咱们来加一个注释

这个就是重新加载什么呢

我们数据库中的规则,对吧

然后创建这个deroast相关对象

然后这是一个service

别忘了加一个service

注解

然后在这里边我们很显然应该会操作数据库,对吧

来查询我们这个rules那张表

所以说先把咱们刚才定义的这个如了Mapper接口把它注入一下

叫做如了Mapper

然后通过一个autoware是不是就注进来了

然后我们最终是想创建一个KE container,对吧

并且这个container对象我们希望它是一个全局的

所以在这儿我们定义成一个public static

静态的

那么对于这种对象全局只要有一个就可以

叫做KE container

这个对象不用我们注入

我们是需要把这个对象创建出来,对吧

把这个对象创建出来

然后复制给它就可以了

所以这个地方不需要一个autoware的

这是一个全局的

全局唯一这个叫做容器对象

用于什么呢

用于创建我们的session,对吧

然后来操作什么呢

操作我们的session,对吧

我们的session,对吧

把这个对象先来声明一下

然后在这里边我们很显然需要查询数据库,对吧

先把我们数据库里边

也就是我们如了这张表里边所有的内容给它查出来

咱们在这儿可以封装这么一个方法

这个方法叫做什么呢

叫做loadRules,对吧

定义这么一个方法

返回值肯定是个粒子的集合,对吧

因为可能有多条数据

因为我们这个如了表里边

大家要注意

如了表里边可能存的是多个规则,对吧

多个规则

所以说呢这里边呢

我们肯定是一个粒子集合

然后呢这里边是不是封装成如了这种对象

咱们这就叫什么呢

叫做loadRules

然后在这儿呢

我们是不是就可以调用我们这个什么如了Mapper,对吧

如了Mapper

点什么呢

它是不是有一个叫做SelectList

然后呢这儿是不是传条件

咱们条件是空

那就是查所有

好

就把所有的都查出来

然后呢直接返回就可以了

Return

OK

这个是查询我们数据库中啊

数据库中

所有的规则

然后呢给我们封装成粒子的集合这种形式

来返回

这个方法呢就已经写完了

这比较简单,对吧

然后接下来呢

我们需要再来提供一个方法

这个方法呢就叫做Reload

那么我们移掉这个方法呢

它就需要干什么呢

把我们这个KE Container对象是不是来

创建出来

所以重点呢就是这个方法

Public

然后Void

这个方法叫做Reload

重新加载

好

在这个方法内部呢

我们是不是就可以干什么呢

把我们创建好的那个Container

复制给咱们这个全局的这个静态的

这个Container对象就可以了

这个方法呢

这就是

重新这个创建

创建我们这个KE Container对象

对吧

对象

Reload

然后创建这个对象的过程呢

其实还是挺繁琐的

对吧

所以说呢我们可以啊

把这个方法呢再来封装一下

也就是说我们再来提供一个方法

这个方法呢就是干什么呢

就是根据我们这个方法的返回值

这时候把所有的这个规则内容查出来

根据这个作为条件

然后呢

把我们这个KE Container创建出来

然后我们在Reload这个方法上呢

直接掉下边这个方法就可以了

好

Public Container创建出来之后呢

我们就把这个KAE Container创建出来之后呢

Public

那么返回值呢

它肯定是一个KE Container对象了

对吧

然后这个方法呢

叫做什么呢

叫做Load Container

Container

然后呢

From吧

From String

好

就是根据字符串对吧

字符串类型的

然后呢

它这里边传进来的参数呢

很显然应该就是我们这个方法的返回值

对吧

这个方法的返回值

咱就叫做Ruler吧

Ruler List

好

这个是根据我们这个方法的返回值

我们这个什么呢

规则

规则内容

对吧

来创建这个KE Container对象

好

然后具体怎么创建一会儿

我们再来看这个方法

咱们暂时呢

先return一个Null

保证啊

它编译通过

然后呢

我们再reload这个方法这呢

其实就非常简单了

直接调用什么

Z4.2 Load

然后呢

这个地方是不是要给它传一个

List集合进去

List集合怎么获得呢

是不是调这个方法获得

所以我们在这呢

直接Load Ruler

好

然后呢

这样是不是就能返回一个KE Container

然后呢

把返回的这个对象呢

把它复制给我们这个静态的这个对象

就可以了

好

所以这就是什么呢

Z4.2 KE Container

等于我们返回的这个KE Container

对吧

好

那么这个方法就写完了

比较简单

重点呢

其实就是写这个方法

对吧

重点就是写这个方法

那么这个方法呢

就是什么呢

把我们这个List集合传进来

然后呢

按照我们这个

DRAWS给我们提供的一套API

对吧

然后呢

把它加载过来

最终呢

把这个KE Container

把它创建出来

那接下来呢

我们可以来简单写一下这个代码

首先呢

我们肯定要操作这个DRAWS的话呢

肯定是需要一个什么呢

肯定是需要一个KE Service

对吧

那么前面我们也都通过入门案例的方式

已经写过很多次了

就是KE什么

Service

Service

点什么呢

Factory

对吧

Factory

然后呢

点什么呢

Get

对吧

然后呢

这样的话

我是不是就获得了一个什么呢

这个KE Service

咱们就叫KS吧

然后接下来呢

我们是不是还需要来获得一个什么呢

Repository

其实就是仓库

对吧

这个仓库里边存储的

就是我们规则的内容

所以我们可以通过这个什么呢

通过这个KS点什么

Get一个Repository

这个得到的就是我们的仓库

这个仓库呢

我们就叫做

KR

KE Repository

KR

对吧

然后呢

我们还需要来创建一个什么呢

文件系统

对吧

文件系统对吧

那么也是通过这个KS

点什么呢

New一个什么

New一个

大家来看一下

叫做

KE

KE File

File System

文件系统

对吧

好

然后呢

咱们就叫KFYS吧

简单一点

好

这些都属于固定的代码

固定的代码

简单写一下就可以

然后接下来呢

我们就需要来

便利咱们这个

List集合了

便利这个List集合

然后RulerList.for

来便利它

把每一个规则

便利出来

对吧

但是它是封装成了

这种Ruler对象

然后呢

我们是就需要什么呢

通过我们这个

KFS

就是这个文件系统

对吧

这个是文件系统对象

文件系统这个对象呢

来写

就是将我们这个

从数据库里面查出来的

这个内容呢

把它写到我们这个

物理磁盘

首先呢

我们先来读取

它文件的内容

是不是就是

get content的这个字段

这就是我们

这个DRL文件的内容

好

然后呢

接下来我们就需要通过

这个什么呢

KFS对吧

就是文件系统这个对象了

调用它的write方法

来进行写

那么把这个内容

把它写到我们

本地磁盘的

某个目录下边

比如说我现在呢

就写在咱们这个

resource下边

这个Ruler

这个目录下边

或者是直接放在

这个resource下边

也可以

这都没有关系啊

好

那么我们在这来写一下

应该是在src对吧

然后呢

main

然后是resources

resources

ourc

别拼错了

那么第一个参数呢

是不是就是一个字符串

对吧

一个字符串

然后加上什么呢

加上我们这个文件名

这个文件名的话呢

咱们就使用这个DRL

点什么呢

hashcode

使用它的hashcode

作为文件名

然后呢再加上后缀

后缀的话呢

就是点DRL

好

那么我们就来写一下

然后写的内容呢

就是这个

你看这个write

第一个参数呢

是不是就是我们写完之后

这个文件名

包括它的路径对吧

然后呢

第二个呢

就是写的内容

写的内容呢

就是我们从数据库里面

读出来的这个内容

好

然后呢

进入放行环

是不是一个一个来写

写完之后呢

咱们就可以什么呢

通过我们这个ks对象啊

就是这个service对象对吧

ke service对象

然后呢来

创建什么呢

来new一个这个builder

其实就是一个构建器对吧

new一个ke builder

ke builder

ke builder

这个

好

然后呢

把我们这个文件系统对象

把它传进去

刚才经过放行环

它是不是把这些内容

都写到我们磁盘上了

对吧

然后呢

我们在这呢

就可以通过这个构建器啊

来构建

你看得到了一个什么呢

kb对吧

就是ke builder

好

就是kb

然后呢

我们来调用kb点什么呢

它这里边有个叫做build all

构建所有

那么

它就会啊

把我们这个文件系统

整个构建出来

好

构建出来之后呢

咱们是不是就可以啊

来创建我们这个什么呢

来创建我们这个container了

咱们通过什么呢

通过我们这个ke service

也就是这个ks对吧

它里边是不是有一个方法

叫做new一个ke

ke container

你看

然后呢

它这里边是不是要

我们传入一个什么呢

传入一个这个release id对吧

那这个release id呢

是什么呢

我们就可以通过这个kr

也就是这个release id

这个reposit对象

来获得什么呢

获得它default

release id

这样的话呢

我们就得到了一个ke container

然后呢

把这个ke container对象返回就可以了

当然了

这段代码呢

大家其实大概看一下就可以

因为也都属于模板化的代码

主要内容就是什么呢

只要大家能够读懂

它主要的就是什么呢

从我们数据库里面

加载出来的这个粒子集合

对吧

然后呢

把它循环读解

最终呢

把我们这个文件系统对象

创建好

把它写到我们本地磁盘

然后基于本地磁盘

这一份这个规则文件

然后呢

再把这个ke container对象

创建出来

大概就是这么一个套路

好

那么这是关于咱们

这个方法的编写

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在 Spring Boot 项目中实现动态加载 Drools 规则的功能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个 `ReloadDroolsRulesService` 服务类，该服务负责从数据库中查询规则、将规则内容写入文件系统、并使用 Drools 的 `KieServices` 和 `KieBuilder` API 重新构建一个 `KieContainer` 对象，从而实现规则的热加载。整个过程是面向 Java 开发者的实战教学，重点在于代码实现和 API 调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程介绍与项目背景。讲师展示了项目的大纲，当前位于“第4章 订单中心服务数据模型”下的“8. 实现动态规则”部分，具体是“8.2 实现步骤”。
*   **00:05 - 00:15**: 介绍目标服务。讲师在代码编辑器中展示了 `ReloadDroolsRulesService` 类的定义，其目的是“重新加载数据库中的规则”。
*   **00:15 - 00:25**: 定义服务类成员。讲师为 `ReloadDroolsRulesService` 类添加了两个成员变量：一个 `@Autowired` 注入的 `RuleMapper` 接口实例，用于查询数据库；另一个 `static KieContainer`，用于存储最终创建的规则容器。
*   **00:25 - 00:35**: 实现 `loadRules` 方法。讲师编写了 `loadRules()` 方法，该方法通过 `ruleMapper.selectList(null)` 查询数据库中所有的规则对象，并返回一个 `List<Rule>`。
*   **00:35 - 00:45**: 实现 `reload` 方法。讲师编写了 `reload()` 方法，该方法调用 `loadContainerFromString(loadRules())` 来重新加载规则，并将返回的 `KieContainer` 赋值给类的静态成员变量 `this.kieContainer`。
*   **00:45 - 00:55**: 实现 `loadContainerFromString` 方法。讲师开始编写 `loadContainerFromString(List<Rule> ruleList)` 方法，该方法是核心，负责将规则内容写入文件并构建 `KieContainer`。
*   **00:55 - 01:05**: 初始化 Drools 服务。在 `loadContainerFromString` 方法中，讲师使用 `KieServices.Factory.get()` 获取 `KieServices` 实例，并通过 `getRepository()` 获取 `KieRepository`。
*   **01:05 - 01:15**: 创建文件系统。讲师使用 `KieRepository` 的 `newKieFileSystem()` 方法创建一个 `KieFileSystem` 实例，用于将规则文件写入磁盘。
*   **01:15 - 01:25**: 遍历规则并写入文件。讲师使用 `for` 循环遍历 `ruleList`，调用 `rule.getContent()` 获取规则的文本内容，并使用 `KieFileSystem` 的 `write` 方法将规则写入到 `src/main/resources` 目录下，文件名采用 `规则内容的hashCode + .drl` 的格式。
*   **01:25 - 01:35**: 构建 KieContainer。讲师使用 `KieServices` 的 `newKieBuilder(kfs)` 创建一个 `KieBuilder`，然后调用 `buildAll()` 方法进行编译。接着，使用 `ks.newKieContainer(kr.getDefaultReleaseId())` 创建并返回一个 `KieContainer` 对象。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   项目大纲：`品达物流TMS项目` -> `第4章 订单中心服务数据模型` -> `8. 实现动态规则` -> `8.2 实现步骤`。
    *   服务类注释：`// 重新加载规则`，`// 全局唯一容器对象，用于创建Session操作Drools`。
    *   方法注释：`// 查询数据库中所有的规则`，`// 重新创建KieContainer对象`，`// 根据规则内容创建KieContainer对象`。
*   **代码关键内容**:
    *   **接口定义**:
        ```java
        @Mapper
        public interface RuleMapper extends BaseMapper<Rule> {
        }
        ```
    *   **服务类定义**:
        ```java
        @Service
        public class ReloadDroolsRulesService {
            @Autowired
            private RuleMapper ruleMapper;
            public static KieContainer kieContainer;
        }
        ```
    *   **核心方法 `loadRules`**:
        ```java
        public List<Rule> loadRules() {
            return ruleMapper.selectList(queryWrapper: null);
        }
        ```
    *   **核心方法 `reload`**:
        ```java
        public void reload() {
            KieContainer kieContainer = this.loadContainerFromString(loadRules());
            this.kieContainer = kieContainer;
        }
        ```
    *   **核心方法 `loadContainerFromString`**:
        ```java
        public KieContainer loadContainerFromString(List<Rule> ruleList) {
            KieServices ks = KieServices.Factory.get();
            KieRepository kr = ks.getRepository();
            KieFileSystem kfs = ks.newKieFileSystem();
            for (Rule rule : ruleList) {
                String drl = rule.getContent();
                kfs.write("src/main/resources" + drl.hashCode() + ".drl", drl);
            }
            KieBuilder kb = ks.newKieBuilder(kfs);
            kb.buildAll();
            KieContainer kieContainer = ks.newKieContainer(kr.getDefaultReleaseId());
            return kieContainer;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与服务创建 (00:00-00:15)**:
    *   讲师在 IntelliJ IDEA 中打开项目，展示了 `ReloadDroolsRulesService.java` 文件。
    *   讲师在类中添加了 `@Service` 注解，并定义了 `@Autowired` 的 `RuleMapper` 成员变量和 `static KieContainer` 成员变量。
*   **场景二：查询规则 (00:15-00:25)**:
    *   讲师在 `loadRules` 方法中调用 `ruleMapper.selectList(null)`，并用 `return` 语句返回查询结果。
*   **场景三：重新加载规则 (00:25-00:35)**:
    *   讲师在 `reload` 方法中调用 `loadContainerFromString(loadRules())`，并将返回的 `KieContainer` 赋值给静态成员变量 `this.kieContainer`。
*   **场景四：构建规则容器 (00:45-01:35)**:
    *   讲师在 `loadContainerFromString` 方法中，使用 `KieServices.Factory.get()` 获取服务工厂。
    *   讲师使用 `ks.getRepository()` 获取 `KieRepository`。
    *   讲师使用 `ks.newKieFileSystem()` 创建 `KieFileSystem`。
    *   讲师使用 `for` 循环遍历规则列表，调用 `rule.getContent()` 获取内容，并用 `kfs.write(...)` 将规则写入文件系统。
    *   讲师使用 `ks.newKieBuilder(kfs)` 创建 `KieBuilder`，并调用 `buildAll()` 方法进行编译。
    *   讲师使用 `ks.newKieContainer(kr.getDefaultReleaseId())` 创建并返回 `KieContainer`。
*   **场景五：代码补全与调试 (00:05-01:35)**:
    *   在整个过程中，讲师多次使用 IntelliJ IDEA 的智能提示（如 `Ctrl+Shift+Space`）来补全方法名和参数，例如 `selectList`、`newKieFileSystem`、`write`、`newKieBuilder`、`buildAll` 等。
    *   讲师在代码中添加了中文注释，以解释每一部分的功能。

---
