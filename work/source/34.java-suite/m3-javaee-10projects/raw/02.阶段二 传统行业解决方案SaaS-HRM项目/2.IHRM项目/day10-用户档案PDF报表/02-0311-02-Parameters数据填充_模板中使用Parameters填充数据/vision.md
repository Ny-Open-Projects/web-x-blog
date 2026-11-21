# 画面线理解：02-Parameters数据填充：模板中使用Parameters填充数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\02-Parameters数据填充：模板中使用Parameters填充数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:10, 01:38, 02:34, 02:50, 04:29, 04:55, 07:00, 07:48, 08:21, 08:43, 10:12, 11:25, 12:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:38:43

1) 这一组画面整体在讲如何在 JasperReports Studio 中创建并配置带参数的报表模板，包括添加静态文本、定义参数并绑定数据字段。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中关于 JasperReport 填充数据源的说明，重点是“参数Map填充数据”和“1.1.1 模板制作”小节。
画面2：在 JasperReports Studio 中打开项目 TestReports2，显示一个名为 “JasperReport” 的报表文件。
画面3：在 JasperReports Studio 中打开报表文件 testParam.jrxml，进入设计视图，准备创建新模板。
画面4：切换到 SQLyog Ultimate 数据库管理工具，准备连接数据库。
画面5：在 SQLyog 中连接到本地数据库，显示了数据库表结构和数据，其中包含 username、password、mobile、company、dept 等字段。
画面6：打开画图工具，准备绘制一个简单的表格。
画面7：在画图工具中绘制了一个包含“用户名”和“张三”的表格，用于模拟数据展示。
画面8：在 JasperReports Studio 中打开 testParam.jrxml 报表，设计视图中包含“用户名”、“手机号”、“所属企业”、“所属部门”等静态文本框。
画面9：在设计视图中选中“所属企业”静态文本框，查看其属性，位置 x=0px, y=60px，大小 100px x 30px。
画面10：在属性面板中修改参数名称，从 “Parameter1” 改为 “departmentName”。
画面11：在属性面板中设置参数 “dept” 的 Class 为 “java.lang.String”，Description 为 “所属部门”。
画面12：在设计视图中，将字段绑定到报表元素，如 SP(username)、SP(mobile)、SP(company)、SP(dept)。
画面13：预览报表，显示“用户信息”标题和绑定的数据字段。
画面14：在报表参数输入界面，输入参数值：username=张三，mobile=110，company=传智播客，dept=讲师，然后点击“Preview”预览报表。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
public static JasperPrint fillReport(InputStream is, Map<String, Object> parameters, JRdatasource datasource) throws JRException {
```

画面5：
```sql
SELECT * FROM user_info;
```

画面11：
```xml
<parameter name="dept" class="java.lang.String">
    <description>所属部门</description>
</parameter>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 无。
