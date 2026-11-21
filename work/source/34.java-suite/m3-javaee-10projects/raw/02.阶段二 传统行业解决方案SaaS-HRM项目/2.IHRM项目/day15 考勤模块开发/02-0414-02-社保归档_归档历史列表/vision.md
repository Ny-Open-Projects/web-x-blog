# 画面线理解：02-社保归档：归档历史列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\02-社保归档：归档历史列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:09, 01:18, 02:00, 02:41, 02:57, 03:16, 03:39, 04:25, 05:08, 05:39, 06:02, 06:15, 06:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:28:39

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中实现社保历史归档功能，包括前端页面展示、后端 Java 控制器与服务层代码编写、数据库操作及接口调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 iHRM 系统的社保人员列表页面，筛选条件为部门“test1”，显示员工信息如姓名、工号、入职时间、社保城市、公积金城市、社保基数、公积金金额等。
画面 2：在 Visual Studio Code 中查看 Vue 项目文件结构，当前编辑的是 `list.vue` 文件，其中包含 CSS 样式代码，用于定义 `.cont-bod-box` 和 `.page-list` 等元素的样式。
画面 3：在 IntelliJ IDEA 中打开 `SocialSecurityController.java`，展示 `@RequestMapping` 注解的 `list` 方法，用于分页查询社保人员列表，接收 `page` 和 `pageSize` 参数。
画面 4：在浏览器中打开开发者工具，查看 HTTP 请求详情，请求 URL 为 `http://localhost:8888/api/social_security/history/2019`，状态码为 404 Not Found。
画面 5：在 IntelliJ IDEA 中查看 `SocialSecurityController.java`，展示 `@RequestMapping` 注解的 `historiesDetail` 和 `historiesList` 方法，用于处理历史归档的详情和列表请求。
画面 6：在 IntelliJ IDEA 中查看 `SocialSecurityController.java`，展示 `historiesList` 方法的代码，其中调用 `archiveService.findArchiveByYear(companyId, year)` 方法。
画面 7：在 SQLyog 数据库管理工具中，显示数据库表结构，包括 `archive`、`archive_detail`、`company`、`worker` 等表。
画面 8：在 IntelliJ IDEA 中查看 `ArchiveService.java`，展示 `findArchiveByYear` 方法的代码，其中调用 `archiveDetailDao` 的 `findArchiveByYear` 方法。
画面 9：在 IntelliJ IDEA 中查看 `ArchiveService.java`，展示 `findArchiveByYear` 方法的代码，其中调用 `archiveDetailDao` 的 `findArchiveByYear` 方法。
画面 10：在 IntelliJ IDEA 中查看 `ArchiveDao.java`，展示 `findByCompanyIdAndYearsMonthList` 方法的定义，该方法用于根据公司 ID 和年月查询归档记录。
画面 11：在 IntelliJ IDEA 中查看 `ArchiveDao.java`，展示 `findByCompanyIdAndYearsMonthList` 方法的定义，该方法用于根据公司 ID 和年月查询归档记录。
画面 12：在 IntelliJ IDEA 中查看 `ArchiveDao.java`，展示 `findByCompanyIdAndYearsMonthLike` 方法的定义，该方法用于根据公司 ID 和年月模糊查询归档记录。
画面 13：在 IntelliJ IDEA 中查看 `ArchiveDao.java`，展示 `findByCompanyIdAndYearsMonthLike` 方法的定义，该方法用于根据公司 ID 和年月模糊查询归档记录。
画面 14：在浏览器中打开 iHRM 系统的“历史归档”页面，页面内容为空白，显示加载中或未完成状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```java
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    Integer page = (Integer) map.get("page");
    Integer pageSize = (Integer) map.get("pageSize");
    PageResult pr = userService.findList(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS, pr);
}

@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable String id) {
    Map map = new HashMap();
    Object obj = systemSignInClient.findById(id).getData();
    map.put("user", obj);
    UserSocialSecurity userSocialSecurity = userSocialService.findById(id);
    map.put("userSocialSecurity", userSocialSecurity);
    return new Result(ResultCode.SUCCESS, map);
}
```

画面 5：
```java
@RequestMapping(value = "/historys/{yearMonth}/archive", method = RequestMethod.POST)
public Result historiesDetail(@PathVariable String yearMonth) throws Exception {
    archiveService.archive(yearMonth, companyId);
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/historys/{year}/list", method = RequestMethod.GET)
public Result historiesList(@PathVariable String year) throws Exception {
    archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS);
}
```

画面 6：
```java
public List<Archive> findArchiveByYear(String companyId, String year) {
    archiveDetailDao.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, list);
}
```

画面 8：
```java
if (archive != null) {
    archive.setCompanyId(companyId);
    archive.setYearsMonth(yearMonth);
    archive.setId(worker.nextId());
    archive.setEnterprisePayment(enterMoney);
    archive.setPersonalPayment(personMoney);
    archive.setTotal(enterMoney.add(personMoney));
    archive.save(archive);
    for (ArchiveDetail archiveDetail : archiveDetails) {
        archiveDetail.setId(worker.nextId() + "");
        archiveDetail.setArchiveId(archive.getId());
        archiveDetailDao.save(archiveDetail);
    }
}
```

画面 10：
```java
package com.ihrm.social.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

public interface ArchiveDao extends JpaRepository<Archive, String>, JpaSpecificationExecutor<Archive> {
    List<Archive> findByCompanyIdAndYearsMonthList(String companyId, String yearMonth);
}
```

画面 12：
```java
package com.ihrm.social.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

public interface ArchiveDao extends JpaRepository<Archive, String>, JpaSpecificationExecutor<Archive> {
    List<Archive> findByCompanyIdAndYearsMonthLike(String companyId, String yearMonth);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
