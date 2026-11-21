---
title: "Drools 实战：WorkBench 远程加载规则、个人所得税计算器与信用卡申请规则设计"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 实战：WorkBench 远程加载规则、个人所得税计算器与信用卡申请规则设计

WorkBench 的最后一步，是在自己的项目里使用已部署到 Maven 仓库的规则：工程里不写任何规则文件，通过远程加载 jar 包完成规则调用。随后进入 Drools 实战章节：第一个案例是基于 2011 版个税规则的个人所得税计算器，从规则设计、DRL 编写到 Spring Boot 集成完整走一遍；第二个案例信用卡申请完成规则设计与项目骨架，规则实现留待下一篇。

## 先给结论

- WorkBench 部署的本质是把数据对象和规则文件打成 jar 包安装到内置 Maven 仓库，应用端走 HTTP 远程加载这个 jar 包即可触发规则，工程内不需要任何 DRL 文件。
- 远程加载通过 UrlResource 完成，必须带 Basic 认证（用户名、密码都是 kie，来自安装时 Tomcat 的 tomcat-users 配置），流程是取输入流 → addKieModule → newKieContainer → newKieSession，属于模板化代码，实际只需修改 URL 地址。
- WorkBench 里修改规则重新构建部署后，应用端代码一行不改，再次执行就能加载到最新规则，实现业务规则与应用完全分离、动态变更。
- 个人所得税计算器共 9 条规则，分三类：计算应纳税所得额、按区间设置税率与速算扣除数（7 条）、计算税后工资；示例输入 15000，输出应纳税所得额 11500、税率 0.25、速算扣除数 1005、扣税额 1870、税后工资 13130。
- DRL 里用 salience 保证执行顺序，date-effective 控制生效日期，no-loop 防止 update 死循环，activation-group 保证七档税率规则只触发一条。
- 信用卡申请涉及两类规则：4 条合法性检查加 5 条额度确定；实体类 checkResult 默认 true、额度默认 0，检查不通过就 setCheckResult(false) 并调用 drools.halt() 直接终止规则引擎。

## WorkBench 收尾：在项目中远程加载部署的规则

在 WorkBench 中点击齿轮按钮进入 artifacts 页面，可以看到所有已部署的 jar 包，当前只有一个 myproject-1.0.0。点击下载按钮，控制台会打印出这个 jar 包的完整网络访问地址：

```text
http://localhost:8080/kie-drools-wb/maven2wb/com/mspace_1/myproject_1/1.0.0/myproject_1-1.0.0.jar
```

这个地址的构成值得拆开看：localhost:8080 是 WorkBench 所在 Tomcat 的地址和端口；kie-drools-wb 是应用名；maven2wb 是固定写法，由于安装时已配置名为 maven2 的第三方 Maven 仓库，这段写成 maven2 也能访问；后半部分是 jar 包的 GAV 坐标加文件名。只要网络相通，任何机器访问这个地址都能拿到 jar 包，"远程"指的就是通过网络获取。

在 IDEA 里创建 Maven 工程 TestWB，依赖只需要 drools-compiler 和 junit 两个包。这里有个容易被问到的点：jar 包已经在 Maven 仓库里了，能不能直接用 Maven 依赖引入？可以，但课程提供的是另一种方式——通过服务动态加载。因为不直接依赖 jar 包，WorkBench 里创建的 Student 数据对象必须在本地工程照原样建一份：包名、类名、属性名、getter/setter 完全一致，并实现 Serializable 接口，甚至逐字复制过来都可以。

单元测试的核心代码如下：

```java
// 远程加载 Maven 仓库中的 jar 包，通过此 URL 可访问到 Maven 仓库中的 jar 包
String url = "http://localhost:8080/kie-drools-wb/maven2wb/com/mspace_1/myproject_1/1.0.0/myproject_1-1.0.0.jar";

KieServices kieServices = KieServices.Factory.get();
UrlResource resource = (UrlResource) kieServices.getResources().newUrlResource(url);
// 访问 WorkBench 服务需要身份认证，账号密码即登录 WorkBench 的账号
resource.setUsername("kie");
resource.setPassword("kie");
resource.setBasicAuthentication("enabled");

// 将资源转换为输入流
InputStream inputStream = resource.getInputStream();

// 创建仓库对象，通过输入流读取 jar 包数据，包装成 KieModule 添加到仓库
KieRepository repository = kieServices.getRepository();
KieModule kieModule = repository.addKieModule(
        kieServices.getResources().newInputStreamResource(inputStream));

// 基于 KieModule 创建容器，再获取 session
KieContainer kieContainer = kieServices.newKieContainer(kieModule.getReleaseId());
KieSession session = kieContainer.newKieSession();

session.insert(person);      // 插入满足条件的 Fact 对象
session.fireAllRules();      // 触发规则
session.dispose();
```

与入门案例的区别在于：以前规则文件就在本工程类路径下，用 newClassPathContainer 从类路径创建容器即可；现在规则在远程 jar 包里，只能先经 UrlResource 拿输入流，读成 KieModule 加入 KieRepository，再用 kieModule.getReleaseId()（对应 jar 包的 GAV 坐标）创建容器。代码层次多一点，但全是模板化写法。

认证这一步不能省：jar 包通过 WorkBench 服务对外发布，访问 WorkBench 本身就要登录，账号密码正是安装时配置在 Tomcat 的 tomcat-users.xml 里的那一对（用户名 kie、密码 kie）。不设置用户名密码，资源根本访问不到。

验证规则动态变更：WorkBench 里的规则要求 age 等于 20 且 name 不为空。本地直接执行单元测试不报错但规则不触发（没插 Fact）；插入 age=20、name 非空的 Student 后输出"规则1"，触发成功。接着在 WorkBench 把规则改成 age < 20，重新构建部署覆盖原版本，应用端代码不动，age 传 20 不触发，改成 10 又触发成功。这就是这套方案的价值：应用与业务规则完全分离，类似 Web Service 的远程调用；WorkBench 修改规则后应用无需改动即可加载最新规则，实现动态变更。加载过程虽然繁琐，但除 URL 里的 IP、端口需按环境修改外，其余都是固定写法。

## 个人所得税计算器：规则设计与完整实现

个人所得税计算器基于 2011 年 9 月 1 日生效的个税规则：输入税前月收入，计算应纳税所得额、税率、速算扣除数、扣税额和税后工资。几个名词先对齐：应纳税所得额是税前月收入减去 3500 元（2011 版允许扣除的支出）后的余额；税率随收入浮动；速算扣除数是为简化超额累进税率分级计算而预先算出的数值。

完整的 9 条规则如下：

| 规则 | 条件 | 动作 |
| :--- | :--- | :--- |
| 1 | 计算应纳税所得额 | 应纳税所得额 = 税前工资 − 3500 |
| 2 | 应纳税所得额 ≤ 1500 | 税率 0.03，速算扣除数 0 |
| 3 | 1500 < 应纳税所得额 ≤ 4500 | 税率 0.1，速算扣除数 105 |
| 4 | 4500 < 应纳税所得额 ≤ 9000 | 税率 0.2，速算扣除数 555 |
| 5 | 9000 < 应纳税所得额 ≤ 35000 | 税率 0.25，速算扣除数 1005 |
| 6 | 35000 < 应纳税所得额 ≤ 55000 | 税率 0.3，速算扣除数 2755 |
| 7 | 55000 < 应纳税所得额 ≤ 80000 | 税率 0.35，速算扣除数 5505 |
| 8 | 应纳税所得额 > 80000 | 税率 0.45，速算扣除数 13505 |
| 9 | 计算税后工资 | 扣税额 = 应纳税所得额 × 税率 − 速算扣除数；税后工资 = 税前工资 − 扣税额 |

手工推演一遍税前工资 10000 的情况：应纳税所得额 10000 − 3500 = 6500，落在 4500~9000 档，税率 0.2、速算扣除数 555；扣税额 6500 × 0.2 − 555 = 745；税后工资 10000 − 745 = 9255。换 15000 验证：应纳税所得额 11500 落在 9000~35000 档，扣税额 11500 × 0.25 − 1005 = 1870，税后工资 13130。写规则之前必须先会算，否则规则文件无从下手。

工程采用主流的 Spring Boot 整合 Drools 方式，工程名 calculation。pom.xml 继承 spring-boot-starter-parent 2.0.6.RELEASE，Drools 坐标与前面整合章节完全一致，编译插件指定 1.8。application.yml 只配端口 8080 和应用名 calculation，没有数据源等配置。

配置类 DroolsConfig 里有一句前面章节强调过的 System.setProperty("drools.dateformat", "yyyy-MM-dd")：规则文件里使用了日期且不是 Drools 默认格式时必须设置，否则启动时的预检查就会报错。配置类扫描 classpath 下 rules 目录的所有 .drl 文件写入 KieFileSystem，buildAll 后暴露 KieContainer 和 KieBase 两个 Bean。实体类 Calculation 与页面字段一一对应，六个属性全是 double：wage（税前工资）、wagemore（应纳税所得额）、cess（税率）、preminus（速算扣除数）、wageminus（扣税额）、actualwage（税后工资）。

规则文件 calculation.drl 放在 resources/rules 下，package 为 calculation，import 实体类。文件里的规则分三类，第一类和第三类各一条，第二类七条。核心规则如下：

```java
package calculation
import com.itheima.drools.entity.Calculation

// 第一类：计算应纳税所得额
rule "计算应纳税所得额"
    salience 100
    date-effective "2011-09-01"
    no-loop true
    when
        $cal : Calculation(wage > 0)
    then
        double wagemore = $cal.getWage() - 3500;
        $cal.setWagemore(wagemore);
        update($cal);
end

// 第二类：设置税率、速算扣除数（共 7 条，此处列两条）
rule "设置税率，应纳税所得额在1500至4500之间"
    salience 90
    no-loop true
    activation-group "SETCess_Group"
    when
        $cal : Calculation(wagemore > 1500 && wagemore <= 4500)
    then
        $cal.setCess(0.1);
        $cal.setPreminus(105);
        update($cal);
end

// 第三类：计算税后工资
rule "个人所得税：计算税后工资"
    salience 80
    when
        $cal : Calculation(wage > 0 && wagemore > 0 && cess > 0)
    then
        double wageminus = $cal.getWagemore() * $cal.getCess() - $cal.getPreminus();
        $cal.setWageminus(wageminus);
        double actualwage = $cal.getWage() - wageminus;
        $cal.setActualwage(actualwage);
end
```

几个属性配合使用的逻辑值得细看。计算顺序必须是先算应纳税所得额、再设置税率、最后算税后工资，所以用 salience 控制优先级（数值越大越优先）：第一条 100，设置税率的一组 90，最后一条 80。第一条规则里改完对象后必须 update——不更新后面的规则感知不到新值；而一旦 update，当前规则自己也会重新匹配，条件 wage > 0 依然成立，就会无限执行，所以每个用了 update 的规则都要加 no-loop true 防死循环。七个设置税率的规则都放进 activation-group "SETCess_Group"，保证组内只能触发一个：课程里的边界值已处理干净（条件无重叠），这层不是必须的，但万一边界写重（两条同时写成 ≤4500 和 ≥4500，恰好 4500 时两条都命中），激活组是最后一道保险。date-effective 只需在第一条规则上设置：第一条不触发时 wagemore 是默认值 0，后面所有区间规则都匹配不上，整条链路都不会执行。最后一条规则的 LHS 没限制速算扣除数大于 0，因为第一档它本来就是 0。

服务层很薄：

```java
@Service
public class RuleService {
    @Autowired
    private KieBase kieBase;

    // 调用 Drools 规则引擎实现个人所得税计算
    public Calculation calculate(Calculation calculation) {
        KieSession session = kieBase.newKieSession();
        session.insert(calculation);
        session.fireAllRules();
        session.dispose();
        return calculation;
    }
}
```

KieBase 能直接注入，靠的就是配置类里的 @Bean 声明。这个方法返回的还是传入的那个对象：insert 进工作内存的 Fact 与 Java 侧是同一个引用，规则文件里对它做的所有 set 操作，Java 代码都能感知到——Fact 对象就是 Java 程序和规则引擎之间的数据桥梁。传进去时只设置了税前工资，返回时其余字段已经全部是计算结果。控制器 @RestController + @RequestMapping("/rule")，/calculate 接收 wage 参数，new 一个 Calculation 只 set wage，调完 service 后把对象转成 JSON 返回页面。

前端页面 calculation.html 放在 resources/static 下，用 Vue 的 v-model 做双向绑定：输入框绑 cal.wage，计算按钮触发 calculate 方法。方法先判断税前月收入是否小于等于 3500——没到免征额不用交税，直接 alert 提示并 return；否则 axios 发 GET 请求到 /rule/calculate，回调里 this.cal = res.data，Vue 自动把结果回填到各输入框。页面用了 ES6 语法，IDEA 语言级别切到 ECMAScript 6 即可消除报错。

启动后访问 localhost:8080/calculation.html 实测：输入 10000，页面显示扣税额 745、税后工资 9255；输入 15000，显示税率 0.25、速算扣除数 1005、扣税额 1870、税后工资 13130，与规则表推演一致。控制台同时输出规则文件里的调试打印和 controller 里的 toString——核心计算逻辑全部在规则文件里，页面只负责展示结果。

## 信用卡申请开篇：两类规则与项目骨架

第二个实战案例回到第一章问题引出时提过的信用卡申请场景：表单提交姓名、性别、年龄、学历、月收入、现持有信用卡数量、是否有房、是否有车等信息，规则引擎先对申请人做合法性检查，通过后再根据规则确定信用卡额度，页面反馈"恭喜你，信用卡申请成功"加额度，或提示申请不通过的原因。

合法性检查规则共 4 条：

| 规则 | 名称 | 描述 |
| :--- | :--- | :--- |
| 1 | 检查学历与薪水1 | 既没房也没车，学历大专以下，月薪少于 5000，不通过 |
| 2 | 检查学历与薪水2 | 既没房也没车，学历大专或本科，月薪少于 3000，不通过 |
| 3 | 检查学历与薪水3 | 既没房也没车，学历本科以上，月薪少于 2000，且之前没有信用卡，不通过 |
| 4 | 检查已有信用卡数量 | 现持有信用卡数量大于 10，不通过 |

额度确定规则共 5 条，前提是合法性检查通过：

| 规则 | 描述 |
| :--- | :--- |
| 1 | 有房有车，或者月收入 20000 以上，额度 15000 |
| 2 | 没房没车，月收入 10000~20000，额度 6000 |
| 3 | 没房没车，月收入 10000 以下，额度 3000 |
| 4 | 有房没车或没房但有车，月收入 10000 以下，额度 5000 |
| 5 | 有房没车或没房但有车，月收入 10000~20000，额度 8000 |

实现依旧基于 Spring Boot 整合 Drools，工程名 creditCardApply。pom 坐标、application.yml（端口 8080、应用名 creditCardApply）、DroolsConfig 配置类都与个税案例一致；配置类里重点还是 KieBase——它直接注入给 service，而 KieBase 来自 KieContainer，KieContainer 又来自 KieRepository，一层套一层，应用直接打交道的只有 KieBase。规则文件路径同样指向 resources/rules，需要提前建好目录。

实体类 CreditCardApplyInfo 封装表单信息：name、education（学历）、telephone、monthlyIncome（月收入）、address、hasHouse（是否有房）、hasCar（是否有车）、hasCreditCardCount（现持有信用卡数量）；外加两个规则匹配后产生的结果字段：checkResult（审核是否通过，默认 true）和 quota（额度，默认 0）。重写的 toString 按 checkResult 分支：true 返回"审核通过，信用卡额度为 x"，false 直接返回"审核不通过"——额度只在审核通过后才有意义。

规则文件 creditCardApply.drl 共 9 条规则。合法性检查的 4 条全部设置 salience 100（额度规则优先级更低，保证检查类先执行）和 no-loop true。以第一条为例：

```java
rule "如果申请人既没房也没车，同时学历为大专以下，并且月薪少于5000，那么不通过"
    salience 100
    no-loop true
    when
        $c : CreditCardApplyInfo(hasHouse == false, hasCar == false,
                education == Education1, monthlyIncome < 5000)
    then
        $c.setCheckResult(false);
        drools.halt();
end
```

LHS 里逗号和 && 是一回事，多个条件直接并列即可；学历不用魔法数字，实体类里定义了常量（Education1 对应大专以下、Education2 大专、Education3 本科等），引用常量避免手写出错；规则 2 的"大专或本科"要用括号把 (education == Education2 || education == Education3) 组成一个大条件。所有检查规则的 then 部分相同：setCheckResult(false) 之后立刻调用内置对象方法 drools.halt() 终止规则引擎执行——审核都没通过，后面五条额度规则没有任何执行必要。规则 4 最简单，只看 hasCreditCardCount > 10 一个条件。额度确定的 5 条规则在下一篇继续实现。

## 小结

这一单元把 WorkBench 的用法真正闭环：部署产物是 Maven 仓库里的规则 jar 包，应用端用一段模板化代码（UrlResource + Basic 认证 + addKieModule + newKieContainer）远程加载即可触发规则，WorkBench 侧改规则重新部署，应用零改动拿到最新逻辑，"规则与业务分离"完整落地。个税计算器示范了规则文件的组织方式：三类规则、salience 定顺序、update 传递中间结果、no-loop 和 activation-group 兜底防错，Fact 对象承担 Java 与引擎之间的数据桥梁。信用卡申请完成了规则清单设计和工程骨架，合法性检查用 setCheckResult(false) 加 drools.halt() 短路整个引擎，额度规则的实现留待下一篇。
