# 16-考勤归档：查看月报表数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\16-考勤归档：查看月报表数据_【海量资源尽在 666java.com】.mp4
- 时长 14分17秒（音频 857s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在呢已经完成了考勤的绝大部分功能当然了接下来我们要完成最后一部分就是这个考勤规档相关的那对于这个考勤规档呢首先呢就是说那我在数据库这边可以设置一下比如说呢我们现在要查看一下8月份的记录或者查看一下7月份的记录点击那过来之后重新发现你发现现在我们关注的就是7月份相关的这个考勤的相关内容了
[00:33] 好了那接下来当前这个月份的考金如果没有问题的话我们就可以统计一下7月份这个报表的一个数据没错吧好了那接下来呢咱们就来看一下如何把这个归档的这个报表数据呢给它获取出来那首先是这样的我们一点击打开F12一点击过来之后呢会发送一个对应的请求那这个请求发送过来来看就是reports
[01:03] 那请求过来了一个我们的日期就是当前的这个月份那接下来回到我们的Controller当中把这个代码呢给它补充完整好了这个就是获取我们的月报表的归档归档数据okcontrol ccontrol v这边呢我们拿过来一份好了那接着请求的路径就叫做reports没错吧
[01:37] 好了那他请求的参数有这么一个参数死君类型OK那这个方法名呢我也叫做Reports了那请求的方式叫做Get没什么问题OK好了那接下来那接下来我们来看一下就是目前而言他能够需要我们给他封装的数据究竟是什么样子OK需要各位注意啊你请求过来的时候这个考前统计这些数据我归档了吗注意还未归档
[02:11] 未归档也就意味着这些数据呢是我们需要自己的把它查出来啊当然了如果已归档就不需要了嘛没错了所以我们查询的是未归档的这些明细数据那不管是已归档还是未归档其实跟之前的套路都差不多我们其实查询的就是这边归档表这个明细的相关的数据其实就可以了所以在我们这边你查询过来之后得到的其实就是我们归档的这么一个明细对象的粒子集合
[02:40] 我们找到这个对象就是这个对象咱们得到它的一个list集合是不是就可以了所以这边我们来看一下list类型的对象拿过来等于好了找到我们这边归档Service归档Service我们写了吗找到Service归档Service注入进来了那我们就可以归档Service点
[03:22] 诶, 规档Service.getreport, e-p-o-r-t, getreports,那接着把这个日期给它传下去就可以了,当然除了日期还有我们,诶,别忘了就是一个company id,好了,那接下来呢,把这个list,诶,拿过来即可,这个应该各位都能接受,那接下来呢,就是我们Service补充相应的我们的方法,查询我们的规档数据,
[03:50] 那咱们现在要去查询对应的这个归档的相应的这些数据那我们想说我们这个Service应该怎么去进行处理才对呢还是那句话因为我们这回查询的数据实在是太多了所以我们用户呢就是用user deal了user deal那其实我们要去查询归档数据要查询每一个用户所有的这一个月他的一个上下班的这么一个情况比如说里面有试驾
[04:19] 调修正常的迟到次数早退次数等等等等等等这些那针对这些内容前面部分其实就是我们用户的内容那后面一部分其实就是考勤上做统计的一些内容没错吧所以呢在我们这边咱要进行操作呢首先第一件事好了就是查询所有咱们的企业用户那企业用户全部都查询好了之后接着呢第二件事我们要做的事情就是根据每个循环
[04:49] 便利我们的用户列表那循环便利我们的用户列表那接下来呢就是查询每然后呢统计每个用户用户登月的哎我们的考勤哎记录其实就是这么一个逻辑那我们来看一下首先呢查询所有企业用户这个比较简单user deal咱们写过了方法
[05:17] 就是Findbar Company ID查询这个企业里面的所有用户就是私那接着呢我们这边开始循环编例ITR 报循环 循环编例那拿到其中的每一个用户那拿到其中的每一个用户那接下来我们要做什么这个是需要各位要注意的我们的一个用户呢就需要去构造出这么一个归档的明细对象没错吧所以我们
[05:48] 先把这个list结合呢给它构造出来等于new一个arrayarraylist先把这个list结合呢给它构造出来arraylist那好了接下来我们就开始一个用户对应一个明细info等于new一个明细因为我们刚才看过了明细是不是也需要用户组的属性啊所以我们这边info.set就是user.get一个一个往里设置当然了我已经写好了一个构造方法它会自动的把值复制进去
[06:19] 好了那为了我们不报错我先把这个list点add把这个info呢先传递进去那最后呢这个主要是我这个人个人记忆不太好啊总是丢三拉四OK好了那接着中间我们要做的事情其实就比较明确了这是我们最关键的就是统计每个用户的叫做考勤
[06:49] 那统计每个用户的考勤记录这个统计考勤记录那从哪统计是不是就要去统计一下当前他打卡的这个考勤记录在这里面开始做查询没错吧那在里面做查询那我们这边应该怎么进行查询要查什么各位来看我们要查的他究竟请了多少天试驾请了多少天调休有多少天是正常的有多少天迟到的有多少天早退有多少天他的一个旷工的天数
[07:18] 是不是全勤实际出勤等等等等等等有很多内容那所以在我们这边就设立到一个查询那这个查询由于查询的比较多那我们用什么方式来做很简单咱们要统计一个用户的天数我们就可以select count from att一下滑线att in
[07:52] 没错了但是我这一统计统计的是所有的人没错了好了那接下来呢咱们除了要统计所有人之外可能还要统计其他的一些东西比如说呢这边我们还有不同的人员比如说呢我们要统计的是每一个用户所以我们这边要加一个条件whereuser下网线IDID比如说呢我们要统计一下统计一下这个这个这个这个用户吧OK拿过来
[08:26] 那一共有三条这个没什么问题但是我想说啊咱们这边日期啊有可能这个人啊是七月份的统计有可能是八月份的没错吧所以我们这边还应该有条件就是有一个叫做按StateLike比如说我们模糊查询201907那这样一来是不是统计的全部都是七月份的这些报表数据啊这个不对吗201907后面加个百分号
[09:06] ok没错了好了但是我们现在只统计的是一个count那其实在我们这统计的时候啊可以加很多的其他的统计比如说呢我要统计一下统计一下呢这里面的根据状态如果状态呢等于1代表是正常的如果状态等于4代表的是异常的没错了那这边我们可以用一个circle的一个小小处理方式case1好了case1 adt小花线sta
[09:39] t t u如果这玩意等于1我们给他加1如果是1我们就加1如果不是1 9-0懂意思吗好了那接着我们来看一下他有1的是不是有两条啊1的有两条我们来试一下总记录三条状态为1的有两条来走哎这边加一逗号kiss伺候语句什么地方写错了send count 新kiss问 adtsta
[10:23] tu等于1,n1,n好了,接着fromcase1哦,抱歉,这边应该是问,case1,这么一个条件的一个函数OK,好了,我们再来试一下好了,各位发现总数有三条,但是状态唯一的是不同,两条啊那我们说了状态唯一的啥意思状态唯一的是不是就有两天是正常那如果你想统计矿工的个数我们是不是就可以再来一条诶,再来一条
[11:02] 二如果你想统计其他的比如说想统计加班的天数那是不是就可以再来一条统计如果想统计旷工的如果统计其他的是不是就来相应的这些是不是就可以了OK那其实这个Circle宇宙的思路已经跟各位写好了那如果你想统计其他的就是一个一个的Count进行去获取就可以了那对于这个完整的Circle在今天的资料当中也给各位准备好了就在这儿
[11:32] Ctrl C拿过来回到我们这个笔记里回到我们这边好了这个其实就是我们今天的一个思维句OK好了切过来贴到我们这边咱们来看要统计每个它的考勤数量我们可以通过咱们的统计DU点好了这个其实可以随便起一个名字都行啊STATIS by user
[12:07] 好了我们可以传递过去两个参数一个就是user.get id第二个就是我们当前查询的日期好了千万别忘了咱们是模糊查询后面要加一个百分号搜索语句刚才说过了好了这边少一个返回值返回值是一个map集合好了同样的我们这边用一个ata querynet circle等于 true代表的是我们用circle语句来查好了接下来这边的valuevalue等于那接着把我们准备好的circle语句给它拷过来
[12:46] 这边的-n是看着不太舒适啊OK好了呢注意这边呢有几个需要各位注意的点第一个点呢我们这边要改一下改成1第二个点呢这边我们也要改一下改成2那这样一来我们这个搜索语句就已经准备好了那各位会发现如果状态0的我们叫AT0如果1叫AT1AT2AT3AT4没错吧
[13:16] 好了那这样一来呢我们这个map集合该有的数据都已经有了那接下来你这个统计需要什么我们就从map集合里面获取即可那这边呢我也在里面写了一个方法点set static dates它会从map里面一个一个拿并且得到数据就这么一个含义好了这样一来呢我们对应的这个数据规档咱们也写好了重新启动一下我们这边的
[13:47] 微服务一起来静待它的效果好了这边呢我们的微服务已经启动成功了回到我们的页面刷新一把一起来看一下这个月份的数据呢是否已经有了好了注意我们现在是7月份的贵档数据那7月份呢我们刚才有一个人叫A01好了两天正常一天早退没错了当然了这边还有一些其他的细节问题留给我们去处理这个之后慢慢再处理其实就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 后端代码实现并查询员工考勤月报数据，涉及数据库查询、实体类定义、服务层逻辑和前端页面展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 2: 前端页面显示员工考勤列表，用户可按部门、状态筛选，当前筛选条件为“test1”。
画面 3: 浏览器开发者工具显示前端请求后端 API `/attendances/reports?atteDate=201907` 的响应，状态码为 200 OK。
画面 4: IDE 中展示 `ArchiveMonthlyInfo` 实体类定义，包含 `id`, `userId`, `name`, `workNumber` 等字段。
画面 5: IDE 中展示 `AttendanceController` 控制器类，包含 `getReports` 方法用于获取月报数据。
画面 6: IDE 中展示 `AtteService.java` 文件，包含 `editAtte` 方法用于编辑考勤记录。
画面 7: IDE 中展示 `AtteService.java` 文件，`getReports` 方法中遍历用户列表并创建 `ArchiveMonthlyInfo` 对象。
画面 8: 前端页面显示月报生成界面，用户点击“新建报表”后，浏览器开发者工具显示请求 `/attendances/reports?atteDate=201907` 的状态码为 200 OK。
画面 9: SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 10: SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 11: IDE 中展示 `AtteService.java` 文件，`getReports` 方法中调用 `attendanceDao.save` 方法保存数据。
画面 12: IDE 中展示 `AttendanceDao.java` 文件，定义了 `findByUserIdAndDay` 方法，并使用 `@Query` 注解指定 SQL 查询。
画面 13: IDE 中展示项目结构和运行日志，显示 Spring Boot 应用启动并成功解析 Eureka 服务端点。
画面 14: 前端页面显示 201907 月人事报表，包含员工姓名、工号、部门、考勤等详细数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```sql
SELECT COUNT(*) FROM
(SELECT (CASE WHEN atts.att_status = 1 THEN 1 END) att,
       (CASE WHEN atts.att_status = 2 THEN 1 END) att,
       (CASE WHEN atts.att_status = 3 THEN 1 END) att,
       (CASE WHEN atts.att_status = 4 THEN 1 END) att,
       (CASE WHEN atts.att_status = 5 THEN 1 END) att
FROM acto_attendance WHERE user_id = 1 AND DAY LIKE '201907%') t
```

画面 4:
```java
@Entity
@EqualsAndHashCode(callSuper = true)
@Table(name = "atte_archive_monthly_info")
@Data
@AllArgsConstructor
public class ArchiveMonthlyInfo extends BaseEntity implements Serializable {
    @Id
    private String id;
    private String userId;
    private String atteArchiveMonthlyId;
    private String name;
    private String workNumber;
    private String mobile;
    private String attResolution;
    private String department;
    private String workCity;
    private String yearLeaveDays;
    private String sickLeaveDays;
}
```

画面 5:
```java
@RequestMapping(value = "/reports", method = RequestMethod.GET)
public Result getReports(String atteDate) throws Exception {
    return new Result(ResultCode.SUCCESS, atteService.getReports(atteDate));
}
```

画面 6:
```java
public void editAtte(Attendance attendance) {
    //1.查询考勤是否存在,更新
    Attendance vo = attendanceDao.findByUserIdAndDay(attendance.getUserId(), attendance.getDay());
    //2.如果不存在,设置对象id,保存
    if (vo == null) {
        attendance.setId(idWorker.nextId() + "");
    } else {
        attendance.setId(vo.getId());
    }
    attendanceDao.save(attendance);
}
```

画面 7:
```java
public List<ArchiveMonthlyInfo> getReports(String atteDate, String companyId) {
    //1.查询所有用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户列表,统计每个用户当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //3.查询当月的考勤记录
        attendanceDao.save(info);
        list.add(info);
    }
    return list;
}
```

画面 11:
```java
list.add(attendanceDao.save(info));
```

画面 12:
```java
@Query("SELECT att FROM Attendance att WHERE att.userId = ?1 AND att.day = ?2")
Attendance findByUserIdAndDay(String id, String day);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

