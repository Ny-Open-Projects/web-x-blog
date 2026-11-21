# 画面线理解：11-部门前端：构造部门树形列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\11-部门前端：构造部门树形列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:31, 00:52, 01:20, 01:41, 01:55, 02:32, 03:33, 03:45, 04:09, 04:36, 05:58, 06:18, 07:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:33:34

1) 这一组画面整体在讲如何在 Vue 项目中使用 Element UI 的树形组件（el-tree）实现部门组织架构的展示与增删改操作。

2) 按时间顺序列出每张画面的要点：
画面1：
- 编辑器中显示 Vue 组件 `index.vue` 的模板部分，包含一个 `el-tree` 组件，用于展示部门树形结构。
- 代码片段：
  ```html
  <div style="overflow: scroll;white-space:nowrap" class="treeBox">
    <span class="fa fa-university" aria-hidden="true"></span>
    <span><strong>{{departData.companyName}}</strong></span>
    <span class="fr">
      <span class="departInfo">
        <span class="colGreen" title="在岗人数">...</span>
        <span class="colGreen" title="正式员工">...</span>
      </span>
    </span>
    <div class="treeInfo">
      <div class="treeInfo">
        <span class="el-dropdown-link">
          <span class="el-icon-arrow-down el-icon-right"></span>
          <span class="el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click="handAddD">添加子部门</el-dropdown-item>
            <el-dropdown-item @click="handleListD">查看子部门员工</el-dropdown-item>
          </el-dropdown-menu>
        </span>
      </div>
    </div>
  </div>
  ```

画面2：
- 代码中 `el-dropdown-menu` 的 `slot="dropdown"` 语法被修改为 `slot-scope`，并添加了 `@click` 事件绑定。
- 代码片段：
  ```html
  <span class="el-dropdown-link">
    <span class="el-icon-arrow-down el-icon-right"></span>
    <span class="el-dropdown-menu slot="dropdown">
      <el-dropdown-item @click="handAddD">添加子部门</el-dropdown-item>
      <el-dropdown-item @click="handleListD">查看子部门员工</el-dropdown-item>
    </el-dropdown-menu>
  </span>
  ```

画面3：
- 浏览器地址栏显示 `Swagger UI`，页面为空白，表明正在访问 API 文档页面。

画面4：
- 浏览器中打开 Element UI 官网的 Tree 组件页面，展示了树形结构的使用示例，包含“使用 render-content”和“使用 scoped slot”两种方式。

画面5：
- 编辑器中显示 `el-tree` 组件的 `slot-scope` 语法，用于自定义节点内容。
- 代码片段：
  ```html
  <el-tree
    node-key="id"
    default-expand-all
    expand-on-click-node="false"
    slot-scope="{ node, data }"
  >
    <span class="custom-tree-node">
      <span>{{ node.label }}</span>
      <span>
        <el-button type="text" size="mini" @click="() => append(data)">Append</el-button>
        <el-button type="text" size="mini" @click="() => remove(node, data)">Delete</el-button>
      </span>
    </span>
  </el-tree>
  ```

画面6：
- Element UI 官网 Tree 组件页面，展示了“使用 scoped slot”示例的代码片段。
- 代码片段：
  ```html
  <div class="custom-tree-container">
    <div class="block">
      <el-tree
        :data="data"
        show-checkbox
        node-key="id"
        default-expand-all
        :render-content="renderContent"
      >
      </el-tree>
    </div>
  </div>
  ```

画面7：
- Element UI 官网 Tree 组件页面，展示了“使用 render-content”示例的代码片段。
- 代码片段：
  ```html
  <div class="custom-tree-container">
    <div class="block">
      <el-tree
        :data="data"
        show-checkbox
        node-key="id"
        default-expand-all
        :render-content="renderContent"
      >
      </el-tree>
    </div>
  </div>
  ```

画面8：
- 编辑器中显示 Vue 组件 `index.vue` 的脚本部分，正在编写 `getList` 方法，用于获取部门数据。
- 代码片段：
  ```js
  import { list } from "@/api/base/dept";
  import commonApi from "@/utils/common";
  export default {
    data() {
      return {
        activeName: 'first',
        departData: {},
        depts: []
      }
    },
    methods: {
      // 不选表格方法
      getList() {
        list().then(res => {
          this.departData = res.data.data;
          this.depts = commonApi.transformFreezFormat(res.data.depts);
        })
      }
    }
  }
  ```

画面9：
- 编辑器中显示 `getList` 方法的代码，正在添加 `transformFreezFormat` 方法对数据进行格式化。
- 代码片段：
  ```js
  this.depts = commonApi.transformFreezFormat(res.data.depts);
  ```

画面10：
- 浏览器中显示 HRM 系统的部门管理页面，页面标题为“组织架构”，显示了公司名称“江苏传智播客教育科技股份有限公司”。

画面11：
- 编辑器中显示 `index.vue` 的脚本部分，正在编写 `created` 生命周期钩子，用于在组件创建后调用 `getList` 方法。
- 代码片段：
  ```js
  created: function() {
    this.getList();
  }
  ```

画面12：
- Element UI 官网 Tree 组件页面，展示了 `el-tree` 组件的 `data` 数据结构示例。
- 代码片段：
  ```js
  export default {
    data() {
      return {
        data: [
          {
            id: 1,
            label: '一级 1',
            children: [
              {
                id: 4,
                label: '二级 1-1',
                children: [
                  {
                    id: 9,
                    label: '三级 1-1-1'
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  ```

画面13：
- 编辑器中显示 `index.vue` 的模板部分，使用了 `el-tree` 组件，并设置了 `data` 和 `slot-scope`。
- 代码片段：
  ```html
  <el-tree
    :data="depts"
    node-key="id"
    default-expand-all
    slot-scope="{ node, data }"
    style="width:100%"
  >
    <span class="custom-tree-node slot-scope="{ node, data }">
      <span>{{ node.label }}</span>
      <span>
        <el-button type="text" size="mini" @click="() => append(data)">Append</el-button>
        <el-button type="text" size="mini" @click="() => remove(node, data)">Delete</el-button>
      </span>
    </span>
  </el-tree>
  ```

画面14：
- 浏览器中显示 HRM 系统的部门管理页面，页面标题为“组织架构”，显示了多个部门，如“研发部”、“测试部”、“开发部”等，每个部门旁边有“Append”和“Delete”按钮。
