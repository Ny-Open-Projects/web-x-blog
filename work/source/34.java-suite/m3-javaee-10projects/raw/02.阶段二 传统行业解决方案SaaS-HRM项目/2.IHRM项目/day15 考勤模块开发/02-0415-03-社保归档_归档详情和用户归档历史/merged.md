# 03-社保归档：归档详情和用户归档历史

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\03-社保归档：归档详情和用户归档历史_【海量资源尽在 ubkz.com】.mp4
- 时长 11分34秒（音频 695s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们现在已经把这个列表呢展示出来了那接下来呢我们就继续往下看了那除了这个列表之外我们这边可以点击得到我们当前六月份归档的这个明细数据那得到这个明细数据呢其实很简单那点击过来之后各位发现其实这个功能已经准备好了或者已经写好那这个功能在什么位置呢其实是在我们昨天这个代码的部分咱们已经做过了
[00:32] 那我们昨天呢这边说过一个就是查询月份的这个数据报表如果是一查询当业数据咱们要接入工具类获取那如果呢不是一是不是就是从这个明细表里面把相应的明细给它查询出来所以这个方法呢不需要我们再去额外的编写已经准备好了OK那咱们把这个功能呢咱们已经实现出来了那接下来呢其实是这样的在我们这个系统当中啊
[01:01] 页面所需要的这些接口呢我们就已经准备好了但是为了我们最后能够计算薪资那其实还需要提供一个接口来做是这样的好了我这边简单的来画一下那注意各位我们接下来呢要完成的这块功能呢其中有一个叫做薪资的这么一个模块好了我这边调一下字体没问题薪资管理的这么一个模块那除了薪资管理我们现在已经完成了
[01:33] 有社保管理那除了社保管理我们接下来即将要做到的好了这边呢是我们的考勤管理那接下来呢在制作薪资的时候就是制作薪资个人薪资那制作个人薪资的时候我们要统计出他的总的薪资那以及当月社保扣款
[02:16] 当月好了公积金扣款扣款那除了这个之外呢注意除了这个之外我们还有考勤那考勤因为你做薪资的时候也要看一下你考勤是否达标看一下你的这个考勤的一些记录没错吧那这些数据从什么地方得到那薪资里面显然没有因为它是独立的一个模块那从哪得到咱们只能是通过薪资管理来进行查询
[02:48] 查询社保模块那查询考勤模块分别得到对应的社保的扣款考勤的记录等等所以我们就需要在社保管理这边向薪资管理提供一个接口那提供一个接口就是查根据用户ID和这个考勤的年月查询他这个社保记录
[03:23] 比如说你要制作张三的具体薪资你要看一下张三你知道是哪个月吧那看一下他究竟社保是怎么记录的那还有考勤当然考勤我们做到的时候再说所以我想说我们现在社保管理当中还少一个功能主要是为了给薪资计算提供数据支持那接下来呢就是说一下那我们薪资管理
[03:50] 你要去计算这个薪资要有社保要有考勤的这些数据那这个社保数据和考勤数据必须已经归档因为只有归档了才认为你这个数据是最终要落实到我们的实处的所以这边呢我想说你查询我们的社保管理的时候我们要查询的表各位应该就知道了其实我们要查到就是要去查询一下我们这边考勤
[04:21] 考勤归档的这个明细表里面会有当前这个员工在某个年份他的一个我们的社保记录没错吧所以接下来呢我们要把这个工作呢给他完成出来那回到我们的idea当中好了接下来呢我就继续往下写找到Controller我们这边要写的就是根据用户ID和考勤的年月
[04:53] 查询用户考勤归档明细OK好那接下来呢这边呢我简单说一下那请求的在这边Ctrl C Ctrl V 拷过来哎我直接拷过一大段好那接下来呢这边呢可以给他一个我们的请求地址啊就叫做History来一个Data吧那我们的请求方式呢就用Get这回就是HistoryAData
[05:29] 那么这边的请求的参数究竟有什么呢其实这个参数不多啊一个是死菌类型的user id好了一个是死菌类型的死菌类型的我们叫做aarmonthmonth这个应该各位都能理解好了那这个我们看过了之后方法定义好了那接下来呢我们请就开始调用Service进行查询我们可以通过Service点
[06:00] Find就是FindBy就是FindUserDetail好了查询用户的归档名系那这边呢需要的参数一个是我们的UserID另一个就是我们的演绎好了那这样一来呢最终能够得到一个对象那这个对象呢我们要用Result的话其实就不太方便了当然用Result也可以也可以
[06:32] 因为这个result主要是为了我们前后端分离的这种开发方式更加统一但是我们现在是用的要从微服务进行请求了所以我这边直接给他改一下就是直接得到我们的归档明细就可以了改成一对象好了我这边直接return好那接下来survey层里面少方法我们得到的是归档明细
[07:01] 对象所以接下来呢在这边咱们在思维层补充一个新的方法就是根据用户ID和年月查询用户归档名系那当然了这边呢咱们就开始要去调用DU return好了我们的DU呢是名系DU啊detailDU点那注意我们这个DU应该怎么进行查询
[07:29] 好了这个是需要跟各位要做交代的那各位可以一起来看一下我们的数据库表找到数据库表找到这个归档明细这个表那这里面的数据呢实在是太多了但是各位我们能够提取出有用的比如说U的ID那我们查询是不是要查询这个U根据U的ID要查这是一个条件那除了这个条件之外注意在最下边我也加了一个条件这个是不是就是我们的考勤的记录年月
[07:55] 那么可以看一下表的数据比如说我要查询哎68的要查询他几月份呢比如说6月份的哎这些是不是就已经都对上了所以我们直接根据他的名称查询直接编写do即可好了回到我们这边来看一下就是find by我们可以要根据user id来查user id and
[08:22] 注意了各位这个AND不能瞎写了因为我之前就写错过直接从属性call吧year month好了接着把这个user id传递过去年月传递过去do层添加一个方法好了do层写断注释OK那这样一来咱们这个为咱们考其模块准备的这个数据接口就已经写好了那好了我们重新启动一下
[09:00] 那需要各位注意的是我这个重新启动呢因为我这边打开的工程比较多打开了六七个工程同时这边还有前端的工程以及Redis等等所以可能有点慢所以我这边呢就先去暂停一下那等它启动成功了我们继续好了这边呢我这个微服务已经重新启动成功了那接下来呢我们就可以一起来做个测试了注意啊这个接口呢我们
[09:28] 页面上没有对应的请求所以我们就只能用postman自己来测试一下看效果好了这边我打开postmanOK那打开了之后咱们可以一起来测试一下注意我们这边测试我就不去测试网关了因为在网关层我们做了全线的相关的校验所以我直接去测试我们写好的新的微服务接口就可以了而我们请求的是127.0.0.1
[10:00] 冒号我们叫做9004好了那接下来呢请求的路径就是我这边拼接一下拿下来我拼接一下OK那接着后面要拼上user id等于某某好了接着再加一个参数因为是get请求等于某某比如说我要查201906好了看一下数据库啊有没有这个记录啊有06那这个user id呢我就用上面这一个好了没问题
[10:44] Ctrl C贴到postman来我们发送一个请求看一下有没有数据走好了各位发现这边的其实已经查询出相应的数据内容了那这样一来说明我们当前这个接口是没有问题啊OK好了那到目前为止呢其实就是咱已经把第一个小节
[11:09] 昨天留的相关作业还有我们为之后数据做准备的这些接口呢咱们就已经写好了其实对于这几个接口呢不太难咱们就是回顾一下传统的这些增删改查的一些写法就可以了其实套路都是一样的Dio ServiceControllerServiceDio当然了我们现在呢是通过页面发起请求的形式来进行测试的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何实现员工社保归档历史数据的前后端功能，包括前端展示、数据库设计、后端接口开发与测试。

2) 按时间顺序列出每张画面的要点：
画面1：前端展示2019年社保归档数据，包含企业缴纳、个人缴纳、合计金额及员工列表。
画面2：前端展示2019年社保归档数据，点击“社保报表”后切换至2019年数据。
画面3：PPT页面，展示“薪资管理”、“社保管理”、“考勤管理”三个模块。
画面4：SQLyog中查看`archive`表结构，包含`archive_id`, `user_id`, `username`, `time_of_entry`, `mobile`, `id_number`, `the_highest_degree`等字段。
画面5：IntelliJ IDEA中展示`SocialSecurityController`类，包含`historysDetail`和`historysList`两个接口。
画面6：IntelliJ IDEA中展示`SocialSecurityController`类，新增`historysData`接口，用于根据用户ID和年月查询归档明细。
画面7：SQLyog中查看`archive`表数据，包含员工ID、用户名、入职时间、手机号、身份证号等信息。
画面8：SQLyog中查看`archive`表数据，包含员工ID、学历、开户行、银行卡号、一级部门、二级部门等信息。
画面9：IntelliJ IDEA中展示`ArchiveDetailDao`接口，定义了`findByUserIdAndYearsMonth`方法。
画面10：IntelliJ IDEA中展示项目结构，包含`ihm_parent`、`ihm_common`、`ihm_company`等模块。
画面11：IntelliJ IDEA中展示`SocialSecurityController`类，`historysData`接口已编写完成。
画面12：Postman界面，准备发送GET请求，用于测试后端接口。
画面13：SQLyog中查看`archive`表数据，包含员工ID、用户名、入职时间、手机号、身份证号等信息。
画面14：PDF文档，展示“1.1 归档历史列表”和“1.2 归档详情”两个章节，包含Controller和Service层的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面4 SQL：
```sql
CREATE TABLE `archive` (
  `archive_id` varchar(32) NOT NULL,
  `user_id` varchar(32) NOT NULL,
  `username` varchar(32) NOT NULL,
  `time_of_entry` datetime NOT NULL,
  `mobile` varchar(32) NOT NULL,
  `id_number` varchar(32) NOT NULL,
  `the_highest_degree` varchar(32) NOT NULL,
  `opening_bank` varchar(32) NOT NULL,
  `bank_card_number` varchar(32) NOT NULL,
  `first_level_department` varchar(32) NOT NULL,
  `second_level_department` varchar(32) NOT NULL,
  PRIMARY KEY (`archive_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面5 Java代码：
```java
@RequestMapping(value = "/histories/{yearMonth}/archive", method = RequestMethod.POST)
public Result historysDetail(@PathVariable String yearMonth) throws Exception {
    return new Result(ResultCode.SUCCESS);
}

//查询历史归档列表
@RequestMapping(value = "/histories/{year}/list", method = RequestMethod.GET)
public Result historysList(@PathVariable String year) throws Exception {
    List<Archive> list = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, list);
}

//根据用户id和年月查询用户考勤归档明细
@RequestMapping(value = "/histories/data", method = RequestMethod.GET)
public ArchiveDetail historysData(String userId, String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面6 Java代码：
```java
@RequestMapping(value = "/histories/data", method = RequestMethod.GET)
public ArchiveDetail historysData(String userId, String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面9 Java代码：
```java
package com.ihm.social.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.stereotype.Repository;

public interface ArchiveDetailDao extends JpaRepository<ArchiveDetail, String>, JpaSpecificationExecutor<ArchiveDetail> {
    void deleteByArchiveId(String archiveId);
    List<ArchiveDetail> findByUserIdAndYearsMonth(String userId, String yearMonth);
}
```

画面14 Java代码：
```java
//查询历史归档列表
@RequestMapping(value = "/histories/{year}/list", method = RequestMethod.GET)
public Result historysList(@PathVariable String year) throws Exception {
    List<Archive> archiveList = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, archiveList);
}

//根据用户id和年月查询用户考勤归档明细
@RequestMapping(value = "/histories/data", method = RequestMethod.GET)
public ArchiveDetail historysData(String userId, String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

4) PPT标题、架构图/流程图的结构、表格数据：
画面3：PPT页面，标题为“薪资管理”、“社保管理”、“考勤管理”三个模块，无具体流程图或表格数据。

5) 无其他内容。

