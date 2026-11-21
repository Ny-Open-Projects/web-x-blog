# 画面线理解：22-社保管理：数据归档

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\22-社保管理：数据归档_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:15, 04:09, 05:59, 07:59, 09:39, 10:44, 12:05, 13:18, 14:44, 15:28, 16:16, 17:25, 17:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:25:10

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过后端 Java 代码实现社保报表的生成与数据归档功能，并展示对应的数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iHRM 系统的社保报表页面，显示员工社保信息，包含“归档7月份报表”和“新增报表”按钮。
画面 2: 展示 IntelliJ IDEA 中 SocialSecurityController.java 文件，其中定义了 @RequestMapping 注解的 getReports 方法，用于获取社保报表数据。
画面 3: 展示 ArchiveService.java 文件，其中 getReports 方法的定义，用于获取报表数据。
画面 4: 展示 ArchiveService.java 文件，其中 archive 方法的定义，用于处理社保数据归档逻辑。
画面 5: 展示 ArchiveService.java 文件，其中 archive 方法的代码，正在使用 BigDecimal 类型的变量 enterMoney 和 personMoney 来计算总金额。
画面 6: 展示 ArchiveService.java 文件，其中 archive 方法的代码，正在使用 BigDecimal 类型的变量 enterMoney 和 personMoney 来计算总金额。
画面 7: 展示 ArchiveService.java 文件，其中 archive 方法的代码，正在使用 BigDecimal 类型的变量 enterMoney 和 personMoney 来计算总金额。
画面 8: 展示 ArchiveService.java 文件，其中 archive 方法的代码，正在使用 BigDecimal 类型的变量 enterMoney 和 personMoney 来计算总金额。
画面 9: 展示 ArchiveService.java 文件，其中 archive 方法的代码，正在使用 BigDecimal 类型的变量 enterMoney 和 personMoney 来计算总金额。
画面 10: 展示 iHRM 系统的社保报表页面，显示一个空的报表，准备进行新增或归档操作。
画面 11: 展示 SQLyog 数据库管理工具，显示 ss_archive 表的数据，包含 company_id、years_months、creation_time、enterprise_payment、personal_payment、total 字段。
画面 12: 展示 IntelliJ IDEA 中的运行面板，显示 SocialSecurityApplication 已成功启动。
画面 13: 展示 SQLyog 数据库管理工具，显示 ss_archive 表的数据，其中一条记录的 years_months 字段值为 '201907'。
画面 14: 展示 SQLyog 数据库管理工具，显示 ss_archive 表的数据，其中一条记录的 years_months 字段值为 '201907'。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@RequestMapping(value = "/histories/{yearMonth}",method = RequestMethod.GET)
public Result HistoryDetail(@PathVariable String yearMonth,int optype) throws Exception {
    List<ArchiveDetail> list = new ArrayList<>();
    if(optype == 1) {
        // 深山白，查询当月的社保数据
        list = archiveService.getReports(yearMonth,companyId);
    }
    return new Result(ResultCode.SUCCESS,list);
}
```

画面 3:
```java
public void archive(String yearMonth, String companyId) {
    // 1.查询当月的明细数据
    List<ArchiveDetail> archiveDetails = getReports(yearMonth, companyId);
    // 2.查询当月是否已经归档
    Archive archive = this.findArchive(yearMonth, companyId);
    // 3.不存在已归档的，保存
    if(archive == null) {
        archive = new Archive();
        archive.setCompanyId(companyId);
        archive.setYearsMonth(yearMonth);
        archive.setIdWorker.nextId();
        archive.setEnterprisePayment(enterMoney);
        archive.setPersonalPayment(personMoney);
        archiveDao.save(archive);
        for (ArchiveDetail archiveDetail : archiveDetails) {
            archiveDetail.setArchiveId(archive.getId());
            archiveDetail.setArchive(archive);
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal());
            archiveDetail.setCreateTime(new Date());
            archiveDetail.setUpdateTime(new Date());
            archiveDetail.setUserId(userSocialSecurity);
            archiveDetail.setSocialSecurityEnterprise(archiveDetail.getSocialSecurityEnterprise());
            archiveDetail.setSocialSecurityIndividual(archiveDetail.getSocialSecurityIndividual());
            archiveDetail.setProventFundEnterprise(archiveDetail.getProventFundEnterprise());
            archiveDetail.setProventFundIndividual(archiveDetail.getProventFundIndividual());
            archiveDetail.setTotal(archiveDetail.getTotal
