# 24-规则引擎Drools-Drools基础语法（比较操作 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

我们继续来看我们这个比较操作符

刚才呢我们讲的是

member of以及not member of

再往下呢是我们这个match

match呢

它这个后边要跟的是一个证则表达式

证则表达式

继续回到咱们的规则文件

我们继续来编写

我就直接复制了

这边

然后呢在它的基础之上呢改造一下

我们这个呢

要测试的是这个

叫做match

这个比较操作符

然后呢把这个呢也改一下

叫做match

好匹配

然后在这个地方呢

我们就可以这么写了

比如说啊

我现在呢想匹配的是什么呢

这个names属性

就是这个

这种类型的这种属性

它必须怎么弄呢

match

必须匹配什么呢

后边注意

后边这个字符串啊

它对应的应该就是一个

正字

表达式啊

比如说呢

我在这儿啊来写一个什么呢

王

点

行

那是不是表示就是必须是姓王的

对吧

以王开始的

这样的名字

那么它才能够匹配到

才能匹配到

那么如果能够匹配到的话呢

我们在这个地方呢

可以来输出一下

好

那么

这就是这个match它的用法

后边呢主要就是写一个正则表达式

我们直接再来执行这个test2啊

大家可以看一下

我们现在来看一下

就我们当前设置的这个值

这个names是不是等于理4啊

理4的话

那很明显

它跟我们这个正则表达式

肯定是匹配不上的对吧

因为你这传进来的

是不是它动态一解析

是理4

然后呢跟这个正则表达式来匹配

那肯定是匹配不上

那么匹配不上的话呢

那很显然这个规则呢

它肯定也就

不会执行

你看

这还是原先的规则出发了

我们刚刚编写的这个规则呢

并没有出发

那么如果你想让它出发的话呢

你必须怎么做呢

把这个理4呢

给它改成王4

那么是以王开始的对不对

第一个字必须是王

然后呢

才能够匹配上

这个时候呢

我们再来执行一下

来看看啊

稍等一下

你看

现在呢

这个matchs

它是不是就已经出发了

当然了其他的这些啊

什么不包含的

不是这个成员的这些

是不是也都出发了

那么我们主要还是看最后一个输出

这样的话

它就会出发了

它就出这个出发了

然后还有一个叫做not matches

是不是就是不匹配啊

当然跟这个等于就是取反对吧

那么我们一块来复制一下

好这个呢

测试的是not matches

然后呢在这来写下not matches

但是现在呢

它因为能匹配到上面这个

所以下面这个肯定是匹配不到的

也就是说一个

当时这你得加一个not啊

这个加个not

这两个呢因为它俩是

等于是正好相反对不对

所以上面这个能成立

那下面这个肯定是成立不了的

再来验证一下

你看这个matchs这个是不是成立了

因为刚才我们已经测过了

那现在呢我把这个

王4呢重新改回李4

改回李4之后呢

那上面这个是不是就匹配不上了

而下面这个

因为它是not matches

是不是它就能够匹配上了

所以说它这些比较操作符啊

其实还是比较简单的

也比较直观

你看这个not matches

它是不是就已经这个匹配成功了

就是我们这条规则就已经匹配成功了

好这个呢是我们讲了一下

咱们这个matchs

这个比较操作符

以及not matches

比较操作符它的用法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一门关于 **Drools 规则引擎** 的技术课程，主要演示了如何在 Java 项目中使用 Drools 的 **比较操作符**（Comparison Operators）进行规则匹配。讲师通过 IntelliJ IDEA 开发环境，展示了如何编写和测试包含 `memberOf`、`not memberOf`、`matches` 和 `not matches` 等操作符的规则文件（`.drl`），并编写对应的 Java 测试代码（`DroolsTest.java`）来验证规则的执行。视频内容侧重于实践操作，通过修改测试数据和规则条件来观察规则引擎的匹配行为，旨在帮助学习者掌握 Drools 中这些核心比较操作符的用法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各帧对应的具体时间点，以下章节按画面内容和逻辑顺序排列：

*   **章节 1: 规则文件结构与比较操作符概览 (0:00 - 0:05)**
    *   展示了 `comparisonOperator.drl` 文件中的规则片段，包括 `memberOf` 和 `not memberOf` 操作符的语法结构。
    *   展示了 `matches` 和 `not matches` 操作符的语法结构。
    *   画面中显示了讲师正在讲解这些操作符的用法。

*   **章节 2: 编写测试用例 (0:05 - 0:15)**
    *   讲师在 `DroolsTest.java` 文件中编写了 `test20` 方法。
    *   该方法用于初始化 `KieServices`、`KieContainer` 和 `KieSession`。
    *   创建了一个 `ComparisonOperatorEntity` 实例 `fact`，并为其设置属性 `names` 和 `list`。
    *   调用 `session.insert(fact)` 将事实对象插入会话。
    *   调用 `session.fireAllRules()` 触发规则匹配。

*   **章节 3: 测试 `memberOf` 和 `not memberOf` (0:15 - 0:25)**
    *   讲师在 `comparisonOperator.drl` 文件中展示了 `memberOf` 和 `not memberOf` 规则。
    *   通过修改 `fact` 对象的 `list` 属性值，演示了规则的触发条件。
    *   画面中显示了 `System.out.println("规则: rule_comparison_memberOf触发了...");` 和 `System.out.println("规则: rule_comparison_not memberOf触发了...");` 语句。

*   **章节 4: 测试 `matches` 和 `not matches` (0:25 - 0:35)**
    *   讲师在 `comparisonOperator.drl` 文件中展示了 `matches` 和 `not matches` 规则。
    *   规则条件为 `names matches "王.*"`，用于匹配以“王”开头的字符串。
    *   讲师通过修改 `fact` 对象的 `names` 属性值（如设置为“王四”），来测试规则的触发情况。
    *   画面中显示了 `System.out.println("规则: rule_comparison_matches触发了...");` 和 `System.out.println("规则: rule_comparison_not matches触发了...");` 语句。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容 (来自 Typora 文档):**
    *   **章节标题:** `4.5.2 操作步骤`
    *   **第一步:** `创建实体类，用于测试比较操作符`
    *   **实体类代码:**
        ```java
        package com.ithema.drools.entity;
        import java.util.List;
        /**
         * 实体类
         * 用于测试比较操作符
         */
        public class ComparisonOperatorEntity {
            private String names;
            private List<String> list;
        }
        ```

*   **Drools 规则文件 (`.drl`) 代码:**
    *   **`memberOf` 操作符:**
        ```drl
        rule "rule_comparison_memberOf"
        when
            ComparisonOperatorEntity(names memberOf list)
        then
            System.out.println("规则: rule_comparison_memberOf触发了...");
        end
        ```
    *   **`not memberOf` 操作符:**
        ```drl
        rule "rule_comparison_not memberOf"
        when
            ComparisonOperatorEntity(names not memberOf list)
        then
            System.out.println("规则: rule_comparison_not memberOf触发了...");
        end
        ```
    *   **`matches` 操作符:**
        ```drl
        rule "rule_comparison_matches"
        when
            ComparisonOperatorEntity(names matches "王.*")
        then
            System.out.println("规则: rule_comparison_matches触发了...");
        end
        ```
    *   **`not matches` 操作符:**
        ```drl
        rule "rule_comparison_not matches"
        when
            ComparisonOperatorEntity(names not matches "王.*")
        then
            System.out.println("规则: rule_comparison_not matches触发了...");
        end
        ```

*   **Java 测试代码 (`DroolsTest.java`):**
    *   **核心方法 `test20`:**
        ```java
        @Test
        public void test20() {
            KieServices kieServices = KieServices.Factory.get();
            KieContainer kieContainer = kieServices.newKieClasspathContainer();
            KieSession session = kieContainer.newKieSession();

            // Fact对象，事实对象
            ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
            fact.setNames("李四");

            List<String> list = new ArrayList<String>();
            list.add("张三");
            list.add("李四");

            fact.setList(list);

            // 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
            session.fireAllRules();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景 1: 规则文件编辑与测试 (0:00 - 0:15)**
    *   讲师在 IntelliJ IDEA 中打开 `comparisonOperator.drl` 文件。
    *   通过高亮显示和滚动，展示了 `memberOf` 和 `not memberOf` 规则的代码。
    *   讲师在 `DroolsTest.java` 中编写了 `test20` 方法，用于创建事实对象并插入会话。
    *   通过修改 `fact` 对象的 `names` 属性值（如从“李四”改为“王四”），演示了规则的触发条件。

*   **场景 2: `matches` 与 `not matches` 规则测试 (0:15 - 0:35)**
    *   讲师在 `comparisonOperator.drl` 文件中编写了 `matches` 和 `not matches` 规则。
    *   规则条件为 `names matches "王.*"`，用于匹配以“王”开头的字符串。
    *   讲师在 `DroolsTest.java` 中修改了 `fact` 对象的 `names` 属性值，使其匹配规则条件。
    *   通过运行测试，演示了 `matches` 规则的触发，以及 `not matches` 规则在条件不匹配时的不触发情况。
    *   画面中显示了 `System.out.println("规则: rule_comparison_matches触发了...");` 语句的执行结果。

*   **场景 3: 规则条件修改与结果观察 (0:35 - 0:45)**
    *   讲师在 `comparisonOperator.drl` 文件中修改了 `not matches` 规则的条件。
    *   通过修改 `fact` 对象的 `names` 属性值，观察规则的触发情况。
    *   画面中显示了 `System.out.println("规则: rule_comparison_not matches触发了...");` 语句的执行结果。

---

以上是根据视频画面内容进行的结构化技术分析。
