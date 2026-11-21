# 03-考勤归档：归档列表和详情

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\03-考勤归档：归档列表和详情_【海量资源尽在 ubkz.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好了我们现在呢已经完成了这个新的报表的一个制作那接下来呢咱们就开始把剩下的最后一块内容给它完成出来那在这边呢各位来看是不是这边有一个历史规档那对于历史规档呢其实很简单就是去查询一下所有已经制作好的这些考勤的数据当然是查询每一个年度里面的每一个月的
[00:27] 那我们怎么做很简单那各位来看一点击历史归档那进入到这么一个页面那这个页面呢是根据年度去查询所有已归档的总表那每一个里面还有每一个总表每一个已归档总表下面的所有明细的一些数据那我们先把这个列表项给它做出来那我们可以打开F12各位一起来看一下我一点击刷新
[00:57] 好了各位会发现呢这边呢他会请求对应的这么一个链接reports year后面呢会携带一个参数当然了这边会多携带一个参数啊抱歉这个是前端应该出一点问题但是我想说最关键的year2019是对的那其实是查询2019年他涉及到的每一个月公司的考勤情况那我们查询表查询哪个表
[01:26] 注意那归档的数据呢是这两个表一个叫做monthly一个叫做monthlyinfo那上边是我们的主表数据底下代表的是我们的明细表数据那我们很明确要先查主表那如果看当前2019年7月看里面的每一个员工的信息是不是再去查这个info的明细表啊所以对于我们这边来说咱们要写的这个代码很简单请求的方法呢在这边摆着
[01:56] Ctrl C拿到这边咱们把这个代码呢给它补充完整归档归档的历史列表好了请求路径是这样的那请求方法就是一个get那同样的配置controllerOK同样的去配置里面的请求方法好了report year那注意这回呢我们携带的参数只需要一个year是不是就够了那接下来呢我们这边查询之后
[02:34] 应该要得到一个list列表那这个list列表里面封装的是不是就是主表的数据就是这个monthly没错吧所以我们这边monthly a t t找一下a t t e a r c ha t t e a r c hmonthly抱歉没有info好了这是我们最终要得到的数据列表
[03:20] 那注意我们查询呢就可以通过对应的归档Service点其一个方法名词呢就叫做find by year吧y y e a r要查询当年度的那把这个年份呢给他传进去就可以了好了这边是Service啊s e r v s e ok那注意这个方法呢不能重名我这边也是就叫做find reports by years
[03:58] 这样好看一下要明确那思维当中少方法在思维当中补充对应的一个方法就可以了根据年份查询当年的所有考勤历史好了那在这思维当中我们都知道这回就要调用DU了基本上逻辑都是比较简单的这个DU注入进来了吗注入进来了把这个DU拿过来点
[04:37] Find by a company ID抱歉这边呢少传递过来一个参数了我们要查询企业的company ID也传递过来那这边呢补充一个请求参数就是死菌类型的companycompany IDC-U-M-P-A-N-YID那注意这个第U层的方法我已经写好了直接把这个参数呢按照顺序传递过去就可以了好了我们一起来看一下
[05:09] 对应到这边returnreturn对应的do里面的这个方法好了里面这个方法呢其实就是按照名称FindBy开头来进行查询我们要根据common id以及传递的年份来查那我们来看一下数据库当中你传递过来有年份有common id是不是就按照这两个参数来进行查询好了这个就是我们查询的这么一个逻辑好了那这个方法比较简单那咱们继续再写一个
[05:40] 那如果说呢我们在页面上已经以列表的形式展示出来了每一个月份的这个数据有很多数据那接着呢它只是按月份展示它的统计数据那点击其中的一项里面要展示它的明细那这个是我们要做的那我需要说一下那我们现在做的事情相当于咱们展示出了主表
[06:08] 那接着是不是要显示从表里面的那些记录啊那主从结构根据我们这个表的规则来看我们现在把主表的列表产出来了我想看从表里面的明细那我们是不是就可以按照主表的ID从从表里面找到对应的这种外界关系来进查询啊所以呢咱们要进行查询呢还需要这么一个对应的详情就是查询查询
[06:39] 归档详情的这么一个对应的请求那同样的咱们拿过来Ctrl C Ctrl V考一份这个是我们接下来要查询的那我们这回呢来一个ID过来那注意它传递的一个参数这个参数ID代表的就是我们归档历史主表的ID懂我意思吧好那接下来
[07:08] 接下来同样是get请求没什么问题那我们这边就是find detail就叫find enforce吧enforce by id那把这个id咱们获取到就可以了好了那同样的这回呢我们得到的应该也是一个例子集合只不过呢这回我们的例子集合就不是monthly而是后面要加info等于
[07:45] 那同样的我们归档Service点Find好了注意这回呢就是Find这个MonthlyInfoBy注意这回别ByID了咱们By就叫AMID吧OK把这个ID呢传过去因为我们知道传过来的其实是这个从表的ID这个怕有疑问啊OK那接着Service补充一个方法查询归档详情列表
[08:30] 好了那接下来呢在这个里面呢咱做的这个方法呢其实也比较简单直接return那找到我们对应的info的dealinfo deal点find by其实这个咱们都已经写好了直接调用注意直接调用这个monthly这个ID各位来看一下数据库表外建是不是叫做att好了什么什么monthly下方向ID是不是就根据这个外建来查呀所以这边呢我们直接把这个
[09:01] 传递过来就可以了好了那这两个方法呢都比较简单那注意不管是刚才的归档历史列表还是我们这个详情那操作成功之后是不是要把对应的放到我们这个result当中把它返回到前端页面让页面去动态展示内容没错吧OK好了这个方法我们都写好了之后重新启动一下我们的微服务好了这边呢服务已经重新启动了我们回到页面一起来看一下
[09:31] 在这边呢可以找到历史归档点过来好了哎这个列表呢已经展示出来了没错吧那接着我们看一下7月份它的详情点击过来好了这个数据呢现在是暂无数据我们看一下哪报错了回到页面那回到我们的Java代码哎这边没什么问题那接着我们来检查一下
[09:54] 好了查看详情哦抱歉这边呢是我们的地址参数上边这是一个请求参数啊那对于这种地址参数呢我们需要在前边加上at pass哎玩儿宝是不是就可以了OK好了抱歉这个有点粗心了重新启动我们再来看一下效果好了这边呢让它去慢慢重启回到页面我们耐心等待刷新看一下最终的结果就可以了来重新加载还没有
[10:28] 耐心等待一下好了各位来看现在呢列表呢已经出现了那接下来来看一下详情已经有了同样的A01有11天正气上一个迟到一个早退那这样一来我们的员工历史归党相关的这块内容呢咱们也已经给他搞定了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中实现考勤历史归档功能，包括前端页面展示、后端 Controller 层接口定义、Service 层业务逻辑和 Dao 层数据持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示课程大纲，当前章节为“1.1 归档列表”，内容涉及 Controller 和 Service 层代码。
- Controller 层代码：
  ```java
  //查询年度归档
  @RequestMapping(value = "/reports/year", method = RequestMethod.GET)
  public Result findReports(String year) throws Exception {
      List<ArchiveMonthly> list = archiveService.findReportsByYears(year, companyId);
      return new Result(ResultCode.SUCCESS, list);
  }

  //查询月考勤明细
  @RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)
  public Result findReportsById(String id) throws Exception {
      List<ArchiveMonthlyInfo> list = archiveService.findReportsById(id);
      return new Result(ResultCode.SUCCESS, list);
  }
  ```

画面 2：
- 前端页面显示“员工历史归档”，但请求返回 404 Not Found。
- 网络面板显示请求 URL 为 http://localhost:8080/api/attendances/reports/year/...，状态码 404。

画面 3：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/archive/item", method = RequestMethod.GET)` 和 `@RequestMapping(value = "/newReports", method = RequestMethod.GET)` 方法。

画面 4：
- 在 AttendanceController.java 中，光标位于 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法的注释上方。
- 代码中显示 `List<ArchiveMonthly> list = archiveService.findReportsByYear(year, companyId);`。

画面 5：
- 在 AttendanceController.java 中，光标位于 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法的注释上方。
- 代码中显示 `List<ArchiveMonthly> list = archiveService.findReportsByYear(year, companyId);`。

画面 6：
- 展示 ArchiveService.java 文件，其中包含 `for (User user : users) { ... }` 循环和 `public List<ArchiveMonthly> findReportsByYear(String year, String companyId) { ... }` 方法。

画面 7：
- 展示 ArchiveService.java 文件，其中包含 `for (User user : users) { ... }` 循环和 `public List<ArchiveMonthly> findReportsByYear(String year, String companyId) { ... }` 方法。

画面 8：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 9：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 10：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)` 方法。

画面 11：
- 展示 ArchiveService.java 文件，其中包含 `public List<ArchiveMonthlyInfo> findMonthlyInfoByAid(String id) { ... }` 方法。
- 代码提示中显示 `findByArchiveMonthlyId(String atteArchiveMonthlyId)` 方法的多个重载选项。

画面 12：
- 前端页面显示“员工历史归档”列表，包含员工编号、姓名、工号、部门、手机和每日考勤状态。

画面 13：
- 展示项目结构，包含 `ihrm_parent` 和 `ihrm_attendance` 模块。
- 代码中显示 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 14：
- 前端页面显示“员工历史归档”列表，包含员工编号、姓名、工号、部门、手机和每日考勤状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
//查询年度归档
@RequestMapping(value = "/reports/year", method = RequestMethod.GET)
public Result findReports(String year) throws Exception {
    List<ArchiveMonthly> list = archiveService.findReportsByYears(year, companyId);
    return new Result(ResultCode.SUCCESS, list);
}

//查询月考勤明细
@RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findReportsById(String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findReportsById(id);
    return new Result(ResultCode.SUCCESS, list);
}
```

画面 6：
```java
for (User user : users) {
    ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
    //统计每个用户的考勤记录
    Map map = attendanceDao.statsByUser(user.getId(), archiveDate + "%");
    info.setStatsData(map);
    info.setTid(idWorker.nextId());
    info.setAtteArchiveMonthlyId(archiveMonthly.getId());
    archiveMonthlyInfoDao.save(info);
}

//总人数
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year) {
    archiveMonthly;
}
```

画面 11：
```java
public List<ArchiveMonthlyInfo> findMonthlyInfoByAid(String id) {
    return_archiveMonthlyInfoDao.findByArchiveMonthlyId(id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

