# 02-代码生成器之数据模型：处理自定义properties数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\02-代码生成器之数据模型：处理自定义properties数据_【海量资源尽在 ubkz.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好那我们接下来呢就对这两块数据来做处理首先呢咱们搞的第一块就是自定义的这个数据那对于自定义数据呢咱们首先呢和用户有一个简单的说明就是说呢你可以自定义数据但是这个数据放到哪以什么的形式进行存放我们要说清楚那在我们这个工程当中我们把它放到当前项目同级目录下的properties文件当中文件夹下文件夹下
[00:33] 比如说你自己想定义一个自己的配置文件那你就new一个fail好了这个fail呢就随便写了c-u-s-t-o-m自定义的p-i-o-p-i-t-i-e-s好了这个properties文件呢咱们都知道它是一个key value形式的比如说呢这边我就来一个testkey等于testvalueOK那这样一来那这样一来在我们的程序自动加载的时候它就会去加载properties文件当中的所有properties文件
[01:05] 那把这些数据存放到MAP集合里那如何存放到MAP集合当中那在我的代码的咱们第一天写的工具类当中有这么一个Properties Utils那这个Properties Utils当中这个代码写起来比较简单那接着和各位简单的来看一下这个代码呢咱们就不是从头到尾去写了因为这个代码比较简单其实就是借助Properties这么一个对象一个一个来进行加载的
[01:33] 好了这个代码逻辑呢先简单的跟各位来做一个分析首先定义了公共map也就是自定义的数据模型map集合那这个map集合里面通过static静态代码块的形式当加载过来的时候它自动的去找相对路径properties也就是相对于当前工程src相对于当前工程src的properties目录在这那这个是找到相对目录
[02:05] 那找到相对目录之后底下调用一个方法fill utils.searchofill那这个searchofill昨天跟各位说过了它其实是查询某个目录下的所有文件那这样以来它去查询这个properties目录下的所有文件那所有文件查到了之后我开始放寻环那放寻环里面找到是properties文件因为里面有可能很多你想放的一些内容很多文件都在里面那我们只找properties的那找到properties文件大家都知道
[02:35] 大家都知道剩下的事情Properties对象一个对象认识了加载加载之后把Properties里面的所有内容存到Map集合里面即可这样一来当我的程序访问Properties Utils的时候它就会去加载Properties里面所有内容加载好了之后存到Map集合里这个代码比较简单各位应该都能看懂同时我底下写了一个问方法我们一起来试一下能不能够得到这类的内容好了我们一起来看一下
[03:06] 好了闷方法执行大家会发现里面有个test key有一个test value没错吧那有的朋友说如果有多个配置文件怎么办好了在今天的这个资料当中资源有一个代码叫做type convert properties这个呢是我们是我们当前的这个代码生成器所依赖的一个配置文件这个配置文件呢其实就定义了一点点基础内容你也可以把它copy到properties里面
[03:38] 那这个代码里面比较简单一共有这么几个两方面的内容第一方面是一个数据库里面的类型和我们Java类型的一个对照的一个关系Whatcha对应死菌好了Data代表Java的Data好了这边Test代表死菌Double对应Double等等这个应该都能看懂还有一个就是Table的前追或者后追这个Table的前追或者后追干嘛呢是这样的就是说呢在我们的数据库表里面可能是BS BS CO等等开头的
[04:07] 叫做表明比如BS下滑线userBS下滑线user那么一般转化成实体类的时候是不是不要BS下滑线只要user是不是就可以了所以这边呢我做了一个配置这个配置说你要对表的哪一部分的字符串进行删减比如说我要对PE下滑线进行删减那我这边就逗号继续PE下滑线进行配置即可所以这个也是我们公共的一个配置那这些内容呢都会通过我们这个Public Utils
[04:38] 给我加载进来我们执行一起来看那这样一来是不是所有内容都在map集合里面存放了当然了比如说有这么一个场景你想要在你的在你的模板当中定义一下比较独特的内容那独特的内容这个独特内容数据库里没有不是原数据
[04:57] 那各位可以怎么做呢是不是可以在Properties目录下创建一个自己的配置文件那这个配置文件以key value的形式是不是定义你自己的匹配关系是不是就可以了那并且呢这么一配置我自己就可以通过工具类全部存放到custom map当中那这个需要简单的说一下就是不管是用我们自己的公共配置还是用户自定义的配置这个key不能有出名
[05:27] 这个应该各位都能理解OK那这样一来呢其实我们第一方面自定义数据这块内容呢咱们就已经跟各位简单的说过了其实主要就是这个代码和刚才跟各位说的这个思想主要目的是为了用户扩展方便一些让他去加载Publish相应相对这些内容其实就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

