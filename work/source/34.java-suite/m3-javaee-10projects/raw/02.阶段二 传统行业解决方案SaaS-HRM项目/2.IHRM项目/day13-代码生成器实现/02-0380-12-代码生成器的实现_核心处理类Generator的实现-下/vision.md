# 画面线理解：12-代码生成器的实现：核心处理类Generator的实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\12-代码生成器的实现：核心处理类Generator的实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:25, 00:36, 00:46, 01:02, 01:08, 01:35, 02:00, 03:04, 04:02, 04:18, 04:43, 05:11, 05:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:03:24

1) 这一组画面整体在讲如何通过 Java 代码结合模板引擎（FreeMarker）实现根据数据库表结构自动生成 Java 实体类和相关文件。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Generator.java 中的 executeGenerator 方法，用于处理模板文件、设置输出路径、创建文件并调用模板处理。同时展示 main 方法，用于初始化 Generator 并执行代码生成。
画面2: 展示 GeneratorFacade.java 中的 generatorByDatabase 方法，用于遍历数据库表，获取数据模型并调用 Generator 核心类处理。
画面3: 展示 GeneratorFacade.java 中的 generatorByDatabase 方法，光标位于 for 循环内部，准备处理每个表的数据模型。
画面4: 展示 GeneratorFacade.java 的构造函数，用于初始化模板路径、输出路径、配置和数据库对象。
画面5: 展示 GeneratorFacade.java 中的代码，光标位于构造函数内部，准备初始化 Generator 核心类。
画面6: 展示 Generator.java 中的 scanAndGenerator 方法，用于扫描模板路径下的所有模板文件并进行生成。
画面7: 展示 GeneratorFacade.java 中的 getDataModel 方法，用于根据表对象获取数据模型，并自定义配置。
画面8: 展示项目结构，选中 GeneratorFacade.java，右键菜单中选择“Create Git...”。
画面9: 展示运行结果，生成的 $ClassName.java 文件为空，终端显示 Java 进程成功结束。
画面10: 展示代码生成器对话框，模板选择为“通用模板”，项目路径为“E:\Users\ThinkPad\Desktop\day13”，用户名为 root，密码为 111111。
画面11: 展示数据库管理工具界面，显示表结构，包含 id、name、age、email、phone 等字段。
画面12: 展示代码生成器对话框，模板选择为“springboot程序的模板”，项目路径为“E:\Users\ThinkPad\Desktop\day13”，用户名为 root，密码为 111111。
画面13: 展示生成的 Java 文件列表，包含 City.java、Company.java、Department.java 等实体类。
画面14: 展示 PPT 页面，标题为“2 实现代码生成”，子标题“2.1 需求分析”和“2.2 模板生成”，并列出 GeneratorFacade 和 Generator 两个类的作用。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
private void executeGenerator(Map<String, Object> dataModel, File file) throws Exception {
    //1.文件路径：E:\项目路径
    //TemplatePath：E:\项目路径
    String templateFileName = file.getAbsoluteFile().getParent().replace(this.templatePath, replacement: "");
    //2.读取文件数据
    Template template = cfg.getTemplate(templateFileName);
    template.setEncoding("utf-8"); //指定生成文件的字符编码
    //3.创建文件
    File file1 = FileUtils.mkdir("outPath", outFileName);
    FileWriter fw = new FileWriter(file1);
    template.process(dataModel, fw);
    fw.close();
}

public String processTemplateString(String templateString, Map dataModel) throws Exception {
    Template template = new StringWriter();
    Template template = new Template("ts", new StringReader(templateString), cfg);
    template.process(dataModel, out);
    return out.toString();
}

public static void main(String[] args) throws Exception {
    String templatePath = "C:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径";
    String outPath = "C:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径";
    Generator generator = new Generator(templatePath, outPath);
}
```

画面2:
```java
public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
    this.templatePath = templatePath;
    this.outPath = outPath;
    this.settings = settings;
    this.db = db;
}

/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDataBase() throws Exception {
    List<Table> tables = DataBaseUtils.getObjInfo(db);
    for (Table table : tables) {
        //为每一个table对象,进行代码生成
        //获取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("--------------------------------");
    }
}
```

画面3:
```java
/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDataBase() throws Exception {
    List<Table> tables = DataBaseUtils.getObjInfo(db);
    for (Table table : tables) {
        //为每一个table对象,进行代码生成
        //获取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("--------------------------------");
    }
}
```

画面4:
```java
/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public class GeneratorFacade {
    private String templatePath;
    private String outPath;
    private Settings settings;
    private DataBase db;
    private Generator generator;

    public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
        this.templatePath = templatePath;
        this.outPath = outPath;
        this.settings = settings;
        this.db = db;
    }
}
```

画面5:
```java
// 拷贝Generator核心处理类
Map<String, Object> dataModel = getDataModel(table);
```

画面6:
```java
public void scanAndGenerator(Map<String, Object> dataModel) throws Exception {
    //1.根据模板路径找到此路径下的所有模板文件
    List<File> fileList = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成（调用模板）
}
```

画面7:
```java
private Map<String, Object> getDataModel(Table table) {
    Map<String, Object> dataModel = new HashMap<>();
    //1.自定义配置
    dataModel.putAll(PropertiesUtils.customMap);
    //2.配置
    dataModel.put(key, table); //table.name
}
```

画面10:
```text
模板：通用模板
代码生成路径：E:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径
项目名（英文）：
包名：
项目中文名称：
作者：
数据库：
用户名：root
密码：111111
```

画面12:
```text
模板：springboot程序的模板
代码生成路径：E:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径
项目名（英文）：
包名：
项目中文名称：
作者：
数据库：
用户名：root
密码：111111
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14:
PPT 标题：2 实现代码生成
子标题：2.1 需求分析
内容：
- 为了代码更加直观和易于调用，实现代码生成共有两个类组成：
  - UI 界面统一调用入口类：GeneratorFacade
    - 方便多种界面调用，主要完成数据模型获取，调用核心代码处理类完成代码生成
  - 代码生成核心处理类：Generator
    - 根据数据模型和模板文件路径，统一生成文件到指定的输出路径

子标题：2.2 模板生成
内容：
(1) 配置统一调用入口类 GeneratorFacade
代码：
```java
// 1.根据传入数据模型信息构造数据
// 2.根据模板完成代码生成
// 3.公共数据模型Map集合（处理文件路径等公共代码替换）
public class GeneratorFacade {
    private Generator generator;
}
```

5) 无。
