# 画面线理解：08-代码生成器的实现：测试GeneratorFacade获取数据模型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\08-代码生成器的实现：测试GeneratorFacade获取数据模型_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:39, 00:52, 01:05, 01:27, 01:37, 02:09, 03:09, 03:19, 04:15, 04:34, 04:52, 05:16, 06:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:59:59

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Java 的数据库逆向工程代码生成器的实现，包括核心生成逻辑、数据模型构建、UI 界面调用及配置文件的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 GeneratorFacade.java 文件中构造函数和 generatorByDatabase 方法的代码，注释说明了“准备数据模型”和“调用核心处理类完成代码生成”。
画面 2: 在 generatorByDatabase 方法中，光标位于 for 循环的开始处，IDE 显示了 Map.Entry 的自动补全建议。
画面 3: 光标移动到 for 循环的末尾，IDE 显示了 Map.Entry 的方法列表，如 getkey()、getValue() 等。
画面 4: 光标在 for 循环内部，调用 entry.getKey() 和 entry.getValue()，并打印输出。
画面 5: 展示项目结构，选中了 CodeUtil.java 文件，终端显示了运行命令。
画面 6: 展示 CodeUtil.java 文件中 generator 方法的代码，注释说明了参数含义。
画面 7: 光标在 generator 方法的末尾，准备添加代码。
画面 8: 展示项目结构，选中了 DatabaseUtil.java 文件，终端显示了运行命令。
画面 9: 展示 DatabaseUtil.java 文件中 main 方法的代码，注释说明了参数含义。
画面 10: 光标在 main 方法中，准备添加代码。
画面 11: 展示项目结构，选中了 custom.properties 文件，终端显示了编译成功。
画面 12: 展示 GeneratorFacade.java 文件中 generator 方法的代码，注释说明了“根据 Table 对象获取数据模型”。
画面 13: 展示一个“代码生成器 1.0”的弹窗界面，用户输入了项目名、包名、作者等信息。
画面 14: 展示 custom.properties 文件的内容，其中定义了数据库字段类型映射和项目配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private String outPath;
private Settings settings;
private DataBase db;

public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
    this.templatePath = templatePath;
    this.outPath = outPath;
    this.settings = settings;
    this.db = db;
}

/**
 * 1.准备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDatabase() throws Exception {
    List<Table> tables = DataBaseUtils.getDbInfo(db);
    for (Table table : tables) {
        //对每一个Table对象进行代码生成
        //读取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
    }
}
```

画面 2:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 3:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 4:
```java
for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
    System.out.println(entry.getKey() + "--" + entry.getValue());
}
```

画面 5:
```java
//UI调用程序入口
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选择代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    System.out.println(templatePath);
    System.out.println(outpath);
    System.out.println(settings);
    System.out.println(db);
    GeneratorFacade gf = new GeneratorFacade(templatePath, outpath, settings, db);
    gf.generatorByDatabase();
}
```

画面 6:
```java
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选择代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    System.out.println(templatePath);
    System.out.println(outpath);
    System.out.println(settings);
    System.out.println(db);
    GeneratorFacade gf = new GeneratorFacade(templatePath, outpath, settings, db);
    gf.generatorByDatabase();
}
```

画面 7:
```java
/**
 * @param templatePath
 * 模板所在路径
 * @param outpath
 * 选代码生成路径
 * @param settings
 * 工程配置对象
 * @param db
 * 数据库信息
 */
private void generator(String templatePath, String outpath, Settings settings, DataBase db) {
    GeneratorFacade facade = new GeneratorFacade(templatePath, outpath, settings, db);
    facade.generatorByDatabase();
}
```

画面 8:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 9:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 10:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 11:
```properties
author=itcast
CHAR=String
project=String
BIGINT=Long
TEXT=String
VARCHAR=String
INT=Integer
path1=String
path2=String
path3=String
projectComment=String
table=Table(name='sys_file', name2='SysFile', comment='', keys='id', columns=[Column(columnName='id', columnName2='id', columnType='String')
author=itcast
project=String
```

画面 12:
```java
/**
 * @param args the command line arguments
 */
public static void main(String[] args) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
```

画面 13:
```java
//代码生成器 1.0
模板: springboot模板的模板
代码生成路径: E:\test
项目名（英文）:
包名:
项目中文名称:
作者:
数据库名: itim
用户名: root
密码: 111111
生成代码
关闭
```

画面 14:
```properties
author=itcast
CHAR=String
project=String
BIGINT=Long
TEXT=String
VARCHAR=String
INT=Integer
path1=String
path2=String
path3=String
projectComment=String
table=Table(name='sys_file', name2='SysFile', comment='', keys='id', columns=[Column(columnName='id', columnName2='id', columnType='String')
author=itcast
project=String
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
