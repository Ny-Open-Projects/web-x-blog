# 18-构造代码生成器环境：实体类和工具类介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\18-构造代码生成器环境：实体类和工具类介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 8分52秒（音频 532s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了分析的过程呢我们都已经搞定了接下来呢我们就开始着手去搭建基本的这个环境首先呢我们需要搞一个工程在里面添置所有的坐标那这个工程呢我就用我们刚才一直玩的这个测试工程来举例了就是这个code utel那这个code utel当中呢我已经把pwn文件全部都引入进来了好了这个步骤我们都已经搞定了那接下来就需要去搞一些实体类那么实体类呢刚才说过一共呢分成这么四个部分
[00:31] 有信息采集的database相关的还有工程设置相关的没错吧当然还有table相关的和column相关的这些实体类注意各位不需要各位一个一个去写了因为实在是太浪费时间了我在今天的资料当中已经给各位准备好了工具的一些代码直接拿过来就能用比如说这边我可以把它放到send.itcastgenerate好了entity这个包下右键
[01:06] 创建一个包OK那这些呢把这些实体类call过来Ctrl CCtrl Vsetting好了还有Ctrl CCtrl Vcopy过来那call的实体类呢各位简单来看一下首先呢database这个database呢写的这个代码呢写的稍微有一点点多我想跟各位简单的解释一下为什么设置成这个逻辑首先呢注意来看数据库类型那数据库类型其实就是我们图片
[01:43] 这边让你填写的比如说可以填写MySQL或者Oracle没错吧好了接下来用户名密码用户名密码这也都好理解用户密码这个也都好理解这个放到上边好了接下来还有两个一个叫driver一个叫做url这个driver应该如何去做我们都知道根据数据库类型我们自己就能拼接出driver没错吧所以各位来看我这边写了一个构造函数
[02:14] 那这个构造函数我接收三个参数这三个参数接收这么四个参数抱歉四个参数第一个参数数据库类型第二个参数是IP因为你在页面前端传递的IP地址127.0.1没错吧OK那这边呢还有你可以去选择你的数据库比如说呢我的数据库DB叫做IHRM那part我们默认就是3306
[02:42] 那接下来我想说你只有这些基本的数据只有这些基本的数据那这些基本的数据能够帮助我们连接数据库吗显然不能没错吧因为我们要有驱动那驱动如何判断如果是一个MySQL的话我这边com.mySQL.driver那如果是MySQL的话我这个UIL其实不能直接写127.0.1因为我们这边是不是要通过JDBC的形式来进行连接
[03:10] 所以我这边写了一个内置字符串这个内置字符串留了这么几个小小的被替换的内容比如说IP比如说的Port比如说的DB那我们要做的事情是不是对这个字符串进行一个简单的处理把你输入的IP替换到中框IP把你输入的Port替换到Port把你输入的DB抱歉把你输入的DB名称是不是替换过来那经过一替换之后我们这边经过替换之后我们这边
[03:43] 变成了127.0.0.13306是不是叫做IHM那这样一来我们是不是连接数据库的UIL就已经都准备好了没错吧所以这个代码比较简单主要目的就是构造用户数内容DatabaseOK那Database我们看过了之后接下来还有一个Siting那这个Siting里面这边还有一点点简单的错误这个不用管它不用管它一会儿咱们做一些箱子操作就可以了
[04:13] 那这个setting当中呢这个内容呢就是更简单了首先跟我们输入的内容一一相关输入的内容一一相关首先第一个projectproject代表的是你项目名称你这个项目名究竟叫啥随便写好了还有一个包名那这个包名呢其实就是一个完整的路径比如说呢cn.itcast.比如说就是im那这个im注意包名就在这儿包名就在这儿
[04:45] 那接下来呢我想说的是那这个包名其实对应到我们真正的一个Java程序当中是不是应该是一个这种结构CN这是一个一级目录接着再进来ITCast好了接着再进来HRIIHM没错吧所以我要做的事情呢我可以把这个字幕串呢把它分成这么几个结构第一个路径第二个路径第三个路径这个能不能理解
[05:16] 好了所以这边呢虽然你传递的是叫cn.itcast.it.ihm我呢把你分成了三段能理解吧OK那接下来呢还有一个就是我们的project工程的中文描述信息还有当前的一个作者当然这个pass就是完整的路径是一个做拼接的这么一个过程OK好了那这个setting也简单说过接下来呢就是table那table呢就是我们真正要查询数据库构造成的实体类
[05:47] table接着还有一个叫做column这column就是列的相关内容刚才咱们都做过简单介绍了OK实体类我们已经copy过来之后还需要一些基本的我们叫做utils工具类在这边我也刷新一个包cn.itcast.generate这些工具类在今天资料当中也给各位准备好了
[06:19] 那这些工具类呢在UtilsCtrl C也copy过来好了这些工具类当中有什么第一个死菌Utils这个死菌Utils里面的内容比较多主要涉及的就是一个字符串转化字符串替换字符串判断的这么一个过程这里面内容由于比较多呀我们用到哪个说哪个其实就可以了当然了有的朋友其实可以通过里面的一些方法名就能看到我是干嘛的就判断字符串是否是空是否是非空得到某一个字符串的后缀名啊等等等等
[06:51] OK第一个不说了这个比较简单好了第二个Fill Utils那Fill Utils主要目的其实就是创建文件的时候可能要对文件进行操作那把文件操作的相关内容我也封装到一个工具类里面了里面比如说可以创建文件可以递归获取某一个目录下的所有文件比如说还有得到某一个文件的一个相对路径OK那好了接着还有一个Property Utils
[07:20] 那这个Property Utils它的主要目的就是去读取主要目的就是去读取咱们自己的一些配置包含用户自定义一些配置那不管是我们自己的配置还是用户自定义的配置我都要把它放到我当前工程的某一个文件夹下New一个Directly
[07:47] 注意我读的是当前SRC相对路径的Properties目录这是目录也就是说你必须把所有的文件配置文件写到Properties这个目录下才能用当然了你的文件名也是得是一个Properties文件这边读的就是.Properties文件所以对于不管是我们自己的一些配置文件还是其他人的一些配置文件都需要我们有一个约定需要将自定义的配置信息
[08:20] 写入到PiO PiTIS文件中那这个Property文件需要配置到相对于工程的文件夹下这个也能理解吧当然了你这个我叫Properties你可以改成中文叫配置都可以OK那这样一来我当前的实体类已经有了操作的这个工具类也给各位准备好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并使用代码生成器（基于Freemarker）来自动生成Java实体类和相关工具类，包括环境搭建、依赖配置、数据库连接设置和模板文件处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了PDF文档中“4.2 搭建环境”章节的“4.2.1 配置坐标”部分。
- 文档中列出了代码生成所需的操作步骤。
- 显示了Maven依赖配置代码：
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.freemarker</groupId>
          <artifactId>freemarker</artifactId>
          <version>2.3.20</version>
      </dependency>
      <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.12</version>
          <scope>test</scope>
      </dependency>
      <dependency>
          <groupId>mysql</groupId>
          <artifactId>mysql-connector-java</artifactId>
          <version>5.1.8</version>
      </dependency>
  </dependencies>
  ```

画面2：
- 展示了IntelliJ IDEA中项目结构，选中了“Find Usages”选项。
- 未显示具体代码内容。

画面3：
- 展示了IntelliJ IDEA中`Column.java`文件的内容，该文件定义了实体类`Column`。
- 代码中包含字段如`columnName`、`columnDbType`等及其对应的getter和setter方法。

画面4：
- 展示了PDF文档中“4.2 搭建环境”章节的“4.2.1 配置坐标”部分。
- 文档中列出了代码生成所需的操作步骤。
- 显示了Maven依赖配置代码（与画面1相同）。

画面5：
- 展示了IntelliJ IDEA中`DataBase.java`文件的内容，该文件定义了数据库连接类。
- 代码中包含数据库连接构造函数和根据数据库类型设置驱动和URL的方法。

画面6：
- 展示了IntelliJ IDEA中`Column.java`文件的内容，该文件定义了实体类`Column`。
- 代码中包含字段如`columnName`、`columnDbType`等及其对应的getter和setter方法。

画面7：
- 展示了IntelliJ IDEA中`Column.java`文件的内容，该文件定义了实体类`Column`。
- 代码中包含字段如`columnName`、`columnDbType`等及其对应的getter和setter方法。

画面8：
- 展示了PDF文档中“4.2 搭建环境”章节的“4.2.1 配置坐标”部分。
- 文档中列出了代码生成所需的操作步骤。
- 显示了Maven依赖配置代码（与画面1相同）。

画面9：
- 展示了Windows资源管理器中`cn`目录下的文件夹结构。
- 显示了`day1`至`day12`的文件夹。

画面10：
- 展示了IntelliJ IDEA中`Column.java`文件的内容，该文件定义了实体类`Column`。
- 代码中包含字段如`columnName`、`columnDbType`等及其对应的getter和setter方法。

画面11：
- 展示了IntelliJ IDEA中`Column.java`文件的内容，该文件定义了实体类`Column`。
- 代码中包含字段如`columnName`、`columnDbType`等及其对应的getter和setter方法。

画面12：
- 展示了IntelliJ IDEA中`FileUtils.java`文件的内容，该文件定义了文件处理工具类。
- 代码中包含获取相对路径、搜索所有文件和递归搜索子目录文件的方法。

画面13：
- 展示了IntelliJ IDEA中项目结构，选中了`FileUtils`类。
- 未显示具体代码内容。

画面14：
- 展示了IntelliJ IDEA中`PropertiesUtils.java`文件的内容，该文件定义了属性文件处理工具类。
- 代码中包含读取配置文件并加载到Map中的方法，以及一个main方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependencies>
    <dependency>
        <groupId>org.freemarker</groupId>
        <artifactId>freemarker</artifactId>
        <version>2.3.20</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.8</version>
    </dependency>
</dependencies>
```

画面3：
```java
package cn.itcast.generate.entity;

/**
 * 列对象
 */
public class Column {
    private String columnName;//列名称
    private String columnName2;//列名称(处理后的列名称)
    private String columnType;//列类型
    private String columnDbType;//列的数据类型
    private String columnComment;//列备注
    private String columnKey;//是否主键
    public String getColumnName() { return columnName; }
    public void setColumnName(String columnName) { this.columnName = columnName; }
    public String getColumnName2() { return columnName2; }
    public void setColumnName2(String columnName2) { this.columnName2 = columnName2; }
    public String getColumnType() { return columnType; }
    public void setColumnType(String columnType) { this.columnType = columnType; }
    public String getColumnDbType() { return columnDbType; }
    public void setColumnDbType(String columnDbType) { this.columnDbType = columnDbType; }
    public String getColumnComment() { return columnComment; }
    public void setColumnComment(String columnComment) { this.columnComment = columnComment; }
    public String getColumnKey() { return columnKey; }
    public void setColumnKey(String columnKey) { this.columnKey = columnKey; }
}
```

画面5：
```java
private String password;
private String driver;
private String url;
public DataBase() {}
public DataBase(String dbType, String db) {
    this.dbType = dbType;
    this.url = "jdbc:mysql://127.0.0.1:3306/";
}
public DataBase(String dbType, String ip, String port, String db) {
    this.dbType = dbType;
    if("MYSQL".equalsIgnoreCase(dbType)) {
        this.driver = "com.mysql.jdbc.Driver";
        this.url = "jdbc:mysql://" + ip + ":" + port + "/" + db;
    }else{
        this.driver = "oracle.jdbc.driver.OracleDriver";
        this.url = "jdbc:oracle:thin:@" + ip + ":" + port + ":" + db;
    }
}
```

画面6：
```java
package cn.itcast.generate.entity;

/**
 * 列对象
 */
public class Column {
    private String columnName;//列名称
    private String columnName2;//列名称(处理后的列名称)
    private String columnType;//列类型
    private String columnDbType;//列的数据类型
    private String columnComment;//列备注
    private String columnKey;//是否主键
    public String getColumnName() { return columnName; }
    public void setColumnName(String columnName) { this.columnName = columnName; }
    public String getColumnName2() { return columnName2; }
    public void setColumnName2(String columnName2) { this.columnName2 = columnName2; }
    public String getColumnType() { return columnType; }
    public void setColumnType(String columnType) { this.columnType = columnType; }
    public String getColumnDbType() { return columnDbType; }
    public void setColumnDbType(String columnDbType) { this.columnDbType = columnDbType; }
    public String getColumnComment() { return columnComment; }
    public void setColumnComment(String columnComment) { this.columnComment = columnComment; }
    public String getColumnKey() { return columnKey; }
    public void setColumnKey(String columnKey) { this.columnKey = columnKey; }
}
```

画面12：
```java
package cn.itcast.generate.utils;

/**
 * 文件处理工具类
 */
public class FileUtils {
    //得到相对路径
    public static String getRelativePath(File baseDir, File file) {
        if(baseDir.equals(file) == null) {
            return file.getAbsolutePath().substring(baseDir.getAbsolutePath().length());
        }
        return file.getAbsolutePath().substring(baseDir.getAbsolutePath().length() + 1);
    }
    //遍历某个目录下的所有文件
    public static List<File> searchAllFile(File dir) throws IOException {
        ArrayList arrayList = new ArrayList();
        searchAll(dir, arrayList);
        return arrayList;
    }
    //递归获取某个目录下的所有文件
    public static void searchFiles(File dir, List<File> collector) throws IOException {
        if(dir.isDirectory()) {
            File[] subFiles = dir.listFiles();
            for(int i = 0; i < subFiles.length; i++) {
                searchFiles(subFiles[i], collector);
            }
        }
    }
}
```

画面14：
```java

