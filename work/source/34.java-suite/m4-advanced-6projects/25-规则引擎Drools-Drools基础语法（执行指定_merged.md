# 25-规则引擎Drools-Drools基础语法（执行指定 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看D-Rose基础语法

那么第六个小节呢,叫做执行指定规则

这个到底是什么意思呢?我们一块来看一下

通过前面的案例呢,咱们可以看到

我们在调用规则代码的时候呢

满足条件的规则是不是都会被执行到

比如说我们刚才,这个地方

你看啊,我们满足条件的是不是有三个规则

那么你可以看到这三个规则是不是都触发了

那么现在呢,我们,如果我们只想执行什么呢

其中的某个规则应该如何来实现

也就是说我们并不希望满足条件的所有的规则都执行到

而是什么呢,我只想执行指定的某个规则

那么这个我们如何实现呢

D-Rose呢,给我们提供的方式是什么呢

是通过过滤器啊,规则过滤器来实现执行指定的规则

那么实际上对于我们的规则文件呢

不用做任何修改

我们只需要来修改什么呢

咱们的Java代码就可以了

那么具体怎么来修改

那么我们来看一下

咱们呢,可以把这个,整个这个代码呢,来复制一下

原先这个呢,我就不再动它了

对吧

上面呢,我们Test2呢,主要测试的是我们这些比较操作符

对不对,这个是测试的我们的比较操作符

然后这个呢,我们希望来测试的是我们执行指定规则

咱们在这里面呢,把代码来改造一下

但是这些呢,我们就不管了

那么我们需要改造的是哪个代码呢

注意看,就是这个

咱们现在呢,调用的是session.failall

Rules,对吧,这个方法

那么调用这个方法,它的作用是什么呢

就是触发规则

然后呢,根据我们这个前面讲过的

进行模式匹配,对吧

只要匹配成功的,所有的规则是不是都会被执行到

那么现在呢,我们来看一下

其实呢,这个方法呢

还有另外几个啊,就是跟它是同名的

但是呢,是有参数的

咱们调用的是当前这个,对吧

注意看,我现在是到它的原版里边来了

failall, rules

那么除了它之外呢,你看

这儿是不是还有这么一个带参数的

那么我们需要来传进来一个什么呢

叫做agenda filter

大家还记得agenda是什么意思吗

agenda是不是翻译过来叫做议程,对吧

当时我们解释啊,它的含义是什么呢

就是当我们这些规则匹配成功之后

是不是会放到我们的agenda

这个区域

所以说啊,agenda里边存放的就是我们这些

已经匹配成功的规则,对吧

好,那么现在呢,我们需要这么一个规律器

通过这个规律器呢

我们就可以来指定啊

指示执行某个规则

或者是某一些规则

但是呢,注意看啊

它其实是一个接口,对吧

那么我们要给它传进来的

应该是它的一个具体的实现类

具体的实现类

那么具体呢

我们可以选中它

然后呢,来看一下

它的实现类

是不是一种规则呢,就是它的实现类,对吧

是不是有这么多

在这呢,我们首先来看这个

叫做rulerNameEcosAgendaFilter

这个是什么意思呢

这个Ecos,重点看这

Ecos是不是就是相等啊

就是指定名称啊,指定名称

指定名称,就是我们要执行某一个

哪一个规则

你把那个规则的Name给我传进来

就可以了

所以说呢,咱们这个Java代码改造起来呢

其实还是非常简单的

在这个方法里边,我们直接给它传一个什么呢

NuE

这个filter对象,对吧

当然我们需要来导入一下,import一下

然后呢,把这个Name给它传进去

哎,你看啊

它是不是要求我们传进来一个Name

这个Name是什么Name呢

就是规则的名称

比如说,注意看啊

咱们现在呢

可以这样来验证一下

就是什么呢

我暂时先把这个去掉

CtrlX,我先把它剪切掉

然后呢

我们再来执行一下

现在呢

因为我

没有进行这个过滤,对吧

规则的过滤

所以说呢

只要匹配成功的规则呢

都会被执行到

现在呢

你可以看到这三个规则是不是都执行了

好

现在呢

我把它重新放到这来

然后呢

把这个规则的名称啊

给它放到这

规则的名称

这是不是这个NodeContents

这个规则

好

在这呢

我们最好还是来检查一下

因为我们毕竟这个是控制台输出的

对吧

它有可能并不是我们真正的那个规则的名称

刚才我这个考的应该是NodeContents

是不是应该是这个规则

所以这儿指定的应该是规则的名称

规则的名称

那这样的话

我们再来执行一下这个单元测试

大家来看一下

稍等一下

你看现在呢

是不是只有这一个规则触发了

而我们刚才看到是不是有三个规则触发

那么为什么变成了一个呢

就是因为我们现在是不是指定了是这个规则

那这样的话

即使其他的规则能够匹配成功

因为我们这儿是不是使用到了过滤器

所以说匹配成功的那些规则

它也不会执行

它只有可能会执行这个

但是需要再来强调一下

就是说这个规则一定会触发吗

不一定

你还是要看这个规则到底能不能匹配成功

对吧

前提是它必须得匹配成功

而且我们在这儿又指定了它的名字

这个规则是不是才会触发

这个呢

我们用的这个规则器叫做什么呢

RulerNameEcos

真的

这个Ecos是不是就是等值的

等值的

那比如说我现在呢

我想执行某一些规则

并不是所有的

比如我们希望要执行的是什么呢

是这个Ruler下滑线开始的这些规则

但是咱们现在这几个规则

其实都是这样命名的

这个倒无所谓了

就是什么呢

我们刚才看到了

这个接口

它其实的它的实现类是不是很多呀

我们可以大概来看一下

RulerNameAnswerWithAgendaFilter

其实从这个命名上大家应该也能看出来

这个限制的是什么呢

是不是必须是以某某结尾

对吧

以某个字符串结尾的这样的规则

然后呢

这个Ecos刚才我们演示了

对吧

等值的

然后Matches呢

这个就类似于我们的这个证则表达式的

对不对

然后这个是一个序列化的

然后这个呢

StartWith

这个是以某个字符串开始的

对吧

那么咱们可以来试一下这个

比如说我现在把这个来改造一下

我先把它贴这儿

这句话呢

我们可以暂时给它注释起来

我希望把这个代码保留起来

所以说我就不在它这儿直接改了

那么我们可以给它注释起来

然后呢

把咱们这个规则的

把这个过滤器拿过来

你看这个呢

是叫做StartWith

就是以什么什么开始

对吧

以什么什么开始

比如说以这种Ruler向下滑线开始

然后呢

咱们再来执行一下

好

你看这三个规则是不是又都触发了

因为什么呢

因为这三个规则是不是

它都是以这个Ruler向下滑线开始的

那比如说我现在啊

我给它改造一下

刚才我们看啊

都是谁触发的

是这个NOTContent这个触发了

对吧

然后呢

这个NOTMembersOf

NOTMatches

这三个触发的

三个加这个NOT的

对吧

你比如说这个我加给NOTMatches

这个A

然后呢

这个呢

NOTMembers这个我加个B

好

然后呢

这个呢

我就不改了

可以吧

咱们来看一下

那么现在的话

我很明显这两个规则

我刚才改的这两个规则

是不是已经不满足要求了

好

然后呢

我们再来执行

哎

你看现在它是不是只有这一个规则触发了

好

这就是我们提供的这种啊

通过这种规则过滤器啊

这我还撤回来啊

好

撤回来

这就是我们提供的

哎

这种规则过滤器来执行什么呢

来执行指定的规则啊

执行指定规则

在这呢

我们可以来加一个注释

哎

使用我们这个框架啊

Dirose框架提供的什么呢

提供的规则过滤器啊

来执行什么

指定规则

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一个关于 **Drools 规则引擎** 的技术演示，主要讲解如何在 Java 项目中使用 Drools 进行规则匹配，并重点演示了如何通过 **Agenda Filter**（议程过滤器）来精确控制规则的触发顺序和条件。演示通过一个名为 `ComparisonOperatorEntity` 的事实对象，结合 `rule_comparison_matches`、`rule_comparison_not_matches`、`rule_comparison_not_memberOf` 等规则，展示了 `matches`、`not matches`、`not memberOf` 等比较操作符的用法。视频中还展示了如何通过 `RuleNameEqualsAgendaFilter` 来指定只触发特定名称的规则，以及如何通过 `session.fireAllRules()` 来触发所有规则。整个过程在 IntelliJ IDEA 开发环境中进行，代码和规则文件均清晰可见。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **章节 1: 项目环境与基础规则测试 (0:00 - 0:30)**
    *   展示了项目结构，包括 `DroolsTest.java` 和 `comparisonOperator.drl` 文件。
    *   演示了 `test20` 方法，创建 `KieServices`、`KieContainer` 和 `KieSession`。
    *   创建并设置了一个 `ComparisonOperatorEntity` 事实对象。
    *   在终端中运行测试，成功触发了 `rule_comparison_notcontains` 和 `rule_comparison_not_matches` 规则。

*   **章节 2: 引入 Agenda Filter 概念 (0:30 - 1:00)**
    *   通过查看 `AgendaFilter.java` 的源码，讲解了 `AgendaFilter` 接口的作用：它用于过滤即将触发的规则匹配项。
    *   重点讲解了 `accept(Match match)` 方法，该方法返回 `true` 表示允许规则触发，返回 `false` 则阻止。

*   **章节 3: 使用 RuleNameEqualsAgendaFilter (1:00 - 1:30)**
    *   在 `test20` 方法中，将 `session.fireAllRules()` 的参数改为 `new RuleNameEqualsAgendaFilter("rule_comparison_notcontains")`。
    *   这样做是为了只让名称为 `rule_comparison_notcontains` 的规则触发，其他规则将被过滤掉。

*   **章节 4: 规则文件内容与操作符详解 (1:30 - 2:00)**
    *   展示了 `comparisonOperator.drl` 文件中的规则定义。
    *   详细解释了 `matches`、`not matches`、`not memberOf` 等操作符的含义和用法。
    *   通过修改规则中的正则表达式（如 `王.*`）来演示规则匹配的灵活性。

*   **章节 5: 代码与规则的关联与执行 (2:00 - 2:30)**
    *   回到 `DroolsTest.java`，演示了如何通过 `session.insert(fact)` 将事实对象插入到规则引擎中。
    *   通过 `session.fireAllRules()` 触发规则匹配。
    *   展示了终端输出，确认规则被成功触发。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 (Java):**

    ```java
    // 获取Kie容器对象
    KieServices kieServices = KieServices.Factory.get();
    KieContainer kieContainer = kieServices.newKieClasspathContainer();
    // 从Kie容器对象中获取会话对象
    KieSession session = kieContainer.newKieSession();

    // Fact对象，事实对象
    ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
    fact.setNames("李四");

    List<String> list = new ArrayList<String>();
    list.add("张三");
    list.add("李四"); // 该行代码在演示中被注释或修改

    fact.setList(list);
    session.insert(fact);

    // 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
    session.fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"));
    ```

*   **关键代码片段 (Drools 规则文件):**

    ```drl
    // 测试比较操作符 matches
    rule "rule_comparison_matches"
    when
        ComparisonOperatorEntity(names matches "王.*")
    then
        System.out.println("规则：rule_comparison_matches触发了...");
    end

    // 测试比较操作符 not matches
    rule "rule_comparison_not_matches"
    when
        ComparisonOperatorEntity(names not matches "王.*")
    then
        System.out.println("规则：rule_comparison_not_matches触发了...");
    end

    // 测试比较操作符 not memberOf
    rule "rule_comparison_not_memberOf"
    when
        ComparisonOperatorEntity(names not memberOf list)
    then
        System.out.println("规则：rule_comparison_not_memberOf触发了...");
    end
    ```

*   **关键接口定义 (Java):**

    ```java
    package org.kie.api.runtime.rule;

    public interface AgendaFilter {
        /**
         * Determine if a given match should be fired.
         * @param match The match that is requested to be fired
         * @return boolean value of "true" accepts the match for firing.
         */
        boolean accept(Match match);
    }
    ```

*   **关键类/接口 (Java):**

    *   `KieServices`: Drools 的核心服务类，用于获取容器和会话。
    *   `KieContainer`: 用于加载规则文件并创建会话。
    *   `KieSession`: 规则引擎的执行环境，用于插入事实和触发规则。
    *   `AgendaFilter`: 用于过滤规则匹配项的接口。
    *   `RuleNameEqualsAgendaFilter`: `AgendaFilter` 的一个具体实现，用于根据规则名称过滤。

---

### 4) 关键场景与演示描述

*   **场景 1: 基础规则匹配演示**
    *   **描述**: 开发者在 `DroolsTest.java` 中编写了 `test20` 方法，创建了 `KieSession`，并插入了一个 `ComparisonOperatorEntity` 事实对象。
    *   **演示**: 通过 `session.fireAllRules()` 触发规则，终端输出显示 `rule_comparison_notcontains` 和 `rule_comparison_not_matches` 规则被触发，证明了规则引擎的基本功能。

*   **场景 2: Agenda Filter 的引入与使用**
    *   **描述**: 开发者切换到 `AgendaFilter.java` 文件，查看其接口定义，理解其作用。
    *   **演示**: 在 `test20` 方法中，将 `session.fireAllRules()` 的参数改为 `new RuleNameEqualsAgendaFilter("rule_comparison_notcontains")`。这使得只有名称为 `rule_comparison_notcontains` 的规则被触发，其他规则被过滤掉。这展示了如何通过过滤器来控制规则的执行。

*   **场景 3: 规则文件内容与操作符详解**
    *   **描述**: 开发者打开 `comparisonOperator.drl` 文件，展示其中定义的规则。
    *   **演示**: 通过修改规则中的正则表达式（如 `王.*`），演示了如何通过 `matches`、`not matches`、`not memberOf` 等操作符来控制规则的匹配条件。

*   **场景 4: 事实对象与规则的关联**
    *   **描述**: 开发者在 `DroolsTest.java` 中创建了一个 `List<String>`，并将其设置到 `ComparisonOperatorEntity` 事实对象中。
    *   **演示**: 通过 `session.insert(fact)` 将事实对象插入到规则引擎中，然后通过 `session.fireAllRules()` 触发规则，终端输出显示规则被触发，证明了事实对象与规则之间的关联。

*   **场景 5: 规则执行结果的验证**
    *   **描述**: 视频最后展示了终端的输出结果。
    *   **演示**: 输出显示了 `rule_comparison_notcontains` 和 `rule_comparison_not_matches` 规则被触发，验证了规则引擎的正确性。
