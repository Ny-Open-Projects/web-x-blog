# 07-权限基本操作：测试权限的操作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\07-权限基本操作：测试权限的操作_【海量资源尽在 ubkz.com】.mp4
- 时长 5分21秒（音频 322s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 完成了全线操作的这个代码之后呢接下来的我们就可以把相应的这些页面全部都配套放到我们的前端完成我们这个全线的测试那在今天资源当中呢已经把今天要用到前端的代码都给各位准备好了其中用到我们的全线用到我们的setting就是刚才的这个角色还有一个用户管理当然了这几个用户管理呢如果想加就加不加其实也无所谓之前我们都有把这些内容呢全部都引入到我们的
[00:31] VS Code工程当中好了这边的SRC我就开始去添加过去了那这个前端呢不是我们的重点我们就快速的一带而过就可以了好了那这些代码呢我们搞过来了之后呢当然了还需要一个API的一个支持这个API呢我也给各位准备好了我们可以简单的看一下API里面呢这个是全线相关的就是我们刚才操作的那些内容当然了还有我们之前写过的用户还有我们之前写过的角色这些呢都比较简单我就不再一个一个的再去看了
[01:02] OK把这些APICtrl C全部都拿到我们的代码的API目录下Ctrl A不抱歉放到base目录下基本的好了直接就替换了那好了接下来呢在这个用在我们这个前端工程当中呢在MEN这边把我们相应的这些模块全部都进行一个注册我们刚才添加了一个新的叫做permission权限相关的这个模块好了permission 4permission 4进行一个注册
[01:37] 好了直接保存它就会自动的刷新工程好了那接下来呢我们这边localhost808名进行访问现在已经进来了并且呢左侧出现了一个菜单呢叫做权限设置那么可以点击进来来看现在呢已经查询到了所有的权限信息其实现在是已经联系到了我们的后台那么可以简单的看一下后台呢我已经重新启动了当然我再重启一下看一下效果OK这边呢这有一个异常啊
[02:15] 刚才没注意不小心删掉了好了接着我们再去启动一下OK程序正在启动那启动好了之后呢我们再去完成一个访问那我刷新一把这边呢已经有了所有的数据已经出来了那出来了之后呢其实这里面的功能比较简单我列出来的全部都是我们的一级权限也就是我们的菜单那在这个菜单呢你点击一下能够看到这个菜单里面所绑定的一些按钮比如说呢员工碗里为点
[02:53] 查询获取到了这个员工管理这个菜单下边的所有的一些按钮这都是我之前测试的添加的一些测试数据那SaaS协议管理里面也有自己的一些按钮如果没有按钮的话你点这边会爆出一个无死权限的这个错误那这个我们看过了之后接下来呢就是对于权限可以有查看那有查看好了那接下来呢这边呢还可以有对权限的一个删除那当然了还可以添加菜单
[03:20] 那我这边一点添加那各位来看底下就是菜单的一些内容比如说全线名称呢我就叫做测试菜单好了随便填随便填随便填走填成功有一个测试菜单我们可以对它进行一个查看好了加上123可见45走修改成功那12345可见没问题那接下来呢我们可以把它进行一个删除走你发现它已经删除了
[03:53] 那删除了抱歉他已经删除了那这个其实就是我们所有的这些内容那当然了如果想对某一个菜单底下去添加他的一些权限点或者我们叫做菜单的话你可以在这边添加选点好了同样的逻辑底下就变成了是一些按钮了比如说呢AAA好了AAA这边勾选是否可见点击确定这边报了一个简单的错误我们一起来看一下OK这个简单的看一下其实你能猜到这个状态
[04:25] 不是1就是它是一数字啊不能用a呀来1吧走好了也没问题来看里面又多了一个a那好了把它也可以删掉了那接下来就是说呢在这边呢除了这个之外呢一个菜单可以绑定一些按钮这个啊一个菜单或者是按钮下是不是还可以给它添加相应的API的一些权限比如说这边可以绑定API权限那这边你可以点击看没有那没有的话我可以添加OK好了这边呢
[04:55] 找一个我记得哪个里面有啊查看API全线都没有都没有吗我找一个哎这个菜单里面有这不是一个添加一个API全线当然了你可以去添加这边就变成了API的相关内容OK好了这样一来呢我们基本的这个全线相关内容我们就已经都搞定了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Vue.js 和 Java 的 SaaS 人力资源管理系统中权限管理模块的前后端代码实现与前端界面操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”两个机构的标志。
画面2：文件资源管理器中显示项目根目录，选中了“module-permissions”文件夹，同时预览了“src”目录下的文件结构。
画面3：Notepad++ 编辑器中显示了“users.js”文件内容，其中定义了多个与用户相关的 API 请求方法。
画面4：文件资源管理器中显示“api”文件夹，选中了“permissions.js”文件。
画面5：Visual Studio Code 编辑器中显示“main.js”文件，导入了多个模块并注册了 Vue 实例，底部显示应用已成功编译并在本地运行。
画面6：IntelliJ IDEA 中显示 Java 代码，具体为“PermissionService.java”中的删除权限方法，包含对不同权限类型的判断和删除操作。
画面7：IntelliJ IDEA 中显示“PermissionController.java”中的删除权限方法，包含对不同权限类型的判断和删除操作。
画面8：浏览器中显示 HRM 系统的“权限管理”页面，列出了多个菜单项及其权限标识。
画面9：浏览器中显示“权限管理”页面，选中了“test”权限项并点击“编辑”按钮。
画面10：浏览器中显示“权限管理”页面，选中了“权限菜单1”并点击“编辑”按钮。
画面11：浏览器中弹出“编辑权限”对话框，包含“权限名称”、“权限标识”、“权限描述”、“企业可见”、“按钮样式”、“按钮icon”、“按钮状态”等字段。
画面12：浏览器中弹出“编辑权限”对话框，切换到“API权限列表”标签页，包含“权限名称”、“权限标识”、“权限描述”、“企业可见”、“API请求地址”、“API请求方式”、“API类型”等字段。
画面13：浏览器中显示“API权限列表”弹窗，列出了“查看部门”权限项及其操作按钮。
画面14：浏览器中显示“API权限列表”弹窗，列出了“查看部门”权限项及其操作按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```javascript
import {createAPI} from '@/utils/request'

export const list = data => createAPI('/sys/user', 'get', data)
export const simple = data => createAPI('/sys/user/simple', 'get', data)
export const add = data => createAPI('/sys/user', 'post', data)
export const update = data => createAPI('/sys/user/${data.id}', 'put', data)
export const remove = data => createAPI('/sys/user/${data.id}', 'delete', data)
export const detail = data => createAPI('/sys/user/${data.id}', 'get', data)
export const assignRoles = data => createAPI('/sys/user/assignRoles', 'put', data)
```

画面5：
```javascript
import 'font-awesome/css/font-awesome.css'
import '@/mock' // 模拟数据
import dashboard from '@/module-dashboard' // 图表
import demo from '@/module-demo' // 高级
import saasClients from '@/module-saas-clients' // 企业客户
import departments from '@/module-departments' // 部门
import employees from '@/module-employees' // 员工
import settings from '@/module-settings' // 设置

import tools from '@/utils/common.js'
Vue.prototype.Stools = tools

Vue.use(dashboard, store)
Vue.use(demo, store)
Vue.use(saasClients, store)
Vue.use(departments, store)
Vue.use(employees, store)
Vue.use(settings, store)
```

画面6：
```java
return permissionDao.findAll(spec);
```

画面6：
```java
public void deleteById(String id) throws Exception {
    // 1.通过传递的权限id获取权限
    Permission permission = permissionDao.findById(id).get();
    // 2.根据权限类型不同的处理
    int type = permission.getPermissionType();
    switch (type) {
        case PermissionConstants.PERMISSION_MENU:
            permissionMenuDao.deleteById(id);
            break;
        case PermissionConstants.PERMISSION_POINT:
            permissionPointDao.deleteById(id);
            break;
        case PermissionConstants.PERMISSION_API:
            permissionApiDao.deleteById(id);
            break;
    }
}
```

画面7：
```java
@GetMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws Exception {
    Map map = permissionService.findById(id);
    return new Result(ResultCode.SUCCESS, map);
}
```

画面7：
```java
@DeleteMapping(value = "/permission/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) throws Exception {
    permissionService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

