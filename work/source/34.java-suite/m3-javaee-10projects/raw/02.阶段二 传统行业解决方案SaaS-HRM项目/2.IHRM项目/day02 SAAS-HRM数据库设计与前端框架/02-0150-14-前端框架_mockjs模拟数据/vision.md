# 画面线理解：14-前端框架：mockjs模拟数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\14-前端框架：mockjs模拟数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:07, 00:25, 01:43, 02:06, 02:40, 03:17, 03:40, 03:58, 04:07, 04:29, 05:13, 05:43, 06:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:15:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue 项目中通过 mock.js 模拟 API 请求，以实现前端数据的本地化展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 HRM 系统的登录或首页界面，页面显示“demo页面”，并有“首页”、“demo”等导航项。
画面 2：展示 HRM 系统的“操作日志”列表页，包含“操作类型”、“操作人”、“执行结果”、“操作时间”、“描述”等列。
画面 3：在 Visual Studio Code 中打开 `index.vue` 文件，展示用于渲染表格的 Vue 模板代码，包含多个 `<el-table-column>` 定义。
画面 4：在浏览器开发者工具中，点击“首页”按钮后，页面跳转至“/dashboard”路径，同时开发者工具显示“[MP] waiting for update signal from HMR...”。
画面 5：在 Visual Studio Code 中，`index.vue` 文件的编辑器中，光标位于 `<template>` 标签内，显示表格结构代码。
画面 6：在 Visual Studio Code 中，打开 `mock/index.js` 文件，展示 mock.js 的初始化配置和对 `/VtableV1/list`、`/VframeV1/profile`、`/VframeV1/login` 三个接口的模拟。
画面 7：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 8：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 9：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 10：在 Visual Studio Code 中，鼠标悬停在 `index.vue` 文件标签页上。
画面 11：在 Visual Studio Code 中，鼠标悬停在 `table.js` 文件标签页上。
画面 12：在 Visual Studio Code 中，打开 `table.js` 文件，展示一个用于处理分页和过滤的 JavaScript 函数，包含 `list: config`, `mocklist.filter`, `mocklist.reverse`, `mocklist.filter` 等逻辑。
画面 13：在浏览器开发者工具的 Network 面板中，显示了对 `localhost:8080` 的请求，状态码为 304 和 200，表明页面已成功加载。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```vue
<template>
  <el-table :data="datalist" fit highlight-current-row style="width: 100%" border>
    <el-table-column align="center" label="table.operationtype">
      <template slot-scope="scope">
        <span>{{scope.row.type}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.operator">
      <template slot-scope="scope">
        <span>{{scope.row.author}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.results">
      <template slot-scope="scope">
        <span>{{scope.row.title}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.operationdate">
      <template slot-scope="scope">
        <span>{{scope.row.display_time}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.describe">
      <template slot-scope="scope">
        <span>{{scope.row.forecast}}</span>
      </template>
    </el-table-column>
  </el-table>
</template>
```

画面 6：
```javascript
import Mock from 'mockjs';
import tableAPI from '@/table';
import ProfileAPI from '@/profile';
import LoginAPI from '@/login';

Mock.setup({
  // timeout: 1000
});

Mock.mock(/VtableV1\/list/, 'get', tableAPI.list);
Mock.mock(/VframeV1\/profile/, 'post', ProfileAPI.profile);
Mock.mock(/VframeV1\/login/, 'post', LoginAPI.login);
```

画面 12：
```javascript
export default {
  list: config => {
    const { type, page, limit = 20, sort } = paramObj(config.url);
    let mocklist = list.filter(item => {
      if (type && item.type !== type) return false;
      if (title && item.title.indexOf(title) < 0) return false;
      return true;
    });

    if (sort === '-id') {
      mocklist = mocklist.reverse();
    }

    const pagelist = mocklist.filter((item, index) => index < limit * page && index >= limit * (page - 1));

    return {
      total: mocklist.length,
      items: pagelist
    };
  }
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
