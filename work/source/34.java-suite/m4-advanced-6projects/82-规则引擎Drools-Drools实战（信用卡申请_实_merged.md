# 82-规则引擎Drools-Drools实战（信用卡申请_实 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

继续咱们这个信用卡申请实战

刚才呢我们是把规则文件已经编辑好了

再往下呢就需要来创建一个Ruler Service了

在这个Service里边呢

可以直接来注入一个KE Base

通过这个Base呢

我们就可以来创建一个Session

有了Session呢

我们就可以来跟我们的规则引擎进行交互了

比如调用Insert

把我们对应的这个Fag的对象

插入到工作内存里面去

然后呢调用相应的方法来触发规则等等

这个Ruler Service呢也比较简单

我就直接来考了

先把这个包创建一下吧

创建这么一个Service包

然后我们在这来考一下这个

被名叫做Ruler Service

这里边呢我们把这一块

整个考吧

整个这个

这段都考过来

然后把这块覆盖一下就行了

这块呢基本上没什么好解释的

跟我们第一个

实战案例呢基本上是一个套路

咱们在这边呢

是设计了这么一个方法

叫做Credit Card Apply

你看字面翻译过来就是什么呢

信用卡申请

然后呢传进来的是咱们这个实体对象

对吧

然后直接扔到工作内存里面去

然后呢进行规则的触发

最终呢把这个对象还返回回来

因为这里边呢

经过我们规则引擎内部处理之后呢

现在这个对象里边呢

应该就产生结果了

主要是什么呢

主要就是设置的我们这两个值

对吧

可能把它设置成False了

那就表示审额不通过了

也有可能设置了这个额的结果了

那就说明审额通过

并且额度也确定下来了

所以这是咱们这个Service要做的事

把这个对象重新给我们返回

再往下呢

就需要来创建一个Controller了

在我们的Controller里边

来调用我们的Service

所以呢我们接下来

把这个Controller也来创建一下

先是把这个包呢创建出来

然后把这个Ruler Controller

来创建一下

这里面这代码呢

我就直接烤了

我们课上呢就不再去手敲了

一个Rest Controller加一个注解

还有Request Mapping对吧

然后呢这个设置是这个

杠如了通过这个路径呢

再加上这个路径

就可以访问到我们这个Controller的方法了

别忘了注入这个Service对吧

然后在这里边呢

我们就需要来接收一个参数啊

这个参数呢就是这个实体类

需要注意的是什么呢

有这样有个Request Body

这说明什么呢

前端页面是不是给我们提交的数据格式

应该是JSON的

加这么一个注解呢

这会由我们Spring MVC框架去解析JSON

并且呢把它对应的封装成我们这个实体对象

然后呢这个实体对象呢

我们就可以直接给到Service里面去

最终呢给到我们的规则引擎内部去进行规则匹配

对吧

好

这个对象返回来之后呢

我们直接给它返回到页面上

返回到页面

然后在页面上呢

再进行处理

好

这是关于我们的Controller

也就已经编写好了

再往下呢

就是需要有我们的这个静态资源文件

对吧

以及这个什么启动类

对吧

启动类呢

我先创建一下

启动类在Dirose这层目录里面来创建

就叫Dirose Application

然后里边只有一个MainFarm码

对吧

好

这个MainFarm来启动我们Spring Boot的工程

这个呢就不再多说了

最后呢

还有一步啊

就是来导入我们相关的这个资源文件

在我们今天提供的资料里边啊

我们的实战就是这个申请信用卡的

这是不是有个Static目录啊

这里边呢

有一个页面以及用到的两个JS文件

咱们把整个Static这个目录拷头复制

复制到哪呢

复制到我们这个Resources下边

这个是存放我们静态资源文件的

直接把它粘贴在这个位置就可以了

OK

这样就过来了

大概读一下

我们考进来的这个页面啊

这个页面的是这样的

首先呢

是一个表格

对吧

一个表格

然后呢

表格里边呢

有一些输入框

而这些输入框呢

我们都已经设计好了

并且的通过V-Model

是通过我们VUE的数据绑定的吧

都绑定到了这么一个JS对象上

它其实本身是一个本质上是一个JSON对吧

一个JSON对象

这些呢

其实都是对应的是咱们这个实体类里边的一些属性啊

然后这个是学历设计成了是一个下拉框

然后呢

还有月收入对吧

就是一个普通的输入框

还有新款的数量也是输入框

是否有房用的是一个下拉框

还有是否有车也是一个下拉框

还有个按钮对吧

一点击了

它就会触发这么一个方法

这个方法咱们一会再看啊

在下面定义的

还有呢

就是我们的结果信息

这个结果信息呢

它是不是通过我们这种差值表达式啊

从这个地方来取值

而这个地方呢

默认是不是给了一个出入值

给了一个空的字符串对吧

好

然后再往下呢

这就是我们定义的这个方法credit card apply

这个方法

然后在这个方法这儿呢

我们可以看到

首先呢

我们是不是发送了一个阿达克斯请求

请求咱们这个controller

就是对应我们刚才编写的controller的那个方法

并且把我们这个JSON对象是不是给传过去

然后呢

回来之后呢

在这个地方是不是来解析结果

解析什么呢

解析我们

这个chat

这个result

它如果等于true的话呢

就是审核通过

这个时候呢

我们把这个信息呢

显示在这儿的吧

最终呢

这个值呢

会显示在我们这个地方

如果审核失败的话呢

也是设置只不过就是变成抱歉对吧

就是这个审核不通过啊

这是关于咱们这个页面上

页面呢

我们就先说到这儿啊

然后接下来呢

咱们就把这个工程的来启动一下

因为它是一个Spring Boot的工程啊

所以我们直接使用咱们这个什么呢

这个什么呢

启动类来启动一下

这些启动类来启动

然后呢

我们直接来执行

看一下启动啊

有没有报错

看一下控制台是没有报错的

说明启动成功了

端口号呢

还是8080啊

8080咱们现在呢

直接来访问什么呢

直接来访问我们刚才考进来的这个页面就可以了

然后我们可以打开一个浏览器

在这儿来输入一下HTTP

然后localhost呢

端口呢

8080对吧

ruler

咱们那个页面叫什么呢

这个页面我来考一下啊

就是这个叫creditcardapply.html

好

走

我们看啊

它这是报了一个404对吧

它没有找到这个页面

在这儿多了一个ruler

这样我们可以看到啊

这个页面就已经展示出来了对吧

已经展示出来了

那接下来呢

我们来发送一个请求

随便啊

直接先点申请

你看信用卡申请成功

信用卡的额度呢是15000

为什么是15000呢

是因为我们这儿是不是选的是有房有车

咱们来对比一下我们的规则

对比着我们的规则文件来看

你看它是不是有房有车

月收入就不用管了

对吧

因为它俩之间是或者的关系

只要有房有车啊

信用卡的额度呢就是15000

然后呢我们可以这样啊

有房没车对吧

然后看这种情况是5000

它卡的是5000这一档

5000这一档

那就说明是最后这个

那就是有房没车或者是没车有房

然后月收入是一万以下对吧

这种情况

你看是不是车跟房是不是只有一项

然后呢

月收入我们没填啊

月收入没有填的话

它其实默认是

默认是这个零对不对

因为我们没轨默认值

然后在这的话呢

我也可以输入一下

比如说我来一个1000

其实效果是一样的

效果是一样的啊

应该还是5000

然后呢

我再加个零的吧

一万

信用卡额度是不是变成8000

这说明它卡的是8000

8000这一档

就是车跟房是不是只有一项

月收入呢是一万到两万之间

对吧

卡的是这一档

那这个时候呢

它的额度就是8000

OK

这些呢

我们都可以测一下

你看因为这一项呢

它其实没有涉及到我们的学历啊

所以说你这个学历改不改

其实都没有什么关系

但是呢

我如果把这个没房没车

对吧

还是学历还低

这个时候呢

它卡的就是6000这一档

如果我把这个月收入再去点

你看它是不是就审核不通过了

但是这呢

这各种各样的这些组合方式非常多

我们就不可能把每一样

都测

每一样都都去试验一遍啊

主要还是去检查什么呢

检查我们的规则

看我们的规则设计是否合理

以及呢

所有的情况是否都已经被覆盖全了

好

这个呢是关于咱们这个信用卡申请啊

这个实战案例呢

我们就说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析。

---

### 1) 视频摘要

本视频课程为一个关于 **Drools 规则引擎在 Spring Boot 项目中实战应用** 的教学视频。课程通过一个“信用卡申请审批”的完整案例，系统地演示了如何从零开始搭建项目、编写规则、集成到 Web 应用并进行前端交互。主要内容包括：创建 Spring Boot 项目、配置 Drools、编写 Java 服务层（`RuleService`）调用规则引擎、编写 RESTful 控制器（`RuleController`）暴露接口、创建前端页面（`creditCardApply.html`）进行数据输入、编写 DRL 规则文件（`creditCardApply.drl`）定义审批逻辑、以及最后启动应用并测试。整个过程强调了 DRL 规则文件的编写和与 Java 代码的集成。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程介绍与项目背景。
*   **00:00:05 - 00:00:15**：**第六步：创建 RuleService**。在 IntelliJ IDEA 中创建 `RuleService.java` 文件，编写服务层代码，用于调用 Drools 引擎。
*   **00:00:15 - 00:00:30**：**第七步：创建 RuleController**。在 `controller` 包下创建 `RuleController.java`，编写 RESTful 接口，用于接收前端请求并调用 `RuleService`。
*   **00:00:30 - 00:00:45**：**第八步：创建启动类 DroolsApplication**。在 `main` 包下创建 `DroolsApplication.java`，编写 Spring Boot 启动类。
*   **00:00:45 - 00:01:00**：**第九步：导入静态资源文件**。将前端页面 `creditCardApply.html` 和相关资源文件放入 `src/main/resources/static` 目录下。
*   **00:01:00 - 00:01:15**：**第九步：保险产品准入规则**。介绍后续将要实现的另一个规则案例。
*   **00:01:15 - 00:01:30**：**第九步：保险产品准入规则**。讲解 DRL 规则文件的格式和扩展名（`.drl` 和 `.xls`）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程大纲：清晰列出了从“创建空间、项目”到“在项目中使用部署的规则”的各个步骤。
    *   项目结构：展示了 `src/main/java` 和 `src/main/resources` 目录下的标准 Spring Boot 项目结构。
    *   规则文件说明：说明了 DRL 规则文件的格式和可支持的其他文件格式（如 `.xls`）。

*   **代码关键内容**：

    *   **`RuleService.java`** (服务层)
        ```java
        package com.ithema.drools.service;
        import org.kie.api.runtime.KieSession;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.stereotype.Service;

        @Service
        public class RuleService {
            @Autowired
            private KieBase kieBase;

            // 调用Drools规则引擎实现信用卡申请
            public CreditCardApplyInfo creditCardApply(CreditCardApplyInfo creditCardApplyInfo) {
                KieSession session = kieBase.newKieSession();
                session.insert(creditCardApplyInfo);
                session.fireAllRules();
                session.dispose();
                return creditCardApplyInfo;
            }
        }
        ```

    *   **`RuleController.java`** (控制器层)
        ```java
        package com.ithema.drools.controller;
        import org.springframework.web.bind.annotation.*;

        @RestController
        @RequestMapping("/rule")
        public class RuleController {
            @Autowired
            private RuleService ruleService;

            @PostMapping("/creditCardApply")
            public CreditCardApplyInfo creditCardApply(@RequestBody CreditCardApplyInfo creditCardApplyInfo) {
                CreditCardApplyInfo result = ruleService.creditCardApply(creditCardApplyInfo);
                return result;
            }
        }
        ```

    *   **`DroolsApplication.java`** (启动类)
        ```java
        package com.ithema.drools;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;

        @SpringBootApplication
        public class DroolsApplication {
            public static void main(String[] args) {
                SpringApplication.run(DroolsApplication.class);
            }
        }
        ```

    *   **`creditCardApply.html`** (前端页面)
        ```html
        <h3 align="center">XX银行信用卡申请</h3>
        <table align="center" width="50%" border="0">
            <tr>
                <td>姓名</td>
                <td><input type="text" v-model="creditCardApplyInfo.name"></td>
            </tr>
            <tr>
                <td>性别</td>
                <td><input type="text" v-model="creditCardApplyInfo.sex"></td>
            </tr>
            <tr>
                <td>年龄</td>
                <td><input type="text" v-model="creditCardApplyInfo.age"></td>
            </tr>
            <tr>
                <td>手机号</td>
                <td><input type="text" v-model="creditCardApplyInfo.phone"></td>
            </tr>
            <tr>
                <td>是否有车</td>
                <td>
                    <select v-model="creditCardApplyInfo.hasCar">
                        <option value="true">是</option>
                        <option value="false">否</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td colspan="4" align="center">
                    <br>
                    <input type="button" value="申请" @click="creditCardApply()">
                </td>
            </tr>
            <tr>
                <td colspan="4" align="center">
                    {{applyResultMessage}}
                </td>
            </tr>
        </table>
        ```

    *   **`creditCardApply.drl`** (DRL 规则文件)
        ```drl
        rule "如果申请人有房没车或者没房有车，月收入在10000以下，那么发放的信用卡额度为5000"
            salience 10
            no-loop true
            activation-group "quota_group"
            when
                $c:CreditCardApplyInfo(checkResult == true &&
                    (hasHouse == true && hasCar == false) ||
                    (hasHouse == false && hasCar == true)) &&
                    monthlyIncome < 10000
            then
                $c.setQuota(5000);
        end

        rule "如果申请人有房没车或者没房有车，月收入在10000~20000之间，那么发放的信用卡额度为8000"
            salience 10
            no-loop true
            activation-group "quota_group"
            when
                $c:CreditCardApplyInfo(checkResult == true &&
                    (hasHouse == true && hasCar == false) ||
                    (hasHouse == false && hasCar == true)) &&
                    monthlyIncome >= 10000 && monthlyIncome <= 20000
            then
                $c.setQuota(8000);
        end
        ```

    *   **前端 JavaScript 代码** (用于调用后端接口)
        ```javascript
        creditCardApplyInfo: {
            education: "本科",
            hasHouse: true,
            hasCar: true,
            applyResultMessage: ''
        },
        methods: {
            creditCardApply() {
                axios.post('/rule/creditCardApply', this.creditCardApplyInfo).then(res => {
                    if (res.data.checkResult) {
                        this.applyResultMessage = "恭喜您信用卡申请成功，信用卡额度为：" + res.data.quota;
                    } else {
                        this.applyResultMessage = "抱歉，您提交的信息审核未通过，您不能申请信用卡！";
                    }
                });
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建服务层 `RuleService`**
    *   讲师在 IntelliJ IDEA 中创建 `RuleService.java` 文件。
    *   通过 `@Autowired` 注解注入 `KieBase` 实例。
    *   编写 `creditCardApply` 方法，该方法创建 `KieSession`，插入事实对象，触发所有规则，最后释放会话。

*   **场景二：创建控制器层 `RuleController`**
    *   讲师在 `controller` 包下创建 `RuleController.java`。
    *   使用 `@RestController` 和 `@RequestMapping` 注解定义 RESTful 接口。
    *   `@PostMapping` 注解定义了 `/creditCardApply` 接口，接收前端
