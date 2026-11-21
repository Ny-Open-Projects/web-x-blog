---
title: "Drools 属性收尾与高级语法：date-effective/date-expires、global、query、function 与 LHS 加强"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 中台战略与组件化开发]
tags: [Java, 项目实战, Drools]
---

# Drools 属性收尾与高级语法：date-effective/date-expires、global、query、function 与 LHS 加强

规则属性还剩两个时间属性没有落演示，本篇先补上 date-effective/date-expires 这对"生效-失效"开关；随后进入 Drools 高级语法——一套完整规则文件里此前没用到的三个组成部分：global 全局变量、query 查询、function 函数，再加上 LHS 部分的新用法 in/not in 与 eval。这些语法把规则文件从"只会匹配工作内存里的对象"升级为能与 Java 程序双向交互、可复用业务逻辑的完整组件。

## 先给结论

- date-effective 指定规则生效时间（系统时间大于等于该值才可能触发），date-expires 指定失效时间（系统时间小于等于该值才可能触发）；默认格式 dd-MMM-yyyy，要用习惯的年月日格式，先执行 System.setProperty("drools.dateformat", "yyyy-MM-dd HH:mm")，属性名是 Drools 定义好的，不能写错。
- 日期格式是个全局性坑：rules 目录里只要存在使用自定义日期格式的规则文件，所有单元测试都得先设置 drools.dateformat——规则引擎启动时会把所有 drl 加载进规则库并做检查，格式不匹配直接报 InvalidDataInputFormat。
- global 定义全局变量（global 类型 名称），Java 侧用 session.setGlobal("名称", 值) 注入，名字必须与 drl 里一致，不注入就空指针；包装类型的修改只在当前规则内生效（相当于副本），集合类型和 JavaBean 的修改对 Java 程序和所有规则全局可见。
- query 在规则文件里定义"查工作内存"的入口：只有 LHS 部分，不写 when/then；Java 侧 session.getQueryResults("名称", 可选参数) 返回 QueryResults，size() 拿个数，遍历时 row.get("绑定变量名") 取出 Fact 对象。
- function 在规则文件里定义函数，相当于 Java 类里的方法，把业务逻辑集中在一处便于修改，规则的 RHS 按函数名直接调用。
- LHS 加强：in/not in 是复合值限制，类似 SQL 里的 in；eval(布尔表达式) 在 LHS 显式返回布尔值，eval(true) 与不写条件等价。

## 时间属性：date-effective 与 date-expires

date-effective 用于指定规则的生效时间：只有当系统时间大于等于设置的时间或日期时，规则才有可能触发。默认日期格式是 dd-MMM-yyyy（日-月-年），更习惯 yyyy-MM-dd 开头的写法，所以演示直接用自定义格式——前提是先把格式告诉 Drools：

```java
package testdateeffective
import java.text.SimpleDateFormat
import java.util.Date

rule "rule_dateeffective_1"
    date-effective "2020-10-10 10:00" // 指定规则生效时间
    when
    then
        System.out.println("规则: rule_dateeffective_1触发了，触发的时间为："
            + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()));
end
```

单元测试在拿 KieSession 之前多一行系统属性设置：

```java
@Test
public void test8() {
    // 设置日期格式，属性名是Drools定义好的，不能写错
    System.setProperty("drools.dateformat", "yyyy-MM-dd HH:mm");

    KieServices kieServices = KieServices.Factory.get();
    KieContainer kieContainer = kieServices.newKieClasspathContainer();
    KieSession session = kieContainer.newKieSession();
    session.fireAllRules();
    session.dispose();
}
```

这行不改，执行时直接报 InvalidDataInputFormat（非法的日期输入格式）——默认只认 dd-MMM-yyyy。设置好格式之后再跑，规则依然没触发，原因很简单：date-effective 写的 2020-10-10 还没到，规则未生效就不会触发；把时间改成已经过去的 2019-10-10，规则立刻执行，输出里带上了触发时刻。

date-expires 是规则属性的最后一个，指定规则的失效时间：只有当前系统时间小于等于设置的时间，规则才有可能触发。用法与 date-effective 一致，默认格式相同，也需要同样设置 drools.dateformat，否则同样报格式错误：

```java
rule "rule_dateexpires_1"
    date-expires "2019-10-10 10:00" // 指定当前规则的失效时间
    when
    then
        System.out.println("规则：rule_dateexpires_1触发了...");
end
```

写 2019-10-10 10:00 时规则不触发——已经失效了；改成 2020-10-10 10:00，还没失效，规则正常触发。一个管"从什么时候开始活着"，一个管"到什么时候为止"，两个属性组合起来就是规则的时间窗。

这里有个工程上的连锁坑值得单独记：日期规则文件写完之后，此前所有单元测试突然都报 InvalidDataInputFormat。原因是规则引擎启动时会把 rules 目录下所有规则文件加载进规则库并做检查，不管这条规则最终能不能触发。所以一旦项目里存在自定义日期格式的 drl，每个测试方法都要补上 System.setProperty 这一行。

## global 全局变量：包装类型与集合/JavaBean 行为不同

一套完整的规则文件写全了包含六个部分：package 定义包名、import 导入类或静态方法、global 定义全局变量、function 定义函数、query 定义查询、rule...end 规则体。前三样之前一直在用，现在从 global 开始补齐。

global 让应用程序的对象在规则文件中可被访问，可以为规则文件提供数据或服务，语法是 `global 对象类型 对象名称`。演示建 global.drl，三种类型的全局变量各来一个：

```java
package testglobal
import com.itheima.drools.service.UserService

global java.lang.Integer count    // 包装类型的全局变量
global java.util.List gList       // 集合类型的全局变量
global UserService userService    // JavaBean类型的全局变量

rule "rule_global_1"
    when
    then
        count += 10; // 包装类型的修改只对当前规则生效
        gList.add("itcast");
        System.out.println("全局变量count计算之后的值为：" + count);
        System.out.println("全局变量gList的size：" + gList.size());
        userService.save();
end

rule "rule_global_2"
    when
    then
        System.out.println("全局变量的值为：" + count);
        System.out.println("全局变量gList的size：" + gList.size());
end
```

UserService 是个简单的 JavaBean，save 方法里没有真正调 DAO 操作数据库，只打印一句话，用来演示"把 Service 对象交给规则文件使用"。全局变量的初始值必须在 Java 程序里注入，变量名要和规则文件里定义的完全一致（全局变量可以定义多个，名字对不上就没法对应）：

```java
// 设置全局变量，变量名称必须和规则文件中定义的变量名一致
session.setGlobal("count", 5);

List<String> list = new ArrayList<String>();
list.add("itheima");
session.setGlobal("gList", list);
session.setGlobal("userService", new UserService());

// 只触发以rule_global为前缀的规则，排除其他规则输出的干扰
session.fireAllRules(new RuleNameStartsWithAgendaFilter("rule_global"));

System.out.println("在Java程序中全局变量gList的size为：" + list.size());
```

忘了 setGlobal 会直接空指针——规则文件拿不到全局变量的初始值。fireAllRules 传了一个 AgendaFilter 参数，它是个接口，这里用实现类 RuleNameStartsWithAgendaFilter：只执行名称以 rule_global 开头的规则，其他规则不匹配、不执行，测试时排除干扰输出。

运行结果把两种类型的行为差异摆得很清楚。rule_global_1 里 count 计算之后是 15（5 加 10），但 rule_global_2 里看到的还是 5——包装类型（Integer、Double 这类）的全局变量，在一个规则里改值只对当前规则有效，相当于当前规则代码里的一份副本，规则内部修改不影响全局使用。gList 则完全相反：初始 list 只有 itheima 一个元素，规则里 add 了 itcast 之后，rule_global_2 里 size 是 2，回到 Java 程序里再打印 list.size() 也是 2——集合类型或 JavaBean 类型的全局变量一旦被修改，其他规则和 Java 程序全部可见。断点调试看更直观：new 出来 size 为 0，add 一个变 1，规则执行完变 2，全程操作的是同一个对象。

## query 查询与 function 函数

query 查询提供了一种查询工作内存中符合约束条件的 Fact 对象的简单方法。它只包含规则文件中的 LHS 部分，不用指定 when 和 then，查到符合条件的 Fact 对象直接返回，没有 RHS 动作部分：

```java
package testquery
import com.itheima.drools.entity.Student

// 不带参数的查询：查工作内存中age等于50的Student
query "query_1"
    $s: Student(age == 50)
end

// 带参数的查询：age大于5且name等于传入参数
query "query_2" (String sname)
    $s: Student(age > 5 && name == sname)
end
```

Java 侧按名称调用查询，getQueryResults 的后续参数是可变长度的，查询定义了参数就要传、没定义就不用传：

```java
// 根据名称调用规则文件中定义的查询
QueryResults results1 = session.getQueryResults("query_1");
System.out.println("符合条件的Fact对象个数：" + results1.size());

Student s1 = new Student();
s1.setAge(50);
s1.setName("张三");
session.insert(s1);

// 遍历查询结果，"$s"对应LHS里的绑定变量名
for (QueryResultsRow row : results1) {
    Student s = (Student) row.get("$s");
    System.out.println(s);
}

// 带参数的查询：通过可变参数把值传进去
QueryResults results2 = session.getQueryResults("query_2", "张三");
System.out.println("符合条件的Fact对象个数：" + results2.size());
```

不向工作内存插入对象时，query_1 的 size 是 0；插入一个 age=50 的 Student 变 1，插入两个变 2。QueryResults 实现了 Iterable 接口，可以直接遍历，row.get("$s") 按绑定变量名取出对象强转回 Student。带参查询的演示同样直观：两个 age=50 的 Student 都没设 name 时查"张三"得 0，把 s1 的 name 设成张三得 1，两个都叫张三得 2——注意 LHS 里的 name 是 Student 类的属性名，不能写错；参数名 sname 才是随便起的。另一个测试技巧：调用查询本身不需要触发规则，只是到工作内存里查找，测试纯查询时可以把 fireAllRules 注释掉，控制台立刻清爽。

function 用关键字在规则文件中定义函数，其实就相当于 Java 类里的方法，可以在规则体中调用。用它的好处是把业务逻辑集中放在一个地方，根据需要修改函数即可：

```java
package testfunction
import com.itheima.drools.entity.Student

// 定义一个函数
function String sayHello(String name) {
    return "hello " + name;
}

// 在规则中调用上面的函数
rule "rule_function_1"
    when
        $s: Student(age > 60)
    then
        String ret = sayHello($s.getName());
        System.out.println("调用sayHello函数，获得返回结果：" + ret);
end
```

语法是 function 返回值类型 函数名(可选参数) { 逻辑代码 }。规则匹配到 age 大于 60 的 Student 后，在 RHS 里调用 sayHello，把匹配对象的 name 传进去，返回值直接输出。测试时插入 age=60 的 Student 匹配不上（要求大于 60），控制台没有输出；把 age 改成 61，输出"调用sayHello函数，获得返回结果：hello 张三"。

## LHS 加强：in/not in 与 eval

LHS 是规则体中介于 when 和 then 之间的部分，主要用作模式匹配，匹配结果为 true 时才触发 RHS 执行。这一部分还有几个新用法。

第一个是复合值限制 in/not in——超过一种匹配值的限制条件，类似 SQL 语句里的 in 关键字。语法是 Object(field in (比较值1, 比较值2...))，多个比较值用逗号分隔：

```java
rule "rule_lhs_1"
    when
        $s: Student(name in ("张三", "李四", "王五"))
    then
        System.out.println("规则: rule_lhs_1触发了...");
end

rule "rule_lhs_2"
    when
        $s: Student(name not in ("张三", "李四", "王五"))
    then
        System.out.println("规则: rule_lhs_2触发了...");
end
```

插入 name 为张三的 Student，rule_lhs_1 触发；把测试数据改成"test"，rule_lhs_1 不再匹配，rule_lhs_2 触发。一条用 in 一条用 not in，两条规则天然互斥——一个成立另一个必然不成立。

第二个是条件元素 eval，用于规则体的 LHS 部分，返回一个 Boolean 类型的值。语法是 eval(表达式)，通常直接传 true 或 false，也可以传任何布尔表达式：

```java
rule "rule_lhs_3"
    when
        eval(1 == 1)
    then
        System.out.println("规则: rule_lhs_3触发了...");
end
```

eval(true) 与干脆不写条件等价——都是恒返回 true，区别只是显式写了出来；写成 eval(1 == 2) 就永远匹配不上。前面演示里用来"恒匹配"的 eval(true) 正是它。PPT 里同属这一族的还有条件元素 not：not 用于判断工作内存中不存在某个 Fact 对象，不存在返回 true，写法如 not Student()，可以在对象约束前直接加 not。

## 小结

date-effective 与 date-expires 给规则加上了时间窗，配合自定义日期格式时记得 System.setProperty("drools.dateformat", ...)，而且这个设置对所有测试都是必需的。global 把 Java 对象交给规则文件使用：包装类型改动只留在当前规则，集合和 JavaBean 改动全局可见，注入时 setGlobal 的名字必须与 drl 中一致。query 提供从 Java 侧反查工作内存的入口，function 让规则文件内聚业务逻辑，in/not in 与 eval 丰富了 LHS 的匹配表达。至此规则属性与高级语法全部过完，规则文件六个组成部分（package/import/global/function/query/rule）也凑齐了。
