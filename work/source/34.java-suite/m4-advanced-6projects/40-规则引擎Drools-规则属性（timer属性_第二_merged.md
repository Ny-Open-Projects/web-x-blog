# 40-规则引擎Drools-规则属性（timer属性_第二 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们的规则属性

刚才我们是讲到了timer属性

第一种使用方式我们刚才已经讲完了

接下来咱们来看第二种使用方式

第二种使用方式是使用这种call-on表达式

来定义我们规则出发的时间

而这个call-on表达式是基于我们标准的

这种unicode call-on表达式

它的语法来定义这个规则

当然关于这个call-on表达式

我们本课程就不再展开去讲解了

大家如果说对call-on表达式不了解的

可以自行去参考一下

而且我们其实在学习Java语言的时候

有一个框架

学习Java的大家应该大部分人都了解

有一个叫做call的框架

包括还有一个叫做sprint task

这些框架它其实都属于一个任务调度

其实说白了就是我们的定时任务

这样的框架

在定时任务上

使用这些框架的时候

我们就会编写很多定时任务

并且通过call-on表达式

来指定任务出发的时间

所以这都属于类似的这些表达式

只不过我们这个地方使用到的表达式

是用于我们timer属性这个位置

这是咱们D-Rose里边

也会使用到类似的这些call-on表达式

那么通过它也可以来定义

咱们规则出发的时间

那么现在我们就在

这个

咱们的框架里边

咱们刚才编写的规则文件里面

来编写我们第二种

再来编写第二个规则

这个应该是第二种

下面这应该是第一种

把这个稍微改造一下

把这改成个2

然后这块我们就需要来改造一下了

第二种使用方式是怎么用呢

来看一下我们的语法

是这样的

首先有一个call

然后跟上一个冒号

后边就是给我们的语法

跟我们标准的这种call-on表达式

这个表达式咱们可以写一个简单的

因为这块我们重点还是讲的是这块

并不会重点去讲call-on语法

所以说我们在这儿可以编写一个简单一点的

比如说我在这儿来个0-1

这个斜线其实表示的是递增

对吧

就是每隔多长时间

然后后边我们是不是可以跟上几个星

这个它其实一共是有七位

如果写全了

它应该是有七位

注意刚才我写的是个中文的符号

好

第一位它其实代表的是秒

然后后边是不是代表的是分钟

然后是不是代表的是小时

然后是日月周

然后最后一个是年

大概是这么七位

但是最后这个年我们可以不写

然后我们可以看到

这星的话是不是匹配所有

就是相当于每小时每分钟

对吧

然后从第0秒开始

然后每隔多长时间触发一次

比如说我这儿写个1

那就是每隔1秒

这儿写2的话

那就是每隔2秒

是这么一个效果

后边这个问号表示放弃

对吧

就是这一位我不再进行控制

所以用的是一个问号

你看跟咱们写法是类似的

这样的

好

那么为了能看到它触发的时间

到底是不是隔了2秒触发

咱们可以在它规则执行的时候

我们也可以

把触发的时间给它来输出一下

就是触发的时间为

好

这个时间我们是不是可以来new一个data

然后通过我们simple data format来格式化一下

所以说咱们在这儿需要使用到一个data

import java.util.data

然后还需要使用到一个什么

simple data format

这个是在哪个包下面

是在这个java.test的下边

我直接拿过来

好

把它也导入一下simple data format

然后我们在这儿就可以直接来new一个什么

simple data format

对吧

然后在这里边来指定我们这个格式

一会儿我们再来指定格式

先调用它的format的方法

对吧

把咱们这个当前时间new一个data

放进去

这个时间我们来输出一下年月

年月

年月

年月

年月

日

然后十分秒

好

然后new一个data放进去就可以了

这样方便我们来观察它这个规则触发的时间

到底是不是每隔两秒触发的

好

接下来咱们继续来执行这个单元测试

还是使用刚才我们编写的这个单元测试就可以

同样的它还是持续十秒钟的时间

这样的话它就可以输出几次了

大家来看

控制台输出

哎

这次呢

是不是触发了触发的时间

你看06

08

然后呢

10

然后12

14

ok

正好是五次对不对

十秒钟正好能触发五次

然后呢

这个规则

因为我们这个地方是不是持续十秒钟之后呢

调用了这个help的方法

所以整个程序呢

其实就结束了

所以我们通过控制台呢

也能够看到啊

咱们在这呢

是通过编写的我们这种call表达式来指定啊

这个是这个执行的方法啊

这个是基于我们这个call表达式来指定我们规则触发的时间

好

这是关于我们这个timer属性啊

它的第二种用法

好

这就是call表达式这种用法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 中 **`timer` 属性** 的教学内容。讲师通过演示如何在规则文件（`.drl`）中使用两种不同的定时器语法来控制规则的触发时机：第一种是基于 `java.util.Timer` 的 `timer(int: initialDelay, <repeatInterval>)` 语法，第二种是基于标准 Unix `cron` 表达式的 `timer(cron: <cron expression>)` 语法。视频通过在 IntelliJ IDEA 中编写和测试规则文件，并配合单元测试代码，直观地展示了这两种定时器的配置和执行效果。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序进行的划分：

*   **章节 1: 介绍 `timer` 属性的两种用法 (0:00 - 0:30)**
    *   画面显示 PPT 内容，明确指出 `timer` 属性有两种使用方式：`timer(int: initialDelay <repeatInterval>?)` 和 `timer(cron: <cron expression>)`。
    *   讲师解释了第一种方式遵循 `java.util.Timer` 的用法，第一个参数是初始延迟，第二个参数是重复间隔（可选）。
    *   讲师解释了第二种方式使用标准的 Unix `cron` 表达式。

*   **章节 2: 第一步 - 创建规则文件 (0:30 - 1:00)**
    *   讲师在 PPT 中指出需要创建规则文件 `/resources/rules/timer.drl`。
    *   画面切换到 IntelliJ IDEA，显示了 `timer.drl` 文件的内容，其中包含了用于测试 `timer` 属性的两个规则：`rule_timer_1` 和 `rule_timer_2`。

*   **章节 3: 编写单元测试代码 (1:00 - 2:00)**
    *   讲师在 PPT 中提示“第二步：编写单元测试”。
    *   画面切换到 `DroolsTest.java` 文件，展示了如何使用 `KieServices` 和 `KieSession` 来加载规则并启动引擎。
    *   讲师演示了如何使用 `new Thread(...).start()` 启动规则引擎，并使用 `session.fireUntilHalt()` 让引擎持续运行，直到调用 `session.halt()` 方法。

*   **章节 4: 运行测试并观察结果 (2:00 - 3:00)**
    *   讲师运行单元测试。
    *   画面切换到测试运行结果窗口，显示了规则 `rule_timer_1` 和 `rule_timer_2` 按照设定的时间间隔被触发，并打印了精确到秒的时间戳。
    *   讲师通过观察控制台输出，验证了两种定时器语法的正确性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容:**
    *   **`timer` 属性的两种用法:**
        *   **方式一:** `timer(int: initialDelay <repeatInterval>?)`
        *   **方式二:** `timer(cron: <cron expression>)`
    *   **第一步:** 创建规则文件 `/resources/rules/timer.drl`
    *   **第二步:** 编写单元测试

*   **代码关键内容:**

    **规则文件 `timer.drl`:**
    ```drl
    package testtimer
    import java.text.SimpleDateFormat
    import java.util.Date

    /*
     * 此规则文件用于测试timer属性
     */

    rule "rule_timer_1"
    timer (5s 2s) // 含义：5秒后触发，然后每隔2秒触发一次
    when
    then
        System.out.println("规则: rule_timer_1触发了...");
    end

    rule "rule_timer_2"
    timer (cron:0/1 * * * * ?) // 含义：每隔1秒触发一次
    when
    then
        System.out.println("规则: rule_timer_2触发了...触发的时间为：" + 
            new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()));
    end
    ```

    **单元测试文件 `DroolsTest.java`:**
    ```java
    public class DroolsTest {
        @Test
        public void test7() throws Exception {
            KieServices kieServices = KieServices.Factory.get();
            KieContainer kieContainer = kieServices.newKieClasspathContainer();
            final KieSession session = kieContainer.newKieSession();

            new Thread(new Runnable() {
                public void run() {
                    // 启动规则引擎进行规则匹配，直到调用halt方法才结束规则引擎
                    session.fireUntilHalt();
                }
            }).start();

            Thread.sleep(10000); // 等待一段时间让规则触发

            // 结束规则引擎
            session.halt();

            // 关闭会话
            session.dispose();
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 展示两种定时器语法 (0:30)**
    *   讲师在 PPT 上高亮显示了 `timer` 属性的两种语法。
    *   他解释了第一种语法 `timer(int: initialDelay <repeatInterval>?)` 与 `java.util.Timer` 的对应关系，并说明了参数含义。
    *   他解释了第二种语法 `timer(cron: <cron expression>)` 使用标准的 Unix `cron` 表达式。

*   **场景 2: 创建并编辑规则文件 (1:00)**
    *   讲师在 IntelliJ IDEA 中打开并编辑 `timer.drl` 文件。
    *   他首先编写了 `rule_timer_1`，使用 `timer (5s 2s)` 语法，表示5秒后触发，然后每2秒触发一次。
    *   他接着编写了 `rule_timer_2`，使用 `timer (cron:0/1 * * * * ?)` 语法，表示每隔1秒触发一次。
    *   两个规则的 `then` 子句都包含了打印触发信息的代码，其中 `rule_timer_2` 的代码还包含了格式化当前日期时间的 `SimpleDateFormat`。

*   **场景 3: 编写并运行单元测试 (2:00)**
    *   讲师在 `DroolsTest.java` 中编写了测试方法 `test7()`。
    *   他使用 `KieServices` 和 `KieContainer` 加载规则文件。
    *   他创建了一个 `KieSession`，并使用 `new Thread(...).start()` 启动规则引擎。
    *   他调用 `session.fireUntilHalt()` 让引擎持续运行。
    *   他使用 `Thread.sleep(10000)` 等待一段时间，让规则有足够的时间触发。
    *   他调用 `session.halt()` 结束引擎，`session.dispose()` 关闭会话。

*   **场景 4: 观察测试结果 (2:30)**
    *   讲师运行测试。
    *   画面切换到测试运行结果窗口。
    *   控制台输出显示了规则 `rule_timer_1` 和 `rule_timer_2` 按照设定的时间间隔被触发。
    *   `rule_timer_1` 的输出是简单的“规则: rule_timer_1触发了...”。
    *   `rule_timer_2` 的输出包含了精确到秒的时间戳，例如：“规则: rule_timer_2触发了...触发的时间为：2020-02-10 16:40:06”。
    *   讲师通过观察输出，验证了两种定时器语法的正确性。
