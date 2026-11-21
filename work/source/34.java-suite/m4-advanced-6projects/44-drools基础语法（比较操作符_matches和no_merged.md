# 44-drools基础语法（比较操作符_matches和no — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

我们继续来看我们这个比较操作符

刚才呢我们讲的是member of

以及not member of

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

比如说我现在呢想匹配的是什么呢

这个names属性

就是这个这种类型的

这种属性它必须

怎么弄呢match

必须匹配什么呢后边注意

后边这个字符串

它对应的应该就是一个

证则表达式啊

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

那么这就是这个match

它的用法

后边呢主要就是写一个证则表达式

我们直接再来执行这个

test2

大家来看一下

就我们当前设置的这个值

这个names是不是等于理四啊

理四的话

那很明显

它跟我们这个证则表达式

肯定是匹配不上的对吧

因为你这传进来的

是不是它动态一解析是理四

然后呢跟这个证则表达式来匹配

那肯定是匹配不上

那么匹配不上的话呢

那很显然这个规则呢

它肯定也就不会执行

你看

这还是原先的规则出发了

我们刚刚编写的这个规则呢

并没有出发

那么如果

你想让它触发的话呢

你必须怎么做呢

把这个理四呢

给它改成王四

那么是以王开始的对不对

第一个字必须是王

然后呢才能够匹配上

这个时候呢

我们再来执行一下

来看看啊

稍等一下

你看现在呢

这个matchs

它是不是就已经触发了

当然了

其他的这些啊

什么不包含的

不是这个成员的

这些是不是也都触发了

那么我们主要还是看最后一个输出

这样的话

它就出这个触发了

然后还有一个叫做not matchs

是不是就是不匹配啊

当然跟这个等于就是取反

对吧

那么我们一块来复制一下

好

这个呢

测试的是not matchs

好

然后呢

在这来写下not matchs

但是现在呢

它因为能匹配到上面这个

所以下面这个肯定是匹配不到的

也就是说一个

当然这你得加一个not

这个加个not

这两个呢

因为它俩等于等于是正好相反

对不对

所以上面这个能成立

那下边这个肯定是成立不了的

好

再来验证一下

你看这个matchs这个是不是成立了

因为刚才我们已经测过了

那现在呢

我把这个王四呢

重新改回李四

改回李四之后呢

那下面这个是不是就匹配不上了

而下边这个因为它是not matchs

是不是它就能够匹配上了

所以说它这些比较操作符啊

其实还是比较简单的

也比较直观

你看这个not matchs

你看这个not matchs

你看这个not matchs

你看这个not matchs

它是不是就已经这个匹配成功了

就是我们这条规则就已经匹配成功了

好

这个呢是我们讲了一下咱们这个matchs

这个比较操作符

以及not matchs比较操作符

它的用法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的技术教学内容，主要演示如何在 Java 项目中使用 **`matches`** 和 **`not matches`** 这两种比较操作符来编写规则。讲师通过 IntelliJ IDEA 开发环境，展示了如何创建测试类、定义事实对象、编写规则文件（`.drl`），并最终通过 `KieSession.fireAllRules()` 方法触发规则执行。视频内容聚焦于规则的条件匹配逻辑，特别是正则表达式匹配的用法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 开场，展示项目结构和 `DroolsTest.java` 测试类的代码，准备进行规则测试。
*   **00:05 - 00:15**: 讲解并演示 `memberOf` 和 `not memberOf` 操作符的规则（画面中显示了相关代码，但未执行）。
*   **00:15 - 00:30**: 转向 `matches` 和 `not matches` 操作符。讲师在 `DroolsTest.java` 中设置事实对象 `fact` 的 `names` 字段为 `"王四"`，并创建一个包含 `"张三"` 的 `list`。
*   **00:30 - 00:45**: 在 `comparisonOperator.drl` 文件中，编写并演示 `matches` 规则。规则条件为 `names matches "王.*"`，当事实对象的 `names` 为 `"王四"` 时，该规则会匹配成功并打印日志。
*   **00:45 - 01:00**: 在 `comparisonOperator.drl` 文件中，编写并演示 `not matches` 规则。规则条件为 `names not matches "王.*"`，当事实对象的 `names` 为 `"王四"` 时，该规则不会匹配成功，因此不会打印日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   展示了 DRL 规则文件中 `matches` 和 `not matches` 语法结构的说明。
    *   语法结构为：`Object(field matches "正则表达式")` 和 `Object(field not matches "正则表达式")`。

*   **关键代码**:
    *   **测试类 `DroolsTest.java`**:
        ```java
        public class DroolsTest {
            @Test
            public void test20() {
                KieServices kieServices = KieServices.Factory.get();
                KieContainer kieContainer = kieServices.newKieClasspathContainer();
                KieSession session = kieContainer.newKieSession();

                // Fact对象，事实对象
                ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
                fact.setNames("王四");

                List<String> list = new ArrayList<String>();
                list.add("张三");

                fact.setList(list);

                session.insert(fact);
                session.fireAllRules(); // 激活规则
            }
        }
        ```
    *   **规则文件 `comparisonOperator.drl`**:
        ```drl
        // 测试比较操作符 matches
        rule "rule_comparison_matches"
            when
                ComparisonOperatorEntity(names matches "王.*")
            then
                System.out.println("规则: rule_comparison_matches触发了...");
        end

        // 测试比较操作符 not matches
        rule "rule_comparison_not_matches"
            when
                ComparisonOperatorEntity(names not matches "王.*")
            then
                System.out.println("规则: rule_comparison_not_matches触发了...");
        end
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建和配置测试环境**
    *   讲师在 IntelliJ IDEA 中打开了 `DroolsTest.java` 文件。
    *   代码中通过 `KieServices.Factory.get()` 获取 `KieServices` 实例，然后创建 `KieContainer` 和 `KieSession`。
    *   创建了一个 `ComparisonOperatorEntity` 类型的 `fact` 对象，并为其 `names` 字段赋值为 `"王四"`。
    *   创建了一个 `ArrayList`，并添加了 `"张三"` 作为元素，然后将该列表设置到 `fact` 对象的 `list` 字段中。
    *   调用 `session.insert(fact)` 将事实对象插入到规则引擎中。
    *   最后调用 `session.fireAllRules()` 来触发所有规则的匹配和执行。

*   **场景二：演示 `matches` 规则**
    *   讲师在 `comparisonOperator.drl` 文件中编写了 `rule_comparison_matches` 规则。
    *   规则条件是 `names matches "王.*"`，表示匹配以“王”开头的任意字符串。
    *   由于事实对象的 `names` 是 `"王四"`，该规则匹配成功。
    *   视频中显示了控制台输出日志：`规则: rule_comparison_matches触发了...`。

*   **场景三：演示 `not matches` 规则**
    *   讲师在 `comparisonOperator.drl` 文件中编写了 `rule_comparison_not_matches` 规则。
    *   规则条件是 `names not matches "王.*"`，表示不匹配以“王”开头的任意字符串。
    *   由于事实对象的 `names` 是 `"王四"`，该规则不匹配。
    *   视频中显示了控制台没有输出该规则的触发日志，证明规则未被触发。
