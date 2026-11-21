# 05-Jdbc数据源数据填充：构造fields

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\05-Jdbc数据源数据填充：构造fields_【海量资源尽在 ubkz.com】.mp4
- 时长 5分23秒（音频 324s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 已经配置好了模拟的这个数据库连接那我们切换到我们创建好的这个模板那在这个模板当中对当前的这些band进行一个删减那我只保留title和detail了好了page header不要了column header不要了这些都删掉都删掉都不要了那我们关注的其实就是一个title以及detail那首先呢对这个title呢做一个静态的一个文件那文本的一个说明比如说呢我们现在
[00:31] 其实就是去查询所有的用户列表OK那接着底下呢其实就是我们要去构造整个的这个数据的一个列表了那构造这个数据列表如何去做那我们一共要分成这么几步首先呢注意首先呢跟各位简单的声明一下就是这个detail里面这个detail里面的数据其实它会动态的根据查询出来的列表
[01:01] 自动的给你进行提价也就是说我们进行编辑的时候只需要构造一行只需要构造一行就够了这个是Detail它的一个特性如果你查到了一个数据列表比如说有10条它就会根据这第一条给你创建出10条数据出来这就是它的一个比较好玩的一个特性注意这个只有在Detail部分才有效
[01:26] 那接下来就是说你如果要构造了这么几个格子那这个格子里面的内容应该填充什么注意这个填充的叫做fields里面填的是一个一个的fields那这个fields那就目前来说其实用的是你查询出来的这个数据库的列也就是数据库的字段能理解吧那接下来我们这个看过了之后看过了之后我们接下来关注的其实就是
[01:54] 这么几点第一点这个Fuse现在你看一下空啊什么都没有啊那怎么办呢有朋友说你右键一看它有创建注意我们现在不去创建它能自动的根据数据库里面把数据库里面的字段全部给我导出来那我们如何去做来各位来看一下首先右键TestCNN当前模板那接着这边有一个叫做Data Set and Query好了点击它这有点慢各位
[02:24] 那先等待一下现在已经进来了那进来了之后注意我们要选择一把那选择什么注意这边呢要选择你当前这个报表当中数据究竟从哪来我们的数据来源是不是要准备从我们搭建好的这个数据库来获取啊数据库名称IHRMDB选择那选过来了之后接下来各位来看我要构造的是对IHRM表里面的一些内容来进行生成那比如说底下
[02:54] 点击了HRM之后里面有所有的表格有很多的表格那这个表格我们关注的就是BS User我们的用户表这个各位应该也能理解没错那这个用户表里面有很多的字段它其实已经帮我们读取出来了那接下来就说你要去查询BS User要去查询里面的值那你要执行什么语句
[03:18] 别忘了既然是让他帮助我们去执行必然是通过Circle语句查询之后得到结果没错吧所以各位我们做到这一步还不行那右边你会发现这有一个红色的叉是因为这个里面的查询语句各位还没写所以接下来我们这边构造的其实就是查询语句当然这个查询语句因人而异因项目而异我写的简单一点我就slag新from bs下划线
[03:46] 那这样以来他就会帮我去根据这条语句查询BS user表得到里面的所有内容好了那接下来我们要怎么做呢就是说目前而言他还不知道我们要查的内容他查询资段究竟有多少究竟有什么那怎么办read fields那我一直点击read fields他会执行这个语句得到你查询出来的所有资段我们一起来试一下走这边在执行那执行成功了之后你会发现当前你执行circle语句
[04:15] 查出来的所有资段底下已经帮我们填充过来了那剩下的事情就是说你可以点击OK没问题但是我觉得你每次只用这么几个属性ID用户名你只用四个你每次都查询slack新服务这么多查一大堆是不是有点浪费效率所以剩下的事情就是对查询出来这些内容做适当的删减比如说这边用户头像我不要了level不要了
[04:46] dpt name我留着company name我留着company id我也留着删掉删掉到这都删掉我点击shift它就帮我批量的勾选了都删掉这样一来我只留了如下这么几个字段好了这样一来我们点击OK各位去看一下刚才的这fields里面fields里面你会发现已经有我们得到的这几个我们的属性或者我们的字段类型了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 JasperReports Studio 中设计一个包含标题、数据表和字段区域的报表，并配置数据源和查询。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperReports Studio 中打开名为 testConn.jrxml 的报表文件，界面显示设计视图，包含 Title、Detail 1、Summary 三个带状区域，左侧为项目资源管理器，右侧为属性面板。
画面2：在标题带（Band: Title）中拖放一个文本框，文本框内显示“标题”。
画面3：在标题带中选中文本框，属性面板显示其布局为 Free Layout，高度为 79 px，分隔类型为 Stretch。
画面4：切换到画图工具，创建一个包含“id”和“用户名”列的表格。
画面5：切换到画图工具，创建一个包含“fields”文本框的区域。
画面6：在画图工具中，将“fields”文本框复制并排列成一行四个。
画面7：在画图工具中，调整“fields”文本框的大小和位置。
画面8：在 JasperReports Studio 中打开“Dataset and Query Dialog”，选择“java Bean”作为查询语言。
画面9：在“Dataset and Query Dialog”中，选择“mysql”数据库，查询语句为“select * from bs_user”。
画面10：在“Dataset and Query Dialog”中，查看并选择“bs_user”表的字段，包括 id, mobile, username, password, enable_state, create_time, department_id, time_of_entry, form_of_employment。
画面11：在 JasperReports Studio 中，点击“OK”按钮确认数据源和查询配置。
画面12：在 JasperReports Studio 中，点击“Preview”按钮预览报表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8：
Language: java Bean
Query: java Bean
No Metadata. Double click to refresh.

画面9：
Language: sql
Query: java Bean
select * from bs_user

画面10：
Language: sql
Query: java Bean
select * from bs_user
Field Name	Class Type	Description	Time zone	Column na...	Column la...	Column in...	Properties
id	java.lang.String		...	...	...	...
mobile	java.lang.String		...	...	...	...
username	java.lang.String		...	...	...	...
password	java.lang.String		...	...	...	...
enable_state	java.lang.String		...	...	...	...
create_time	java.lang.String		...	...	...	...
department_id	java.lang.String		...	...	...	...
time_of_entry	java.lang.String		...	...	...	...
form_of_employment	java.lang.String		...	...	...	...

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

