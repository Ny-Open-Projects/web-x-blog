# 29-规则引擎Drools-Drools基础语法（内置方法_i — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来我们继续来看咱们D-Rose内置方法

刚才呢我们讲的是update的方法

接下来我们要讲的是insert的方法

insert的方法呢

它的作用是向工作内存中来插入数据

刚才update是不是更新那个fact的数据啊

而我们那个是插入数据

那么并且让相关的规则呢重新匹配

好,咱们呢还是回到我们的规则文件

这是刚才我们在测试这个update的内置方法的时候

咱们是不是写了这么三个规则,对吧

现在呢我来再写一个规则

我在最上面这儿来写

这个呢是当前我们这个规则呢用于测试什么呢

我们这个insert内置方法

好,我们来定义一下

Ruler,这个名字呢一会儿再指定,对吧

然后呢, when, then, and

好,先把主体这个结构把它写好

然后规则的名称呢

咱们从这儿呢来改造一下

好

比方说这个age是,我来个等于吧

等于10岁

那么如果是等于10岁的话

咱们把这句拿过来

是不是把这改成等号就可以了

需要注意啊,应该是两个等号,对吧

好,这是等于

如果是等于10岁的话呢

那么当前这个规则是不是就匹配到了

匹配到之后呢

我们同样先来一个输出语句啊

规则,哪个规则呢

来,从这儿来指定一下

然后呢,触发了

好

并且呢,我们回过头来

来修改一下这个规则文件啊

这个内置方法呢

我们刚才写的是update,对吧

update方法

咱们来复制一份啊

尽量呢,我们就不改造代码

而是复制新的代码

把我们原先这些呢

都给保留下来

然后这个呢,我们测试的是insert方法

insert方法呢

现在我如果希望

我如果希望当前这个规则能触发

那这个age是不是

就得设置成10啊

把这个age设置成10岁

好

如果是10岁的话呢

这样的话我们一匹配

第一个规则是不是就触发了

然后我们来看

后边这些规则会触发吗

应该不会触发吧

这个是小于10岁

这个也就是他们是不是都没有等于10岁的这种情况

所以说后边这三个规则应该都不会触发

只有第一个规则会触发

咱们来执行一下

好

你看,是不是等于10岁的这个

这个规则触发了

好

触发了

那现在呢

我想达到一个什么样的效果呢

就是啊

我希望当我这个规则触发的时候呢

后边这些规则也跟着能触发

那这个如何来实现呢

你看因为他这个要求的这个student

他的age是不是应该是小于10岁啊

是小于10岁

他匹配不上啊

那么这个时候呢

我们就可以啊

在咱们这个规则里边来干什么呢

创建一个新的student的对象

并且呢

把这个student对象呢

通过insert的方法

把它插入到内存里面去

就是我们工作内存里面去

那么一插入的话呢

是不是其他的规则呢

又会重新匹配了

对不对

一匹配的话呢

他是不是就有可能会匹配成功

所以说呢

我们在这儿呢

创建一个新的

注意创建一个新的student对象

student等于new一个student

并且呢

我们在这个student这儿呢

给他设置这个age

age等于多少呢

这个地方来看

他是小于10岁对吧

所以随便给他一个

比如5岁

然后呢

别忘了执行一个insert的方法

你看

然后把这个s是不是传进去

好

这个呢

我们是调用的这个insert的方法

insert的方法

它的作用是什么呢

是

像我们的这个工作内存中

是不是插入我们的fag的对象

对吧

哎

对吧

会导致什么呢

会导致我们的相关规则

是不是重新来匹配

重新匹配

那么它一匹配的话

是不是这个规则就能匹配成功

而且呢

我们再来分析一下

这个规则匹配成功之后啊

它是不是把这个age又改成了15

一直行更新

又会导致重新匹配

所以这个是不是又有匹配成功了

这是我们刚才在进行update方法的时候

都已经说过了

对吧

所以说呢

我在这儿呢

加了一个insert语句之后

就会导致啊

一个连锁反应

最终这四个规则都会执行到

咱们来看一下

哎

你看这四个规则是不是都触发了

那么我们这儿呢

重点看的其实是这个insert方法

insert方法

它的作用呢

再来强调一遍

就是向工作内存里面插入fag的对象

对吧

然后呢

它会导致我们规则重新匹配

重新一匹配呢

下面这些是不是也就匹配成功了

好

这个呢

这是关于咱们这个insert方法

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于 **Drools 规则引擎** 的技术教学演示。演示者通过 IntelliJ IDEA 开发环境，展示如何在 Java 项目中编写、测试和使用 Drools 的内置方法（如 `update` 和 `insert`）。核心内容包括：
*   **规则文件 (`student.drl`)**：定义了多个基于学生年龄的业务规则。
*   **测试类 (`DroolsTest.java`)**：编写单元测试来验证规则的触发条件和内置方法的行为。
*   **内置方法演示**：
    *   `update()`：用于修改已存在的 Fact 对象，触发规则重新匹配。
    *   `insert()`：用于向工作内存中添加新的 Fact 对象，触发规则重新匹配。
*   **演示重点**：通过修改学生年龄属性并调用 `update()`，或创建新学生对象并调用 `insert()`，来观察不同规则的触发情况，并在控制台输出结果。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节是根据画面内容和逻辑顺序划分的：

*   **章节 1: 项目结构与规则文件概览 (00:00 - 00:05)**
    *   展示项目结构，包括 `java` 和 `resources` 目录。
    *   重点介绍 `resources/rules/student.drl` 文件，这是规则的定义文件。

*   **章节 2: `update` 方法演示 (00:05 - 00:15)**
    *   代码聚焦于 `student.drl` 中的规则。
    *   展示了两个规则：一个用于 `age < 10`，另一个用于 `10 < age < 20`。
    *   通过 `update($student)` 方法修改学生年龄，演示规则如何被重新触发。

*   **章节 3: `insert` 方法演示 (00:15 - 00:25)**
    *   代码聚焦于 `student.drl` 中的规则。
    *   展示了用于 `age == 10` 的规则。
    *   通过 `insert(s)` 方法向工作内存中插入一个新学生对象，演示规则如何被触发。

*   **章节 4: 测试类代码与结果 (00:25 - 00:35)**
    *   展示了 `DroolsTest.java` 中的测试方法 `test4()` 和 `test5()`。
    *   `test4()` 用于测试 `update` 方法。
    *   `test5()` 用于测试 `insert` 方法。
    *   运行测试后，控制台输出了规则触发的相应信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码文件：`student.drl` (规则文件)**
    *   **规则 1 (用于测试 `update`):**
        ```drl
        rule "要求Student的age小于10岁"
        when
            $student:Student(age < 10)
        then
            $student.setAge(15);
            update($student); // update方法用于更新Fact对象，会导致相关规则重新匹配
            System.out.println("规则：要求Student的age小于10岁触发了...");
        end
        ```
    *   **规则 2 (用于测试 `update`):**
        ```drl
        rule "要求Student的age大于10岁并且小于20岁"
        when
            $student:Student(age < 20 && age > 10)
        then
            $student.setAge(25);
        end
        ```
    *   **规则 3 (用于测试 `insert`):**
        ```drl
        rule "要求Student的age等于10岁"
        when
            $student:Student(age == 10)
        then
            Student s = new Student();
            s.setAge(5);
            insert(s); // insert方法用于向工作内存中插入Fact对象，会导致相关规则重新匹配
            System.out.println("规则：要求Student的age等于10岁触发了...");
        end
        ```

*   **代码文件：`DroolsTest.java` (测试类)**
    *   **测试方法 `test4()` (测试 `update`):**
        ```java
        @Test
        public void test4() {
            KieServices kieServices = KieServices.Factory.get();
            KieContainer kieContainer = kieServices.newKieClasspathContainer();
            KieSession session = kieContainer.newKieSession();

            Student student = new Student();
            student.setAge(4);

            // 激活规则，fireAllRules();
            // 关闭会话
            session.dispose();
        }
        ```
    *   **测试方法 `test5()` (测试 `insert`):**
        ```java
        @Test
        public void test5() {
            KieServices kieServices = KieServices.Factory.get();
            KieContainer kieContainer = kieServices.newKieClasspathContainer();
            KieSession session = kieContainer.newKieSession();

            Student student = new Student();
            student.setAge(4);

            // 激活规则，fireAllRules();
            // 关闭会话
            session.dispose();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景 1: `update` 方法触发规则 (00:05 - 00:15)**
    *   **演示过程**：演示者在 `student.drl` 文件中，将学生年龄设置为 4，然后调用 `update($student)` 方法将年龄修改为 15。
    *   **结果**：控制台输出“规则：要求Student的age小于10岁触发了...”，表明规则成功匹配并执行。

*   **场景 2: `insert` 方法触发规则 (00:15 - 00:25)**
    *   **演示过程**：演示者在 `student.drl` 文件中，定义了一个 `age == 10` 的规则。然后在测试代码中，创建一个新学生对象并调用 `insert(s)` 方法将其插入工作内存。
    *   **结果**：控制台输出“规则：要求Student的age等于10岁触发了...”，表明新插入的 Fact 触发了规则。

*   **场景 3: 多规则同时触发 (00:25 - 00:35)**
    *   **演示过程**：演示者运行了 `test5()` 方法，该方法会创建一个学生对象并插入工作内存。
    *   **结果**：控制台输出了三条信息：
        1.  “规则：要求Student的age等于10岁触发了...” (来自 `insert` 触发的规则)
        2.  “规则：要求Student的age小于10岁触发了...” (来自 `update` 触发的规则)
        3.  “规则：要求Student的age大于10岁并且小于20岁触发了...” (来自 `update` 触发的规则)
    *   **说明**：这表明 Drools 的规则引擎可以同时处理多个规则，并根据 Fact 的状态变化触发多个规则。
