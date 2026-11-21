# 画面线理解：05-前端权限控制：按钮的权限控制

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\05-前端权限控制：按钮的权限控制_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:19, 00:44, 00:59, 01:19, 01:34, 01:43, 02:34, 03:06, 03:51, 04:04, 04:12, 04:19, 04:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:11:05

1) 这一组画面整体在讲什么（一句话）：
演示 iHRM 人事管理系统中“权限配置”功能的前端页面操作与后端 Vue.js 代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：登录页面，输入用户名“13800000001”并点击“登录”。
画面 2：登录成功后，进入“员工”模块页面，显示工作日历和快捷导航。
画面 3：在左侧菜单中点击“权限设置”。
画面 4：弹出“为【人事经理】分配权限”对话框，勾选多个权限项，点击“确定”。
画面 5：页面跳转至空白页，显示“正在加载...”。
画面 6：页面加载完成，显示员工列表，同时在任务栏中可见 Visual Studio Code 编辑器窗口。
画面 7：在 Visual Studio Code 中打开 `index.vue` 文件，展示 `<el-table-column>` 和 `<router-link>` 等组件代码。
画面 8：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `import` 和 `export default` 的模块定义代码。
画面 9：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `hasPermission` 函数的实现代码。
画面 10：在 Visual Studio Code 中打开 `JS/permission.js` 文件，展示 `methods` 中 `doQuery` 方法的代码。
画面 11：页面跳转至空白页，显示“正在加载...”。
画面 12：页面加载完成，显示“公司设置”页面。
画面 13：页面跳转至空白页。
画面 14：页面加载完成，返回“员工”模块页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7 代码：
```vue
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
