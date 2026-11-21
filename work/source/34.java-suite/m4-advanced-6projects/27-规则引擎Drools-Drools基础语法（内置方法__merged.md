# 27-规则引擎Drools-Drools基础语法（内置方法_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们D-Rose基础语法

那么下一个小节我们讲的是D-Rose的内置方法

那么规则文件的RHS部分

主要作用是通过插入删除或修改工作内存中的FAC的对象

来达到控制我们规则引擎执行的这么一个目的

首先我们来看RHS

前面我们已经解释过了

是不是就是指的我们哪一部分呢

就是我们这个Zen跟N的中间加的这一部分

这个是我们的RHS部分

那么在这一部分主要做的事

我们通常写的代码是什么呢

就是通过插入删除或是修改

我们工作内存中的FAC的对象或是FAC的数据

大家还记得什么是FAC的吗

是不是指的就是我们将一个Java对象

把它加到工作内存中的这种对象

我们就称为FAC的对象

那么我们可以在咱们这个RHS

这个部分通过我们D-Rose提供的一些内置的方法

就是插入删除修改这些方法

来操作我们的FAC的对象

最终来达到控制我们规则引擎执行的这么一个目的

这是我们经常在这个RHS这个部分来编写的这一类的代码

那么D-Rose提供了一些方法

用来操作我们工作内存中的这些数据

操作完成后注意看

操作完成后

规则引擎会重新进行相关的执行

相关规则的匹配

这一句非常重要

一会儿我们也可以演示出来这个效果

就是操作完成之后

原先就是原来没有匹配成功的这个规则

在我们操作数据后

有可能就会匹配成功了

那么匹配成功之后

它是不是就会执行

好

这是我们先简单介绍了一下

首先我们D-Rose内置了一些方法

这些方法可以在哪用呢

可以在我们规则文件

或者说规则体的RHS

这个部分来使用这些方法

那么这几个方法呢

就是什么呢

大家可以看到有Update的方法

有Insert的方法

还有Retrack的方法

那么这是它内置的一些方法

我们通过这些方法可以干什么呢

可以插入删除修改

我们工作内存里面的这些Fag的对象

那么修改之后

能达到一个什么样的效果呢

就是它可以导致我们规则引擎

重新进行规则的匹配

原来呢

有一些可能没有匹配成功的规则了

在我们操作完成这些对象之后

有可能它就会匹配成功了

这是我们这些内置方法

能够起到的作用

那么为了演示这些内置的方法呢

咱们可以来创建一个实体类

一会儿呢

我们就基于这个实体类来操作

这个实体类呢

也是非常简单

比如就我们来一个Student

对吧

学生这么一个实体类

然后呢

这个类里面呢

就三个属性ID、Name、Age

这个都比较简单

我们先把它来创建一下

为我们一会儿编写这个测试啊

来提供这个支持

那么我们在这儿呢

来创建一个Student

在这儿呢

我就不再手敲了

我直接

把这块吧

整个三个属性以及对应的getSet方法

对吧

都复制过来

这个没什么好说的

这是我们的学生实体

好

这是我们的学生实体类

我们先做好一些准备工作

等一下呢

我们就来测试一下这三个方法

update、insert

还有retrack的这些方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的技术教学内容，主要讲解其内置的 **数据操作方法**。讲师通过在 IntelliJ IDEA 开发环境中演示，结合 Markdown 文档和代码示例，系统地介绍了 `update`、`insert` 和 `retract` 三个核心方法的作用。这些方法用于动态修改工作内存中的 Fact 数据，从而触发规则引擎重新评估和匹配规则。视频内容结构清晰，通过创建 `Student` 实体类和编写测试规则，直观地展示了如何在规则文件（`.drl`）中使用这些方法来控制规则的执行流程。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节按画面内容和逻辑顺序排列：

*   **章节 1: DRL 规则文件的 RHS 部分与内置方法介绍 (00:00:00)**
    *   画面显示 Markdown 文档，标题为“4.8 Drools内置方法”。
    *   内容解释了规则文件的 RHS（右侧）部分用于操作工作内存中的 Fact 数据，以控制规则引擎的执行。
    *   强调了 `update`、`insert`、`retract` 等方法的作用是修改数据后，触发规则重新匹配。

*   **章节 2: 创建 Student 实体类 (00:00:00 - 00:00:05)**
    *   讲师在 Markdown 文档中展示了一个 `Student` 类的代码示例，包含 `id`、`name`、`age` 字段和 `getId()` 方法。
    *   同时在 IDEA 中展示了 `Student.java` 文件，讲师正在编写 `setName` 和 `setAge` 等 setter 方法。

*   **章节 3: 介绍 `update` 方法 (00:00:05 - 00:00:10)**
    *   讲师在 Markdown 文档中点击并高亮了“4.8.1 update方法”。
    *   文档内容解释了 `update` 方法的作用是更新工作内存中的数据，并让相关规则重新匹配。
    *   画面切换到 IDEA，展示了 `Student.java` 文件，讲师正在编写 `setAge` 方法。

*   **章节 4: 介绍 `insert` 方法 (00:00:10 - 00:00:15)**
    *   讲师在 Markdown 文档中点击并高亮了“4.8.2 insert方法”。
    *   文档内容解释了 `insert` 方法的作用是向工作内存中插入数据，并让相关规则重新匹配。
    *   画面切换到 IDEA，展示了 `comparisonOperator.drl` 文件，其中包含两个规则：`rule_comparison_matches` 和 `rule_comparison_not_matches`，用于演示 `matches` 和 `not matches` 操作符。

*   **章节 5: 介绍 `retract` 方法 (00:00:15 - 00:00:20)**
    *   讲师在 Markdown 文档中点击并高亮了“4.8.3 retract方法”。
    *   文档内容解释了 `retract` 方法的作用是将 Fact 从工作内存中移除，从而触发规则重新匹配。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / Markdown 文档内容:**
    *   **标题:** “4.8 Drools内置方法”
    *   **核心概念:** 规则文件的 RHS 部分用于操作 Fact 数据，以控制规则引擎执行。
    *   **方法列表:**
        *   `update` 方法：用于更新工作内存中的数据。
        *   `insert` 方法：用于向工作内存中插入数据。
        *   `retract` 方法：用于从工作内存中移除 Fact。
    *   **代码示例:**
        ```java
        package com.itheima.drools.entity;

        import java.util.List;

        /**
         * 学生
         */
        public class Student {
            private int id;
            private String name;
            private int age;

            public int getId() {
                return id;
            }

            public void setId(int id) {
                this.id = id;
            }

            public String getName() {
                return name;
            }

            public void setName(String name) {
                this.name = name;
            }

            public int getAge() {
                return age;
            }

            public void setAge(int age) {
                this.age = age;
            }
        }
        ```

*   **IDEA 项目结构与代码:**
    *   **项目路径:** `drools_quicksart`
    *   **规则文件:** `comparisonOperator.drl`
    *   **规则代码:**
        ```drl
        rule "rule_comparison_matches"
            when
                ComparisonOperatorEntity(names matches "王.*")
            then
                System.out.println("规则: rule_comparison_matches触发了...");
            end

        rule "rule_comparison_not_matches"
            when
                ComparisonOperatorEntity(names not matches "王.*")
            then
                System.out.println("规则: rule_comparison_not_matches触发了...");
            end
        ```

---

### 4) 关键场景与演示描述

*   **场景 1: 展示 DRL 规则文件的 RHS 功能 (00:00:00)**
    *   讲师通过 Markdown 文档，向观众解释了规则引擎中 RHS（右侧）部分的核心作用：通过插入、删除或修改 Fact 数据来控制规则的执行。这为后续介绍内置方法奠定了理论基础。

*   **场景 2: 创建并完善 Student 实体类 (00:00:00 - 00:00:15)**
    *   讲师在 IDEA 中打开 `Student.java` 文件，逐步编写 `setName` 和 `setAge` 方法。同时，他在 Markdown 文档中展示了一个完整的 `Student` 类代码，强调了实体类是规则匹配的基础数据对象。

*   **场景 3: 演示 `insert` 方法 (00:00:10)**
    *   讲师在 IDEA 中打开 `comparisonOperator.drl` 文件，展示了两个规则：`rule_comparison_matches` 和 `rule_comparison_not_matches`。
    *   他通过注释 `//插入数据，导致相关的规则会重新匹配` 来说明 `insert` 方法的作用，即在规则中插入一个 Fact 后，会触发规则重新评估。

*   **场景 4: 演示 `update` 方法 (00:00:05)**
    *   讲师在 Markdown 文档中高亮了 `update` 方法，并在 IDEA 中展示了 `Student.java` 文件。
    *   他通过编写 `setAge` 方法，向观众说明 `update` 方法用于修改已存在的 Fact 数据，从而触发规则重新匹配。

*   **场景 5: 演示 `retract` 方法 (00:00:15)**
    *   讲师在 Markdown 文档中高亮了 `retract` 方法。
    *   虽然视频中未直接演示 `retract` 方法的代码，但通过上下文可以推断，该方法的作用是将一个 Fact 从工作内存中移除，从而触发规则重新评估。这与 `insert` 和 `update` 方法共同构成了对工作内存数据的完整操作能力。
