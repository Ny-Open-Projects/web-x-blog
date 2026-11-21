# 画面线理解：10-代码生成器的实现：核心处理类Generator的实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\10-代码生成器的实现：核心处理类Generator的实现-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:48, 02:31, 03:08, 06:12, 06:39, 07:03, 08:39, 09:55, 10:48, 11:34, 11:48, 12:28, 13:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:01:33

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java 中的 FreeMarker 模板引擎，通过代码动态生成文件，包括配置模板加载器、扫描模板文件、处理数据模型并输出生成文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Generator.java 文件的开头部分，定义了模板路径、输出路径和配置对象，并初始化了 FileTemplateLoader。
画面2：在代码编辑器中，光标位于“File”类的自动补全列表中，准备输入“File”。
画面3：在代码编辑器中，光标位于“Print”类的自动补全列表中，准备输入“Print”。
画面4：展示 Generator.java 文件中 scanAndGenerator 方法的注释和部分代码，用于扫描模板路径下的所有模板文件并逐个生成。
画面5：在代码编辑器中，光标位于“String”类的自动补全列表中，准备输入“String”。
画面6：展示 Windows 文件资源管理器，路径为 E:\hrm，选中了名为“模板文件.txt”的文件。
画面7：在文件资源管理器中，选中了名为“新建文本文件.txt”的文件。
画面8：展示 Generator.java 文件中 generatorByDatabase 方法的注释和部分代码，用于根据数据库表生成模板。
画面9：展示 Generator.java 文件中 scanAndGenerator 方法的注释和部分代码，用于扫描模板路径下的所有模板文件并逐个生成。
画面10：在代码编辑器中，弹出“Select Classes to Import”对话框，选中了“freemarker.template.Template”类。
画面11：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。
画面12：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。
画面13：在代码编辑器中，光标位于“String”类的自动补全列表中，准备输入“String”。
画面14：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import java.io.File;
import java.io.IOException;
import java.util.Map;

/**
 * 代码生成器的核心处理类
 * 使用Freemaker完成文件生成
 * @author
 * 数据模型
 * 模板的位置
 * 生成文件的路径
 */
public class Generator {
    private String templatePath;//模板路径
    private String outPath;//代码生成路径
    private Configuration cfg;

    public Generator(String templatePath, String outPath) throws Exception {
        this.templatePath = templatePath;
        this.outPath = outPath;
        //初始化Configuration对象
        cfg = new Configuration();
        FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
        cfg.setTemplateLoader(ftl);
    }
```

画面4：
```java
/**
 * 扫描生成
 * 1.扫描模板路径下的所有模板
 * 2.对每个模板进行文件生成（默认模板文件）
 */
public void scanAndGenerator(Map<String,Object> dataModel) throws IOException {
    //1.根据模板路径获取此路径下所有模板文件
    List<File> filelist = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成
    for (File file : filelist) {
        executeGenerator(dataModel,file);
    }
}
```

画面8：
```java
/**
 * 根据数据库表生成模板
 */
public void generatorByDatabase() throws Exception {
    List<Table> tables = DatabaseUtilis.getTbInfo(db);
    for (Table table : tables) {
        //对每个table对象进行代码生成
        Map<String,Object> dataModel = getDataModel(table);
        for(Map.Entry<String,Object> entry:dataModel.entrySet()){
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("........................");
    }
}
```

画面9：
```java
/**
 * 扫描生成
 * 1.扫描模板路径下的所有模板
 * 2.对每个模板进行文件生成（默认模板文件）
 */
public void scanAndGenerator(Map<String,Object> dataModel) throws IOException {
    //1.根据模板路径获取此路径下所有模板文件
    List<File> filelist = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成
    for (File file : filelist) {
        executeGenerator(dataModel,file);
    }
}
```

画面10：
```java
// Select Classes to Import
// The code fragment which you have pasted uses classes that are not accessible by imports in the new context.
// Select classes that you want to import to the new file
freemarker.template.Template
```

画面11：
```java
/**
 * 1.读取文件模板
 * 2.创建文件
 * 3.模板处理（文件生成）
 */
public void processTemplateString(String templateString,Map dataModel) throws Exception {
    //1.字符串模板
    String templateString = "欢迎${username}";
    //2.创建模板
    Template template = new Template(name:"nam1",new StringReader(templateString),cfg);
    //3.处理模板
    Map<String,Object> dataModel = new HashMap<>();
    dataModel.put("username","张三");
    //4.处理模板
    template.process(dataModel,new PrintWriter(System.out));
}
```

画面12：
```java
private void executeGenerator(Map<String,Object> dataModel,file file) throws Exception {
    //1.文件路径处理
    String templateFileName = file.getAbsolutePath().replace(this.templatePath, replacement: "");
    //2.读取文件模板
    //3.创建文件
    //4.模板处理（文件生成）
}
```

画面13：
```java
public String processTemplateString(String templateString,Map dataModel) throws Exception {
    StringWriter out = new StringWriter();
    Template template = new Template(name:"ts",new StringReader(templateString),cfg);
    template.process(dataModel,out);
    return out.toString();
}
```

画面14：
```java
public String processTemplateString(String templateString,Map dataModel) throws Exception {
    StringWriter out = new StringWriter();
    Template template = new Template(name:"ts",new StringReader(templateString),cfg);
    template.process(dataModel,out);
    return out.toString();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
