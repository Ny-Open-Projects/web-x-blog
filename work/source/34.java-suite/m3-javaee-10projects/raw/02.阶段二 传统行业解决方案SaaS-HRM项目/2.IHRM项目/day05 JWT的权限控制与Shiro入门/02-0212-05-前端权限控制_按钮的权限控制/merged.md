# 05-前端权限控制：按钮的权限控制

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\05-前端权限控制：按钮的权限控制_【海量资源尽在 ubkz.com】.mp4
- 时长 5分21秒（音频 321s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们简单的看了一下就是目前前端的这个菜单的权限我们已经灵活的可以控制了那接下来就是说那如果要针对某一个按钮如何去做呢好的这边呢我用我们第三个用户访问一下他是我们的一个普通用户那点击过来之后呢各位来看他对于这个用户操作呢有查看分配角色和删除的这么几个按钮那首先呢我们要想对这个进行操作的话
[00:28] 咱们就需要指定当前员工他所属的一个角色看一下他这个角色有没有删除按钮的操作权限那好了我们一起呢回到我们这边企业管理管理员企业管理员这个企业管理员的点进去之后他可以对这个公司他这个角色人事部门这个角色来进行分配权限那分配权限的时候各位来看这个员工管理里面
[00:53] 有用户删除的等等等等这些按钮比如说呢我把用户删除的按钮给它去掉那这个人是那这个删除按钮在哪呢各位来看其实是在我们这边权限管理后台添加的它隶属于员工管理这个菜单下那这个删除按钮它的一个权它这个名称呢或者一个标示我们叫做point user delete把它呢复制过来control c那好了接下来我退出那再以第三个档号切换一下登录进来
[01:23] 那按道理说呢当前这个用户他是一个我们叫做人事经理那人事经理这个删除按钮就不应该有那我们应该怎么做呢其实很简单我们需要在这个删除按钮找到他好了我已经定位到了我们这个用户这个页面这里面呢有分配角色删除来看分配角色删除都没问题那我们需要在分配角色删除这边进行一个判断很简单v-if那判断比如说瘦写一方法判断一下
[01:53] 那受什么呢咱们注意这个删除按钮是不是给它来了一个权限标志我们就判断一下这个权限标志point user delete好了如果说这个玩意儿触发的一个方法返回的是false那它就隐藏了如果返回的是一个处就显示所以这个很明确我们的做法也比较简单v刚一幅写一个方法进行判断这边呢添加一个受方法那接着呢在受方法当中我们通过
[02:20] 获取用户信息拿到的所有的按钮的这些操作权限和我们这个当前的这玩意进行比较那如果包含这个那选回false如果不包含这个标示是不是就返回处啊所以这边我们可以写一个受方法来做好了传递一个name进来好了那接下来呢里面就可以进行一个返回了return那注意了这个比较的代码呢我们已经给各位准备好了
[02:48] 那写到了什么地方我先给它引进来已经放到了我们的叫做ETAUTILS下的PRMSSLN这个文件下好了在这边呢我也已经打开了这里面呢写了一个方法就是你可以传递一个名称过来我判断一下是否存在那判断是否有这个悬念点给它起了一个方法是一个工具类叫做HASPOMISSION POINT这里面的代码呢不难首先呢ROSE
[03:21] 是我们刚才登录获取用户信息的ros里面的具备了menus和pounds那pounds代表所有的权限点我们这边指的是按钮那我判断一下如果有pounds如果你有所有的按钮的sum那这个就是一个过滤循环比较的一个配置就是看一下你这边不区分大小写随便填都可以如果能找到返回处如果找不到返回false这个比较简单所以呢我把这个方法引进来引进来之后那在这边show里面我们就可以直接return
[03:53] 工具类里面把内幕传下去让它去自动的根据权限标志进行比较好了这个受方法我们补充完整了之后当前这个用户是没有删除的那各位来看删除按钮已经隐藏了那如果说我再把这个权限给它分配上啊这个别些麻烦这个就是不断的测试的过程好了在这边呢把这个人事经理的删除权限给它配置上好了配置上了之后呢我这边再退出再去以03
[04:22] 普通用户这个身份进行登录来各位来看删除按钮不就又回来了吗那这样一来我们就已经做到了前端页面的菜单以及按钮的这一个权限控制但是呢我想跟各位来聊的就是说啊那就目前而言菜单我们搞定了那我们的按钮也搞定了但是难道真的你这个按钮你不能显示他就不能发送这个请求吗
[04:49] 好了那这个呢其实我们都知道前端归前端后台归后台你后台如果不做防御性的措施你只要有一点点常识我们是不是就可以通过postman等等等等这些的软件进行攻击我们的我们的服务端后台啊所以我们现在做的前端控制仅仅是皮帽而已那么我们接下来关注的就是如何在我们的服务端对我们的API权限进行我们叫做判断

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 iHRM 人事管理系统中“权限配置”功能的前端页面操作与后端 Vue.js 代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：登录页面，输入用户名“13800000001”并点击“登录”。
画面 2：登录成功后，进入“员工”模块页面，显示工作日历和快捷导航。
画面 3：在左侧菜单中点击“权限设置”。
画面 4：弹出“为【人事经理】分配权限”对话框，勾选多个权限项，点击“确定”。
画面 5：页面跳转至空白页，显示“正在加载...”。
画面 6：页面加载完成，显示员工列表，同时在任务栏中可见 Visual Studio Code 编辑器窗口。
画面 7：在 Visual Studio Code 中打开 `index.Vue` 文件，展示 `<el-table-column>` 和 `<router-link>` 等组件代码。
画面 8：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `import` 和 `export default` 的模块定义代码。
画面 9：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `hasPermission` 函数的实现代码。
画面 10：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `methods` 中 `doQuery` 方法的代码。
画面 11：页面跳转至空白页，显示“正在加载...”。
画面 12：页面加载完成，显示“公司设置”页面。
画面 13：页面跳转至空白页。
画面 14：页面加载完成，返回“员工”模块页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7 代码：
```Vue
<el-table-column sortable prop="timeEntry" label="入职日期" width="140">
  <template slot-scope="scope">
    <el-switch
      v-model="scope.row.accountStatus"
      active-color="#ff4400"
      inactive-color="#ff4400"
      @change="handleStatus(scope.row)">
    </el-switch>
  </template>
</el-table-column>
<el-table-column
  label="操作"
  width="280">
  <template slot-scope="scope">
    <router-link :to="'/employees/details/' + scope.row.id" class="el-button el-button--text el-button--small">
      查看
    </router-link>
    <el-button @click="handleDelete(scope.row)" type="text" size="small" class="el-button el-button--text el-button--small">
      删除
    </el-button>
    <el-button @click="handleEdit(scope.row)" type="text" size="small" class="el-button el-button--text el-button--small">
      编辑
    </el-button>
  </template>
</el-table-column>
<div class="pagination">
  <el-pagination
    :requestParameters.page="requestParameters.page"
    :requestParameters.pageSize="requestParameters.pageSize"
    :total="counts"
    :page-size="10"
    layout="prev, pager, next, jumper"
    @current-change="handleCurrentChange">
  </el-pagination>
</div>
```

画面 8 代码：
```javascript
import store from '@/store'
import constantApi from '@/api/constant/departments'
import { listRemove } from '@/api/base/users'
import PageTool from '@/components/page-tool'
import employeesAdd from '@/components/add'
import addRole from '@/components/addRole'
export default {
  name: 'employeesList',
  components: {
    PageTool,
    employeesAdd,
    addRole
  },
  data() {
    return {
      employeesAdd: 'employeesAdd',
      addRole: 'addRole',
      baseData: constantApi,
      dataList: [],
      counts: '',
      requestParameters: {
        page: 1,
        size: 10
      }
    }
  }
}
```

画面 9 代码：
```javascript
import { hasPermissionPoint } from '@/util/permission'
export function hasPermission(route, route) {
  if (roles.menus && route.name) {
    return roles.menus.some(role => role.toLowerCase() === route.name.toLowerCase())
  } else {
    return false
  }
}
```

画面 10 代码：
```javascript
import { hasPermissionPoint } from '@/util/permission'
export default {
  name: 'employeesList',
  components: {
    PageTool,
    employeesAdd,
    addRole
  },
  data() {
    return {
      employeesAdd: 'employeesAdd',
      addRole: 'addRole',
      baseData: constantApi,
      dataList: [],
      counts: '',
      requestParameters: {
        page: 1,
        size: 10
      }
    }
  },
  methods: {
    show(name) {
      return
    },
    doQuery(params) {
      list(this.requestParameters)
        .then(res => {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

