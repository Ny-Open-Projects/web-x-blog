---
title: "Drools 实战收尾：信用卡申请额度规则实现与保险产品准入决策表"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 实战收尾：信用卡申请额度规则实现与保险产品准入决策表

信用卡申请案例在上一篇完成了合法性检查的 4 条规则，这一篇先把 5 条额度规则写完并跑通接口联调；随后进入第三个实战——保险产品准入规则，引出 Drools 的另一个重要形态：决策表（Decision Table），用 Excel 表格替代 DRL 文件来承载规则，最后以 11 条保险准入规则的完整落地收尾。

## 先给结论

- 5 条额度规则全部放进 activation-group "quota_group" 互斥组、salience 10 低于检查规则，且每条都以 checkResult == true 作为前置条件，保证"先检查、后定额度、额度只定一次"。
- checkResult 默认值设计为 true 是业务决定的：4 条检查规则任意一条命中就置 false 并 drools.halt()，全部未命中即为通过，默认 true 语义才成立。
- 决策表是 XLS 格式的规则文件，与 DRL 无缝替换、描述同一套条件逻辑；drools-decisiontables 依赖提供 SpreadsheetCompiler 把 Excel 编译成 DRL 字符串，KieHelper 再基于字符串建 KieSession。
- 决策表结构固定：RuleTable 行下面依次是 Condition/Action 关键字行、两行模式匹配（类型约束、属性约束）、一行被忽略的注释行，之后每行一条规则；占位符 $1、$2 按逗号分隔的顺序取该行单元格的值。
- 保险产品准入共 11 条规则（保险公司 PICC、区域北京天津、投保年龄 0~17 岁等），全部反向写成"不满足条件"，实体类 param1~param24 配注释弥补可读性。
- 判定逻辑是反向的：全局变量 listRules 为空（size 等于 0）即准入成功；只要有失败信息就是准入失败。改决策表里的指标值，程序不改、不重启，下次请求立即生效。

## 信用卡申请收尾：额度规则与接口联调

### checkResult 默认 true 的逻辑

4 条合法性检查规则任意一条匹配成功，then 部分都会把 checkResult 置为 false 并调用 drools.halt() 终止引擎；四条全部未命中，说明申请人不踩任何红线，就是审核通过。所以实体类里 checkResult 的默认值给 true 才符合业务——如果默认 false，"没触发任何检查规则"这种通过场景反而无法表达。

### 5 条额度规则

额度规则统一使用三个属性：salience 10（低于检查规则的 100，保证检查先执行）、no-loop true（防死循环习惯写法）、activation-group "quota_group"（组内互斥，最多一条触发）。互斥组在这里是防御性的：万一条件写得有重叠（既匹配上这条又匹配上下条），额度以哪条为准就成了隐患，加组之后最多触发一条。代表性规则如下：

```java
rule "如果申请人有房有车，或者月收入在20000以上，那么发放的信用卡额度为15000"
    salience 10
    no-loop true
    activation-group "quota_group"
    when
        $c : CreditCardApplyInfo(checkResult == true &&
            (hasCar == true && hasHouse == true) || monthlyIncome > 20000)
    then
        $c.setQuota(15000);
end

rule "如果申请人有房没车或者没房有车，月收入在10000~20000之间，那么发放的信用卡额度为8000"
    salience 10
    no-loop true
    activation-group "quota_group"
    when
        $c : CreditCardApplyInfo(checkResult == true &&
            ((hasHouse == true && hasCar == false) || (hasHouse == false && hasCar == true)) &&
            monthlyIncome >= 10000 && monthlyIncome <= 20000)
    then
        $c.setQuota(8000);
end
```

有房有车是一个大条件，必须用括号括起来再与"月收入 20000 以上"做或运算；"有房没车或没房有车"要拆成两组括号内的小条件再取或。每条规则的 LHS 都带 checkResult == true——审核不通过时确定额度毫无意义。5 条规则对应额度 15000、6000、3000、5000、8000，覆盖了房、车、收入的所有组合。设计时必须自查覆盖完整性：不能出现合法性检查通过了、五条额度规则却一条都没匹配上的情况，那说明规则设计有漏洞。

### 接口联调与验证

服务层与个税案例同一套路：注入 KieBase，creditCardApply 方法里 newKieSession → insert → fireAllRules → dispose → 返回同一个对象，规则内部 set 过的 checkResult、quota 在 Java 侧直接可读。控制器注意接收方式：前端提交的是 JSON，参数加 @RequestBody，由 Spring MVC 解析 JSON 并封装成 CreditCardApplyInfo。

```java
@PostMapping("/creditCardApply")
public CreditCardApplyInfo creditCardApply(@RequestBody CreditCardApplyInfo creditCardApplyInfo) {
    CreditCardApplyInfo result = ruleService.creditCardApply(creditCardApplyInfo);
    return result;
}
```

前端页面 creditCardApply.html 放入 resources/static：表单字段用 Vue 的 v-model 绑定到 creditCardApplyInfo 对象，学历、是否有房、是否有车是下拉框；申请按钮触发 axios.post('/rule/creditCardApply', this.creditCardApplyInfo)，回调里按 res.data.checkResult 分支，通过则显示"恭喜您信用卡申请成功，信用卡额度为 x"，否则显示审核未通过的提示。

启动后访问 localhost:8080/creditCardApply.html 实测（第一次误加了 /rule 前缀返回 404，去掉即可）：默认表单选了有房有车，额度直接 15000——因为"或"的关系月收入不用看；改有房没车、月收入留空（默认 0）→ 5000 档；月收入填 1000 仍是 5000；填 10000 命中 8000 档；没房没车且学历低命中 6000 档；再把月收入调低则合法性检查规则触发，返回审核不通过。组合方式很多不必逐一测，核心是验证规则设计合理、所有情况覆盖完整。

## 决策表：用 Excel 描述规则

保险产品准入案例引出新知识点——决策表。Drools 除了 DRL 文件还支持 XLS（Excel）格式的规则文件，通常称为决策表（Decision Table）：一种精确而紧凑的条件逻辑表示方式，非常适合商业级别的规则，与 DRL 文件可以无缝替换——两者描述的信息完全一样，类似同一个数据既可以用 JSON 也可以用 XML 表达。Drools 提供的 API 能把 XLS 文件编译成 DRL 格式的字符串再进行操作。

操作决策表需要 Maven 坐标 drools-decisiontables；如果只是简单应用不整合 Spring，只导这一个包即可，依赖传递会把 drools-core、drools-compiler、drools-templates 全带过来：

```xml
<dependency>
    <groupId>org.drools</groupId>
    <artifactId>drools-decisiontables</artifactId>
    <version>7.10.0.Final</version>
</dependency>
```

决策表的关键字与 DRL 概念一一对应：

| 关键字 | 对应 DRL | 说明 |
| :--- | :--- | :--- |
| RuleSet | package | 必须，只能一个；值可省略，省略用默认 rule_table |
| Sequential | 优先级 | 可选；true 按表格自上而下顺序执行，false 乱序，一般写 true |
| Import | import | 可选；多个类用逗号分隔，写在右侧单元格 |
| Variables | global | 可选；定义全局变量，多个用逗号分隔 |
| RuleTable | 规则名前缀 | 必须；值与关键字写在同一个单元格，如 "RuleTable personCheck" |
| Condition | when | 条件列 |
| Action | then | 动作列 |
| Agenda-Group | agenda-group | 议程组，组内规则只有获得焦点才能执行 |
| No-Loop | no-loop | 可选，防死循环 |

表格结构是定死的：RuleTable 往下第一行是 Condition、Action 等关键字行；第二、三行是 LHS 的模式匹配，第一行类型约束（如 PersonInfoEntity），第二行属性约束（如 sex != $1）；第四行相当于注释，随便写什么解析时都会被忽略；从第五行开始，每一行就是一条规则，只看有值的单元格，空单元格忽略。占位符 $1、$2（$ 符号加数字）用来替换每条规则里设置的具体值：某行年龄格写 "22,25"，则 age < $1 取 22、age > $2 取 25；Action 列的 $1 同理取该行的提示文字。

入门案例（女生找对象）不引 Spring，只导 junit 和 drools-decisiontables。决策表 testRule.xls：RuleSet rules，全局变量 List 类型的 listRules，Sequential true，import 实体类和 java.util.List，RuleTable personCheck；三个 Condition 分别约束 sex != $param、age < $param || age > $param、salary < $param，三个 Action 分别向 listRules 添加"性别不对""年龄不合适""工资太低了"，三条规则全归入 agenda-group "sign"（组名任意）。注意条件全是反向写的——写的都是"不满足要求"的情况（性别不是男、年龄小于 22 或大于 25、月薪低于 10000），任意一条成立就是不符合要求。

编译与执行的 API 很短：

```java
File file = new File("d:\\testRule.xls");
InputStream is = new FileInputStream(file);
SpreadsheetCompiler compiler = new SpreadsheetCompiler();
String drl = compiler.compile(is, InputType.XLS);   // 编译成 DRL 字符串
System.out.println(drl);

KieHelper kieHelper = new KieHelper();
kieHelper.addContent(drl, ResourceType.DRL);
KieSession session = kieHelper.build().newKieSession();
```

打印出的 drl 就是完整的规则文件内容，开头带注释 "generated from decision table"：RuleSet 变成 package，Variables 变成 global java.util.List listRules，Sequential true 让每条规则的 salience 从 65535 起依次递减（自上而下优先级），Import 生成两条 import，规则名 personCheck_10、personCheck_11 的前缀来自 RuleTable 的值，后缀数字对应规则所在的行号。测试时 new PersonInfoEntity（男、35 岁、月薪 1000）insert 进去，session.setGlobal("listRules", list)，再 session.getAgenda().getAgendaGroup("sign").setFocus()（用了议程组必须先获得焦点），fireAllRules 后遍历全局变量输出"年龄不合适""工资太低了"；把月薪调到 12000 只剩年龄不合适；年龄改 23 则完全无输出。把表格里的年龄上限从 25 改成 40，代码一行不动，再次执行年龄这条也不触发了——改表格立即生效。

再补一个扩展说明：一行规则上可以同时填多个条件值，比如同一行填"男""23,35""5000"，编译出的规则就会合并三个约束（sex != 男 && age < 23 || age > 35 && salary < 5000）；把某个单元格清空，对应条件就从规则里消失。

## 保险产品准入：11 条规则的决策表实战

保险行业的场景：各保险产品准入人群不同，保险公司会针对不同人群特征制定不同的交费和赔付规则，筛选出符合公司利益最大化的客户。某款产品的简化版准入规则共 11 条，不满足任意一条就返回准入失败标识和原因：

| 规则 | 要求 |
| :--- | :--- |
| 1 | 保险公司必须是 PICC（中国人保） |
| 2 | 销售区域仅北京、天津 |
| 3 | 投保人年龄 0~17 岁 |
| 4 | 保险期间仅 20 年、25 年、30 年三选 |
| 5 | 交费方式为趸交（一次性交清）或年交 |
| 6 | 保险期 20 年：交费期间最长 10 年，且不能趸交 |
| 7 | 保险期 25 年：交费期间最长 15 年，且不能趸交 |
| 8 | 保险期 30 年：交费期间最长 20 年，且不能趸交 |
| 9 | 投保年龄 + 保险期间不得大于 40 周岁 |
| 10 | 保额最低 5 万元，超过部分必须为 1000 元整数倍 |
| 11 | 线上出单基本保额限额 62.5 万元，超出需转线下出单 |

真实产品的规则会远多于 11 条，这里只是简化版。规则文件这次直接用 Excel 决策表：业务人员直接改文件里的指标值（北京、天津、年龄范围这些可配置的具体值），系统不需要任何变更，这正是决策表的核心好处。

工程 insuranceInfoCheck 基于 Spring Boot 整合 Drools。pom 里重点坐标是 kie-spring——导入它时会把 drools-decisiontables 传递进来，无需再显式导入。application.yml 仍是端口 8080 加应用名。实体类 InsuranceInfo 用 param1 到 param24 共 24 个属性封装保险信息：param1 保险公司、param2 方案代码、param3 渠道号、param4 销售区域、param5 投保年龄、param6 保险期间、param7 交费期间、param8 交费方式、param9 保障类型、param10 等待期、param11 犹豫期……编号命名可读性差，注释就必须写清楚。

决策表文件 insuranceInfoCheck.xls 由资料提供， Drools 解析 Excel 默认只解析第一个标签页，真正有用的内容必须放在第一个 sheet。结构上：RuleSet rules，Variables 定义 List 类型全局变量 listRules，import InsuranceInfo、List、ArrayList 三个类，RuleTable insurance-rules；Condition 有 11 个（条件维度 11 个），类型约束都是 InsuranceInfo，属性约束全部反向：param1 != $1（值 PICC，保险公司不对即准入失败）、param4 != $1 && param4 != $2（值北京、天津）、投保年龄用 Integer.parseInt(param5) 做数值比较，等等；11 条规则全归入 agenda-group "sign"；Action 统一向 listRules 添加失败原因，如"保险公司不正确""销售区域不正确，仅支持北京和天津"。

Java 侧把入门案例的 API 封装成工具类 KieSessionUtils：私有构造防止实例化；getDRL(realPath) 读磁盘 Excel 编译成 DRL 字符串；createKieSessionFromDRL(drl) 里比入门案例多了一步 verify 校验——转换出来的 DRL 可能有语法问题，先校验再建 session，失败就打印错误信息并抛异常；对外直接调 getKieSessionFromXLS(realPath) 一步到位。RuleService.insuranceInfoCheck(InsuranceInfo) 返回 List<String>：Excel 路径这里写死在磁盘根目录（真实项目应做成可配置），通过工具类拿 session，setFocus 让 sign 组获得焦点，insert 实体，setGlobal 设置 listRules，fireAllRules 后 dispose 并返回全局变量。

判定逻辑一定要捋清楚：规则条件全是反向写的"准入失败条件"，所以 listRules 的 size 等于 0（一条都没匹配上）才是准入成功，size 大于 0 就是准入失败。控制器没有做专门页面，用模拟数据构造 InsuranceInfo（param1 picc、param4 上海、param5 101 等，真实场景这些值来自页面提交），调 service 后按返回的 list 组装 Map：非空则 checkResult false、msg 准入失败、detail 放失败明细；空则 checkResult true、msg 准入成功；异常时 msg 未知错误。@RestController 会把 Map 转成 JSON 写回浏览器。

启动访问 localhost:8080/rule/insuranceInfoCheck，返回准入失败，detail 里有"销售区域不正确，仅支持北京和天津""投保年龄在0到17岁之间"——模拟数据填的上海和 101 岁确实踩线。现在想让上海也支持：不改任何代码，直接改决策表，在销售区域格子里加上"上海"，并在属性约束里补一段 param4 != $param（占位符对应新加的取值），保存后项目不重启直接重新请求，销售区域那条失败信息消失；再把年龄格子里的上限改成 102 保存重试，年龄那条也没了。指标值一改规则立即生效，程序零修改零重启，这就是决策表在商业规则场景下的价值。

## 小结

信用卡申请案例至此闭环：5 条额度规则用 activation-group 互斥、checkResult 前置过滤，配合 @RequestBody 接口和 Vue 页面完成了从表单到额度的全链路验证。决策表是这一单元真正的新东西——它把规则从 DRL 文本搬进 Excel：RuleSet/Sequential/Import/Variables/RuleTable 与 DRL 关键字一一映射，Condition/Action 两行模式匹配加占位符替换，SpreadsheetCompiler 编译成 DRL 字符串后由 KieHelper 建 session 执行，整条链路对 Java 侧几乎无感知。保险产品准入用 11 条反向规则验证了这套玩法的工程价值：业务人员维护表格里的指标值，失败原因通过议程组和全局变量回传，规则变更不碰代码、不重启服务。至此 Drools 的三种用法——本工程 DRL、WorkBench 远程规则、Excel 决策表——全部走通。
