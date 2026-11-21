# 59-根据规则计算订单价格（实现步骤_5） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才呢咱们是对这个规则文件呢

简单优化了一下

那接下来呢我们就需要来编写什么呢

编写我们这个配置类

主要就是在我们的Spring Boot应用当中

对吧,来整合D-Rose

配置类这块呢

我们就直接从咱们讲义上

把这个代码抄过来就可以了

这个配置类呢叫什么呢

叫做D-Rose Auto Configuration

好,Ctrl-C把它复制一下

然后呢在咱们这个Config下边

那么我们来创建它

然后具体的代码呢咱们就直接抄过来了

这些代码呢咱们前面

其实都已经讲过了

这个都已经讲过了

这是在我们那个什么

前面Spring Boot

整合D-Rose的时候呢

也已经这个实现过了

当然我们当时呢也没有去手敲

对吧,因为这个配置类呢

它就相当于配置文件啊

其他配置文件的作用

那么这些代码呢基本上也都是模板化的

大家只要能看明白

它这里边在创建什么对象就可以了

大家可以来看一下这里边

一个是什么呢

创建的我们这个KE File System

那么它会读取什么呢

它会读取我们这个Rules目录下边

所有的这个规则文件

所以要保证我们的规则文件呢

都在这个Rules目录下

对吧

然后呢它是怎么读取呢

你看是在这个地方对吧

通过这个什么Resource Factory

然后呢New Class Path Resource

然后呢它是不是来创建我们的资源

对吧,给它构造成资源

然后呢就是这个

这个地方

这是我们拼的这个Rules

然后呢加上什么File Name对吧

但是它加载的话

在这个地方就是写

然后这个地方是加载

这不是GetRulesFile吗

从这个地方呢是不是调用这个方法

把我们这个Rules目录下

所有的文件是不是都给它取过来

然后呢封装成这么一个Resource

输送对象对吧

把它取过来

然后呢来写我们这个File System

其实在这呢就是创建这个KE的

这个文件系统这个对象

然后呢有了它之后呢

我们就可以来创建什么呢

这个KE Container对吧

这个Container就是我们的这个容器对象

我们使用这个容器对象呢

就可以获得Session

对吧,就可以获得Session

然后呢

下面这个是不是创建我们这个KE Base

而这个Base的话呢

直接通过这个Container就可以Get Base

所以你看前面呢

我们其实这个Session的话

你既可以通过这个什么呢

KE Container来创建

也可以通过KE Base来创建

然后呢这个地方呢

这是创建了Session对吧

然后呢这是创建我们那个后处理类

后处理器

这是这个配置类呢

咱们直接拿过来就可以了

唯一需要我们可能需要去修改的

也就这么一个路径

其他的呢都是固定的代码

然后呢不用做任何修改就可以了

好,这个配置类呢

我们就已经搞定了

然后接下来呢

我们需要来

这个在我们这个I-order Service接口里边来

扩展一个方法

这个方法呢就是计算我们这个定位的数据

这个方法呢就是计算我们这个定位的数据

和这个订单的价格

咱们在这个方法里面来算

你看我们当前呢

导入的这个初始工程里边啊

咱们来找一下有这么一个Service接口

叫做I-order Service

然后这里边呢

已经存在了一些方法的声明

比如说什么Save Order

这是不新增订单

还有什么Find by Page对吧

这应该是分页查询的

然后Find All

还有什么Page Like for Custom

这其实也是一个分页查询

只不过呢是有这个参数对吧

根据这些参数来进行计算

进行这个自定义的分页查询

那么这是已有的这些方法

那么我们就不用管了

然后在这个基础之上呢

我们再来扩展一个方法

这个方法呢叫做什么呢

Calculate Amount

计算订单价格

直接呢把这个方法呢

咱们复制到这个接口里边来

复制到这个接口里边来

然后呢这个方法呢

返回值是一个Map对吧

为什么是一个Map呢

就是因为我们这个返回值啊

这个Map里边

封装的数据比较多

所以我们使用一个Map来

在这个封装

这是Service接口

然后对应的呢

这个Service实现类呢

你看这边它是不是报错了

我们需要呢

把这个方法呢

给它实现出来

Calculate Amount

所以一会儿呢

我们重点就是来写这个方法

这个方法要做的就是什么呢

就是计算我们这个订单价格

好

但是这个方法写起来

其实还是比较

比较复杂的

因为什么呢

我们要计算订单价格

是不是前提需要知道它这个订单的距离

所以说这块呢

除了要计算订单价格之外呢

还需要来计算什么呢

订单这个距离

然后有了这个距离呢

然后才能去计算订单价格

而计算订单价格呢

就是调用什么呢

调用我们这个DRoze相应的这些API

对吧

所以一会儿呢

我们就具体来编写这个方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于在 Java 项目中集成 Drools 规则引擎的实战教学。讲师通过一个“订单运费计算”的业务场景，演示了如何将复杂的业务规则（如不同重量、不同距离的运费计算）从代码中剥离出来，封装为 Drools 规则文件，并通过 Spring Boot 配置类进行动态加载和执行。课程重点讲解了 Drools 规则的编写语法、Spring Boot 中的配置类（`DroolsAutoConfiguration`）如何自动装配 `KieContainer` 和 `KieSession`，以及如何在业务服务中调用规则引擎进行计算。整个过程旨在展示如何实现业务逻辑的“动态化”和“可维护性”。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 课程开场，介绍本节将讲解如何在项目中集成 Drools 规则引擎。
*   **00:10 - 00:30**: 展示项目结构，重点介绍 `rules` 目录下的规则文件（如 `orderAmountCalc.drl`）。
*   **00:30 - 01:00**: 讲解 Drools 规则文件的编写，展示如何定义规则（`rule`）、条件（`when`）和结果（`then`），并演示了如何在规则中调用 Java 代码。
*   **01:00 - 02:00**: 讲解 Spring Boot 配置类 `DroolsAutoConfiguration`，展示如何通过 `@Configuration` 和 `@Bean` 注解自动创建 `KieContainer` 和 `KieSession`。
*   **02:00 - 03:00**: 讲解 `DroolsAutoConfiguration` 中的 `kieFileSystem` 和 `kieBuilder` 配置，展示如何从类路径中加载规则文件并构建规则库。
*   **03:00 - 04:00**: 讲解如何在业务服务中（如 `OrderService`）调用 `DroolsRulesService` 来执行规则。
*   **04:00 - 05:00**: 展示 `OrderService` 中的 `calculateAmount` 方法，演示如何将订单数据传递给规则引擎进行计算。
*   **05:00 - 06:00**: 总结本节内容，强调规则引擎的动态性和可维护性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文档标题**: “品达物流TMS项目 - 第4章 订单中心服务开发(pd-oms)”
*   **章节**: “7.1 规则” 和 “7.2 实现步骤”
*   **关键步骤**: “第六步：创建Drools规则引擎配置类”，“第七步：创建Drools规则文件”，“第八步：在业务服务中调用规则”。

#### 代码关键内容

*   **Drools 规则文件 (`orderAmountCalc.drl`)**
    ```drl
    package rules;

    import com.ithema.pinda.entity.fact.AddressRule;
    import com.ithema.pinda.entity.fact.AddressCheckResult;
    import com.ithema.pinda.service.DroolsRulesService;
    import com.ithema.pinda.service.impl.DroolsRulesServiceImpl;

    dialect "java"

    rule "1千克以内20元"
        activation-group "mygroup"
        salience 10
    when
        addressRule : AddressRule(totalWeight != null && totalWeight <= 1.00)
    then
        checkResult : AddressCheckResult();
        checkResult.setPostCodeResult(true);
        checkResult.setResult("20");
        System.out.println("1千克以内20元");
    end

    rule "1千克以上，订单距离在200公里以下的，首重1千克，首重价格20元，续重每1千克资费为6元"
        activation-group "mygroup"
    when
        address : AddressRule(totalWeight != null && totalWeight > 1.00 && distance <= 200.00)
    then
        address.setFirstFee(20.00);
        address.setContinuedFee(6.00);
        address.setFirstWeight(1.00);
        DroolsRulesServiceImpl droolsRulesService = new DroolsRulesServiceImpl();
        String fee = droolsRulesService.calcFee(address);
        checkResult.setPostCodeResult(true);
        checkResult.setResult(fee);
        System.out.println("大于1kg,500公里以上！");
    end
    ```

*   **Spring Boot 配置类 (`DroolsAutoConfiguration.java`)**
    ```java
    @Configuration
    public class DroolsAutoConfiguration {

        @Bean
        @ConditionalOnMissingBean(KieFileSystem.class)
        public KieFileSystem kieFileSystem() throws IOException {
            KieFileSystem kieFileSystem = getKieServices().newKieFileSystem();
            for (Resource file : getRuleFiles()) {
                kieFileSystem.write(ResourceFactory.newClassPathResource(path + RULES_PATH + file.getFilename(), encoding: "UTF-8"));
            }
            return kieFileSystem;
        }

        @Bean
        @ConditionalOnMissingBean(KieContainer.class)
        public KieContainer kieContainer() throws IOException {
            final KieRepository kieRepository = getKieServices().getRepository();
            kieRepository.addKieModule(new KieModule() {
                public ReleaseId getReleaseId() {
                    return kieRepository.getDefaultReleaseId();
                }
            });

            KieBuilder kieBuilder = getKieServices().newKieBuilder(kieFileSystem);
            kieBuilder.buildAll();

            KieContainer kieContainer = getKieServices().newKieContainer(kieRepository.getDefaultReleaseId());
            return kieContainer;
        }

        @Bean
        @ConditionalOnMissingBean(KieBase.class)
        public KieBase kieBase() throws IOException {
            return kieContainer().getKieBase();
        }

        @Bean
        @ConditionalOnMissingBean(KieSession.class)
        public KieSession kieSession() throws IOException {
            return kieContainer().newKieSession();
        }

        @Bean
        @ConditionalOnMissingBean(KModuleBuilderFactoryPostProcessor.class)
        public KModuleBuilderFactoryPostProcessor kiePostProcessor() {
            return new KModuleBuilderFactoryPostProcessor();
        }
    }
    ```

*   **业务服务 (`OrderService.java`)**
    ```java
    public class OrderServiceImpl implements OrderService {

        @Override
        public IPage<Order> findByPage(Integer page, Integer pageSize, Order order) {
            Page<Order> page = new Page(page, pageSize);
            LambdaQueryWrapper<Order> lambdaQueryWrapper = new LambdaQueryWrapper<>();
            if (StringUtils.isNotEmpty(order.getId())) {
                lambdaQueryWrapper.eq(Order::getId, order.getId());
            }
            if (order.getStatus() != null) {
                lambdaQueryWrapper.eq(Order::getStatus, order.getStatus());
            }
            if (order.getPaymentStatus() != null) {
                lambdaQueryWrapper.eq(Order::getPaymentStatus, order.getPaymentStatus());
            }
            if (StringUtils.isNotEmpty(order.getSenderName())) {
                lambdaQueryWrapper.like(Order::getSenderName, order.getSenderName());
            }
            if (StringUtils.isNotEmpty(order.getSenderPhone())) {
                lambdaQueryWrapper.like(Order::getSenderPhone, order.getSenderPhone());
            }
            if (StringUtils.isNotEmpty(order.getSenderProvinceId())) {
                lambdaQueryWrapper.eq(Order::getSenderProvinceId, order.getSenderProvinceId());
            }
            if (StringUtils.isNotEmpty(order.getSenderCityId())) {
                lambdaQueryWrapper.eq(Order::getSenderCityId, order.getSenderCityId());
            }
            lambdaQueryWrapper.orderByDesc(Order::getCreateTime);
            return page(page, lambdaQueryWrapper);
        }

        @Override
        public Map calculateAmount(OrderDTO orderDTO) {
            // 计算订单价格
            // 计算订单距离
            return null;
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：规则文件编写与调试**
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `orderAmountCalc.drl` 文件，逐行讲解规则的语法结构。他特别强调了 `when` 子句中如何定义条件（如 `totalWeight <= 1.00`），以及 `then` 子句中如何调用 Java 方法（如 `System.out.println`）来输出结果。
    *   **演示**: 通过高亮显示代码行，讲师解释了 `salience` 和 `activation-group` 的作用，以及如何通过 `checkResult` 对象来传递计算结果。

*   **场景二：Spring Boot 配置类开发**
    *   **描述**: 讲师在 `DroolsAutoConfiguration.java` 文件中，演示了如何使用 `@Configuration` 注解创建一个配置类。他重点讲解了 `@Bean` 和 `@ConditionalOnMissingBean` 注解的使用，以及如何通过 `KieBuilder` 和 `KieContainer` 来构建和加载规则库。
    *   **
