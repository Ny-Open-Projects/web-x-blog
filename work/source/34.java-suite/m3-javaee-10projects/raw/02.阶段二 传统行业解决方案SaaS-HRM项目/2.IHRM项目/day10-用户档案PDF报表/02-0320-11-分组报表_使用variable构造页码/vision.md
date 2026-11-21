# 画面线理解：11-分组报表：使用variable构造页码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\11-分组报表：使用variable构造页码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:27, 00:56, 02:45, 03:29, 04:40, 05:11, 05:45, 07:01, 07:36, 08:37, 09:03, 09:13, 09:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:43:53

1) 这一组画面整体在讲如何在 JasperReports 中通过分组功能实现报表的分组展示，并结合后端 Java 代码生成分组报表。

2) 按时间顺序列出每张画面的要点：
画面1：展示最终生成的分组报表，包含“传智播客”和“黑马程序员”两个分组，每个分组下显示对应员工数据。
画面2：在 JasperReports 设计界面中，创建了两个数据区域，分别用于显示“传智播客”和“黑马程序员”分组的数据。
画面3：空白画布，无内容。
画面4：JasperReports 设计界面，提示按“companyName”字段进行分组，设置“Group Header”和“Group Footer”。
画面5：与画面2相同，设计界面中两个数据区域。
画面6：JasperReports 设计界面，定义了一个名为“totalNum”的变量，用于统计分组数量。
画面7：与画面2相同，设计界面中两个数据区域。
画面8：在设计界面中，选中“传智播客”分组的区域，准备进行编辑。
画面9：预览窗口显示“User Operation is Waiting”，提示后台工作完成。
画面10：JasperReports 设计界面，显示“Group1 Group Header 1”和“Group1 Group Footer 1”。
画面11：JasperReports 设计界面，显示空白报表。
画面12：IDE 中的 Java 代码，定义了 `JasperController05` 类中的 `getUsersList` 方法，用于生成报表数据。
画面13：展示最终生成的分组报表，包含“传智播客”和“黑马程序员”两个分组，每个分组下显示对应员工数据。
画面14：JasperReports 设计界面，显示“Group1 Group Header 1”和“Group1 Group Footer 1”，以及“Page Footer”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面6：
```java
Name: totalNum
Value Class Name: java.lang.Integer
Calculation: Count
Expression: $F{company}
Increment type: None
Incrementer Factory Class Name: 
Reset type: Report
```

画面12：
```java
Map parameters = new HashMap<>();
//JRE System Library
List<User> userList = getUserList();
//JRE System Library
JRECollectionDataSource userDataSource = new JRECollectionDataSource(userList);
JasperPrint print = JasperFillManager.fillReport(jfs, parameters, ds);
JasperExportManager.exportReportToPdfStream(print, os);
catch (JRException e) {
    e.printStackTrace();
}
finally {
    os.flush();
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面4：
- 标题：按字段“companyName”进行分组。
- 内容：设置完毕，点击“Next”，系统显示细节设置页面。此处可以设置是否加入“group header”和“group footer”区。建议保持默认选中，加入这两个区域，这样可以控制每组报表的结尾，打印相应的信息，例如统计信息等。

画面10：
- 标题：Group1 Group Header 1
- 内容：*已企业名分组，企业名称=+ SF[company]*
- 标题：Group1 Group Footer 1
- 内容：共计：+SV[totalNum]+条数

画面14：
- 标题：Group1 Group Header 1
- 内容：*已企业名分组，企业名称=+ SF[company]*
- 标题：Group1 Group Footer 1
- 内容：共计：+SV[totalNum]+条数
- 标题：Page Footer
- 内容：SV[PAGE_NUMBER]
