# 画面线理解：04-考勤设置：需求分析和表介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\04-考勤设置：需求分析和表介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:02, 02:01, 02:36, 04:27, 04:45, 05:42, 06:34, 06:44, 07:08, 07:42, 08:03, 08:33, 09:16, 09:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:30:14

1) 这一组画面整体在讲什么（一句话）：
演示并讲解考勤系统的“加班设置”功能配置，包括前端界面操作和后端数据库表结构设计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT第2页，标题为“2.1 需求分析”，内容涉及考勤系统需求，下方弹窗为“设置”界面，当前选中“出勤设置”，部门为“研发部”，出勤时间为05:15-17:30。
画面2：前端界面，弹窗“设置”中“请假设置”标签页被选中，部门为“研发部”，下方列出“假期类型”及其“是否可用”开关，如“年假”、“事假”等均开启。
画面3：前端界面，弹窗“设置”中“请假设置”标签页，展示“假期类型”列表，包括“年假”、“事假”、“病假”、“婚假”、“丧假”、“产假”、“奖励假”、“陪产假”、“探亲假”、“工伤假”、“病假”、“产检假”、“长期病假”、“测试用”等，所有开关均开启。
画面4：前端界面，弹窗“设置”中“加班设置”标签页，显示“加班规则”选项，包括“工作日可申请加班”、“休息日可申请加班”、“法定节假日可申请”，均未开启，下方有“打卡验证”和“开启补偿”开关，以及“调休有效期”设置。
画面5：前端界面，弹窗“设置”中“加班设置”标签页，用户已开启“休息日可申请加班”选项，其他选项未开启。
画面6：数据库管理工具（SQLyog）界面，显示“attendance”数据库下的“atte_extra_duty_config”表结构，包含字段如“id”、“company_id”、“department_id”、“create_by”等，以及“atte_extra_duty_rule”表结构。
画面7：前端界面，弹窗“设置”中“加班设置”标签页，显示“加班规则”选项，包括“工作日可申请加班”、“休息日可申请加班”、“法定节假日可申请”，均未开启。
画面8：PPT页面，展示“薪资管理”、“社保管理”、“考勤管理”三个模块的流程图，其中“薪资管理”指向“社保管理”和“考勤管理”，并标注“制作个人薪资”、“当月社保扣款”、“当月公积金扣款”、“考勤记录”等。
画面9：桌面多窗口视图，展示多个开发工具窗口，包括“day15.pdf”、“list.vue”、“ihrm_parent”、“day15.md”、“Postman”、“无标题 - 画图”等。
画面10：PPT页面，展示“考勤设置表”、“加班请假的配置表”、“请调配置表”等，用红色箭头指向“atte_extra_duty_config”、“atte_extra_duty_rule”、“atte_extra_duty_config”等表名。
画面11：PPT页面，展示“考勤设置表”、“加班请假的配置表”、“请调配置表”等，用红色箭头指向“atte_extra_duty_config”、“atte_extra_duty_rule”、“atte_extra_duty_config”等表名，下方标注“请调配置表”。
画面12：前端界面，弹窗“设置”中“加班设置”标签页，显示“加班规则”选项，包括“工作日可申请加班”、“休息日可申请加班”、“法定节假日可申请”，均未开启。
画面13：数据库管理工具（SQLyog）界面，显示“atte_extra_duty_rule”表的创建语句，包含字段如“id”、“company_id”、“department_id”、“rule_name”、“rule_content”、“rule_start_time”、“rule_end_time”、“is_enable”等，以及“PRIMARY KEY (id) USING BTREE”。
画面14：课程PPT第2页，标题为“2. 考勤设置”，内容与画面1相同，下方弹窗为“设置”界面，当前选中“出勤设置”，部门为“研发部”，出勤时间为05:15-17:30。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6 SQL：
```sql
SELECT COUNT(CASE WHEN adt_status = 1 THEN 1 END) as '正常出勤',
       COUNT(CASE WHEN adt_status = 2 THEN 1 END) as '迟到',
       COUNT(CASE WHEN adt_status = 3 THEN 1 END) as '早退',
       COUNT(CASE WHEN adt_status = 4 THEN 1 END) as '旷工',
       COUNT(CASE WHEN adt_status = 5 THEN 1 END) as '加班',
       COUNT(CASE WHEN adt_status = 6 THEN 1 END) as '请假',
       COUNT(CASE WHEN adt_status = 7 THEN 1 END) as '调休',
       COUNT(CASE WHEN adt_status = 8 THEN 1 END) as '出差',
       COUNT(CASE WHEN adt_status = 9 THEN 1 END) as '病假',
       COUNT(CASE WHEN adt_status = 10 THEN 1 END) as '事假',
       COUNT(CASE WHEN adt_status = 11 THEN 1 END) as '婚假',
       COUNT(CASE WHEN adt_status = 12 THEN 1 END) as '丧假',
       COUNT(CASE WHEN adt_status = 13 THEN 1 END) as '产假',
       COUNT(CASE WHEN adt_status = 14 THEN 1 END) as '陪产假',
       COUNT(CASE WHEN adt_status = 15 THEN 1 END) as '探亲假',
       COUNT(CASE WHEN adt_status = 16 THEN 1 END) as '工伤假',
       COUNT(CASE WHEN adt_status = 17 THEN 1 END) as '病假',
       COUNT(CASE WHEN adt_status = 18 THEN 1 END) as '产检假',
       COUNT(CASE WHEN adt_status = 19 THEN 1 END) as '长期病假',
       COUNT(CASE WHEN adt_status = 20 THEN 1 END) as '测试用'
FROM attendance.attendance_daily_config;
```
画面13 SQL：
```sql
CREATE TABLE `atte_extra_duty_rule` (
  `id` varchar(40) NOT NULL COMMENT '主键',
  `company_id` varchar(60) DEFAULT NULL COMMENT '公司ID',
  `department_id` varchar(60) DEFAULT NULL COMMENT '部门ID',
  `rule_name` varchar(60) DEFAULT NULL COMMENT '规则名称',
  `rule_content` varchar(100) DEFAULT NULL COMMENT '规则内容',
  `rule_start_time` time DEFAULT NULL COMMENT '规则生效开始时间',
  `rule_end_time` time DEFAULT NULL COMMENT '规则生效结束时间',
  `is_enable` int(10) DEFAULT NULL COMMENT '是否开启 0开始 1关闭',
  `create_by` varchar(60) DEFAULT NULL COMMENT '创建人',
  `update_by` varchar(60) DEFAULT NULL COMMENT '更新人',
  `create_date` datetime DEFAULT NULL COMMENT '创建时间',
  `update_date` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='加班规则';
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：架构图/流程图结构：
- “薪资管理”指向“社保管理”和“考勤管理”。
- “社保管理”指向“当月社保扣款”。
- “考勤管理”指向“当月公积金扣款”和“考勤记录”。
- “制作个人薪资”指向“当月社保扣款”、“当月公积金扣款”、“考勤记录”。
- “根据用户id和考勤年月查询社保记录”指向“社保管理”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
