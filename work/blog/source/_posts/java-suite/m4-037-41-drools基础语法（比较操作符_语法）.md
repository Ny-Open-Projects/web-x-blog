---
title: "Drools 语法进阶：十二种比较操作符、执行指定规则与 update/insert/retract 内置方法"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 品达物流TMS]
tags: [Java, 项目实战, Drools]
---

# Drools 语法进阶：十二种比较操作符、执行指定规则与 update/insert/retract 内置方法

上篇搭起了规则文件的骨架：规则体结构、注释与"绑定变量名: 类型(Field约束)"的模式匹配。本篇继续在语法层面推进——模式匹配里能用的十二种比较操作符、只让某条规则触发的 AgendaFilter 过滤器、硬软两类关键字，以及 RHS 里最关键的 update/insert/retract 三个内置方法。最后这一组方法是规则"连锁反应"的开关，也是规则引擎区别于一次性 if-else 判断的关键。

## 先给结论

- 比较操作符共十二个：>、<、>=、<=、==、!= 前六个与 Java 含义用法完全一致；重点是后六个，且两两成对取反——contains/not contains、memberOf/not memberOf、matches/not matches。
- contains 与 memberOf 方向相反：contains 说的是"前面的属性值包含后面指定的值"，memberOf 说的是"前面的属性值是后面集合的一个成员"，即后面的集合包含前面的值。
- matches 后面跟的是标准 Java 正则表达式，例如 `names matches "王.*"` 表示必须是以王开头的名字。
- 只想执行指定规则时规则文件不用动，改 Java 代码即可：`fireAllRules(AgendaFilter)`；AgendaFilter 是接口，常用实现有 RuleNameEqualsAgendaFilter、RuleNameStartsWithAgendaFilter、RuleNameEndsWithAgendaFilter、RuleNameMatchesAgendaFilter。指定了名称也不代表一定触发，前提仍是匹配成功。
- Drools 关键字分两类：硬关键字 true、false、null 不能用作包名或规则名，不加引号直接报 `Parser returned a null Package`；软关键字可用但不建议用，很多正是后面的规则属性名。
- RHS 内置方法三件套：update 更新、insert 插入、retract 删除工作内存中的 Fact 对象，共同效果是让相关规则重新匹配——原先匹配不上的规则可能被连锁触发；update 要防死循环，retract 的先后顺序靠 salience 优先级保证。

## 比较操作符：前六个照搬 Java，后六个才是重点

模式匹配的属性约束里其实已经用过了比较操作符——入门案例的 `originalPrice >= 100 && originalPrice < 200` 就是。这里系统梳理一下，Drools 提供的比较操作符共十二个：

| 操作符 | 说明 |
| --- | --- |
| > / < / >= / <= | 大于 / 小于 / 大于等于 / 小于等于，与 Java 一致 |
| == | 等于，注意是两个等号 |
| != | 不等于 |
| contains | 检查一个 Fact 对象的某个属性值是否包含一个指定的对象值 |
| not contains | 检查一个 Fact 对象的某个属性值是否不包含一个指定的对象值 |
| memberOf | 判断一个 Fact 对象的某个属性值是否在一个或多个集合中 |
| not memberOf | 判断一个 Fact 对象的某个属性值是否不在一个或多个集合中 |
| matches | 判断一个 Fact 对象的属性是否与提供的标准 Java 正则表达式匹配 |
| not matches | 与 matches 取反，不匹配时条件成立 |

前六个写法和 Java 完全一样，不必再看；后六个成对出现、两两取反，语法结构是：

```java
Object(field contains value)          // field 往往是集合或数组类型
Object(field memberOf value)          // value 往往是集合或数组类型
Object(field matches "正则表达式")
```

contains 和 memberOf 长得很像，方向是反的：contains 是前面的属性值包含后面的值；memberOf 是前面的属性值作为成员被后面的集合包含。not 版本只是在前面加一个 not（memberOf 中间有空格，别连着写）。

### contains / not contains 实操

先建一个测试实体 ComparisonOperatorEntity，作用类似入门案例的 Order——把原始数据传进工作内存。两个属性就够测完全部操作符：`names`（String）和 `list`（List<String>），补上 getter/setter。

规则文件建议按类分。所有规则写进一个文件语法上是允许的，bookDiscount.drl 的四条图书优惠规则就属于同一类业务；现在测的是比较操作符，属于另一类，新建 comparisonOperator.drl 更清晰：

```java
package comparisonOperator
import com.itheima.drools.entity.ComparisonOperatorEntity

// 测试比较操作符 contains
rule "rule_comparison_contains"
    when
        ComparisonOperatorEntity(names contains "张三")
        ComparisonOperatorEntity(list contains names)
    then
        System.out.println("规则: rule_comparison_contains触发了...");
end
```

上下两个 Pattern 没写连接词，默认就是 and，必须同时成立规则才触发。绑定变量名这里省略了——它是可选的，RHS 用不到对象引用就可以不写，要用就必须写。IDEA 的 Drools 插件对属性名有提示，但 contains 这类关键字提示不出来，只能手敲，敲完会变色。

测试代码还是模板五步，Fact 换个类型：

```java
ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
fact.setNames("张三");
List<String> list = new ArrayList<String>();
list.add("张三");
fact.setList(list);
session.insert(fact);
session.fireAllRules();
session.dispose();
```

演示分几步走：对象什么值都不设，names 是空，控制台无任何输出——编写了规则不代表会执行，必须先匹配成功；只设 names="张三"，第一个条件成立但 `list contains names` 不成立，仍然不触发；再把 list 里 add 一个"张三"并 setList 进去，规则触发。中间还踩了个典型坑：new 了 ArrayList 却忘记 fact.setList(list)，新 list 和 fact 对象没有任何关系，规则照样不动。

not contains 在两个条件前各加一个 not。把 names 改成"李四"、list 里的元素也改成不含 names 的值，rule_comparison_notcontains 就触发了。

### memberOf / matches 实操

memberOf 的规则结构相同，条件换成 `ComparisonOperatorEntity(names memberOf list)`——names 必须是 list 集合里的一个成员。names="李四"、list 只有"张三"时不触发；往 list 里 add 一个"李四"，规则触发。not memberOf 反过来：把李四从 list 里去掉，names 不再是集合成员，规则触发。

这一轮测试还能直观看到一个现象：一次 fireAllRules 可以同时触发多条规则，只要都匹配成功，not contains、not memberOf 的输出会一起出现在控制台，并不是只有一条规则能执行。

matches 后面跟正则表达式：

```java
// 测试比较操作符 matches
rule "rule_comparison_matches"
    when
        ComparisonOperatorEntity(names matches "王.*")
    then
        System.out.println("规则: rule_comparison_matches触发了...");
end
```

"王.*" 表示姓王的名字。names="李四" 时匹配不上；改成"王四"，第一个字是王，规则触发。not matches 与它正好相反：王四时它不成立，改回李四它就成立。六个新操作符都不难，核心是记住成对取反。

## 执行指定规则：AgendaFilter 过滤器

前面的案例里，满足条件的规则全会被执行——一次触发了三条。如果只想执行其中某一条，Drools 提供的方式是规则过滤器：规则文件不做任何修改，只改 Java 代码。

fireAllRules 有带参重载，参数是 AgendaFilter。Agenda 就是之前讲执行过程时的"议程"，存放匹配成功、待执行的规则；过滤器决定议程里的哪些规则真正放行。它是一个接口，需要传实现类：

```java
public interface AgendaFilter {
    boolean accept(Match match);
}
```

实现类不少，从命名就能看出过滤逻辑：

| 实现类 | 过滤逻辑 |
| --- | --- |
| RuleNameEqualsAgendaFilter | 规则名等于指定字符串 |
| RuleNameStartsWithAgendaFilter | 规则名以指定字符串开始 |
| RuleNameEndsWithAgendaFilter | 规则名以指定字符串结束 |
| RuleNameMatchesAgendaFilter | 规则名匹配正则表达式 |

用 RuleNameEqualsAgendaFilter 验证：不加过滤时三条规则都触发；换成

```java
session.fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"));
```

就只有这一条触发——即便其他规则也匹配成功，被过滤器拦下不会执行。再换 RuleNameStartsWithAgendaFilter 按"rule"前缀过滤，三条又都触发；把其中两条规则的名称改掉、破坏前缀，就只剩一条。要强调的是：指定了名称也不代表一定触发，前提仍是这个规则能匹配成功，两者缺一不可。

## 关键字：三个硬关键字与一串软关键字

Java 有关键字，规则文件里也有，分成两类：

| 类别 | 成员 | 约束 |
| --- | --- | --- |
| 硬关键字 | true、false、null | 定义包名或规则名时不能使用，否则程序报错 |
| 软关键字 | lock-on-active、date-effective、date-expires、no-loop、auto-focus、activation-group、agenda-group、ruleflow-group、entry-point、duration、package、import、dialect、salience、enabled、rule、when、then、end、query、declare、function、global、eval、not、in、or、exists、forall、accumulate、collect、from 等 | 可以使用，但不建议——其中很多正是规则属性名 |

拿硬关键字演示。写成 `rule "true"`——名称在双引号里，整个字符串是规则名，没问题，单元测试照常通过。去掉引号写成 `rule true`，规则文件校验时直接报错，执行单元测试抛异常：

```
java.lang.RuntimeException: Error while creating kieBase
...
Message [id=2, kieBase=myKbase, level=ERROR, text=Parser returned a null Package]
```

换成 null 同样不行。反过来，名称不是硬关键字时引号可以去掉，但中间不能有空格（用下划线连成整体），这种写法也能正常执行。不过强烈建议规则名始终带双引号：写法规范，IDE 能把引号里的内容识别成一个整体，里面带空格都没问题。

## 内置方法：update / insert / retract 与规则重新匹配

规则文件的 RHS 部分（then 到 end 之间），主要作用是通过插入、删除或修改工作内存中的 Fact 对象来控制规则引擎的执行。Drools 为此提供了三个内置方法：

| 方法 | 作用 |
| --- | --- |
| update(object) | 更新工作内存中的数据，并让相关的规则重新匹配 |
| insert(object) | 向工作内存中插入数据，并让相关的规则重新匹配 |
| retract(object) | 删除工作内存中的数据，并让相关的规则重新匹配 |

共同点是"让相关规则重新匹配"：操作完成后，原先没匹配成功的规则有可能匹配成功进而执行。测试实体换成 Student（id、name、age 三个属性），规则文件 student.drl 集中放这几条规则：

```java
package student
import com.itheima.drools.entity.Student

// 测试 retract 内置方法
rule "要求Student的age等于10岁用于删除"
    salience 10
    when
        $s:Student(age == 10)
    then
        retract($s);
        System.out.println("规则: 要求Student的age等于10岁用于删除触发了...");
end

// 测试 insert 内置方法
rule "要求Student的age等于10岁"
    when
        $s:Student(age == 10)
    then
        Student s = new Student();
        s.setAge(5);
        insert(s);
        System.out.println("规则: 要求Student的age等于10岁触发了...");
end

// 测试 update 内置方法
rule "要求Student的age小于10岁"
    when
        $s:Student(age < 10)
    then
        $s.setAge(15);
        update($s);
        System.out.println("规则: 要求Student的age小于10岁触发了...");
end

rule "要求Student的age大于10岁并且小于20岁"
    when
        $s:Student(age > 10 && age < 20)
    then
        $s.setAge(25);
        update($s);
        System.out.println("规则: 要求Student的age大于10岁并且小于20岁触发了...");
end

rule "要求Student的age大于20岁"
    when
        $s:Student(age > 20)
    then
        System.out.println("规则: 要求Student的age大于20岁触发了...");
end
```

**update 的演示最能说明"重新匹配"的价值。** 单元测试里 `student.setAge(5)` 后 insert、fireAllRules。先不写 update：只有"age小于10岁"这条规则触发。setAge(15) 不是已经满足第二条规则了吗？没有触发——匹配发生在调用 fireAllRules 的时候，匹配成功的规则放进议程；执行阶段只跑议程里的规则，数据被改了但没有重新匹配，第二条规则根本进不了议程。在 `$s.setAge(15);` 后面加上 `update($s);`，效果立变：update 更新 Fact 对象并导致相关规则重新匹配，第二条规则匹配成功执行；它里面再 setAge(25) 加 update，连锁到"age大于20岁"那条。三条规则像多米诺一样依次触发。代价也要清楚：这种连锁可能转成死循环，编写规则文件时必须注意防范。

**insert 是往工作内存里塞新 Fact。** 把测试数据的 age 设成 10，"age等于10岁"这条规则触发；它的 then 里 new 了一个 age=5 的新 Student 并 `insert(s)` 插入工作内存——注意新对象是局部变量 s，与绑定变量 $s 指向的原对象不是一回事。插入完成后相关规则重新匹配，age=5 的新 Fact 命中"age小于10岁"，再经 update 连锁，最终所有规则都执行到。

**retract 是把 Fact 从工作内存里删掉。** "用于删除"那条与 insert 规则的条件完全一样（都是 age == 10），规则名不能相同。两个条件相同的规则，怎么保证删除规则先执行？靠规则属性 salience——执行优先级，数值越大越优先，默认 0；不指定时优先级相同，按规则文件里的上下顺序执行。这里显式给 salience 10 更明确。age=10 时：删除规则先触发，retract 把这个 Fact 移出工作内存，后面那条 age==10 的规则重新匹配时已经找不到对象，不会触发——控制台只有删除规则的输出。把 retract 注释掉再跑：对象还在，后面规则也匹配到并执行，insert 又插入新对象，一连串连锁反应，所有规则全部触发。

## 小结

本篇把 Drools 基础语法收尾。十二种比较操作符里，前六个照搬 Java，后六个成对取反：contains/not contains 看属性值是否包含指定值，memberOf/not memberOf 看属性值是否为集合成员，matches/not matches 对标准 Java 正则——contains 与 memberOf 记住方向相反就不易混。执行指定规则靠 AgendaFilter 过滤器，规则文件零改动，只在 fireAllRules 时传入 RuleNameEquals/StartsWith/EndsWith/Matches 等实现，但指定名称不等于必然触发，匹配成功仍是前提。关键字分硬软：true/false/null 三个硬关键字不能用作包名和规则名，软关键字多为规则属性名、可用不建议用。三个内置方法是本篇的重心：update 更新、insert 插入、retract 删除工作内存中的 Fact，都会让相关规则重新匹配，由此产生了"age 从 5 到 15 到 25"这样的规则连锁——RHS 的改动会反哺匹配过程，工作内存因此是"活"的。salience 优先级在这里初次露面，它的完整用法以及十个规则属性、SpringBoot 整合、订单计价落地，留给下一篇。
