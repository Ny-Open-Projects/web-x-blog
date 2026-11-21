# 16-企业列表：构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\16-企业列表：构造数据_【海量资源尽在 ubkz.com】.mp4
- 时长 9分28秒（音频 568s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那到目前为止呢我们的API也已经构造出来了那构造出来API之后按照我们刚才的这张图形的一个分析我们可以构造它整个的执行的这么一个过程也就是说接下来呢我要搞出来企业列表那要搞出企业列表那我们就可以在页面的crate的方法调用methodmethod是不是去调用我们写好的API啊那我们先把这个
[00:31] 方法的调用过程先给它构造出来那找到我的代码找到我的代码部分找到src找到里面的model-sasclient找到index.Vue那我在created的方法呢咱们之前就做过演示了我在created里面可以去调用method那method又要去调用api那对于api来说我们也需要把它引入到当前的我们这个代码框当中
[01:03] 好那我们一起来看一下如何引入啊其实这个代码如果不会写的话咱们可以参照人家的demo人家demo部分呢这些内容都是已经为我们准备好的好了Ctrl C我call过来Ctrl V好了这个代表的含义是从API里面引出它的list方法那我们的API在哪呢放到了API目录下base文件夹下我们叫做sas client
[01:35] sasklintOK那这样一来list方法就已经有了那list方法有了之后我们可以method写一个我们自己的方法比如说就叫做get list那get list方法是不是可以调用我们API的list方法完成操作list.好了list注意这个是发起我们请求调用API发起请求
[02:06] 那发起请求之后呢必然有响应那如何获取响应我们接触的是一个zin来做的它指的是获取响应结果那获取响应结果里面接收的是一个回调函数res好了这种写法呢比较怪比较怪但是它确确实实是我们js里面的一个函数ok那这个res其实代表的就是我们的响应数据那我们可以在这边呢console.log
[02:43] 把我们这个res打印出来一起来看一下效果一会儿好了那我们get list方法写好了之后我们是不是可以通过created调用get list那调用的方式呢比较简单list.get list即可那这样一来当页面创建完毕的时候它就会帮我去调用get list调用get list发送请求得到数据我们把它在空台输出出来OK
[03:14] 我们这些基本的代码我们写好了那但是呢就是说现在我这个API发送到什么地方我们还不知道那发送到我们的后台后台我还没有那这个时候我们怎么办呢哎没错我们刚才说过在我们这个代码当中它支持我们自己去构造模拟数据所以我在这边呢打开MOOC在MOOC里面我们可以构造一些
[03:41] 简单的模拟数据我们先不发送到后台我先请求到我的模拟数据看一下能不能它拦截我请求的API接口能不能把数据先给我返回到我们先把前端都调好了再去联系后端那这样我们调的顺序就比较效率就比较高一些那这个MOK.js这个代码好了在这边创建一个文件比如说我就叫做company.js那这个company.js里面
[04:13] 模拟的数据咱们就不再一行一行写了实在是太麻烦了那在今天的资料里面有一个代码company把你的内蒙Ctrl C拷过来Ctrl A拷过来即可好了那需要各位注意的是需要各位注意的是在这个代码里面注意在这个代码里面我返回了两个方法一个叫list一个叫做sas detail
[04:40] 上面其实是访问列表底下访问的其实就是SUSDEL当然我构造的这些数据其实严格的按照了我们的API接口来构造的比如说我举一个例子我们有一个全部列表全部列表响应的数据有code有code有success有success有message我这边说成功还有data代表的是一个数组这里面数组有很多
[05:10] 那我这里面搞了一个data搞了一个listlist其实是一个数组当然了我这边循环了一下构造了三条数据OK那这样一来我们可以拦截一下我们请求的URL后缀让它去执行list方法同样的这边有一个sus.data那sus.data指的是我们一会儿要完成的根据ID查询根据ID查询有响应code success message datacode success message data
[05:39] 对它里面这回根据ID查询返回的对象只有一个OK好了这个模拟数据我们添加进来之后我们需要配置一把写到底下就是配置我们的模拟数据接口好了配置的时候呢首先呢在上边我也可以把我们刚才写好的这个API引入进来模拟数据的APICMPAN1 Company API这边就叫做CMPAN1 CompanyOK那好了接下来
[06:13] 底下可以匹配我们拦截UIL的后缀那我们这回请求的地址呢就叫来各位来看我请求列表的时候company所以我这边-companyOK那我们请求的方式呢get这个样来我们其实访问企业列表那访问企业列表我们调用的就是company API那company API里面
[06:52] 的list方法所以这边list去构造模拟数据那除了这个之外呢我们还有一个还有一个那我们这回拿到的其实就是详情详情我们访问的是company下这边各位来看是不是应该有一个id呀那id其实代表的是一个字幕串嘛那所以我这边匹配的时候呢我也匹配ok点心
[07:29] 好了那接下来呢这边呢我们就可以配置上company API这回呢应该叫做sas detail了sas detail好了这边就是根据ID查询当然了各位来看啊这个company里面配置的这边能支持正责别达式啊正责别达式OK好了这样一来呢我的API接口呢其实咱们就已经匹配成功了
[07:54] 匹配成功了那匹配成功之后我们可以一起刷新一下页面看一下我们刚才打印的内容究竟有没有数据别忘了我请求过来之后调用get listlist方法那list方法呢我们刚才看过API里面的list方法请求的路径-company那我这边一请求路径company的话我们的moke.js我们的moke.js就会拦截就会拦截
[08:27] 把我们自己购到的数据给我们返回过来好了我们一起来看一下打开F2看一下控台刷新好了各位来看现在它已经出现了一些内容出现的内容有很多有config等等一大堆但是对于我来说我注重关注的是我们返回结果难道我要什么config什么header什么request吗我不需要
[08:59] 我只关注的是Data这个对象里面的这些内容对象里面才有1万才有这些数据才有查询成功等等所以呢我这边的写法打印出来RS点Data才是我关注的内容来再来刷新一把好了给我来看这样一来1万代表成功好了查询成功等等Data里面有三条数据我们已经构造出来了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue 项目中通过 Mock.js 模拟公司管理模块的 API 接口，以实现前端页面的数据展示和交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Visual Studio Code 中打开 `saasClient.js` 文件，展示用于创建 API 的代码，其中包含 `createAPI` 函数的调用。
画面 2: 展示了公司管理模块的 API 文档，包含 POST 和 GET 请求的接口定义。
画面 3: 在 `index.Vue` 文件中，展示 `getlist()` 方法的定义，用于获取公司列表。
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

