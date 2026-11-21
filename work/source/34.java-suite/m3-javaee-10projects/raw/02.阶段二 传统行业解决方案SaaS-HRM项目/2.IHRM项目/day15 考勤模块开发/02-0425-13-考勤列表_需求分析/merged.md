# 13-考勤列表：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\13-考勤列表：需求分析_【海量资源尽在 ubkz.com】.mp4
- 时长 8分29秒（音频 510s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在已经把这个代码呢全部都已经写好了但是这个代码现在还存在一些问题因为我们现在只关注的这个考勤状态呢只有有问题的是不是那些正常的状态还没管啊好了我们把这个代码呢简单的再来处理一下elseif如果这个没有迟到和早退那最后else就给它来一个这是我们的正常状态正常正常的一个状态点setadtaadtsdate好了我们给它来一个
[00:30] 注意数据库里面这边的状态全部都有相关的说明1代表正常OK好了那这样一来我们这个代码就已经全部都写好了把这些不相关的全部都关掉那我重新启动一下这个我们的微服务找到run来咱们开始启动好了我们这边让它启动回到我们这个页面部分咱们一起试一下刷新好了这边呢咱们找到导入设置
[01:13] 导入进去点击上传那在我桌面上呢已经准备好了一个咱们的数据那我这边呢导出之前啊先把这个数据库里面所有记录全给它干掉注意数据库里面一条记录都没有来点击上传好了这边呢已经导入成功了回到我们这边数据库一起再来看一下刷新好了里面有三条记录各位发现呢这边有一个是两个状态都是11
[01:49] 好了这个正常应该是对的这边有一个各位来看这个12点30它是不是应该是属于早退啊来看一下4是不是早退OK没问题好了那这样一来呢咱们就已经把这个数据导入这个功能呢已经给它做好了那数据导入咱们做好了之后咱们继续往下看那接下来呢我们关注的就是一个考勤的这么一个数据列表对应的我们这张图呢导入没问题接着我们来看这个考勤列表
[02:18] 那对于这个考勤列表咱们看一下它是怎么做到的那打开F12我们刷新一下页面来看一下好了这边呢有一个错误的请求就在这Attendance这么一个请求那请求过来之后呢有Page有Page Size代表的是我要进行一个分页查询的这么一个操作了那我简单的和各位做一个交代就是现在呢我们要做的是这个列表查询放到这边
[02:53] 代表的是我们考勤列表查询那对于这个考勤列表查询呢我们请求的这个UIL在这边给各位摆到这儿那接下来那对于这个列表呢它需要我们的有一些返回值那这个返回值呢我这边呢来写一下这个返回值呢是这样的什么result部分的那些内容我就不写了就主要写它的数据部分数据部分呢它需要三个第一个叫做data
[03:34] 是真正的数据好了接着呢第二个部分呢叫做monthofreport好那接着第三个呢代表countok一共有三个那第二个代表的是我们需要处理的日期就是我们现在考勤记录的这个处理日期那它底下这个代表的是我们代处理的处理的考勤考勤数量一共有这么
[04:10] 三部分内容那对于这个上面这部分内容呢它里面又划分了很详细啊那首先呢在里面一部分内容呢代表的是用户的信息那这个用户信息里面又包含一个历史集合那注意这个历史集合里面存的就是当前这个月份每天的考勤所以它就是这么一个返回值的这么一个状态那接下来呢我们想做的是你要写这么一个方法来进行匹配
[04:43] 那我们这边那应该怎么做呢好了我们可以一起来写一下好了首先呢我们这边请求的路径呢在这边那请求的方式是get回到我们的Controller当中回到Controller在Controller当中我们开始写一个查询数据列表查询我们的考勤数据列表at request买品啊这边呢考过来
[05:18] 那么请求路径就是这玩意儿所以这个我们就可以给它省略了我们的请求方式是get那这边会携带两个参数第一个int类型的叫做page第二个就是int类型的says这些应该各位都没有什么问题好那接下来那在我们这边要想进行处理咱们就需要调用Service来进行查询
[05:48] 这个应该各位都能够理解但是我查询得到一个什么类型的对象各位来看我要得到类型其实是三部分一个Data一个Mouse一个这一个三部分类型那这玩意是不是可以封装成一个Map集合每个Map里面再有自己对应的数据是就可以了所以我想说的是我们这边得到的应该是一个Map集合Map等于调用Service好了ServiceAutoVal注入进来PrivateService这边应该是
[06:24] 写错了叫 attserviceatt Service好了接下来拿到Service我们开始进行查询即可点其一个方法就是get attdata 好了接下来对于我们这个方法来说里面需要三个参数第一个参数就是一个map抱歉第一个参数就是我们的 company idok 第二个参数就是 page第三个参数就是 page set
[07:10] 去page set别写错啊要不就拿不到了好了引一下包把map传递进去好了那接下来呢在我们这个思维层方法咱们就开始去进行编写了那么要想去编写这个思维方法呢需要各位一定一定要明确的事情我们这边要获取用户的考勤的这个数据那这个考勤数据究竟从何而来
[07:42] 那首先咱们要看一下第一个找两个问这么几个问题就跟各位要说一下第一个这个考勤月究竟什么时候那你不能随便指定啊随便一月份二月份是这不行那第一个问题就是考勤月我们需要关注一下第二个问题就是这边我们要有一个分页显示没错吧要有一个分页的一个显示那接着呢还有第三个问题就是我们应该怎么查询那为什么要有这个问题呢是因为各位
[08:15] 在我们的页面上显示的内容呢相对来说可能比较多除了有当前这个考前记录还应该有用户所设计到的一些记录各位应该能够明白我意思OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个考勤系统中，通过前端上传Excel文件导入考勤数据，后端通过Spring Boot控制器接收并调用服务层处理，最终将数据写入数据库的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在IntelliJ IDEA中，展示`ExcelImportService.java`文件中处理考勤数据的逻辑，包括判断节假日、工作日、午休等规则，并调用`AttendanceConfig`和`AttendanceDao`进行数据处理。
画面2：在SQLyog中，展示一个用于查询考勤数据的SQL语句，使用了`CASE WHEN`语句根据`att_status`字段进行分组统计。
画面3：浏览器空白页，表示页面正在加载或尚未完成。
画面4：显示考勤导入页面，包含“点击上传”按钮和“将文件拖到此处”区域，提示用户上传考勤数据。
画面5：考勤导入页面，鼠标悬停在“点击上传”按钮上，显示“选择文件”和“拖拽文件”提示。
画面6：展示PPT页面，内容为“day15”，标题为“3.3 考勤修改”，并展示了一段Java代码，用于保存月度考勤数据。
画面7：浏览器开发者工具中，显示了页面加载的网络请求，包括`localhost`和`app.js`。
画面8：浏览器开发者工具中，显示了对`/attendances/page=10/pageSize=10`请求的404错误响应。
画面9：在IntelliJ IDEA中，展示项目结构，包括`AttendanceController`、`AttendanceService`等类，并显示了Hibernate日志，记录了数据库的增删改查操作。
画面10：在IntelliJ IDEA中，展示`AttendanceController.java`文件，其中定义了`@RequestMapping("/attendances")`和`@Autowired private ExcelImportService excelImportService;`。
画面11：在IntelliJ IDEA中，展示`@RestController`注解下的`@RequestMapping`方法，用于处理上传Excel文件。
画面12：在IntelliJ IDEA中，展示`AttendanceController.java`文件，其中定义了`@Autowired private Attoce`，并显示了`@RequestMapping`方法。
画面13：在IntelliJ IDEA中，展示`AttendanceController.java`文件，其中定义了`@RequestMapping`方法，用于处理分页查询考勤数据。
画面14：在IntelliJ IDEA中，展示`AtteService.java`文件，其中定义了`@Autowired`注解的多个DAO对象，并展示了一个`getAtteDate`方法的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
if(holidays.contains(attuploadvo.getAtteDate())) {
    attendance.setAtteStatus(22); //休息
} else if(DateUtil.isWeekend(attuploadvo.getAtteDate()) && !workingDays.contains(attuploadvo.getAtteDate())) {
    attendance.setAtteStatus(22); //休息
} else if(DateUtil.comparingDate(att.getAfternoonStartTime(), attuploadvo.getAtteTime()) //第一个参数：规定时间，第二个参数：打卡时间
    attendance.setAtteStatus(3); //迟到
} else {
    //...
}
```

画面2：
```sql
SELECT COUNT(*) as c,
       COUNT(CASE WHEN att_status = 1 THEN 1 END) as t,
       COUNT(CASE WHEN att_status = 2 THEN 1 END) as s,
       COUNT(CASE WHEN att_status = 3 THEN 1 END) as l,
       COUNT(CASE WHEN att_status = 4 THEN 1 END) as d,
       COUNT(CASE WHEN att_status = 5 THEN 1 END) as a,
       COUNT(CASE WHEN att_status = 6 THEN 1 END) as f,
       COUNT(CASE WHEN att_status = 7 THEN 1 END) as h,
       COUNT(CASE WHEN att_status = 8 THEN 1 END) as i,
       COUNT(CASE WHEN att_status = 9 THEN 1 END) as n,
       COUNT(CASE WHEN att_status = 10 THEN 1 END) as o,
       COUNT(CASE WHEN att_status = 11 THEN 1 END) as p,
       COUNT(CASE WHEN att_status = 12 THEN 1 END) as q,
       COUNT(CASE WHEN att_status = 13 THEN 1 END) as r,
       COUNT(CASE WHEN att_status = 14 THEN 1 END) as s,
       COUNT(CASE WHEN att_status = 15 THEN 1 END) as t,
       COUNT(CASE WHEN att_status = 16 THEN 1 END) as u,
       COUNT(CASE WHEN att_status = 17 THEN 1 END) as v,
       COUNT(CASE WHEN att_status = 18 THEN 1 END) as w,
       COUNT(CASE WHEN att_status = 19 THEN 1 END) as x,
       COUNT(CASE WHEN att_status = 20 THEN 1 END) as y,
       COUNT(CASE WHEN att_status = 21 THEN 1 END) as z,
       COUNT(CASE WHEN att_status = 22 THEN 1 END) as A,
       COUNT(CASE WHEN att_status = 23 THEN 1 END) as B,
       COUNT(CASE WHEN att_status = 24 THEN 1 END) as C,
       COUNT(CASE WHEN att_status = 25 THEN 1 END) as D,
       COUNT(CASE WHEN att_status = 26 THEN 1 END) as E,
       COUNT(CASE WHEN att_status = 27 THEN 1 END) as F,
       COUNT(CASE WHEN att_status = 28 THEN 1 END) as G,
       COUNT(CASE WHEN att_status = 29 THEN 1 END) as H,
       COUNT(CASE WHEN att_status = 30 THEN 1 END) as I,
       COUNT(CASE WHEN att_status = 31 THEN 1 END) as J,
       COUNT(CASE WHEN att_status = 32 THEN 1 END) as K,
       COUNT(CASE WHEN att_status = 33 THEN 1 END) as L,
       COUNT(CASE WHEN att_status = 34 THEN 1 END) as M,
       COUNT(CASE WHEN att_status = 35 THEN 1 END) as N,
       COUNT(CASE WHEN att_status = 36 THEN 1 END) as O,
       COUNT(CASE WHEN att_status = 37 THEN 1 END) as P,
       COUNT(CASE WHEN att_status = 38 THEN 1 END) as Q,
       COUNT(CASE WHEN att_status = 39 THEN 1 END) as R,
       COUNT(CASE WHEN att_status = 40 THEN 1 END) as S,
       COUNT(CASE WHEN att_status = 41 THEN 1 END) as T,
       COUNT(CASE WHEN att_status = 42 THEN 1 END) as U,
       COUNT(CASE WHEN att_status = 43 THEN 1 END) as V,
       COUNT(CASE WHEN att_status = 44 THEN 1 END) as W,
       COUNT(CASE WHEN att_status = 45 THEN 1 END) as X,
       COUNT(CASE WHEN att_status = 46 THEN 1 END) as Y,
       COUNT(CASE WHEN att_status = 47 THEN 1 END) as Z,
       COUNT(CASE WHEN att_status = 48 THEN 1 END) as a,
       COUNT(CASE WHEN att_status = 49 THEN 1 END) as b,
       COUNT(CASE WHEN att_status = 50 THEN 1 END) as c,
       COUNT(CASE WHEN att_status = 51 THEN 1 END) as d,
       COUNT(CASE WHEN att_status = 52 THEN 1 END) as e,
       COUNT(CASE WHEN att_status = 53 THEN 1 END) as f,
       COUNT(CASE WHEN att_status = 54 THEN 1 END) as g,
       COUNT(CASE WHEN att_status = 55 THEN 1 END) as h,
       COUNT(CASE WHEN att_status = 56 THEN 1 END) as i,
       COUNT(CASE WHEN att_status = 57 THEN 1 END) as j,
       COUNT(CASE WHEN att_status = 58 THEN 1 END) as k,
       COUNT(CASE WHEN att_status = 59 THEN 1 END) as l,
       COUNT(CASE WHEN att_status = 60 THEN 1 END) as m,
       COUNT(CASE WHEN att_status = 61 THEN 1 END) as n,
       COUNT(CASE WHEN att_status = 62 THEN 1 END) as o,
       COUNT(CASE WHEN att_status = 63 THEN 1 END) as p,
       COUNT(CASE WHEN att_status = 64 THEN 1 END) as q,
       COUNT(CASE WHEN att_status = 65 THEN 1 END) as r,
       COUNT(CASE WHEN att_status = 66 THEN 1 END) as s,
       COUNT(CASE WHEN att_status = 67 THEN 1 END) as t,
       COUNT(CASE WHEN att_status =

