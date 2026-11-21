# 画面线理解：14-考勤列表：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\14-考勤列表：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:01, 02:51, 03:58, 06:16, 07:02, 07:59, 09:32, 11:05, 12:28, 13:08, 14:23, 15:48, 16:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:38:51

1) 这一组画面整体在讲如何在 Java Spring Boot 项目中，通过服务层（AttService）调用数据访问层（Dao）查询用户考勤数据，并将结果封装为业务对象（AttItemBO）返回。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了数据库表结构和用户权限，重点是 `attc_attendance` 表的字段定义和权限配置。
画面2: 展示了 `AttService` 类中 `getAttDate` 方法的初步代码，包含对 `CompanySettingsDao` 的依赖注入。
画面3: 展示了 `UserDao` 接口定义，包含 `findByMobile` 和 `findByCompanyId` 方法。
画面4: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建分页查询。
画面5: 展示了 `AttService` 中 `getAttDate` 方法的代码，添加了分页查询逻辑。
画面6: 展示了 `AttService` 中 `getAttDate` 方法的代码，添加了分页查询逻辑。
画面7: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面8: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面9: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面10: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面11: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面12: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面13: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。
画面14: 展示了 `AttService` 中 `getAttDate` 方法的代码，开始构建业务对象 `AttItemBO`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```sql
SELECT COUNT(*) as c,
       COUNT(CASE WHEN att_status = '1' THEN 1 END) as t,
       COUNT(CASE WHEN att_status = '2' THEN 1 END) as a,
       COUNT(CASE WHEN att_status = '3' THEN 1 END) as d,
       COUNT(CASE WHEN att_status = '4' THEN 1 END) as s,
       COUNT(CASE WHEN att_status = '5' THEN 1 END) as c,
       COUNT(CASE WHEN att_status = '6' THEN 1 END) as f,
       COUNT(CASE WHEN att_status = '7' THEN 1 END) as n,
       COUNT(CASE WHEN att_status = '8' THEN 1 END) as t,
       COUNT(CASE WHEN att_status = '9' THEN 1 END) as r,
       COUNT(CASE WHEN att_status = '10' THEN 1 END) as p,
       COUNT(CASE WHEN att_status = '11' THEN 1 END) as l,
       COUNT(CASE WHEN att_status = '12' THEN 1 END) as v,
       COUNT(CASE WHEN att_status = '13' THEN 1 END) as w,
       COUNT(CASE WHEN att_status = '14' THEN 1 END) as x,
       COUNT(CASE WHEN att_status = '15' THEN 1 END) as y,
       COUNT(CASE WHEN att_status = '16' THEN 1 END) as z,
       COUNT(CASE WHEN att_status = '17' THEN 1 END) as u,
       COUNT(CASE WHEN att_status = '18' THEN 1 END) as i,
       COUNT(CASE WHEN att_status = '19' THEN 1 END) as o,
       COUNT(CASE WHEN att_status = '20' THEN 1 END) as p,
       COUNT(CASE WHEN att_status = '21' THEN 1 END) as q,
       COUNT(CASE WHEN att_status = '22' THEN 1 END) as r,
       COUNT(CASE WHEN att_status = '23' THEN 1 END) as s,
       COUNT(CASE WHEN att_status = '24' THEN 1 END) as t,
       COUNT(CASE WHEN att_status = '25' THEN 1 END) as u,
       COUNT(CASE WHEN att_status = '26' THEN 1 END) as v,
       COUNT(CASE WHEN att_status = '27' THEN 1 END) as w,
       COUNT(CASE WHEN att_status = '28' THEN 1 END) as x,
       COUNT(CASE WHEN att_status = '29' THEN 1 END) as y,
       COUNT(CASE WHEN att_status = '30' THEN 1 END) as z,
       COUNT(CASE WHEN att_status = '31' THEN 1 END) as a,
       COUNT(CASE WHEN att_status = '32' THEN 1 END) as b,
       COUNT(CASE WHEN att_status = '33' THEN 1 END) as c,
       COUNT(CASE WHEN att_status = '34' THEN 1 END) as d,
       COUNT(CASE WHEN att_status = '35' THEN 1 END) as e,
       COUNT(CASE WHEN att_status = '36' THEN 1 END) as f,
       COUNT(CASE WHEN att_status = '37' THEN 1 END) as g,
       COUNT(CASE WHEN att_status = '38' THEN 1 END) as h,
       COUNT(CASE WHEN att_status = '39' THEN 1 END) as i,
       COUNT(CASE WHEN att_status = '40' THEN 1 END) as j,
       COUNT(CASE WHEN att_status = '41' THEN 1 END) as k,
       COUNT(CASE WHEN att_status = '42' THEN 1 END) as l,
       COUNT(CASE WHEN att_status = '43' THEN 1 END) as m,
       COUNT(CASE WHEN att_status = '44' THEN 1 END) as n,
       COUNT(CASE WHEN att_status = '45' THEN 1 END) as o,
       COUNT(CASE WHEN att_status = '46' THEN 1 END) as p,
       COUNT(CASE WHEN att_status = '47' THEN 1 END) as q,
       COUNT(CASE WHEN att_status = '48' THEN 1 END) as r,
       COUNT(CASE WHEN att_status = '49' THEN 1 END) as s,
       COUNT(CASE WHEN att_status = '50' THEN 1 END) as t,
       COUNT(CASE WHEN att_status = '51' THEN 1 END) as u,
       COUNT(CASE WHEN att_status = '52' THEN 1 END) as v,
       COUNT(CASE WHEN att_status = '53' THEN 1 END) as w,
       COUNT(CASE WHEN att_status = '54' THEN 1 END) as x,
       COUNT(CASE WHEN att_status = '55' THEN 1 END) as y,
       COUNT(CASE WHEN att_status = '56' THEN 1 END) as z,
       COUNT(CASE WHEN att_status = '57' THEN 1 END) as a,
       COUNT(CASE WHEN att_status = '58' THEN 1 END) as b,
       COUNT(CASE WHEN att_status = '59' THEN 1 END) as c,
       COUNT(CASE WHEN att_status = '60' THEN 1 END) as d,
       COUNT(CASE WHEN att_status = '61' THEN 1 END) as e,
       COUNT(CASE WHEN att_status = '62' THEN 1 END) as f,
       COUNT(CASE WHEN att_status = '63' THEN 1 END) as g,
       COUNT(CASE WHEN att_status = '64' THEN 1 END) as h,
       COUNT(CASE WHEN att_status = '65' THEN 1 END) as i,
       COUNT(CASE WHEN att_status = '66' THEN 1 END) as j,
       COUNT(CASE WHEN att_status = '67' THEN 1 END) as k,
       COUNT(CASE WHEN att_status = '68' THEN 1 END) as l,
       COUNT(CASE WHEN att_status = '69' THEN 1 END) as m,
       COUNT(CASE WHEN att_status = '70' THEN 1 END) as n,
       COUNT(CASE WHEN att_status = '71' THEN 1 END) as o,
       COUNT(CASE WHEN att_status = '72' THEN 1 END) as p,
       COUNT(CASE WHEN att_status = '73' THEN 1 END) as q,
       COUNT(CASE WHEN att_status = '74' THEN 1 END) as r,
       COUNT(CASE WHEN att_status = '75' THEN 1 END) as s,
       COUNT(CASE WHEN att_status =
