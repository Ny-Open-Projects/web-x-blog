# 12-1 行程规划经理挂载Skills

## 【学习目标】

- 理解 `AgentSkill` 对象的三种手工构建方式及其适用场景。
- 掌握以文件夹（`FileSystemSkillRepository`）方式加载 Skills 的工程化路径。
- 完成 `SkillBox` 到行程规划智能体的挂载，并记住「SKILL.md 的 name 与文件夹同名」这条硬约束。

## 【正文】

### 1. Skills 的载体与挂载入口

第 10 章讲过：Skills 的载体是 skill markdown 文件，一个技能对应一个文件夹，`SKILL.md` 必须存在；其中 `name` 与 `description` 两个标签为必填。AgentScope 把 Skills 挂载到智能体分两步：先把 `SKILL.md` 的内容转化为 `AgentSkill` 对象，再通过 `SkillBox` 装载，`SkillBox.registerSkill(...)` 装入技能对象，智能体侧的 `skillBox(...)` 方法把 `SkillBox` 加载进去，挂载即完成。

### 2. 三种手工构建 AgentSkill 的方式

**方式一：builder 工厂方法。** `name()`、`description()` 与 `SKILL.md` 中的标签一一对应，附加内容通过 `skillContent(...)`、`addResource(...)`、`source(...)` 补充：

```java
AgentSkill skill = AgentSkill.builder()
    .name("data_analysis")
    .description("Use this skill when analyzing data...")
    .skillContent("...")
    .addResource("references/formulas.md", "常用公式")
    .source("custom")
    .build();
```

**方式二：整段 MD 字符串 + 工具类转换。** 把 `SKILL.md` 全文作为字符串，附带上资源文件映射，交给 `SkillUtil.createSkillFromMD` 转换：

```java
String skillMD = """
name: data_analysis
description: Use this skill when analyzing data...
Content:
...
""";

Map<String, String> resources = Map.of(
    "references/formulas.md", "常用公式",
    "examples/sample.csv", "name,value,100,200"
);

AgentSkill skill = SkillUtil.createSkillFromMD(skillMD, resources);
```

**方式三：构造器直接 new。** 把 `name`、`description`、正文内容与资源按序传入构造方法：

```java
AgentSkill skill = new AgentSkill(
    "data_analysis",
    "Use when analyzing data...",
    "Data Analysis...",
    resources
);
```

三种方式对比：

| 方式 | 内容来源 | 资源携带 | 适用场景 |
|---|---|---|---|
| builder | 链式逐个赋值 | `addResource` 逐个添加 | 代码里动态生成技能 |
| MD 字符串 | 完整 `SKILL.md` 文本 | `Map` 批量映射 | 从别处（库/接口）读到 MD 文本 |
| 构造器 | 构造参数按序传入 | 直接传资源集合 | 最简单的硬编码演示 |

### 3. 挂载：SkillBox 与智能体

`SkillBox` 负责收纳技能对象，可以基于 `Toolkit` 创建；智能体通过 `skillBox(...)` 完成加载。课程给出的装配示例：

```java
Toolkit toolkit = new Toolkit();
SkillBox skillBox = new SkillBox(toolkit);
skillBox.registerSkill(skill);

ReActAgent agent = ReActAgent.builder()
    .toolkit(toolkit)
    .model(model)
    .toolkit(toolkit)
    .memory(new Memory())
    .build();
```

按原稿如实说明：示例中 `.toolkit(toolkit)` 连续出现了两次，属重复设置，此处按原稿保留、不作改写；实际编写时设置一次即可。此外该示例聚焦 Toolkit 与 SkillBox 的装配，`skillBox(...)` 的加载调用在前文叙述中给出。

### 4. 工程化选择：按文件夹加载

三种手工方式对工程化都不友好：技能内容硬编码在 Java 代码中，改一句文案就要重新编译。前面课程用 Spring AI 1.1.2 演示时采用的是文件形式，在 `resources` 下放置 `SKILL.md`，直接加载文件。AgentScope 的 `AgentSkill` 文档同样提供了文件加载方式（除文件外还支持从 Nexus 仓库加载）。

按文件方式改造：在 `resources` 下建 `skills` 文件夹，每个技能一个子文件夹（技能不止一个，需要分别存放）；通过 `FileSystemSkillRepository` 指向该目录，按名读取技能。必须注意：`SKILL.md` 中 `name` 属性的值必须与所在文件夹名称相同，否则按名加载会失败。

```java
// 构建Skill
SkillBox skillBox = new SkillBox();
skillBox.registerSkill(skillMD);

// 从文件系统读取技能
llRepository repo = new FileSystemSkillRepository(
    Path.of("./skills")
);

// 读取并注册技能
ll SuggestSightsSkill = repo.getSkill(name: "Suggest_Sights");
ll MakeATableSkill = repo.getSkill(name: "Make_A_Table");
.registerSkill(SuggestSightsSkill);
.registerSkill(MakeATableSkill);
```

按原稿如实说明：该代码块为文档示例摘录，存在明显缺行与错位，`llRepository`、`ll SuggestSightsSkill` 中的 `ll` 前缀应为 `AgentSkill` 类型的简写残留，末尾两个 `.registerSkill(...)` 缺少调用主语且缩进错位。此处按原稿保留、不作改写；实际编写时应先取得 `AgentSkill` 实例，再逐个调用 `skillBox.registerSkill(...)` 完成注册。

### 5. 挂载到行程规划智能体

回到行程规划模块的智能体创建方法：`new SkillBox()` 创建技能盒，用 `registerSkill(...)` 装入景点推荐技能与表格制作技能两个 `AgentSkill` 对象，再通过智能体的 `skillBox(...)` 方法把 `SkillBox` 加载进去，两个技能即挂载到行程规划智能体。

挂载顺序上有一个细节：先建 `SkillBox` 并完成注册，再挂到智能体。顺序颠倒会导致智能体持有的是一个空技能盒，技能注册是挂载前的动作，不是挂载后的补充。

从课程演进看，这条挂载链是第 10 章 Skills 三讲（是什么 → 装载什么 → 渐进式加载）的落地终点：文件结构标准（10-5）规定目录长什么样，`FileSystemSkillRepository` 负责按标准读取，`SkillBox` 完成收纳，`skillBox(...)` 完成注入。四步各自职责单一，任何一步出问题都能独立定位。

```mermaid
flowchart LR
    A["resources/skills/ 技能文件夹"] -->|"FileSystemSkillRepository 按名读取"| B["AgentSkill 技能对象"]
    B -->|"SkillBox.registerSkill"| C["SkillBox 技能盒"]
    C -->|"agent.skillBox(skillBox)"| D["行程规划智能体"]
```

## 【易错点 / 面试题】

1. **`name` 与文件夹不同名会怎样？** 按名加载（`getSkill(name)`）直接失败或返回空，这是加载类问题里最高频的一类，改文件夹名或改 `name` 标签保持一致即可。
2. **三种手工方式与文件夹方式怎么选？** 一次性演示、技能内容需动态生成时用手工方式；工程化维护用文件夹方式，技能内容与代码解耦，改 `SKILL.md` 即生效，无需重新编译。
3. **面试题：`SkillBox` 与 `Toolkit` 是什么关系？** `Toolkit` 管理「可执行工具」，`SkillBox` 管理「专业知识与工作流程」，且 `SkillBox` 可基于 `Toolkit` 创建；两者共同挂到 Agent，一个回答「用什么」，一个回答「怎么做」。第 10 章讲过的渐进式加载正是 `SkillBox` 的行为特征：先读 `description` 决定是否加载，再读全文。

## 【小结】

本节完成了行程规划智能体挂载 Skills 的全链路：`SKILL.md` → `AgentSkill` → `SkillBox` → 智能体，并选定文件夹加载作为工程化方案。下一节（12-2）深入一个具体技能，看景点推荐技能的 `SKILL.md` 该如何编写。在 `981-demo` 工程中，对应能力的载体是 `com/travel/agent/agent/TeamMembers.java` 的 `attractionAgent` Bean 与 `com/travel/agent/tool/AttractionTools.java`：课程用 `SkillBox` + `Toolkit` 双轨挂载「知识 + 工具」，工程版把同类「专业知识」下沉为 `sysPrompt` 与工具描述，保持同一套双轨结构。
