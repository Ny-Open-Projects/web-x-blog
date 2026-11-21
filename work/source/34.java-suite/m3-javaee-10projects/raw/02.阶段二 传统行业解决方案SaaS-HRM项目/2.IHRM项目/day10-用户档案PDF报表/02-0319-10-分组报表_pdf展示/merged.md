# 10-分组报表：pdf展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\10-分组报表：pdf展示_【海量资源尽在 ubkz.com】.mp4
- 时长 3分3秒（音频 184s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 当前的这个数据接口呢我们已经构造的差不多了当然咱们可以preview预览一下它这个效果那接下来就是说呢为了方便我们进行打印是不是还要对这里面的涉及到的一个中文进行一个处理所以这边拿过来对中文进行一个统一的编码的设置好了我们叫做华文送体好了给它来一个12号字那为了方便观察呢这几个我需要以边框的形式给它体现出来
[00:30] 所以回到这边的border跟之前套路都是一模一样的OK再来看一下也没什么问题接下来就是说这里面的字母这里面的文字还是做一个居中处理好了接下来我们可以编译一下当前的模板编译编译成功之后拿到.jasper文件Ctrl C给它拖到我们的Java代码里Ctrl V拖拽过来
[01:05] 同样一样的逻辑Ctrl C Ctrl Vcopy一个Controller方便我们测试现在我们测试的是分组报表分组报表test Jasper 5OK这边group这儿oup接着我想说我们传递的数据还是基于对象list集合的bin data source
[01:38] 那接下来就是说我们现在关注的其实如何构造这个列表了内部是自动的对列表根据企业名称进行分类那现在你会发现我构造的数据呢只是全部都在传职博客这个公司下所以我再去构造一份这边呢来五个现在呢就不在这个公司下了我让他
[01:59] 划分到黑马程序员这个公司下那为了我方便观察这边这个用户名称呢我也给他做一个简单的修改比如说呢传职博客的用户名都是ITcast某某那黑马成员IT黑马某某某为了方便观察吧OK那这样一来我这个数据也构造好了那接下来我们要做的事情重新启动一下当前这个微服务刷新浏览器看一下效果回到浏览器这回请求的是
[02:29] 五走各位发现现在这个数据呢已经出来了现在就做到了以企业名称进行分组那上面传说博客的全部都是ITcast等等等等一共有十个那继续往下看就是黑马成员都是IT黑马等等等等一共有五条数据没错吧OK那这样一来呢其实我们的数据已经构造好了
[02:56] 那构造好了之后呢其实还有很多的细节问题我们需要一起来看一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Java Spring Boot 项目中集成 JasperReports，通过控制器生成并预览分组报表。

2) 按时间顺序列出每张画面的要点：
画面1: 在 JasperSoft Studio 中打开并设计名为 testGroup.jasper 的报表，设计视图中包含分组表头、分组表尾和多个字段（SF[id], SF[username], SF[mobile], SF[company], SF[dept]），右侧属性面板显示 Report Name 为 testGroup，Language 为 java。
画面2: 在 JasperSoft Studio 中，鼠标悬停在报表设计视图中的 SF[company] 字段上，右侧属性面板仍显示 Report: testGroup。
画面3: 在 JasperSoft Studio 中，点击 Preview 按钮后，预览窗口显示“分组报表”，但内容为空（One Empty Record），右侧属性面板显示当前选中的是 Band Group_1 [50px]，其 Group Band Properties 中 Min Height To Start New Page 为 0 px。
画面4: 在 JasperSoft Studio 中，点击 Preview 按钮后，预览窗口显示“分组报表”，内容为空，右侧属性面板显示当前选中的是 Band Group_1 [50px]，其 Group Band Properties 中 Min Height To Start New Page 为 0 px。
画面5: 在 IntelliJ IDEA 中打开名为 jasper-Spring Boot 的 Spring Boot 项目，项目结构显示 src/main/java 下的 Controller 包和 src/main/resources/strong/templates 下的 .jasper 文件。
画面6: 在 IntelliJ IDEA 中，鼠标悬停在 src/main/resources/strong/templates 目录下的 testGroup.jasper 文件上。
画面7: 在 IntelliJ IDEA 中，鼠标悬停在 src/main/java/cn/itcast/Controller 包下的 JasperController04.java 文件上。
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

