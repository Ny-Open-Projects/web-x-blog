---
title: "Drools 语法下半：六个特殊比较操作符、执行指定规则与 update/insert/retract 内置方法"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 语法下半：六个特殊比较操作符、执行指定规则与 update/insert/retract 内置方法

上篇收掉了入门案例，并讲完基础语法上半场：规则文件构成、规则体模板、注释和"绑定变量名: 类型(Field 约束)"的模式匹配。本篇进入语法下半场：模式匹配里真正好用的比较操作符、只想让某条规则触发时怎么用过滤器指定执行、规则文件里哪些名字不能用，以及 RHS 部分最能体现规则引擎特色的三个内置方法——它们让"改数据触发重新匹配"成为可能，也是规则连锁反应的开关。

## 先给结论

- 比较操作符共十二个：>、<、>=、<=、==、!= 前六个与 Java 含义用法完全一致；重点是后六个，且两两成对取反——contains/not contains、memberOf/not memberOf、matches/not matches。
- contains 与 memberOf 方向相反：contains 是前面的属性值包含后面指定的值，memberOf 是前面的属性值作为成员被后面的集合包含；写 not 时 memberOf 中间有空格，别连着写。
- matches 后面跟的是标准 Java 正则表达式，例如 `names matches "王.*"` 表示必须是以王开头的名字。
- 只想执行指定规则时规则文件不用动，改 Java 代码即可：`fireAllRules(AgendaFilter)`；AgendaFilter 是接口，常用实现有 RuleNameEqualsAgendaFilter、RuleNameStartsWithAgendaFilter、RuleNameEndsWithAgendaFilter、RuleNameMatchesAgendaFilter。指定了名称也不代表一定触发，前提仍是匹配成功。
- Drools 关键字分两类：硬关键字 true、false、null 不能用作包名或规则名，不加引号直接在规则文件校验阶段报错，执行单元测试同样报错；软关键字可以用但不建议，很多正是后面的规则属性名。
- RHS 内置方法三件套：update 更新、insert 插入、retract 删除工作内存中的 Fact 对象，共同效果是让相关规则重新匹配——原先匹配不上的规则可能被连锁触发；update 要防死循环，retract 的先后顺序靠 salience 优先级保证。

## 比较操作符：前六个照搬 Java，后六个成对取反

模式匹配的属性约束里其实已经用过比较操作符——入门案例的 `originalPrice >= 100 && originalPrice < 200` 就是。这里系统梳理一遍，Drools 提供的比较操作符共十二个：

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

contains 和 memberOf 长得很像，方向是反的：contains 说的是前面的属性值包含后面的值；memberOf 说的是前面的属性值是后面集合的一个成员，即后面的集合包含前面的值。not 版本只是在前面加一个 not。

### 测试准备：实体类与规则文件

新建实体类 ComparisonOperatorEntity（比较操作符实体），作用类似入门案例的 Order——把原始数据传进工作内存。两个属性就够测完全部操作符：`names`（String）和 `list`（List<String>），补上 getter/setter。

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
        System.out.println("规则：rule_comparison_contains触发了...");
end
```

两个细节值得注意。第一，这条规则没写绑定变量名——then 部分根本没用到对象引用，所以绑定变量名可以省略；要用到就必须写。第二，IDEA 的 Drools 插件提示能力有限，package、import 这些能提示出来，contains 这类操作符提示不出来，只能手敲，敲完它会变色。

单元测试复制一份改成 test2，前三个对象的模板代码不动，Fact 对象换成 ComparisonOperatorEntity。属性不设值直接 insert，控制台没有任何输出但执行成功——规则没触发；设上 names 为张三再跑，规则就触发了。

第二个 Pattern `list contains names` 不写连接词，默认就是 and，所以 list 也得包含 names：new 一个 ArrayList 加进张三，set 到 fact 对象上。演示时踩了个坑——只 new 了 list 忘了 set，规则死活不触发，因为这个 list 和对象没有关系；set 进去才触发。改成 or 则一个条件成立即可。测 not contains 反着来：names 改李四，list 元素与 names 不一致即可触发。

### memberOf 与 matches

memberOf 的方向反过来：

```java
// 测试比较操作符 memberOf
rule "rule_comparison_memberOf"
    when
        ComparisonOperatorEntity(names memberOf list)
    then
        System.out.println("规则：rule_comparison_memberOf触发了...");
end
```

含义是 names 必须是 list 的一个成员。names 给李四、list 里只有张三时执行，规则不触发；往 list 里 add 一个李四，memberOf 规则就触发了。not memberOf 是取反，注意 not 和 memberOf 之间有空格。这轮测试还有个观察：只要匹配成功，多个规则可以同时触发。

matches 后面跟正则：

```java
rule "rule_comparison_matches"
    when
        ComparisonOperatorEntity(names matches "王.*")
    then
        System.out.println("规则：rule_comparison_matches触发了...");
end
```

"王.*" 表示必须以王开头。names 是李四时匹配不上，规则不执行；改成王四，第一个字是王，matches 触发。not matches 取反：王四时它不触发，改回李四它就触发了。整组操作符演示下来，除正则外都很直观。

## 执行指定规则：AgendaFilter 过滤器

前面的案例里，满足条件的规则都会被执行——三条匹配成功就三条全触发。如果不想让所有匹配成功的规则都执行，只想执行指定的某一条或某一些，怎么实现？Drools 给的方式是规则过滤器，规则文件不用做任何修改，只需要改 Java 代码。

具体改哪行？`fireAllRules()` 这个方法除了无参版本，还有带参数的同名重载，需要传一个 AgendaFilter。Agenda 就是前面讲过的议程，存放匹配成功、将要执行的规则；过滤器就是在这批规则里再筛一遍。注意它是个接口，要传具体实现类，常用的有四个：RuleNameEqualsAgendaFilter（规则名等值）、RuleNameStartsWithAgendaFilter（以某字符串开始）、RuleNameEndsWithAgendaFilter（以某字符串结尾）、RuleNameMatchesAgendaFilter（类似正则匹配）。接口定义就一个方法，返回 true 表示允许这个匹配触发：

```java
public interface AgendaFilter {
    boolean accept(Match match);
}
```

演示时数据保持不变，本来 notcontains、not memberOf、not matches 三条规则都匹配成功都触发了；把触发那一行改成按名称过滤：

```java
// 使用 Drools 框架提供的规则过滤器来执行指定规则
session.fireAllRules(new RuleNameEqualsAgendaFilter("rule_comparison_notcontains"));
```

再执行，就只有 rule_comparison_notcontains 这一条触发了，其他两条即使匹配成功也不执行。换成 StartsWith 版本、传入前缀"rule_"，所有以此开头的规则都触发；把其中两条规则的名字改得不满足前缀要求，就只剩剩下的那条。

要再强调一遍：指定了名称不代表这个规则一定触发。前提是它得匹配成功——匹配成功、又在过滤器允许范围内，才会执行。

## 关键字：硬三个，软一堆

Java 有关键字，规则文件里同样有，Drools 把它们分成两类：硬关键字（hard keywords）定义包名或规则名时不能使用，否则程序报错；软关键字（soft keywords）可以使用，只是不建议。

硬关键字只有三个：true、false、null。这里有个写法上的细节：`rule "true"` 是可以的——双引号包起来，整个字符串就是规则的名称，执行单元测试正常通过；写成 `rule true`，不加引号，规则文件在校验阶段就直接报错，执行单元测试同样报错。这个约束针对的就是后者。

规则名的引号还有一层讲究。如果规则名不是硬关键字，双引号可以省略，但省了引号就不能有空格——必须保证是一个整体，有空格就写不成；用下划线连接是常见做法。带双引号则随便带空格也没问题，因为引号内自动被识别成一个整体。强烈建议定义规则名时统一用双引号，这是规范写法。

软关键字比较多，很多正是后面要讲的规则属性名：lock-on-active、date-effective、date-expires、no-loop、auto-focus、activation-group、agenda-group、ruleflow-group、entry-point、duration；再加上 package、import、dialect、salience、enabled、rule、extend、when、then、template、query、declare、function、global、eval、not、in、or、exists、forall、accumulate、collect、from、end、over、init 这些语法关键字。既然是属性名和语法成分，拿它当包名或规则名容易冲突，所以不建议——能用，但别用。

## RHS 内置方法：update / insert / retract

规则文件的 RHS 部分（then 与 end 之间）主要作用，是通过插入、删除或修改工作内存中的 Fact 对象，来达到控制规则引擎执行的目的。Drools 提供了三个内置方法做这件事：update、insert、retract。它们有一个共同的核心效果——操作完成后，规则引擎会重新进行相关规则的匹配；原先没有匹配成功的规则，在数据被操作之后有可能就匹配成功了，匹配成功就会执行。这句话是理解后面所有演示的钥匙。

准备一个 Student 实体类，三个属性 id、name、age，配套 getter/setter。规则文件新建 student.drl，package student、import Student。

### update：改完数据必须让它重新匹配

```java
// 当前规则用于测试 update 内置方法
rule "要求Student的age小于10岁"
    when
        $s: Student(age < 10)
    then
        $s.setAge(15);
        System.out.println("规则一触发");
end

// 规则二
rule "要求Student的age大于10岁并且小于20岁"
    when
        $s: Student(age < 20 && age > 10)
    then
        System.out.println("规则二触发");
end
```

规则名用中文没有问题，双引号里的字符串可以任意。演示时 age 设成 5：规则一匹配成功，规则二匹配不上。有个关键问题值得想清楚——规则一的 then 里已经 `setAge(15)` 了，15 正好落在 10 到 20 的区间，规则二会跟着触发吗？答案是不会。因为规则匹配发生在调用 fireAllRules 的时候：当时 age 是 5，只有规则一匹配成功并放入议程；执行阶段只执行议程里的规则，规则一内部改了 age，但没有触发重新匹配，规则二根本不在议程里。

让规则二也执行，就用 update。在规则一的 then 里 setAge 之后加一行：

```java
$s.setAge(15);
update($s); // update方法用于更新Fact对象，会导致相关规则重新匹配
```

update 的签名是 `update(Object newObject)`，把 Fact 对象传进去。更新完成后相关规则重新匹配，age 已经是 15，规则二匹配成功并执行。连锁反应还能继续：规则二触发时再 `setAge(25)` 并 update，age 大于 20 的规则三也会被带着触发；规则二不写 update，链条就停在它那里。

用 update 有一点必须注意：防止死循环。规则一触发导致规则二匹配，规则二又改数据可能让别的规则匹配上，连锁反应如果绕回去，就会一直循环执行下去，编写规则文件时要特别留意。

### insert：塞一个新 Fact 进工作内存

insert 的作用是向工作内存中插入数据，并让相关规则重新匹配。加一条 age 等于 10 的规则：

```java
rule "要求Student的age等于10岁"
    when
        $s: Student(age == 10)
    then
        Student s = new Student();
        s.setAge(5);
        insert(s); // insert方法用于向工作内存中插入Fact对象，会导致相关规则重新匹配
        System.out.println("规则：要求Student的age等于10岁触发了...");
end
```

注意条件是 age == 10，两个等号。单元测试里把 age 设成 10 执行：只有这一条规则触发，小于 10、10 到 20、大于 20 都匹配不上。然后在这条规则里 new 一个 age 为 5 的新 Student 并 insert 进去：插入完成后相关规则重新匹配，"age 小于 10 岁"那条规则对新的 Fact 匹配成功，它又 setAge(15) 加 update，继续重新匹配——一连串连锁反应下来，四条规则全部执行。

### retract：删掉 Fact，后面的规则就匹配不到

retract 的作用是删除工作内存中的数据，并让相关规则重新匹配。再写一条测试它的规则：

```java
// 当前规则用于测试 retract 内置方法
rule "要求Student的age等于10岁用于删除"
    when
        $s: Student(age == 10)
    then
        retract($s); // retract方法用于删除工作内存中的Fact对象，会导致相关规则重新匹配
        System.out.println("规则：要求Student的age等于10岁用于删除触发了...");
end
```

它的条件和 insert 那条完全一样（age == 10），但规则的名称必须是唯一的，不能相同，所以起了个不同的名字。现在的意图是：上面这条执行，下面那条不执行。做法就是在这条规则里把 Fact 删掉——retract 执行后工作内存里没有这个 Student 对象了，重新匹配时下面那条规则自然匹配不到。

有个顺序问题要交代：两个条件一样的规则，怎么保证先执行上面这条、再轮到下面那条？靠规则属性 salience，即执行优先级，这个属性后面会专门讲。不指定时所有规则默认优先级相同（为 0），按规则文件里的编写顺序由上到下执行，当前场景不写也能得到正确结果；显式给上面这条加个 `salience 10` 则更明确。

验证效果：age 设成 10，只有"用于删除"这条触发，下面的规则没触发，因为对象被删掉了。把 retract 注释掉再跑——下面那条也匹配到并执行，它又 insert 新对象进来，连锁反应启动，所有规则全部触发。删与不删，就是两条链路的分叉点。

## 小结

本篇把基础语法下半场走完。比较操作符十二个，前六个照搬 Java，后六个成对取反：contains 与 memberOf 包含方向相反，matches 吃标准 Java 正则。想精确控制执行范围，规则文件不动，`fireAllRules(AgendaFilter)` 配合四个按规则名过滤的实现类即可，但指定名称的前提仍是匹配成功。硬关键字 true、false、null 绝对不能用作包名或规则名，软关键字能用不建议用。RHS 三件套 update/insert/retract 分别更新、插入、删除工作内存中的 Fact，共同点是都会引发相关规则重新匹配，由此产生规则连锁反应；update 链要防死循环，retract 依赖 salience 保证执行顺序。基础语法到此收尾，下一篇进入十个规则属性，salience 会是第一个重点。
