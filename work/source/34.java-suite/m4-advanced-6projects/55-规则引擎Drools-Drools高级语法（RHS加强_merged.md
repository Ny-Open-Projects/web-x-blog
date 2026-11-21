# 55-规则引擎Drools-Drools高级语法（RHS加强 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来呢,我们继续来看RHS部分的加强。

刚才我们介绍的是D-Rose这个内置对象的第一个方法,叫做Health,对吧?

接下来我们要看的叫做Get Working Memory。

这个方法呢,它的作用是返回我们工作内存这么一个对象。

好,你看我们还是调用这个内置对象D-Rose,它有一个Get Working Memory这么一个方法,对吧?

然后呢,我们可以来看一下,这就比较简单了,我就直接在这写了。

我们就不用单独再去编写一个规则了,咱们直接在这来调用什么呢?

D-Rose,你看,Get Working Memory。

好,然后呢,我们可以让它返回一下,你看它返回的其实就是一个Working Memory这么一个对象。

然后呢,我们可以在这来输出一下。

而这个对象的话,通过输出呢,你会发现它其实是一个什么呀,KIE Session对象。

而这个Working Memory呢,

它其实是一个接口,还没有?

它其实是一个接口,而它的实现类呢,大家可以看到,就有我们这个Session对象。

但是这个呢,是Stateful Knowledge Session,IMPL,对吧?

它其实代表的是一个什么呢?

有状态的Session这么一个对象。

但是这里边呢,定义的这个类呢,它其实实现的接口就更多了,对吧?

好,你看它这里边属性也非常多。

所以说呢,我们拿到这个Working Memory对象之后啊,

这里边相应的这些属性呢,

其实都可以拿到,都可以拿到。

因为这个属性很多啊,我们就不再一个一个测试了。

咱们呢,直接在这儿来,在我们规则文件里面,

就可以通过这种方式来取到我们这个Working Memory对象。

然后呢,有了Working Memory对象之后呢,

我们想要什么样的对象呢,就可以直接调用Get的方法。

你看,Get它这个什么Environment,

获得我们相关的这个环境对象。

还有这个什么呢,Agenda,是不是就是我们的议程啊,对吧?

还有我们这个,也能看出来吧,

这个是Global,是不是获得相应的,

这个全局变量这个对象,对吧?

还有我们的这个知识库对象,等等啊,

这里边Get的方法非常多。

你看,还可以获得我们的Get Query Results,对吧?

通过这个查询的这个名称,

然后呢,可以去调用我们这个查询的结果。

那这里边的这些方法非常多。

好,这些呢,我们就直接啊,先把这个去掉。

咱们先来执行一下。

还是执行咱们刚才这个,

呃,

测试的,测试方法就可以。

好,执行一下。

来看一下我们控制台,你看,

下面它其实输出的是这个KIE Session 0,对吧?

因为它的,这是它的tools string方法。

那么这是我们通过derose,

这个内置对象,然后调用它的Get Working Memory这个对象,

然后呢,来获得我们的这个什么,获得,

获得工作什么呀,内存对象。

而这个工作内存对象,它其实本质上啊,

是一个什么呀,一个绘画对象。

是一个Session对象,对吧?

KIE Session。

好,那么拿到这个对象之后呢,我们就可以调用它这里边相关的这些,呃,方法。

你看,这个Working Memory这是我们的接口定义,对吧?

在接口里边呢,你看,这是定义的一些set方法,也有get方法,对吧?

get global,还有我们的environment,这是不是我们的环境,对吧?

相应的一些环境。

好,然后呢,这个是不是执行?

好,然后呢,这个是不是执行?

这fireAllRules,对吧?

这是我们进行这个规则要执行,对吧?

触发的时候可以调用这个方法。

你看,咱们当时是不是全都是调用的这个Session对象的这个fireAllRules这个方法。

而这个Working Memory呢,其实就是我们对应的接口。

而这个Session呢,就是它的实现类。

是这么一个继承关系。

好,这个呢,是关于咱们这个getWorkingMemory这个方法,通过它呢,返回工作内存对象。

有了这个对象呢,

我们可以从这个对象出发,对吧?

调用相关的一些get的方法来获得其他的一些对象。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于 **Drools 规则引擎** 的技术教学视频，主要聚焦于 **工作内存（Working Memory）** 和 **规则执行控制** 的高级特性。讲师通过 IntelliJ IDEA 编辑器展示 Java 代码，并结合 Typora 中的 PPT 文档进行讲解。核心内容包括：
*   **`getWorkingMemory()` 方法**：用于获取当前规则引擎会话的工作内存对象，该对象是规则匹配和事实操作的核心载体。
*   **`halt()` 方法**：用于立即终止当前规则的执行，并阻止后续所有规则的触发，常用于调试或控制流程。
*   **`getRule()` 方法**：用于获取已加载规则的元数据对象。
*   **`StatefulKnowledgeSession` 类**：讲解了其内部结构和关键方法，如 `getKnowledgeBase()`、`getProcessInstance()` 等，以帮助理解规则引擎的底层工作原理。
*   **全局变量（Global）**：演示了如何在规则文件中定义全局变量，并在 Java 代码中通过 `setGlobal` 方法进行设置和使用。
*   **规则激活与执行**：通过 `fireAllRules` 方法触发规则，并展示了如何通过 `dispose` 方法关闭会话。

整个视频旨在帮助开发者深入理解 Drools 的核心机制，特别是工作内存的管理与规则执行的控制流。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序进行的划分：

*   **00:00 - 00:05**: 开场，展示 Typora 文档的目录结构，定位到“6.5.2 getWorkingMemory”章节。
*   **00:05 - 00:15**: 讲解 `getWorkingMemory()` 方法的作用，并在 IntelliJ IDEA 中展示对应的 Java 代码示例。
*   **00:15 - 00:25**: 展示 `StatefulKnowledgeSessionImpl` 类的源码，重点讲解其继承关系和内部成员变量，如 `kBase`、`agenda`、`lock` 等。
*   **00:25 - 00:35**: 继续浏览 `StatefulKnowledgeSessionImpl` 的源码，重点讲解其构造函数和关键成员变量。
*   **00:35 - 00:45**: 在 Java 代码中调用 `getWorkingMemory()` 方法，并通过 `getEnvironment()` 方法获取 `Environment` 对象，进而调用 `getKnowledgeBase()` 方法。
*   **00:45 - 00:55**: 展示 `getProcessInstance(long id)` 方法的调用，用于获取特定的流程实例。
*   **00:55 - 01:05**: 演示如何设置全局变量，代码中使用 `session.setGlobal(...)` 方法。
*   **01:05 - 01:15**: 展示 `session.fireAllRules(...)` 方法，用于激活并执行所有匹配的规则。
*   **01:15 - 01:25**: 展示 `session.dispose()` 方法，用于关闭规则会话。
*   **01:25 - 01:35**: 回到 Typora 文档，讲解 `halt()` 方法的作用，并在代码中展示其调用。
*   **01:35 - 01:45**: 展示 `getRule()` 方法的代码示例，用于获取规则对象。
*   **01:45 - 01:55**: 总结本节内容，强调 `getWorkingMemory()` 和 `halt()` 方法的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文档标题**：`视频Drools讲义.md - Typora`
*   **章节标题**：
    *   `6.5.2 getWorkingMemory`
    *   `6.5.3 getRule`
*   **关键注释**：
    *   `//当前规则并不会触发，因为上面的规则调用了halt方法导致后面所有规则都不会执行`
    *   `//获得工作内存对象，本质上是一个WorkingMemory对象`
    *   `//当前方法表示终止后面所有规则的执行`

#### 代码关键内容

*   **规则文件 (`testrhs1.drl`)**
    ```drl
    rule "rule_rhs_1"
    when
    then
        System.out.println("规则: rule_rhs_1触发了...");
        WorkingMemory workingMemory = drools.getWorkingMemory();
        System.out.println(workingMemory.get());
    end

    rule "rule_rhs_2"
    when
    then
        System.out.println("规则: rule_rhs_2触发了...");
    end
    ```

*   **Java 代码 (`DroolsTest.java`)**
    ```java
    // 设置全局变量
    List<String> list = new ArrayList<String>();
    list.add("itheima");
    session.setGlobal(identifier: "gList", list);

    session.setGlobal(identifier: "userService", new UserService());

    // 激活规则
    session.fireAllRules(new RuleNameStartsWithAgendaFilter(prefix: "rule_rhs"));

    // 关闭会话
    session.dispose();
    ```

*   **`StatefulKnowledgeSessionImpl` 类关键代码**
    ```java
    public class StatefulKnowledgeSessionImpl extends AbstractRuntime
        implements StatefulKnowledgeSession,
                   WorkingMemoryEntryPoint,
                   InternalKnowledgeRuntime,
                   KieRuntime,
                   KieRuntimeEventManager,
                   EventSupport,
                   RuleEventManager,
                   ProcessEventManager,
                   CorrelationAwareProcessRuntime,
                   Externalizable {
    // ... 其他成员变量和方法 ...
    }
    ```

*   **`WorkingMemory` 接口关键方法**
    ```java
    Object getGlobal(String identifier);
    Environment getEnvironment();
    void setGlobalResolver(GlobalResolver globalResolver);
    ```

---

### 4) 关键场景与演示描述

*   **场景一：工作内存对象获取**
    *   **描述**：讲师在 IntelliJ IDEA 中编写 Java 代码，通过 `drools.getWorkingMemory()` 方法获取工作内存对象，并将其赋值给 `workingMemory` 变量。
    *   **演示**：在代码中调用 `workingMemory.get()` 方法，并打印其内容，以展示工作内存的内部状态。

*   **场景二：规则执行控制**
    *   **描述**：讲师在规则文件中定义了两个规则 `rule_rhs_1` 和 `rule_rhs_2`。
    *   **演示**：在 `rule_rhs_1` 中调用 `drools.halt()` 方法，演示其作用是立即终止当前规则的执行，并阻止后续所有规则的触发。在 `rule_rhs_2` 中，由于 `halt()` 方法的调用，该规则不会被执行。

*   **场景三：全局变量设置**
    *   **描述**：讲师在 Java 代码中使用 `session.setGlobal()` 方法设置全局变量。
    *   **演示**：代码中设置了两个全局变量，一个为 `List<String>` 类型，另一个为 `UserService` 类型，并在规则文件中引用这些变量。

*   **场景四：规则激活与执行**
    *   **描述**：讲师在 Java 代码中调用 `session.fireAllRules()` 方法。
    *   **演示**：该方法会自动匹配规则文件中的规则，并执行匹配成功的规则。在演示中，`rule_rhs_1` 会执行，而 `rule_rhs_2` 由于 `halt()` 方法的调用而不会执行。

*   **场景五：会话关闭**
    *   **描述**：讲师在 Java 代码中调用 `session.dispose()` 方法。
    *   **演示**：该方法用于关闭当前的规则会话，释放相关资源。在演示中，该方法在规则执行完成后被调用。

*   **场景六：`StatefulKnowledgeSessionImpl` 类源码浏览**
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `StatefulKnowledgeSessionImpl.java` 文件，浏览其源码。
    *   **演示**：重点讲解了该类的继承关系、内部成员变量（如 `kBase`、`agenda`、`lock`）和构造函数，以帮助理解规则引擎的底层实现。

*   **场景七：`WorkingMemory` 接口方法调用**
    *   **描述**：讲师在 Java 代码中调用 `getEnvironment()` 方法。
    *   **演示**：通过 `getEnvironment()` 方法获取 `Environment` 对象，并调用其 `getKnowledgeBase()` 方法，以获取当前会话的 `KnowledgeBase` 对象。

---

以上是根据视频画面进行的结构化技术分析报告。希望对您有所帮助。
