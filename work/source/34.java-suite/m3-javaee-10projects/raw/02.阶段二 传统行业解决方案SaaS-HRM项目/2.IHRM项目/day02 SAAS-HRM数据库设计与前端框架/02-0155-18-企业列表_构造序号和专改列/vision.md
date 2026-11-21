# 画面线理解：18-企业列表：构造序号和专改列

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\18-企业列表：构造序号和专改列_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:37, 00:46, 01:17, 01:40, 02:14, 03:03, 03:41, 04:13, 04:27, 05:01, 05:18, 05:35, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:18:26

1) 这一组画面整体在讲如何在 Vue 项目中使用 Element UI 的 Switch 组件来控制表格中“状态”字段的显示，并通过代码修改实现动态切换。

2) 按时间顺序列出每张画面的要点：
画面1：在 Visual Studio Code 中编辑 `index.vue` 文件，展示表格列定义和操作按钮的代码，其中包含 `el-table-column` 和 `el-button` 组件。
画面2：浏览器中显示 SaaS 企业列表页面，展示企业信息表格，包含序号、企业名称、当前版本、联系人、联系电话、所在地区、申请时间、操作列。
画面3：浏览器中继续展示企业列表，滚动显示更多企业记录，序号从 8 到 17。
画面4：浏览器中切换到“体验版”页面，显示“江苏传智播客教育科技股份有限公司”的企业列表，顶部有“体验版”标签。
画面5：浏览器中切换到“SaaS企业”页面，显示企业列表，其中第4行“常州新北区”企业被选中，状态为“正常”。
画面6：浏览器中打开 Element UI 官网的 Switch 组件页面，展示其用法和代码示例。
画面7：在 Visual Studio Code 中编辑 `index.vue` 文件，添加 `el-switch` 组件，并设置 `v-model="scope.row.state"`。
画面8：在 Visual Studio Code 中编辑 `index.vue` 文件，继续修改 `el-switch` 组件的属性，设置 `active-color="#f56c6c"` 和 `inactive-color="#fff999"`。
画面9：在 Visual Studio Code 中编辑 `index.vue` 文件，修改 `el-switch` 组件的 `active-value` 和 `inactive-value` 属性。
画面10：在 Visual Studio Code 中编辑 `index.vue` 文件，将 `el-switch` 组件的 `active-value` 设置为“1”，`inactive-value` 设置为“0”。
画面11：在 Visual Studio Code 中编辑 `index.vue` 文件，修改 `el-switch` 组件的 `active-value` 为“是”，`inactive-value` 为“否”，并调整 `el-switch` 的位置。
画面12：浏览器中显示 SaaS 企业列表页面，其中第1行“企业0”和第2行“企业1”的状态开关为“开”。
画面13：在 Visual Studio Code 中编辑 `index.vue` 文件，修改 `el-switch` 组件的 `active-value` 为“是”，`inactive-value` 为“否”，并调整 `el-switch` 的位置。
画面14：浏览器中显示 SaaS 企业列表页面，表格中显示“暂无数据”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```vue
<el-table :data="dataList" border style="width: 100%">
  <el-table-column fixed prop="index" label="序号" width="50"></el-table-column>
  <el-table-column fixed prop="name" label="企业名称" width="200"></el-table-column>
  <el-table-column fixed prop="version" label="当前版本" width="150"></el-table-column>
  <el-table-column fixed prop="companyphone" label="联系电话" width="150"></el-table-column>
  <el-table-column fixed prop="expirationDate" label="截止时间" width="150"></el-table-column>
  <el-table-column fixed prop="state" label="状态" width="150"></el-table-column>
  <el-table-column fixed="right" label="操作" width="150">
    <template slot-scope="scope">
      <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
    </template>
  </el-table-column>
</el-table>
```

画面7：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面8：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面9：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="1"
    inactive-value="0"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面10：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="1"
    inactive-value="0"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面11：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="是"
    inactive-value="否"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面13：
```vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="是"
    inactive-value="否"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
