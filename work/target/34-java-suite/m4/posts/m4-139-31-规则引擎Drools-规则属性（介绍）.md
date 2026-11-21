---
title: "Drools 规则属性全集：salience 排序、enabled 开关、分组互斥与 timer 定时"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 规则属性全集：salience 排序、enabled 开关、分组互斥与 timer 定时

规则体语法里 rule 名称与 when 之间一直留着一段空位——attributes。前面把 LHS 比较操作符和 update/insert/retract 内置方法过完之后，规则的触发顺序、启用开关、组间互斥、定时触发这些"运行策略"还没真正握在手里，而内置方法引发的重新匹配又埋下了死循环隐患。本篇把 Drools 常用的十个规则属性逐个落地演示：两个轻量属性（dialect、enabled）、一个排序属性（salience）、四个分组与防护属性（no-loop、activation-group、agenda-group、auto-focus）加一个定时器（timer），date-effective/date-expires 留到下篇。

## 先给结论

- 属性位置固定：写在 rule "名称" 与 when 之间，可以同时定义多个；常用十个属性为 salience、dialect、enabled、date-effective、date-expires、activation-group、agenda-group、timer、auto-focus、no-loop。
- salience 指定执行优先级，取值 Integer，数值越大越优先；所有规则都不设置时按文件书写顺序由上到下执行，建议显式声明。dialect 指定规则语言类型（java/mvel，默认 java），enabled 是启用开关（默认 true，设为 false 则无论是否匹配成功都不触发）。
- no-loop true 防死循环：then 里调用 update 之类的方法会触发规则重新匹配，条件仍成立时当前规则被反复激活；no-loop 默认 false 不做防护。
- activation-group 组内互斥：组名相同的规则只能有一个触发，具体谁触发由 salience 决定；agenda-group 组内不互斥，但只有获取焦点的组中的规则才可能被触发，焦点通过 session.getAgenda().getAgendaGroup("组名").setFocus() 设置。
- auto-focus true 让所在议程组自动获取焦点（默认 false），且同一组内只要任意一个规则设置了 true，整组生效。
- timer 定时器两种写法：timer(初始延迟 重复间隔?)（如 timer(5s 2s)）和 timer(cron: 表达式)；测试时必须用新线程跑 fireUntilHalt()，主线程 sleep 一段时间后调 halt() 停引擎，否则 timer 没有持续运行的宿主环境。

## 属性全景：写在 rule 名称与 when 之间

先把规则体的完整结构摆出来，属性部分就是之前一直空着的那一段：

```java
rule "ruleName"
    attributes
    when
        LHS
    then
        RHS
end
```

attributes 出现的位置是固定的——规则名称和 when 之间，而且可以在这一段同时定义多个属性。Drools 提供的属性不止下面这些，课程要展开讲的是十个：

| 属性 | 说明 |
| --- | --- |
| salience | 指定规则执行优先级 |
| dialect | 指定规则使用的语言类型，取值 java 和 mvel |
| enabled | 指定规则是否启用 |
| date-effective | 指定规则生效时间 |
| date-expires | 指定规则失效时间 |
| activation-group | 激活分组，具有相同分组名称的规则只能有一个规则触发 |
| agenda-group | 议程分组，只有获取焦点的组中的规则才有可能触发 |
| timer | 定时器，指定规则触发的时间 |
| auto-focus | 自动获取焦点，一般结合 agenda-group 一起使用 |
| no-loop | 防止死循环 |

演示之前交代三个小语法点。第一，LHS 条件不写默认恒为 true，规则匹配成功直接执行 then 部分；也可以显式写 eval(true)，作用一样——返回 true 即视为匹配成功，eval 表达式后面章节还会专门讲。第二，规则名称必须唯一，演示 agenda-group 时复制规则忘改名字，单元测试直接报错。第三，包名别拿属性名当一段：package 写成 test.salience 会报错，因为 salience 本身是属性关键字，要连写成 testsalience。

## 优先级与开关：salience、dialect、enabled

salience 在内置方法的演示里已经露过面，这里单独建一个 salience.drl，用三条恒匹配规则验证执行顺序：

```java
package testsalience

rule "rule_1"
    salience 9
    when
        eval(true)
    then
        System.out.println("规则: rule_1触发了...");
end

rule "rule_2"
    salience 10
    when
        eval(true)
    then
        System.out.println("规则: rule_2触发了...");
end

rule "rule_3"
    salience 8
    when
        eval(true)
    then
        System.out.println("规则: rule_3触发了...");
end
```

先把三条 salience 注释掉跑一遍，输出按 rule_1 → rule_2 → rule_3，也就是文件书写顺序、由上到下；加回来再跑，顺序变成 rule_2 → rule_1 → rule_3，和 salience 值的大小排序完全一致。每个规则都有默认执行顺序，但没有显式指定时全靠书写位置，建议编写规则文件时明确用 salience 声明优先级，哪个先执行哪个后执行一目了然。

dialect 与 enabled 是两个轻量属性。dialect 指定当前规则使用的语言类型，取值 java 或 mvel，默认 java。MVEL 是一种基于 Java 语法的表达式语言，类似正则表达式，直接支持集合、数组、字符串匹配的操作符，还提供用来配置和构造字符串的模板语言；表达式内容涵盖属性表达式、布尔表达式、方法调用、变量赋值、函数定义等。规则 RHS 里写的其实就是 Java 代码，靠的就是默认的 java 方言，实际开发基本都用 java 编写，MVEL 了解即可。

enabled 取值 true/false，默认 true，用于指定当前规则是否启用。演示接在上篇的 student.drl 上，给"要求Student的age等于10岁用于删除"这条加一行属性：

```java
rule "要求Student的age等于10岁用于删除"
    salience 10
    enabled false // 取值true或者false，默认值true
    when
        $student:Student(age == 10)
    then
        retract($student);
        System.out.println("规则：要求Student的age等于10岁用于删除触发了...");
end
```

执行单元测试，这条规则不再触发——条件明明匹配得上。副作用也看得清楚：它不触发就不会执行 retract 删除工作内存里的 Fact 对象，条件相同的另一条 age==10 规则（insert 那条）反而被放出来触发了，后面又引起一连串连锁反应。把 enabled 明确改回 true 再跑，一切恢复原样。这就是开关的意义：规则可以写好放在那里，随时用一行属性停用。

## 分组与防死循环：no-loop、activation-group、agenda-group、auto-focus

no-loop 处理的是内置方法留下的死循环隐患。什么时候会死循环？规则通过 update 这类内置方法修改了 Fact 对象，导致相关规则重新匹配，当前规则条件仍然成立就会再次被激活，如此往复。建 noLoop.drl 演示：

```java
package testnoloop
import com.itheima.drools.entity.Student

rule "rule_noLoop"
    no-loop true
    when
        $s:Student(age == 50)
    then
        update($s);
        System.out.println("规则: rule_noLoop触发了...");
end
```

测试数据把 Student 的 age 设成 50 让规则匹配成功。先不加 no-loop：规则触发，then 里 update($s) 让相关规则重新匹配，age 没改条件还是成立，又触发又 update——控制台无限刷屏，程序永远停不下来，只能强制杀进程；死循环消耗内存资源非常多，IDE 都卡了半天才停住。加上 no-loop true（Boolean 类型，默认 false）再跑，只输出一遍就结束——即使调用了 update 方法，当前规则也不会重新匹配。写规则时只要用到 update、insert、retract 这几个内置方法，先想清楚有没有死循环的可能，有就加 no-loop。

activation-group 是激活分组，取值 String 类型，组名相同的规则互斥，只能有一个被触发。两条恒匹配规则都挂上 activation-group "mygroup"：不加分组时两条都触发；加了之后只剩第一条触发（没设 salience，按文件顺序）。同一个组里多条规则都能匹配成功时，具体哪个被触发由 salience 决定——把第二条的优先级调到 10、第一条留 5，这次触发的就是第二条。

agenda-group 是议程分组，属于另一种可控的规则执行方式，和 activation-group 的区别有两点：组内规则不互斥，多个规则可以同时被触发；但只有获取焦点的组中的规则才有可能触发。建 4 条规则，前两条挂 agenda-group "myagendagroup_1"，后两条挂 "agenda_group_2"：

```java
rule "rule_agendagroup_1"
    agenda-group "myagendagroup_1"
    when
    then
        System.out.println("规则: rule_agendagroup_1触发了...");
end
```

不做任何设置直接跑单元测试，四条规则全都没触发——没有任何组获得焦点。让某个组获得焦点要在 Java 代码里做：

```java
// 指定组获得焦点
session.getAgenda().getAgendaGroup("myagendagroup_1").setFocus();

// 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
session.fireAllRules();
session.dispose();
```

getAgenda() 拿到议程对象，getAgendaGroup("组名") 按名字取组，setFocus() 设置焦点。这时第一组里的两条规则都触发了（组内不互斥），第二组仍然沉默；把组名换成 agenda_group_2，触发的就换成后两条。注意是"有可能触发"：焦点只是入场券，条件不匹配照样不执行——把其中一条的 LHS 写成 eval(false)，获得焦点的组里它也没触发。

auto-focus 补的是"不想写 Java 代码设焦点"的场景。Boolean 类型，默认 false，一般结合 agenda-group 使用：当某个议程分组未获取焦点时，设置 auto-focus true 让它自动获得焦点。在 agenda_group_2 的规则上加 auto-focus true，Java 测试代码一行不改，后两条规则就触发了。还有一个组级别的特性：同一组内只要任意一个规则设置了 auto-focus true，整组自动获得焦点——组内另一条规则哪怕显式写 auto-focus false，也照样触发。

## timer 定时器：interval 与 cron 两种写法

timer 通过定时器的方式指定规则执行的时间，类似 Java 里的定时器对象。两种使用方式：

- timer(int: <初始延迟> <重复间隔>?)：遵循 java.util.Timer 的用法，第一个参数几秒之后执行，第二个参数每隔几秒执行一次，问号表示可选；
- timer(cron: <cron 表达式>)：基于标准 Unix cron 表达式，时间定义更灵活、功能更强大。

建 timer.drl 演示第一种：

```java
package testtimer

// timer第一种使用方式
rule "rule_timer_1"
    timer (5s 2s) // 5秒后触发，之后每隔2秒触发一次
    when
    then
        System.out.println("规则: rule_timer_1触发了...");
end
```

timer 要持续触发，单元测试不能再调 fireAllRules()——它匹配触发完就返回，整个测试方法执行完程序就退了，定时器根本没机会跑起来。要换成 fireUntilHalt()：启动规则引擎持续进行规则匹配，直到调用 halt() 才结束：

```java
@Test
public void test7() throws Exception {
    KieServices kieServices = KieServices.Factory.get();
    KieContainer kieContainer = kieServices.newKieClasspathContainer();
    final KieSession session = kieContainer.newKieSession();

    new Thread(new Runnable() {
        public void run() {
            // 启动规则引擎进行规则匹配，直到调用halt方法才结束规则引擎
            session.fireUntilHalt();
        }
    }).start();

    Thread.sleep(10000); // 持续10秒

    // 结束规则引擎
    session.halt();
    session.dispose();
}
```

几个细节：session 要加 final（匿名内部类里引用它）；规则引擎跑在新线程里，主线程 sleep 一万毫秒让程序存活 10 秒；到点后调用 session.halt()（halt 就是停机、关机的意思，类似 Linux 的 shutdown 命令），规则引擎停止，timer 随之停止——timer 的执行基于整个规则引擎的运行环境。跑起来观察输出：其他规则立刻打印，rule_timer_1 隔了设定的延迟才第一次出现，之后每 2 秒一次，直到 10 秒后被 halt 掐掉。单元测试只能靠线程睡眠撑时间；如果是基于 Tomcat 的 Web 项目，服务常驻运行，就不存在这个问题。

第二种用 cron 表达式，语法是 timer 后跟 cron: 前缀再加表达式。表达式写全共 7 位：秒、分、时、日、月、周、年，最后一位年可以省略；* 匹配所有值，/ 表示递增（每隔多长时间），? 表示该位不做控制（用在日、周）。演示规则加上了触发时间输出：

```java
rule "rule_timer_2"
    timer (cron:0/1 * * * * ?) // 每隔1秒触发一次
    when
    then
        System.out.println("规则: rule_timer_2触发了...触发的时间为：" +
            new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()));
end
```

SimpleDateFormat 在 java.text 包下，Date 在 java.util 包下，规则文件顶部先 import 再用。观察输出里的时间戳就能核对间隔：演示时把秒位调成 0/2，即从第 0 秒开始每 2 秒触发一次，10 秒的持续窗口里 06、08、10、12、14 各一次，正好 5 次。cron 表达式本身课程不展开，写 Quartz、Spring Task 这类定时任务框架时都用它指定触发时间，只是这里把表达式放到了 timer 属性的位置。

## 小结

规则属性全部写在 rule 名称与 when 之间，可多个并存。salience 管顺序（值越大越优先，默认按书写顺序），enabled 管启停，dialect 管规则语言（默认 java，MVEL 了解即可）。no-loop true 防 update 引发的死循环；activation-group 组内互斥只出一个，agenda-group 组内不互斥但要先获得焦点（Java 侧 setFocus 或规则侧 auto-focus true，组内一个设置整组生效）。timer 用 interval 或 cron 两种表达式定时触发，测试时以 fireUntilHalt + halt 撑起引擎的持续运行。剩两个时间属性 date-effective/date-expires，连同 global、Query、function、LHS 加强等高级语法，下篇继续。
