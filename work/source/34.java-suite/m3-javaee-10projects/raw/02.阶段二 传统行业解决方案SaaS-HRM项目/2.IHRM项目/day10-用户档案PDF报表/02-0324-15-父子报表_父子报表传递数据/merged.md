# 15-父子报表：父子报表传递数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\15-父子报表：父子报表传递数据_【海量资源尽在 ubkz.com】.mp4
- 时长 12分9秒（音频 729s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的和各位说了一下这个父子报表它的一个作用那其实呢通过父报表它有没有数据其实也可以分成这么两种父子报表的形式第一种呢就是它不显示任何数据一个数据不显示它主要是作为一个载体那把一个一个的子报表是不是填充到父报表当中以这种形式来进行体现好了那接着还有一种就是它显示一部分数据那另一部分数据呢
[00:31] 其实很难构造了那这个时候呢另一部分数据就通过子报表来进行弥补这个应该各位都能理解那接下来呢我们就可以写一个案例一起来看一下这个子副报表应该如何去做那我们这个案例呢其实就是使用的是第二种方式主要让各位来看一下这个父子报表它的一个制作的过程还里面的一些细节问题那针对这种情况我来一个案例这个案例呢也跟各位做一个简单的介绍就以这个为例了
[01:01] 那现在复报表是一个载体那我呢先抽取一个子报表那这个子报表的功能我以谁为为例呢我就以刚才的这个差的图形差图形那我现在要做的事情呢就是去创建一个复报表把我们刚才的那个差的图形给它引入到复报表当中进行展示其实就可以了这个各位应该也能理解没错吧好了那接下来回到我们的studio那接下来呢在这边右键去创建一个report
[01:31] 那注意这回我创建的其实是一个副报表那这个副报表当中要添加一个chart图形的子报表各位应该都能理解好了点击next在这边创建一个副报表了我叫做men01吧叫做men01OK那点击finish那这样一来呢我这个副报表呢其实已经创建成功了
[02:00] 那接下来呢删除一些不必要的一些内容比如说呢这个page header我不想要了比如说呢column header我不想要了我只留detail部分我只留detail部分那我要做的事情其实就是这边修改一下我们的title添加一个静态的标题拿过来父子报表好了来一杠我们现在解决的是作为载体里面填充填充
[02:31] 我们的图形chartOK拉的长一点那这样一来呢我们的标题部分已经有了当然了把这个标题呢它还是有点长啊有点宽啊有点高OK做一个修改那这样一来我们这个标题已经构造好了那接下来在title部分我们去引入或者去创建一个子报表给它拿过来那怎么往这个mint当中添加子报表呢那如何去做很简单注意找到这个plant
[03:09] 我们找到所有的这些组件那这个组件里面你往下拖往下拖其中有个叫做sub report就是往里填一个子报表填进去那怎么填注意拖拽过来左键拖拽过来那拖拽过来之后这边就让你去选择子报表的一些内容了当然如果说你子报表还没写你就create一个new report就是创建一个新的子报表那我现在已经存在那我去找到我们刚才
[03:38] 创建charts图形的这个子报表是不是就可以了所以接下来我们开始去找那从哪找这边有一个叫做select a report field那找那从哪找到这边有可以从workspace也就是当前的这个工程当中找那从当前的workspace找那boss去找一下我们现在用到的是哪个test charts没错吧那选择ok选择ok那这样一来这个test charts子报表
[04:07] 就能够引入进来了接着点击finish即可当然了这个test charts里面呢我们一起简单的来看一下test charts好了这个test charts里面呢其实既然它是一个组件而言这个title其实就没必要要了我们可以把这个title呢也删掉OK那接着这块区域呢我们给它来一个来的稍微窄一点别这么高了就OK保存
[04:45] 那接下来回到副组件就放到这个位置就可以了那各位来看就目前而言我副报表当中已经引入到了子报表这个内容但是有一个问题咱们一定要说清楚就是子报表它需要数据而且子报表它需要的是一个我们叫做list这么一个数据没错吧那接下来我副报表如何往list里面传递值呢
[05:20] 是这样的我们整个的一个调用过程各位我们要通过Java程序进行调用调用进行填充但是我们Java程序调用填充的时候永远调用或者填充的它其实是我们的副报表也就是说我往里面要存数据那数据先传递到副报表接着通过把副报表里面的内容是不是再去传递给一个一个的子报表
[05:48] 那子报表是不是才能去展示出里面动态的内容啊所以这边就涉及到一个辅报表与子报表传递值的这么一种方式那这个我们又来如何去做呢并且我现在子报表它需要的是一个粒子数组没错吧所以接下来我们来看一下如何去做那首先注意针对这种情况
[06:16] 看一下我们需要的值那我们这边需要的值是一个粒子的数组那粒子的数组那有的朋友说针对这个情况我能不能定一个在负报表这边定一个Fuse那你定义Fuse的话Fuse其实代表的是对象当中的某一个属性那显然不能满足我们的需求这个各位能不能理解那我们现在要往子报表这边传递传递一个粒子集合那根据我们之前讲过的两种传执方式
[06:43] 第一个parameter那parameter里面可以传它其实parameter它代表的是一个map集合map集合里面既能传子军旅行的数据也能传一个历史数组没错吧所以我需要传值的话我在复报表这边接收一个parameter参数那这边create parameter那这个create parameter里面可以给它来一个叫做sublist我随便写的那这个sublist里面这边呢它的class选什么
[07:13] 注意我们可以自己去找一下注意里面可以搜索list找到list集合list集合注意java.youtube.listOK那这样一来我们就已经说清楚了你一会调用的时候你往这个里面传值传至一个map集合传一个map集合进来那这个map集合呢它与一个key这个key呢代表的是sublist还有一个value那这个value它是一个list的数组
[07:48] 那这个list数组是我们刚才这个chart图里面所需要的叫做user countlist没错吧那这样一来我副报表拿到了那拿到了之后我关注的是如何把这个数据传递给我们的子报表那子报表如何接收数据各位继续往下看那如何接收呢左键点击一下我们这个子报表那接着这边找到它的property找到属性
[08:18] 那找到属性找到subreport那找到这个subreport之后呢各位这个里面其实就可以对子报表数据进行填充了可以对子报表的数据进行填充那接下来呢我们再去回到我们这张图形各位我们刚才单独的去找这个chart图的时候这个chart图里面这里面接收的Java对象是什么各位还有印象吗是我们new的一个叫做JRbinConnectionDataSource
[08:47] 传递过去我们之前是new这么一个对象传递进去那传递进去之后这边需要根据粒子集合抱歉我长一点根据粒子集合是不是构造了一个JRBIN connection data source没错吧而我们现在副报表拿到的是不是只有一个粒子集合那我们要想把副报表的数据传递给子报表是不是也需要new出来这么一个玩意儿这个各位能理解吗能够理解的话那接下来
[09:17] 回到我们这个studio当中我们接下来要做的事情各位就有了那如何去做注意这边呢它有一个叫做connection pro这玩意儿我们不需要该删就删那接下来呢在这个里面有一个叫做data source expression就是你数据的来源数据究竟从哪来那接下来这边关注的是写里面的表达式OK这个表达式里面呢咱们开始一个一个去找这里面其实都没有关注的是底下这边value class
[09:51] 那这个value class我们继续进行查找注意来找找什么我们刚才说过了我构造子列表数据的时候需要把复报表拿到的list构造成一个new一个jrbinconnectiondatasource所以我这边要找jrbinconnectiondatasource我找到了我找到了接下来接下来那这个里面要填什么内容你各位来看啊各位来看啊
[10:22] 我把这个呢Ctrl C拷过来把这个拖得长一点那我要做的事情new这个对象那new一个对象之后其实就意味着这句话我们在通过表达式的形式在模拟它那中间是不是接收一个list集合那这个list集合是不是通过sublist进行获取啊没错吧所以我这里面得到的是$P注意这个$P代表的是我们刚才定义的叫做sublist
[10:57] 所以这边$P中间大括号sublistOK那这样一来我这个表达式其实已经写好了好了这个表达式究竟有没有写错其实你可以观察一下在这儿如果没有红叉的话其实代表你这个表达式其实已经写对了OK点击finish那这样一来其实我们已经完成了父子报表传执的这么一个操作其实这个有点绕其实各位只要能够
[11:31] 看懂这张图形的话其实就已经都能够掌握了那我们主要目的通过Java传信器以MAP集合的时候往复报表传值那传的值之后呢其实我们能够拿到一个List集合那这个List集合想要传递给我们的子报表那这个子报表我们之前子报表里面得到的是这么一个对象那我现在拿到的是一个List那这个List显然不满足这个对象那怎么做呢我们自己Nu一个那恰巧Studio又接收这种写表达式的形式
[12:00] 所以我们通过表达式就去构造了这么一个对象OK当然了这边有点显示不全OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 JasperReports 中创建和配置子报表（Subreport），包括拖拽组件、设置数据源和参数映射。

2) 按时间顺序列出每张画面的要点：
画面1: 讲解制作子报表的步骤，提示点击“Subreport”按钮并拖动到工作区。
画面2: 展示一个手绘的报表结构图，包含“交报表”、“功能1-子报表1”、“功能2-子报表2”和“list”四个部分。
画面3: 在 JasperReports Studio 中，弹出“New Report Wizard”对话框，提示选择父报表文件夹，当前文件名为“main01.jrxml”。
画面4: JasperReports Studio 主界面，显示“main01.jrxml”和“testCharts.jrxml”两个文件，工作区为空。
画面5: 展示一个手绘的报表结构图，与画面2类似，但左侧标注了“java程序”。
画面6: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Parameter1”参数的配置，类型为“java.lang.String”。
画面7: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”。
画面8: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“chart”字样。
画面9: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样。
画面10: 在浏览器中预览报表，显示“用户列表”，包含用户ID、用户名、薪资、部门等字段。
画面11: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Expression”为“testCharts.jasper”。
画面12: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Data Source Expression”为“new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”。
画面13: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样。
画面14: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Data Source Expression”为“new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面3: “Report file Please select your reports file name with .jrxml extension.” “Enter or select the parent folder: TestReports/” “The name: main01.jrxml” “Opening file for editing...”

画面6: “Parameter1” “Name: Parameter1” “Class: java.lang.String”

画面9: “new JRBeanCollectionDataSource(userList)”

画面12: “new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2: 展示一个手绘的报表结构图，包含“交报表”、“功能1-子报表1”、“功能2-子报表2”和“list”四个部分，其中“交报表”通过三条线分别指向“功能1-子报表1”、“功能2-子报表2”和“list”。

画面7: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”、“功能2-子报表2”和“list”三个框通过线连接。

画面8: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“chart”字样，通过线连接。

画面9: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样，通过线连接。

画面10: 展示一个表格，标题为“用户列表”，包含以下列：用户ID、用户名、薪资、部门。数据行包括：
- 用户ID: 1065705989262279, 用户名: a123, 薪资: 1380000002, 部门: 传智播客, 用户名: test1
- 用户ID: 10663704986334863, 用户名: zhe, 薪资: 1380000003, 部门: 传智播客, 用户名: 测试部
- 用户ID: 10716327602228101, 用户名: ll, 薪资: 1380000004, 部门: 传智播客, 用户名: 测试部
- 用户ID: 10742388013307043, 用户名: a01, 薪资: 1340000001, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10742388014020775, 用户名: a02, 薪资: 1340000002, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10753831331064258, 用户名: test001, 薪资: 1350000001, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10753831353713500, 用户名: test002, 薪资: 1350000002, 部门: 传智播客, 用户名: 开发部
- 用户ID: 1075383135494304, 用户名: test003, 薪资: 1350000003, 部门: 传智播客, 用户名: 开发部

5) 无

