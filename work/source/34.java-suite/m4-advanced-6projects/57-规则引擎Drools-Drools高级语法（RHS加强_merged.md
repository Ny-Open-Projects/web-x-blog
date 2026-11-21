# 57-规则引擎Drools-Drools高级语法（RHS加强 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们D-Rose高级语法

还有最后一部分

最后这一部分不属于我们新的知识点了

它是针对我们编写规则文件的时候

有一些规范需要去遵守的

我们在进行DL类型的规则文件

编写时尽量来遵循如下的这些规范

这是比较好的一种习惯

第一个是所有的规则文件

应该统一放在一个规定的文件夹中

当前咱们其实就是这样做的

你看我们创建了这么多的规则文件

统一全都是放在Rules这个目录下

方便统一管理

这是第一个尽量做到

然后第二个是我们书写的每个规则

尽量加上注释

注释清晰明了

严谨宜改

这个不光是针对我们规则文件

包括我们写Java代码的时候

我们进行项目开发的时候

也都是这样的

尽量把注释写详细一点

然后第三个是同一类型的对象

尽量放在一个规则文件中

例如所有对于这种Student的类型对象

进行匹配的时候

放在统一的一个文件里边

而不是说好几个文件都用到Student的类

那么这个时候

我们尽量放在一个文件里边

方便统一管理

再下一个是规则结果部分

也就是我们的RHS部分

尽量不要有条件语句

就是说在我们这个

针后边这一部分

这里边就不要再出现if else了

如果再出现if else说明什么呢

说明我们当前这个规则

是不是还能再拆

所以说如果出现这种if

尽量不要有复杂的

这种什么逻辑和深层次的

前套语句

如果真的有这种情况

这就说明我们当前这个规则

它还可以再进行拆

把这一个规则

是不是按照我们的条件

给它拆成多个规则

那么每一个规则

尽量放在一块

不要有这种条件语句

应该是单一的

那么每个规则最好都加上

这个silence

明确执行的顺序

这就是我们执行的优先级

这个也是比较好的一个习惯

最后就是我们D-Rose默认的

这个方言是Java

尽量避免使用这种MVER

这是关于我们在进行

规则文件开发的时候

有一些编辑文件

就是我们的一些规范

这是我们的一些建议

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于 **Drools 规则引擎** 的技术教学课程。讲师通过 **IntelliJ IDEA** 集成开发环境，演示了如何在 Java 项目中编写和测试 Drools 规则文件（`.dsl` 文件）。主要内容包括：
- 展示了项目结构，特别是 `src/main/resources/rules/` 目录下的规则文件。
- 详细讲解了如何在 Java 测试类 `DroolsTest.java` 中通过 `drools.getRule()` 方法获取并操作规则对象。
- 重点演示了 `RuleImpl` 对象的多个属性，如 `getAutoFocus()`、`getId()`、`getDateExpires()` 等。
- 通过 `drools.halt()` 方法来暂停规则引擎的后续执行。
- 同时，讲师也展示了配套的 PPT 内容，讲解了 Drools 规则文件的编码规范和与 Spring 的整合方法。

整个演示过程旨在帮助学习者理解 Drools 规则引擎在 Java 应用中的集成方式和核心 API 的使用。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:05**：开场，展示项目结构，聚焦于 `src/main/resources/rules/` 目录。
- **0:05 - 0:15**：在 `DroolsTest.java` 文件中，讲解 `rule "rule_rhs_1"` 的代码块，重点是获取 `WorkingMemory` 和 `RuleImpl` 对象。
- **0:15 - 0:25**：继续讲解 `RuleImpl` 对象的属性，如 `getAutoFocus()`、`getId()`、`getDateExpires()`。
- **0:25 - 0:35**：演示 `drools.halt()` 方法的作用。
- **0:35 - 0:45**：切换到 PPT，讲解“6.6 规则文件编码规范”。
- **0:45 - 1:00**：回到代码，讲解 `rule "rule_rhs_2"` 的代码块。
- **1:00 - 1:10**：在 PPT 中，讲解“7.1 Spring简单整合Drools”的内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

- **章节标题**：
  - `6.6 规则文件编码规范`
  - `7.1 Spring简单整合Drools`

- **6.6 规则文件编码规范**：
  - **核心规范**：
    - 所有的规则文件（`.dsl`）应统一放在一个指定的文件夹中，如 `/rules`。
    - 每个规则文件应尽量加上注释，注释要清晰明了，语言简练。
    - 同一类型的对象尽量放在一个规则文件中，如所有 `Student` 类型的对象。
    - 规则结果部分（RHS）尽量不要有条件语句（如 `if(...)`），避免复杂的逻辑和深层次的嵌套。
    - 每个规则最好都加上 `salience` 属性，明确执行顺序。
    - Drools 默认使用 `dialect "java"`，尽量避免使用 `dialect "mvel"`。

- **7.1 Spring简单整合Drools**：
  - **核心内容**：在项目中使用 Drools 时，通常会与 Spring 整合。具体整合步骤如下（PPT 中未展开详细步骤，但标题暗示了后续内容）。

#### 代码内容

- **Java 代码（`DroolsTest.java`）**：
  ```java
  package tesths;

  import org.drools.core.WorkingMemory;

  rule "rule_rhs_1"
  when
  then
      System.out.println("规则: rule_rhs_1触发了...");
      WorkingMemory workingMemory = drools.getWorkingMemory(); // 获取工作内存对象
      System.out.println(workingMemory);
      org.drools.core.definitions.rule.impl.RuleImpl rule = drools.getRule(); // 获取当前规则对象
      System.out.println(rule);
      System.out.println(rule.getAutoFocus());
      System.out.println(rule.getId());
      System.out.println(rule.getDateExpires());
      drools.halt(); // 当前方法表示终止后面所有规则的执行
  end

  rule "rule_rhs_2"
  when
  then
      System.out.println("规则: rule_rhs_2触发了...");
  end
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构展示**
  - 讲师在 IntelliJ IDEA 中，通过项目导航面板（Project View）高亮显示了 `src/main/resources/rules/` 目录。
  - 展示了该目录下包含的多个 `.dsl` 文件，如 `activationsgroup.drl`、`agenda.drl`、`buildincomparator.drl` 等，说明规则文件的组织方式。

- **场景二：规则对象操作演示**
  - 讲师在 `DroolsTest.java` 文件中，将光标移动到 `rule "rule_rhs_1"` 的代码块。
  - 逐行讲解代码逻辑：
    - `drools.getWorkingMemory()`：获取工作内存对象。
    - `drools.getRule()`：获取当前规则对象。
    - `rule.getAutoFocus()`、`rule.getId()`、`rule.getDateExpires()`：分别获取规则的自动聚焦、ID 和过期时间属性。
    - `drools.halt()`：暂停规则引擎的后续执行。

- **场景三：PPT 规范讲解**
  - 讲师切换到 PPT，讲解“6.6 规则文件编码规范”。
  - 重点强调了规则文件的命名规范、注释要求、对象分组、RHS 简化、`salience` 属性和默认 dialect 的选择。

- **场景四：规则文件对比**
  - 讲师在代码中展示了 `rule "rule_rhs_1"` 和 `rule "rule_rhs_2"` 两个规则。
  - 通过高亮和滚动，对比了两个规则的结构和功能，为后续的规则执行和测试做准备。

- **场景五：代码注释与中文说明**
  - 代码中包含大量中文注释，如 `//获得工作内存对象，本质上是...`、`//获得当前规则对象`、`//当前方法表示终止后面所有规则的执行`。
  - 这些注释帮助学习者理解代码的业务逻辑和 API 的作用。

---

以上是根据视频画面进行的结构化技术分析。
