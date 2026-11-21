# 05-模板打印：代码实现-加载模板抽取公共样式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\05-模板打印：代码实现-加载模板抽取公共样式_【海量资源尽在 ubkz.com】.mp4
- 时长 9分10秒（音频 551s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那好接下来呢我们就可以使用准备好的模板以模板打印的形式完成PUI报表的一个导出好了这回呢我们回到我们的代码部分那把这些代码呢我先给它注释起来注释起来Ctrl CCtrl V 靠一份好了那接下来呢我们这里面就是采用模板打印的形式完成我们PUI报表的一个生成in的形式完成
[00:38] 报表生成好了那接下来呢就是说对于我们来说呢应该有一个叫做模板那这个模板呢其实也应该把它添加到我们当前的这个工程当中把其他受影响的我都关掉了哎抱歉我错了好了那这个模板呢应该也让它加载到我们当前这个工程那放到哪呢注意我就把它放到我们这个resource意思下好了给它创建一个目录比如说呢我就叫做excel-template
[01:08] 好了这个模板呢在今天资料当中给各位也提供了好了这个模板这个模板呢在今天资料当中也给各位提供了就在这边Ctrl C把它copy过来OK那模板已经给各位准备到这边了那接下来我想跟各位来聊的就是我这个代码部分应该如何去写好了底下那些代码又因为一会要用到啊所以我就不先删除了我就在这边呢咱们开始
[01:45] 简单的说一下我们这个操作步骤那对于我们这里面呢首先第一件事想都不要想数据必须得有没错吧那有了数据之后接下来我们这一回就是不是去生成一个什么我们叫做工作部了我们这回要做的事情不是有模板吗我们是不是应该要加载模板文件那加载了模板之后那接下来根据我们叫做模板去创建工作部OK
[02:16] 那这个工作簿我们创建好了之后接下来第四件事要做的事情那要做的就是读取工作表那这几步相当于加点模板模板有了那从里面读读到第一个sheet那第一个sheet读到了之后接着读里面的模板的一些样式没错吧好了这边的工作表读取了之后接着第五件事我们就可以抽取公共样式
[02:48] 好了这些公共样式都抽取出来了之后接着第六件事第六件事其实就开始我们叫做生成我们的数据了构造单元格单元格OK那这些都搞定了之后接着第七件事其实就是我们叫做下载好了那接着我们开始把这个代码呢一个一个的给他搞定那接下来呢就是说
[03:19] 加载模板那这个模板应该如何加载希望各位注意我其实把它放到了我们的resources这个目录下那在我们这边如何去加载我们叫做资源文件那这个资源文件我们可以借助Sprint提供的一种方式那Sprint提供了一个叫做resources这么一个对象这是Sprint提供的那这个resources的对象重点其实就是用于加载我们配置文件的当然了我这个不是配置文件但是它也能加载得到的其实就是一个流数据我们叫做文件流
[03:50] 好了接下来如何做resource等于new一个这个resource其实是Spring提供的一个接口它有很多个实现类都可能去加载配置文件得到流我们现在放到了我们叫做class pass下所以我这边是class passresource中间就可以写我们class pass下的配置文件路径配置文件路径我就这边我就复制一下了怕写错吗-hrdemo
[04:25] 扣过来那这样一来它就开始加载那加载好了之后我们主要目的其实就是为了得到文件流那文件流我们自己去构造其实就可以了Fill input stream fs等于new一个Fill input stream那好了我这个流信息在哪注意全部都可以通过resource打点get fill获取到直接通过文件的形式得到流OK那这样一来我的模板全部加载进来了
[04:53] 并且是一个文件的input stream文件流那好了接下来如何去创建工作部那这回创建工作部怎么去做呢其实我们就可以根据文件流的形式加载过来直接得到一个工作部好了workbook wb等于new一个还是跟之前一样我们用的是2007所以xss workbook好了接下来中间可以把文件流输入进来那这样一来它就根据我们的文件流叫做加载
[05:22] 并且创建出了一个工作部那剩下的事情就是读取工作表那各位我这个表呢咱们只有第一个表格有数据嘛所以我就把这个整个的这个这页读出来那读这页也比较简单咱们之前都学过WB打点我们之前是create是创建现在是要读取所以我们叫做get sheet at好了0这个应该各位都还有印象好那这样一来我们的第一个sheet
[05:51] 也就是第一页我们已经读取出来了我们现在已经读取到了Excel报表里面的第一页这一页读取到了之后接下来我们关注的其实就是公共的这些样式其实到目前为止我整个的Excel报表其实我是已经都有了的因为Workbook里面都有了现在这些内容全部都有我只需要拿到这些公共的样式一个一个的
[06:21] 都存起来那我接下来再往里面每一个格子复制的时候是不是直接用以存取的这个样式往里面填充是不是就可以了所以呢我们这边不得不做的就是我们接下来这件事获取到公共的样式并且把它保存起来那这个如何去做呢其实也很简单我们先去定位到公共的样式在哪一行0 1 2在第二行所以我们先去拿到第二行的内容那如何去做很简单shit打点get sale
[06:51] 我们之前是crate现在是get那get row保全got row得到第二行OK那好了这一行呢是我们的全部的样式的这么一个行那接下来呢我们开始对它进行一个循环便利因为我们之前说过了我们之前说过了我们要想去把所有的这里面的每一个格子的样式是不是都保存起来了那怎么保存我把它抽取到一个我们的数组当中sell still
[07:22] Style4是一竖组等于new一个StyleStyle我们之前也说过StyleStyle其实代表的就是一个样式那现在是一个样式竖组那竖组有多长就代表格子有多少个那竖组有多长所以我这边row打点get last cell numberOK那好了接下来我们开始for循环去抽取到公共的样式把它保存到我们的竖组当中for循环好了int i等于0i小于
[07:55] 爱小于我们叫做row get就是最后一个好了爱加加好了这里面我们要做的事情抽取到每一个单元格的样式首先要得到单元格没错吧好了回到代码我们去得到单元格row点get cell好了把爱爱现在代表的其实就是一个所以因这样一来我们得到了每一个cell每一个格子我们重点其实要的就是格子当中的样式打点get cell cell
[08:25] 得到格子的样式那得到格子样式把它存储到我们的数组当中即可i等于selstel这样写更加好看一下OK那各位你会发现你会发现我这个数组里面的元素0 1 2 3 4 5对应的其实就是编号姓名手机它的样式
[08:52] 没错了那我一会儿要再对它复职的时候复职的时候直接得从数组里面拿到零号编号的样式有了拿到姓名姓名的样式是不是就已经有了OK那这样一来我们公共的样式就已经全部都抽取出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过读取 Excel 模板文件并填充数据，实现员工人事报表的导出功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“1.2 模板打印的操作步骤”和“1.3 代码实现”部分，列出导出操作的 8 个步骤，并展示代码中 @RequestMapping 注解和初步的 Java 代码。
画面 2: 在 IntelliJ IDEA 中展示 EmployeeController.java 文件，代码正在填充单元格，设置单元格值，如“编号”、“姓名”、“手机”等。
画面 3: 展示项目目录结构，选中“excel-template”文件夹，弹出“新建目录”对话框，准备创建新目录。
画面 4: 展示“复制文件”对话框，将“hr-demo.xlsx”复制到“excel-template”目录下。
画面 5: 展示项目目录结构，选中“excel-template”文件夹，文件列表中显示“hr-demo.xlsx”。
画面 6: 展示“重命名”对话框，将文件“hr-demo.xlsx”重命名为“excel-template”。
画面 7: 展示项目目录结构，选中“excel-template”文件夹，文件列表中显示“hr-demo.xlsx”，代码中正在创建 Workbook 对象。
画面 8: 展示代码中创建 Sheet 对象，使用 wb.getSheetAt(0) 获取第一个工作表。
画面 9: 展示 Excel 文件“hr-demo.xlsx”，内容为“2018年2月份人事报表”，包含“编号”、“姓名”、“手机”等列。
画面 10: 展示代码中调用 sheet.getCell() 方法，弹出“Quick Documentation View”显示方法签名。
画面 11: 展示代码中创建 CellStyle 对象，准备设置单元格样式。
画面 12: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 13: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 14: 展示代码中设置单元格样式，使用 CellStyle 对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
}
```

画面 2:
```java
cell = row.createCell(0);
cell.setCellValue(employeeReportResult.getUserId());
cell = row.createCell(1);
cell.setCellValue(employeeReportResult.getUsername());
cell = row.createCell(2);
cell.setCellValue(employeeReportResult.getMobile());
cell = row.createCell(3);
cell.setCellValue(employeeReportResult.getHighestDegreeEducation());
cell = row.createCell(4);
cell.setCellValue(employeeReportResult.getNationalArea());
cell = row.createCell(5);
cell.setCellValue(employeeReportResult.getPassportNo());
cell = row.createCell(6);
cell.setCellValue(employeeReportResult.getNativePlace());
cell = row.createCell(7);
cell.setCellValue(employeeReportResult.getBirthDay());
cell = row.createCell(8);
cell.setCellValue(employeeReportResult.getZodiac());
cell = row.createCell(9);
cell.setCellValue(employeeReportResult.getResignationTime());
```

画面 3:
```java
//1.获取未读数据
List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet();
String [] titles = {"编号","姓名","手机","最高学历","国家地区","护照号","籍贯","生日","属相","入职时间","离职类型","离职原因","离职时间"};
```

画面 4:
```java
Copy file C:\Users\ThinkPad\Desktop\hrm\day\hr demo.xlsx
New name: hr-demo.xlsx
To directory: C:\Users\ThinkPad\workspace\hrm_parent\hrm_employee\src\main\resources\excel-template
```

画面 5:
```java
//参数：年月-月（2018-02）
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    List<EmployeeReportResult> list = userCompanyPersonalService.findByReport(companyId,month);
}
```

画面 6:
```java
Rename file 'hr-demo.xlsx' and its usages to:
hr-demo.xlsx
```

画面 7:
```java
Resource resource = new ClassPathResource("excel-template/hr-demo.xlsx");
FileInputStream fis = new FileInputStream(resource.getFile());
Workbook wb = new XSSFWorkbook(fis);
```

画面 8:
```java
Sheet sheet = wb.getSheetAt(0);
```

画面 9:
```java
//2018年2月份人事报表
编号	姓名	手机	最高学历	国家地区	护照号	籍贯	生日	属相	入职时间	离职类型	离职原因	离职时间
1	张三	13800138000	本科	中国大陆	4	北京	1997/1/1	属相	2018/1/1	主动	无	2018/1/1
```

画面 10:
```java
sheet.getCell()
```

画面 11:
```java
CellStyle styles [] = new CellStyle[];
```

画面 12:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

画面 13:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

画面 14:
```java
for(int i=0;i<row.getLastCellNum();i++) {
    Cell cell = row.getCell(i);
    styles[i] = cell.getCellStyle();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.2 模板打印的操作步骤”和“1.3 代码实现”。
画面 9: Excel 文件标题为“2018年2月份人事报表”，包含“编号”、“姓名”、“手机”等列。
画面 10: 弹出“Quick Documentation View”显示方法签名。
画面 11: 展示代码中创建 CellStyle 对象。
画面 12: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 13: 展示代码中使用 for 循环遍历单元格，设置单元格样式。
画面 14: 展示代码中设置单元格样式，使用 CellStyle 对象。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

