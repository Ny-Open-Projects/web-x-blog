# 10-考勤数据导入：操作步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\10-考勤数据导入：操作步骤分析_【海量资源尽在 ubkz.com】.mp4
- 时长 10分39秒（音频 640s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们现在已经把对应的这个工具类做了一个小小的测试那好了接下来咱们就开始着手去完成我们这个文件上传的相关工作那首先呢回到我们的这个页面部分来看一下这边呢页面它就有一个导入的功能点击导入之后我们可以点击上传好了打开F12我们打开F12并且呢把这个demo的放到我们的页面部分OK方便我们进行拖拽啊
[00:34] 点击上传点击我们这个demo那各位你会发现它请求的一个路径请求到了我们attendance这个import那注意这个玩意儿其实就是我们咱们的考勤模块涉及到的一个新的一个类好了这边import那注意注意了
[00:55] 我们这边的烤琴设置还有这边的烤琴的这个管理呢它是在一个模块当中但是它分散到不同的请求路径上边了所以呢我们这边要想去做这个操作的话咱们要简单的说一下回到我们这个网关部分找到这边的配置那我们这个网关这边呢是不是只是对社保请求做了一个处理啊那接下来呢再去配置一份这个对应的就是我们的
[01:30] 注意这回对应的就是我们的ATTE我们的真正的社保这边也改下名字OK这个代表的是我们看那我们这回请求的路径的全部都在这儿摆着好了没问题了那网关的这边我先去重新启动一下我们接着再去写我们的代码OK这边网关着它启动不管了那我们这边呢各位发现你请求的时候请求到的是一个Controller当中
[02:04] 是一个引炮的方法那我们的请求方式是 post 这边呢会上传一个文件 fill 过来那接着我们就开始把这个代码呢给它一点一点的编写完成那回到我们的 java 代码部分找到我们的考其模块在考其模块当中我们配置一个新的 controllernew 一个 Controller这个 Controller 我们就是叫做 addendance 就是我们 attendancecontrollerc-o-n-t-r-o-l-o-e Controller好了那这边
[02:41] Etense Base Controller就是常规操作那接下来里面会有一些设置啊就是说你的附路径是什么然后呢Rest Controller等等好了我们请求的路径第一块拿过来OK好了那接下来这边需要配置一个方法就是我们叫做文件就是上传我们的考勤数据考勤数据哎没错吧那这边配置一个哎抱歉这个我就直接从其他的地方拷一段过来
[03:14] 做一个小小修改就可以了好那接着我们请求的这个路径呢刚才看过叫做importmport import那接下来method的部分没问题post都没问题那接下来呢是这样的就是请求方法呢就叫做import一一个cellok那在这我们的参数究竟有啥这个需要跟各位说明一下我们的参数呢在这种死不认
[03:47] boot 这种工程啊其实把它封装了一个 multi-part fill是一个文件对象所以我们这边就可以 add request pattern好了注意name 等于各位来看你上传的这个文件呢是不是叫做 fill 啊所以我这边就叫做 fill那接下来呢对应的是我们这边一个文件对象multi-part fillok 就叫 fill 了好了那么最终的文件上传了之后
[04:26] 这个玩意儿我们就不要了直接告他上传成功或者上传失败其实就可以了那中间部分我们就开始想方设法的解析数据接着把这些数据导入到我们自己的考勤数据表里没错吧各位OK那注意了这边呢我写这个代码呢就不想让他跟其他的代码混为一谈了我就专门的搞一个serviceprivate抱歉
[05:00] 我这边的专门的去搞一个Service这个Service专门就是用来负责处理我这个Excel文件上传的这边已经准备好了就是一个Excel import Service专门用来处理口琴文件上传的所以我把这个文件呢把这个直接引入进来out to be privateok 拿过来好了接下来呢我们要进行上传这个口琴功能呢其实很简单了借助Service我们在Service里面写一个方法
[05:40] 取完成就可以了好了打点起一个方法就叫做mpertattendance.ancerxcl好了那我们要上传文件的时候呢其实很简单把这个文件传递过去那千万别忘了我们上传的文件里面没有企业认可的关系所以我们这边还需要把这个企业ID传下去OK那这样一来我们的Controller层已经写好了接下来问题的关键来到了我们的solve层
[06:15] OK这个色位层我们就是处理考勤数据的文件上传那咱们要处理这个抱歉上传那我们要处理文件的考勤数据上传呢其实咱们要做的事情啊一共有这么几个需要各位要注意的那首先的这边的参数啊第一个就是我们的Excel文件好了接着第二个呢就是代表的是我们的企业ID这个各位应该都知道那我们这个操作的一个步骤
[06:50] 简单的来说一下那我们的这个操作步骤呢首先呢咱们的第一项第一项是这样的就是说呀咱们是不是需要将咱们需要将咱上传的这个Excel是不是解析成我们刚才测试的VO对象所以就是将导入的这个Excel文件解析为解析为我们的VO的粒子集合OK这个是第一个没问题好了接下来呢第二件事
[07:22] 那我们这个Excel文件解析呢已经解析成功了比如说已经解成功了那回到我们这边来看那这边有张三手机号和公号那我想问各位了那这玩意儿是不是要对应到是一个用户啊那在我们的用户是不是叫做user那么用哪个来对应它是一个用户呢所以我们要查询用户那用户呢可以是用公号来查也可以用手机号来查
[07:49] 当然用哪个查都可以因人而异因项目而异那我们的是一个SaaS系统当时也说过SaaS系统我们的手机号是唯一的所以我们就用手机号来去查询箱的用户就可以了回到我们这边来看一下就是循环VO对象VO的循环我们的list集合那在这个里面咱要做的根据上传的手机号码查询
[08:21] 用户这个应该各位都没问题好了用户呢我们查询出来了之后接下来呢这边有2.2那接下来干嘛呢就是说我要把注意我们这个上传考勤主要目的就是把这个Excel里面的数据是不是给它导入到我们对应的这个考勤表里啊那考勤表里面有很多的字段当然了它对比也是我们的一个考勤对象所以在我们这边2.2咱们就想
[08:50] 想方设法的就是构造我们的考勤考勤对象啊这个各位应该也能够理解那这些各位都能够理解那接下来呢还有一些啊2.3咱们就需要一些判断是这样的你上传的考勤对象考勤的这个表数据周六周日或者休息等等等等是不是他没有考勤数据但是他休息难道真的他就代表他旷工了吗
[09:21] 未必那对于这个对于我们的休假就是判断是否是一个休假的这么一个考进记录判断是否休假那接下来呢这边呢还有就是2.4啊那是这样的咱们的一个系统当中咱们的一个系统当中可能你打卡上午是9点打的卡或者10点打的卡这个时候咱们是不是代表他已经迟到那下午2点就打卡走了是不是代表早退所以我们要去判断一下他的迟到
[09:50] 早退的一些迟到早退的一些状态好了这个是我们要做的一些事情好了那接着还有第五个那第五个要做什么呢实际上在我们的系统当中有这么一个规定啊因为这个Excel你可以导入一次导入两次导入三次我们以第一次导入的为准也就是说防止你这个考勤作弊所以这边呢我需要做一个处理就是查询
[10:20] 是用户查询查询用户是否已经有考勤记录如果不存在我们保存数据库这个就是我们要做的这么几个操作步骤OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过前端上传Excel文件，后端通过Spring Boot接收并处理考勤数据，涉及控制器、服务层代码及配置文件的编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示PoTest.java代码，用于测试Excel导入功能，通过ExcelImportUtil读取Excel文件并打印内容。
画面2：展示iHRM系统考勤导入页面，用户可点击“点击上传”按钮上传Excel文件。
画面3：在浏览器开发者工具中切换到Network标签页，准备记录网络请求。
画面4：展示application.yml配置文件，其中定义了多个服务的请求路径和Eureka服务ID。
画面5：在IDEA中展示项目结构，选中application.yml文件。
画面6：在浏览器开发者工具的Network面板中，查看上传文件的请求头信息。
画面7：在IDEA中右键点击AttendanceController.java，准备进行测试或重构。
画面8：在浏览器开发者工具的Network面板中，查看上传文件的请求详情，状态码为404 Not Found。
画面9：展示AttendanceController.java代码，包含一个用于处理考勤配置的接口。
画面10：在AttendanceController.java中，为importExcel方法添加@RequestPart注解，用于处理文件上传。
画面11：展示项目结构，选中AttendanceController.java。
画面12：在AttendanceController.java中，为importExcel方法添加@RequestPart注解，用于处理文件上传。
画面13：展示ExcelImportService.java代码，定义了处理Excel文件上传的服务方法。
画面14：在ExcelImportService.java中，为importAttendaceExcel方法添加注释，说明其功能。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
package cn.itcast;
import com.itcast.common.pos.ExcelImportUtil;
import com.itcast.common.att.vo.AttUploadVo;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
public class PoTest {
    public static void main(String[] args) throws FileNotFoundException {
        ExcelImportUtil<AttUploadVo> util = new ExcelImportUtil<>(AttUploadVo.class);
        FileInputStream stream = new FileInputStream(new File("E:\\demo.xlsx"));
        List<AttUploadVo> list = util.readExcel(stream, rowindex: 1, cellindex: 0);
        for (AttUploadVo attaluploadVo : list) {
            System.out.println(attaluploadVo);
        }
    }
}
```

画面4：
```yaml
path: /sys/** #配置请求URL的请求规则
serviceId: ihrm-system #指定Eureka注册中心中的服务id
customSensitiveHeaders: true #对指定路由开启自定义敏感头
path: /employees/** #配置请求URL的请求规则
serviceId: ihrm-employee #指定Eureka注册中心中的服务id
stripPrefix: false
sentitiveHeaders: true #对指定路由开启自定义敏感头
path: /social-security/** #配置请求URL的请求规则
serviceId: ihrm-social-security #指定Eureka注册中心中的服务id
stripPrefix: false
sentitiveHeaders: true #对指定路由开启自定义敏感头
path: /cfg/** #配置请求URL的请求规则
serviceId: ihrm-attendance #指定Eureka注册中心中的服务id
stripPrefix: false
sentitiveHeaders: true #对指定路由开启自定义敏感头
path: /attendance/** #配置请求URL的请求规则
serviceId: ihrm-attendance #指定Eureka注册中心中的服务id
stripPrefix: false
sentitiveHeaders: true #对指定路由开启自定义敏感头
```

画面9：
```java
package com.itcast.att.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/attendances")
public class AttendanceController extends BaseController {
    @RequestMapping(value = "/atte/item", method = RequestMethod.POST)
    public Result atteConfig(String departmentId) {
        AttendanceConfig ac = configurationService.getAtteConfig(companyId, departmentId);
        return new Result(ResultCode.SUCCESS, ac);
    }
}
```

画面10：
```java
@RequestMapping(value = "/import", method = RequestMethod.POST)
public Result importExcel(@RequestPart("file") MultipartFile file) {
    return new Result(ResultCode.SUCCESS);
}
```

画面13：
```java
public class ExcelImportService {
    @Autowired
    private UserDao userDao;
    @Autowired
    private AttendanceDao attendanceDao;
    @Autowired
    private AttendanceConfigDao attendanceConfigDao;
    @Autowired
    private IdWorker idWorker;
    public void importAttendaceExcel(MultipartFile file, String companyId) {
        //1.将导入的excel文件解析为list集合
        //2.1根据上传的手机号码查询用户
        //2.2校验考勤对象
        //2.3判断是否在休
        //2.4 共同返回，导出的头
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

