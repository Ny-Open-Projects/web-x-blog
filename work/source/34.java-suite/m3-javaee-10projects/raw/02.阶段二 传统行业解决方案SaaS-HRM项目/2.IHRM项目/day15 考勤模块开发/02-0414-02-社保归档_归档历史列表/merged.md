# 02-社保归档：归档历史列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\02-社保归档：归档历史列表_【海量资源尽在 ubkz.com】.mp4
- 时长 6分53秒（音频 414s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好那么咱们一个一个的把这些功能都给它实现首先做的就是把之前的这个作业给它完成那首先看到第一件事情呢就是这个归档历史的列表那对于这个归档历史的列表呢我们打开网页一起来看一下首先呢这个网页的右上角这边是不是有一个历史归档其实就是查询一下当前这个年度那已经归档了的这些社保的
[00:31] 总的历史记录的一个列表那我们可以打开F12一起简单的来看一下它是发送了什么样的请求那点击历史归档那各位会发现这边请求的其实是一个咱们的社保模块到History中间指的是我们的年份这么一个请求URL没错吧那对于我们来说呢其实就是一个套路
[00:55] 那第一个事情找到Controller编写对应的一个方法调用Service调用do完成操作就可以了那好了回到我们的这个代码部分咱们开始把这个先给它搞定出来好了control c回到我们的这个java代码那找到我们的社保模块那注意了我这边呢就不去写新的Controller了因为这一个Controller里面咱们就能够放下所有的这些代码ok好了这个就是查询
[01:25] 查询历史归档的这个列表OK这个请求的URL呢放到这边好了那接下来配置对应的这么一个Controller好了请求的路径这边就改成year后面改成list因为是2019年所以请求19年如果是18年2000年那这边怎么做对应的修改其实就可以了那当然了我们这边请求方式给大家看
[01:59] 同时也是get请求所以这边改成a get好了我们开始就搞成起一个名字就叫做HitTrayList得了HitTrayListOK那我们这边请求的pass variable一个参数咱们就叫做year即可那接下来咱们这边的方法写好了咱们就可以调用Service得到数据那么调用Service就是我们的归档Service.好了.咱们起一个名字叫做find
[02:31] Find by yearFind by year那传递过来两个参数第一个company id别忘了还有year好那这样一来我们就能够得到一个list的一个集合因为我们查询的其实是一个list集合的列表OK我call一个实体类自己写吧ch OKlist那接着我们可以把这个list封装到伪造当中我们返回那各位应该还记着
[03:08] 我们现在要查询的表呢其实是我们的归档的这个历史总记录表也就是我们的主表那底下是不是有明细表我们现在查的是不是就是这个叫做历史的这个总表也就是我们的主表没错吧OK好那接下来回到代码当中思维层补充一个新的方法好写到下边那在思维层呢我们其实就可以通过do直接进行查询就可以了do点
[03:41] 那接着我想说的是我们通过DU来进行查询那么分析一下我们数据库表里面的数据在我们数据库表里面的数据呢咱们要查询的是当前某一个指定年份它这个月的是不是所有啊所以我们要查询的是这边就应该有六月份比如说有八月份九月份当然这是18年如果19年是不是就有六月份和七月份
[04:06] 没错吧所以我们这边查询根据什么查比较简单的是不是就可以根据这个ears mouse那以lack的方式来进行查询因为别忘了我们传递的参数刚才看过就是一个年份所以通过年份lack来查是不是更加靠谱啊OK那接着回到我们这边代码里那我们就可以叫做find by company id and注意啊别搞错
[04:40] 我这参数虽然叫 year但是我们用的是里面的这个字段叫做 years mouse好了最后加一个like那接下来把这个 company id传递进去那这边呢还有一个 year注意这个 year 呢是 2019我们说了要模糊查询所以我这边加一个百分号各位应该能看懂那接下来呢do 层少方法我们在 do 层当中补充一个方法哎就可以了在这边我写下注释就是根据企业
[05:15] ID和年份查询归档数据当了我们这边是一个模糊查询好那咱们把这个代码呢已经写好了那接下来呢重新启动一下我们这个微服务一起来看看效果来走好了这个启动相对来说有点点慢我这边就暂停一下好了各位在启动过程当中呢这边爆出了一个错误啊我检查了一下各位会发现我这写的应该是一个like才对啊
[05:47] 好了这边是likeearth monthOK好了这边的再来重启一下看一下好了这边的我已经启动成功了各位那接下来呢回到我们的页面部分一起来看一下我们这个历史归档列表是否有数据好了社保点击过来之后点击历史归档
[06:26] 那它自动的会查询2019年那各位会发现这回已经查询出了2019年的历史的报表其实我们这个展示还是有点不太理想为了让它展示的更好一些其实我们可以按照月份给它来一个倒序显示是不是就可以了这样一来最新的月份就在上面让企业看起来更加直观OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中实现社保历史归档功能，包括前端页面展示、后端 Java 控制器与服务层代码编写、数据库操作及接口调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 iHRM 系统的社保人员列表页面，筛选条件为部门“test1”，显示员工信息如姓名、工号、入职时间、社保城市、公积金城市、社保基数、公积金金额等。
画面 2：在 Visual Studio Code 中查看 Vue 项目文件结构，当前编辑的是 `list.Vue` 文件，其中包含 CSS 样式代码，用于定义 `.cont-bod-box` 和 `.page-list` 等元素的样式。
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

