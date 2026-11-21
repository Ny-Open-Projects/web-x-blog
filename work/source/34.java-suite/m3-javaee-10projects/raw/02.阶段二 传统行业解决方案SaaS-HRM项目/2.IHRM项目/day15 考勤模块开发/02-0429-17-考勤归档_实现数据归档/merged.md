# 17-考勤归档：实现数据归档

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\17-考勤归档：实现数据归档_【海量资源尽在 ubkz.com】.mp4
- 时长 11分13秒（音频 674s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们现在呢已经完成了它这个归档数据表的这个查询那接下来呢我们就开始真真正正的实现归档把我们查询的记录把它保存到对应的归档历史表还有归档明细表当中好那针对这个应该怎么做呢回到我们的页面打开F12一起来看一下好了点击归档走你会发现它请求了一个UIL请求到这个归档item下
[00:31] 传递一个日期管来是用get的方式指的是我们要对2019年7月份的数据真正进行归档了那我们这个写起来呢相对来说呢也没那么难因为我们能够查询这个数据就能够查询出来把它保存到数据库里没错吧好了那接着回到我们这边找到对应的方法咱们一起把这个代码呢给它完善出来写到下边这个就是我们真正的数据归档归A档
[01:07] 好了在上面的配置一个方法好了那这边的需要各位注意一下需要各位注意一下我们要写这个数据轨档的这有一个小小的问题是因为页面部分啊因为部分他请求的是叫做什么哎这这这这这个路径请求的是这么一个路径那这些这个路径的究竟请到请求到好不好呢这个因人而异了那如果说要让他能够进入到我们当前的这个系统需要改一下我们这个页面部分
[01:39] 在页面部分前面给他再去加一个请求注意我这边呢已经给他改好了改好了之后回到我们这边呢再来试一下因为他这个请求的这个路径有点问题OK没问题了那接下来呢我们就可以了把这个路径呢Ctrl C拷过来再来去写我们的代码OK请求的是这一串那请求方式我们刚才看过没问题那我们的参数呢也没问题那这样一来
[02:23] 我们就开始着手去写里面的代码当了操作成功之后直接告他成功就可以了好了接下来我们调用的就是Service跟上面一样了归档Service arch归档Service.好了我们叫做save归档信息ach arch ave ar ch ave没问题好了接着把我们日期传递过去就可以了接着在Service层我们开始真正的
[02:58] 完成我们的数据归档那对于Service层这个数据归档呢其实这个代码呢跟我们刚才自己写的那套归档代码其实差不太多啊那么把之前这个代码呢给它拷过来一部分就在这儿把这一段Ctrl C拷过来然后呢我们做一个简单的修改好了这段先别管它我们来看一下那就是说呢我们现在要做相应的这个数据归档那数据归档呢
[03:34] 我们之前这段查询是不是只是去查询或者统计到了我们这边用户的明细部分那对于上边这个总表数据是不是还没有啊所以我们这回呢进行归真正的归档不仅要底下上边其实也需要有了哎这个是我们需要关注的点好了所以我们这边呢要进行归档一共要做两两件事第一个事情呢就是保存我们对归档主表数据
[04:05] 那第二个点呢就是保存我们的归档归档明细表的数据OK那归档主表数据归档明细表数据这些呢都需要我们自己去创建出来那当然了那当然了我们这边呢先去把这个基本的代码呢先给它编写出来归档的主表数据呢我们是一个对象啊这个对象呢就叫做什么什么Mosley好了我们来找到这个对象OK
[04:50] 等于new一个对象出来好了那接下来呢咱们这一个归档主表数据那归档的主表的这些数据究竟有什么呢我们这边可以一起来看一下这个表里面需要什么这个表里面company id好了这个部门id呢其实这是一个选填的填不填都行好了这边有我们的归档的年份有我们的归档月份各位应该看到了它是有年份有月份还有总人数以及全勤的人数
[05:22] 就是这么几个字段那对于咱们这边来说呢总人数等等其实这个比较好查先去在上边查询用户抱歉我们归档的时候应该少传一参数啊ID好了这边少一参数死去类型的company ID好了userdo上边我们已经有了那通过userdo我们能够把这个给他查询出来OK好了那接下来
[06:07] 那我们就可以往里面设置相应的数据了设置数据打点set id id worker点一大堆那接着呢就是一个一个的把这些值呢给它设置上其实就可以了点set company idcompany id拿进来点set好了注意我们这边有统计计算的年点set我们这边有统计计算的月这个相对来说有点麻烦
[06:43] 我们需要对这个日期呢做一个小小的处理点substream哎我们传递过来的是0.4因为我们传递的数据类型是这样2019-07哎07那这样我们拿前四位是不是就可以了从零开始那这个月份呢就是从哎我们就是从第五位开始拿拿到第七位就可以了从第五位开始拿substream哎从第五位开始拿就可以了OK
[07:17] 好了那这样一来呢我们把这个主表的这些数据呢给它准备好了接下来呢我们就开始构造明细表的数据那构造明细表的数据其实这边也就是开始循环嘛开始循环那循环的时候呢同样我们要明细的这个info同样的用map同样也要这边只不过我们要涉及到保存那保存的话就不需要给它收集到list结合里了嘛好了保存就需要我们多去添加一个IDinfo.setid
[07:48] ID worker.nextint没错吧除了这个之外除了这个之外我们还应该要保存它们之间的关系上面这个主表底下是从表所以从表应该保存一个主表的外件好了我们开始info.set能够找到这个外件那就是上面这玩意儿.get.getID没错吧好了那接下来我们就可以把这个明细给它保存起来明细.info.
[08:20] sale info存进去好了注意啊这个日期这改一下那这样一来呢我们的明细保存进去了那明细保存进去之后我们这边呢其实可以设置这个设置还没设置完啊在底下设置吧点我们设置的因为我们刚才这个历史的总表或者主表我们刚才看过里面还需要设置一些比如说其他的参数比如说总人数总人数比如说其他的一些参数
[08:58] 直接写吧点set total people number那这个其实就是我们的users点set就是你一共有多少人点set就是这个是全勤的这些人那注意这个全勤的这些人呢其实需要从数据库里面进行统计吧那这个统计这个统计查询呢我这边就不做了我就认为总人数他全部都统全勤了
[09:26] 好了这边呢还有一些其他的比如说点set is注意这个是一个固定值只是一个0就可以了最后我们可以把这个我们的这个主表数据给它保存到数据库当中哎抱歉不是info哎保存到数据库当中这个啊在这儿ok那好了这样一来我们这个归档的相关工作咱们也就已经做好了怎么变大写了奇怪啊ok再来一下改成小写的才对啊
[10:22] OK好了这样一来我们这个代码写好了重新启动一下我们这边的微服务一起来看一下效果好了还是那句话这个重新启动实在是有点慢不浪费各位时间我暂停一下好了这边呢Tomcat已经启动成功了那我们在晋升归档之前呢我把这些归档的数据呢全部给它删掉啊主表数据全部删掉从表数据全部删掉好了东西比较多没有了哎没有了那接着我们开始归档来试一下
[10:55] 来走归档确定好了这边呢其实已经归档成功了我们一起来看一下好了主表有数据那接着从表示数据也已经导进来了好了那这样一来其实我们这个归档的操作呢就已经完成了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事系统中，通过后端 Java 代码实现“导出月度考勤报表”的功能，包括前端页面展示、控制器方法定义、服务层逻辑处理及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：前端页面展示“201907月人事报表”，包含员工姓名、工号、部门、考勤数据等字段，页面有“导出”按钮。
画面 2：后端控制器 `AttendanceController.java` 中定义了 `/reports` 和 `/archive/item/archiveDate=201907` 的 GET 请求，用于获取报表数据。
画面 3：前端页面再次展示“201907月人事报表”，鼠标悬停在“调休”列。
画面 4：服务层 `ArchiveService.java` 中的 `getReports` 方法，用于获取月度报表数据。
画面 5：`ArchiveService.java` 中的 `saveArchive` 方法，用于保存归档数据，包含查询用户、统计考勤、创建归档对象等逻辑。
画面 6：`ArchiveService.java` 中的 `saveArchive` 方法，展示注释和代码结构。
画面 7：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置公司ID。
画面 8：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置归档年份和月份。
画面 9：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置部门ID。
画面 10：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置归档月份。
画面 11：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置总人数和全勤人数。
画面 12：控制器 `AttendanceController.java` 中定义了 `/archive/item/archiveDate=201907` 的 GET 请求，用于获取归档数据。
画面 13：数据库表 `archive_monthly_info` 的结构，包含 `id`, `company_id`, `department_id`, `archive_month`, `archive_year`, `total_people_num`, `full_attendance_people_num`, `is_archived` 等字段。
画面 14：数据库表 `archive_monthly_info` 的结构，与画面 13 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
public Result importExcel(int page,int pagsize) throws Exception {
    Map map = attService.getAttDate(page,pagesize);
    return new Result(ResultCode.SUCCESS,map);
}

/**
 * 编辑用户的考勤记录
 */
@RequestMapping(value = "/id",method = RequestMethod.PUT)
public Result editAtte(Attendance attendance) throws Exception {
    attService.editAtte(attendance);
    return new Result(ResultCode.SUCCESS);
}

/**
 * 获取月度报表数据
 */
@RequestMapping(value = "/reports",method = RequestMethod.GET)
public Result reports(String attDate) throws Exception {
    List<ArchiveMonthlyInfo> list = attService.getReports(attDate,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

/**
 * 数据归档
 */
@RequestMapping(value = "/archive/item/archiveDate=201907",method = RequestMethod.GET)
```

画面 4：
```java
public List<ArchiveMonthlyInfo> getReports(String attDate, String companyId) {
    List<User> users = userDao.findByCompanyId(companyId);
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
    return list;
}
```

画面 5：
```java
public static void saveArchive(String archiveDate) {
    //1.查询所有企业用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户，统计每个用户的当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //统计每个用户的考勤记录
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
}
```

画面 6：
```java
private ArchiveMonthlyInfoDao archiveMonthlyInfoDao;
private UserDao userDao;
private Idworker idworker;

//数据归档
public void saveArchive(String archiveDate,String companyId) {
    //1.查询所有企业用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户，统计每个用户的当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //统计每个用户的考勤记录
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
}
```

画面 7：
```java
archiveMonthly.setCompanyId(companyId);
```

画面 8：
```java
archiveMonthly.setArchiveYear(archiveDate.substring(0, 4)); //201908
archiveMonthly.setArchiveMonth(archiveDate.substring(5));
```

画面 9：
```java
archiveMonthly.setDepartmentId(departmentId);
```

画面 10：
```java
archiveMonthly.setArchiveMonth(archiveDate.substring(5));
```

画面 11：
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttendancePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
```

画面 12：
```java
/**
 * 获取月度报表数据
 */
@RequestMapping(value = "/reports",method = RequestMethod.GET)
public Result reports(String attDate) throws Exception {
    List<ArchiveMonthlyInfo> list = attService.getReports(attDate,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

/**
 * 数据归档
 */
@RequestMapping(value = "/archive/item/archiveDate=201907",method = RequestMethod.GET)
```

画面 13：
```sql
CREATE TABLE `archive_monthly_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `archive_month` varchar(255) DEFAULT NULL,
  `archive_year` varchar(255) DEFAULT NULL,
  `total_people_num` int(11) DEFAULT NULL,
  `full_attendance_people_num` int(11) DEFAULT NULL,
  `is_archived` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

