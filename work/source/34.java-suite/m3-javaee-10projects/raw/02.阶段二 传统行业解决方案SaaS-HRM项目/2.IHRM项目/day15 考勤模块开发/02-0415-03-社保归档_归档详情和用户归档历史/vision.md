# 画面线理解：03-社保归档：归档详情和用户归档历史

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\03-社保归档：归档详情和用户归档历史_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 01:00, 01:58, 04:20, 05:12, 06:52, 07:35, 08:01, 08:41, 09:10, 09:35, 09:56, 10:32, 11:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:29:19

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
画面14：PDF文档，展示“1.1 归档历史列表”和“1.2 归档详情”两个章节，包含controller和service层的代码。

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
