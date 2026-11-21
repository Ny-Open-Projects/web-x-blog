# 画面线理解：08-FreeMarker的模板：if指令和list指令

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\08-FreeMarker的模板：if指令和list指令_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:27, 02:00, 02:50, 03:58, 04:42, 05:47, 06:16, 07:09, 07:43, 08:42, 09:20, 09:38, 10:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:46:32

1) 这一组画面整体在讲什么（一句话）：
讲解 FreeMarker 模板引擎的常用标签和指令，通过 Java 代码演示如何加载模板、传入数据模型并输出结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：PPT页面，标题“2.4.3 模板的常用标签”，展示 FreeMarker 模板数据结构示例：(root) + user = "Big Joe" + latestProduct + url = "products/greenmouse.html" + name = "green mouse"，并列出标签类型：$(...)、<#if>、<#else>、<#assign>。
画面2：PPT页面，标题“2.4.3 模板的常用标签”，内容与画面1相同，顶部有“黑马程序员”Logo和联系方式。
画面3：PPT页面，标题“2.4.3 模板的常用标签”，内容与画面1相同，下方开始出现“2.4.4 模板的常用指令”标题。
画面4：IDEA 编辑器，打开 `template01.ftl` 文件，光标在第一行，内容为：欢迎，${username}。
画面5：IDEA 编辑器，`template01.ftl` 文件中添加了条件判断标签：<#if flag==1>...<#else>...</#if>。
画面6：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#if flag==1>` 行，显示了条件判断标签。
画面7：IDEA 编辑器，显示 `FreeMarkerTest01.java` 文件，代码为：
```java
public class FreeMarkerTest01 {
    @Test
    public void test01() throws Exception {
        //1.创建FreeMarker配置，有模板存入缓存中
        Configuration cfg = new Configuration();
        //2.指定模板路径，将模板存入缓存中
        FileTemplateLoader ftl = new FileTemplateLoader(new File(pathname: "templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate(name: "template01.ftl");
        //4.创建数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //user对象
        dataModel.put("username", "传智播客");
        dataModel.put("flag", 3);
        //文件输出
        //处理模型
        //参数一：数据模型
        //参数二：writer（fileWriter（文件输出）.printWriter（控制台输出））
        //template.process(dataModel,new FileWriter(new File("C:\\Users\\ThinkPad\\Desktop\\zhrm\\day12\\test1.txt")));
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```
画面8：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#if flag==1>` 行，显示了条件判断标签。
画面9：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `list<String> list` 行，显示了创建列表的代码。
画面10：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `list.add("星期一");` 行，显示了添加列表元素的代码。
画面11：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `dataModel.put("weeks", list);` 行，显示了将列表放入数据模型的代码。
画面12：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `Configuration cfg = new Configuration();` 行，显示了创建配置对象的代码。
画面13：Word 文档，内容为：
1. 动态页面：
   替换 jsp
2. 静态化：
3. 代码生成器
画面14：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#list weeks as abc>` 行，显示了遍历列表的标签。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7：
```java
public class FreeMarkerTest01 {
    @Test
    public void test01() throws Exception {
        //1.创建FreeMarker配置，有模板存入缓存中
        Configuration cfg = new Configuration();
        //2.指定模板路径，将模板存入缓存中
        FileTemplateLoader ftl = new FileTemplateLoader(new File(pathname: "templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate(name: "template01.ftl");
        //4.创建数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //user对象
        dataModel.put("username", "传智播客");
        dataModel.put("flag", 3);
        //文件输出
        //处理模型
        //参数一：数据模型
        //参数二：writer（fileWriter（文件输出）.printWriter（控制台输出））
        //template.process(dataModel,new FileWriter(new File("C:\\Users\\ThinkPad\\Desktop\\zhrm\\day12\\test1.txt")));
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```

画面9：
```java
list<String> list
```

画面10：
```java
list.add("星期一");
```

画面11：
```java
dataModel.put("weeks", list);
```

画面12：
```java
Configuration cfg = new Configuration();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、2、3：PPT标题“2.4.3 模板的常用标签”，内容包括：
- 数据结构示例：(root) + user = "Big Joe" + latestProduct + url = "products/greenmouse.html" + name = "green mouse"
- 标签类型：
  1. $(...)：称为interpolations，FreeMarker会在输出时用实际值进行替代。
     - $(name)可以取得root中key为name的value。
     - $(person.name)可以取得成员变量为person的name属性。
  2. <#if>：FTL标记（FreeMarker模板语言标记）：类似于HTML标记，为了与HTML标记区分。
  3. <#else>：宏，自定义标签。
  4. 注释：包含在<#-- 和 -->之间。

画面13：Word 文档，内容为：
1. 动态页面：
   替换 jsp
2. 静态化：
3. 代码生成器

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
