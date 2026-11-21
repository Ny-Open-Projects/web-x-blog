# 04-考勤归档：查询用户归档历史

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\04-考勤归档：查询用户归档历史_【海量资源尽在 ubkz.com】.mp4
- 时长 7分52秒（音频 472s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那就目前呢咱们已经完成了这个归档这块内容那除了归档之外呢其实还有最后一个功能那最后一个功能是这样的就是我们计算工资的时候是不是要从社保获取数据那同样的也要从考勤当中获取其中一个人员当月的这个考勤情况其实说的直白一点重点就是看他以归档的这些数据的考进情况那比如说我一会要制作
[00:29] 7月份工资那制作7月份工资的时候要去拿7月份已归档的社保的情况要去拿7月份已归档的这个考勤情况再去计算那所以我一会儿要为其他的微服务是不是还要提供这么一个接口那这个接口主要目的是不是就是去查询已归档的详情那比如说要查A02要查7月份的这么一个归档数据没错吧
[00:57] 所以我们接来就把这个功能呢也给他哎搞定那回到我们这边Controller那接来呢咱们开始补充一个方法这个方法就是根据用户ID和月份咱们查询以以归档的我们叫做考勤明细好了这个是我们要做的事情那注意啊这边呢
[01:27] 这个UIL我直接就跟各位交代清楚了那么要请求的UIL注意啊就是好了接着再来传递过来两个参数一个叫做user ID好了那接着再来一个就是我们的年份和月year monthOK这个是我们要请求的UIL那注意请求方式呢其实就是get过来各位发现两个参数一个是ID一个是不是这个
[02:00] 月份没错吧那接着我们把这个方法呢给他补充出来at request 啊买品注意我从上面直接call了那请求的这个 ui 号ctrl c 给他拿过来ctrl v那接下来呢参数一个有 user id再来一份好了一个是年份哎月份那我们这个请求的方法名称呢换一下咱们就叫做 history date就是查询历史归档的明细数据
[02:35] 那接下来呢我们这边要查询明细那明确得到的这个详情明细里面是不是只有一条记录所以就不应该是list我们只能得到一条记录就可以了info那接着把这个info呢放到我们的返回当中即可那中间我们要查询就可以点finduser就是查他的归档明细嘛detail
[03:05] 这个起了一个名字那把这两个参数呢层层传递下去这回传到Service好了Service当中补充对应的一个方法根据用户ID和年月查询查询归档名系主要是为了我们之后计算工资主要是为了页面一个显示的一个效果那在这边呢咱们直接return通过do来查询
[03:39] 好了我们一起来看一下数据库那这边数据库呢咱们现在对应的就是这个info表那看一下这个数据其实各位会发现我们这个数据库表上呢有user id还有就是你归档的这个日期那我们要查询是不是就可以根据user id还有归档日期来查没错了好了那回到我们代码那我们就可以写个方法就是findfind吧好了我在do里面把这个方法补充完成吧返回值没问题
[04:14] Find by user id按到好了我们还要根据归档日期来进行查询好了归档日期arch没问题归档日期那我们这边需要传递两个参数死去类型的user id进来死去类型的我们的归档日期传进来好了我补充一段
[04:57] 注释OK那我们的DU准备好了这边直接调用DU直接在因为在DU里面写这个方法定义方法它有提示会快一些底下这个方法Bandby user ID&这个提示搞得不太好多一段内容OK这样一来Bandby user ID&这边是归档日期这回没什么问题了改一下方案名OK这回没什么问题了
[05:39] 那这样一来我们这个方法呢已经写好了同样的这个比较麻烦啊要重新启动一下我们再来验证一下好了验证这个呢相对来说呢很简单找到我们这边的postman好了打开它那我们现在要请求的直接呢就是去请求一下我们当前的这个微服务我就不经过网关了因为我当前这个微服务呢不用登录也能访问好了请求的端口呢就是9005
[06:11] 那接着我把这边呢该清的我就清空了关掉127.0.0.1冒号9005-抄一下请求路径咱们一起来看一下效果一段拷过来user id我从数据库里面随便找一个替换请求日期201907这个都没什么问题好了那接下来走
[06:54] 这个还要我登录是吧这个就有点麻烦了那没办法我就先去登录了127.0.0.1这个其实不用登录也行啊因为这边呢咱们说了少一个header那我们从页面上把这个header直接给它拷过来其实就行了好了这边呢我们随便找一个请求各位发现在浏览器上咱们访问的时候是不是这直接有一个头
[07:35] 我们的认证的头那加一个header过去那value就是这一大段control c拿过来好了接着再来请求一下这样一来各位发现数据呢其实已经产生出来了没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot 后端代码实现员工考勤档案的查询与展示功能，并通过 Postman 进行接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iHRM 系统前端页面，显示“员工历史归档”列表，包含年份筛选和数据表格。
画面 2: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，展示用于查询年份报表和用户月度详情的两个 GET 接口方法。
画面 3: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，展示用于查询用户月度详情的接口方法。
画面 4: 在 SQLyog 中查看数据库表结构，左侧显示数据库对象列表，右侧为空白。
画面 5: 在 IntelliJ IDEA 中查看 ArchiveMonthlyInfoDao.java 文件，展示根据归档ID查询的接口方法。
画面 6: 在 IntelliJ IDEA 中查看 ArchiveMonthlyInfoDao.java 文件，光标在方法名后，准备输入。
画面 7: 在 IntelliJ IDEA 中查看 ArchiveService.java 文件，展示用于查询用户月度详情的方法。
画面 8: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，光标在方法名后，准备输入。
画面 9: 展示桌面，显示“黑马程序员”和“博学谷”的标志。
画面 10: 在 Postman 中设置一个 POST 请求，目标地址为 127.0.0.1:9007/user/process/deploy。
画面 11: 在 Postman 中显示多个窗口的缩略图，包括 IntelliJ IDEA、SQLyog、浏览器等。
画面 12: 在 Postman 中设置一个 GET 请求，目标地址为 127.0.0.1:9007/attendance/archive/1063705899262277968/201907，请求体为 JSON 格式。
画面 13: 在浏览器开发者工具中查看网络请求，显示“2019-7月员工报表”的页面加载情况。
画面 14: 在 Postman 中查看 GET 请求的响应结果，显示 JSON 格式的数据，包含“success”、“code”、“message”等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping(value = "/reports/year", method = RequestMethod.GET)
public Result findReportsByYear(String year) throws Exception {
    List<ArchiveMonthly> list = archiveService.findReportsByYear(year,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

// 查询归档详情
@GetMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findInfosById(@PathVariable String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findMonthlyInfoByMid(id);
    return new Result(ResultCode.SUCCESS,list);
}

// 快速用户月度详情
// /archive/{userId}/{yearMonth}
@GetMapping("/archive/{userId}/{yearMonth}")
```

画面 3:
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
atteArchiveMonthlyDao.save(archiveMonthly);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year,String companyId) {
    return atteArchiveMonthlyDao.findByCompanyIdAndArchiveYear(companyId,year);
}

// 查询当月详情列表
public List<ArchiveMonthlyInfo> findMonthlyInfoByMid(String id) {
    return archiveMonthlyInfoDao.findByAtteArchiveMonthlyId(id);
}

//根据用户id和月度查询
public ArchiveMonthlyInfo findUserArchiveDetail(String userId, String yearMonth) {
    return archiveMonthlyInfoDao.findUserArchiveDetail(userId,yearMonth);
}
```

画面 5:
```java
package com.ihrm.attendance.dao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

public interface ArchiveMonthlyInfoDao extends CrudRepository<ArchiveMonthlyInfo,String>, JpaRepository<ArchiveMonthlyInfo,String> {

    //根据归档列表查询月度详情
    @Query("select a from ArchiveMonthlyInfo a where a.atteArchiveMonthlyId = :atteArchiveMonthlyId")
    List<ArchiveMonthlyInfo> findByAtteArchiveMonthlyId(String atteArchiveMonthlyId);

}
```

画面 7:
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
atteArchiveMonthlyDao.save(archiveMonthly);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year,String companyId) {
    return atteArchiveMonthlyDao.findByCompanyIdAndArchiveYear(companyId,year);
}

// 查询当月详情列表
public List<ArchiveMonthlyInfo> findMonthlyInfoByMid(String id) {
    return archiveMonthlyInfoDao.findByAtteArchiveMonthlyId(id);
}

//根据用户id和月度查询
public ArchiveMonthlyInfo findUserArchiveDetail(String userId, String yearMonth) {
    return archiveMonthlyInfoDao.findUserArchiveDetail(userId,yearMonth);
}
```

画面 8:
```java
@GetMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findInfosById(@PathVariable String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findMonthlyInfoByMid(id);
    return new Result(ResultCode.SUCCESS,list);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

