# 86-规则引擎Drools-Drools实战（保险产品准入 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是完成了我们决策表这个入门案例啊

其实关于这个入门案例呢,我们再来看一下

打开我们这个决策表

这块呢,我们需要来说明一下

但是我们强调是每一行,对吧

从这一行开始,每一行表示一个规则

但是呢,并不是说这一行上面这几个条件啊

只能写一个

只不过我们举的这个例子是这样的

你比如说我现在在这个地方,对吧

这一行是不是一条规则嘛

我这个单元格里面是不是写了个男

然后呢,这个单元格呢,我写一个什么呢

23,然后逗号,然后35

大家来看一下

那也就是说我这一行上面是不是写了两个条件呢

一个要求的是sex,就是性别的要求

还有一个是对年龄的要求

甚至这个地方呢,我也可以写

比方说我这写个5000

好,那就是这个呢

这一行是不是有三个条件

三个条件

三个条件

但是最终呢

它肯定是给我们合并成一个条件啊

这其实都是不同的这个属性约束嘛

好,那接下来你看我改完之后啊

咱们接下来再来执行一下我们这个单元测试方法

我们主要看什么呢

主要就是看它给我们编译完之后

咱们看它生成的这个规则到底长得什么样

大家来看一下

就看我们第一条

你看

这个地方是不是就已经发生了变化

首先一个是sex,不等于男

是不是对应的

就是我们这个地方

这个条件,对不对

然后呢

接下来是age小于23

或者age大于35

那这个从哪来的呢

它是不是来自于我们这个条件啊

这个条件

咱们现在是不是写到23,35嘛

然后还有一个是5000的

这个是salary,对吧

你看

这个是不是就加上了

那你比如说我现在啊

把这个5000这个给去掉

咱们当时也一再强调

如果这个单元格为空

那么我们这条

这个规则

就会忽略这个条件

就会忽略这个条件

所以你看我把这个5000删掉之后啊

然后我们再来执行一下

再来看我们注意是第一个规则

第一个规则

你看

它现在是不是就没有那个条件了

对吧

就是salary

然后大于5000那个条件

小于5000那个条件就没有了

好

所以说

我们一再强调是每一行

这个数据表示一个规则

然后呢

如果这里边是空的单元格

就可以忽略

不是空的呢

它就会把这个条件

是不是对应的给我们加上

对应的就是这个条件

对吧

然后呢

它可以通过这个站位符

$1表示取第一个值

$2呢

表示取第二个值

好

对应的一个单元格

它的第二个值

好

这个呢

是对咱们这个入门案例的一个扩展吧

一个扩展的说明

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析报告：

---

### 1) 视频摘要

本视频演示了如何使用 **Drools** 规则引擎结合 **Excel 决策表** 来实现业务规则的自动化判断。核心流程包括：
1.  在 Excel 中创建一个结构化的决策表，定义规则的条件（Condition）和对应的执行动作（Action）。
2.  使用 Drools 的 `SpreadsheetCompiler` 工具将 Excel 决策表编译成可执行的 DRL（Drools Rule Language）规则文件。
3.  在 Java 代码中加载编译后的规则，创建一个 `PersonInfoEntity` 对象作为事实（Fact），并将其放入规则引擎的会话（KieSession）中。
4.  触发规则引擎执行，根据事实数据匹配决策表中的规则，并执行相应的动作（如将提示信息添加到一个列表中）。
5.  最终通过打印列表内容，验证规则引擎是否成功执行了预期的规则。

整个演示旨在说明如何将复杂的业务规则从业务人员熟悉的 Excel 表格形式，转化为可由程序自动执行的规则引擎逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **引言与环境准备**。展示 Excel 决策表的初始状态，介绍规则引擎的背景和目标。
*   **00:16 - 00:30**: **创建决策表**。在 Excel 中定义规则集（RuleSet）、变量（Variables）、导入（Import）和规则表（RuleTable）的结构。
*   **00:31 - 00:45**: **定义规则条件与动作**。在 Excel 表格中为“性别规则”、“年龄规则”、“月薪规则”分别设置具体的条件值和对应的中文提示动作。
*   **00:46 - 01:00**: **Java 代码实现**。展示如何在 IntelliJ IDEA 中编写 Java 测试类 `DTTest`，并使用 `SpreadsheetCompiler` 编译 Excel 决策表。
*   **01:01 - 01:15**: **执行规则引擎**。在 Java 代码中创建 `PersonInfoEntity` 对象，设置其属性（性别、年龄、月薪），并将其放入 `KieSession`。
*   **01:16 - 01:30**: **触发规则并输出结果**。调用 `session.fireAllRules()` 触发规则执行，并通过循环打印 `listRules` 列表中的所有提示信息，验证规则是否生效。
*   **01:31 - 01:45**: **结果分析与总结**。展示最终输出的提示信息，说明规则引擎成功匹配并执行了所有符合条件的规则。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲中明确提到了“9.3.2 规则介绍”和“9.3.3 实现步骤”，说明本节内容属于一个更大型的“Drools 实战”系列课程。
    *   文档中提到“各保险公司针对人身、财产推出了不同的保险产品...”，这是规则引擎应用的典型业务场景。

*   **关键代码**:
    *   **Excel 决策表结构**:
        *   **RuleSet**: `personCheck`
        *   **Variables**: `java.util.List`, `Sequential: true`
        *   **Import**: `com.ithema.drools.entity.PersonInfoEntity`, `java.util.List`
        *   **RuleTable**: `personCheck`
        *   **规则条件**: `sex = $1`, `age < $1 || age > $2`, `salary < $1`
        *   **规则动作**: `listRules.add("$1");`
        *   **规则分组**: `agenda-group "sign"`
    *   **Java 代码**:
        ```java
        public void test1() throws Exception {
            String realPath = "d:\\testRule.xls"; // 指定决策表x1s文件的磁盘路径
            File file = new File(realPath);
            InputStream is = new FileInputStream(file);
            SpreadsheetCompiler compiler = new SpreadsheetCompiler();
            String drl = compiler.compile(is, InputType.XLS);
            System.out.println(drl);

            KieHelper kieHelper = new KieHelper();
            kieHelper.addContent(drl, ResourceType.DRL);
            KieSession session = kieHelper.build().newKieSession();

            PersonInfoEntity personInfoEntity = new PersonInfoEntity();
            personInfoEntity.setSex("男");
            personInfoEntity.setAge(35);
            personInfoEntity.setSalary(12000);

            session.setGlobal("listRules", new ArrayList<String>());
            session.insert(personInfoEntity);
            session.getAgenda().getAgendaGroup("sign").setFocus();
            session.fireAllRules();

            for (String s : (List<String>) session.getGlobal("listRules")) {
                System.out.println(s);
            }

            session.dispose();
        }
        ```

*   **关键公式 / 图表**:
    *   **决策表中的条件表达式**:
        *   `sex = $1`：表示性别条件，$1 是 Excel 表格中第一列的值。
        *   `age < $1 || age > $2`：表示年龄条件，$1 和 $2 分别是 Excel 表格中第二列和第三列的值。
        *   `salary < $1`：表示月薪条件，$1 是 Excel 表格中第三列的值。
    *   **规则引擎输出**:
        *   `listRules.add("性别不对");`
        *   `listRules.add("年龄不合适");`
        *   `listRules.add("工资太低了");`

---

### 4) 关键场景与演示描述

*   **场景一：Excel 决策表的创建与编辑**
    *   **描述**: 视频首先展示了 Excel 表格 `testRule.xls` 的初始状态，其中包含了规则集、变量、导入等元信息。随后，演示者在表格中逐行添加具体的规则条件和动作，例如在“性别规则”行中输入“男”，在“年龄规则”行中输入“22.40”，在“月薪规则”行中输入“10000”。
    *   **技术点**: 展示了如何在 Excel 中定义规则的条件和动作，以及如何使用 `$1`, `$2` 等占位符来引用表格中的列值。

*   **场景二：Java 代码的编写与编译**
    *   **描述**: 视频切换到 IntelliJ IDEA，演示者编写了一个名为 `DTTest` 的 Java 类。代码中使用 `SpreadsheetCompiler` 类将 Excel 文件 `testRule.xls` 编译成 DRL 规则文件，并打印出编译后的规则内容。
    *   **技术点**: 展示了如何使用 Drools 的 API 将 Excel 决策表编译成可执行的规则文件，以及如何在 Java 代码中加载和使用这些规则。

*   **场景三：规则引擎的执行与结果输出**
    *   **描述**: 在 Java 代码中，演示者创建了一个 `PersonInfoEntity` 对象，并为其设置性别、年龄和月薪属性。然后，将该对象插入到规则引擎的会话中，并调用 `fireAllRules()` 方法触发规则执行。最后，通过循环打印 `listRules` 列表中的所有提示信息。
    *   **技术点**: 展示了如何将业务数据（事实）放入规则引擎，并通过触发规则来执行业务逻辑。最终输出的提示信息“性别不对”、“年龄不合适”、“工资太低了”表明规则引擎成功匹配并执行了所有符合条件的规则。

*   **场景四：规则匹配与动作执行的验证**
    *   **描述**: 视频展示了规则引擎执行后，`listRules` 列表中的内容。通过打印这些内容，可以验证规则引擎是否成功执行了预期的规则。
    *   **技术点**: 通过输出结果来验证规则引擎的正确性，这是规则引擎开发和测试中的关键步骤。

---

以上是根据您提供的视频画面进行的结构化分析。希望这份报告对您理解该技术课程有所帮助。
