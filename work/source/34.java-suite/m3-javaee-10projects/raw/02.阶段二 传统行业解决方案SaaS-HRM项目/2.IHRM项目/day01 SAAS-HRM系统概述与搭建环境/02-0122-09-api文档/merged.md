# 09-api文档

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\09-api文档_【海量资源尽在 ubkz.com】.mp4
- 时长 5分8秒（音频 308s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那除了这个系统结构图之外呢咱们第三节呢还有一块内容就是一个API文档那这个API文档是什么呢为什么要重点拿出来提呢是因为我们刚才说过了前后端维系关系是通过一个接口文档我们用的是SWAGA那对于这个SWAGA文档来说它不是我们学习的重点但是我已经给各位提供好了那么可以一起来看一下今天给各位准备的这个资料
[00:34] 打开资源找到API好了这边呢它其实是一个已经打包好的一个NGX服务器我已经做好了所有的操作把所有的API已经放到这个NGX里面了那对于各位来说直接双击解压解压好了之后那就是这样的API跟NGX点击进去点击进去找到NGX.exe双击运行即可好了我这边已经双击运行了那运行成功了之后
[01:03] 我们可以打开浏览器那我这个NGX自己改造过它的访问端口呢就是801那么可以一起来看一下localhost801点击回车那各位来看这个就是我们整个的一个API文档的一个说明里面的API有很多比如说有企业的有组织结构的有用户员工的角色的权限的工资的等等等等有很多那我以其中的企业为例点击过来
[01:34] 那里面就会说明了你当前我们需要在企业这个服务当中需要给他提供一系列的接口这些接口里面包含增加的查询列表的还有根据ID查询的修改的等等等等有很多有很多那比如说我以添加一个企业为例来看一下点开它往下走你会发现
[02:04] 你发现需要你往后台传递数据,parameter代表参数嘛,就是你前端要往后端传递的数据,那传递的数据我要封装成一个company实体类,那你传递的数据要包含这些所有的内容等等等等,比如说有Name,比如说有Version,比如说等等等等这些内容,那好了继续往下看,继续往下看,那你当前传递过来了一些参数,我们后端进行处理,
[02:34] 那处理之后必然有响应必然有响应那response代表响应那响应的其实也是一个阶层走串那接下来就是响应的时候呢我们发送一个请求必然会有一个叫做返回的一个状态咱们大家都知道HTTP返回状态200代表成功200代表我的请求是成功的那你请求成功不代表真正的我后台处理成功
[03:01] 那我们处理成功全部是以返回值的形式告他的也是一阶层子不串其中code代表的是一个返回码当然了我这边这个文档是举了一个例子写了一个零当然这个返回码是我们前端之间前后端之间要做约定的这个约定我们一会写代码的时候再说那除了返回码之外还有flag代表是你真正的操作成功还是失败了当然了还有可能携带一些你这个说明比如说你操作成功了为什么成功啊为什么操作是成功的
[03:31] 比如说你操作失败了有用户名密码登录错误这些就是一些说明也应该给他携带过来那这些我们看过了之后还有一个就是说你请求或者响应的时候请求或者响应的时候有这么多参数那这些参数究竟代表的是什么含义究竟代表的什么含义底下有说明比如说company他有就这玩意儿他都有说明我就不一个一个举例去说了比如说他有name代表的是公司名称
[04:00] 比如说它有版本Bosch当前你用的是哪个版本的系统比如这边的Mailbox代表的是邮箱等等OK那咱们大致的对这个API文档做了一个简单的介绍其实是想各位知道前后端维系关系前端除了传递什么参数后端需要做出什么样的响应里面的数据格式是什么我们全部是借照API的形式来做的只不过我们这个API是借助Swaga文档的形式来做的但是这个Swaga文档不是我们的重点
[04:31] OK好了到目前为止就跟各位简单的分享了一下我们HRM系统它的一个设计我们的开发方式前后端分离维系关系通过文档SWAGA文档技术架构前端用的是VUE生态后端用的是Sprung全家桶这边是它的一个系统结构图当然了比较复杂随着课程深入我们会不断的讲解
[04:56] 那简单的还说了一个API文档我们用的是Swaga当然了各位不需要重点关注只需要和我一样解压了资金灯的资料打开它访问即可

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 SaaS-HRM 系统的前后端分离架构、技术栈、API 文档及工程搭建要求。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 的“3.4 API文档”章节，说明系统提供 Swagger 编写的 API 文档，并与 Nginx 整合，访问地址为 http://localhost:801。
画面 2: 展示 PPT 的“3.1 开发方式”章节，图示前端与后端通过“接口文档”（Swagger）交互。
画面 3: 展示 SaaS-HRM 系统的前端管理界面，包含工作日历、快速导航和绩效指数等模块。
画面 4: 展示浏览器地址栏输入 http://localhost:801，页面跳转至 Google 搜索页，说明该端口可访问 API 文档。
画面 5: 展示 Swagger API 文档页面，显示“API-Company”模块的接口列表，包括 POST、GET、PUT、DELETE 等操作。
画面 6: 展示在 Swagger 中点击“POST /company 增加Company”接口，准备发送请求。
画面 7: 展示“POST /company 增加Company”接口的请求体（body）参数，包含 Company 实体的 JSON 结构。
画面 8: 展示“POST /company 增加Company”接口的响应示例，返回状态码 200 和成功信息。
画面 9: 展示 Swagger API 文档页面，显示“API-Company”模块的接口列表。
画面 10: 展示“API-Company”模块中“Company”实体的字段列表，包括 id、name、managerId 等。
画面 11: 展示“API-Company”模块中“Models”部分，显示 Company 实体的 JSON Schema 结构。
画面 12: 展示在 Swagger 中点击“DELETE /company/{companyId} 删除Company”接口，准备发送请求。
画面 13: 展示 PPT 的“3.3 系统结构”章节，图示前端（Vue.js）与后端（Spring全家桶）通过 Nginx 交互。
画面 14: 展示课程 PPT 的“3.4 API文档”章节，说明系统提供 Swagger 编写的 API 文档，并与 Nginx 整合，访问地址为 http://localhost:801。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 7:
```json
{
  "id": "string",
  "name": "string",
  "managerId": "string",
  "version": "string",
  "renewalDate": "string",
  "expirationDate": "string",
  "companyArea": "string",
  "companyAddress": "string",
  "businessLicenseId": "string",
  "healthBox": "string",
  "companySize": "string",
  "industry": "string",
  "ceramics": "string",
  "auditState": "string",
  "state": "string",
  "balance": "string",
  "createTime": "string"
}
```

画面 8:
```json
{
  "Code": 6,
  "flag": true,
  "message": "string"
}
```

画面 11:
```json
Company {
  id: string
  name: string
  managerId: string
  version: string
  renewalDate: string
  expirationDate: string
  companyArea: string
  companyAddress: string
  businessLicenseId: string
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图结构：前端 → 接口文档 → 后端；接口文档 → Swagger。
画面 13: 架构图结构：前端（Vue.js）←→ Nginx ←→ 后端（Spring全家桶）。
画面 13: 表格数据（PPT 文本）：
(1) 前端技术栈：以 Node.js 为核心的 Vue.js 前端技术生态架构。
(2) 后端技术栈：Spring Boot+Spring Cloud+SpringMVC+SpringData (Spring全家桶)。

5) 不要评价画面美观，不要输出与课程无关的内容。

