# 06-模板打印：代码实现和总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\06-模板打印：代码实现和总结_【海量资源尽在 ubkz.com】.mp4
- 时长 4分57秒（音频 297s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们现在抽取到了公共的样式那接下来呢是不是就可以去构造我们的数据的单元格那构造数据的单元格我们找到我们这边的代码找到我们这边的Excel那我们构造数据单元格那先声明我们这个数据应该是从第几行开始构造那有的朋友说第四行那不行啊
[00:25] 第三行是我们的一条模板的一条数据这个不是我们的真实数据我们主要用这条数据里面的样式没错吧所以对于我们而言第一行没什么用所以我们添加新的数据报表的时候要从第三行开始走起这个应该也能理解那所以呢在这边我先去定义我们的一个构造数据单元行它的所以int由number因为比如说就等于2
[00:58] 好了那接下来的事情呢其实就是拿到每一行开始去创建每一个单元行接着往里面去填充所有的数据是不是就可以了那这一步呢和我们之前的代码呢很相似和我们之前的代码很相似那我直接Ctrl C Copy过来Ctrl V我们之前这个代码叫Row Index那我也叫Row Index我们刚才说过了要从R开始
[01:27] 那这样一来它就开始是不是创建从第二每一行创建创建创建创建创建创建一直创建那并且是不是往每一个格子也都创建出来复制上我们想要的数据那只不过当前这个报表构造出来之后每一个格子当中还没有样式那么的样式全部都抽取到这个数组当中了所以在这边我们可以对每一个单元格打点set
[01:57] C1死掉了那这个样式在哪刚才我们说过了编号的样式不就是这个数组的零号元素吗所以零号元素拿过来那接下来里面剩下要做的事情都是类似的1号2号3号那国家和地区4号这都是重复工啊5号好了这边呢就是6号同样的7号
[02:35] 8号因为我们把所有的样式都抽取到这个数组里面了这边直接从以数组下标的形式从里面获取就可以了并且我们这个数组下标和我们这个存的这个属性是一一对应的所以这个就比较简单了OK12那这样一来我整个的这些样式就已经全部给单元格复制上了那复制当了之后剩下最后一件事那就是下载那下载的逻辑和我们之前下载的逻辑一模一样逐情删减
[03:05] 就可以了OK那这样一来我使用模板下载的形式这个代码呢咱们就已经都写好了那写好了之后我可以重新启动一下我这个员工微服务好了让它去重启这边员工微服务呢让它去重启我呢打开我的浏览器刷新一下浏览器我们来看一下能不能够把数据真正的给它导出出来这边还在重启啊刷新走导出
[03:37] 好了各位来看能够导出过来好了并且叫做02那接着我们找到2这个报表打开各位来看这一回我们的数据就已经全部都给我打印出来了并且是不是都有这个样式那其实对于这个整个模板打印来说代码很简单重点其实就是想让各位知道我们模板打印的这个思想那因为我们很多Excel报表生成的时候都有
[04:09] 各种各样的样式的一个要求那比如说我这边就有自己的要求我的数据都是这样那如果说这些代码我们放到Java代码去一个一个给它告造一个一个给它去写那太麻烦了我们就可以生成这么一份带数据的样式报表以它为模板那我们接下来要做的事情是把这个报表这个模板模板里面的样式给它提取出来那接着再复制是不是就可以啊所以这个代码虽然简单但是这个思想希望各位要知道
[04:37] 当然了对于模板打印而言这个操作步骤也是希望各位要了解的首先制作模板接着我们根据模板文件得到工作簿好了读取工作行读取读取读取抽取到公共的样式剩下跟我们之前写一个Excel报表其实是一模一样的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Apache POI 库，通过读取 Excel 模板并填充数据，实现动态生成人事报表的功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个名为“2018年2月份人事报表”的 Excel 文件，其中包含员工编号、姓名、手机、最高学历、国家地区、护照号、籍贯、生日、属相、入职时间、离职类型、离职原因、离职时间等字段，第一行数据已填充。
画面2：在 Excel 文件基础上，切换到 IntelliJ IDEA 开发环境，显示了项目结构和两个终端窗口，其中一个终端显示了项目路径。
画面3：在 IntelliJ IDEA 中，展示 EmployeeController.java 文件的代码，其中定义了 Workbook 和 Sheet 对象，并通过循环设置单元格值。
画面4：继续展示代码，设置单元格样式和值，包括员工编号、姓名、手机、最高学历、国家地区、护照号等字段。
画面5：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面6：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面7：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面8：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面9：继续展示代码，设置单元格样式和值，包括籍贯、生日、属相等字段。
画面10：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面11：继续展示代码，设置单元格样式和值，包括入职时间、离职类型、离职原因、离职时间等字段。
画面12：切换到桌面，显示了“黑马程序员”和“博学谷”的标志。
画面13：展示了一个 PPT 页面，标题为“1 模板打印”，子标题为“1.1 概述”、“1.2 模板打印的操作步骤”和“1.3 代码实现”，其中“1.3 代码实现”部分展示了 @RequestMapping 注解和 public void export 方法的代码。
画面14：继续展示 PPT 页面，内容与画面13相同，但滚动到了“1.3 代码实现”的下一部分，展示了 List<EmployeeReportResult> list = userCompanyPersonalService.findBByReport(companyId, month) 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet();
String [] titles = "编号,姓名,手机,最高学历,国家地区,护照号,籍贯,生日,属相,入职时间,离职类型,离职原因,离职时间".split(",");
Row row = sheet.createRow(0);
int titleIndex=0;
for (String title : titles) {
    cell = row.createCell(titleIndex++);
    cell.setCellValue(title);
}
int rowIndex = 1;
Cell cell=null;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    //编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    //姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    //手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    //最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    //国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    //护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
}
```

画面4：
```java
//设置单元格样式
CellStyle styles[] = new CellStyle[row.getLastCellNum()];
for(int i=0;i<row.getLastCellNum();i++){
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
//设置单元格
int rowIndex = 2;
Cell cell=null;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    //编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    cell.setCellStyle(styles[0]);
    //姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    cell.setCellStyle(styles[1]);
    //手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    cell.setCellStyle(styles[2]);
    //最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    cell.setCellStyle(styles[3]);
    //国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    cell.setCellStyle(styles[4]);
    //护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
    cell.setCellStyle(styles[5]);
    //籍贯
    cell = row.createCell(6);
    cell.setCellValue(employeeReportResult.getNativePlace());
    cell.setCellStyle(styles[6]);
    //生日
    cell = row.createCell(7);
    cell.setCellValue(employeeReportResult.getZodiac());
    cell.setCellStyle(styles[7]);
    //属相
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.getBirthDay());
    cell.setCellStyle(styles[8]);
    //入职时间
    cell = row.createCell(9);
    cell.setCellValue(employeeReportResult.getTimeOfEntry());
    cell.setCellStyle(styles[9]);
    //离职类型
    cell = row.createCell(10);
    cell.setCellValue(employeeReportResult.getTypeOfTurnover());
    cell.setCellStyle(styles[10]);
    //离职原因
    cell = row.createCell(11);
    cell.setCellValue(employeeReportResult.getReasonsForLeaving());
    cell.setCellStyle(styles[11]);
    //离职时间
    cell = row.createCell(12);
    cell.setCellValue(employeeReportResult.getResignationTime());
    cell.setCellStyle(styles[12]);
}
```

画面10：
```java
//3.下载
ByteArrayOutputStream os = new ByteArrayOutputStream();
wb.write(os);
new DownloadUtils().download(os, response, returnName + "人事报表.xlsx");
```

画面11：
```java
/**
 * 采用模板打印的形式完成报表生成
 * @param month
 * @return
 */
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    //1.加载模板
    Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.读取模板
    Workbook wb = new XSSFWorkbook(fis);
    //3.读取工作表
    Sheet sheet = wb.getSheetAt(0);
    //4.读取行
    Row row = sheet.getRow(2);
    CellStyle styles[] = new CellStyle[row.getLastCellNum()];
    for(int i=0;i<row.getLastCellNum();i++){
        Cell cell = row.getCell(i);
        styles[i] = cell.getCellStyle();
    }
    //5.设置单元格
    int rowIndex = 2;
    Cell cell=null;
    for (EmployeeReportResult employeeReportResult : list) {
        row = sheet.createRow(rowIndex++);
        //编号
        cell = row.createCell(0);
        cell.setCellValue(employeeReportResult.getUserId());
        cell.setCellStyle(styles[0]);
        //姓名
        cell = row.createCell(1);
        cell.setCellValue(employeeReportResult.getUsername());
        cell.setCellStyle(styles[1]);
        //手机
        cell = row.createCell(2);
        cell.setCellValue(employeeReportResult.getMobile());
        cell.setCellStyle(styles[2]);
        //最高学历
        cell = row.createCell(3);
        cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
        cell.setCellStyle(styles[3]);
        //国家地区
        cell = row.createCell(4);
        cell.setCellValue(employeeReportResult.getNationalArea());
        cell.setCellStyle(styles[4]);
        //护照号
        cell = row.createCell(5);
        cell.setCellValue(employeeReportResult.getPassportNo());
        cell.setCellStyle(styles[5]);
        //籍贯
        cell = row.createCell(6);
        cell.setCellValue(employeeReportResult.getNativePlace());
        cell.setCellStyle(styles[6]);
        //生日
        cell = row.createCell(7);
        cell.setCellValue(employeeReportResult.getZodiac());
        cell.setCellStyle(styles[7]);
        //属相
        cell = row.createCell(8);
        cell.setCellValue(employeeReportResult.getBirthDay());
        cell.setCellStyle(styles[8]);
        //入职时间
        cell = row.createCell(9);
        cell.setCellValue(employeeReportResult.getTimeOfEntry());
        cell.setCellStyle(styles[9]);
        //离职类型
        cell = row.createCell(10);
        cell.setCellValue(employeeReportResult.getTypeOfTurnover());
        cell.setCellStyle(styles[10]);
        //离职原因
        cell = row.createCell(11);
        cell.setCellValue(employeeReportResult.getReasonsForLeaving());
        cell.setCellStyle(styles[11]);
        //离职时间
        cell = row.createCell(12);
        cell.setCellValue(employeeReportResult.getResignationTime());
        cell.setCellStyle(styles[12]);
    }
}

