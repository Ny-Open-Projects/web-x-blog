# 07-考勤管理：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\07-考勤管理：需求分析_【海量资源尽在 ubkz.com】.mp4
- 时长 8分7秒（音频 487s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们已经完成了考勤设置相关的一些内容当然了我们考勤设置呢代码实现只写了一个考勤的它的一个出勤时间的一个相关设置那剩下的这三块呢留给各位去完成当然了相应的代码呢也会在资料当中提供那这块搞定了之后接下来呢就进入到今天的第三块就是一个考勤管理那对于这个考勤管理其实才是真正的
[00:28] 在我们的页面上去显示一个员工当月他的一个考勤数据情况当呢这边呢也可以对当月的这个考勤数据进行报表生成以及归档其实这些逻辑呢跟我们这边社保的差不多那接下来呢我们简单的就说一下我们要去完成这个考勤管理所设置的一个大体的一个业务逻辑
[00:56] 好了,一张图呢,和各位做一个简单的说明。
[01:02] 好,那这边呢,代表的就是我们的考勤管理。
[01:09] 设置一下字体,考勤管理。
[01:12] 那这个考勤管理,进来之后呢,是什么样的,需要各位注意一下。
[01:22] 进来之后呢,其实就是去展示我们当前的这个考勤列表。
[01:30] 考勤,考勤,列表。
[01:32] 那对于这个考勤列表的数据,其实呢,有很...
[01:39] 但是这些数据的来源究竟应该从什么地方来这个是希望各位注意的一点所以这边呢有一个小小的疑问跟各位来做一个说明就是这个考勤数据那对于这种考勤数据呢往往啊往往是通过
[01:58] 咱们现有的一些系统或者现有的一些工具导入过来的所以这边的数据应该是导入过来的那我们都知道这个烤琴呢就涉及到你上午的上班打卡时间下午下班的打卡时间等等那这些数据从哪来大家都知道了就是从烤琴机里获取到所以我们这些数据从哪来的这边呢就涉及到我们的每个公司都会有的这么一个烤琴烤琴机那烤琴机里面会进行记录
[02:29] 那这个数据呢怎么导入到考勤咱们的人力资源这个系统里怎么通过考勤机把数据导入到人力资源管理系统当中哎有两种方式哎这边就涉及到一个数据导入那这个数据导入呢有两种方式第一种方式是这样就是两个系统一统进行连通把两个系统连到一起那在我们的数据库里面是不是能拿到人家这个数据库表里的数据啊
[03:05] 那这种方式呢这个不太现实不太现实为啥不太现实是这样的我说一下就是这个考勤机呢每个公司它都有并且是五花八门的你定个公司如果是用的是一号公司它的数据库一这类型二号公司的考勤机它是二号类型所以这个呢不太现实往往还有第二种形式第二种形式就是将考勤机数据生成为Excel接着将
[03:35] EXCL导入导入到我们的人力资源里这个是两种方案但是呢对于第二种方案呢用的会稍微多一点当然我们用的也是这种方案OK好那这样一来呢我们考勤机把这个数据导入到我们的考勤管理当中那接下来我们就可以展示考勤列表那考勤列表呢我们展示好了之后那接下来呢咱们就继续往下走
[04:06] 那针对某些人的考勤呢可能会存在一些小小的问题比如说呢你这边记录的时间有误或者说我今天上午忘了打卡了我们可能涉及到一个补充打卡的这么一个环节所以这边呢还有一个小小的环节就是我们的考勤记录的一个修改修改我们这个考勤记录这也是我们需要做到的一件事情
[04:36] 那这个考勤记录我们修改好了之后那接下来呢当前咱们这个考勤列表说的考勤都没有问题了那接下来我们要做的事情就跟之前一样接下来我们要做的第三件事抱歉我这边写了序号第二个就是修改我们的这个修改修改我们的考勤考勤的一些数据考勤数据那接下来呢这边还有第三件事第三件事情是这样的就涉及到我们的月
[05:08] 报表月报表与数据归档所以这边就是我们的第三个叫做数据归档相关的操作所以对于我们人力资源管理系统而言人力资源管理系统为了能够比较良好的去展示我们的考勤列表这些数据是从考勤机获取到了考勤机获取到了之后我们可以以列表的形式展示出当前所有员工所涉及到这些考勤记录
[05:39] 那对于不符合或者对于某些记录错误的这些考勤记录我们可以做修改那修改全部完毕了之后各位发现考勤列表没问题了我们进行数据归档好了我们进行数据归档我们可以展示一下当前月它的一个保表数据那接着进行归档归档之后就可以为我们计算薪资提供数据支持
[06:05] 好了这个就是我们考勤管理所涉及到的这些业务逻辑那么要想去完成考勤管理相关的业务逻辑所涉及到的数据库表各位一起来看一下在咱们的资料当中在我们的数据库当中呢准备了这么几张表各位来看第一个Attendance这个代表的是我们的考勤记录的一张表考勤记录的一张表里面涉及到的字段呢其实都比较简单比如说有用户
[06:32] 比如说有公司比如说有部门这边还有考勤那个情况正常打卡等等等等好了这边有上班考勤的时间下班考勤的时间其实这个玩意就跟我们打卡机差不多我们要做的就是把打卡机的数据导入到这张表当中OK那这张表呢咱们简单的介绍了一下那接下来呢还有第二张表那第二张表是这样的就是上边这边有一个归档的一个
[06:59] 按月归档的这么一个考勤记录表注意这个是我们考勤总的一个归档表里面会记录企业当中本月一共多少人全勤一共多少人这是一个归档的一个我们叫做主表那除了这个表之外还有一个归档明细表叫做info这个里面就比较详细了记录当前这个月每一个员工他的一个数据情况
[07:30] 所以呢这回这个表呢比较简单一共有这么三张当然除了这三张我们还有一个就是company setting这个company setting跟我们之前做社保其实是一样的这个表都是一模一样的主要是为了记录一下你当前你当前设置考勤设置到哪个月份方便我们进行月份的轮转OK当然了有朋友说这个表呢是不是有点重复了没关系这个表呢如果你不喜欢其实通过一张表里面也能够完成这样的操作
[08:00] OK 那我们这边就把它单门拿出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个考勤管理系统的功能界面、业务流程图设计以及对应的数据库表结构和SQL建表语句。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示考勤管理系统的前端界面，显示“无数据”状态，左侧菜单栏选中“考勤”。
画面2：前端界面加载出考勤数据列表，包含员工ID、姓名、部门、考勤状态、考勤日期等字段。
画面3：在绘图工具中新建一个矩形框，准备绘制流程图。
画面4：在矩形框内输入文字“考勤管理”。
画面5：在“考勤管理”框下方添加一个菱形框，标注“考勤列表”，并用箭头连接，标注“1.考勤数据(导入)”。
画面6：在“考勤管理”框右侧添加一个矩形框“考勤机”，并用箭头连接“考勤列表”，标注“i.两个系统连通 ii.将考勤机数据生成为excel,将excel导入到人力资源中”。
画面7：在“考勤列表”下方添加一个椭圆形框“修改考勤记录”，并用箭头连接。
画面8：在“考勤列表”左侧添加一个椭圆形框“月报表与日志”，并用箭头连接。
画面9：在SQL工具中查看数据库表结构，当前选中表为“att_attendance_config”。
画面10：在SQL工具中查看表“att_attendance”的结构，显示字段如“id”、“company_id”、“Department_id”等。
画面11：在SQL工具中查看表“att_archive_monthly”的结构，显示字段如“att_archive_monthly_id”、“work_number”等。
画面12：在SQL工具中查看表“att_leave”的结构，显示字段如“leave_type”、“start_time”、“end_time”等。
画面13：在SQL工具中查看表“att_leave”的结构，显示字段如“leave_type”、“start_time”、“end_time”等。
画面14：在SQL工具中查看表“att_company_settings”的结构，显示字段如“company_id”、“is_settings”、“data_punch”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9：
```sql
CREATE TABLE `att_attendance_config` (
  `id` varchar(40) NOT NULL COMMENT '主键ID',
  `user_id` varchar(40) DEFAULT NULL COMMENT '用户ID',
  `company_id` varchar(40) DEFAULT NULL COMMENT '公司ID',
  `Department_id` varchar(40) DEFAULT NULL COMMENT '部门ID',
  `Job_id` varchar(40) DEFAULT NULL COMMENT '岗位ID',
  `att_in_place` varchar(30) DEFAULT NULL COMMENT '考勤地点',
  `att_in_consulate` varchar(120) DEFAULT NULL COMMENT '考勤地点',
  `att_out_place` varchar(30) DEFAULT NULL COMMENT '离岗地点',
  `att_out_consulate` varchar(120) DEFAULT NULL COMMENT '离岗地点',
  `create_by` varchar(40) DEFAULT NULL COMMENT '创建人',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` varchar(40) DEFAULT NULL COMMENT '更新人',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `mobile` varchar(255) DEFAULT NULL COMMENT '手机号',
  `department_name` varchar(40) DEFAULT NULL COMMENT '部门名称',
  `department_code` varchar(40) DEFAULT NULL COMMENT '部门编码',
  `att_in_time` varchar(40) DEFAULT NULL COMMENT '考勤时间',
  `att_out_time` varchar(40) DEFAULT NULL COMMENT '离岗时间',
  `att_in_status` varchar(40) DEFAULT NULL COMMENT '考勤状态',
  `att_out_status` varchar(40) DEFAULT NULL COMMENT '离岗状态',
  `att_in_type` varchar(40) DEFAULT NULL COMMENT '考勤类型',
  `att_out_type` varchar(40) DEFAULT NULL COMMENT '离岗类型',
  `att_in_reason` varchar(40) DEFAULT NULL COMMENT '考勤原因',
  `att_out_reason` varchar(40) DEFAULT NULL COMMENT '离岗原因',
  `att_in_note` varchar(40) DEFAULT NULL COMMENT '考勤备注',
  `att_out_note` varchar(40) DEFAULT NULL COMMENT '离岗备注',
  `att_in_location` varchar(40) DEFAULT NULL COMMENT '考勤地点',
  `att_out_location` varchar(40) DEFAULT NULL COMMENT '离岗地点',
  `att_in_device` varchar(40) DEFAULT NULL COMMENT '考勤设备',
  `att_out_device` varchar(40) DEFAULT NULL COMMENT '离岗设备',
  `att_in_ip` varchar(40) DEFAULT NULL COMMENT '考勤IP',
  `att_out_ip` varchar(40) DEFAULT NULL COMMENT '离岗IP',
  `att_in_mac` varchar(40) DEFAULT NULL COMMENT '考勤MAC',
  `att_out_mac` varchar(40) DEFAULT NULL COMMENT '离岗MAC',
  `att_in_gps` varchar(40) DEFAULT NULL COMMENT '考勤GPS',
  `att_out_gps` varchar(40) DEFAULT NULL COMMENT '离岗GPS',
  `att_in_longitude` varchar(40) DEFAULT NULL COMMENT '考勤经度',
  `att_out_longitude` varchar(40) DEFAULT NULL COMMENT '离岗经度',
  `att_in_latitude` varchar(40) DEFAULT NULL COMMENT '考勤纬度',
  `att_out_latitude` varchar(40) DEFAULT NULL COMMENT '离岗纬度',
  `att_in_height` varchar(40) DEFAULT NULL COMMENT '考勤高度',
  `att_out_height` varchar(40) DEFAULT NULL COMMENT '离岗高度',
  `att_in_speed` varchar(40) DEFAULT NULL COMMENT '考勤速度',
  `att_out_speed` varchar(40) DEFAULT NULL COMMENT '离岗速度',
  `att_in_direction` varchar(40) DEFAULT NULL COMMENT '考勤方向',
  `att_out_direction` varchar(40) DEFAULT NULL COMMENT '离岗方向',
  `att_in_angle` varchar(40) DEFAULT NULL COMMENT '考勤角度',
  `att_out_angle` varchar(40) DEFAULT NULL COMMENT '离岗角度',
  `att_in_distance` varchar(40) DEFAULT NULL COMMENT '考勤距离',
  `att_out_distance` varchar(40) DEFAULT NULL COMMENT '离岗距离',
  `att_in_duration` varchar(40) DEFAULT NULL COMMENT '考勤时长',
  `att_out_duration` varchar(40) DEFAULT NULL COMMENT '离岗时长',
  `att_in_count` varchar(40) DEFAULT NULL COMMENT '考勤次数',
  `att_out_count` varchar(40) DEFAULT NULL COMMENT '离岗次数',
  `att_in_status_code` varchar(40) DEFAULT NULL COMMENT '考勤状态码',
  `att_out_status_code` varchar(40) DEFAULT NULL COMMENT '离岗状态码',
  `att_in_status_name` varchar(40) DEFAULT NULL COMMENT '考勤状态名称',
  `att_out_status_name` varchar(40) DEFAULT NULL COMMENT '离岗状态名称',
  `att_in_status_desc` varchar(40) DEFAULT NULL COMMENT '考勤状态描述',
  `att_out_status_desc` varchar(40) DEFAULT NULL COMMENT '离岗状态描述',
  `att_in_status_color` varchar(40) DEFAULT NULL COMMENT '考勤状态颜色',
  `att_out_status_color` varchar(40) DEFAULT NULL COMMENT '离岗状态颜色',
  `att_in_status_icon` varchar(40) DEFAULT NULL COMMENT '考勤状态图标',
  `att_out_status_icon` varchar(40) DEFAULT NULL COMMENT '离岗状态图标',
  `att_in_status_class` varchar(40) DEFAULT NULL COMMENT '考勤状态类',
  `att_out_status_class` varchar(40) DEFAULT NULL COMMENT '离岗状态类',
  `att_in_status_type` varchar(40) DEFAULT NULL COMMENT '考勤状态类型',
  `att_out_status_type` varchar(40) DEFAULT NULL COMMENT '离岗状态类型',
  `att_in_status_level` varchar(40) DEFAULT NULL COMMENT '考勤状态等级',
  `att_out_status_level` varchar(40) DEFAULT NULL COMMENT '离岗状态等级',
  `att_in_status_order` varchar(40) DEFAULT NULL COMMENT '考勤状态排序',
  `att_out_status_order` varchar(40) DEFAULT NULL COMMENT '离岗状态排序',
  `att_in_status_group` varchar(40) DEFAULT NULL COMMENT '考勤状态分组',
  `att_out_status_group` varchar(40) DEFAULT NULL COMMENT '离岗状态分组',
  `att_in_status_parent` varchar(40) DEFAULT NULL COMMENT '考勤状态父级',
  `att_out_status_parent` varchar(40) DEFAULT NULL COMMENT '离岗状态父级',
  `att_in_status_children` varchar(40) DEFAULT NULL COMMENT '考勤状态子级',
  `

