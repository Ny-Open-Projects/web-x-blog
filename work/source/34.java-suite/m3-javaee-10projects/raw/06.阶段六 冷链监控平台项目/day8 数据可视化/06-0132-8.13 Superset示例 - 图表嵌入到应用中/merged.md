# 8.13 Superset示例 - 图表嵌入到应用中

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day8 数据可视化
- 源文件：06.阶段六 冷链监控平台项目\day8 数据可视化\8.13 Superset示例 - 图表嵌入到应用中_【海量资源尽在 666java.com】.mp4
- 时长 6分19秒（音频 379s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 而我们使用我们的SuperSight开发了一个报表那么下一步的时候我们希望这个报表被运营人员或者管理人员来查看当然我们可以想象得到的时候针对一个公司它有非常多的系统那么有一个非常有用的功能就是我如何把所有的系统集成在一起来查看这样的时候这样的情况下我们不需要
[00:24] 登录到各个系统里边来做各种各样的一些工作而只是需要在一个统一的一个系统里边来查看了那么针对于报表这样的一个需求SweepSight是一个报表开发平台那么我们开发出来的平台开发出来的报表我们就希望把这些报表放到我们的业务系统里边来也就是说比如我们的冷链设备监控平台这个系统我们希望在这儿来展示SweepSight的一个报表
[00:52] 那么下面我们来看一看如何把我们SuperSight的报表迁入到我们的应用系统里边那首先第一步是我们需要进行一些配置而这个配置呢是说我们针对我们的这个SuperSight它的一个权限来做了一些设置我们登录到因为我们的SuperSight是在我们的Docker里边所以说第一步我们需要先登录到我们的SuperSight的它的一个叫做
[01:22] CubeSight它的一个容器里边而针对于这个容器呢我们可以查看我们这个容器的一个呃配置文件这个配置文件的地址我们在我们的讲义里边已经填上了我们现在直接把它拷贝过来我们编辑这个文件而编辑完文件之后呢打开它之后有一个public row like gamma
[01:46] public row like gamma因为本身我们知道我们在super set的权限里边它默认的有一个gamma权限而这个gamma权限我们它是有一些基本的默认的一些权限信息我们在只需要在我们的这个配置文件里边把我们public row like gamma设置成to那么设置完to之后呢我们第二步需要在我们的这个
[02:14] 当然了我们在配置文件里边还有另外的一些配置信息可以添加一个信息是说我们的默认的开发语言默认的一些语言是中文的还是英文的第二部分来讲的话是说我们是否进行跨域的一个访问那么把http header设置成一个空的一个大的大括号那么这样的话我们的
[02:40] iFrame就可以进行跨域的访问了那下一步的话我们配置我们的这个权限这个权限是在我们的安全Security里面的一个角色在这个角色里边我们添加一个我们的新记录添加新记录的时候呢我们可以输入它的用户名输入它的名字叫做public然后权限的话有三个权限第一个权限就是Can explore on SuperSight第二个权限是Can explore
[03:10] JSON on Supersight也就是说从Supersight里面直接打开或者说是查询JSON那第三个的话是AuditBase Access也就是说是数据库的一个权限我们在对于public用户就能够直接访问了当然这种情况有些人可能是说会不会有安全问题你的疑问是正确的或者说是有道理的
[03:37] 但是有一个地方是说我们的数据是在我们的内网里边而我们的这个报表呢大多数情况都是给我们的内网用户来访问的所以在这里边的话我们假定它的用户权限并没有那么高要求用户的安全性属性要求并没有那么高它只是需要在内网中访问我们的业务系统访问我们查看我们的这些报表就OK了我们添加完这些
[04:05] 全线之后呢下一步我们就可以开发我们具体如何把我们的这个怎么说呢把我们的报表迁入到我们的表单里边迁入到我们的应用里边那我们看一看我们的一个报表而这个报表呢是我们开始编辑或者说开始设计的一个报表在这个报表的右侧呢我们能够看到哎就是当前这个区域里边我们能够看到毕业生数量这个图表那么上面有那么几个按钮
[04:35] 第二个按钮第一个按钮是我们直接把一个链接拷贝过去别人点这个链接就能打开这个报表那第二部分是一个JSON的一个文件JSON的一段代码而这个JSON代码它其实是一个iFrame我们可以设置这个iFrame的一个宽度的一个大小还有是我们的高度大小然后点击一下复制到间贴板然后我们把它复制出来了
[05:03] 复制出来之后呢我们实际上只需要在我们的HTML页面里边我们在HTML页面里边就把我们这个文件就是刚才看到的这个JS的文件我们直接把它拷贝过来然后下一步我们把它打开的时候我们就能够把这个报表直接展现出来了因为这是纯粹的HTML页面而我们能够把HTML页面迁入到我们的应用系统
[05:42] 它的HTML页面里边去那么所以我们直接就能够在业务系统直接访问SuperSight它的一个报表这就是我们整个把SuperSight的报表迁入到我们业务系统的一个过程简单的来讲的话就是两个步骤第一个步骤我们开发我们配置我们的这个权限
[06:04] 在系统里面配置和在我们配置文件里面添加一个配置那么第二部分是把我们的iFrame的代码迁入拷贝到业务系统里面

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何将 Superset 报表通过 iframe 嵌入到其他应用中，并配置角色权限。

2) 按时间顺序列出每张画面的要点：
画面1：显示 Superset 的仪表盘界面，展示“毕业生数量”图表，时间范围为 2012-2014 年。
画面2：在 Typora 编辑器中，显示 Superset 的配置文件内容，包括修改角色权限的命令和配置项。
画面3：在 Typora 编辑器中，显示 Superset 的配置文件内容，包括修改角色权限的命令和配置项。
画面4：在 Typora 编辑器中，显示 Superset 的配置文件内容，包括修改角色权限的命令和配置项。
画面5：在 Typora 编辑器中，显示 Superset 的配置文件内容，包括修改角色权限的命令和配置项。
画面6：在 Superset 界面中，显示“角色列表”，其中“Admin”角色具有所有权限。
画面7：在 Superset 界面中，显示“编辑角色”页面，正在编辑“Public”角色的权限。
画面8：在 Typora 编辑器中，显示 Superset 的配置文件内容，包括修改角色权限的命令和配置项。
画面9：在 Superset 界面中，显示空白页面，可能是在加载或未正确嵌入。
画面10：在桌面，右键点击“test.html”文件，选择“新建”->“文本文件”。
画面11：在桌面，右键点击“test.html”文件，选择“新建”->“文本文件”，弹出“警告”对话框。
画面12：在 Notepad++ 编辑器中，显示空白页面，准备创建新文件。
画面13：在浏览器中，打开“test.html”文件，显示空白页面。
画面14：在浏览器中，打开“test.html”文件，显示 Superset 的“毕业生数量”柱状图，数据源为“users”，图表类型为“Bar Chart”，时间维度为“graduated”，时间范围为“year”，指标为“毕业生数量”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2-5、8：
# 查看superset容器
[root@node2-v806 superset]# Docker ps | grep superset
0d648295313   amancevice/superset   "gunicorn superset:a..."   13 days ago   Up 2   hungry_lovelace
days (healthy)   0.0.0.0:7080->8080/tcp

# 进入superset容器
[root@node2-v806 superset]# Docker exec -u root -it 0d648295313 /bin/bash
root@0d648295313:/home/superset# vim /usr/local/lib/python3.6/site-packages/superset/config.py
PUBLIC_ROLE_LIKE_GAMMA = True

# 设置默认语言
BABEL_DEFAULT_LOCALE = 'zh'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'superset/translations'
# The allowed translation for you app
LANGUAGES = {
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'en': {'flag': 'us', 'name': 'English'},
}

# 通过iframe屏蔽无访问权限
HTTP_HEADERS = ()

画面6：
[Admin]
[can this form post on ResetPasswordView, can this form on UserinfoEditView, can this form on UserEditView, can this form on UserDBModelView, can show on UserDBModelView, can edit on UserDBModelView, can delete on UserDBModelView, can add on RoleModelView, can edit on RoleModelView, can delete on RoleModelView, can add on PermissionModelView, can edit on PermissionModelView, can delete on PermissionModelView, can list on Base Permissions, can list on ViewMenuModelView, can list on Views, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users, can list on Users

