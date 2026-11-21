# 10-部门前端：构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\10-部门前端：构造数据_【海量资源尽在 ubkz.com】.mp4
- 时长 5分55秒（音频 356s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 请求的API我们也已经写好了那接下来我们就是着手去看一下如何当我在点击组织架构的时候在这个页面能够发送请求并且呢得到基础的数据OK那我们怎么做呢其实就是我们昨天给各位一起来画的那张图希望各位还有印象在第二天资料里面
[00:31] 就是我们这个叫做执行流程的这么一张图那我页面访问一个链接的时候它根据试图找到根据我们的路由配置找到试图那试图里面又有这么几个方法首先呢create是页面加载之前执行的它可以去执行指定的method那method当中调用API跟服务端后台拿到数据拿到数据之后是不是可以把数据绑定到我们的数据模型上啊
[00:56] 所以这是我们的一个基本的一个执行的流程所以接下来呢我们就根据这个流程在页面编写method调用通过create调用method是不是发送请求啊好了那接下来呢我们就可以着手把这几个方法给它填写出来那找到我们跳转的页面找到我们跳转的页面department index
[01:21] 在index上边首先我要用这个API我要引入API那引入API importOKfromAPI下的我们叫做base目录下的API下的base目录下的叫做dapt那你想从这个dapt里面引出什么方法比如说我想用listsale find等等那我这边直接就写比如说我要用list那我就引出list好了那接下来
[01:55] create方法可以调用method那我们在method的部分好了构造查询方法好了构造查询方法呢比如说呢我就叫做get list那get list方法我们可以调用list方法点Zin得到响应那接下来呢响应放到里面的回调函数当中response那么可以一起console点logres
[02:41] 一起来看一下能不能够获取到数据那当然了我们需要在create方法里面调用类似点get list好了这个我们写好了之后打开浏览器打开F12走各位来看发送了一个请求那并且呢发送的就是我们目标的这个地址啊localhouse9091companydepartments那么可以观察一下观察一下这边呢
[03:15] 发送了请求并且呢有相应的响应相应响应比如说company idcompany namecompany manager等等等等所有内容就都已经出来了好了呢这个发送了请求之后接下来呢就按照我们刚才看的那张图的一个执行逻辑是不是就可以是不是就可以把我们这个得到的数据给他想方设法的绑定到我们的数据模型部分啊那绑定到数据模型部分的时候注意
[03:45] 我们可以再来看一下我们打印的这个内容console打印的这个内容就目前来说我们打印的内容其实还是有点多里面有config data等等我们现在关注的是不是就想的这个数据是不是叫做data所以我在这边所以这边关注的是res.data注意.data里面有所有那我们是不是关注的是得到的这个真正的数据结构而不是code message或者success所以我这边继续.data
[04:16] 接下来把这个数据绑定到department data这个数据模型上即可OK那这样一来department data数据模型上就已经有值了那已经有值接下来我们观察一下页面页面有一些地方我们需要做一些修改比如说这边应该显示企业名称比如说这边要显示企业的负责人那显示企业名称我们找到需要修改的页面部分
[04:48] 那企业名称呢我们就可以把这段删掉可以做替换我们的所有内容都已经放到了模型depart data里面其中我们现在关注的是返回结果当中的company namecompany nameokcontrol c拿过来control v替换保存我们一起刷新一下看看效果好了这样一来企业名称已经有了
[05:20] 那好了除了企业名称之外呢这边还有企业的负责人企业的负责人那企业的负责人我们API返回的属性呢叫做company name叫做company manager找到页面部分负责人把它删掉depart date点负责人好了再刷新好了张三也已经查询出来了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 项目中为部门管理模块编写前端代码，包括定义 API 接口、实现数据获取与展示逻辑，并通过浏览器调试查看网络请求。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 API 文档，列出部门模块的 CRUD 接口：POST /department（添加）、GET /department（全部列表）、GET /department/{departmentId}（根据 ID 查询）、PUT /department/{departmentId}（修改）、DELETE /department/{departmentId}（删除）。
画面 2：展示项目文件目录结构，当前选中的是 pages 文件夹下的 index.Vue 文件。
画面 3：在 VS Code 中编辑 index.Vue 文件，定义 data() 函数，初始化 activeName、departData 和 depts 数组。
画面 4：在 VS Code 中编辑 index.Vue 文件，导入 createAPI，并定义了多个 API 方法：list、find、save、deleteById、update、saveOrUpdate。
画面 5：在 VS Code 中编辑 index.Vue 文件，导入 list 和 commonApi，定义 data() 函数，初始化数据。
画面 6：在 VS Code 中编辑 index.Vue 文件，为 methods 添加 getlist 方法，准备调用 list API。
画面 7：在浏览器开发者工具 Network 面板中，准备录制网络请求，页面显示“Recording network activity...”。
画面 8：在 VS Code 中编辑 index.Vue 文件，调用 list API 并在控制台打印响应数据。
画面 9：在浏览器开发者工具 Network 面板中，显示了 API 请求的响应数据，包括 code、message、data 等字段。
画面 10：在 VS Code 中编辑 index.Vue 文件，使用 el-tree 组件构建部门树形结构。
画面 11：在 VS Code 中编辑 index.Vue 文件，继续完善 el-tree 组件的结构，添加部门名称、负责人、状态等信息。
画面 12：在浏览器开发者工具 Network 面板中，显示了 API 请求的响应数据，包括 department、webpocket 等资源。
画面 13：在 VS Code 中编辑 index.Vue 文件，继续完善 el-tree 组件的结构，添加操作下拉菜单。

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

