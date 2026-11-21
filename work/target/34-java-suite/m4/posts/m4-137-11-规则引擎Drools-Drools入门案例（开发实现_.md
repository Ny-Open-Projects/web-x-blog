---
title: "Drools 入门收官：跑通单元测试、规则引擎构成与基础语法上半"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 入门收官：跑通单元测试、规则引擎构成与基础语法上半

上篇把入门案例的地基打完了：Maven 工程、kmodule.xml、Order 实体类和 bookDiscount.drl 四条图书优惠规则都已就位。本篇把最后一步补上——编写单元测试，看规则引擎怎么把优惠后的价格算出来并传回应用；然后集中补齐入门案例里没细讲的三个概念：规则引擎的构成与执行过程、KIE 体系，最后进入基础语法上半场：规则文件构成、规则体语法、注释与模式匹配。

## 先给结论

- 单元测试六步固定套路：`KieServices.Factory.get()` → `newKieClasspathContainer()` → `newKieSession()` → `insert` 事实对象 → `fireAllRules()` → `dispose()`；前三步全是模板化代码，和 JDBC 一个性质，与规则引擎交互主要靠 KieSession。
- 计算结果不靠返回值传回：insert 进工作内存的对象，规则文件里改的就是同一个引用。fireAllRules 之前取 realPrice 是 null，规则触发之后才能从 order 对象上拿到优惠后的价格——Fact 对象就是应用与规则引擎数据交互的桥梁。
- Drools 规则引擎由三部分构成：Working Memory（工作内存）存 Fact 对象、Rule Base（规则库）存规则、Inference Engine（推理引擎）负责推理；推理引擎内部又分匹配器、议程、执行引擎。
- 执行过程五步循环：输入 fact 到工作内存 → 匹配器把规则库中的规则和 fact 比较 → 同时激活多个规则时冲突进冲突集合 → 解决冲突后按顺序放入议程 → 执行议程中的规则并重复，直到全部执行完毕；冲突由引擎内部自动解决，不用开发者管。
- KIE 全称 Knowledge Is Everything（知识就是一切），是 JBoss 一系列项目的总称，Drools 只是这套体系下的一个组件；核心 API 类几乎都以 Kie 开头，Drools 还自带 Drools-WB 可视化规则编辑器。
- 基础语法上半：规则文件由 package、import、global、function、query、规则体六类构成；规则体是 rule + 属性（可选）+ when（LHS）+ then（RHS）+ end；LHS 里的条件又称 Pattern，语法是"绑定变量名: 类型(Field 约束)"，多个 Pattern 之间默认 and 连接。

## 单元测试：六步跑通规则引擎

在 test 目录下新建 DroolsTest 类，加 @Test 注解。代码怎么写完全对着前面讲过的 API 开发步骤来，六步一个不落：

```java
@Test
public void test1() {
    // 1. 获取 KieServices 对象（注意类名带 s，靠 Factory 获取，不是 new）
    KieServices kieServices = KieServices.Factory.get();

    // 2. 获取 KieContainer 容器对象，框架会到 rules 目录下加载所有规则文件
    KieContainer kieContainer = kieServices.newKieClasspathContainer();

    // 3. 从容器中获取会话对象
    KieSession session = kieContainer.newKieSession();

    // 4. 创建 Fact 对象（事实对象），只需要设置原始价格
    Order order = new Order();
    order.setOriginalPrice(500D);

    // 5. 将 Fact 对象插入到工作内存中
    session.insert(order);

    // 6. 激活规则，由 Drools 框架自动进行规则匹配，匹配成功则执行当前规则
    session.fireAllRules();

    // 关闭会话
    session.dispose();
    System.out.println("优惠后价格：" + order.getRealPrice());
}
```

几个容易踩的点。第一步获取 KieServices，注意类名是带 s 的那个，别找错了；它不是 new 出来的，而是通过 `KieServices.Factory.get()` 拿到，这是固定写法。第二步拿 KieContainer 用的是 `newKieClasspathContainer()`，因为规则文件放在 resources/rules 下面，框架会自动到 rules 目录加载全部规则。第三步拿 session 之所以可以不指定名称，是因为 kmodule.xml 里把这个 ksession 配成了 default——并不是所有情况下都能这样直接获取，前提就是配置文件里确实有这个默认会话。

中间的业务数据部分：new 一个 Order，只设置原始价格，double 类型记得加 d；realPrice 不用设置，因为使用 Drools 的目的就是让它帮我们计算最终价格。设置完通过 `session.insert(order)` 插入工作内存——工作内存是规则引擎里的一块内存区域，插进去的对象在 Drools 里有个专属名字，叫 Fact 对象，翻译过来就是事实对象。

`fireAllRules()` 是触发开关：不管有多少条规则整体激活一遍，看传进去的对象到底能匹配上哪条，匹配成功就执行那条规则的 then 部分。最后 `session.dispose()` 关闭会话，注意方法名是 dispose，不是 close。

跑起来验证两种情况。原始价格 50，命中规则一，无优惠；原始价格 500，命中规则四，减 100，优惠后 400。有意思的是结果怎么传回来的：在 fireAllRules 之前先输出一次 `order.getRealPrice()`，得到的是 null，因为 new 对象时确实没设置；规则触发之后再取，值就有了。规则文件里 `$order.setRealPrice(...)` 修改的那个 `$order`，指向的就是我们传进去的同一个 Order 对象，规则引擎不通过返回值反馈结果，而是通过这个对象引用——insert 什么进去，规则改的就是什么，应用再从同一个对象上取值。

## 规则引擎的构成与执行过程

案例跑通之后有个疑问值得正面回答：代码里确实没写 if-else 了，可规则文件里描述的不还是这些判断逻辑吗？无非是把 Java 代码里的逻辑挪到了 DRL 文件里，有什么本质区别？

区别在于规则可以动态管理。把 if-else 这些判断逻辑单独抽到规则文件里之后，可以把规则看成数据，像管理数据一样查询规则、添加规则、更新规则，从而做到在不重启服务器的情况下调整业务规则。类比很直接：早年用 JDBC 时 SQL 全写死在 Java 代码里，调整起来很不方便，后来 MyBatis 把 SQL 抽到 XML 里统一配置；规则引擎干的是同一类事，只不过抽出来的不是 SQL，而是散落在代码里的业务规则，并且配套了动态管理的 API。

这个入门案例里其实已经接触了规则引擎的全部构件。Drools 规则引擎由三部分构成：

| 构成 | 作用 |
| --- | --- |
| Working Memory（工作内存） | 存放 Fact 对象的内存区域，insert 方法插入的就是这里；模式匹配时引擎从这里取数据 |
| Rule Base（规则库） | 存放编写好的业务规则，程序运行时规则文件里的规则被加载到这里；可以简单想象成内存中的数据库 |
| Inference Engine（推理引擎） | 具有模式匹配、执行、推理功能，内部又分三部分 |

推理引擎内部的三部分串起了整个执行链路：匹配器（Pattern Matcher）负责模式匹配，它从工作内存里把 Fact 对象取出来，再从规则库把规则取出来逐一比较——originalPrice 是 500 时，规则一、二、三都不满足，规则四匹配成功；匹配成功的规则会被放入议程（Agenda），议程里存放的都是将要执行的规则；最后由执行引擎（Execution Engine）执行议程中的规则。

把链路整理成执行过程，就是五步循环：

1. 将初始数据（fact）输入至工作内存；
2. 使用匹配器将规则库中的规则和工作内存中的数据比较；
3. 如果执行规则存在冲突（同时激活了多个规则），将冲突的规则放入冲突集合；
4. 解决冲突，将激活的规则按顺序放入议程；
5. 执行议程中的规则，重复第 2 至第 5 步，直到议程中的所有规则执行完毕。

第 3、4 步的冲突不需要自己处理：匹配时 Fact 对象多、规则也多，难免同时激活很多规则，引擎内部会自动解决冲突，再按顺序放进议程。

## KIE：Drools 所属的体系

操作 Drools 时接触到的核心 API，除了已经用过的 KieServices、KieContainer、KieSession，还有 KieRepository、KieBase、KieProject 等，大部分类名都以 Kie 开头。这门技术的类名、接口名、包名命名都很规范，不会随便起名，这个 Kie 必然有讲究。

KIE 全称 Knowledge Is Everything，翻译过来是"知识就是一切"，它是 JBoss 一系列项目的总称，如今已经形成一套体系，Drools 只是 KIE 体系下的一个组件。KIE 的主要模块包括 OptaPlanner、Drools、UberFire、jBPM——jBPM 是 JBoss 的工作流框架，同样属于 KIE 系列；Drools 下还包含一个 Drools-WB 模块（WB 即 Workbench），是一个可视化的规则编辑器，课程后面会专门讲。

这个关系类似 SpringData：SpringData 是 Spring 框架下专注于数据存取方向的项目群，下面又细分成 Spring Data JPA、Spring Data Redis、Spring Data ES、Spring Data JDBC 等子项目。KIE 是系列总称，Drools 是其中的组件，Drools 核心 API 都以 Kie 命名，也正是这个家族归属的体现。

## 基础语法上半：规则文件、规则体、注释与 Pattern

### 规则文件由什么构成

使用 Drools 时最重要的工作就是编写规则文件，通常后缀是 drl——它是 Drools Rule Language（Drools 规则语言）的缩写。除了 drl 文件形式，Drools 还支持 Excel 文件形式的规则，不过课程主要用 drl。一套完整的规则文件由以下关键字构成：

| 关键字 | 描述 |
| --- | --- |
| package | 包名，只限于逻辑上的管理，同一个包名下的查询或函数可以直接调用；规则文件必须有 package |
| import | 用于导入类或者静态方法 |
| global | 全局变量 |
| function | 自定义函数 |
| query | 查询 |
| rule end | 规则体，规则文件中最重要的部分 |

package 的"逻辑管理"要特别强调：它只是个逻辑概念，不要求和规则文件实际所在的目录对应——这点和 Java 类的 package 必须与目录完全一致不一样。入门案例里第一行 `package book.discount`，第二行 `import com.itheima.drools.entity.Order`，把要用到的实体类导入进来。

### 规则体语法结构

规则体是规则文件中进行业务规则判断、处理业务结果的部分，语法结构是一个固定模板：

```java
rule "ruleName"
    attributes
    when
        LHS
    then
        RHS
end
```

rule 关键字表示规则开始，后面跟规则名称；attributes 是规则属性，写在 rule 与 when 之间，是可选的——入门案例里定义完规则名就直接写 when 了，规则属性一共有十个，后面会专门讲，全都出现在这个部分。

when 后面跟规则的条件部分，统称 LHS（Left Hand Side，左手边），由零个或多个条件元素构成。LHS 可以为空，为空则被视为始终为 true 的条件元素——意味着这条规则不管什么情况都会触发。then 后面跟规则的结果部分，统称 RHS（Right Hand Side，右手边），是规则的后果或行动部分的通用名称；end 表示一个规则结束。

### 注释

规则文件里可以写注释，分单行和多行两种，用法与 Java 完全一致：单行用两个斜线 `//`，多行以 `/*` 开始、以 `*/` 结束，中间可以写多行。入门案例规则文件里"所购图书总价在100元以下的没有优惠"这类说明，用的就是单行注释。

### Pattern：条件就是模式

前面说过匹配器会把规则库中的规则和工作内存中的 Fact 对象进行模式匹配，而匹配的定义就写在 LHS 里。LHS 由一个或多个条件组成，条件又可以称为 Pattern。它的语法结构是：

```java
绑定变量名: Object(Field约束)
```

对照入门案例规则二：`$order: Order(originalPrice < 200 && originalPrice >= 100)`。

`$order` 是绑定变量名，名字可以任意起，不是必须叫这个，官方建议用 $ 开头；它不是必须的，可以省略，但通常要写——因为一般要在 then 部分通过这个变量名来修改 Fact 的值，要用它就得先绑定。`Order` 是对象类型，称为类型约束，要求匹配的对象必须是 Order 类型。括号里的 `originalPrice < 200 && originalPrice >= 100` 是 Field 约束（属性约束），要求返回 true 或 false 的零个或多个表达式——可以不写，但要写就必须是布尔表达式，不能返回其他值。

这样规则二的匹配条件就是三个，必须同时满足，规则才有可能被激活：工作内存中必须存在 Order 类型的 Fact 对象（类型约束）；对象的 originalPrice 必须小于 200；originalPrice 必须大于等于 100。只有被激活的规则才有可能被执行。

绑定变量既可以用在对象上，也可以用在对象的属性上：

```java
rule "book_discount_2"
    when
        $order: Order($op: originalPrice < 200 && originalPrice >= 100)
    then
        System.out.println($op);
        $order.setRealPrice($order.getOriginalPrice() - 20);
        System.out.println("成功匹配到规则二");
end
```

这里的 `$op` 就是属性 originalPrice 的绑定变量，规则触发时在 RHS 里可以直接使用它。

LHS 还可以定义多个 Pattern，多个条件之间用 and 或 or 连接，不写的话默认就是 and：

```java
rule "book_discount_2"
    when
        $order: Order($op: originalPrice < 200 && originalPrice >= 100) and
        $customer: Customer(age > 20 && gender == 'male')
    then
        $order.setRealPrice($order.getOriginalPrice() - 20);
        System.out.println("成功匹配到规则二");
end
```

两个 Pattern 用 and 相连，意味着规则要触发必须两个大条件同时满足：既有价格区间符合的 Order，又有年龄大于 20 且性别为 male 的 Customer；换成 or 则只要满足其中一个。

## 小结

本篇收掉了入门案例的尾巴。单元测试六步：KieServices、KieContainer、KieSession、insert 事实对象、fireAllRules 激活规则、dispose 关闭会话，结果通过对象引用传回，规则触发前后取 realPrice 分别是 null 和优惠后的值。规则引擎由工作内存、规则库、推理引擎构成，推理引擎内部是匹配器、议程、执行引擎，执行过程五步循环、冲突自动解决。把规则抽到规则文件的真正价值是像管理数据一样动态管理规则，不重启服务即可调整——这也是它与"换个地方写 if-else"的本质区别。KIE（Knowledge Is Everything）是 JBoss 项目群总称，Drools 是其中一个组件。基础语法上半讲完规则文件六类构成、规则体 rule-when-then-end 模板、Java 风格的注释，以及"绑定变量名: 类型(Field 约束)"的 Pattern 匹配。下一篇进入基础语法下半：比较操作符全集、执行指定规则与 RHS 内置方法。
