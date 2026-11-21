# 22-Activiti流程变量-Global全局变量的注意事项及小结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\22-Activiti流程变量-Global全局变量的注意事项及小结_【海量资源尽在 ubkz.com】.mp4
- 时长 3分6秒（音频 187s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 全局变量,Global类型的变量它在实际操作中我们要注意的一些事项中间关于它的测试过程我们基本上都已经测完了我们现在接着往后走如果UAL表达式流程变量不存在报错如果我们的表达式中流程变量为空为空,long流程
[00:26] 不按UEL表达式去执行则流程结束如果表达式都不符合了见那我们的流程直接结束或者是我们连线不设置条件那这个时候会按我们的这个俯落需要小的这个线去走好这是我们在这里头其实所看见的一些注意的点那我们再来看一下就是关于我们的这个流程变量
[00:54] 它真正在操作的时候所引起的这个表的变化对吧那刚才我们其实前面已经分析过那我们在这个actru variable这个表中会去记录当前我们的流程变量那这个是我们流程变量存放的这个表对吧但是如果我们对应的真正放的是具体的这个流程变量具体的这个取值我们将来
[01:23] 历史记录中也可以去查看我们的sathivarinstance这个表当然如果我们设置的是一个如果我们在这里面设置的是一个POGO类型的话那我们这个POGO类型呢也会在我们的这个beta rate这个表中给我们存储一份对吧就是在这个表中也会将真正的这个变量的值保存起来对吧这个是因为我应该是可能把这个库清了
[01:53] 所以在这个表中其实也会存着一封这是我们之前说过的这个部分介绍清楚了那我们基本上给各位就把我们的这个全局类型变量它的一些注意事项以及它背后所操作的这个数据库表给大家简单的介绍了一下当然这里头除了除了这个表我们这边还有具体的这样的一些字段
[02:22] 这些字段呢各位同学可以去好好去观察一下去看一下其中这里面就说到了一个如果是我们存储一个POGO类型的话那我们serisable类型呢所对应的这个变量真正所存储的值我们还要去看一下叫做ACTGEBitarray这个表对吧这个表中也一样会存储它的ID好这是我们在这边呢
[02:51] 把我们的整个这个全局类型的这个变量啊四种方式以及它的注意事项以及它背后所操作的数据库表给各位啊大概做了一个这样的整洁啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

