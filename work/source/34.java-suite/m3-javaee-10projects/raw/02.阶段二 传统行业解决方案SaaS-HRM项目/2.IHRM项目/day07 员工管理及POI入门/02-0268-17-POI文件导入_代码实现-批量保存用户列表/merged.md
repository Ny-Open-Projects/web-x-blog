# 17-POI文件导入：代码实现-批量保存用户列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\17-POI文件导入：代码实现-批量保存用户列表_【海量资源尽在 ubkz.com】.mp4
- 时长 8分28秒（音频 508s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那剩下的内容就比较简单了我们可以在Service这边写一个方法实现接收用户list然后呢完成保存的这面个操作那我们一起来完成它好了user Service打点好了user Service打点呢我们这个方法呢比如说呢我就叫做CUR方法那我们首先接收的是一个list结合我们的用户list结合那除了用户list结合之外呢就是说啊对于这一个用户必然从属于某一个企业
[00:32] 所以我们需要把当前这个企业的一些属性也给它设置过去那这个企业在哪呢其实就是说当前你操作或者当前谁在去批量导入那这个用户是不是必然它内部也有这个企业的一些内容所以这些企业内容我们已经在我们的base Controller当中给它写好了所以我这边直接company idcompany name是不是直接用就可以也就是说谁操作必然你这个列表都属于这个人的公司
[01:02] 没错好了接下来我们的Service现在少方法少方法好办少什么我们就添加什么即可好了找到用户Service我在最上边咱们就可以完成一个批量用户保存批量用户保存好了public vid cu我这里面接受的这么几个参数也给它补充出来list userlist
[01:41] 死菌类型的company id死菌类型的name好了对于这个里面的代码写起来呢比较简单it而放循环那有的朋友问我为什么不直接调用方法为什么要用放循环呢是因为对于我们这里面要想要想完成批量那我们这个用户数据还不够还有一些我们基本的一些配置比如说呢我们的默认密码好了那接下来呢比如说呢我们还需要设置id那除了这些之外对一个用户来说是不是还有它的基本的一些属性
[02:15] 没错吧那接下来呢我们就可以去把这几个代码给他都设置过去设置密码user.setpassword那你设置密码的时候那注意我们这个密码是不是应该要经过MD5的一个加密处理MD5 hash那我们之前的一个规则初始密码123456还有音箱吧当然了对这个密码进行加密好了那对于我们来说还需要给他加盐
[02:47] 那延试上嘛是不是就是user打点get我们的登录手机号那接下来呢后面就是加密次数来一三这样一来呢打点突死菌我们就能得到默认加密好的这个密码那好了接着设置IDuser打点set id那这个id通过我们的id worker打点生成next id好了接下来就是一些基本的一些属性那对于这些基本属性首先第一个set我们叫做set
[03:18] company id给他设置进去还有打点setcompany name也设置进去那剩下的事情呢就是一些他自己状态的一些设置比如说user打点set in Service是否是一个正常的入职状态好了user打点set enable当前这个用户呢是否可以登录我们的系统他是否可以使用
[03:48] 好了还有一个就是user.setLevel就是这个用户的一个级别是不是应该是一个普通用户啊OK那好了这样一来我基本的这些所有属性都给它设置成功了那剩下的一件事就可以调用user.du.m我们这边呢叫做save方法一个一个的去保存但是我们这个保存内容呢会比较多啊所以上边呢ata.transessional加上事物的一个处理即可
[04:17] 好了那这样一来我基本的这个用户导入咱们就已经都写好了那写好了之后在这边我重新启动一下系统微服务好了我的项目已经启动成功了那接下来呢就是回到我们这个代码的这个部分前端那接着我们可以去实现一个用户上传的这个功能去测试一下代码是否有问题好了这边的点击上传那定位到我们今天的资源给各位提供的这个数据导入模板
[04:49] 那其实就是导入了这么几条用户的这么一个数据那拿到这些数据我们把它保存到数据库里面来看一下效果其实就可以了好添加进去走各位发现这边导入成功了那我们这个数据呢一共有三条我们来看一下数据库来那打开我们的数据库呢我们会看到导入成功了之后注意我们这边数据呢你会发现现在有两条是啊
[05:20] 那我们的Excel是不是应该有三条数据啊好了这个是一个问题那除了这个问题之外呢还有一个就是说在这边我们这个部门的一个ID不对我们应该是部门ID和部门名称现在是不是用的是一个部门编码那当然了还有一个就是worker number现在是挂了一个点零没错吧好了那接下来呢就是对于这几个问题呢我们一个一个来进行处理首先呢数据为什么变成两条了我们检查一下代码呢这边打开代码
[05:49] 其实这个应该能想到因为我们之前做导入案例的时候刚才我们就说过了对于每一行而言对于每一行而言你拿到的行号0123其实是3我们这边是不是就应该是小于等于的这种形式来做它跟我们这边拿到列拿到格子不一样格子其实是1234567
[06:16] 所以它正好有一个不太一样的地方这个其实拿到的是最大索引这个拿到的是最大编号没错吧咱们之前就有做过分析那所以这个跟他刚才之前那个错误应该是一样的好了呢这个问题我们解决了那接下来呢还有一个问题那接下来一个问题是这样的就是说对于我们这个DBTDV这个部门编码这个部门编码呢可能就要用到通过我们的服务去调用企业备付因为企业服务备付才能根据部门编码拿到企业信息
[06:45] 那当然除了这个之外还有一个零点几的这个情况零点几这个情况是因为在Excel其实默认它已经把这些玩意儿给它变成一个数字了变成数字我们之前说过对于PY而言它把这个咱们是部门这个公号Worker Number那对于这个Worker Number而言它其实把它变成了一个数字那数字是不是一个Double类型的那既然是Double类型肯定是以.0结尾那.0结尾必然有一个.0的这么一个转化成死去
[07:14] 这么一个形式所以呢我们也可以把这个进行一个处理那处理这个比较简单直接借助一个decembr format一个工具类其实就可以了decembrdecembrdecembr format这么一个工具类里面可以接收一个警号好了这个代表的是你要保留的一个数字的一个处理的一个形式当它点format好了接着把我们这个double放进去这样一来它就处理掉处理掉之后点凸死菌即可
[07:47] 好了这些我们都写好了之后系统微幅我重启一下耐心等待一下我们再去保存一下当然我们要想完成这个呢需要把之前的这两条数据给它删掉给它删掉OK那好了找到页面再去重新上传一次我们再来看一下效果走好了导入成功好了回到我们的数据库刷新一把你会发现三条数据都在123都没问题
[08:19] 那现在还遗留最后一个问题就是我们这边的一个部门编码因为刚才说过了部门编码涉及到跨服务调用

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码读取 Excel 文件中的用户数据，并批量保存到数据库，涉及用户服务层、数据转换和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 UserController.java 中，展示从 Excel 读取数据后调用 userService.saveAll() 方法批量保存用户。
画面 2: 在 UserController.java 中，展示 saveAll 方法的实现，其中包含对用户对象的属性设置，并调用 userService.saveAll。
画面 3: 在 UserService.java 中，展示 save 方法的实现，其中设置用户 ID、密码、部门等属性。
画面 4: 在 UserService.java 中，展示 findUserByMobile 方法的实现，用于根据手机号查找用户。
画面 5: 在 UserService.java 中，展示 setMobile 方法的实现，用于设置用户手机号。
画面 6: 在 UserService.java 中，展示 setDepartmentId 方法的实现，用于设置用户部门 ID。
画面 7: 在 UserService.java 中，展示 setEnableState 方法的实现，用于设置用户状态。
画面 8: 在 UserController.java 中，展示 getCellValue 方法的实现，用于获取单元格的值。
画面 9: 展示 Excel 文件“导入测试模板.xlsx”，其中包含用户数据，如用户名、手机号、工号、聘用形式、入职时间、部门编码。
画面 10: 在 SQLyog 中，展示查询用户表（b_user）的 SQL 语句，用于验证数据。
画面 11: 展示 Excel 文件“导入测试模板.xlsx”，其中部门编码列被选中。
画面 12: 在 User.java 中，展示构造函数的实现，用于从数组中解析用户属性。
画面 13: 在 User.java 中，展示构造函数的实现，其中使用 DecimalFormat 格式化工号。
画面 14: 在 SQLyog 中，展示查询用户表（b_user）的 SQL 语句，用于验证数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
return new Result(ResultCode.SUCCESS);
```
画面 2:
```java
for(int cellNum=1; cellNum <= row.getLastCellNum(); cellNum++) {
    (cell cell = row.getCell(cellNum);
    Object value = getCellValue(cell);
    values[cellNum] = value;
}
User user = new User(values);
list.add(user);
//3.批量保存用户
userService.saveAll(list,companyId,companyName);
return new Result(ResultCode.SUCCESS);
```
画面 3:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 4:
```java
//根据mobile查找用户
public User findByMobile(String mobile) { return userDao.findByMobile(mobile); }
//批量保存用户
public void saveAll(List<User> list, String companyId, String companyName) {
    for (User user : list) {
        user.setPassword(new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString());
        user.setId(IdWorker.nextId()+"");
        user.setCompanyId(companyId);
        user.setCompanyName(companyName);
        user.setServiceStatus(1);
        user.setEnableState(1);
        user.setLevel("user");
    }
}
```
画面 5:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 6:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 7:
```java
//设置主键id
String id = IdWorker.nextId()+"";
String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
user.setId(id);
user.setPassword(password);
```
画面 8:
```java
public static Object getCellValue(Cell cell) {
    //获取单元格属性类型
    CellType cellType = cell.getCellType();
    Object value = null;
    switch (cellType) {
        case STRING:
            value = cell.getStringCellValue();
            break;
        case BOOLEAN:
            value = cell.getBooleanCellValue();
            break;
        case NUMERIC:
            value = cell.getNumericCellValue();
            break;
        case FORMULA:
            value = cell.getCellFormula();
            break;
        case BLANK:
            value = "";
            break;
        case ERROR:
            value = cell.getErrorCellValue();
            break;
    }
    return value;
}
```
画面 9:
（无代码）
画面 10:
```sql
SELECT * FROM em_company_personnel a, b_user b WHERE a.user_id = b.user_id AND a.resignation_time BETWEEN '2018-01-01' AND '2018-12-31'
```
画面 11:
（无代码）
画面 12:
```java
public User(Object[] values) {
    //用户名
    this.username = values[1].toString();
    //手机号
    this.mobile = values[2].toString();
    //工号
    this.workNumber = values[3].toString();
    //聘用形式
    this.formOfEmployment = (Double) values[4].intValue();
    //入职时间
    this.timeOfEntry = (Date) values[5];
    //部门编码
    this.departmentId = values[6].toString();
}
```
画面 13:
```java
public User(Object[] values) {
    //用户名
    this.username = values[1].toString();
    //手机号
    this.mobile = values[2].toString();
    //工号
    this.workNumber = new DecimalFormat(pattern: "0000000000").format(values[3]).toString();
    //聘用形式
    this.formOfEmployment = (Double) values[4].intValue();
    //入职时间
    this.timeOfEntry = (Date) values[5];
    //部门编码
    this.departmentId = values[6].toString();
}
```
画面 14:
```sql
SELECT * FROM em_company_personnel a, b_user b WHERE a.user_id = b.user_id AND a.resignation_time BETWEEN '2018-01-01' AND '2018-12-31'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT、架构图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

