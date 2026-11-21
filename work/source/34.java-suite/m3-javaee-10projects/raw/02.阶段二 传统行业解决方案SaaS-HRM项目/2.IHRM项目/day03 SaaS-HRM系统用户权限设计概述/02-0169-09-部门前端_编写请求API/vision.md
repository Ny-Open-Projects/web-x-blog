# 画面线理解：09-部门前端：编写请求API

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\09-部门前端：编写请求API_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:19, 01:27, 01:34, 01:41, 01:47, 02:46, 02:51, 03:15, 03:33, 05:32, 05:41, 06:11, 06:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:32:10

1) 这一组画面整体在讲什么（一句话）：
在 Vue.js 项目中，为 SaaS-HRM 系统的部门模块编写 API 请求函数，同时在浏览器中查看对应的 API 文档。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 SaaS-HRM 系统的“组织架构”页面，同时在任务栏预览了代码编辑器窗口。
画面 2: 在 Visual Studio Code 中，编辑 `src/api/depts.js` 文件，定义了获取部门列表的 API 函数 `list`。
画面 3: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 4: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 5: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 6: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 7: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 8: 在浏览器中打开了 API 文档页面，显示了 `/department` 路径下 POST、GET、PUT、DELETE 四种 HTTP 方法的接口。
画面 9: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 10: 在浏览器中，SaaS-HRM 系统的“组织架构”页面显示了“企业名称”输入框。
画面 11: 在 API 文档页面，点击了 POST 方法，查看了请求参数和示例值。
画面 12: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 13: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 14: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 3:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 4:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 5:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 6:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 7:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 9:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 12:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
```

画面 13:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
```

画面 14:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
export const saveDuplicate = data => createAPI('/company', 'post', data)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: API 文档页面，显示了 `/department` 路径下 POST、GET、PUT、DELETE 四种 HTTP 方法的接口。
画面 11: API 文档页面，显示了 POST 方法的请求参数和示例值。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
