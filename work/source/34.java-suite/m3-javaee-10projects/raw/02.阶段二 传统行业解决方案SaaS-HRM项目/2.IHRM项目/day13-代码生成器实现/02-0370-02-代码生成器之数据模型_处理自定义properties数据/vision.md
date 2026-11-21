# 画面线理解：02-代码生成器之数据模型：处理自定义properties数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\02-代码生成器之数据模型：处理自定义properties数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:12, 00:47, 01:20, 01:55, 02:17, 03:03, 03:24, 03:47, 04:16, 04:36, 05:12, 05:33, 05:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:55:01

1) 这一组画面整体在讲什么（一句话）：
讲解如何通过 PropertiesUtils 工具类加载并统一管理项目中多个 .properties 文件，以支持代码生成器的自定义数据配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 第 1.1 节“需求分析”，内容提到使用 Freemarker 生成代码时，数据模型 = 文件，需处理数据库字段和用户自定义数据。
画面 2: 展示 Table.java 文件，其中定义了实体类属性，如 name、comment、key、columns，并提供 getter/setter 方法。
画面 3: 展示项目结构，选中 custom.properties 文件，准备创建或编辑自定义配置文件。
画面 4: 展示 PropertiesUtils.java 文件，其中定义了静态 Map 用于存储配置，并包含加载 .properties 文件的逻辑。
画面 5: 展示项目结构，选中 properties 文件夹，准备处理自定义配置文件。
画面 6: 展示 PropertiesUtils.java 文件，聚焦于加载 .properties 文件的代码块。
画面 7: 展示 custom.properties 文件，内容为空，准备添加自定义配置。
画面 8: 展示文件资源管理器，显示 day13 目录下的 city.sql 和 typeConverter.properties 文件。
画面 9: 展示 typeConverter.properties 文件内容，包含 SQL 类型与 Java 类型的映射规则和表前缀移除规则。
画面 10: 展示 typeConverter.properties 文件，光标位于 tableRemovePrefixes 配置行。
画面 11: 展示 PropertiesUtils.java 文件，聚焦于 main 方法，用于打印加载的配置。
画面 12: 展示 PropertiesUtils.java 文件，光标位于 main 方法的结束大括号。
画面 13: 展示课程 PPT 第 1.2 节“自定义数据”，内容说明通过 PropertiesUtils 工具类统一加载 .properties 文件。
画面 14: 展示课程 PPT 第 1.2 节“自定义数据”，内容与画面 13 相同，同时显示了两个 IDE 窗口的分屏视图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public class Table {
    private String name;//表名
    private String name2;//处理后的表名
    private String comment;//注释
    private String key;//主键
    private List<Column> columns;//列集合

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getName2() { return name2; }
    public void setName2(String name2) { this.name2 = name2; }
    public String getComment() { return comment; }
    public void setComment(String comment) { this.comment = comment; }
    public String getKey() { return key; }
    public void setKey(String key) { this.key = key; }
}
```

画面 4:
```java
public class PropertiesUtils<String> {
    public static Map<String,String> customMap = new HashMap<>();

    static {
        File dir = new File("properties");
        try {
            List<File> files = FileUtils.searchAllFile(new File(dir.getAbsolutePath()));
            for (File file : files) {
                if(file.getName().endsWith(".properties")) {
                    Properties prop = new Properties();
                    prop.load(new FileInputStream(file));
                    customMap.putAll((Map) prop);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        PropertiesUtils.customMap.forEach((k, v) -> {
            System.out.println(k+"--"+v);
        });
    }
}
```

画面 9:
```properties
#SQL类型与Java类型转换规则
VARCHAR=String
BIGINT=Long
INT=Integer
DATE=java.util.Date
DATETIME=java.util.Date
DOUBLE=Double
TEXT=String
VARCHAR2=String
MARCHAR2=String
NUMBER=long
CHAR=String
#表的前缀或者后缀
tableRemovePrefixes="th_,co_"
```

画面 13:
```java
/**
 * 需要将自定义的配置信息写入到properties文件中
 * 配置到相对于工程的properties文件夹下
 */
public class propertiesutils {
    public static Map<string,String> custommap = new HashMap<>();

    static {
        File dir = new File("properties");
        try {
            List<File> files = FileUtils.searchAllFile(new File(dir.getAbsolutePath()));
            for (File file : files) {
                if(file.getName().endsWith(".properties")) {
                    Properties prop = new Properties();
                    prop.load(new FileInputStream(file));
                    custommap.putAll((Map) prop);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1 构造数据模型”，子标题“1.1 需求分析”，内容包括“借助 Freemarker 机制...”、“数据库字段、字段等信息”、“用户自定义的数据”。
画面 13: PPT 标题为“1.2 自定义数据”，内容包括“通过 PropertiesUtils 工具类...”、“需要将自定义的配置信息写入到 properties 文件中”、“配置到相对于工程的 properties 文件夹下”。
画面 14: PPT 标题为“1.2 自定义数据”，内容与画面 13 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
