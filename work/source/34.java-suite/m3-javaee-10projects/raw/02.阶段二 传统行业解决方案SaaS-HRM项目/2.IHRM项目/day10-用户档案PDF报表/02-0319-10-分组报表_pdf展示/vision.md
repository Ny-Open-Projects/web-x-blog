# 画面线理解：10-分组报表：pdf展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\10-分组报表：pdf展示_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:13, 00:38, 00:54, 01:01, 01:05, 01:11, 01:42, 02:18, 02:25, 02:30, 02:35, 02:39, 02:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:43:27

1) 这一组画面整体在讲如何在 Java Spring Boot 项目中集成 JasperReports，通过控制器生成并预览分组报表。

2) 按时间顺序列出每张画面的要点：
画面1: 在 JasperSoft Studio 中打开并设计名为 testGroup.jasper 的报表，设计视图中包含分组表头、分组表尾和多个字段（SF[id], SF[username], SF[mobile], SF[company], SF[dept]），右侧属性面板显示 Report Name 为 testGroup，Language 为 java。
画面2: 在 JasperSoft Studio 中，鼠标悬停在报表设计视图中的 SF[company] 字段上，右侧属性面板仍显示 Report: testGroup。
画面3: 在 JasperSoft Studio 中，点击 Preview 按钮后，预览窗口显示“分组报表”，但内容为空（One Empty Record），右侧属性面板显示当前选中的是 Band Group_1 [50px]，其 Group Band Properties 中 Min Height To Start New Page 为 0 px。
画面4: 在 JasperSoft Studio 中，点击 Preview 按钮后，预览窗口显示“分组报表”，内容为空，右侧属性面板显示当前选中的是 Band Group_1 [50px]，其 Group Band Properties 中 Min Height To Start New Page 为 0 px。
画面5: 在 IntelliJ IDEA 中打开名为 jasper-springboot 的 Spring Boot 项目，项目结构显示 src/main/java 下的 controller 包和 src/main/resources/strong/templates 下的 .jasper 文件。
画面6: 在 IntelliJ IDEA 中，鼠标悬停在 src/main/resources/strong/templates 目录下的 testGroup.jasper 文件上。
画面7: 在 IntelliJ IDEA 中，鼠标悬停在 src/main/java/cn/itcast/controller 包下的 JasperController04.java 文件上。
画面8: 在 IntelliJ IDEA 中，显示 JasperController05.java 文件内容，其中包含创建 JasperPrint 对象并导出 PDF 的代码，以及 getuserList() 方法中创建 User 对象的代码，其中 company 为“传智播客”，dept 为“讲师”。
画面9: 在 IntelliJ IDEA 中，显示 JasperController05.java 文件内容，其中 getuserList() 方法中创建 User 对象的代码被修改，company 为“黑马程序员”，dept 为“讲师”。
画面10: 在浏览器中访问 localhost:8181/testJasper4，显示一个分组报表，表头为“javacar数据流块”，包含 10 行数据，每行包含 id、用户名、手机号、公司名、职位。
画面11: 在浏览器地址栏中输入 testJasper5，访问 localhost:8181/testJasper5。
画面12: 在浏览器中访问 localhost:8181/testJasper5，显示一个分组报表，表头为“分组报表”，包含 10 行数据，每行包含 id、用户名、手机号、公司名、职位，其中公司名显示为“传智播客”。
画面13: 在浏览器中访问 localhost:8181/testJasper5，显示一个分组报表，表头为“分组报表”，包含 10 行数据，每行包含 id、用户名、手机号、公司名、职位，其中公司名显示为“黑马程序员”。
画面14: 在浏览器中访问 localhost:8181/testJasper5，显示一个分组报表，表头为“分组报表”，包含 10 行数据，每行包含 id、用户名、手机号、公司名、职位，其中公司名显示为“黑马程序员”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8 代码：
```java
Map parameters = new HashMap<>();
//1.创建javaBean的列表
List<User> userList = getUserList();
//2.当List集合创建javaBean的数据源
JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userList);
JasperPrint print = JasperFillManager.fillReport(fis,parameters,ds);
JasperExportManager.exportReportToPdfStream(print,os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
}

public List<User> getUserList() {
    List<User> list = new ArrayList<>();
    for(int i=0;i<10;i++) {
        User user = new User( id: i+1, username: "用户"+i, company: "传智播客", dept: "讲师", mobile: "13800000000"+i);
        list.add(user);
    }
    return list;
}
```

画面9 代码：
```java
Map parameters = new HashMap<>();
//1.创建javaBean的列表
List<User> userList = getUserList();
//2.当List集合创建javaBean的数据源
JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userList);
JasperPrint print = JasperFillManager.fillReport(fis,parameters,ds);
JasperExportManager.exportReportToPdfStream(print,os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
}

public List<User> getUserList() {
    List<User> list = new ArrayList<>();
    for(int i=0;i<5;i++) {
        User user = new User( id: i+1, username: "itcast"+i, company: "传智播客", dept: "讲师", mobile: "13800000000"+i);
        list.add(user);
    }
    for(int i=5;i<10;i++) {
        User user = new User( id: i+1, username: "itheima"+i, company: "黑马程序员", dept: "讲师", mobile: "13800000000"+i);
        list.add(user);
    }
    return list;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
