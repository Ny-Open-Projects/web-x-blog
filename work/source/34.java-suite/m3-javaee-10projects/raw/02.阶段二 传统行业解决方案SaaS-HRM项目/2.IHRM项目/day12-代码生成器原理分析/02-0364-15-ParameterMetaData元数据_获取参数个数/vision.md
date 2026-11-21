# 画面线理解：15-ParameterMetaData元数据：获取参数个数

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\15-ParameterMetaData元数据：获取参数个数_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:18, 01:24, 01:45, 02:03, 02:30, 02:48, 03:01, 03:13, 03:28, 04:09, 04:26, 04:33, 05:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:50:39

1) 这一组画面整体在讲如何通过 PreparedStatement 获取参数元数据（ParameterMetaData），并演示了如何使用 getParameterCount 方法获取 SQL 语句中占位符参数的个数。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT 的目录结构，当前选中“3.3 参数元数据”。
画面2: PPT 页面显示“3.3 参数元数据”章节内容，介绍 ParameterMetaData 是由 PreparedStatement 通过 getParameterMetaData 方法获取，主要提供占位符参数个数和 SQL 类型等信息。
画面3: 展示 IntelliJ IDEA 中的项目结构，选中了“ParameterMetaDataTest.java”文件，右键菜单显示了“Run Tests in 'cn.itcast.metadata.test'”等选项。
画面4: PPT 页面显示“3.3 参数元数据”章节内容，下方有“黑马程序员”的水印。
画面5: 展示 IntelliJ IDEA 中的项目结构，选中了“ParameterMetaDataTest.java”文件，代码编辑器中显示了该类的开头部分。
画面6: 展示 SQLyog 数据库管理工具界面，显示了“bs_user”表的数据，其中包含 id、username、password 等字段。
画面7: 展示 IntelliJ IDEA 中的“DatabaseMetaDataTest.java”文件，代码中定义了连接数据库的 URL、用户名、密码等配置。
画面8: PPT 页面显示“3.3 参数元数据”章节内容，下方有“黑马程序员”的水印。
画面9: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中定义了 init 方法用于建立数据库连接，并在 test 方法中使用 PreparedStatement。
画面10: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法使用了 PreparedStatement 的 setString 方法设置参数值。
画面11: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法使用了 PreparedStatement 的 setString 方法设置参数值，光标位于 setString 方法的参数位置。
画面12: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法注释了 setString 方法，添加了获取参数元数据的代码。
画面13: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法添加了获取参数元数据的代码，并在控制台输出了参数个数。
画面14: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法添加了获取参数元数据的代码，并在控制台输出了参数个数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7:
```java
import java.util.Properties;

//测试数据库连接
public class DatabaseMetaDataTest {
    private Connection connection,

    @Before
    public void init() throws Exception {
        String driver = "com.mysql.jdbc.Driver";
        String url = "jdbc:mysql://127.0.0.1:3306/thrm?useUnicode=true&characterEncoding=utf8";
        String username = "root";
        String password = "111111";

        Properties props = new Properties();
        props.put("remarksReporting", "true");//获取数据库的备注信息
        props.put("user", username);
        props.put("password", password);

        //1.获取连接
        Class.forName(driver);//注册驱动
        connection = DriverManager.getConnection(url, props);
    }
```

画面9:
```java
//sql = SELECT * FROM bs_user WHERE id = '1063705482939731968'
@Test
public void test() throws Exception {
    String sql = "select * from bs_user where id=?";
    PreparedStatement pstmt = connection.prepareStatement(sql);
    pstmt.setString(1, "1063705482939731968");
}
```

画面10:
```java
//sql = SELECT * FROM bs_user WHERE id = '1063705482939731968'
@Test
public void test() throws Exception {
    String sql = "select * from bs_user where id=?";
    PreparedStatement pstmt = connection.prepareStatement(sql);
    pstmt.setString(parameterIndex: 1, "1063705482939731968");
}
```

画面12:
```java
//获取参数元数据
ParameterMetaData metaData = pstmt.getParameterMetaData();
int count = metaData.getParameterCount();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

画面4: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

画面8: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

5) 不要评价画面美观，不要输出与课程无关的内容。
