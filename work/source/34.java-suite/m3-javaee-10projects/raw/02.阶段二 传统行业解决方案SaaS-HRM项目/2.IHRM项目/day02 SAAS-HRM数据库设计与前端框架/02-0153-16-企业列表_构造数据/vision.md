# 画面线理解：16-企业列表：构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\16-企业列表：构造数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:35, 02:12, 04:16, 04:34, 05:01, 05:20, 05:47, 06:10, 06:36, 06:56, 07:59, 08:34, 09:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:17:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue 项目中通过 Mock.js 模拟公司管理模块的 API 接口，以实现前端页面的数据展示和交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Visual Studio Code 中打开 `saasClient.js` 文件，展示用于创建 API 的代码，其中包含 `createAPI` 函数的调用。
画面 2: 展示了公司管理模块的 API 文档，包含 POST 和 GET 请求的接口定义。
画面 3: 在 `index.vue` 文件中，展示 `getlist()` 方法的定义，用于获取公司列表。
画面 4: 展示了项目文件夹结构，包含 `day1` 和 `day2` 文件夹。
画面 5: 在 `company.js` 文件中，展示公司数据模型的定义，包含多个字段如 `companyName`、`companyAddress` 等。
画面 6: 在 `company.js` 文件中，展示 `list()` 函数的返回值，包含 `code`、`success`、`message` 和 `data` 字段。
画面 7: 在 `company.js` 文件中，展示 `sassDetail()` 函数的返回值，包含 `id`、`name`、`managerId` 等字段。
画面 8: 在 `index.js` 文件中，展示导入 Mock.js 和其他 API 文件的代码。
画面 9: 在 `index.js` 文件中，展示 `Mock.setup()` 的配置，设置超时时间。
画面 10: 在 `index.js` 文件中，展示 `Mock.mock()` 的调用，用于模拟登录接口。
画面 11: 在 `index.js` 文件中，展示 `Mock.mock()` 的调用，用于模拟公司列表接口。
画面 12: 在 `index.js` 文件中，展示 `Mock.mock()` 的调用，用于模拟公司详情接口。
画面 13: 在浏览器开发者工具中，展示页面加载状态。
画面 14: 在浏览器中，展示公司管理模块的前端页面，包含导航菜单和公司管理标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
import (createAPI, createFormAPI) from '@utils/request';
export const list = data => createAPI('/company', 'get', data);
export const detail = data => createAPI('/company/${data.id}', 'GET', data);
```

画面 3:
```javascript
<script>
import { list } from '@/api/saasClient';
export default {
  name: 'saas-clients-index',
  data() {
    return {
    }
  },
  methods: {
    getList() {
      // 调用后端接口
      list().then()
    },
    created() {
    }
  }
}
</script>
```

画面 5:
```javascript
companyName: "string",
companyAddress: "string",
businessLicenseCode: "string",
legalRepresentative: "string",
companyPhone: "13800138000",
mailbox: "string",
companySize: "string",
industry: "string",
remarks: "string",
auditState: "string",
state: "1",
balance: "string",
createTime: "string"
```

画面 6:
```javascript
export default {
  list() => {
    return {
      code: 10000,
      success: true,
      message: "查询成功",
      data: list
    }
  },
  sassDetail() => {
    return {
      code: 10000,
      success: true,
      message: "查询成功",
      data: {
        id: "18001",
        name: "南京公司",
        managerId: "string",
        version: "此版本1.0",
        renewalDate: "2019-01-01",
        expirationDate: "2019-01-01",
        "string"
      }
    }
  }
}
```

画面 8:
```javascript
import Mock from 'mockjs';
import tableAPI from '@/table';
import profileAPI from '@/profile';
import LoginAPI from '@/login';
import CompanyAPI from '@/company'
```

画面 9:
```javascript
Mock.setup({
  // timeout: 1000
})
```

画面 10:
```javascript
Mock.mock(/\/Frame\/login/, 'post', LoginAPI.login)
```

画面 11:
```javascript
Mock.mock(/\/Frame\/profile/, 'post', ProfileAPI.profile)
```

画面 12:
```javascript
Mock.mock(/\/company/, 'get', CompanyAPI.list) //模拟企业列表
Mock.mock(/\/company/, 'get', CompanyAPI.sassDetail) //模拟企业详情
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
