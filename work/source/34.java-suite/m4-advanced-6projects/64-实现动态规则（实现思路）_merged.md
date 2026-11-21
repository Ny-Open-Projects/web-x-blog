# 64-实现动态规则（实现思路） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们是已经实现了我们根据规则计算订单价格,对吧

那接下来呢,我们来看下一个小节呢,就是实现动态规则

这个是怎么回事呢

咱们虽然说我们前面这个规则啊

根据规则计算订单价格呢,虽然已经实现了

但是呢,还有一个问题需要解决

就是什么呢

如果说我们这个规则呢,发生变动了

那么如何在不重启服务的情况下

来这个进行规则的切换呢

比如说我们现在这个啊

我们这个规则呢,是写在这个规则文件里面了,对吧

那么如果说其中有一些规则呢,发生变动了

咱们是不是需要去修改这个规则文件,对吧

那么改完之后呢,它其实不会生效的

那个时候我们必须重启服务,对吧

那么重启服务之后,它才能生效

那现在呢,我们希望能做到什么呢

就是说在不重启服务的情况下

就可以进行规则的切换

那么这就需要我们去实现什么呢

动态规则

具体这个实现的思路呢,我们先来说一下

然后一会儿我们再看具体怎么操作,对吧

那么实现的思路其实是这样的

就是将我们这个规则文件里面

编写的这些规则,这些内容

把它存储到什么呢,存储到数据库中

也就是说把它存储起来

然后呢,我们这个D-Rose相关对象的创建啊

比如说我们这个KIE Container啊

什么KIE这个File System啊等等

那一堆对象,对吧

这些对象呢

全都是基于我们数据库中

那么编写的这些规则

存储的这些规则来创建的

然后呢,我们再来提供一个HTTP的访问接口

然后呢,当我们这个规则发生变化的时候呢

我们就可以请求一下这个接口

然后呢

让它重新来这个

从数据库里面来加代我们这个规则

然后呢,重新来创建这一堆对象

其中最重要的呢,就是这个KIE Container,对吧

那么这就是我们实现的这个思路

大概就是分成这么三步,对吧

第一步呢,是什么呢

就是把我们规则的内容保存到数据库中

然后第二步呢,就是数据库

就是我们D-Rose当中这些对象的创建

那么都是从我们这个数据库中读出来的这个规则

基于这个规则来创建

然后第三步呢

就是我们再来提供一个HTTP访问接口,对吧

那么规则发生变化的时候呢

我们就请求一下这个接口

这个时候呢

一触发,它就会重新去加代我们数据库中的规则

最终呢

把这些对象重新再来创建一遍

这样呢

我们这个规则就切换过来了

这是我们实现的一个思路

先来明确一下

然后一会儿呢

我们就需要实际来操作

那么来通过编码的方式来实现这个过程

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频课程讲解了如何在 Spring Boot 项目中集成 Drools 规则引擎，并实现一个**动态的、可热加载的订单运费计算系统**。核心内容包括：
*   **静态规则实现**：首先展示如何在 `orderAmountCalc.drl` 文件中编写基础的运费计算规则，根据订单重量和距离分段计费。
*   **动态规则实现**：重点讲解如何将规则从静态文件迁移到数据库中，实现规则的热更新。具体步骤包括：
    1.  在 `pdm_oms` 数据库中创建 `rule` 表来存储规则内容。
    2.  通过 HTTP 接口，当规则发生变化时，动态加载数据库中的新规则并重新创建 `KieContainer` 对象，从而无需重启服务即可生效。
*   **技术栈**：Java, Spring Boot, Drools, MySQL。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：课程开场，展示项目结构和 `OrderController.java` 中的 `@PostMapping` 方法，用于接收订单并调用服务层计算价格。
*   **00:05 - 00:15**：展示 `orderAmountCalc.drl` 文件，讲解第一个规则：当订单重量小于等于 1 千克时，运费固定为 20 元。
*   **00:15 - 00:25**：讲解第二个规则：当订单重量大于 1 千克且距离在 200 公里以内时，运费为首重 20 元，续重每 1 千克 6 元。
*   **00:25 - 00:35**：讲解第三个规则：当订单重量大于 1 千克且距离在 200-500 公里之间时，运费为首重 20 元，续重每 1 千克 9 元。
*   **00:35 - 00:45**：讲解第四个规则：当订单重量大于 1 千克且距离超过 500 公里时，运费为首重 20 元，续重每 1 千克 15 元。
*   **00:45 - 00:55**：切换到 PPT 页面，讲解“实现动态规则”的思路，即把规则文件内容存入数据库。
*   **00:55 - 01:05**：在 PPT 中展示创建 `rule` 表的 SQL 语句，用于存储规则内容。
*   **01:05 - 01:15**：回到代码，讲解如何通过 HTTP 接口触发规则的热加载，动态创建 `KieContainer`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容：

*   **章节标题**：8.1 实现思路，8.2 实现步骤。
*   **8.1 实现思路**：
    1.  将规则文件的内容存储在数据库中。
    2.  Drools 对象（如 KieContainer）的创建基于数据库中存储的规则。
    3.  提供 HTTP 接口，当规则发生变化时，通过 HTTP 调用接口，重新加载数据库中的规则，重新创建 KieContainer。
*   **8.2 实现步骤**：
    1.  在 `pdm_oms` 数据库中创建 `rule` 表。
    2.  SQL 语句：`CREATE TABLE rule (id bigint(20) NOT NULL AUTO_INCREMENT, content text ... PRIMARY KEY (id), UNIQUE INDEX UK_... (rule_key), UNIQUE INDEX UK_... (version))`

#### 代码内容：

*   **`OrderController.java`**：
    ```java
    @PostMapping("save")
    public OrderDTO save(@RequestBody OrderDTO orderDTO, HttpServletResponse res) {
        // ... 省略部分代码 ...
        orderService.saveOrder(order);
        OrderDTO result = new OrderDTO();
        BeanUtils.copyProperties(order, result);
        return result;
    }
    ```

*   **`orderAmountCalc.drl`**：
    ```drl
    rule "1千克以内20元"
    activation-group "mygroup"
    salience 10
    when
        addressRule : AddressRule(totalWeight != null && totalWeight <= 1.00)
    then
        checkResult.setPostCodeResult(true);
        checkResult.setResult("20");
        System.out.println("1千克以内20元");
    end

    rule "1千克以上，订单距离在200~500公里的，首重1千克，首重价格20元，续重每1千克资费为9元"
    activation-group "mygroup"
    salience 8
    when
        addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance > 200.00 && distance <= 500.00)
    then
        addressRule.setFirstFee(20.00);
        addressRule.setFirstWeight(1.00);
        addressRule.setContinuedFee(9.00);
        DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
        String orderAmount = droolsRulesService.calcFee(addressRule);
        checkResult.setPostCodeResult(true);
        checkResult.setResult(orderAmount);
        System.out.println("1千克以上，订单距离在200~500公里的，首重1千克，首重价格20元，续重每1千克资费为9元");
    end

    rule "1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元"
    activation-group "mygroup"
    salience 7
    when
        addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance > 500.00)
    then
        addressRule.setFirstFee(20.00);
        addressRule.setFirstWeight(1.00);
        addressRule.setContinuedFee(15.00);
        DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
        String orderAmount = droolsRulesService.calcFee(addressRule);
        checkResult.setPostCodeResult(true);
        checkResult.setResult(orderAmount);
        System.out.println("1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元");
    end
    ```

---

### 4) 关键场景与演示描述

*   **场景一：静态规则演示** (00:05-00:45)
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `orderAmountCalc.drl` 文件，逐条讲解并高亮显示了四个运费计算规则。
    *   **演示**：通过鼠标滚轮和光标移动，逐行展示规则的条件（`when`）和结果（`then`），并解释了 `salience`（优先级）的作用。例如，第一个规则的 `salience` 为 10，意味着它在匹配时优先于其他规则。

*   **场景二：动态规则实现思路** (00:45-01:05)
    *   **描述**：讲师切换到 PPT 页面，讲解如何实现规则的动态更新。
    *   **演示**：在 PPT 上用鼠标指针高亮“实现动态规则”标题，并逐条讲解实现思路：将规则存入数据库、创建 KieContainer 基于数据库规则、通过 HTTP 接口触发热加载。

*   **场景三：数据库表结构演示** (00:55-01:05)
    *   **描述**：在 PPT 上展示创建 `rule` 表的 SQL 语句。
    *   **演示**：鼠标指针在 SQL 语句上移动，高亮 `id`, `content`, `rule_key`, `version` 等关键字段，解释它们的作用。

*   **场景四：代码热加载逻辑** (01:05-01:15)
    *   **描述**：讲师回到代码编辑器，讲解如何通过 HTTP 接口触发规则的热加载。
    *   **演示**：鼠标在 `DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();` 这行代码上停留，说明这是在服务层创建 Drools 服务对象，用于执行规则。同时，高亮 `checkResult.setPostCodeResult(true);` 用于设置结果状态。
