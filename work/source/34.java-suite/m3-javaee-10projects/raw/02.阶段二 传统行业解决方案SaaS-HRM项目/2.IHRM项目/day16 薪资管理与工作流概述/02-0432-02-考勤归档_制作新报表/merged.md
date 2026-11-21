# 02-考勤归档：制作新报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\02-考勤归档：制作新报表_【海量资源尽在 ubkz.com】.mp4
- 时长 8分37秒（音频 518s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了咱们先来看第一项啊就是这个归档报表那这个归档报表呢在之前的课程当中呢我们已经把代码给他写好了没错吧好了在这边点击考勤点击到月报表那注意啊这边呢我发现了一个小小的问题就是A1这个人啊他这边这个当月呢应该有这么很多数据那我一点击7月份报表呢各位发现这个A1现在这个数据呢是不是还都是
[00:29] 零啊没错吧所以这儿有一个小小的问题我们先把这个问题呢给它解决掉啊那打开F12咱们一起来检查一下我先刷新一把看一下它发送的请求好了发送的请求叫做Reports传递了一个ATDEData这么一个参数那回到我们的Controller当中咱们来找一下好了我们的Controller请求的就是上边这个了我们的考勤Controller点进去好了Reports
[01:04] 应该是reports没错吧reports get方式请求那reports get方式请求抱歉咱们这边接收的参数是不是这个data应该改成attdata是不是就可以了这样一来就可以了因为刚才的参数没有对应上那SpriteVC就不会把数据接收过来所以这边改一下就可以了OK好了我这边重新启动一下
[01:32] A服务咱们一起再来看一下效果看一下数据是不是已经显出来了好了我这边呢服务已经重新启动成功了清空一下空台回到浏览器来刷新再来看一下效果OK没关系啊刚刚重启可能是我们的网关没有反应过来好了现在呢数据已经有了那各位会发现当前这边A1这个人有10个正常的流程没错吧那接着回到我们的考勤列表这边
[02:06] 默认呢我们现在是7月份的考勤那在这边呢咱们可以给他来一个这个就来一个叫迟到吧有一天迟到好了有一天早退那再来一天正常我们来看一下数据呢是不是有变化来走好了进来之后各位发现正常是一天一天迟到一天早退OK
[02:39] 没什么问题没错吧OK好了那这样一来呢咱们这个报表呢进来了那接下来呢咱们也完成了归档为点归档好了已经归档成功这个都没什么问题那已经归档成功了之后接下来呢就是说啊那你点击考勤就会发现现在制作的还是七月份的考勤没错吧那我们如何让它变成下一个月考勤呢
[03:04] 好了是在这边找到这个报表那如果想要制作新月份的报表我们只需要在这边点击新建报表其实就可以了那不知道各位还有没有印象其实这个逻辑跟我们之前做的社保逻辑基本上是一模一样的那社保逻辑这边打到社保逻辑那报表点进来之后你发现这边是不是有一个新建报表那新建报表也就意味着7月份报表归档之后没有问题了我们可以制作8月份的内容了
[03:33] 同理考勤也是这么一个逻辑那各位来看一下那我们之前是用什么进行控制其实就是通过在数据库当中一张表叫做company settingcompany setting好了这边还有company setting好了以及我们这边的考勤同样也有这么一个company setting这么一个表这个就是在去记录企业他已经完成的
[04:03] 制作报表的这个月份那比如说现在是07所以你需要去做7月份报表那我要做8月份怎么办只需要在页面部分是不是点击新建把当前的这个07改成08那进来的时候是不是就开始制作8月份的报表没错吧所以我先把这个功能给它完善出来那回到页面
[04:25] 我一点击新在报表点击确定你会发现这边向服务器传递了一个请求代表的是new report制作新的它传递了这么一个参数两个参数第一个是ATTData当前时间以及咱们要制作的新的时间201908当前是不是07月份OK接着我们开始把这个给它完善出来注意是get请求Ctrl C回到我们的代码部分
[04:55] 找到当前的Controller叫做新建报表好了请求的链接在这边我们的请求方式是get那好了配置一个方法control c control v配置一个方法过来我们的请求附路径前面已经有了所以这边不需要再去进行编写了那注意他请求过来路径就是new reports那接下来这回是以get形式是不是提交过来两个请求参数
[05:30] 所以呢我们这两个请求参数配置到方法上边那注意我说一下这两个参数呢其实我们只用这个ear mouse其实就够了哎没错了OK那接着我们点击新建报表之前说过了很简单就是去调用Service那调用do把我们这个相应的数据呢由刚才的07是不是改成08呀那注意我们怎么做很简单找到对应的Service
[06:02] 好了我看一下哪个Service里面有对应的这个setting deal我就用这个Service了Service点好了我叫new report那接着把这个ear mouse传过去千万别忘了我们还有company id也传递过去就可以了那Service当中补充一个方法新建报表其实说的直白一点就是将settingcm pny中的这个月份
[06:39] 修改为指定的数据指定的这个数据其实就可以了这个比较简单那我们这回呢要做的事情注意很明确了就是把数据库表这个setting查询出来是不是把它进行修改就可以了没错吧那我们查询就根据企业ID来查就可以了那回到这边我们找到对应的docompany setting do点那注意啊
[07:06] 咱们这个系统当中呢这个company是它的主件是它的主件我们来看一下company id主件所以我们调用do就是find by id把咱们传递过来的company id传过来就可以了find by idid传过来点点点get好了得到了这个siting数据那我们接下来要做的事情就是siting点setdatamounts
[07:45] 把这个传递进去好了接下来调用do.save那我们知道save呢它其实两层含义可以保存也可以诶更新诶抱歉setting传进去好了这样一来咱们这个代码呢就已经写好了我刷新诶我重新启动一下咱们一起来看一下效果好了这边呢我已经重新启动成功了回到我们的页面部分来刷新一把好了数据呢已经获取到了目前呢我们还是制作的是
[08:19] 7月份相关的报表那接下来我点击新建报表点击确定好那这样一来你会发现它已经重新跳转到了我这个列表页面是不是这回制作就变成了8月份报表没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的人事考勤系统，重点讲解月度考勤报表的前端展示、后端控制器与服务层代码实现，以及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：前端页面显示“201907月人事报表”，包含员工姓名、工号、手机号、部门、考勤状态等字段，数据来自后端接口。
画面2：IDEA项目结构，展示项目根目录 `ihrm_parent` 及其子模块，如 `ihrm_attendance`、`ihrm_common` 等。
画面3：打开 `AttendanceController.java`，查看 `@RequestMapping(value = "/reports", method = RequestMethod.GET)` 方法，用于获取月度考勤报表。
画面4：前端页面显示“201907月人事报表”，数据加载完成，页面状态正常。
画面5：前端页面展示“201907月考勤明细”，显示员工每日考勤状态，弹窗提示“统计考勤时，异常状态优先正常状态”。
画面6：前端页面显示“201907月人事报表”，数据中某员工“正常”考勤次数为11，“迟到次数”为1，“早退次数”为1。
画面7：点击左侧菜单“社保”。
画面8：SQLyog 数据库管理工具，显示 `att_archive_monthly` 表结构，字段包括 `company_id`, `department_id`, `archive_year`, `archive_month`, `total_people_num`, `full_attend_people_num`, `late_num`, `early_leave_num`, `create`。
画面9：IDEA 中 `AttendanceController.java`，查看 `@RequestMapping(value = "/archive/item", method = RequestMethod.GET)` 方法，用于获取月度考勤明细。
画面10：IDEA 中 `AtteService.java`，查看 `@Autowired` 注解的 `excelImportService`、`atteService`、`archiveService` 字段。
画面11：IDEA 中 `AtteService.java`，查看 `getReports` 方法，其中包含 `UserDao.findUserByCompanyId` 查询用户，`attendanceDao.statsByUser` 获取考勤统计。
画面12：IDEA 中 `AtteService.java`，查看 `getReports` 方法，光标在 `companySettingsDoc.findById(companyId).isPresent()` 语句上，提示“expected”。
画面13：IDEA 项目结构，展开 `src/main/java/com/ihrm/attendance/Service` 目录，显示 `AtteService.java` 文件。
画面14：前端页面显示“201907月考勤明细”，展示员工每日考勤状态，如“迟到”、“旷工”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3代码：
```java
/**
 * 获取月度考勤数据
 * /attendances/archive/item?archiveDate=201907
 */
@RequestMapping(value = "/reports", method = RequestMethod.GET)
public Result reports(String archiveDate) throws Exception {
    List<ArchiveMonthlyInfo> reports = atteService.getReports(archiveDate, companyId);
    return new Result(ResultCode.SUCCESS, reports);
}
```

画面9代码：
```java
/**
 * 获取月度考勤明细
 * /attendances/archive/item?archiveDate=201907
 */
@RequestMapping(value = "/archive/item", method = RequestMethod.GET)
public Result item(String archiveDate) throws Exception {
    archiveService.saveArchive(archiveDate, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面11代码：
```java
/**
 * 获取月度考勤数据
 */
public List<ArchiveMonthlyInfo> getReports(String atteDate, String companyId) {
    //1.查询所有企业用户
    List<User> users = userDao.findUserByCompanyId(companyId);
    //2.循环所有用户，查询每个用户的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        Map map = attendanceDao.statsByUser(user.getId(), Integer.parseInt(atteDate.substring(0, 2)) + 1);
        System.out.println(user.getId() + " " + atteDate);
        info.setStatsData(map);
        list.add(info);
    }
    return list;
}
```

画面12代码：
```java
//处理报表，若companySetting中的月份序号为指定的月份
public void newReports(String yearMonth, String companyId) {
    companySettingsDoc.findById(companyId).isPresent();
}
```

画面8 SQL：
```sql
company_id department_id archive_year archive_month total_people_num full_attend_people_num late_num early_leave_num create
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

