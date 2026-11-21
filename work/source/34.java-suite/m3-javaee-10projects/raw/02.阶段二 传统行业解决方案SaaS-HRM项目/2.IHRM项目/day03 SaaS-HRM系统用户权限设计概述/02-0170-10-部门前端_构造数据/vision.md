# 画面线理解：10-部门前端：构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\10-部门前端：构造数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:08, 00:26, 01:25, 01:46, 02:06, 02:16, 02:57, 03:45, 04:13, 04:45, 05:09, 05:21, 05:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:32:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 项目中为部门管理模块编写前端代码，包括定义 API 接口、实现数据获取与展示逻辑，并通过浏览器调试查看网络请求。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 API 文档，列出部门模块的 CRUD 接口：POST /department（添加）、GET /department（全部列表）、GET /department/{departmentId}（根据 ID 查询）、PUT /department/{departmentId}（修改）、DELETE /department/{departmentId}（删除）。
画面 2：展示项目文件目录结构，当前选中的是 pages 文件夹下的 index.vue 文件。
画面 3：在 VS Code 中编辑 index.vue 文件，定义 data() 函数，初始化 activeName、departData 和 depts 数组。
画面 4：在 VS Code 中编辑 index.vue 文件，导入 createAPI，并定义了多个 API 方法：list、find、save、deleteById、update、saveOrUpdate。
画面 5：在 VS Code 中编辑 index.vue 文件，导入 list 和 commonApi，定义 data() 函数，初始化数据。
画面 6：在 VS Code 中编辑 index.vue 文件，为 methods 添加 getlist 方法，准备调用 list API。
画面 7：在浏览器开发者工具 Network 面板中，准备录制网络请求，页面显示“Recording network activity...”。
画面 8：在 VS Code 中编辑 index.vue 文件，调用 list API 并在控制台打印响应数据。
画面 9：在浏览器开发者工具 Network 面板中，显示了 API 请求的响应数据，包括 code、message、data 等字段。
画面 10：在 VS Code 中编辑 index.vue 文件，使用 el-tree 组件构建部门树形结构。
画面 11：在 VS Code 中编辑 index.vue 文件，继续完善 el-tree 组件的结构，添加部门名称、负责人、状态等信息。
画面 12：在浏览器开发者工具 Network 面板中，显示了 API 请求的响应数据，包括 department、webpocket 等资源。
画面 13：在 VS Code 中编辑 index.vue 文件，继续完善 el-tree 组件的结构，添加操作下拉菜单。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```javascript
data() {
  return {
    activeName: 'first',
    departData: {},
    depts: []
  }
}
```

画面 4 代码：
```javascript
import { createAPI } from '@/utils/request'

// 1. 部门列表
export const list = data => createAPI('/company/department', 'get', data)
// 2. 根据ID查询
export const find = data => createAPI('/company/department/${data.id}', 'get', data)
// 3. 添加
export const save = data => createAPI('/company/department', 'post', data)
// 4. 根据ID删除
export const deleteById = data => createAPI('/company/department/${data.id}', 'delete', data)
// 5. 修改
export const update = data => createAPI('/company/department/${data.id}', 'put', data)
// 6. 保存更新
export const saveOrUpdate = data => { return data.id ? update(data) : save(data) }
```

画面 5 代码：
```javascript
import { list } from '@/api/base/dept'
import commonApi from '@/utils/common'

data() {
  return {
    activeName: 'first',
    departData: {},
    depts: []
  }
}
```

画面 6 代码：
```javascript
methods: {
  // 获取列表方法
  getList() {
    list().then(res => {
      console.log(res)
    })
  }
}
```

画面 10 代码：
```html
<div style="overflow: scroll;white-space:nowrap" class="treeBox">
  <div class="treeCon clearfix">
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
  </div>
</div>
```

画面 11 代码：
```html
<div style="overflow: scroll;white-space:nowrap" class="treeBox">
  <div class="treeCon clearfix">
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
  </div>
</div>
```

画面 13 代码：
```html
<div style="overflow: scroll;white-space:nowrap" class="treeBox">
  <div class="treeCon clearfix">
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
    <span class="fa fa-university" aria-hidden="true"></span>
    <span class="treeInfo">
      <div class="treeInfo">
        <span class="treeInfo">
          <em class="colGreen" title="在职人员">在职人员</em>
          <em class="colGreen" title="正式员工">正式员工</em>
          <em class="colGreen" title="试用员工">试用员工</em>
        </span>
      </div>
    </span>
  </div>
</div>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
