# 画面线理解：22-Activiti流程变量-Global全局变量的注意事项及小结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\22-Activiti流程变量-Global全局变量的注意事项及小结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:06, 00:11, 00:13, 00:53, 00:59, 01:18, 01:33, 01:44, 01:49, 01:52, 01:56, 02:09, 02:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:07:02

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中流程变量的注意事项及操作数据库表的 SQL 语句。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“3.5.5 注意事项”，内容包括 UEL 表达式中流程变量名不存在则报错、流程变量值为空 NULL、UEL 表达式不符合条件、连线不设置条件会走 flow 序号小的那条线等四点注意事项。
画面2：PPT 页面“3.5.5 注意事项”，内容与画面1相同，鼠标光标在“3.5.5 注意事项”标题上。
画面3：PPT 页面“3.5.4 测试”和“3.5.5 注意事项”，“3.5.4 测试”部分显示正常测试和异常测试的条件，鼠标光标在“3.5.5 注意事项”标题上。
画面4：PPT 页面“3.5.5 注意事项”，内容与画面1相同，鼠标光标在“3.5.5 注意事项”标题上。
画面5：PPT 页面“3.5.5 注意事项”，内容与画面1相同，鼠标光标在“3.5.5 注意事项”标题上。
画面6：PPT 页面“操作数据库表”，内容包括设置流程变量会插入当前执行和历史流程变量表的说明，以及两个 SQL 查询语句：SELECT * FROM act_ru_variable 和 SELECT * FROM act_hi_varinst。
画面7：PPT 页面“操作数据库表”，内容与画面6相同，鼠标光标在“操作数据库表”标题上。
画面8：PPT 页面“操作数据库表”，内容与画面6相同，鼠标光标在“操作数据库表”标题上。
画面9：SQLyog 数据库客户端界面，显示 SQL 语句：drop database activiti; create database activiti; act_ge_bytearray; act_ru_variable。消息栏显示“1 row(s) affected”。
画面10：SQLyog 数据库客户端界面，显示 SQL 语句：drop database activiti; create database activiti; act_ge_bytearray; act_ru_variable。同时弹出 SQLyog 的“Getting started”窗口。
画面11：SQLyog 数据库客户端界面，显示 SQL 语句：drop database activiti; create database activiti; act_ge_bytearray; act_ru_variable。鼠标光标在“Objects”标签页上。
画面12：PPT 页面“操作数据库表”，内容与画面6相同，鼠标光标在“操作数据库表”标题上。
画面13：PPT 页面“操作数据库表”，内容与画面6相同，鼠标光标在“操作数据库表”标题上。
画面14：PPT 页面“操作数据库表”，内容与画面6相同，鼠标光标在“操作数据库表”标题上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6、7、8、12、13、14：
SELECT * FROM act_ru_variable #当前流程变量表
记录当前运行流程实例可使用的流程变量，包括 global 和 local 变量
Id_ : 主键
Type_ : 变量类型
Name_ : 变量名称
Execution_id_ : 所属流程实例执行 id, global 和 local 变量都存储
Proc_inst_id_ : 所属流程实例 id, global 和 local 变量都存储
Task_id_ : 所属任务 id, local 变量存储
Bytearray_ : serializable 类型变量存储对应 act_ge_bytearray 表的 id
Double_ : double 类型变量值
Long_ : long 类型变量值
Text_ : text 类型变量值
SELECT * FROM act_hi_varinst #历史流程变量表
记录所有已创建的流程变量，包括 global 和 local 变量
字段意义参考当前流程变量表。

画面9：
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、2、3、4、5、6、7、8、12、13、14：
标题：3.5.5 注意事项
内容：
1. 如果 UEL 表达式中流程变量名不存在则报错。
2. 如果 UEL 表达式中流程变量值为空 NULL，流程不按 UEL 表达式去执行，而流程结束。
3. 如果 UEL 表达式都不符合条件，流程结束。
4. 如果连线不设置条件，会走 flow 序号小的那条线。

画面6、7、8、12、13、14：
标题：操作数据库表
内容：
设置流程变量会在当前执行流程变量表插入记录，同时也会在历史流程变量表也插入记录。
SELECT * FROM act_ru_variable #当前流程变量表
记录当前运行流程实例可使用的流程变量，包括 global 和 local 变量
Id_ : 主键
Type_ : 变量类型
Name_ : 变量名称
Execution_id_ : 所属流程实例执行 id, global 和 local 变量都存储
Proc_inst_id_ : 所属流程实例 id, global 和 local 变量都存储
Task_id_ : 所属任务 id, local 变量存储
Bytearray_ : serializable 类型变量存储对应 act_ge_bytearray 表的 id
Double_ : double 类型变量值
Long_ : long 类型变量值
Text_ : text 类型变量值
SELECT * FROM act_hi_varinst #历史流程变量表
记录所有已创建的流程变量，包括 global 和 local 变量
字段意义参考当前流程变量表。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
