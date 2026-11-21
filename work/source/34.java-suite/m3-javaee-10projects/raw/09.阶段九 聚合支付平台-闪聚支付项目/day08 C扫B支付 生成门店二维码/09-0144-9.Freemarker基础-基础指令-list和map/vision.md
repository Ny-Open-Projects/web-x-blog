# 画面线理解：9.Freemarker基础-基础指令-list和map

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\9.Freemarker基础-基础指令-list和map【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:19, 02:16, 03:15, 04:55, 05:51, 06:52, 08:19, 09:19, 09:52, 10:32, 12:18, 13:41, 14:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:52:02

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 FreeMarker 模板引擎，通过 Java 代码准备数据模型并将其渲染到 HTML 页面，重点讲解了 List 和 Map 数据结构的遍历指令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 的空白工作区，标题栏显示当前项目路径和打开的文件为 `FreemarkerController.java`。
画面 2: 在 IntelliJ IDEA 中，展示 `FreemarkerTestApplication.java` 中的 Java 代码，创建了两个 Student 对象并将其放入 List 和 Map 中，准备作为模板数据。
画面 3: 在 Typora 中打开的 FreeMarker 教程文档，显示“2.2 List指令”章节，介绍 FreeMarker 模板中 List 的使用。
画面 4: 在 IntelliJ IDEA 中，展示 `test.ftl` 模板文件，正在编辑一个 HTML 表格结构，准备使用 FreeMarker 指令。
画面 5: 在 IntelliJ IDEA 中，展示 `test.ftl` 模板文件，已编写好用于遍历 List 的 `<#list>` 指令结构。
画面 6: 在 Typora 中打开的 FreeMarker 教程文档，显示“2.1 数据模型”章节，展示 Java 代码中创建 Student 对象并放入 Map 的逻辑。
画面 7: 在 Typora 中打开的 FreeMarker 教程文档，显示“1.1 FreeMarker介绍”章节，介绍 FreeMarker 是一个模板引擎，展示其工作原理图：Template -> FreeMarker -> Output。
画面 8: 在 IntelliJ IDEA 中，展示 `FreemarkerController.java` 中的 Java 代码，将准备好的 Map 数据传递给 FreeMarker 模板。
画面 9: 在 Typora 中打开的 FreeMarker 教程文档，显示“2.3 遍历Map数据”章节，展示如何使用 `<#list stuMap.keys as k>` 指令遍历 Map。
画面 10: 在 IntelliJ IDEA 中，展示 `test.ftl` 模板文件，正在编辑用于遍历 Map 的 `<#list>` 指令结构。
画面 11: 在 IntelliJ IDEA 中，展示 `test.ftl` 模板文件，已编写好用于遍历 Map 的 `<#list>` 指令结构。
画面 12: 在浏览器中显示渲染后的 HTML 页面，展示学生信息，但出现 FreeMarker 错误，提示 `stuMap.keys` 为 null。
画面 13: 在 IntelliJ IDEA 中，展示 `test.ftl` 模板文件，光标位于 `<#list stuMap.keys as key>` 指令上，下方显示 FreeMarker 错误信息。
画面 14: 在 Typora 中打开的 FreeMarker 教程文档，显示“2.3 遍历Map数据”章节，展示如何使用 `<#list stuMap.keys as k>` 指令遍历 Map。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
stul.setMoney(1000.86f);
stul.setBirthday(new Date());
stul.setAge(18);
stul.setName("小明");
Student stu2 = new Student();
stu2.setMoney(200.1f);
stu2.setAge(19);
stu2.setBirthday(new Date());
stu2.setName("小红");
//向数据模型放数据
map.put("stus",stus);
//准备map数据
HashMap<String,Student> stuMap = new HashMap<>();
stuMap.put("stu1",stul);
stuMap.put("stu2",stu2);
//向数据模型放数据
map.put("stuMap",stuMap);
return "test1";
```

画面 4:
```html
<table>
<tr>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
</table>
```

画面 5:
```html
<table>
<tr>
<td>序号</td>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
</table>
```

画面 6:
```java
public String freemarker(Map<String, Object> map){
//向数据模型放数据
map.put("name","world");
Student stul = new Student();
stul.setMoney(1000.86f);
stul.setBirthday(new Date());
stul.setAge(18);
stul.setName("小明");
Student stu2 = new Student();
stu2.setMoney(200.1f);
stu2.setAge(19);
stu2.setBirthday(new Date());
stu2.setName("小红");
//向数据模型放数据
map.put("stus",stus);
//准备map数据
HashMap<String,Student> stuMap = new HashMap<>();
stuMap.put("stu1",stul);
stuMap.put("stu2",stu2);
//向数据模型放数据
map.put("stuMap",stuMap);
return "test1";
```

画面 8:
```java
model.put("stus",stus);
model.put("stuMap",stuMap);
return "test1";
```

画面 9:
```html
<tr>
<td>序号</td>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
<#list stuMap.keys as k>
<td>${k_index + 1}</td>
<td>${stuMap[k].name}</td>
<td>${stuMap[k].age}</td>
<td>${stuMap[k].money}</td>
</tr>
</table>
```

画面 10:
```html
<table>
<tr>
<td>序号</td>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
</table>
```

画面 11:
```html
<table>
<tr>
<td>序号</td>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
</table>
```

画面 12:
```html
Hello world!
序号: 1
姓名: 小明
年龄: 18
钱包: 1000.86
序号: 2
姓名: 小红
年龄: 19
钱包: 200.1
```

画面 13:
```html
<#list stuMap.keys as key>
<td>${stuMap[key].name}</td>
<td>${stuMap[key].age}</td>
<td>${stuMap[key].money}</td>
</tr>
```

画面 14:
```html
<tr>
<td>序号</td>
<td>姓名</td>
<td>年龄</td>
<td>钱包</td>
</tr>
<#list stuMap.keys as k>
<td>${k_index + 1}</td>
<td>${stuMap[k].name}</td>
<td>${stuMap[k].age}</td>
<td>${stuMap[k].money}</td>
</tr>
</table>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: PPT 标题为“1 FreeMarker 入门”，子标题“1.1 FreeMarker介绍”。架构图：Template（包含 `<html>...<h1>Hello ${name}</h1>...</html>`）指向 FreeMarker，FreeMarker 指向 Output（包含 `<html>...<h1>Hello World!</h1>...</html>`）。
画面 9: PPT 标题为“2.3 遍历Map数据”。内容展示如何使用 `<#list stuMap.keys as k>` 指令遍历 Map。
画面 14: PPT 标题为“2.3 遍历Map数据”。内容展示如何使用 `<#list stuMap.keys as k>` 指令遍历 Map。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
