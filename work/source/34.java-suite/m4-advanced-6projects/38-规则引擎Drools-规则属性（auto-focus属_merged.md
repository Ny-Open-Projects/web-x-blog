# 38-规则引擎Drools-规则属性（auto-focus属 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢

咱们继续来看规则属性

下一个呢叫做auto focus

这个字面翻译过来叫做什么呢

auto是不是自动

focus其实就是焦点

那么翻译过来呢

就是叫做自动获取焦点

这么一个含义

这个属性呢

它的取值类型呢

是布雷

对吧布尔类型

那就是true跟false

默认值呢是false

一般呢

这个属性呢

会结合咱们刚刚讲过的

这个agenda group属性来使用

当一个一成分组

未获取焦点的时候呢

咱们可以使用这个

auto focus属性来进行控制

让它自动来获得焦点

再来简单回忆一下

我们刚刚讲的这个agenda group

这个属性它的特点是什么呢

通过它是不是可以来指定一个组

指定我们当前这个规则

属于某个组对不对

那么它的特点是

只有当这个组被激活的时候

这个组内的这些规则

是不是它有可能被触发

才有可能被触发

那么

这个激活的时候呢

如何激活呢

或者说如何获得焦点呢

咱们是不是需要通过

调用这个set focus这个方法

来指定这个组

是不是获得了焦点

那对于我们没有设置这个焦点的

这些规则

如何让它触发呢

我们就可以通过这个

auto focus这个属性呢

让这个组自动来获得焦点

所以这个是自动获得焦点

这就需要在我们的规则文件里面

来编写了

这个呢

我们就不再专门创建一个规则文件了

咱们还是在咱们这个

agenda group

这个第二个文件里面

来进行简单的一个修改

就可以了

你看这是我们刚才创建的

这个agenda group对吧

并且呢

我们的单元测试呢

现在是让第一个组

其实就是上面这个组

这个组呢

里边是不是有两个规则

前面两个规则是属于第一个组

咱们在这儿

是不是已经让他们获得了焦点

然后呢

后边这两个规则

属于第二个组对不对

这

这两个规则呢

并没有获得焦点

所以当我们在执行单元测试的时候

大家来看一下

后边这两个规则呢

并不会触发

现在的情况是这样的

你看后边这两个规则呢

并没有触发

那现在呢

我希望啊

后边这两个规则也触发

那就必须让他们是不是获得焦点

那么怎么获得焦点呢

就可以使用我们这个autofocus

大家来看

autofocus

对吧

注意要给true啊

你别给false

给false的话

它是不起作用的

啊

得给true

这就表示啊

自动获得焦点

哎

这个属性啊

用于指定什么呢

当前所属

所属

这个组

对吧

自动

自动啊

获取焦点

获得焦点

OK

那这个呢

我们把它

Ctrl C拿过来

因为他们是属于同一个组

对吧

所以我在这呢

也复制一份啊

也给一个true

这是自动获得焦点了

自动获得焦点之后

我们再来

执行这个单元测试

注意看啊

我们的

呃

Java代码

这个单元测试的代码呢

没有做任何修改

但是呢

你可以看到

这儿的话

它已经可以输出了

那就说明啊

这两个规则是不是

已经触发了

哎

为什么能触发呢

就是因为我们设置了这个

自动获得焦点

那可能有的同学

看到这个代码呢

看到我们这个规则文件呢

会有点疑问

是什么呢

说你这两个地方

是不是都写了

感觉挺啰嗦的

我们如果只写一个

行不行呢

哎

注意看啊

我们现在呢

注视起来一个

只留

保留上面这个

因为它俩

这两个规则

是不是属于同一个组

所以啊

我们只要在这个地方

写一遍

其实是可以的

咱们来看一下

哎

你看

我们是不是只要

写了一遍

然后这两个规则

是不是都触发了

都触发了

所以说啊

对于同一个组里边的

这些规则来说啊

我们只要写一个

AutoFocus等于触

那么整个组内

所有的规则呢

其实都会生效

都会生效

所以说啊

那这儿的话

我们还有一个疑问

是什么呢

就是说啊

我上面这个写的是

AutoFocus等于触

对不对

然后我下边呢

我来个False

我跟你对着来

对吧

我跟你来个False

那这个时候

会有什么样的效果

哎

咱们来验证一下

其实呢

这个时候呢

它还是会触发的

我们先来看一下

这个执行结果

你看

它是不是

这两个规则都触发了

哎

那看来是

一个什么样的特点呢

这个AutoFocus

就是说啊

对于

对于

同一个

这个Agenda Group组

对吧

这是同一个组内

多个规则

我们只要有任意一个规则

设置了这个AutoFocus等于触

其他的规则

不管你设置还是不设置

对吧

那么它都会自动获得焦点

也就是说

这些规则因为是属于一个组了

它们相当于是一个组为单位

哎

只要有一个设置了

整个组都生效

哎

就是这么一个样的效果

那么通常呢

它是结合着我们这个Agenda Group啊

一块来使用

的这么一个属性

好

这是关于咱们这个AutoFocus

自动获得焦点

这个属性

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 Drools 规则引擎中 **`auto-focus`** 属性的讲解。讲师通过修改规则文件和编写测试代码，演示了如何使用 `auto-focus` 属性来控制规则的执行顺序。核心内容是：`auto-focus` 属性为 `true` 时，该规则组会自动获取焦点，从而在规则引擎中优先被触发，即使它不是当前焦点组。讲师通过对比 `agenda-group` 和 `auto-focus` 的组合使用，说明了如何实现更灵活的规则执行控制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 PPT 上介绍 `auto-focus` 属性的基本概念。
*   **00:00:05 - 00:00:15**: 讲师在 PPT 上展示 `auto-focus` 属性的定义和使用场景，强调其与 `agenda-group` 的区别。
*   **00:00:15 - 00:00:30**: 讲师切换到代码编辑器，展示 `agenda-group.drl` 文件内容，其中包含两个规则，它们都属于 `myagenda_group_1`。
*   **00:00:30 - 00:00:45**: 讲师在 `DroolsTest.java` 文件中编写测试代码，通过 `session.getAgenda().getAgendaGroup("agenda_group_1").setFocus();` 指定焦点组。
*   **00:00:45 - 00:01:00**: 讲师在 `agenda-group.drl` 文件中添加了两个新规则 `rule_agendagroup_3` 和 `rule_agendagroup_4`，它们都属于 `agenda_group_2`。
*   **00:01:00 - 00:01:15**: 讲师在 `DroolsTest.java` 文件中调用 `session.fireAllRules();` 来触发所有规则。
*   **00:01:15 - 00:01:30**: 讲师在终端窗口中查看测试结果，显示规则 `rule_agendagroup_3` 和 `rule_agendagroup_4` 被触发。
*   **00:01:30 - 00:01:45**: 讲师在 `agenda-group.drl` 文件中为 `rule_agendagroup_3` 和 `rule_agendagroup_4` 添加 `auto-focus true` 属性。
*   **00:01:45 - 00:02:00**: 讲师再次运行测试，终端窗口显示规则 `rule_agendagroup_3` 和 `rule_agendagroup_4` 被触发。
*   **00:02:00 - 00:02:15**: 讲师在 PPT 上总结 `auto-focus` 属性的作用和使用方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **5.7 auto-focus属性**: `auto-focus` 属性为自动获取焦点，取值类型为 Boolean，默认值为 false。一般结合 `agenda-group` 属性使用，当一个议程分组未获取焦点时，可以设置 `auto-focus` 属性来控制。
    *   **第一步**: 修改 `/resources/rules/agendagroup.drl` 文件内容如下。
    *   **第二步**: 在规则中添加 `auto-focus true` 属性。

*   **代码关键内容**:
    *   **`agenda-group.drl` 文件内容**:
        ```drl
        package testagendagroup

        rule "rule_agendagroup_1"
        agenda-group "myagenda_group_1"
        when
        then
            System.out.println("规则: rule_agendagroup_1触发了...");
        end

        rule "rule_agendagroup_2"
        agenda-group "myagenda_group_1"
        when
        then
            System.out.println("规则: rule_agendagroup_2触发了...");
        end
        ```
    *   **`DroolsTest.java` 文件内容**:
        ```java
        public void test6() {
            KieServices kieServices = KieServices.Factory.get();
            KieContainer kieContainer = kieServices.newKieClasspathContainer();
            KieSession session = kieContainer.newKieSession();

            //指定组获得焦点
            session.getAgenda().getAgendaGroup(name: "agenda_group_1").setFocus();

            //激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
            session.fireAllRules();

            //关闭会话
            session.dispose();
        }
        ```
    *   **修改后的 `agenda-group.drl` 文件内容**:
        ```drl
        package testagendagroup

        rule "rule_agendagroup_1"
        agenda-group "myagenda_group_1"
        when
        then
            System.out.println("规则: rule_agendagroup_1触发了...");
        end

        rule "rule_agendagroup_2"
        agenda-group "myagenda_group_1"
        when
        then
            System.out.println("规则: rule_agendagroup_2触发了...");
        end

        //第三个规则
        rule "rule_agendagroup_3"
        agenda-group "agenda_group_2"
        auto-focus true
        when
        then
            System.out.println("规则: rule_agendagroup_3触发了...");
        end

        //第四个规则
        rule "rule_agendagroup_4"
        agenda-group "agenda_group_2"
        auto-focus true
        when
        then
            System.out.println("规则: rule_agendagroup_4触发了...");
        end
        ```

---

### 4) 关键场景与演示描述

1.  **场景一：概念讲解** (00:00:00 - 00:00:15)
    *   讲师在 PPT 上讲解 `auto-focus` 属性的概念，强调它是一个布尔值，默认为 `false`，用于控制规则组是否自动获取焦点。
    *   讲师指出，`auto-focus` 通常与 `agenda-group` 属性结合使用，以实现更灵活的规则执行控制。

2.  **场景二：代码演示 - 修改规则文件** (00:00:15 - 00:00:30)
    *   讲师在 IntelliJ IDEA 中打开 `agenda-group.drl` 文件。
    *   展示了初始的规则文件内容，其中包含两个规则 `rule_agendagroup_1` 和 `rule_agendagroup_2`，它们都属于 `myagenda_group_1`。
    *   讲师解释了这些规则的默认行为。

3.  **场景三：代码演示 - 编写测试代码** (00:00:30 - 00:00:45)
    *   讲师在 `DroolsTest.java` 文件中编写测试代码。
    *   代码首先获取 `KieServices` 和 `KieContainer` 对象，然后创建 `KieSession`。
    *   通过 `session.getAgenda().getAgendaGroup("agenda_group_1").setFocus();` 指定 `agenda_group_1` 为当前焦点组。
    *   调用 `session.fireAllRules();` 来触发所有规则。

4.  **场景四：代码演示 - 添加新规则** (00:00:45 - 00:01:00)
    *   讲师在 `agenda-group.drl` 文件中添加了两个新规则 `rule_agendagroup_3` 和 `rule_agendagroup_4`。
    *   这两个规则都属于 `agenda_group_2`，但没有设置 `auto-focus` 属性。
    *   讲师解释了这些规则在当前焦点组 `agenda_group_1` 下不会被触发。

5.  **场景五：代码演示 - 运行测试** (00:01:00 - 00:01:15)
    *   讲师运行 `test6()` 方法。
    *   在终端窗口中，可以看到只有 `rule_agendagroup_1` 和 `rule_agendagroup_2` 被触发，因为它们属于当前焦点组 `agenda_group_1`。
    *   `rule_agendagroup_3` 和 `rule_agendagroup_4` 没有被触发。

6.  **场景六：代码演示 - 添加 `auto-focus` 属性** (00:01:15 - 00:01:30)
    *   讲师在 `agenda-group.drl` 文件中为 `
