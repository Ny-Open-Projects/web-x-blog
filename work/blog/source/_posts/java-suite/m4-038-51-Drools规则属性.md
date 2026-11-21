---
title: "Drools 规则属性与 SpringBoot 整合：落地品达 TMS 订单价格计算六步实现"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 品达物流TMS]
tags: [Java, 项目实战, Drools]
---

# Drools 规则属性与 SpringBoot 整合：落地品达 TMS 订单价格计算六步实现

上篇收尾基础语法时埋了两个伏笔：salience 在 retract 演示里初次露面，update 的死循环风险悬而未决。本篇先把规则属性补齐——五个最常用的属性足以解决优先级、开关、互斥和死循环四类问题；随后把 Drools 搬进 SpringBoot，核心是一个模板化的配置类；最后回到品达 TMS 的订单中心服务，按六步实现"根据规则计算订单价格"：先用百度地图算出订单距离，再把参数交给规则引擎匹配计价。

## 先给结论

- 规则属性写在 rule 名称与 when 之间：salience 优先级（Integer，值越大越优先，默认 0）、dialect 语言类型（java/mvel，默认 java）、enabled 启用开关（默认 true，设为 false 则无论是否匹配成功都不触发）、activation-group 激活分组（组名相同的规则只能有一个触发）、no-loop 防死循环。
- SpringBoot 整合 Drools 的核心是一个配置类：@Bean + @ConditionalOnMissingBean 依次注册 KieFileSystem（扫描 rules 目录所有 drl）、KieContainer（KieBuilder buildAll 构建）、KieBase 等单例；业务侧注入容器后 newKieSession → fireAllRules → dispose。规则文件必须放 rules 目录，配置类别忘了加 @Configuration。
- TMS 计价规则以重量加距离为维度：1 千克以内固定 20 元；超过 1 千克按距离分 200 公里以下、200~500 公里、500 公里以上三档，首重 1 千克 20 元，续重每 1 千克分别 6、9、15 元。
- 六步实现：封装 Fact 实体 AddressRule（参数）与 AddressCheckResult（结果）→ 计算逻辑抽到 DroolsRulesService.calcFee（BigDecimal，超出部分向下取整）→ 编写 orderAmountCalc.drl 四条规则 → activation-group "mygroup" + salience 10/9/8/7 让互斥规则只中一条 → DroolsAutoConfiguration 配置类 + IOrderService 扩展 calculateAmount → getDistance 用百度地图先算距离。
- 规则文件里只设参数不算账：then 里 set 首重、首重价格、续重价格，再 new 一个 DroolsRulesServiceImpl 调 calcFee，把返回价格写回 checkResult——后三条套路相同只有续重不同，抽到 Service 避免重复三遍；这个 Service 不加 @Service 注解，由规则文件自己 new。
- 细节三处：边界值用 <= 卡严（恰好 200、500 公里要有所归属）；百度地图返回的距离单位是米，规则判断的是公里，要除以 1000 并用 DecimalFormat("#.##") 保留两位小数；地址要先经 getCoordinate 转成经纬度坐标才能算距离，且两个坐标都要判空。

## 五个常用规则属性：优先级、开关、分组与防死循环

规则体语法结构里，rule 名称之后、when 之前有一个 attributes 位置，规则属性就写在这里。Drools 的属性很多，这里挑常用的五个整体浏览：

| 属性 | 说明 |
| --- | --- |
| salience | 指定规则执行优先级，Integer，值越大越优先 |
| dialect | 指定规则使用的语言类型，java 或 mvel |
| enabled | 指定规则是否启用，boolean 类型 |
| activation-group | 激活分组，组名相同的多个规则只能有一个触发 |
| no-loop | 防止死循环 |

enabled 最简单：不设置默认就是 true；设成 enabled false，当前规则无论是否匹配成功都不会触发。dialect 指定当前规则使用的语言，取值 java 和 mvel——MVEL 是一种基于 Java 语法的表达式语言，有点类似正则表达式，支持集合、数组、字符串等的匹配操作符；实际写规则基本都用 java，了解即可。

salience 的演示用三条条件为 eval(true) 的规则（恒匹配）：

```java
rule "rule_1"
    salience 9
    when
        eval(true)
    then
        System.out.println("规则rule_1触发");
end
```

rule_2 设 salience 10、rule_3 设 salience 8。不设置 salience 时默认按规则文件自上而下执行；设置后触发顺序变成 rule_2 → rule_1 → rule_3，值越大越优先。建议编写规则文件时明确指定每个规则的优先级，不靠隐式顺序。

no-loop 的演示正好接上上篇的警告。规则条件是 age == 25，then 里又 update 这个对象：

```java
rule "rule_noloop"
    no-loop true
    when
        $student:Student(age == 25)
    then
        update($student); // 注意此处执行update会导致当前规则重新被激活
        System.out.println("规则rule_noloop触发");
end
```

测试时 new 一个 age=25 的 Student 插入工作内存：匹配成功执行 then，update 让当前规则重新被激活，再匹配还是 25，再 update——死循环。先注释掉 no-loop true 跑一遍就能看到这个效果；把 no-loop true 放回属性位置（注意它写在 rule 和 when 之间），规则只触发一次，循环被掐断。

activation-group 的演示用两条 when 为空的规则——LHS 为空视为恒为 true，两条都能匹配：

```java
rule "rule_activationgroup_1"
    activation-group "mygroup"
    when
    then
        System.out.println("规则rule_activationgroup_1触发");
end
```

两条规则的组名都叫 mygroup，同一组里只能有一个规则被触发；没设 salience 时按文件顺序，rule_1 触发、rule_2 不触发。这个特性马上会在 TMS 计价规则里派上大用场。

## SpringBoot 整合：一个配置类搞定

现在的项目都基于 SpringBoot 开发，这也是后面 TMS 里使用 Drools 的方式。整合步骤不复杂：

1. 创建工程，pom 里导入常规 SpringBoot 坐标（spring-boot-starter-parent 2.7.0、starter-web 等）加 Drools 相关坐标；
2. application.yml 配置服务端口号和应用名称；
3. resources 下建 rules 目录，放一个最简单的 helloworld.drl：

```java
package rules
rule "rule_helloworld"
    when
        eval(true)
    then
        System.out.println("规则: rule_helloworld触发了...");
end
```

when 里显式写 eval(true) 恒为真，规则直接匹配成功，所以后面测试时根本不需要 insert Fact 对象。

4. 配置类——整个整合的核心就这一个类，代码模板化，作用相当于配置文件，能看懂、会改路径即可：

```java
@Configuration
public class DroolsConfig {
    // 指定规则文件目录：所有规则文件必须放在这个目录下，否则读取不到
    private static final String RULES_PATH = "rules/";
    private final KieServices kieServices = KieServices.Factory.get();

    // 创建Kie文件系统，读取rules目录下所有规则文件
    @Bean
    @ConditionalOnMissingBean
    public KieFileSystem kieFileSystem() throws IOException {
        KieFileSystem kieFileSystem = kieServices.newKieFileSystem();
        ResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
        Resource[] files = resolver.getResources("classpath:*" + RULES_PATH + "/*.drl");
        for (Resource file : files) {
            kieFileSystem.write(ResourceFactory.newClassPathResource(RULES_PATH + file.getFilename(), "UTF-8"));
        }
        return kieFileSystem;
    }

    // 构建Kie容器
    @Bean
    @ConditionalOnMissingBean
    public KieContainer kieContainer() throws IOException {
        KieRepository kieRepository = kieServices.getRepository();
        KieBuilder kieBuilder = kieServices.newKieBuilder(kieFileSystem());
        kieBuilder.buildAll();
        return kieServices.newKieContainer(kieRepository.getDefaultReleaseId());
    }

    // 从容器中获取规则库
    @Bean
    @ConditionalOnMissingBean
    public KieBase kieBase() throws IOException {
        return kieContainer().getKieBase();
    }
}
```

每个方法都是 @Bean 加 @ConditionalOnMissingBean：Spring 容器里没有这种 Bean 时才创建，保证这些核心对象是单例。KieFileSystem 负责把 rules 目录下的 drl 文件读进来（通过 ResourceFactory 把每个文件构造成资源写入）；有了它再构建 KieContainer，KieBase 直接从容器 get 出来。此外还注册了一个后处理器 KModuleBeanFactoryPostProcessor 的 Bean，KieSession 则既可以通过 KieContainer 创建，也可以通过 KieBase 创建。整套代码唯一可能需要修改的就是 RULES_PATH 这个路径，其余都是固定写法；特别注意配置类的 @Configuration 注解不能漏，不加不生效。

业务侧就轻松了。Service 注入容器，拿会话、触发、关闭：

```java
@Service
public class RuleService {
    @Autowired
    private KieContainer kieContainer;

    public void rule() {
        KieSession kieSession = kieContainer.newKieSession();
        kieSession.fireAllRules();
        kieSession.dispose();
    }
}
```

Controller 注入 RuleService，提供一个端点调用 rule() 即可。启动项目（端口 8080），访问 http://localhost:8080/hello/rule，控制台输出"规则: rule_helloworld触发了..."——整合成功。后面 TMS 里的配置类 DroolsAutoConfiguration 与这个完全同款，只是类名和所在工程不同。

## TMS 落地：六步实现根据规则计算订单价格

规则引擎和百度地图都备齐了，回到订单中心服务。绝大部分代码已经提供好：CargoController 的货物增删改查、OrderController 的订单新增（sale）、分页、详情都是现成的；还没实现的是订单价格和订单距离的计算。sale 方法目前保存完订单就直接返回，而订单价格不可能由前端传过来，必须由服务端根据寄件人地址、收件人地址、货物重量等参数算出来。计价规则四条，维度是货物重量和订单距离：

| 条件 | 计价标准 |
| --- | --- |
| 1千克以内 | 不考虑距离，价格 20 元 |
| 1千克以上，距离 200 公里以下 | 首重 1 千克 20 元，续重每 1 千克 6 元 |
| 1千克以上，距离 200~500 公里 | 首重 1 千克 20 元，续重每 1 千克 9 元 |
| 1千克以上，距离 500 公里以上 | 首重 1 千克 20 元，续重每 1 千克 15 元 |

距离本身也要算——用前面封装好的百度地图接口。整体流程：先调百度地图把距离算出来，再用规则引擎按四条规则匹配，得出订单价格。

### 第一步：封装两个 Fact 实体

entity 包下建 fact 子包，放两个类。AddressRule 封装计算所需的参数，AddressCheckResult 封装计算后的结果——前者是计算依据，后者要跟着一起插入工作内存参与匹配：

```java
public class AddressRule {
    // 货品总重量
    private double totalWeight;
    // 距离
    private double distance;
    // 续重价格
    private double continuedFee;
    // 首重
    private double firstWeight;
    // 首重价格
    private double firstFee;
    // getter/setter 省略
}

public class AddressCheckResult {
    // 是否匹配成功（校验通过），默认 false，匹配上任意一条规则就置为 true
    private boolean postCodeResult;
    // 订单价格计算结果
    private String result;
    // getter/setter 省略
}
```

### 第二步：计算逻辑抽到 Service

一个设计取舍：后三条规则的计费套路完全一样，只有续重资费不同（6/9/15），把计算过程写进规则文件就得重复三遍。所以把真正的计算抽到 Service，规则文件只负责匹配和设参数。这个 Service 不交给 Spring 容器管理，规则文件里自己 new 对象，因此不加 @Service 注解：

```java
public interface DroolsRulesService {
    // 根据条件计算订单价格
    String calcFee(AddressRule addressRule);
}
```

实现类的 calcFee 用 BigDecimal 做财务计算——先把总重量、首重、首重价格、续重价格都转成 BigDecimal，减、乘、加分别对应 subtract、multiply、add 方法：

```java
@Override
public String calcFee(AddressRule addressRule) {
    // 货物总重量、首重、首重价格、续重价格
    BigDecimal totalWeight = new BigDecimal(addressRule.getTotalWeight());
    BigDecimal firstWeight = new BigDecimal(addressRule.getFirstWeight());
    BigDecimal firstFee = new BigDecimal(addressRule.getFirstFee());
    BigDecimal continuedFee = new BigDecimal(addressRule.getContinuedFee());

    // 超过首重部分的重量 = 总重量 - 首重
    BigDecimal lost = totalWeight.subtract(firstWeight);
    // 续重按每超过1千克计费，小数部分舍弃（向下取整）
    lost = lost.setScale(0, BigDecimal.ROUND_DOWN);
    // 续重费用 + 首重价格
    return continuedFee.multiply(lost).add(firstFee).toString();
}
```

能调到这个方法说明走的是后三条规则（1000 克以上的情况），所以方法里直接按这三条算。main 方法验证：totalWeight=5、firstWeight=1、firstFee=20、continuedFee=6，5 减 1 超出 4 公斤，4 乘 6 得 24，加首重 20，输出 44；总重量改成 5.3 结果还是 44——多出的 0.3 公斤不足 1 千克，被 setScale(0, ROUND_DOWN) 舍弃掉了。

### 第三步：编写规则文件 orderAmountCalc.drl

resources/rules 下创建订单价格计算的规则文件。package 叫 rules（逻辑概念，随意），import 两个 Fact 类和 Service 实现类（规则里要 new），指定 dialect "java"。前两条规则：

```java
rule "1千克以内20元"
    when
        addressRule : AddressRule(totalWeight != null && totalWeight <= 1.00)
        checkResult : AddressCheckResult()
    then
        checkResult.setPostCodeResult(true);
        checkResult.setResult("20");
        System.out.println("1千克以内20元");
end

rule "1千克以上，订单距离在200公里以下的，首重1千克，首重价格20元，续重每1千克资费为6元"
    when
        addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance <= 200.00)
        checkResult : AddressCheckResult()
    then
        addressRule.setFirstFee(20.00);
        addressRule.setFirstWeight(1.00);
        addressRule.setContinuedFee(6.00);
        DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
        String orderAmount = droolsRulesService.calcFee(addressRule);
        checkResult.setPostCodeResult(true);
        checkResult.setResult(orderAmount);
        System.out.println("1千克以上，订单距离在200公里以下");
end
```

几个细节：属性是 double 类型，条件里的值写成 1.00、200.00 带小数；第一条规则命中后价格固定 20，直接 setResult("20")，不走计算；后三条的 then 只 set 首重价格、首重、续重价格三个参数，然后 new 实现类调 calcFee，把返回的订单价格写进 checkResult——货物总重量不用在这里设，它在 Fact 对象传进来时就已经确定，是 LHS 里的匹配条件。第三、四条规则结构与第二条完全相同，只是距离范围换成 <= 500.00 和 > 500.00，续重价格换成 9.00 和 15.00。

边界值要专门卡一下：如果距离恰好是 500 整，"小于500"和"大于500"两头都够不着，比较尴尬。讲义的处理是让 <= 200 归第二档、> 200 且 <= 500 归第三档、> 500 归第四档，每个边界值都有归属。

### 第四步：activation-group 与 salience 优化规则

这四条规则互斥，最终只可能有一条匹配。既然如此，给四条规则都加 activation-group "mygroup"（组名务必一致，别写错），同组只能触发一个；再加 salience 10、9、8、7 排序，让匹配按自上而下进行——第一条匹配成功，后面的就不再匹配。互斥还带来一个条件简化：能匹配到第三条就说明前两条都没中，距离必然大于 200，所以第三条的左边界条件可以去掉，直接写 distance <= 500.00；第四条也不用修改。两个属性一加，规则文件在正确性之外又多了效率这一层。

### 第五步：配置类入位，扩展业务接口

把前面那套配置类抄进 TMS，类名 DroolsAutoConfiguration，放在 config 包下，同样全是模板代码——KieFileSystem 扫 rules 目录、KieContainer 构建、KieBase 和 KieSession 提供规则库与会话，唯一要确认的是规则文件路径。然后在 IOrderService 接口扩展一个 calculateAmount 方法，返回值是 Map——要往回带的数据比较多。接口里已有的 saveOrder、findByPage、findAll、findByPageForCustom 都不动，实现类 OrderServiceImpl 把 calculateAmount 实现出来：先算订单距离，有了距离才能调 Drools 相关 API 算订单价格。

### 第六步：getDistance 用百度地图算订单距离

距离是计价的前提参数，单独封装一个方法，入参出参都是 OrderDTO（DTO 属性很多，其中就有 distance）：

```java
public OrderDTO getDistance(OrderDTO orderDTO) {
    // 调百度地图接口，根据寄件人地址获取对应的经纬度坐标
    String begin = BaiduMapUtils.getCoordinate(orderDTO.getSenderAddress());
    // 健壮性：地址解析失败，把错误信息写回对应字段并直接返回
    if (begin == null) {
        orderDTO.setSenderAddress("sender error msg");
        return orderDTO;
    }
    // 收件人地址同样先转坐标
    String end = BaiduMapUtils.getCoordinate(orderDTO.getReceiverAddress());
    if (end == null) {
        orderDTO.setReceiverAddress("receiver error msg");
        return orderDTO;
    }
    // 计算两点之间的距离
    Double distance = BaiduMapUtils.getDistance(begin, end);
    // 米换算成公里，并保留两位小数
    DecimalFormat df = new DecimalFormat("#.##");
    String distanceStr = df.format(distance / 1000);
    orderDTO.setDistance(new BigDecimal(distanceStr));
    return orderDTO;
}
```

顺序上有讲究：算距离需要的是坐标，不能拿地址直接算，所以先用 BaiduMapUtils 的 getCoordinate 把寄件人、收件人地址分别解析成经纬度（begin/end）；两个坐标都要判空——客户随手写个"123"是解析不出坐标的，解析失败就把错误信息写回 DTO 对应字段直接返回。都解析成功才调 getDistance(begin, end) 拿距离。返回的单位是米，而规则文件里判断的是公里，所以要除以 1000 换算；换算后小数可能很长，用 DecimalFormat("#.##") 保留两位小数，格式化得到的是字符串，再包一层 new BigDecimal 设置到 DTO 的 distance 上（该属性就是 BigDecimal 类型），最后把 DTO 返回。calculateAmount 里一行 this.getDistance(orderDTO) 把结果接住，距离就位，剩下的就是把 AddressRule 装好、交给规则引擎匹配计价了。

## 小结

本篇把 Drools 课程主线走完。规则属性补齐五个：salience 管顺序、enabled 管开关、dialect 管语言、activation-group 管互斥分组、no-loop 管死循环——上篇 update 演示里悬着的死循环隐患，一个 no-loop true 就地拆掉。SpringBoot 整合的实质是一个模板化配置类：@Bean 加 @ConditionalOnMissingBean 把 KieFileSystem、KieContainer、KieBase（及后处理器）注册成单例，规则文件统一放 rules 目录，业务侧注入容器、newKieSession、fireAllRules、dispose。TMS 计价则把两条技术线拧成一股：两个 Fact 实体分别装参数和结果，calcFee 用 BigDecimal 把"超出首重部分向下取整、乘续重、加首重"算清楚，orderAmountCalc.drl 四条规则用 activation-group 加 salience 保证互斥命中、边界值用 <= 卡严，getDistance 依托百度地图把地址转坐标、距离从米换算成公里再交回 DTO。到这里，续重资费要调时改的是 drl 文件里那几个数字，而不是 Java 代码里的 if-else——前面"规则即数据"的铺垫，在订单价格上落了地。
