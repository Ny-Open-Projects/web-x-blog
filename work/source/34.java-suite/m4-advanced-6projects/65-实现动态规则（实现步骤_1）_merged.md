# 65-实现动态规则（实现步骤_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看一下我们实现动态规则

刚才呢我们是说了一下实现的思路对吧

那接下来呢我们就需要来实

具体来实现了

刚才提到我们这个实现的思路第一步呢

就是要把这个规则的内容对吧

规则文件的内容把它保存到数据库

那这就需要一张表来存储对吧

所以接下来呢我们实现步骤第一步呢

就是来创建一张表

这个表名呢就叫Ruler

其实这个名字叫什么无所谓啊

那么我们就叫这个名字

然后呢这个表它的作用就是干什么呢

存储我们规则的内容

这个地方呢我们已经提供好了这么一个键表语句

大家直接执行一下就可以了

其实呢在我们现在这个数据库里边呢

也已经创建过了

咱们直接打开

来简单看一下就可以了

好然后呢连到我们数据库上面来

在我们这个pd-oms对吧

在这个数据库里面有这么一张表就叫做Ruler

然后呢我们双击打开它

然后呢我们双击打开它

来看一下有这么几个字段的吧

一个是ID这是主件

然后content这个是什么呢

规则的内容

注意我们这个字段呢

你就不要用VHR了

因为这个字段明显长度是不够的

我们使用的是text的文本这种类型对吧

那么因为它要存储的这个内容

是非常大的

比如说我们整个文件这些内容

你看我选中的这些内容都需要存储在这个字段上

所以说呢这个地方一定要注意啊

是一个text的这种类型

好

我们现在就来看看

这个是存储规则内容的字段

然后还有一个是createTime对吧

这是创建时间

还有是modify

last modify time

就是最后的修改时间

还有一个ruler key

这其实就是一个标识对吧

然后还有一个version就是版本号

这是我们这个表

最重要的呢就是这个content的这个字段

那么大家呢可以直接来复制这个circle对吧

然后呢在数据库里面自己来把这个表创建出来就可以了

好

这是第一步

然后接下来第二步的话呢

我们是不是就需要来提供了这个表呢

我们就需要来提供这个表所对应的实体类对吧

因为我们最终要操作这个表

那么我们这个地方呢就需要来提供一个实体类

这个实体类呢

咱们就放在entity下边

名字呢就叫ruler

然后呢

这个类里面的属性呢

跟咱们表里面的字段呢都是一一对应的

所以接下来呢我们把这个实体类来创建一下

这里有点乱啊

咱们把这个都给关上

然后找到咱们这个entity

对吧

然后在这个包下边呢

来创建我们这个实体

就叫ruler

这里边代码的内容呢

我就不再手敲了

咱们直接复制过来

来大概看一下就可以了

这是ruler

对吧

然后呢它对应的这个table name

对吧

映射的表呢就是刚才我们看到的ruler这个表

然后呢属性呢是不是有id

ruler key content version

还有last modified time

还有curry time

然后呢跟我们刚才看到的表里面的字段呢

都是一一对应的关系

那么这个实体类呢

也就一一对应的关系

这个已经搞定了

然后呢我们是不是要通过mybattieplus的方式呢

来操作这个表

所以说呢我们需要来提供一个什么呢

mapper接口对吧

还mapper接口

所以呢我们在这个mapper包下边来创建一个叫做ruler mapper

这些呢都是比较简单的

在这个mapper下边

注意它是一个接口interface

好

然后呢把这个代码呢

咱们直接复制过来就可以了

好

大家看它是不是只要

继承我们这个mybattieplus

给我们提供的这么一个叫做base mapper

这么一个复接口就可以了

对吧

然后呢指定这个要操作的实体呢

就是这个ruler实体

然后呢再加这么一个mapper注解

标识一下就可以了

其实我们对应的这个映射文件啊

这个地方映射文件呢

可以填也可以不填

可以有也可以没有

因为我们现在呢要调用的这个增伤改查方法呢

都是通用的增伤改查方法

对吧

也就是说我们这个mybattieplus框架呢

呃

都已经提供好了

如果说我们有自己特有的方法

对吧

那么我可能自己需要编写一个sql

那这个时候呢

你可以提供这个映射文件啊

这个插盘文件

那么现在我们这儿呢不需要

那我就不提供了啊

呃

这是我们前三步还是比较简单的

对吧

哎

第一步呢是创建表

第二步呢创建实体类

第三步呢是我们这个mybattieplus接口

对吧

提供好

然后一会儿呢

我们需要来编写这么一个ruler service

在这个service里边呢

就需要来重新加的

在我们数据库里面的规则

对吧

也就是在读取数据库

然后呢

把我们kai container等等

这一堆对象给它创建出来

好

那么这个实现步骤呢

我们暂时先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在订单中心服务中实现**动态规则引擎**。核心目标是解决在不重启服务的情况下，如何应对业务规则（如运费计算规则）的变更。讲师通过分步演示，展示了如何将规则文件存储在数据库中，并通过HTTP接口动态加载和更新规则，从而实现规则的热更新。演示内容包括数据库表结构设计、Java实体类开发、MyBatis Mapper接口定义，以及最终用于热加载规则的 `ReloadDroolsRulesService` 服务的初步代码框架。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 引入问题：当前系统已能根据规则计算订单价格，但如何在不重启服务的情况下实现规则的动态切换？
*   **00:05 - 00:15**: 解决方案概述：将规则文件存储在数据库中，通过HTTP接口动态加载。
*   **00:15 - 00:25**: 第一步：在 `pd-oms` 数据库中创建 `rule` 表，用于存储规则内容。
*   **00:25 - 00:35**: 第二步：创建 `Rule` 实体类，与数据库表 `rule` 对应。
*   **00:35 - 00:45**: 第三步：创建 `RuleMapper` 接口，用于操作数据库。
*   **00:45 - 00:55**: 第四步：创建 `ReloadDroolsRulesService` 服务，用于重新加载数据库中的规则。
*   **00:55 - 01:05**: 展示了 `Rule` 实体类的完整代码结构。
*   **01:05 - 01:15**: 展示了 `RuleMapper` 接口的代码框架。
*   **01:15 - 01:25**: 展示了 `ReloadDroolsRulesService` 服务的初步代码框架。
*   **01:25 - 01:35**: 展示了 `orderAmountCalc.drl` 规则文件的示例内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**：`8.1 实现思路` 和 `8.2 实现步骤`。
*   **核心思路**：
    1.  将规则文件的内容存储在数据库中。
    2.  Drools相关对象（如 `KieContainer`）的创建都基于数据库中存储的规则来创建。
    3.  提供HTTP访问接口，当规则发生变化时调用此接口重新加载数据库中的规则，重新创建 `KieContainer` 等对象。

#### 代码内容

*   **数据库表结构 (`rule` 表)**：
    ```sql
    CREATE TABLE rule (
        id bigint(20) NOT NULL AUTO_INCREMENT,
        content text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        create_time varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        last_modify_time varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
        rule_key varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        version varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        PRIMARY KEY (`id`) USING BTREE,
        UNIQUE INDEX UK_... USING BTREE,
        UNIQUE INDEX UK_... USING BTREE,
        UNIQUE INDEX UK_... USING BTREE
    ) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;
    ```

*   **Java 实体类 `Rule`**：
    ```java
    @ApiModel
    public class Rule implements Serializable {
        @TableId(value = "id", type = IdType.INPUT)
        private Long id;
        private String ruleKey;
        private String content;
        private String version;
        private String lastModifyTime;
        private String createTime;
    }
    ```

*   **MyBatis Mapper 接口 `RuleMapper`**：
    ```java
    @Mapper
    public interface RuleMapper extends BaseMapper<Rule> {
    }
    ```

*   **服务接口 `ReloadDroolsRulesService`**：
    ```java
    package com.iteima.pinda.service;
    import com.iteima.pinda.entity.Address;
    import com.iteima.pinda.entity.Rule;
    import com.iteima.pinda.mapper.RuleMapper;
    import org.kie.api.KieServices;
    import org.kie.api.builder.KieFileSystem;
    import org.kie.api.builder.KieRepository;
    ```

*   **Drools 规则文件 (`orderAmountCalc.drl`)**：
    ```drl
    rule "1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元"
    activation-group "mygroup"
    salience 7
    when
        addressRule : AddressRule(totalWeight != null && totalWeight > 1.0 && distance > 500.00)
    then
        addressRule.setFirstFee(20.00);
        addressRule.setFirstWeight(1.00);
        addressRule.setContinueFee(15.00);
        DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
        String orderAmount = droolsRulesService.calcFee(addressRule);
        checkResult.setPostCodeResult(true);
        checkResult.setOrderAmount(orderAmount);
    end
    ```

---

### 4) 关键场景与演示描述

*   **场景一：问题引入与解决方案** (00:00-00:15)
    *   讲师首先在PPT上指出当前系统已实现规则计算，但存在一个核心痛点：规则变更后需要重启服务。
    *   他随即提出解决方案：将规则文件存储在数据库中，通过HTTP接口实现动态加载，从而避免服务重启。

*   **场景二：数据库表设计** (00:15-00:25)
    *   讲师在PPT上展示 `rule` 表的完整SQL建表语句，包括 `id`, `content`, `create_time`, `last_modify_time`, `rule_key`, `version` 等字段，并强调了 `PRIMARY KEY` 和多个 `UNIQUE INDEX` 的作用。

*   **场景三：实体类开发** (00:25-00:35)
    *   讲师切换到IntelliJ IDEA，展示 `Rule` 实体类的代码。
    *   他解释了类中各字段的含义，并强调了 `@ApiModel` 和 `@TableId` 注解的作用，用于与数据库表映射。

*   **场景四：Mapper接口定义** (00:35-00:45)
    *   讲师在PPT上展示 `RuleMapper` 接口的代码框架。
    *   他解释了该接口继承自 `BaseMapper<Rule>`，用于通过MyBatis进行数据库操作。

*   **场景五：服务层开发** (00:45-00:55)
    *   讲师在PPT上展示 `ReloadDroolsRulesService` 服务的初步代码框架。
    *   他引入了 `org.kie.api` 包下的相关类，如 `KieServices`, `KieFileSystem`, `KieRepository`，为后续实现动态加载Drools规则做准备。

*   **场景六：规则文件示例** (00:55-01:05)
    *   讲师在PPT上展示了一个名为 `orderAmountCalc.drl` 的Drools规则文件。
    *   他详细解读了其中的规则定义，包括规则名称、激活组、优先级、条件和动作，展示了规则如何计算运费。

*   **场景七：多窗口演示** (01:05-01:15)
    *   讲师切换到一个包含多个窗口的视图，展示了IDEA、Navicat Premium和Swagger UI三个工具的协同工作。
    *   他通过这个视图说明了开发、数据库管理和API测试的完整流程。

*   **场景八：代码细节展示** (01:15-01:25)
    *   讲师在PPT上详细展示了 `Rule` 实体类中 `@Data`, `@ToString`, `@EqualsAndHashCode`, `@Accessors` 等Lombok注解的使用，以及 `@ApiModel` 和 `@TableName` 注解的作用。

*   **场景九：服务接口细节** (01:25-01:35)
    *   讲师在PPT上展示了 `ReloadDroolsRulesService`
