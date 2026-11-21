# 08-考勤数据导入：概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\08-考勤数据导入：概述_【海量资源尽在 ubkz.com】.mp4
- 时长 3分46秒（音频 226s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们把这个需求呢简单的和各位说了一下那接下来呢我们就开始按照咱们画的这张图案把这几个功能的全部给它实现出来那其实这里面的功能呢咱们虽然写了三块但是其实一共有四块这四块呢第一个就是我们要做一个考勤数据的一个导入那接下来呢第二块就是去展示我们这个考勤列表
[00:24] 那接着第三块就是去修改我的考勤数据那接着第四块就是去完成我们的数据报表或者数据归档的相关操作那好了我们一个一个来看首先呢就这个考勤数据的一个导入那在我们的讲义上呢这边也有一个小小的说明就是对于这个数据导入而言
[00:47] 那在一个人力资源管理系统当中呢,考勤数据是比较重要的一个部分内容,那这个数据呢从哪来,往往是通过这么两个方面来获取到的,第一个呢就是将我们的系统和考勤机给它打通,也就是通过我们的系统直接能够访问考勤机的数据库,但是呢这种方案呢它是有门槛的,就是说呢你这个考勤机呢必须有它的网络的支持,
[01:14] 并且呢这个烤琴机呢咱们只能实现某一个型号或者某两个型号所以第一种方式它是有门槛而且门槛比较高那还有呢就是第二种方式第二种方式呢就是将烤琴机的数据先导出来生成一个固定格式的Excel那接下来呢再把这个Excel导入到我们的系统当中这种方式呢
[01:39] 就是一个折中的方案当然了现在大部分的企业呢往往是用的是第二种方案居多一些所以我们这边要做这个考前数据导入也是通过Excel进行数据的一个导入那这边呢就涉及到一个小小的问题就是你导入这个数据啊必须是一个固定格式的这个格式必须要正确那我们才能在系统当中进行解析没错啦好了那接着我们来看一下在今天的这个资料当中
[02:12] 给各位准备好了这么一个Excel文件这个Excel文件呢就是咱们需要的一些格式好了各位来看这边呢这个格式是这样的员工姓名手机号公号上班时间下班时间好了当中这个时间呢我们可以给它改一下这个17年太不靠谱了好了上班时间呢我们就改成比如说19年好了0719年07来来多少呀2019
[02:53] -7-比如说1号哎8点半打卡好了这边呢就是1号6点半打卡OKOK好那这样一来呢咱们这个基本的格式呢就已经跟各位简单的交代了一下好了那接下来所有的员工数据呢都需要通过我们的人事来进行操作那人事呢需要把考勤机里面的数据
[03:32] 给它生成符合我们这种规定格式的Excel那在我们系统当中就可以把这个Excel导入到系统当中解析成一条一条的考勤数据生成到我们的系统当中

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Excel 导入考勤数据到人力资源系统，涉及数据库表结构、流程图、代码结构和实际数据操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表结构，包含 SQL 语句和字段信息。
画面2：展示考勤管理的流程图，说明数据从考勤机导入到系统的过程。
画面3：展示 PPT 页面，介绍考勤管理模块和数据导入部分。
画面4：展示 PPT 页面，继续介绍数据导入方案，提及 Controller 代码。
画面5：再次展示考勤管理流程图。
画面6：展示项目目录结构，包含 dao、domain、Service 等文件夹。
画面7：展示 day15.pdf 文件和 demos.xlsx 文件，后者正在被 Excel 打开。
画面8：展示 Excel 表格，包含员工姓名、手机号、工号、上班时间、下班时间等列。
画面9：展示 Excel 表格，数据已更新，下班时间从 2017-12-12 18:30 变为 2019-7-1 18:30。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```sql
CREATE TABLE `att_company_settings` (
  `company_id` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_name` varchar(40) NOT NULL DEFAULT '',
  `data_type` varchar(40) NOT NULL DEFAULT '',
  `data_value` varchar(40) NOT NULL DEFAULT '',
  `data_desc` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status` varchar(40) NOT NULL DEFAULT '',
  `data_match` varchar(40) NOT NULL DEFAULT '',
  `data_status`

