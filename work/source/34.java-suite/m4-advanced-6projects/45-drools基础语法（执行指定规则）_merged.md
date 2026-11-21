# 45-drools基础语法（执行指定规则） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看D-Rose基础语法。

那么第六个小节呢,叫做执行指定规则。

这个到底是什么意思呢?

我们一块来看一下啊。

通过前面的案例呢,咱们可以看到,我们在调用规则代码的时候呢,满足条件的规则是不是都会被执行到。

比如说我们刚才,这个地方,你看啊,我们满足条件的是不是有三个规则。

那么你可以看到这三个规则是不是都触发了。

那么现在呢,我们,如果我们只想执行什么呢?

其中的某个规则应该如何来实现。

也就是说,我们并不希望满足条件的所有的规则都执行到,而是什么呢?

我只想执行指定的某个规则。

那么这个我们如何实现呢?

D-Rose呢,给我们提供的方式是什么呢?

是通过过滤器啊,规则过滤器来实现执行指定的规则。

那么实际上对于我们的规则文件呢,不用做任何修改。

我们只需要来修改什么呢?

咱们的Java代码就可以了。

那么具体怎么来修改?

那么我们来看一下。

咱们呢,可以把这个,整个这个代码呢,来复制一下。

原先这个呢,我就不再动它了,对吧?

上面呢,我们Test2呢,主要测试的是我们这些比较操作符,对不对?

这个是测试的我们的比较操作符。

然后这个呢,我们希望来测试的是我们执行指定规则。

咱们在这里面呢,把代码来改造一下。

但是这些呢,我们就不管了。

那么我们需要改造的是哪个代码呢?

注意看,就是这个。

咱们现在呢,调用的是Session.FairAll,Rules,对吧?

这个方法。

那么调用这个方法,它的作用是什么呢?

就是触发规则。

然后呢,根据我们这个前面讲过的,进行模式匹配,对吧?

只要匹配成功的,所有的规则是不是都会被执行到。

那么现在呢,我们来看一下。

其实呢,这个方法呢,

它还有另外几个啊,就是跟它是同名的,但是呢,是有参数的。

咱们调用的是当前这个,对吧?

注意看,我现在是到它的原版里面来了。

FairAll,Rules。

那么除了它之外呢,你看,

这儿是不是还有这么一个啊,带参数的。

那么我们需要来传进来一个什么呢?

叫做Agenda Filter。

大家还记得Agenda是什么意思吗?

Agenda是不是翻译过来叫做议程,对吧?

当时我们解释啊,它的含义是什么呢?

就是当我们这些规则匹配成功之后,

是不是会放到我们的Agenda。

那个区域。

所以说啊,Agenda呢,里边存放的就是我们这些已经匹配成功的规则,对吧?

好,那么现在呢,我们需要这么一个规律器。

通过这个规律器呢,我们就可以来指定啊,

指示执行某个规则,或者是某一些规则。

当然呢,注意看啊,它其实是一个接口,对吧?

那么我们要给它传进来的应该是它的一个具体的实现类。

具体的实现类。

那么具体呢,我们可以选中它,

然后呢,来看一下。

它的实现类。

实现类是不是有这么多?

在这儿呢,我们首先来看这个啊,叫做RulerNameEcosAgendaFilter。

比如说这个是什么意思呢?

这个Ecos,重点看这儿。

Ecos是不是就是相等啊?

就是指定名称啊,指定名称。

指定名称,就是我们要执行某一个,哪一个规则。

你把那个规则的Name给我传进来就可以了。

所以说呢,咱们这个Java代码改造起来呢,

其实还是非常简单的。

在这个方法里边,我们直接给它传一个什么呢?

New一个这个Filter对象。

对吧?

当然我们需要来导入一下,Import一下。

然后呢,把这个Name给它传进去。

哎,你看啊,它是不是要求我们传进来一个Name。

这个Name是什么Name呢?

就是规则的名称。

比如说啊,注意看啊,咱们现在呢,可以这样来验证一下。

就是什么呢?

我暂时先把这个去掉啊,Ctrl X,我先把它剪切掉。

然后呢,我们再来执行一下。

现在呢,因为我,

没有进行这个过滤,对吧?

规则的过滤。

所以说呢,只要匹配成功的规则呢,都会被执行到。

现在呢,你可以看到这三个规则是不是都执行了。

好,现在呢,我把它重新放到这儿来。

然后呢,把这个规则的名称啊,给它放到这儿。

好,规则的名称。

这是不是这个NotContent,这个规则。

好。

在这儿呢,我们最好还是来检查一下。

因为我们毕竟这个是控制台输出的,对吧?

它有可能并不是我们真正的那个规则的名称。

嗯,刚才我这个考的应该是NotContent,是不是应该是这个规则。

好。

所以,这儿指定的应该是规则的名称。

规则的名称。

那这样的话,我们再来执行一下这个单元测试。

大家来看一下。

稍等一下。

哎,你看,现在呢,是不是只有这一个规则触发了。

而我们刚才看到,是不是有三个规则触发。

哎,那么,为什么变成了一个呢?

就是因为我们现在是不是指定了是这个规则。

那这样的话,

即使其他,

它的规则能够匹配成功。

因为我们这儿是不是使用到了过滤器啊。

所以说,匹配成功的那些规则,

它也不会执行。

它只有可能会执行这个。

但是需要再来强调一下,

就是说这个规则一定会触发吗?

不一定啊。

你还是要看这个规则到底能不能匹配成功,对吧?

前提是它必须得匹配成功。

而且呢,我们在这儿又指定了它的名字。

这个规则是不是才会触发。

这个呢,我们用的这个过滤器叫做什么呢?

RulerNameEcosAddedFilter。

这个Ecos是不是就是等值的啊,等值的。

那比如说我现在呢,

我想执行某一些规则,

并不是所有的。

比如我们希望要执行的是什么呢?

是这个Ruler下滑线开始的这些规则。

但是咱们现在这几个规则其实都是这样命名的啊。

这个倒无所谓了。

就是什么呢?

我们刚才看到了,

这个接口,

它其实的它的实现类是不是很多呀?

我们可以大概,

来看一下,RulerNameEndsWithAgendaFilter。

其实从这个命名上,

大家应该也能看出来。

这个限制的是什么呢?

是不是必须是

以某某结尾,

对吧,以某个字符串结尾的

这样的规则。

然后呢,这个Ecos刚才我们演示了,对吧,等值的。

然后Matched呢,这个就类似于我们的这个

证则表达式的,对不对。

然后这个是一个序列化的。

然后这个呢,StartWith,

这个是

以某个字符串开始的。

对吧。

那么咱们可以来

试一下这个。

比如说我现在

把这个来改造一下。

我先把它贴这儿。

这句话呢,我们

可以暂时给它注释起来。

我希望把这个代码保留起来。

所以说我就

不在它这儿直接改了。

那么我们可以

给它注释起来,然后呢,把咱们这个规则的

把这个过滤器拿过来。

你看这个呢,是叫做

StartWith,就是以什么什么开始,对吧,以什么什么开始。

比如说

以这种

Ruler向滑线开始。

然后呢,咱们再来执行一下。

好,你看,这三个规则是不是又都触发了。

因为什么呢?因为这三个规则是不是

它都是以这个Ruler向滑线开始的。

那比如说我现在啊,

我给它改造一下。

刚才我们看啊,

都是谁触发的。

是这个NodeContent这个触发了,对吧。

然后呢,这个NodeMembersOf,

NodeMatches,

这三个触发的。

三个加这个Node的,对吧。

你比如说这个我加个A,

然后呢,

这个呢,

NodeMembers这个我加个B。

好,然后呢,

这个呢我就不改了。

可以吧。

咱们来看一下。

那么现在的话,我很明显,这两个规则,我刚才改的这两个规则,是不是已经不满足要求了。

然后呢,我们再来

执行。

你看,现在它是不是只有这一个规则触发了。

这就是我们提供的这种啊,

通过这种规则过滤器啊,这我还撤回来。

撤回来。

这就是我们提供的

这种规则过滤器

来执行什么呢?来执行指定的规则。

执行指定规则。

在这儿呢,我们可以来加一个注释。

使用我们这个框架,Dirose框架,提供的什么呢?提供的规则过滤器啊。

来执行什么?

指定规则。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程旨在演示如何在 Java 项目中使用 Drools 规则引擎进行规则匹配和执行。讲师通过 IntelliJ IDEA 开发环境，逐步展示了一个包含多个比较操作符（`matches`, `not matches`, `not contains`, `not memberOf`）的测试用例。核心内容包括：如何创建和配置 Drools 会话（`KieSession`），如何定义和插入事实对象（`ComparisonOperatorEntity`），以及如何通过 `fireAllRules()` 方法触发规则匹配。视频还深入讲解了 Drools 的 `AgendaFilter` 接口及其具体实现类（如 `RuleNameEqualsAgendaFilter`），用于控制规则的触发顺序和条件，从而实现更精细的规则控制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示项目结构和 `DroolsTest.java` 文件中的 `test20` 方法，该方法用于测试规则匹配。
*   **00:05 - 00:15**: 讲师在 `test20` 方法中创建 `KieServices` 和 `KieContainer`，并获取 `KieSession`。接着，创建一个 `ComparisonOperatorEntity` 实例，并设置其 `names` 属性为“李四”。
*   **00:15 - 00:25**: 讲师在代码中创建一个 `List<String>`，并添加了两个元素：“张三”和“李四”。随后，将该列表设置为事实对象的属性。
*   **00:25 - 00:35**: 讲师调用 `session.insert(fact)` 将事实对象插入会话，并调用 `session.fireAllRules()` 来激活并执行所有匹配的规则。
*   **00:35 - 00:45**: 展示了终端输出，显示了多个规则被触发，如 `rule_comparison_notcontains` 和 `rule_comparison_not_matches`。
*   **00:45 - 00:55**: 讲师切换到 `AgendaFilter.java` 文件，讲解 `AgendaFilter` 接口的作用，即用于过滤可能触发的规则。
*   **00:55 - 01:05**: 讲师在 `DroolsTest.java` 中修改代码，将 `fireAllRules()` 替换为 `fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"))`，以仅触发特定名称的规则。
*   **01:05 - 01:15**: 讲师展示了 `RuleNameEqualsAgendaFilter` 的实现类，并解释了其如何通过规则名称进行过滤。
*   **01:15 - 01:25**: 讲师切换到 `comparisonOperator.drl` 文件，展示了规则文件中的内容，包括 `matches`、`not matches`、`not contains` 和 `not memberOf` 等操作符的规则定义。
*   **01:25 - 01:35**: 讲师在 `DroolsTest.java` 中编写了 `test30` 方法，用于测试不同的规则匹配场景，并展示了如何通过 `AgendaFilter` 控制规则的执行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **获取 KieSession**:
        ```java
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();
        ```
    *   **创建和设置事实对象**:
        ```java
        ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
        fact.setNames("李四");
        List<String> list = new ArrayList<String>();
        list.add("张三");
        list.add("李四");
        fact.setList(list);
        session.insert(fact);
        ```
    *   **触发规则**:
        ```java
        session.fireAllRules();
        // 或者使用 AgendaFilter
        session.fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"));
        ```
    *   **Drools 规则文件 (`comparisonOperator.drl`) 内容**:
        ```drl
        rule "rule_comparison_matches"
            when
                ComparisonOperatorEntity(names matches "王.*")
            then
                System.out.println("规则：rule_comparison_matches触发了...");
            end

        rule "rule_comparison_not matches"
            when
                ComparisonOperatorEntity(names not matches "王.*")
            then
                System.out.println("规则：rule_comparison_not matches触发了...");
            end

        rule "rule_comparison_not contains"
            when
                ComparisonOperatorEntity(names not contains "王")
            then
                System.out.println("规则：rule_comparison_not contains触发了...");
            end

        rule "rule_comparison_not memberOf"
            when
                ComparisonOperatorEntity(names not memberOf list)
            then
                System.out.println("规则：rule_comparison_not memberOf触发了...");
            end
        ```

*   **关键接口定义**:
    *   `AgendaFilter` 接口定义：
        ```java
        public interface AgendaFilter {
            /**
             * Determine if a given match should be fired.
             * @param match The match that is requested to be fired
             * @return boolean value of "true" accepts the match for firing.
             */
            boolean accept(Match match);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：规则匹配与执行演示**
    *   **描述**: 讲师在 `test20` 方法中，通过创建一个包含“张三”和“李四”的列表，并将其设置为事实对象的属性，来测试规则。随后，调用 `session.fireAllRules()`，系统自动匹配并执行了多个规则，终端输出显示了规则触发的信息。
    *   **技术点**: 展示了 Drools 的自动规则匹配机制和规则执行流程。

*   **场景二：使用 AgendaFilter 控制规则触发**
    *   **描述**: 讲师修改了 `test20` 方法，将 `fireAllRules()` 替换为 `fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"))`。这使得只有名称为 `rule_comparison_notcontains` 的规则会被触发，从而实现了对规则执行的精确控制。
    *   **技术点**: 展示了 `AgendaFilter` 接口的使用，以及如何通过它来过滤和控制规则的触发。

*   **场景三：规则文件内容展示**
    *   **描述**: 讲师切换到 `comparisonOperator.drl` 文件，展示了定义了四个规则的规则文件。这些规则分别测试了 `matches`、`not matches`、`not contains` 和 `not memberOf` 四种比较操作符。
    *   **技术点**: 展示了 Drools 规则文件的语法和结构，以及如何在规则中使用比较操作符。

*   **场景四：规则执行结果分析**
    *   **描述**: 讲师在终端中查看了规则执行的结果，分析了不同规则触发的原因，并解释了规则匹配的逻辑。
    *   **技术点**: 展示了规则执行的输出结果，并分析了规则匹配的条件和逻辑。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
