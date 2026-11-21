# 01-课程介绍与POI导出人事报表：需求说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\01-课程介绍与POI导出人事报表：需求说明_【海量资源尽在 ubkz.com】.mp4
- 时长 13分45秒（音频 825s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 各位朋友 今天是我们这个SaaS系统的第八天那对于今天的内容呢 先跟各位做一个简单的介绍首先第一块呢 就是把昨天遗留的这个PUI报表导出的这块功能先给它实现掉那这个报表导出呢 其实我们就可以从数据库查询出数据然后呢 生成一个Excel报表然后呢 把它下载到我们的电子浏览器或者下载到我们的电脑上那这个补充完成了之后 接下来就是说呢 在我们
[00:30] 去生成这个报表的过程当中可能它的样式处理是一个比较麻烦的事情那这边跟各位介绍一个更加优良的POI报表的导出的这么一种方式我们叫做模板打印那这些呢基本上我们已经涵盖了POI报表导出和导入的这两部分操作那我们写代码写了很多各位会发现还是不太方便所以接下来呢第二块内容就是跟各位要聊一个我们可以通过自定义注解自定义工具类的形式让我们操作
[00:58] PY更加简单一些那也就是自定义一些工具类那接着第三块第四块第五块内容都是围绕到大数据量的数据报表上面的一些操作比如说呢大数据量咱们都知道2007版本可以支持上百万条数据那这么多数据你去导出一下或者你去导入一下你去试一下很普遍的现象叫做内存溢出所以我们如果操作百万数据的话
[01:23] 也有我们自己的方式那我们最后一块关注的就是百万数据PUI报表如何进行操作OK好了那我们先来看第一个就是去补充一下我们昨天的这个PUI报表导出的这块内容那针对这个PUI报表导出呢首先需要跟各位说一下我们要完成的这个操作那在这边呢我们打开我们这个项目那在这边呢员工管理还是之前一样员工管理
[01:50] 找到员工管理这边呢各位会发现有一个叫做几月份某某月报表那么可以点击过来当然了我这个某月份报表这个现在呢有一点点小小的疑问这个呢瑕不掩瑜那其实是根据我当前登录的月份它应该给我自动的计算出来才对好了比如说呢现在是一月份好了我也点进去来这个其实就是我一月份的人事报表那这个一月份的人事报表里面我们之前做课程介绍的时候说过
[02:16] 人事报表重点统计的是当前这个月你入职了多少人员以及这个有多少人员离职也就是说在这个人事报表里面我要有很多的数据那这个数据里面它就会填写上用户姓名用户性别等等等等很多的内容那当然了里面还有几个就是离职相关的一些声明一些说明那对于我们来说对我们来说那如果说
[02:45] 你是一个新入职的那这个离职类型和离职原因是不是就不用填写那如果说你不是入职的你是一个离职的那我想问各位那离职的时候前面这些用户姓名或者他的手机号或者他的出生日期是不是也应该包含进来啊那所以对于我们这个人事报表来说里面总共的内容第一个用户的详细信息因为他上面什么最高学历就涉及到是一个详细信息那第二个就是如果你离职了是不是就是离职人员的内容
[03:14] 和离职人员的详细信息啊那这个呢我们数据说了一个说了一下那接下来呢这边有一个叫做导出的这么一个功能我点击导出也就是以Excel的形式把一月份我们的人事报表数据导出出来这个就是我们的需求那针对我们这个人事报表导出的这个需求我们应该如何去实现它呢那对于我们来说
[03:43] 最重要的其实就这么两个部分一个部分就是想方设法的搞出数据来也就是说你先能把这个数据给我查出来没数据你导出的报表那就是空对不对所以对于我们来说要完成这个工程首先构造报表所需要的数据那数据已经有了之后接下来就想方设法的是不是创建根据POA创建Excel根据POA创建Excel的步骤有工作簿有sheet
[04:12] 有行对象有单元各对象如果有样式填充样式是不是就可以了好了这是我们Excel报表相关内容那接下来别忘了我们要做的事情是不是还有一个下载所以对于我们人事报表的导出来说大的方向一共就这么几步有数据有报表能下载OK好了这个是对我们PY报表这个需求做了一个说明
[04:37] 以及我们这个PUI报表如果想要去实现它我们的这个操作步骤也说了一下那好了接下来呢我们就开始去写代码实现相应的这个功能好了要发送一个请求那我们这个呢其实是我们员工这个微服务当中的一个范畴所以呢我在员工微服务内中你可以发送请求请求到我的Controller当中好了我就写到下边当月
[05:16] 人事报表导出好了接下来代码应该如何去写其实很简单首先我这边来一个我们请求的路径好了接下来public result好了我就叫做export了好了对于你给我发送请求的时候这边有一个参数就是你这个月份其实说的直白一点这个参数不是一个月份它指的是年月
[05:53] 也就是说你一会给我发送的格式我们是有要求的比如说就是2018-02那这个就是你要查询02月的好了所以这边我就可以接收到的参数at pass variable好了死菌类型的monthOK那接下来我想跟各位说的是对于我们这个人事报表它是要提供下载功能那提供下载功能我就不需要返回值直接vyd以流的形式我们进行下载是不是就可以了
[06:28] 那接下来呢就是对于我这个方法来说我们要去填充这个方法的内容重点关注的就是这么三个逻辑首先第一个逻辑就是获取报表所依赖的数据好了接着第二件事我们就是构造Excel好了接着第三件事就是完成下载那好了接下来我们就针对这三件事一个一个的来去完成它首先第一个就是报表数据那刚才这个报表数据呢已经说的比较清楚了那这个报表数据
[07:03] 首先必须要有当月你入职的人员的基础信息或者他的详细信息这就是详细信息那详细信息有了是不是还应该如果当月有人离职是不是还应该有这个人离职相应的这些内容也就是他你什么时候离职的你的离职原因是什么是不是也有把这个人的信息给我打印出来那接下来我们关注的就是这些信息从哪查询
[07:28] 那从哪查询呢还记着我们今天课程一上来的时候跟各位做过一个说明只要涉及到用户详细信息有一个表叫做Postal那还有一个就是我们的员工离职的这么一个申请表那这个员工离职申请表里面刚才说过了有状态以及有他的离职时间所以对于我们而言我们要查的表呢有Postal他的全部信息那还有我们这个离职的这张表
[07:57] 好了这边呢我们打开数据库简单的来看一下首先呢看这个Personal这里面呢有很多的数据那这个Personal指的是它的详细信息的这张表这张表里面有它的ID有它的用户名有它的手机号有它的一个入职时间注意这个是入职时间OK那好了接下来呢还有一张表呢就是我们的离职表这个离职表里面离职表这个离职表里面呢就有它离职的
[08:29] 为什么离职当然是主动离职好了这边还有离职相应的一些配置那对于我们而言对于我们而言我们要查询的时候是不是直接查Personal表根据我们这边的入职时间来查是不是就可以所以对于我们来说Selecting fromEM下发线user下发线company下发线Personal那接着我们可以进行一个判断Where
[09:01] 那注意呢我们刚才说过了你给我传递的参数呢是不是就是一个2018-02的这么一个形式那在我的这边的入职的这个字段里面是不是2018-03那对于我们来说呢是不是可以做一个简单的like模糊匹配就可以了where好了time小线of小线entylike比如说呢就叫03那好了我查询一把抱歉后面应该有一百分号百分号
[09:34] OK那这样一来就查询出我们三月份的是不是离职的这些人员那三月份离职人员我们已经查询出来了那接下来就是说那还有可能啊那这个是用户的详细信息的表那还有可能你某一个月有人离职了那离职的时候那有的朋友说我只去查离职表行不行slag星fromem下滑线i e s i s i n a t o n这个表
[10:08] 那对于这个离职表REEM下划线RE这个表好了那对于这个表呢里面的数据好了有一条是二月份的这个WHERE注意这里面有个时间就是离职时间TIME同样的也可以用LACK来模糊匹配抱歉上面这个X02吧那X02有这么一条数据好了接下来这边X02有这么一条数据那接下来我想说的是
[10:45] 你直接查离职的时候那我们需求说的很明确我除了有离职他的原因还有离职他的类型之外是不是还应该有他的用户的详细信息那我们应该怎么去做呢那注意用户详细信息里面包含了用户每一个用户的所有内容那对于我们而言是不是这两个表关联起来查是不是就可以了所以对于我们而言如何去把他们关联到一起这个就讲究了注意注意
[11:15] 那我们要用的方式是什么是什么右边左边我们用的是详细信息当月的那右边是不是就应该是他的离职信息那这边我们要查询就可以用左外连接的方式来做好了那怎么去实现呢这个其实就比较简单了slag星form这张表好了接着这张表给他起一个名字A left叫做join好了连接向底下这张表OK那接下来呢后面可以给他添加我们
[11:51] 左半点的条件啊好了我们的关联关系就是A点叫做user下话线ID等于我们第二个表给它起一个名字B点userID即可当然了对于这里面呢还有很多的判断条件比如说呢比如说我们这边呢要根据注意我们这边要查询的是要查询一下你入职是二月份还要查
[12:24] 是不是你离职也应该是二月份的所以这边呢我的查询条件不仅要满足你入职二月份还应该要满足或者要满足你离职是二月份所以对于我们这边来说要加一个all的一个判断更加合适所以我这边这个是入职表A点那我这边all一下就是B点OK拿过来那接着我们把它关联起来
[12:55] 那各位来看那这样一来我们就已经看到了就已经看到了这边现在变成了叫做五条数据那这五条数据呢各位可以看一下它的入职时间那其中呢有这么几条A102这A02那全部都是我们叫做2月1号或者2月份入职的其中有一个11月份入职的那这个11月份入职的显然不满足我们需求但是各位来看就是他呢在11月他入职但是这个人是不是
[13:28] 在2月份它离职了这样一来我们的数据构造咱们的Circle就已经写好了一会我们就可以根据Circle去编写我们的DL层接着通过Service通过我们的Controller构造出我们的数据OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何使用POI技术实现人事报表的导出功能，包括需求分析、代码实现和数据库查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT页面，标题为“5 POI报表导出”，子标题“5.1 需求分析”，内容为“完成当月人事报表的导出：包含当月入职员工信息，离职员工信息”，并展示一个“导出”按钮。
画面2：展示人事报表导出的前端界面，标题为“03月人事报表”，包含“导出”按钮。
画面3：展示PPT页面，标题为“5.1 需求分析”，内容与画面1相同。
画面4：展示PPT页面，标题为“5.2 人事报表导出”，子标题“5.2.1 步骤分析”，列出步骤：“构造Excel表格数据”、“创建工作簿”、“创建sheet”、“创建行对象”、“创建单元格对象”、“填充数据，设置样式”。
画面5：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_common_model/src/main/java/com/hrm/common/domain/response/ProfileResult.java`，代码内容为：
```java
@poran
public ProfileResult(User user, List<Permission> list) {
    this.mobile = user.getMobile();
    this.company = user.getCompanyName();
    this.companyId = user.getCompanyId();
    this.userId = user.getId();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    for (Permission perm : list) {
        if (perm.getType() == 1) {
            menus.add(code);
        } else if (perm.getType() == 2) {
            points.add(code);
        } else {
            apis.add(code);
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}
```
画面6：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/Controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/{id}/positive", method = RequestMethod.GET)
public Employee findPositive(@PathVariable(name = "id") String uid) throws Exception {
    EmployeePositive positive = positiveService.findById(uid);
    if (positive == null) {
        return new Result(ResultCode.SUCCESS, positive);
    }
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer type) throws Exception {
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.PUT)
public Result saveArchives(@PathVariable(name = "month") String month) throws Exception {
    return new Result(ResultCode.SUCCESS);
}
```
画面7：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/Controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer page, @RequestParam(name = "page") Integer page) throws Exception {
    Map<String, Object> map = new HashMap<>();
    map.put("year", year);
    map.put("companyId", companyId);
    map.put("company", company);
    map.put("month", month);
    PageResult<EmployeeArchive> pr = new PageResult<EmployeeArchive>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```
画面8：展示IntelliJ IDEA中的代码，文件路径为`/hrm_parent/hrm_employee/src/main/java/hrm/employee/Controller/EmployeeController.java`，代码内容为：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    //2.将数据写入Excel
    //3.完成下载
}
```
画面9：展示课程PPT页面，标题为“第7章 POI报表的入门”，子标题“1 员工管理”，内容为“1.1 需求分析”和“1.2 数据库表概述”。
画面10：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据。
画面11：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，但未显示具体数据。
画面12：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。
画面13：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。
画面14：展示SQLyog数据库管理工具，显示`hrm_parent`数据库中的`em_user_company_personal`表数据，其中`time_of_entry`字段值为“2018-03-01”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面5：
```java
@poran
public ProfileResult(User user, List<Permission> list) {
    this.mobile = user.getMobile();
    this.company = user.getCompanyName();
    this.companyId = user.getCompanyId();
    this.userId = user.getId();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    for (Permission perm : list) {
        if (perm.getType() == 1) {
            menus.add(code);
        } else if (perm.getType() == 2) {
            points.add(code);
        } else {
            apis.add(code);
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}
```
画面6：
```java
@RequestMapping(value = "/{id}/positive", method = RequestMethod.GET)
public Employee findPositive(@PathVariable(name = "id") String uid) throws Exception {
    EmployeePositive positive = positiveService.findById(uid);
    if (positive == null) {
        return new Result(ResultCode.SUCCESS, positive);
    }
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer type) throws Exception {
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/archives/{month}", method = RequestMethod.PUT)
public Result saveArchives(@PathVariable(name = "month") String month) throws Exception {
    return new Result(ResultCode.SUCCESS);
}
```
画面7：
```java
@RequestMapping(value = "/archives/{month}", method = RequestMethod.GET)
public Result archives(@PathVariable(name = "month") String month, @RequestParam(name = "type") Integer page, @RequestParam(name = "page") Integer page) throws Exception {
    Map<String, Object> map = new HashMap<>();
    map.put("year", year);
    map.put("companyId", companyId);
    map.put("company", company);
    map.put("month", month);
    PageResult<EmployeeArchive> pr = new PageResult<EmployeeArchive>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```
画面8：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    //2.将数据写入Excel
    //3.完成下载
}
```
画面10：
```sql
SELECT * FROM em_user_company_personal
```
画面12：
```sql
SELECT * FROM em_user_company_personal WHERE resignation_time LIKE '2018-03%'
```
画面14：
```sql
SELECT * FROM em_user_company_personal WHERE resignation_time LIKE '2018-03%'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5 POI报表导出”，子标题“5.1 需求分析”，内容为“完成当月人事报表的导出：包含当月入职员工信息，离职员工信息”。
画面3：PPT标题为“5.1 需求分析”，内容与画面1相同。
画面4：PPT标题为“5.2 人事报表导出”，子标题“5.2.1 步骤分析”，列出步骤：“构造Excel表格数据”、“创建工作簿”、“创建sheet”、“创建行对象”、“创建单元格对象”、“填充数据，设置样式”。
画面9：PPT标题为“第7章 POI报表的入门”，子标题“1 员工管理”，内容为“1.1 需求分析”和“1.2 数据库表概述”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）

