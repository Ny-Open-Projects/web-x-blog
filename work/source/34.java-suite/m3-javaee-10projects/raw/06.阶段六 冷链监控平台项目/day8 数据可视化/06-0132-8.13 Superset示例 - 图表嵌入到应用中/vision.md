# 画面线理解：8.13 Superset示例 - 图表嵌入到应用中

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day8 数据可视化
- 源文件：06.阶段六 冷链监控平台项目\day8 数据可视化\8.13 Superset示例 - 图表嵌入到应用中_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 01:29, 01:46, 02:13, 02:24, 02:53, 03:00, 04:10, 04:23, 05:06, 05:17, 05:23, 05:29, 05:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 18:00:10

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
[root@node2-v806 superset]# docker ps | grep superset
0d648295313   amancevice/superset   "gunicorn superset:a..."   13 days ago   Up 2   hungry_lovelace
days (healthy)   0.0.0.0:7080->8080/tcp

# 进入superset容器
[root@node2-v806 superset]# docker exec -u root -it 0d648295313 /bin/bash
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
