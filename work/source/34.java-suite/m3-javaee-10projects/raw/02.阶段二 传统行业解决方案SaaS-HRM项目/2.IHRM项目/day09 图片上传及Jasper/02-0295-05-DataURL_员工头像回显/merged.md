# 05-DataURL：员工头像回显

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\05-DataURL：员工头像回显_【海量资源尽在 ubkz.com】.mp4
- 时长 2分46秒（音频 166s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们实现了这个用户头像的一个上传并且数据库里也有啊那接下来我们重新刷新一下你会发现就目前而言呢这个图片呢还没有给我回显过来那为什么是这样一个情况呢是这样的就是在我们这个代码部分呢有一个地方还要做一个简单的修改是因为我们在这边进入到我当前的这个页面其实发送了一个根据ID查询用户的这么一个请求
[00:28] 那对于这个请求呢我们可以定位到user Controller find by id这个方法各位会发现我得到的返回值是一个user result那这个user result当中并没有用户头像这么一个数据没错吧所以在这边呢如果想要它呢能够正常的显示出内容值内容的话我们需要把用户头像的这个属性复制到我们这个返回值当中
[00:56] 那剩下的内容不要关注直接通过避允条给我往里面copy属性其实就可以了OK那这回我再去重新启动一下我的系统微服务那这边让它去启动应该快启动成功了我们继续打开浏览器再来看一下效果是否能够完成这个用户照片的一个回显来重新加载一下这边让我重新登录了好了员工
[01:26] 那我们刚才搞的是JBZ查看并没有是吧那没有我再传一张看一下002好了传上去之后接着我再去刷新这个有啊那刚才是不是第一个查看给我来看没错那这样一来其实我们这个用户头像的回显咱们也已经完成了那这个其实就是我们灵活对Data UIL的一个运用而已
[01:58] 那我们呢这样一来其实就可以不再介入任何外部存储的情况下直接把一张投票头像保存到数据库当中了那其实针对这种情况呢还是有一个不好的地方在哪呢就是大家可以看到啊我现在呢存储到数据库的某这么一个字段里那这个字段呢其实是有一个格式的或者有自己的一个规定的我们看一下这个字段
[02:28] 配置那注意这边我用了一个比较长的一个test这么一个文本因为它里面存的数据实在是太多了能理解吧所以这个也是它的一个缺点如果你想要存图片的话那它占用的数据库里面的存储就比较多了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 iHRM 人事管理系统中员工信息的增删改查操作，并展示对应的后端 Java 代码实现和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 浏览器显示空白页面，URL 为 /employees/detail/106370598992677368，表示员工详情页加载失败或未完成。
画面 2: iHRM 系统员工详情页，显示员工“aj123”的信息，包括工号、姓名、手机、入职时间、部门和聘用形式。左下角显示 IntelliJ IDEA 中的项目结构。
画面 3: IntelliJ IDEA 中显示 UserController.java 文件，展示用于查询员工列表和根据 ID 查询单个员工的 @RequestMapping 注解和方法。
画面 4: IntelliJ IDEA 中显示 UserResult.java 文件，展示构造函数，用于将 User 对象的属性复制到 UserResult 对象中。
画面 5: IntelliJ IDEA 中显示 UserResult.java 文件，光标位于构造函数末尾。
画面 6: IntelliJ IDEA 中显示 UserResult.java 文件，光标位于添加员工头像字段的注释行。
画面 7: IntelliJ IDEA 的 Run 窗口显示 Spring Boot 应用启动日志，包含多个 RepositoryConfigurationExtensionSupport 的警告信息。
画面 8: iHRM 系统登录页面，显示登录框和默认账号密码。
画面 9: iHRM 系统员工列表页，显示多个员工记录，包括序号、姓名、手机号、工号、聘用形式和操作按钮。
画面 10: iHRM 系统员工详情页，显示员工“zbz”的信息，包括工号、姓名、手机、入职时间、部门和聘用形式。
画面 11: 浏览器显示空白页面，URL 为 /employees/detail/106370498613486136，表示员工详情页加载失败或未完成。
画面 12: iHRM 系统员工详情页，显示员工“aj123”的信息，包括工号、姓名、手机、入职时间、部门和聘用形式，员工照片已成功上传。
画面 13: SQLyog 数据库管理工具，显示 user 表的数据，其中一条记录的 staff_photo 字段值为 base64 编码的图片数据。
画面 14: SQLyog 数据库管理工具，显示 user 表的数据，其中一条记录的 staff_photo 字段值为 base64 编码的图片数据，与画面 13 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
// 查询企业的部门列表
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map, page, size) {
    // 1.查询所有企业
    map.put("companyId", companyId);
    // 2.完成分页
    PageResult pageResult = new PageResult(pageUser.getTotalElements(), pageUser.getContent());
    return new Result(ResultCode.SUCCESS, pageResult);
}

// 根据ID查询user
@RequestMapping(value = "/user/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    User user = userService.findById(id);
    UserResult userResult = new UserResult();
    return new Result(ResultCode.SUCCESS, userResult);
}

// 修改User
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
```

画面 4 代码：
```java
private String workingCity;
// 转正时间
private Date correctionTime;
// 在职状态 1.在职 2.离职
private Integer inServiceStatus;
private String departmentName;
private List<String> roleId = new ArrayList<>();
public UserResult(User user) {
    BeanUtils.copyProperties(user, target: this);
    for (Role role : user.getRoles()) {
        this.roleIds.add(role.getId());
    }
}
```

画面 6 代码：
```java
private String staffPhoto;//用户头像
```

画面 13 SQL：
```sql
SELECT * FROM user;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

