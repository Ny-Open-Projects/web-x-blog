# 49-drools基础语法（内置方法_insert方法） — 课程文稿（声音线+画面线 合并稿）

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

好,我们来定义一下Rule

这个名字呢一会儿再指定,对吧

然后呢win, then, end

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

然后呢触发了

好

并且呢我们回过头来

来修改一下这个规则文件啊

这个内置方法呢

我们刚才写的是update对吧

update方法

咱们来复制一份啊

尽量呢我们就不改造代码

而是复制新的代码

把我们原先这些呢都给保留下来

然后这个呢我们测试的是insert方法

insert方法呢

现在我如果希望啊

我如果希望当前这个规则能触发

那这个age是不是必须要复制呢

必须得设置成10啊

把这个age设置成10岁

好

如果是10岁的话呢

这样的话我们一匹配

第一个规则是不是就触发了

然后我们来看后边这些规则会触发吗

应该不会触发吧

这个是小于10岁

这个也就是他们是不是都没有等于10岁的这种情况

所以说后边这三个规则应该都不会触发

只有第一个规则会触发

咱们来执行一下

好

你看是不是等于10岁的这个

这个规则触发了

那现在呢

我想得达到一个什么样的效果呢

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

那么我们就来看这个规则里边

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

我们在这个student的这儿呢

给他设置这个age

age等于多少呢

这个地方来看

他是小于10岁对吧

所以随便给他一个

比如说5岁

然后呢

别忘了执行一个insert的方法

你看

然后把这个s是不是传进去

好

这个呢

我们是调用的这个insert的方法

insert的方法

它的作用是什么呢

是像我们的这个工作内存中

是不是插入我们的fact的对象

对吧

哎

会导致我们的这个工作内存中

是什么呢

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

就会导致一个连锁反应

最终这四个规则都会执行到

咱们来看一下

哎

你看这四个规则是不是都触发了

那么我们这儿呢

重点看的其实是这个insert方法

insert方法

它的作用呢

再来强调一遍

就是向工作内存里面插入fact的对象

对吧

然后呢

它会导致我们规则重新匹配

重新一匹配呢

下面这些是不是也就匹配成功了

好

这个呢

这是关于咱们这个insert方法

我们就先说到这儿

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于 **Drools 规则引擎** 的技术教学演示。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Java 项目中编写、测试和使用 Drools 的内置方法，特别是 `insert` 和 `update` 方法。演示的核心是通过修改 `student.drl` 规则文件中的条件，来观察不同规则触发时的控制台输出，从而理解 Drools 如何处理事实（Fact）的插入和更新，并触发相应的规则。视频主要围绕 `DroolsTest.java` 测试类中的 `test4` 和 `test5` 方法展开，通过在规则文件中添加或修改规则条件，来验证规则引擎的行为。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **环境与项目概览**。展示 IntelliJ IDEA 中的项目结构，包括 `src/main/java` 和 `src/main/resources/rules` 目录，以及 `student.drl` 规则文件。
*   **00:05 - 00:15**: **演示 `update` 方法**。讲师在 `student.drl` 文件中展示了一个规则，该规则的条件是 `age < 10`，并在 `then` 块中调用 `update($student)` 方法。讲师解释了 `update` 方法的作用是更新事实对象，从而触发规则重新匹配。
*   **00:15 - 00:25**: **演示 `insert` 方法**。讲师在 `student.drl` 文件中添加了一个新的规则，条件是 `age == 10`，并在 `then` 块中使用 `insert(s)` 方法插入一个新事实。讲师解释了 `insert` 方法的作用是向工作内存中添加一个新事实，从而触发规则重新匹配。
*   **00:25 - 00:35**: **测试方法 `test4`**。讲师在 `DroolsTest.java` 文件中展示了 `test4` 方法，该方法通过 `KieServices` 获取 `KieContainer`，然后创建一个 `Student` 对象并设置其年龄为 4。讲师解释了 `test4` 方法的作用是测试 `update` 方法。
*   **00:35 - 00:45**: **测试方法 `test5`**。讲师在 `DroolsTest.java` 文件中展示了 `test5` 方法，该方法通过 `KieServices` 获取 `KieContainer`，然后创建一个 `Student` 对象并设置其年龄为 5。讲师解释了 `test5` 方法的作用是测试 `insert` 方法。
*   **00:45 - 00:55**: **运行测试并观察结果**。讲师运行 `test5` 方法，终端输出显示了三个规则被触发，分别对应 `age == 10`、`age < 10` 和 `age > 10 && age < 20` 的条件。讲师解释了为什么这三个规则都被触发了。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (student.drl - update 方法)**：
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

*   **代码片段 2 (student.drl - insert 方法)**：
    ```drl
    rule "要求Student的age等于10岁"
    when
        $student:Student(age == 10)
    then
        Student s = new Student();
        s.setAge(5);
        insert(s); // insert方法作用是向工作内存中插入Fact对象，会导致相关规则重新匹配
        System.out.println("规则：要求Student的age等于10岁触发了...");
    end
    ```

*   **代码片段 3 (DroolsTest.java - test4 方法)**：
    ```java
    @Test
    public void test4() {
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();

        Student student = new Student();
        student.setAge(4);
    }
    ```

*   **代码片段 4 (DroolsTest.java - test5 方法)**：
    ```java
    @Test
    public void test5() {
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();

        Student student = new Student();
        student.setAge(5);
    }
    ```

*   **终端输出 (test5 方法运行结果)**：
    ```
    规则：要求Student的age等于10岁触发了...
    规则：要求Student的age小于10岁触发了...
    规则：要求Student的age大于10岁并且小于20岁触发了...
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: `update` 方法演示**。讲师在 `student.drl` 文件中展示了一个规则，该规则的条件是 `age < 10`。在 `then` 块中，讲师调用 `update($student)` 方法。讲师解释了 `update` 方法的作用是更新事实对象，从而触发规则重新匹配。
*   **场景 2: `insert` 方法演示**。讲师在 `student.drl` 文件中添加了一个新的规则，条件是 `age == 10`。在 `then` 块中，讲师使用 `insert(s)` 方法插入一个新事实。讲师解释了 `insert` 方法的作用是向工作内存中添加一个新事实，从而触发规则重新匹配。
*   **场景 3: `test4` 方法演示**。讲师在 `DroolsTest.java` 文件中展示了 `test4` 方法，该方法通过 `KieServices` 获取 `KieContainer`，然后创建一个 `Student` 对象并设置其年龄为 4。讲师解释了 `test4` 方法的作用是测试 `update` 方法。
*   **场景 4: `test5` 方法演示**。讲师在 `DroolsTest.java` 文件中展示了 `test5` 方法，该方法通过 `KieServices` 获取 `KieContainer`，然后创建一个 `Student` 对象并设置其年龄为 5。讲师解释了 `test5` 方法的作用是测试 `insert` 方法。
*   **场景 5: 运行测试并观察结果**。讲师运行 `test5` 方法，终端输出显示了三个规则被触发，分别对应 `age == 10`、`age < 10` 和 `age > 10 && age < 20` 的条件。讲师解释了为什么这三个规则都被触发了。
