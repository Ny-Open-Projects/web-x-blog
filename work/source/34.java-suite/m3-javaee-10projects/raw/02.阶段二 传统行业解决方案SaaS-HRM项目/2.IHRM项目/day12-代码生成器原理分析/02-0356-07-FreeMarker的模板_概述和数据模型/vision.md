# 画面线理解：07-FreeMarker的模板：概述和数据模型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\07-FreeMarker的模板：概述和数据模型_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:22, 01:58, 02:26, 02:48, 03:35, 05:08, 05:33, 05:49, 06:13, 06:25, 06:41, 06:58, 08:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:45:51

1) 这一组画面整体在讲什么（一句话）：
演示 FreeMarker 模板引擎的基本用法，包括模板文件创建、数据模型准备、模板处理及输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Java 代码，演示如何创建 Configuration、设置模板加载器、加载模板、准备数据模型并处理模板输出。
画面 2: PPT 展示 FreeMarker 模板的组成，包括数据模型、文本、注释、插值和 FTL 指令。
画面 3: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 4: 展示 PPT 页面，同时显示了多个窗口，包括 PDF 阅读器、IDEA 项目结构和代码编辑器。
画面 5: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 6: PPT 展示 FreeMarker 模板的组成，包括数据模型、文本、注释、插值和 FTL 指令。
画面 7: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 8: 展示 PPT 页面，同时显示了多个窗口，包括 PDF 阅读器、IDEA 项目结构和代码编辑器。
画面 9: PPT 展示 FreeMarker 的数据模型，以树状结构展示 root、user 和 latestProduct。
画面 10: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 11: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 12: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 13: 展示 Java 代码，演示如何创建 FileTemplateLoader、获取模板、准备数据模型并处理模板输出。
画面 14: PPT 展示 FreeMarker 的数据模型，以树状结构展示 root、user 和 latestProduct。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class FreeMarkerTest02 {
    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载模板
        String templateString = "欢迎您，${username}";
        Template template = new Template( name: "name1", new StringReader(templateString), cfg);
        //4.准备数据模型
        Map<String, Object> dataModel = new HashMap<>();
        dataModel.put("username", "张三");
        //5.处理模板
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```

画面 5:
```java
欢迎您，${username}
```

画面 13:
```java
//2.设置模板加载器
cfg.setTemplateLoader(new FileTemplateLoader(new File(pathname: "templates")));
//3.加载模板
Template template = cfg.getTemplate( name: "template01.ftl");
//4.准备数据模型
Map<String, Object> dataModel = new HashMap<>();
//5.处理模板
//参数一：数据模型（文件输出），printWriter（控制台输出）
//参数二：writer (FileWriter (文件输出), PrintWriter (控制台输出))
//template_process(dataModel, new FileWriter(new File("C:/Users/ThinkPad/Desktop/123/test1.txt")));
template_process(dataModel, new PrintWriter(System.out));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题：2.4 Freemarker模板
2.4.1 概述
FreeMarker模板文件主要有5个部分组成：
1. 数据模型：模板能用的所有数据
2. 文本，直接输出的部分
3. 注释，即#--->格式的部分，不会输出
4. 插值（Interpolation）：即${}或者#(...)格式的部分，将使用数据模型中的部分替代输出
5. FTL指令：FreeMarker指令，和HTML标记类似，名字前加#予以区分，不会输出。

画面 6:
标题：2.4.1 概述
FreeMarker模板文件主要有5个部分组成：
1. 数据模型：模板能用的所有数据
2. 文本，直接输出的部分
3. 注释，即#--->格式的部分，不会输出
4. 插值（Interpolation）：即${}或者#(...)格式的部分，将使用数据模型中的部分替代输出
5. FTL指令：FreeMarker指令，和HTML标记类似，名字前加#予以区分，不会输出。

画面 9:
标题：2.4.2 数据模型
FreeMarker（还有模板开发者）并不关心数据是如何计算的，FreeMarker 只是知道真实的数据是什么。模板能用的所有数据被包装成 data-model 数据模型

内容：
(root)
+ user = "Big Joe"
+ latestProduct
++ url = "products/greenmouse.html"
++ name = "green mouse"

画面 10:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 11:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 12:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 14:
标题：2.4.2 数据模型
FreeMarker（还有模板开发者）并不关心数据是如何计算的，FreeMarker 只是知道真实的数据是什么。模板能用的所有数据被包装成 data-model 数据模型

内容：
(root)
+ user = "Big Joe"
+ latestProduct
++ url = "products/greenmouse.html"
++ name = "green mouse"

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
