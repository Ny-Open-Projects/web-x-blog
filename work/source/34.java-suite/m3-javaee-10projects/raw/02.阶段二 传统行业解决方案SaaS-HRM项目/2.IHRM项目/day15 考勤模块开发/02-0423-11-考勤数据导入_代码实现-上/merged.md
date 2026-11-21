# 11-考勤数据导入：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\11-考勤数据导入：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 时长 12分18秒（音频 738s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们简单的把咱们这个操作步骤呢说了一下那接下来呢就可以把这个代码呢给它一个一个都写出来首先呢咱们来看第一步就是将导入Excel文件解析为这个VU结合那对于这一步骤呢很简单我们之前呢自己专门玩过咱们new一个我们自己的工具内就可以了好了那这个里面呢我们让它转型成一个uploadVU对象
[00:31] 好了这边就是upload.Vue.class.read那注意我们刚才说过了read两个参数第一个是三个参数第一个是流第二个是你读的从哪行开始从哪个格子开始这个都比较简单了fill.getInputStream可以得到上传文件的文件流那从第一行开始读从第抱歉从第二行开始从第一个单元格开始获取数据好了这边呢有一个小小的异常啊给大家处理一下
[01:05] OK那注意我写了比较长这个代码就写了一行那这样一来我们就能够得到对应的一个粒子集合好了粒子集合呢我们获取到了接着去循环粒子集合ITER for循环好那循环过来之后我们说过了要在里面去完成这么一些操作要完成这些操作呢要根据上传的用户查询手机号查询用户那这个我想说一下
[01:34] 那其实正规的流程呢我们应该通过咱们自己的系统通过我们自己的系统因为我们这边是有多个微服务的简单的说一下这边是我们的系统微服务系统微服务那这边呢是我们的其他的一些微服务比如说我们这边有考勤比如说呢这边呢我们有其他的比如说有薪资那正常的逻辑在我们考勤微服务应该发送一个http的份请求发送
[02:10] 获取用户数据好了同样的新资如果用也是这样的但是呢这种方式呢究竟好还是不好呢因人而异了是这样的我们这边的系统呢获取的这个用户呢可能比较多了一个公司有一百个用户有一千个用户每天都有考勤记录那这个时候呢就要查询成千上万次这是有可能的所以我说呢咱们如果发送请求呢处理这个就有点太慢了所以在这边呢
[02:39] 咱们用了一个比较取巧的方式或者折中的方案由于我们这边所有的数据呢所有的表呢都在一个库当中所以在这边所以在这边我们配置了一个专门用来处理用户的一个DO注意这种方式究竟是好还是不好因而异但是我们说过了如果直接发送请求的话这个数据量实在是太大了所以我们直接把这个DO直接拿过来我们在这儿用DO直接查询能理解我意思吧
[03:08] OK,接下来这个do呢我已经放到这了所以呢我们就把这个do all to bit也引用进来private user do user doOK,好了呢这个user do呢我们看一下这边怎么会有一个爆红色抱歉啊这个user do其实上面已经引用过了那接下来呢我们这边就可以通过user do手机号码来查询了点注意
[03:50] 在U2DU当中我专门写了一个方法就是FindMobile这个比较简单好了我们直接拿到对应的Mobile.getMobile那这样一来我们就能够得到当前的这个用户对象OK好了用户对象呢我们获取到了之后那接下来呢咱们就开始了咱们说过你要玩这个数据操作
[04:17] 咱们需要去构造对应的考勤对象那考勤对象呢咱们也给各位刚才导入已经导入进来了好了在entity当中那我们这个数据对象呢就是这个就是他考勤表所对应的实体类那我们其实就构造这么一个实体类哎就可以了那回到我们这边呢咱们开始去构造实体类那构造这个实体类就是attendance
[04:50] attin.ce等于你有一个attendance对象出来那我们这个对象当中需要什么数据我们就开始从上边user还有从我们上面导入对象里面是不是开始进行获取比如说里面需要company id部门iduser id好了以及你上班的时间以及你下班的时间等等等等没错吧那所以在这边呢咱们开始一个一个的进行set点
[05:20] set进去比如说set user id那么就是user.get id但是这种方式其实有点显代码显得不太好看啊所以我个人习惯就是全部都写到构造方法当中那这边也给各位准备好了一个构造方法这个构造方法接收两个参数直接它就会一个一个设置进去所以我们这边要用构造方法把数据给它构造出来OK好了呢我们现在已经构造好了对应的这个考勤的这个对象
[05:55] 那除了这个考勤的这个对象之外呢还有一点需要各位一定要注意的是在这个地方就是说我们这个考勤啊为了我们之后方便查询我这边专门写了一个day这个是我们考勤的日期哎这个是我们记录的考勤相关的这个日期那对于这个考勤日期我们也需要做一个小小的处理OK好了所以这个考勤日期我们需要把它保存进去点
[06:30] set我们叫做day那这个考题认识器从哪获取到呢其实就是我们上传的这个上班时间或者下班时间我们是不是直接可以拿前面这一部分是不是就可以了当然了有的朋友就说了它有可能前面这一部分不存在那不存在你可以拿后面这一部分那如果都不存在那这条数据其实都没有懂我意思吧所以我们这边做的可以做一个判断就是上班时间没有我们用下班时间下班没有我们用上班时间
[07:02] 都可以当了我们这边写的稍微简单一点我们就用上班时间来进行获取就可以了好了我们在资料当中给各位之前导入了一个DataUtils这么一个工具类DataUtilsDataUtils这么一个工具类那通过这个工具类打点咱们可以进行一个设置把我们这个数据呢给它处理的好看一点因为我们数据库的格式啊
[07:37] 就处理成我们数据库所需要的这种日期的格式好那接下来呢这边呢咱们就可以处理一下我们说过了要用的是你上传的这个对象里面的上班时间打get in time那我们要处理成什么样子咱们就可以写一下了比如说我要处理成YYYYMMDD好了那接着把这玩意儿set进去OK好那这样一来呢我们这个考勤对象呢就已经给它处理好了
[08:09] 那接下来呢除了考勤对象之外那接下来底下呢咱们这边还应该要处理他这天呢是不是休假那为什么要判断是不是请是不是要休息呢是因为咱们考勤机导出来的这个数据啊有可能他有这么一种情况比如说呢张三还是这个张三第二天呢其实什么数据这边都没有但是呢他可能就设置了一下比如说他可能就导入这么一个02这样的危险
[08:42] 或者他有一天就写了一个什么什么03但是这个7月2号他来不来其实都行因为这天呢他是一个休息日或者是周一或者是周二等等等等或者是11或者是10月2号这些可能是休假的一些情况那为了防止咱们错误的给他记录成为了防止错误的给他记录成我们这边的
[09:11] 需要对这个日期呢进行一个小小的处理当然了有的朋友就说了有朋友就说了你这玩意儿其实看起来还是不太清晰的其实我这边设计的时候就是用这么一个时间来进行统计当然了有朋友就说了我这边呢打卡格式这种方式处理起来比较麻烦那么可以在这儿再加一个excel再去加一个带处理的一个字段就可以了其实这种方式更加简单当然了我们用这种上下班时间来进行排除也行
[09:40] 那有的朋友就说我这需要加一个那咱们可以加一个来试一下比如说呢我再加一个加一个什么呢就是我们考勤时间考勤日期比如说呢这回我们这个考勤日期就能是2019比如说07 01没错吧那比如说这边就是2019-0702这么一种格式那同时呢这个第二天这个是不是就应该是它应该可能是周六
[10:08] 或者周日你没有上班时间也没有下班时间我是不是就可以默认认为你当前这一天是不是就旷工了为了防止它出现这个问题所以我们这边要对这个做一个排除好了咱们既然在考进表里的要求让它多加了一个字段我们这边同样的回到咱们的实体类当中也把这个字段给它加上让它更加完善一点05我叫ATTEDATE注意这是一个死菌类型的
[10:45] 就行了好了同样的这边是死菌类型的OK没问题那接着找到我们刚才这个测试类来看一下能不能够把这个数据呢给我解析出来啊找到刚才我们这个测试类来走这边先注射掉来走各位来看等等data抱歉我这边应该是改错文件了因为我改的是桌面的我们这边拿的是一盘下这个保存一下
[11:46] 再打开看一下有没有果然没有嘛OK保存一下我们再来试一下这回这个数据是不是就已经有了好那这边呢我们对这个代码呢做了一个对这个Excel格式做了一个小小的处理那这边呢咱们就继续往下去看了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中实现Excel考勤数据导入功能，包括服务层代码编写、数据模型定义、数据库操作及Excel解析工具的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE界面显示ExcelImportService.java文件，其中定义了@Autowired注入的AttendanceDao、AttendanceConfigDao和IdWorker。
- 方法importAttendanceExcel接收MultipartFile文件和companyId参数。
- 方法注释说明了处理Excel文件上传、解析、查询用户、构造考勤对象、判断迟到早退、检查重复记录等步骤。

画面2：
- 在importAttendanceExcel方法中，使用ExcelImportUtil工具类读取Excel文件，创建List<AtteUploadVo>集合。
- 代码中使用了rowindex=1，cellindex=0等参数。

画面3：
- 展示一个空白的流程图或架构图，包含三个椭圆形框，分别标注“系统微服务”、“考勤”和一个未命名的框。

画面4：
- IDE项目结构视图，显示了com.ihm.attendance包下的Controller、dao、Service等目录结构。
- 展示了AttendanceController、AttendanceDao、UserDao等类。

画面5：
- 显示ExcelImportService.java文件的import语句部分，包括了AttendanceConfigDao、UserDao、ExcelImportUtil、IdWorker等类的导入。

画面6：
- IDE项目结构视图，高亮显示了UserDao.java文件。
- 在ExcelImportService.java中，代码行显示了userDao.findByMobile方法的调用。

画面7：
- IDE界面显示了多个Java文件标签，包括Attendance.java、UserDao.java、ConfigController.java。
- 在ExcelImportService.java中，代码行显示了userDao.findByMobile方法的调用。

画面8：
- 在ExcelImportService.java中，代码行显示了attendance.setUser(user)的调用。
- 代码提示显示了Attendance类的setUser方法。

画面9：
- 在ExcelImportService.java中，代码行显示了attendance.setDay(attendance.setDay())的调用。
- 代码提示显示了Attendance类的setDay方法。

画面10：
- 在ExcelImportService.java中，代码行显示了attendance.setDay(attendance.setDay())的调用。
- 代码提示显示了Attendance类的setDay方法。

画面11：
- 展示了一个Excel表格，包含“员工姓名”、“手机号”、“工号”、“上班时间”、“下班时间”等列。
- 表格中显示了示例数据，如员工姓名“张三”，手机号“13800138002”，工号“123456”，上班时间“2019-7-1 8:30”，下班时间“2019-7-1 18:30”。

画面12：
- IDE界面显示了AtteUploadVo.java文件，其中定义了@Data和@ToString注解。
- 类中定义了多个私有字段，包括username、mobile、workNumber、inTime、outTime、attStatus等，并使用了@ExcelAttribute注解。

画面13：
- 展示了电脑桌面，显示了“黑马程序员”和“博学谷”的标志。
- 桌面上有多个快捷方式图标，如“Lemon”、“demo.xlsx”、“此电脑”、“回收站”、“优博方式”、“TUA客户”、“截图”、“记事本”等。

画面14：
- IDE界面显示了ExcelImportService.java文件，其中代码行显示了attendance.setDay(DateUtil.parseDate2String(atteUploadVo.getStartTime(), pattern))的调用。
- 代码注释说明了“判断是否迟到”、“判断是否早退”、“查询用户是否已有考勤记录，如果不存在，保存数据库”等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
private AttendanceDao attendanceDao;
@Autowired
private AttendanceConfigDao attendanceConfigDao;
@Autowired
private IdWorker idWorker;

/**
 * 处理考勤数据的文件上传
 * 参数：excel文件
 * 企业
 */
public void importAttendanceExcel(MultipartFile file, String companyId) {
    //1.导入的excel文件解析为vo的list集合
    //2.循环list集合
    //2.1 根据上传的手机号码查询用户
    //2.2 构造考勤对象
    //2.3 判断迟到，早退的状态
    //2.5 查询用户是否已经有考勤记录，如果不存在，保存数据库
}
```

画面2：
```java
public void importAttendanceExcel(MultipartFile file, String companyId) throws Exception {
    //1.导入的excel文件解析为vo的list集合
    List<AtteUploadVo> list = new ExcelImportUtil(AtteUploadVo.class).readExcel(file.getInputStream(), rowindex: 1, cellindex: 0);
    //2.循环list集合
    for (AtteUploadVo atteUploadVo : list) {
    }
}
```

画面4：
```
com.ihm.attendance
├── Controller
├── dao
│   ├── ArchiveMonthlyDao
│   ├── ArchiveMonthlyInfoDao
│   ├── AttendanceDao
│   ├── AttendanceConfigDao
│   ├── DeductionDao
│   ├── DeductionTypeDao
│   ├── ExtraDutyRuleDao
│   ├── UserDao
├── Service
│   ├── AttendanceServiceApplication
│   └── ShiroConfiguration
└── resources
    ├── ihm_attendance.ini
    └── pom.xml
```

画面5：
```java
import com.ihm.attendance.AttendanceConfigDao;
import com.ihm.attendance.AttendanceDao;
import com.ihm.attendance.entity.ResultCode;
import com.ihm.common.exception.CommonException;
import com.ihm.common.utils.ExcelImportUtil;
import com.ihm.common.utils.IdWorker;
import com.ihm.domain.att.vo.AtteUploadVo;
import com.ihm.domain.system.User;
import lombok.extern.log4j.Log4j2;
import org.apache.commons.lang.StringUtils;
import org.apache.poi.ss.usermodel.NSSerialNumber;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import java.io.IOException;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.List;
```

画面6：
```java
User user = userDao.findByMobile(atteUploadVo.getMobile());
```

画面7：
```java
attendance.setUser(user);
```

画面8：
```java
attendance.setDay(attendance.setDay());
```

画面9：
```java
attendance.setDay(attendance.setDay());
```

画面10：
```java
attendance.setDay(attendance.setDay());
```

画面12：
```java
package com.ihm.domain.att.vo;

import java.util.Date;

@Data
@ToString
public class AtteUploadVo {

    //员工姓名
    @ExcelAttribute(sort=0,format="String")
    private String username;
    //手机号
    @ExcelAttribute(sort=1,format="String")
    private String mobile;
    //工号
    @ExcelAttribute(sort=2,format="String")
    private String workNumber;
    //上班时间
    @ExcelAttribute(sort=3,format="Date")
    private Date inTime;
    //下班时间
    @ExcelAttribute(sort=4,format="Date")
    private Date outTime;
    //考勤状态
    @ExcelAttribute(sort=5,format="String")
    private String attStatus;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
- 架构图包含三个椭圆形框，分别标注“系统微服务”、“考勤”和一个未命名的框。
- 未显示任何连接线或指向关系。

画面11：
- 表格包含“员工姓名”、“手机号”、“工号”、“上班时间”、“下班时间”等列。
- 表格中显示了示例数据，如员工姓名“张三”，手机号“13800138002”，工号“123456”，上班时间“2019-7-1 8:30”，下班时间“2019-7-1 18:30”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

