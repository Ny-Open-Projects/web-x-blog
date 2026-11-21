---
title: "Activiti7 入门复盘：环境、配置、建表串成一条线"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段二 传统行业解决方案SaaS-HRM项目]
tags: [Java, 项目实战]
---

# Activiti7 入门复盘：环境、配置、建表串成一条线

day01 学完回头看，内容又多又散：概念、插件安装、Maven 坐标、配置文件、测试类，每一块单独看都不难，可它们到底怎么咬合成一个能跑的工程？验收标准其实只有一条：运行一次测试，数据库里多出 25 张 `act_` 开头的表。

这里把入门阶段的知识重新串一遍，重点不是罗列步骤，而是把每一步「为什么存在」讲清楚。

## 先给结论

- Activiti 解决的核心问题是「业务代码不变更，流程可更新」：流程定义图的节点信息存在数据库表里，改流程改的是定义与表数据，业务代码不动。
- 入门落地只有四步：引 Maven 坐标、放 `log4j.properties`、放 `activiti.cfg.xml`、写测试代码跑一遍。
- 两个核心类要记住：`ProcessEngineConfiguration` 负责配置，`ProcessEngine` 是引擎本体，由前者构建。
- 自动建表的开关是 `databaseSchemaUpdate` 设为 `true`，25 张表在引擎初始化时生成。
- 表结构支撑是一切的前提：连表都没有，流程定义图的节点信息就无处存放，后续工作全部开展不了。

## 一、入门阶段铺开的概念地图

工作流这个词是从业务里长出来的。请假要走「员工填单，部门经理审批，总经理审批，财务经理归档」，调薪调岗又是另一条路径，这类按步骤流转的事务就是工作流。围绕它有几个概念容易混：

- **工作流系统**：把工作流落成软件，让流程在系统里真实跑起来。
- **BPM**：业务流程管理，是一套管理方法论，关心流程怎么设计、怎么优化。
- **BPMN**：业务流程建模标准，是流程定义的标准化语言，流程图按它画出来才能被引擎读懂。

各公司的审批路径不尽相同，有人力资源系统里走四级，有的走两级，这没关系，将来唯一变化的就是流程定义图。为了画这张图，入门课讲了流程设计器插件 Activiti Designer 在 Eclipse 与 IDEA 里的安装，装完都做了安装成功的验证。开发环境则选了 MySQL 作为引擎背后的数据库，引擎自身支持多种数据库，MySQL 是最常用的一种。

## 二、为什么值得引入一个工作流引擎

不用引擎时，流程节点写死在代码里：加一个审批人，就得改代码、改表结构、重新发版。Activiti 的解法是把流程从代码里抽出来，交给「流程定义 + 数据库表」去承载。

这张图把机制串起来：

```mermaid
flowchart LR
    A["流程定义图发生变更"] --> B["重新部署流程定义"]
    B --> C["节点信息读取后写入数据库表"]
    C --> D["业务代码只与引擎交互"]
    D --> E["流程按新图流转"]
    E --> F["业务代码零改动，流程快速更新"]
```

关键环节在「节点信息入库」：流程定义图部署后，各节点的信息被引擎读取并写进表里，后续的流转说到底就是对这些表做操作。流程要更新，改的是定义图和表里的数据，代码层面不需要跟着动。前面讲的流程定义、BPMN 标准、流程设计器，全是围绕这件事服务的。

## 三、四步搭出能建表的工程

**第一步，pom.xml 引入坐标。** 核心是 `activiti-engine` 7.0.0.Beta1，配套还有 `activiti-spring`、`activiti-bpmn-model` 等，外加 MySQL 驱动、junit、log4j、MyBatis、commons-dbcp（完整依赖清单见配套资料里的工程文件）。

**第二步，resources 下放 `log4j.properties`。** 建表过程发生在日志里，一条条 create table 都靠它打出来，没有这份配置，建表对你几乎是静默的。

**第三步，放 `activiti.cfg.xml`。** 这是引擎默认的配置文件名，课程工程里的原文如下（包名无关，配置原样）：

```xml
<!-- 数据源配置，dbcp 连接池 -->
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
    <property name="username" value="root" />
    <property name="password" value="root" />
</bean>

<!-- 引擎单独运行的配置对象，默认约定 bean 的 id 为 processEngineConfiguration -->
<bean id="processEngineConfiguration"
      class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <!-- 代表是否生成表结构 -->
    <property name="databaseSchemaUpdate" value="true"/>
</bean>
```

配置文件名也可以不叫这个，但那样加载时代码里就得显式写出你起的名字，文件叫什么代码就写什么。

**第四步，写测试代码。** 课程工程 `ActivitiTest` 里的写法（包名已改为 `com.example`）：

```java
package com.example.test;

import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.junit.Test;

/** 测试类：测试 Activiti 所需要的 25 张表的生成 */
public class ActivitiTest {

    @Test
    public void testGenTable() {
        // 条件：1.配置文件名称 activiti.cfg.xml  2.bean 的 id 为 processEngineConfiguration
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        System.out.println(processEngine);
    }
}
```

另一种显式写法是把两步拆开：先用 `ProcessEngineConfiguration.createProcessEngineConfigurationFromResource("activiti.cfg.xml")` 创建配置对象，再调 `configuration.buildProcessEngine()` 拿到引擎。两种写法殊途同归，后者在文件名或 bean id 不按默认约定时更灵活。

## 四、配置文件里到底做了什么

**第一件事，配置数据源。** dbcp 连接池的四个连接要素写全即可；这一步其实也可以省掉，不单独声明数据源，直接在配置对象上写 `jdbcDriver`、`jdbcUrl`、`jdbcUsername`、`jdbcPassword` 四个属性，同样能跑通。

**第二件事，创建 ProcessEngineConfiguration 的配置对象。** 采用的是独立运行方式，对应类 `StandaloneProcessEngineConfiguration`，含义是引擎不挂在 Spring 容器里，自己管理自己的运行。

**第三件事，打开自动建表开关。** `databaseSchemaUpdate` 设为 `true`，引擎初始化时检查表结构，缺哪张补哪张。这两个类的对象一旦创建出来，25 张表的工作就完成了。

跑完测试刷新数据库，看到的表名清一色 `act_` 开头：`act_ge_bytearray`、`act_re_procdef`、`act_ru_task`、`act_hi_procinst`、`act_id_user` 等等。前缀里的字母各有含义，是下一篇要展开的命名规范。

## 常见误区

- **配置文件名随手起**：`ProcessEngines.getDefaultProcessEngine()` 只认 `activiti.cfg.xml`，文件改了名而代码没显式传名，直接报找不到文件。
- **bean 的 id 改了名**：默认读取按 `processEngineConfiguration` 找 bean，改名后要么改回来，要么用双参数方法把 bean id 显式传进去。
- **没开 `databaseSchemaUpdate`**：测试照样绿，一张表都不会建，库里空空如也。
- **漏掉 `log4j.properties`**：建表日志打不出来，出了问题无从判断是没执行还是执行失败。

## 面试可能被问到的问题

1. 面试官追问：「Activiti 入门阶段要做哪几步？」
   答：四步：Maven 工程引入 Activiti7 相关坐标；resources 下添加 `log4j.properties`；添加默认配置文件 `activiti.cfg.xml`，配好数据源与引擎配置对象；写 Java 代码创建 ProcessEngineConfiguration 与 ProcessEngine，跑测试自动生成 25 张表。

2. 面试官追问：「ProcessEngineConfiguration 和 ProcessEngine 是什么关系？」
   答：前者是流程引擎的配置对象，承载数据源、建表策略等配置；后者是引擎本体，是工作流的门面。由配置对象调用 buildProcessEngine 构建出引擎实例，引擎再向外提供各类 Service。

3. 面试官追问：「为什么用 Activiti 之后改流程不用改代码？」
   答：流程被抽成流程定义，定义图的节点信息部署后存进数据库表，运行时的流转就是对这些表的操作。流程变化只需更新并重新部署流程定义，业务代码面向引擎接口编程，不感知流程内部结构。

4. 面试官追问：「databaseSchemaUpdate 设为 true 意味着什么？」
   答：引擎初始化时按内置建表脚本检查数据库，表不存在就创建，存在就沿用，保证 25 张表随时可用且不重复建。

5. 面试官追问：「配置文件必须叫 activiti.cfg.xml 吗？」
   答：不是强制。显式创建方式里文件名作为参数传入，叫什么都能加载；只有走 ProcessEngines.getDefaultProcessEngine() 这种最简写法时，才强制要求默认文件名和默认 bean id 两个约定。

## 配套资料

- 课程工程：`materials/code/02/Activiti7-day01-基础原理与使用/Activiti7-day01-基础原理与使用/代码/activiti01/`
  （含 `pom.xml`、测试类 `ActivitiTest.java`、`src/main/resources/activiti.cfg.xml`、`log4j.properties`，文中包名已统一改为 `com.example`）
- 依赖与配置素材：同目录 `素材/pom.xml`、`素材/activiti.cfg.xml`
