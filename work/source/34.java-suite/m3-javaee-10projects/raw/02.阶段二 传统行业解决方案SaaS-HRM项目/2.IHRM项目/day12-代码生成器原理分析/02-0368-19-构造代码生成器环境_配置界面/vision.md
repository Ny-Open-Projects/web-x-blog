# 画面线理解：19-构造代码生成器环境：配置界面

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\19-构造代码生成器环境：配置界面_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:31, 02:15, 02:47, 03:11, 04:15, 04:57, 05:35, 05:58, 06:31, 07:36, 08:15, 09:08, 10:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:53:44

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 工具类连接数据库、获取数据库元数据，并为后续代码生成准备环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了“代码生成器 v1.0”工具的两个配置窗口，左侧是数据库连接配置（服务IP: 127.0.0.1），右侧是工程配置（项目名称、作者等），并用红色箭头指示配置流程。
画面 2: 显示了 IntelliJ IDEA 中的 `DataBaseMetaTest.java` 文件，内容为空，用于后续测试。
画面 3: 显示了 `DataBaseUtils.java` 文件的代码，包含获取数据库连接的静态方法 `getConnection()`，其中使用了 `Properties`、`DriverManager` 等类。
画面 4: 在 `getConnection()` 方法中，代码已修改为使用 `db` 对象获取数据库连接信息，包括 URL、用户名、密码等。
画面 5: 代码中 `getConnection()` 方法已完善，使用 `db` 对象获取数据库连接信息。
画面 6: 在 `getSchemas()` 方法中，代码已修改为使用 `db` 对象获取数据库连接信息。
画面 7: 在 `getSchemas()` 方法中，代码已修改为使用 `db` 对象获取数据库连接信息。
画面 8: 展示了 Windows 资源管理器中 `day12` 目录下的 `ui` 文件夹，其中包含 `CodeUtil.form`、`DatabaseUtil.form`、`DatabaseUtil.java` 等文件。
画面 9: 在 IntelliJ IDEA 中，`DatabaseUtil.java` 文件的代码已修改，包含获取数据库连接和获取数据库列表的方法。
画面 10: 在 `DatabaseUtil.java` 文件中，代码已修改，包含 `main` 方法和 `JButton`、`JComboBox` 等组件的声明。
画面 11: 在 IntelliJ IDEA 中，弹出“新建目录”对话框，提示输入新目录名。
画面 12: 在 IntelliJ IDEA 中，`DatabaseUtil.java` 文件的代码已修改，包含获取数据库连接和获取数据库列表的方法。
画面 13: 在 IntelliJ IDEA 中，弹出“代码生成器”对话框，配置了生成路径和文件类型。
画面 14: 在 IntelliJ IDEA 中，`CodeUtil.java` 文件的代码已修改，包含 `generator` 方法，用于生成代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
import java.util.Properties;
public class DataBaseUtils {
    //获取到mysql中所有的数据库名称
    //获取到mysql中所有的数据库名称
    public static Connection getConnection() throws Exception {
        String url = "jdbc:mysql://127.0.0.1:3306/";
        String user = "root";
        String password = "123456";
        String driver = "com.mysql.jdbc.Driver";
        Properties props = new Properties();
        props.put("remarksReporting","true");//获取数据库的备注信息
        props.put("user",user);
        props.put("password",password);
        Class.forName(driver);//注册驱动
        connection = DriverManager.getConnection(url,props);
    }
}
```

画面 4 代码：
```java
public static Connection getConnection(Database db) throws Exception {
    Properties props = new Properties();
    props.put("remarksReporting","true");//获取数据库的备注信息
    props.put("user",db.getUserName());
    props.put("password",db.getPassword());
    Class.forName(db.getDriver());//注册驱动
    connection = DriverManager.getConnection(db.getUrl(),props);
}
```

画面 5 代码：
```java
public static Connection getConnection(Database db) throws Exception {
    Properties props = new Properties();
    props.put("remarksReporting","true");//获取数据库的备注信息
    props.put("user",db.getUserName());
    props.put("password",db.getPassword());
    Class.forName(db.getDriver());//注册驱动
    return DriverManager.getConnection(db.getUrl(),props);
}
```

画面 6 代码：
```java
public static List<String> getSchemas(Database db) throws Exception {
    Connection connection = getConnection(db);
    DatabaseMetaData metaData = connection.getMetaData();
    //获取所有的数据库列表
    ResultSet rs = metaData.getCatalogs();
    List<String> list = new ArrayList<>();
    while (rs.next()) {
        list.add(rs.getString(columnindex: 1));
    }
    rs.close();
    connection.close();
    return list;
}
```

画面 7 代码：
```java
public static List<String> getSchemas(Database db) throws Exception {
    Connection connection = getConnection(db);
    DatabaseMetaData metaData = connection.getMetaData();
    //获取所有的数据库列表
    ResultSet rs = metaData.getCatalogs();
    List<String> list = new ArrayList<>();
    while (rs.next()) {
        list.add(rs.getString(columnindex: 1));
    }
    rs.close();
    connection.close();
    return list;
}
```

画面 9 代码：
```java
public class DataBaseUtil {
    //获取到mysql中所有的数据库名称
    //获取到mysql中所有的数据库名称
    public static Connection getConnection(Database db) throws Exception {
        Properties props = new Properties();
        props.put("remarksReporting","true");//获取数据库的备注信息
        props.put("user",db.getUserName());
        props.put("password",db.getPassword());
        Class.forName(db.getDriver());//注册驱动
        return DriverManager.getConnection(db.getUrl(),props);
    }
    //获取数据库列表
    public static List<String> getSchemas(Database db) throws Exception {
        Connection connection = getConnection(db);
        DatabaseMetaData metaData = connection.getMetaData();
        //获取所有的数据库列表
        ResultSet rs = metaData.getCatalogs();
        List<String> list = new ArrayList<>();
        while (rs.next()) {
            list.add(rs.getString(columnindex: 1));
        }
        rs.close();
        connection.close();
        return list;
    }
}
```

画面 10 代码：
```java
public static void main(String args[]) {
    java.awt.EventQueue.invokeLater(new Runnable() {
        public void run() {
            new DatabaseUtil().setVisible(true);
        }
    });
}
//GEN-BEGIN:variables
// Variables declaration - do not modify
private JButton jButton1;
private JButton jButton2;
private JComboBox<String> jComboBox1;
private JComboBox<String> jComboBox2;
private JLabel jLabel1;
private JLabel jLabel2;
//GEN-END:variables
```

画面 14 代码：
```java
private void generator(String templetPath,String outpath,Settings settings,Database db) {
    System.out.println(templetPath);
    System.out.println(outpath);
    System.out.println(settings);
    System.out.println(db);
    GeneratorFacade gf = new GeneratorFacade(templetPath,outpath,settings);
    gf.generator(db);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
