# 画面线理解：1.18 系统数据结构

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.18 系统数据结构_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 02:41, 03:35, 04:30, 08:05, 08:52, 09:32, 09:57, 11:06, 11:36, 12:24, 12:56, 13:08, 13:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:48:31

1) 这一组画面整体在讲什么（一句话）：
展示一个名为“cold”的数据库系统的数据结构，包括用户库、业务库、定时任务库等模块下的多个表的字段定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“4.1 用户库 (cold-user)”下的“4.1.1 用户表”，表名为 sys_user，包含 user_id, username, password, salt, email, mobile, status, create_user_id, create_time 等字段。
画面2：展示“4.2 业务库 (cold)”下的“4.2.1 公司表”，表名为 cz_company，包含 id, company, abbreviation, companyNumber, companyAddress, companyPhone, managementName, managementPhone, leader, leaderPhone, message, webAddress, companyType, createdTime, updateTime 等字段。
画面3：展示“4.2.1 公司表”的字段详情，包含 companyType, createdTime, updateTime 字段的定义。
画面4：展示“4.2.1 公司表”的字段详情，包含 companyType, createdTime, updateTime 字段的定义。
画面5：展示“4.2.2 仓库表”，表名为 cz_warehouse，包含 houseCode, houseName, houseAddress, houseType, companyId, companyName, principalTel, longitude, latitude, areaSize, houseStatus, createdTime, updateTime 等字段。
画面6：展示“4.2.4 设备表”，表名为 cz_monitor，包含 id, userName, userPhone, monitorState, hostId, hostCode, hostName 等字段。
画面7：展示“4.2.5 实时指标表”，表名为 cz_message_realtime，包含 meterCode, meterName, hostId, hostCode, hostName, houseId, houseName, companyId 等字段。
画面8：展示“4.2.5 实时指标表”的字段详情，包含 id, userName, userPhone, monitorState, hostId, hostCode, hostName, createdTime, updateTime 等字段。
画面9：展示“4.3 定时任务库 (cold-job)”下的“4.3.1 CRON触发器”，表名为 QRTZ_CRON_TRIGGERS，包含 SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP, CRON_EXPRESSION, TIME_ZONE_ID 等字段。
画面10：展示“4.3.4 锁表”，表名为 QRTZ_LOCKS，包含 SCHED_NAME, LOCK_NAME 等字段。
画面11：展示“4.3.7 触发器表”，表名为 QRTZ_TRIGGERS，包含 SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP, JOB_NAME, JOB_GROUP, DESCRIPTION, NEXT_FIRE_TIME 等字段。
画面12：展示“4.3.10 调度日志表”，表名为 schedule_job_log，包含 log_id, job_id, bean_name, params, status, error, times, create_time 等字段。
画面13：展示“4.3 定时任务库 (cold-job)”下的“4.3.1 CRON触发器”，表名为 QRTZ_CRON_TRIGGERS，包含 SCHED_NAME, TRIGGER_NAME, TRIGGER_GROUP, CRON_EXPRESSION, TIME_ZONE_ID 等字段。
画面14：展示“4.2.4 设备表”，表名为 cz_monitor，包含 id, userName, userPhone, monitorState, hostId, hostCode, hostName, createdTime, updateTime 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
表名：sys_user
| 名称 | 类型 | 长度 | 小数点 | 是否为NULL | 主键 | 注释 |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | bigint | 20 | 0 | 1 | 1 | 主键Id |
| username | varchar | 50 | 0 | 1 | 0 | 用户名 |
| password | varchar | 100 | 0 | 0 | 0 | 密码 |
| salt | varchar | 20 | 0 | 0 | 0 | 盐 |
| email | varchar | 100 | 0 | 0 | 0 | 邮箱 |
| mobile | varchar | 100 | 0 | 0 | 0 | 手机号 |
| status | tinyint | 4 | 0 | 0 | 0 | 状态：0：禁用，1：正常 |
| create_user_id | bigint | 20 | 0 | 0 | 0 | 创建者ID |
| create_time | datetime | 0 | 0 | 0 | 0 | 创建时间 |

画面2：
表名：cz_company
| 名称 | 类型 | 长度 | 小数点 | 是否为NULL | 主键 | 注释 |
| --- | --- | --- | --- | --- | --- | --- |
| id | varchar | 50 | 0 | 1 | 1 | 主键 |
| company | varchar | 100 | 0 | 0 | 0 | 公司名称 |
| abbreviation | varchar | 50 | 0 | 0 | 0 | 公司简称 |
| companyNumber | varchar | 50 | 0 | 0 | 0 | 企业编号 |
| companyAddress | varchar | 100 | 0 | 0 | 0 | 企业地址 |
| companyPhone | varchar | 20 | 0 | 0 | 0 | 公司电话 |
| managementName | varchar | 50 | 0 | 0 | 0 | 质量管理员 |
| managementPhone | varchar | 20 | 0 | 0 | 0 | 联系电话 |
| leader | varchar | 50 | 0 | 0 | 0 | 负责人姓名 |
| leaderPhone | varchar | 20 | 0 | 0 | 0 | 负责人电话 |
| message | varchar | 255 | 0 | 0 | 0 | 备注 |

画面3：
表名：cz_company
| 名称 | 类型 | 长度 | 小数点 | 是否为NULL | 主键 | 注释 |
| --- | --- | --- | --- | --- | --- | --- |
| webAddress | varchar | 100 | 0 | 0 | 0 | 网站 |
| companyType | varchar | 20 | 0 | 0 | 0 | 企业类型 |
| createdTime | timestamp | 0 | 0 | 1 | 0 | 创建时间, CURRENT_TIMESTAMP |
| updateTime | timestamp | 0 | 0 | 1 | 0 | 修改时间, CURRENT_TIMESTAMP, 根据当前时间戳更新 |

画面4：
表名：cz_company
| 名称 | 类型 | 长度 | 小数点 | 是否为NULL | 主键 | 注释 |
| --- | --- | --- | --- | --- | --- | --- |
| webAddress | varchar | 100 | 0 | 0 | 0 | 网站 |
| companyType | varchar | 20 | 0 | 0 | 0 | 企业类型 |
| createdTime | timestamp | 0 | 0 | 1 | 0 | 创建时间, CURRENT_TIMESTAMP |
| updateTime | timestamp | 0 | 0 | 1 | 0 | 修改时间, CURRENT_TIMESTAMP, 根据当前时间戳更新 |

画面5：
表名：cz_warehouse
| 名称 | 类型 | 长度 | 小数点 | 是否为NULL | 主键 | 注释 |
| --- | --- | --- | --- | --- | --- | --- |
| houseCode | varchar | 50 | 0 | 1 | 0 | 仓库编码 |
| houseName | varchar | 100 | 0 | 0 | 0 | 仓库名称 |
| houseAddress | varchar | 255 | 0 | 0 | 0 | 仓库地址 |
| houseType | int | 2 | 0 | 0 | 0 | 仓库类型：1:冷库，2:常温 |
| companyId | varchar | 50 | 0 | 0 | 0 | 所属公司id |
| companyName | varchar | 100 | 0 | 0 | 0 | 公司名称 |
| principalTel | varchar | 20 | 0 | 0 | 0 | 负责人电话 |
| longitude | decimal | 10 | 6 | 0 | 0 | 经度 |
| latitude | decimal | 10 | 6 | 0 | 0 | 纬度 |
| areaSize | double | 6 | 0 | 0 | 0 | 仓库面积 |
| houseStatus | int | 2 | 0 | 0 | 0 | 状态：1:正常,0:空库 |
| createdTime | timestamp | 0 | 0 | 1 |
