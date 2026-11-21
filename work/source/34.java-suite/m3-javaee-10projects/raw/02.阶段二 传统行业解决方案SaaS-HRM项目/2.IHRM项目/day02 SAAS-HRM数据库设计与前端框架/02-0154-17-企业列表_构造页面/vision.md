# 画面线理解：17-企业列表：构造页面

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\17-企业列表：构造页面_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:26, 03:07, 04:03, 04:27, 04:53, 05:53, 06:47, 07:21, 07:52, 08:27, 08:47, 09:41, 10:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:17:51

1) 这一组画面整体在讲如何使用 Vue.js 和 Element UI 框架开发一个 SaaS 企业管理系统，重点展示表格组件的使用、数据绑定和 API 接口调用。

2) 按时间顺序列出每张画面的要点：
画面1：展示 SaaS 企业管理系统登录后的首页，包含“SAAS企业”管理模块，下方是浏览器开发者工具，显示了页面加载的网络请求和响应数据。
画面2：在 Visual Studio Code 中打开 Vue 项目，展示 `index.vue` 文件的模板部分，使用 `v-for` 循环渲染数据列表。
画面3：在百度搜索框中输入“echarts”，展示搜索建议。
画面4：在 Element UI 官网展示“带边框表格”组件，表格包含“日期”、“姓名”、“地址”等列。
画面5：在 Element UI 官网展示“流体高度”表格，表格列包含“日期”、“姓名”、“省份”、“市区”、“地址”、“操作”。
画面6：在 Element UI 官网展示“固定列”表格示例，代码中使用 `fixed` 属性固定列。
画面7：在 Visual Studio Code 中编辑 `index.vue` 文件，添加 Element UI 的表格组件，并设置列的 `prop` 和 `label`。
画面8：在 Element UI 官网展示“固定列”表格的代码示例，包含 `border`、`style`、`fixed` 等属性。
画面9：展示 SaaS 企业管理系统中的“客户”列表页面，包含“当前版本”、“联系人”、“联系电话”、“所在地区”、“申请时间”、“状态”、“操作”等列。
画面10：展示“客户”列表页面的滚动条，显示数据列表。
画面11：展示“客户”列表页面，包含“序号”、“企业名称”、“当前版本”、“联系人”、“联系电话”、“所在地区”、“申请时间”、“状态”、“操作”等列。
画面12：在 Visual Studio Code 中编辑 `index.vue` 文件，添加 Element UI 的表格组件，并设置列的 `prop` 和 `label`。
画面13：展示 SaaS 企业管理系统中的“API 文档”页面，包含 GET、PUT、DELETE 三个 HTTP 方法的接口。
画面14：展示 SaaS 企业管理系统中的“企业”列表页面，包含“企业名称”、“版本”、“联系电话”、“截至时间”、“状态”、“操作”等列。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <div v-for="(item, index) in dataList" :key="index">
          <el-card>
            {{item.name}}
          </el-card>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面6：
```vue
<template>
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="地址">
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  },
  methods: {
    handleClick(row) {
      console.log(row)
    }
  }
}
</script>
```

画面7：
```vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <el-table :data="dataList" border style="width: 100%">
          <el-table-column fixed prop="name" label="企业名称" width="150"></el-table-column>
          <el-table-column fixed prop="phone" label="联系电话" width="150"></el-table-column>
          <el-table-column fixed prop="address" label="所在地区" width="150"></el-table-column>
          <el-table-column fixed prop="applyTime" label="申请时间" width="150"></el-table-column>
          <el-table-column fixed prop="status" label="状态" width="150"></el-table-column>
          <el-table-column fixed prop="operation" label="操作" width="150"></el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面12：
```vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <el-table :data="dataList" border style="width: 100%">
          <el-table-column fixed prop="name" label="企业名称" width="150"></el-table-column>
          <el-table-column fixed prop="phone" label="联系电话" width="150"></el-table-column>
          <el-table-column fixed prop="address" label="所在地区" width="150"></el-table-column>
          <el-table-column fixed prop="applyTime" label="申请时间" width="150"></el-table-column>
          <el-table-column fixed prop="status" label="状态" width="150"></el-table-column>
          <el-table-column fixed prop="operation" label="操作" width="150"></el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面13：
```json
{
  "success": true,
  "message": "string",
  "data": [
    {
      "id": "string",
      "name": "string",
      "manager_id": "string",
      "regional_date": "string",
      "expiration_date": "string",
      "company_code": "string",
      "business_license_id": "string",
      "legal_representation": "string",
      "company_phone": "string",
      "mail_box": "string",
      "company_site": "string",
      "industries": "string",
      "rewards": "string",
      "audit_status": "string",
      "state": "string",
      "balances": "string",
      "create_time": "string"
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：无 PPT 内容。
画面2：无 PPT 内容。
画面3：无 PPT 内容。
画面4：无 PPT 内容。
画面5：无 PPT 内容。
画面6：无 PPT 内容。
画面7：无 PPT 内容。
画面8：无 PPT 内容。
画面9：无 PPT 内容。
画面10：无 PPT 内容。
画面11：无 PPT 内容。
画面12：无 PPT 内容。
画面13：无 PPT 内容。
画面14：无 PPT 内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
