---
title: "Drools 开篇：从信用卡审批的 if-else 到第一条图书优惠规则"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 开篇：从信用卡审批的 if-else 到第一条图书优惠规则

写业务系统绕不开一堆 if-else：审批、风控、促销，规则又多又常改，改一次规则就要动一次代码、发一次版。规则引擎这一章从"为什么需要它"讲起，本篇覆盖课程前三部分：问题引出、规则引擎概述（定义、优势、应用场景、Drools 介绍），以及入门案例的开发上半场，工程、配置、实体类和规则文件。整个课程共九个章节，后面还排着基础语法、十个规则属性、高级语法、Spring 整合、WorkBench 与实战，先把地基打牢。

## 先给结论

- 规则引擎全称业务规则管理系统（BRMS，Business Rule Management System），不是某个具体框架，而是一类系统的统称；核心思想是把业务决策从程序代码里分离出来，用预定义的语义模块编写规则，由用户或开发者按需配置管理。
- 规则在规则引擎里被当成数据：规则库类比数据库，一条条规则就是一条条数据，可以增删改查、动态修改，不重启服务就能变更。
- 用 if-else 硬编码业务规则有三个痛点：难以维护、难以应对变化、改完代码必须重启服务才生效；规则变动越频繁，这些痛点越尖锐。
- 使用规则引擎有六条优势，根源都是规则与代码分离；典型应用场景四类：风险控制、反欺诈、决策平台、促销平台，凡规则复杂且频繁变动的系统都适用。
- Drools 是 JBoss 组织基于 Java 语言开发的开源规则引擎，规则以脚本形式存放（文件、数据库均可），规则变更不改项目代码、不重启服务即可线上生效；单独使用只需导入 drools-compiler 坐标，IDEA 已内置插件。
- Drools API 的主线固定六步：获取 KieServices → 获取 KieContainer → 获取 KieSession → 操作 Fact → 触发规则 → 关闭 KieSession，套路和 JDBC 一样模板化；入门案例按 Maven 工程、kmodule.xml、实体类 Order、rules/bookDiscount.drl 四步搭出来。

## 从信用卡审批看 if-else 之痛

场景是在线申请信用卡：用户在表单里录入姓名、性别、年龄、学历、电话、月收入、是否有房、是否有车、现持有信用卡数量，点击提交后，服务端先做用户信息合法性检查，判断有没有资格申请。银行要承担"先刷卡消费、后还款"的风险，所以重点看学历、月收入、房、车和已有信用卡数量这几项。合法性检查共四条规则：

| 规则 | 条件 | 结论 |
|---|---|---|
| 1 | 无房无车，学历大专及以下，月薪少于 5000 | 不通过 |
| 2 | 无房无车，学历大专或本科，月薪少于 3000 | 不通过 |
| 3 | 无房无车，学历本科以上，月薪少于 2000，且之前没办过信用卡 | 不通过 |
| 4 | 已有信用卡数量大于 10 | 不通过 |

任意一条命中，这个人就没有资格；四条全不命中才算通过。通过之后还要按五条规则确定额度，不同用户的额度不一样：

| 规则 | 条件 | 额度 |
|---|---|---|
| 1 | 有房有车，或月收入 20000 以上 | 15000 |
| 2 | 没房没车，月收入 10000 到 20000 | 6000 |
| 3 | 没房没车，月收入 10000 以下 | 3000 |
| 4 | 有房没车或没房有车，月收入 10000 以下 | 5000 |
| 5 | 有房没车或没房有车，月收入 10000 到 20000 | 8000 |

最容易想到的实现就是分支判断。合法性检查封装成 checkUser 方法，返回 true 表示通过：

```java
public boolean checkUser(User user){
    if(user.getHouse() == null
        && user.getCar() == null
        && user.getEducation().equals("大专及以下")
        && user.getSalary() < 5000){
        return false;
    }
    else if(user.getHouse() == null
        && user.getCar() == null
        && user.getEducation().equals("大专或本科")
        && user.getSalary() < 3000){
        return false;
    }
    else if(user.getHouse() == null && user.getCar() == null
        && user.getEducation().equals("本科以上")
        && user.getSalary() < 2000
        && user.getHasCreditCard() == false){
        return false;
    }
    else if(user.getCreditCardCount() > 10){
        return false;
    }
    return true;
}
```

确定额度的 determineCreditCardLimit 同理，一长串 else-if 从 15000 一路判断到 3000，五条规则五层分支，这是伪代码但和真实写法已经差不多。代码能跑，问题也很清楚：一个规则一个 if，规则有多少条，分支就堆多深。硬编码实现业务规则有三个问题：一是难以维护；二是难以应对变化，月收入区间从一万到两万改成两万到三万，代码就得跟着改；三是改完代码还要重启服务才生效。业务规则变化越频繁，这三条越致命。把规则单独提出来、可以动态修改、无需重启服务，这正是规则引擎的用武之地。

## 规则引擎：把业务规则当数据管理

规则引擎全称业务规则管理系统（BRMS）。它不是具体的技术框架，而是像 OA、ERP、CRM 一样指一类系统；市面上具体的产品有 Drools、VisualRules、iLog 等，本课程用的是 Drools（读音有人读 Drools、有人读 Juice，不必纠结）。

它的核心思想：把业务决策部分从程序中分离出来，用预定义的语义模块编写业务规则，由用户或开发者在需要时配置管理。规则引擎里有一个规则库的概念，可以把它想象成数据库，一条条业务规则就是库里的一条条数据。既然是数据，就能做增删改查：规则不再适用就更新，业务发展了就扩展第五条、第六条规则。

规则引擎也可以理解成一个输入输出平台，类似大脑：输入原始数据（学历、月薪、是否有房、是否有车），内部自动解释并匹配配置好的规则进行计算，输出反馈结果（是否有资格申请信用卡）。引入规则引擎后，业务规则不再以代码形式驻留在业务系统里，而是存在规则库中，完全独立于程序；业务人员可以像管理数据一样查询、添加、更新规则，规则被加载进规则引擎供应用调用。

由此派生出六条优势：业务规则与系统代码分离、集中管理；不重启服务即可随时扩展和维护规则；动态修改规则、快速响应需求变更，改规则就像改数据库里的数据；规则引擎相对独立、只关心业务规则，业务分析人员也能参与编辑维护；减少硬编码业务规则的成本和风险；还提供专门的编辑工具 Workbench（图形化界面），复杂规则的处理变得简单。六条优势归根结底都源于第一条：规则与代码分离。

应用场景上，规则引擎适合"存在复杂业务规则且频繁变动"的系统，典型四类：风险控制系统（风险贷款、风险评估）、反欺诈项目（银行贷款、征信验证）、决策平台系统（财务计算）、促销平台系统（满减、打折、加价购，双十一、618 这类活动规则）。不止这四类，规则多且常变的系统都可以考虑。

## Drools 与它的 API 主线

Drools 是 JBoss 组织提供的基于 Java 语言开发的开源规则引擎，它把复杂多变的业务规则从硬编码中解放出来，以规则脚本的形式存放在文件或特定存储介质中（比如数据库，也可以放 Excel），使业务规则的变更不需要修改项目代码、重启服务器就可以在线上环境立即生效。官网是 drools.org（在国外，打开稍慢），源码托管在 GitHub：github.com/kiegroup/drools。

使用上既可以单独使用，也可以跟 Spring 整合；单独使用只需导入一个 Maven 坐标。开发环境方面，IDEA 已经集成了 Drools 插件，编写规则脚本时全程有提示；用 Eclipse 则要单独安装插件，本课程基于 IDEA。

用 Drools API 开发的主线固定六步：第一步获取 KieServices；第二步通过它获得 KieContainer（容器）；第三步从容器里获取 KieSession（会话）；第四步用 Session 操作 Fact，Fact 翻译过来是事实对象，可以先理解成普通的 JavaBean；第五步规则引擎触发规则、产生结果；第六步关闭 KieSession。整个过程高度模板化，和使用 JDBC 操作数据库（加载驱动、获取连接、编写 SQL、传参执行、解析结果）是同一个套路。先留个整体印象，入门案例里每一步都会用到。

## 入门案例（上）：四步写出图书优惠规则

案例场景：消费者在图书商城购买图书，下单后支付页面要显示订单优惠后的价格。优惠规则四条：

| 规则 | 条件 | 优惠 |
|---|---|---|
| 1 | 所购图书总价 100 元以下 | 无 |
| 2 | 总价 100 到 200 元 | 20 元 |
| 3 | 总价 200 到 300 元 | 50 元 |
| 4 | 总价 300 元以上 | 100 元 |

第一步，创建普通 Maven 工程（不用骨架），artifactId 与讲义保持一致叫 drools-quickstart；检查 JDK 与 Maven 本地仓库配置无误后，在 pom 里导入坐标，顺手带上 junit 方便单元测试：

```xml
<dependency>
    <groupId>org.drools</groupId>
    <artifactId>drools-compiler</artifactId>
    <version>7.10.0.Final</version>
</dependency>
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
```

第二步，提供 Drools 框架所需的配置文件。位置和文件名都是固定写法，框架按约定解析：resources 下的 META-INF 目录，文件名 kmodule.xml，一个都不能写错：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kmodule xmlns="http://www.drools.org/xsd/kmodule">
    <!-- kbase：知识库，name 任意、唯一即可；packages 指向规则文件所在目录 -->
    <kbase name="mykbase" packages="rules" default="true">
        <!-- ksession：会话，可配置多个；default=true 表示默认 session -->
        <ksession name="ksession-rule" default="true"/>
    </kbase>
</kmodule>
```

配置里最要紧的是 kbase 的 packages 属性，它指定规则文件的目录：这里写了 rules，下一步就必须在 resources 下建一个 rules 目录，规则文件放别处是加载不到的。ksession 可以配置多个，当前这个标了 default，是默认会话。

第三步，创建实体类 Order（entity 包下）。它不是给数据库操作用的，而是应用与规则引擎之间输入输出的数据载体：规则引擎是输入输出平台，数据总得有对象来承载。originalPrice 是优惠前的原始价格，作为输入传给规则引擎；realPrice 是优惠后的真实价格，等规则算完反馈回来。

```java
public class Order {
    private Double originalPrice; // 订单原始价格，优惠前
    private Double realPrice;     // 订单真实价格，优惠后
    // getter/setter 与 toString 常规生成即可
}
```

第四步是重头戏：编写规则文件。规则文件后缀固定为 drl，必须放在 resources/rules 下与 kmodule 的 packages 对应，文件名任意，这里叫 bookDiscount.drl（图书打折）。IDEA 内置了 Drools 插件，创建后文件图标直接显示 Drools 的人脸 logo，编写时全程有提示。

规则文件里的 package 是逻辑概念，不必对应真实目录，同一 package 下的规则文件可以互相访问，不同包之间不行；要用 Order 就像写 Java 一样 import 进来。一条规则的结构是 rule 规则名 + when 条件 + then 结果 + end，规则名在文件内唯一，写英文或汉字都可以。第一条规则这样写：

```drl
package book.discount
import com.itheima.drools.entity.Order

// 规则一：所购图书总价在100元以下的没有优惠
rule "book_discount_1"
    when
        $order: Order(originalPrice < 100)
    then
        $order.setRealPrice($order.getOriginalPrice());
        System.out.println("成功匹配到规则一");
end
```

when 里的 Order(originalPrice < 100) 是模式匹配：到规则引擎的工作内存（Working Memory）中找 originalPrice 小于 100 的 Order 对象。之所以找得到，是因为调用方会把原始数据封装成 Order 交给规则引擎；$order 是给匹配到的对象起的名字，名字任意，then 部分拿它来写 Java 代码。没有优惠意味着真实价格等于原始价格，setRealPrice 一下，再打印一句匹配成功，方便测试时确认规则命中。

后面三条规则照葫芦画瓢：规则二 originalPrice 大于等于 100 且小于 200，在原始价格基础上减 20；规则三大于等于 200 且小于 300，减 50；规则四大于等于 300，减 100，没有上限就不写第二个条件。这里有个边界值细节：规则一写 < 100、规则二若写 > 100，总价恰好 100 元时两条都匹配不上，所以下限一律用 >= 把边界包进来。一个规则文件可以写多条规则，理论上没有数量限制，按业务来。到这里，规则文件已经写好，单元测试与规则引擎构成、执行过程、KIE 体系等概念留待下一篇展开。

## 小结

本篇回答了三个问题。为什么需要规则引擎：if-else 硬编码业务规则难维护、难应变、改了还要重启，信用卡审批的九条规则就是明证。规则引擎是什么：BRMS，一类把规则当数据管理的系统，规则库类比数据库，业务决策从代码中分离后可以动态修改、无需重启，Drools 是其中的具体产品。怎么上手：工程、META-INF/kmodule.xml、实体类 Order、rules/bookDiscount.drl 四步，API 主线 KieServices 到 KieSession 六步模板化。规则已就位，下一篇跑通单元测试，看优惠后价格如何从规则引擎传回应用，再进入基础语法。
