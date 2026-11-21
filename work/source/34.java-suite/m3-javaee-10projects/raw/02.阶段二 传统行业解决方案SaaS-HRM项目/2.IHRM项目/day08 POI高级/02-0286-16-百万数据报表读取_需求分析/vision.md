# 画面线理解：16-百万数据报表读取：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\16-百万数据报表读取：需求分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:36, 00:58, 01:06, 01:27, 01:39, 01:45, 02:12, 02:21, 02:28, 02:41, 02:48, 02:55, 03:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:15:22

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Apache POI 库在 Java 中高效读取百万级数据的 Excel 文件，对比用户模式与事件模式的性能差异。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前选中“5 百万数据报表读取”。
画面2：展示 HRM 系统的员工导入页面，用于背景说明。
画面3：展示 PPT 内容，标题为“5 百万数据报表读取”，子标题“5.1 需求分析”和“5.2 解决方案”，其中“5.2.1 思路分析”部分说明了用户模式和事件模式的区别。
画面4：展示文件资源管理器，目录为“ihrm”，包含“day1”至“day8”文件夹和“企业128员工-saas-hrm大表.xlsx”文件。
画面5：展示 Excel 文件“demo.xlsx”，内容为大量医疗数据，列标题包括“id”、“sample”、“cell”、“Staining”、“Supportive”。
画面6：在 Excel 中选中数据后，弹出错误提示框：“Microsoft Excel 无法插入新数据单元格，因为这些数据单元格的行或列超出了工作表的范围。”
画面7：展示 Excel 文件“demo.xlsx”的另一部分数据，内容为脑部组织样本数据。
画面8：在 Excel 中选中数据后，弹出“poi test”和“ihrm_parent”两个 IntelliJ IDEA 项目窗口。
画面9：在 IntelliJ IDEA 中打开“PoITest05.java”文件，代码中使用了“Workbook wb = new XSSFWorkbook(path);”和“Sheet sheet = wb.getSheetAt(0);”等语句。
画面10：展示桌面，有“ihrm”文件夹图标，以及“黑马程序员”和“博学谷”的标志。
画面11：在 IntelliJ IDEA 中，代码中“path”变量的值被修改为“C:\Users\ThinkPad\Desktop\ihrm\day8\资源\百万数据报表\demo.xlsx”。
画面12：在 IntelliJ IDEA 中，代码中“path”变量的值被修改为“C:\Users\ThinkPad\Desktop\ihrm\day8\资源\百万数据报表\demo.xlsx”，并添加了注释“//根据索引获取每一个单元格”。
画面13：在 IntelliJ IDEA 中，代码中“Object value = cell.setCellValue();”被修改为“Object value = cell.getValue();”。
画面14：在 VisualVM 中，监控“cn.itcast.poi.test.PoITest05”程序的运行情况，显示 CPU 使用率、堆内存使用情况和已处理数据量等指标。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9：
```java
public class PoITest05 {
    public static void main(String[] args) throws Exception {
        //1.根据Excel文件创建工作簿
        Workbook wb = new XSSFWorkbook(path); //参数，索引
        //2.获取Sheet中的一行，不是一个单元格
        Sheet sheet = wb.getSheetAt(0); //参数，索引
        //3.获取Sheet中的一行，不是一个单元格
        for (int rowNum = 0; rowNum <= sheet.getLastRowNum(); rowNum++) {
            Row row = sheet.getRow(rowNum); //根据索引获取每一个行
            StringBuilder sb = new StringBuilder();
            for(int cellNum=2; cellNum <= row.getLastCellNum(); cellNum++) {
                //根据索引获取每一个单元格
                Object value = cell.setCellValue();
            }
        }
    }
}
```
画面11：
```java
Workbook wb = new XSSFWorkbook(path: "C:\Users\ThinkPad\Desktop\ihrm\day8\资源\百万数据报表\demo.xlsx");
```
画面12：
```java
Workbook wb = new XSSFWorkbook(path: "C:\Users\ThinkPad\Desktop\ihrm\day8\资源\百万数据报表\demo.xlsx");
//根据索引获取每一个单元格
Object value = cell.getValue();
```
画面13：
```java
Object value = cell.getValue();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：5 百万数据报表读取
子标题：5.1 需求分析
子标题：5.2 解决方案
子标题：5.2.1 思路分析
内容：
- 用户模式：加载并读取Excel时，是通过一次性将所有数据加载到内存中再去解析每个单元格内容。当Excel数据量较大时，由于不同的运行环境可能会造成内存不足甚至OOM异常。
- 事件模式：它逐行扫描文档，一边扫描一边解析。由于应用程序只是在读取数据时检查数据，因此不需要将数据存储在内存中，这对大型文档的解析是个巨大优势。
子标题：5.2.2 步骤分析
内容：
(1) 设置POI的事件模式
- 根据Excel获取文件流
- 根据文件流创建OPCPackage

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
