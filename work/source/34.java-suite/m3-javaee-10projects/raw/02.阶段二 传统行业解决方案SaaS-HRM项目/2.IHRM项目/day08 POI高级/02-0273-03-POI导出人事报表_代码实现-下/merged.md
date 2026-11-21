# 03-POI导出人事报表：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\03-POI导出人事报表：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 时长 9分26秒（音频 566s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那标题部分呢我们处理过了之后接下来关注的就是里面的这些内容那对于这个内容处理来说呢咱们就可以去循环粒子集合因为粒子里面的一个对象其实代表的就是这么一行没错吧所以呢接下来呢我们就开始去进行一个循环的一个操作了OK好了那这边呢我们操作起来呢也比较简单ITR for 循环那么现在循环呢就是一个粒子集合
[00:30] 好了在上面呢由于我这个行呢是一行一行不断的往下叠加的每一行呢其实我也可以给它设置这么一个行的一个编号好了int比如说呢我就叫做rowindex注意我们这个行呢是从正文内容是不是就是12从第二行开始那对于我们的索引来说就是01所以我这边它从1号来进行开始那好了接下来呢里面我们要做的事情首先呢对于我们来说
[01:00] 一个对象代表一行那么这一行是不是应该也创建出来才对啊那么创建的这个行呢就是用肉来表示即可好了那我们创建的行肉index加加那好了接着在这个行创建好了之后那接下来里面就是对于这个行每一行的每一个格子来进行处理其实就可以了剩下的事情我们就开始处理这些内容好了比如说呢我要处理
[01:31] 编号要处理姓名的还要处理手机的学历地区护照籍贯生日属相入职时间离职类型离职原因和离职时间等等这些内容接着对于这么一个属性的其实对应的就是一个单元格所以我这边需要去创建单元格来做sellsale等于老我这边
[02:06] 肉打点create sale我们的第0个格子是不是就应该是用户编号那么的用户编号也把值复值进去其实就可以了sale打点set sale value那么的值在哪呢就是我们的对象里面的打点get比如说呢我就打点getuser idok那这样一来第一个格子我们创建好了接着搞第二个
[02:36] 好了这个sale呢我把它抽取到最上面吧OK方便一些好了那第二格子有了接着第三个剩下的事情就是基本上就是大同小异好了我这边稍微快一点我就直接复制过来这些内容了OK好了接着开始做一个简单的修改那对于姓名来说呢我们应该是第一个格子好了这边打点getuser name好了对于手机呢这边是第二个格子打点get我们叫做mobile
[03:20] 好了第三个最高的一个学历打点get这个比较长啊the high degree of education好了接着第四个格子国家和地区好了打点get国家和地区nation L好了接着第五个打点get护照的编号passport number好了接着就是籍贯同样的再来打点
[03:58] 那对于机关来说呢我们叫做native place好了这边是第六好了第七生日get birthday好了继续往下呢就是属相第九十我先把这个改掉了十一十二好了把这个值也填充上属相大点get属相ok好了入职时间time of entry好了接着离职类型
[04:45] 当然这个离职类型如果有就有如果没有呢其实就是一个空嘛typecrover没错离职原因reasonok好了离职时间打点get这个其实就是一个体力活快点把它补充上就可以了ok那这样一来我们的单元格所有内容都已经设置好了单元格呢我们现在已经构造出来了接下来就是完成一个下撒
[05:19] 那对于下载来说呢相对来说比较简单在今天的资料当中呢给各位准备好了这么一个工具列这个工具列呢主要就是用来下载的可以把它直接引入到我们的工程当中直接去使用其实就可以了那我在这边的工具类其实也给我导入进来了那这个工具列呢叫做download utils那我们可以简单的来看一下这里面呢其实就是获取流信息接着
[05:46] 将 response 设置为我们的一个来流往出输出那这边呢就是 output.stream往里刷新起来就可以了好了那这些呢我们工具比较简单我们直接就可以借助 download utils进行一个下载了好了那我们如何去做呢很简单new一个 download utils打点调用里面的方法download那么 download 里面各位来看三个参数第一个呢是一个我们的bat array output stream
[06:14] 还有第二个就是response第三个是我们的文件名称那对于这些比较简单首先呢第一个就是数组的这么一个输出流那这个输出流里面包含了所有的文档的一些信息我们的excel文档的一些留了一些信息那response和我们的名称给它其实就可以了那所以在上边我需要什么我去构建一下就可以好了这边OS等于new一个byte array output stream好了那这里面的我们的所有的流信息如何设置进去很简单
[06:44] 咱们就可以WB打点叫做write直接写入到我们的OS对象当中那这样一来OS对象有值了第一个参数满足第二个参数response我们的base Controller里面也有好了第三个参数就是我们当前的这个名称那这个名称呢如何去做呢其实也比较简单我们可以给它来一个就是month加上不是叫做人事报表吗点各位千万别忘了我们这边用的是lsx
[07:19] OK那这样一来我整个的这个代码就已经全部都写好了那我重新启动一下我这边的会员微服务重新启动好了打开我们的浏览器咱们耐心等待一下去完成这个导出的这个测试好了呢这个导出测试呢如何去做呢其实很简单这边员工好了这边就是月份报表一个导出那导出的时候注意上面呢其实是当前的这个月份当前的这个月份这个呢我们可以通过Data计算出来
[07:49] 那我们为了测试的更加好看一点呢这边我用03来测试我再去输入可以刷新一下刷新一下因为这个当前三月份会有很多的数据咱们更加好看的数据嘛好了我这边03代表的是2018的三月份我们的代码部分前端会给我拼接成2018-03这种形式好了接下来呢我点击导出我点击导出那各位我点击导出各位一起来看一下效果走
[08:21] 这边报诉了一个系统繁忙是吧好了那接着我们一起来看一下我们的代码部分找到代码部分呢我们往下去看确定是查了这边报了一个空指针的一个错误啊那是在241行我们一起来看这边sale抱歉肉点get sale我们应该是这个是不是得到每一行然后呢去创建每一个格子啊那我们这边应该叫做create saleok create sale没问题
[08:48] 好了那接下来呢再去重新启动一下各位耐心等待一下这个就是我们写代码写的稍微有点匆忙所以它就会有一点点问题嘛好了这边呢让它去启动我们再去导出一下看一下效果来走OK各位来看现在呢报表已经开始让我去下载了我点击保存好了保存好了之后我们一起打开这个报表来看一下那各位来看现在数据是不是都已经给我打印出来了
[09:21] OK那这样一来我们的PY报表导出其实也已经成功了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在Java项目中编写导出员工信息到Excel表格的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个名为“2018-03人员信息.xlsx”的Excel文件，其中包含“编号”、“姓名”、“手机”、“最高学历”、“国家地区”、“护照号”、“籍贯”、“生日”、“入职时间”等列，第一行数据为“test1”、“13000000001”、“初中”、“中国大陆”、“abc”、“北京”、“2018-03-01”。
画面2：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中包含一个for循环遍历employeeReportResult列表，并调用split方法按逗号分割字符串，用于处理离职类型、离职原因、离职时间。
画面3：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中包含一个for循环遍历employeeReportResult列表，用于创建Excel表格的行和单元格。
画面4：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面5：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面6：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面7：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面8：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面9：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面10：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面11：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面12：在浏览器中，展示HRM系统的“03月人员报表”页面，包含“姓名”、“性别”、“手机”、“在职状态”、“出生日期”、“最高学历”、“籍贯地区”、“身份证号”等筛选条件，以及“导出”按钮。
画面13：在IntelliJ IDEA中，展示EmployeeController.java文件的代码，其中在cell.setCellValue(employeeReportResult.get...);语句中，IDE提示getUserId()方法，但提示“Cannot resolve method 'setCellVlaue'”。
画面14：展示“2018-03人员信息.xlsx”文件，其中包含“编号”、“姓名”、“手机”、“最高学历”、“国家地区”、“护照号”、“籍贯”、“生日”、“入职时间”等列，数据已填充，例如“test1”、“13000000001”、“初中”、“中国大陆”、“abc”、“北京”、“2018-03-01”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2：
```java
String[] titles = "离职类型,离职原因,离职时间".split( regex: ",");
```
画面3：
```java
int titleIndex=0;
for (String title : titles) {
    cell = row.getCell(titleIndex++);
    cell.setCellValue(title);
}
int rowIndex = 1;
for (EmployeeReportResult employeeReportResult : list) {
    row = sheet.createRow(rowIndex++);
    Cell cell = null;
    // 编号
    cell = row.createCell(0);
    cell.setCellValue(employeeReportResult.getUserId());
    // 姓名
    cell = row.createCell(1);
    cell.setCellValue(employeeReportResult.getUsername());
    // 手机
    cell = row.createCell(2);
    cell.setCellValue(employeeReportResult.getMobile());
    // 最高学历
    cell = row.createCell(3);
    cell.setCellValue(employeeReportResult.getTheHighestDegreeOfEducation());
    // 国家地区
    cell = row.createCell(4);
    cell.setCellValue(employeeReportResult.getNationalArea());
    // 护照号
    cell = row.createCell(5);
    cell.setCellValue(employeeReportResult.getPassportNo());
    // 籍贯
    cell = row.createCell(6);
    cell.setCellValue(employeeReportResult.getNativePlace());
    // 生日
    cell = row.createCell(7);
    cell.setCellValue(employeeReportResult.getBirthDay());
    // 血型
    cell = row.createCell(8);
    cell.setCellValue(employeeReportResult.getZodiac());
    // 入职时间
    cell = row.createCell(9);
    cell.setCellValue(employeeReportResult.getTimeOfEntry());
    // 离职类型
    cell = row.createCell(10);
    cell.setCellValue(employeeReportResult.getTypeOfTurnover());
    // 离职原因
    cell = row.createCell(11);
    cell.setCellValue(employeeReportResult.getReasonsForLeaving());
    // 离职时间
    cell = row.createCell(12);
    cell.setCellValue(employeeReportResult.getResignationTime());
}
```
画面4：
```java
cell.setCellValue(employeeReportResult.getUserId());
```
画面5：
```java
cell.setCellValue(employeeReportResult.getUserId());
```
画面6：
```java
cell.setCellValue(employeeReportResult.getNationalArea());
```
画面7：
```java
cell.setCellValue(employeeReportResult.getBirthDay());
```
画面8：
```java
cell.setCellValue(employeeReportResult.getNativePlace());
```
画面9：
```java
cell.setCellValue(employeeReportResult.getBirthDay());
```
画面10：
```java
cell.setCellValue(employeeReportResult.getResignationTime());
```
画面11：
```java
cell.setCellValue(employeeReportResult.getResignationTime());
```
画面12：
```java
// 导出
```
画面13：
```java
cell.setCellValue(employeeReportResult.getNationalArea());
```
画面14：
```java
// 数据已填充
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

