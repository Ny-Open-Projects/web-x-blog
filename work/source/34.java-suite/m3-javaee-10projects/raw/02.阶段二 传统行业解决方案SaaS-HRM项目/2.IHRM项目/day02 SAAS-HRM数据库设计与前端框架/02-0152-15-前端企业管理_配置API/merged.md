# 15-前端企业管理：配置API

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\15-前端企业管理：配置API_【海量资源尽在 ubkz.com】.mp4
- 时长 4分14秒（音频 254s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 目前呢我们已经把这个SaaS企业相应的这个菜单挂载上了并且也能够跳转到当前这个页面其实就是根据我们刚才那张图的步骤来的首先请求地址搞定了之后接着呢找到我们的视图那接着找到视图之后我们开始第三第四第五第六第七第八那我们一个一个来进行构造首先呢在这边的create方法去调用我们的methods
[00:31] 那Message是不是要去调用的API方法呀所以这些API等等的内容我们还没有准备那接下来呢我们就先把这个API方法先给它搞出来那对于这个API方法我们应该如何去做呢其实很简单我们之前说过了只要设计到的API全部放到API这个目录下你放到哪儿其实无所谓比如说呢我就放到base下边了那右键创建一个文件
[01:00] 那创建的这个文件我比它叫做就叫做sasclint.js那就是我们的API那里面的写法应该怎么去做呢其实我们可以参照刚才这个table可以参照它Ctrl C这边拿过来Ctrl V这个是引入相应的这个工具类这个工具类是人家框架把我们封装好的那table这里面呢它构造了一个方法叫做list
[01:26] 可以接收参数create API你的请求路径在什么地方你的请求方式还有你的数据究竟是什么那接下来呢我们就参照人家的这个代码拿过来control v好了只不过我们现在请求的路径我就这路径变了那这个路径变了呢这个时候我想跟各位来聊的就是说呢在view it配置请求路径的时候
[01:51] 特别是我们结合这种MOOCJS的时候进行配置你可以写完整路径你也可以写部分的请求路径为什么可以写部分的请求路径是因为在我们这个VOE总配置的Config当中这边可以结合DV或结合POD配置它的前缀比如说我要配置这个它就会帮我拼接上上面的内容当然了这个PowerDuck是我们正式生产环境的
[02:20] 上面DVDV这个是我们的测试环境相关的配置OK那这个配置它究竟是什么写法我们一会还会再说那我们先把这个请求的这个路径先给它配置上好了配置上之后呢它会结合上我们运行环境帮我们拼接它的前缀当然了这些前缀我们也需要在DV或者product配置文件里面进行一个配置
[02:44] 好了那这样一来呢我第一个list呢其实方法写好了但是我现在请求的路径在什么地方呢咱们可以一起来看一下我们的API接口在API接口当中呢企业当中我们一起来找我们现在查询的是全部企业列表那请求的就叫做Gang Company所以呢我这边请求的路径C-O-M-P-A-N-Y Company那我们的请求方式查询全部listAGet没问题Data好了那这样一来我第一个
[03:17] 咱们就已经写好了那第一个写好了之后呢接下来有第二个那因为我一会儿还要完成查询根据ID查询那根据ID查询呢我这边来一个叫做Detail这是我的方法名那Data好了这边呢Create API没什么问题那根据ID进行查询那各位来看我们的请求方式Get那后边是不是要接我们的请求的一个参数那参数呢全部在Data当中那我们就可以Gang
[03:47] 到了大括号拼接我们的一下字符串这个模板字符串进行拼接从Data对象当中拿出来它的ID属性OK那这样一来Data代表的是一个对象你请求的所有数据所有数据里面如果有ID它就会给你拼接到后边了OK那这样一来咱们的两个API方法就已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个基于 Vue.js 的 SAAS 企业管理系统前端页面与后端 API 的交互实现，包括路由配置、组件结构、数据模型绑定以及 API 接口文档的查看。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 SAAS 企业管理系统登录后的首页，标题为“江苏传智播客教育科技股份有限公司”，页面显示“SAAS企业管理”和版权信息。
画面 2: 展示一个 PPT 页面，内容为 Vue.js 组件结构图，包含：
- 1: URL `http://localhost:8080/4/saas-clients/index`
- 2: `demo/pages/index.Vue` 视图
- 3: `created()` 方法（Vue钩子函数）
- 4: `method()` 方法
- 5: 调用 `method()` 方法
- 6: `API方法` 指向 `java服务端后台`
- 7: `data()` 数据模型（双向绑定）
- 8: `<template>` HTML 标签
画面 3: 与画面 2 内容相同，为同一张 PPT 页面。
画面 4: 与画面 2 内容相同，为同一张 PPT 页面。
画面 5: 与画面 2 内容相同，为同一张 PPT 页面。
画面 6: 展示 Visual Studio Code 中的项目目录结构，右键点击 `src` 文件夹，弹出菜单，显示“创建文件”、“创建文件夹”等选项。
画面 7: 展示 Visual Studio Code 中 `saasClient.js` 文件内容，代码为：
```javascript
import { createAPI, createFormAPI } from '@/utils/request';
export const list = data => createAPI('https://mock.issug.com/mock/29/label/list', 'get', data);
```
画面 8: 展示 Visual Studio Code 中 `saasClient.js` 文件内容，代码为：
```javascript
import { createAPI, createFormAPI } from '@/utils/request';
export const list = data => createAPI('https://mock.issug.com/mock/29/label/list', 'get', data);
```
画面 9: 展示 Swagger API 文档页面，显示 `POST /company` 接口，请求体为 `Company` 实体，包含 `id`, `name`, `manager_id`, `created_date`, `expiration_date`, `company_address`, `company_phone`, `legal_representative`, `company_email`, `company_website`, `company_industry`, `company_state`, `balance`, `create_time` 等字段。
画面 10: 展示 Swagger API 文档页面，正在加载 `api/company.yml` 文件。
画面 11: 展示 Visual Studio Code 中 `saasClient.js` 文件内容，光标位于第 3 行。
画面 12: 展示 Visual Studio Code 中的多窗口切换界面，显示多个软件窗口，包括：
- `SaaS-HRM系统API文档`
- `Microsoft Excel`
- `PowerDesigner - IPDM`
- `SQLyog Ultimate`
- `SaaS-HRM-架构.pdf`
画面 13: 展示 Swagger API 文档页面，显示 `POST /company`、`GET /company`、`PUT /company/{companyId}`、`DELETE /company/{companyId}` 四个接口。
画面 14: 展示 Visual Studio Code 中 `saasClient.js` 文件内容，代码为：
```javascript
import { createAPI, createFormAPI } from '@/utils/request';
export const detail = data => createAPI('/company', 'get', data);
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7 代码：
```javascript
import { createAPI, createFormAPI } from '@/utils/request';
export const list = data => createAPI('https://mock.issug.com/mock/29/label/list', 'get', data);
```
画面 14 代码：
```javascript
import { createAPI, createFormAPI } from '@/utils/request';
export const detail = data => createAPI('/company', 'get', data);
```
画面 9 JSON 数据：
```json
{
  "id": "string",
  "name": "string",
  "manager_id": "string",
  "created_date": "string",
  "expiration_date": "string",
  "company_address": "string",
  "company_phone": "string",
  "legal_representative": "string",
  "company_email": "string",
  "company_website": "string",
  "company_industry": "string",
  "company_state": "string",
  "balance": "string",
  "create_time": "string"
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2、3、4、5 的 PPT 内容：
- 节点 1: URL `http://localhost:8080/4/saas-clients/index`
- 节点 2: `demo/pages/index.Vue` 视图
- 节点 3: `created()` 方法（Vue钩子函数）
- 节点 4: `method()` 方法
- 节点 5: `API方法` 指向 `java服务端后台`
- 节点 6: `API方法` 指向 `java服务端后台`
- 节点 7: `data()` 数据模型（双向绑定）
- 节点 8: `<template>` HTML 标签
- 节点 7 与 8 之间有“双向绑定”箭头
- 节点 5 与 6 之间有“调用method方法”箭头
- 节点 7 与 5 之间有“修改数据模型”箭头

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

