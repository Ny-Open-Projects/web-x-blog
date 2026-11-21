# 21-规则引擎内容介绍 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们课程第四章的第六部分。

前面呢,咱们是已经完成了什么呢?这个工具类的封装。

这里边封装呢,其实就是基于我们这个百度地图啊,来计算我们这个订单的距离,对吧?

好,这个都已经封装好了。

那么下一个呢,是我们一个新的技术点,叫做规则引擎,Juice。

有些人呢,叫做D-Rose,有些人读法叫做Juice。

这个读法呢,我们就不用纠结了。

好,然后呢,我们这个地方需要来说明一下,为什么要引入这个新技术。

就是因为我们后边呢,马上要开发的是我们计算订单价格。

而计算订单价格的时候呢,是不是有四个规则,对吧?有四个规则。

当然这四个规则呢,我们按照传统的做法,那么我们通过if-else判断这种方式呢,也能做出来。

但是呢,对于我们这种规则,那么也可以有其他的做法。

比如说啊,我们使用规则。

规则引擎,那么使用它呢,肯定是相对于我们以前传统的这种if-else啊,这种判断的方式呢,它是有一些优势的。

那么后边呢,随着我们学习这个D-Rose呢,大家应该都能体会出来。

那么由于D-Rose啊,整个这个技术体系呢,其实还是非常庞大的。

它包含的内容比较多啊。

所以说呢,我们专门整理了一个另外一个讲义,叫做规则引擎D-Rose讲义。

那么后边呢,我们就会。

来整体学习一下我们这个新的技术。

咱们现在来看一下,先来整个介绍一下我们这个D-Rose呢,会涉及到哪些内容的讲解。

第一个呢,就是问题引出。

这个地方呢,我们会介绍一个业务场景,就是在线申请信用卡,对吧?

基于这么一个业务场景啊,把我们相应的问题引出来。

这个问题是什么呢?

就是啊,在我们申请这个信用卡的时候呢,其实是有很多规则的。

那么你看啊,它这,这有一套规则,有四个,对吧?

然后呢,这又有一套规则,有五个。

好,那么按照以前的传统的做法,那么我们要实现的话呢,可能代码里边有各种各样的if-else判断,对吧?

如果是它符合第一个规则,然后呢,就执行这个操作。

如果符合第二个规则,就执行这个操作。

所以说呢,这个地方呢,按照传统的做法,这种分支判断的方式来实现的话,它其实是有一些问题的。

那么我们这个地方呢,首先呢,

来抛出这么一个业务场景,通过这个业务场景把问题,然后呢,把它引出来。

然后呢,我们再来介绍使用规则引擎呢,是如何来这个解决这个问题的。

然后后边呢,就是规则引擎的概述,对吧?

那么什么是规则引擎,使用规则引擎它的优势,然后它适合的场景。

然后呢,接下来是对这个D-Rose,这是规则引擎里边具体的一个技术,叫做D-Rose,也叫做Juice。

读法这个不一样啊。

那么对它做一个介绍。

然后接下来呢,我们会通过一个入门案例这种方式来学习一下这个D-Rose,它具体是怎么用的,对吧?

然后再往下呢,就是它的一些基础的语法。

因为我们要使用这个D-Rose的话,就需要去编写它的一个文件,这个文件呢,叫做规则文件。

那么在编写规则文件的时候呢,它是有自己的一套语法的。

所以我们在这呢,就需要来学习一下它这套语法。

然后接下来呢,还有它这个规则文件里面呢,有一些属性啊。

我们在这呢,单独再来说一下常用的几个属性,这是规则属性。

最后呢,就是我们在Spring Boot项目当中如何来使用D-Rose,也就是Spring Boot如何整合D-Rose。

好,这是关于我们D-Rose这一块啊,我们会介绍这么多的内容。

整个呢,我们相当于是系统的来学习一下这个技术。

那么学习完之后呢,就可以使用它来解决我们这个问题了。

也就是基于我们这个规则引擎D-Rose这个技术来帮我们。

我们计算什么呢?根据规则来计算出来订单的价格。

好,那么这是关于咱们这个D-Rose啊,要涉及到的内容,就是这么多。

一会儿呢,我们就会展开啊,然后呢,按照我们这个讲义的内容,然后呢,来展开讲解。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，进行的结构化中文技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“规则引擎 DROOLS”的技术讲解，旨在通过一个“在线信用卡申请”的业务场景，引出并介绍规则引擎的核心概念和应用。课程内容分为两个主要部分：

*   **第一部分（引出）**：通过一个信用卡申请的复杂业务规则（如学历、收入、房产、车辆、现有信用卡数量等）来说明，使用传统的 `if-else` 分支判断会非常繁琐且难以维护。这为引入规则引擎（Drools）提供了动机。
*   **第二部分（实现）**：课程展示了如何使用 DROOLS 来解决上述问题。首先，它演示了如何封装业务数据（如 `AddressRule` 类），然后通过 DROOLS 的规则语言（DRL）来定义和管理这些复杂的业务规则，从而实现业务逻辑的解耦和可维护性。

课程内容以 Markdown 文档的形式在 Typora 编辑器中展示，并辅以代码示例和业务规则表，旨在为学习者提供清晰、结构化的学习路径。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取实际的视频时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：**1. 问题引出**
    *   展示“XX银行信用卡申请表”的界面。
    *   介绍用户需要填写的个人信息（姓名、性别、年龄、学历、电话、月收入、邮寄地址、是否有房、是否有车、现有信用卡数量）。
    *   引出核心问题：如何对这些复杂的业务规则进行有效管理？传统的 `if-else` 代码会非常臃肿。

*   **00:30 - 01:00**：**2. 规则引擎概述**
    *   简要介绍规则引擎（Drools）的概念：它是一种允许将业务规则与应用程序代码分离的工具，使业务规则可以由业务专家（而非程序员）独立维护和修改。

*   **01:00 - 02:00**：**3. Drools入门案例**
    *   通过信用卡申请的案例，演示如何使用 DROOLS 来定义规则。
    *   展示业务规则表，例如：
        *   规则1：如果申请人有房或月收入>2000，则额度为15000。
        *   规则2：如果申请人没房，月收入在1000-2000之间，则额度为6000。
        *   规则3：如果申请人没房，月收入<1000，则额度为3000。
        *   规则4：如果申请人没房没车，月收入在1000-2000之间，则额度为5000。
        *   规则5：如果申请人没房没车，月收入在1000-2000之间，则额度为8000。
    *   强调规则引擎的优势：规则可以独立于代码进行修改和测试。

*   **02:00 - 03:00**：**4. Drools基础语法**
    *   介绍 DRL（Drools Rule Language）的基本语法结构。
    *   重点讲解规则的组成部分：`rule`、`when`（条件）、`then`（结果）。
    *   举例说明如何用 DRL 语言编写上述信用卡申请规则。

*   **03:00 - 04:00**：**5. 规则属性**
    *   讲解如何在规则中使用变量和属性。
    *   介绍如何将业务对象（如 `User`）放入规则引擎的“工作内存”中，以便规则可以访问其属性。

*   **04:00 - 05:00**：**6. Spring Boot整合Drools**
    *   介绍如何在 Spring Boot 项目中集成 DROOLS。
    *   展示如何在 Spring Boot 中配置 Drools 并运行规则。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   **信用卡申请表**：一个包含“基本信息”和“其他信息”的表单截图，用于引出业务场景。
    *   **业务规则表**：一个表格，列出了5条信用卡申请的规则，包括规则编号、名称和描述。
    *   **规则引擎 DROOLS 的目录结构**：一个大纲，列出了课程的主要章节，如“问题引出”、“规则引擎概述”、“Drools入门案例”等。

*   **代码**：
    *   **Java 实体类 `AddressRule`**：
        ```java
        package com.itehima.pinda.entity;
        public class AddressRule {
            /**
             * 货品总重量
             */
            private double totalweight;
            // ... 其他属性和方法
        }
        ```
        用于封装订单价格计算所需的参数。

    *   **Java 工具类 `BaiduMapUtils`**：
        ```java
        package com.itehima.pinda.common.utils;
        import com.alibaba.fastjson.JSON;
        import com.alibaba.fastjson.JSONArray;
        import com.alibaba.fastjson.JSONObject;
        import com.google.common.collect.ImmutableMap;
        import com.google.common.collect.Maps;
        import org.apache.commons.lang3.StringUtils;
        import java.io.BufferedReader;
        import java.io.IOException;
        import java.io.InputStream;
        import java.math.BigDecimal;
        import java.net.URL;
        import java.net.URLConnection;
        import java.text.DecimalFormat;
        import java.util.Map;
        import java.util.Map.Entry;
        import java.util.regex.Pattern;
        public class BaiduMapUtils {
            static String AK = "UEBQHc3KZ5Lrso2Cq2sOAslesdlV1zm"; // 百度地图密钥
            // ... 其他方法，如 getCoordinate()
        }
        ```
        用于封装百度地图 API 的调用，获取地理坐标。

    *   **Java 方法 `getCoordinate`**：
        ```java
        public static String getCoordinate(String address) {
            if (address == null || "".equals(address)) {
                return null;
            }
            String url = "http://api.map.baidu.com/geocoding/v3/?output=json&ak=" + AK + "&callback=showLocation&address=" + address;
            String json = loadJSON(url);
            if (json == null || "".equals(json)) {
                return null;
            }
            Map map = JSON.parseObject(json, Map.class);
            if ("0".equals(map.getOrDefault("status", "").toString()) {
                Map childMap = (Map) map.get("result");
                Map posMap = (Map) childMap.get("location");
                double lng = Double.parseDouble(posMap.getOrDefault("lng", "0").toString());
                double lat = Double.parseDouble(posMap.getOrDefault("lat", "0").toString());
                DecimalFormat df = new DecimalFormat("#.####");
                String lngStr = df.format(lng);
                String latStr = df.format(lat);
                return lngStr + "," + latStr;
            }
            return null;
        }
        ```
        用于调用百度地图 API 获取地址的经纬度坐标。

    *   **伪代码 `checkUser`**：
        ```java
        public boolean checkUser(User user) {
            // 规则1：如果申请人既没房也没车，同时学历为大专以下，并且月薪少于5000，那么不通过
            if (user.getHouse() == null
                && user.getCar() == null
                && user.getEducation().equals("大专以下")
                && user.getSalary() < 5000) {
                return false;
            }
            // 规则2：如果申请人既没房也没车，同时学历为大专或本科，并且月薪少于3000，那么不通过
            else if (user.getHouse() == null
                && user.getCar() == null
                && user.getEducation().equals("大专或本科")
                && user.getSalary() < 3000) {
                return false;
            }
            // 规则3：如果申请人既没房也没车，同时学历为本科以上，并且月薪少于2000，同时之前没有信用卡的，那么不通过
            else if (user.getHouse() == null
                && user.getCar() == null
                && user.getEducation().equals("本科以上")
                && user.getSalary() < 2000
                && user.getCardCount() == 0) {
                return false;
            }
            // ... 其他规则
            return true;
        }
        ```
        用于演示传统的 `if-else` 代码实现方式，以引出规则引擎的必要性。

---

### 4) 关键场景与演示描述

*   **场景一：业务场景引出**
    *   **描述**：课程开始时，展示了一个“XX银行信用卡申请表”的截图，详细列出了用户需要填写的个人信息（姓名、性别、年龄、学历、电话、月收入、邮寄地址
