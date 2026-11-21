# 画面线理解：18-百万数据报表读取：步骤分析以及自定义时间处理器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\18-百万数据报表读取：步骤分析以及自定义时间处理器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:24, 02:02, 02:48, 03:41, 05:42, 06:39, 08:15, 09:21, 11:18, 11:58, 13:19, 13:47, 14:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:16:26

1) 这一组画面整体在讲如何使用 Apache POI 的事件驱动模式解析 Excel 文件，并通过自定义处理器类处理单元格数据。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，内容为“5.2.1 思路分析”和“5.2.2 步骤分析”，其中步骤分析包含“（1）设置POI的事件模式”、“根据Excel获取文件流”、“根据文件流创建OPC Package”、“创建XSSFReader对象”、“（2）Sax解析”、“自定义Sheet处理器”。
画面2：IntelliJ IDEA项目视图，显示项目名为“poi-demo”，包含src、test、target、pom.xml等目录。
画面3：IntelliJ IDEA项目视图，选中了“cn.itcast.poi”包。
画面4：IntelliJ IDEA中打开“SheetHandler.java”文件，内容为空。
画面5：Excel文件“demo.xlsx”打开，显示数据表，包含“id”、“breast”、“adipocytes”、“Negative”、“Staining”、“Supportive”等列。
画面6：IntelliJ IDEA中“SheetHandler.java”文件，显示实现了XSSFSheetXMLHandler.SheetContentsHandler接口，包含startRow、endRow、cell三个方法。
画面7：Excel文件“demo.xlsx”打开，选中了“id”列的第2行数据。
画面8：Excel文件“demo.xlsx”打开，选中了“id”列的第3行数据。
画面9：Excel文件“demo.xlsx”打开，选中了“id”列的第1行数据。
画面10：IntelliJ IDEA中“SheetHandler.java”文件，对endRow方法添加了System.out.println(entity)语句。
画面11：IntelliJ IDEA中“SheetHandler.java”文件，对cell方法添加了switch语句，根据列号处理不同字段。
画面12：IntelliJ IDEA中“SheetHandler.java”文件，为switch语句添加了set方法调用，如setAdipocytes、setBreast等。
画面13：IntelliJ IDEA中“SheetHandler.java”文件，完成对cell方法的switch语句编写，调用entity.setAdipocytes(value)。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面4：
package cn.itcast.poi.entity.cn.itcast.poi.handler;
public class SheetHandler {

}

画面6：
public class SheetHandler implements XSSFSheetXMLHandler.SheetContentsHandler {
    /**
     * 当开始解析某一行的时候触发
     */
    @Override
    public void startRow(int i) {

    }
    /**
     * 当结束解析某一行的时候触发
     */
    @Override
    public void endRow(int i) {

    }
    /**
     * 对行中的每一个去格进行处理
     */
    @Override
    public void cell(String cellReference, String value, XSSFComment xssfComment) {

    }
}

画面10：
@Override
public void endRow(int i) {
    System.out.println(entity);
}

画面11：
@Override
public void cell(String cellReference, String value, XSSFComment xssfComment) {
    if(entity != null) {
        String pxs = cellReference.substring(beginIndex, endIndex);
        switch (pxs) {
            case "A":
                break;
            case "B":
                break;
            case "C":
                break;
            case "D":
                break;
            case "E":
                break;
            case "F":
                break;
            default:
                break;
        }
    }
}

画面12：
@Override
public void cell(String cellReference, String value, XSSFComment xssfComment) {
    if(entity != null) {
        String pxs = cellReference.substring(beginIndex, endIndex);
        switch (pxs) {
            case "A":
                entity.setId(value);
                break;
            case "B":
                entity.setBreast(value);
                break;
            case "C":
                entity.setAdipocytes(value);
                break;
            case "D":
                break;
            case "E":
                break;
            case "F":
                break;
            default:
                break;
        }
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题为“5.2.1 思路分析”和“5.2.2 步骤分析”，步骤分析包含“（1）设置POI的事件模式”、“根据Excel获取文件流”、“根据文件流创建OPC Package”、“创建XSSFReader对象”、“（2）Sax解析”、“自定义Sheet处理器”。

5) 不要评价画面美观，不要输出与课程无关的内容。
