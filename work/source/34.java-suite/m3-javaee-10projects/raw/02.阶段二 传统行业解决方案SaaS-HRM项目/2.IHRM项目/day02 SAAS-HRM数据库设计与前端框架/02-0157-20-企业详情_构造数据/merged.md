# 20-企业详情：构造数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\20-企业详情：构造数据_【海量资源尽在 ubkz.com】.mp4
- 时长 8分58秒（音频 538s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] OK目前的页面已经跳转过来了那跳转过来之后呢我们在这个页面重点要完成的事情呢其实第一个就是我们要构造相应的这样的一种样式那接下来呢完成第一个企业信息它的一个信息展示就可以了那我们要想完成这两件事首先第一个就构造这个样式那构造这个样式呢其实这个样式不是我们自己去做的
[00:28] 我们其实也是使用EleMUI提供的这一系列组件来构造出来的那这里面的组件呢其中有一个啊我们来找一下叫做Tips这个Tips各位来看和我们这种效果其实就一样的可以点击可以点击那我们在这边可以借助这个Tips来完成我们的这种需求好了我们一起来看一下人家是怎么做的看一下人家的源码好了里面有一个EL Tips
[00:57] 好了里面有用户管理等等等等有这么四个可选择的标签那它呢那怎么就能让它定位到初始是第一个还是第二个还是第三个呢各位我们一起来看一下首先呢这边有一个叫做V-model它叫做ActiveName那ActiveName代表的是我们模型当中的值ActiveName它返回的值你看叫做Second那各位来看这四个标签它都有一个名字叫做First Second Third还是Fourth那这样一来咱们就比较明确了
[01:26] 那如果让它默认显示第二个我这边就要second如果让显示用户完理我是不是就应该用first来做是不是就可以了所以对于我们而言要做的事情很明确Ctrl C把这一段copy到我们这个页面当中那copy到页面当中呢我们有一个模型叫做actual namedata部分data list不要了好了我们首先呢让它显示的是第一个叫做first好了那对于我这个案例只需要三个其实就可以了
[01:58] 当然这边有个table-clack这个玩意我们不需要不需要的话先把它删掉好了接下来我们一起关注的就是改一下名字其中有企业信息好了还有账户信息好了以及最后一个叫做交易记录我这边自己手动打吧OK这边呢构造一下构造一下好了那接下来model name first
[02:46] 哎force没问题好了我们再来看一下我们的页面刷新一把你发现默认显示的就是企业信息跟这个基本上是一样的一样的好了接下来呢默认显示企业信息那在企业信息当中我们接下来关注的第二件事刚才说过了就是根据ID发送查询得到数据把它展示出来好了那怎么得到数据把它展示出来呢这个其实也是分成两个操作啊第一件事
[03:19] 想方设法的我们发送请求得到数据第二件事才是去构造我们页面相关的内容那我们点击到这个页面的时候呢可以借助我们刚才总结的一点点内容借助里面的credit方法调用methodmethod发送请求但是前提条件我们得有API那API呢其实我们之前呢已经写好了已经写好了这边内容太多了我把所有内容都关掉我再重新打开我们的API之前写好了在API下
[03:49] base里面的susclient其中有一个叫做detail那我们要做的事情呢就是把这个detail引入到我当前的这个工程当中OK我从API里面获取detail那接下来呢底下我们通过create方法去调用method比如说呢这边method里写一个方法就叫做detail好了通过API打点z res
[04:25] 这个是一个固定写法各位写几次基本上就已经会了那接下来呢我们可以把这个内容绑定到我们的数据模型上比如说呢我这边有一个数据模型叫做比如就叫做formData它是一对象加一逗号那这样一来我们关注的其实就是list.formData.data.data别忘了第一个data代表的是所有得到的这个数据那我们关注的是封装到的data里面的内容
[04:59] 抱歉等于res.data.data好了但是我们可以看一下还是看一下我们刚才的这个接口这个接口当中Detail里面要得到一数据别忘了我们是根据ID查所以我们调用这个方法的时候就需要把ID属性给它传过去ID把这个ID属性给它传过去这个ID我们要从什么地方获取注意这个ID我们可以就在Detail这边
[05:30] 你给我传一ID我这边就把ID传过去好了那这个那在我们create的方法呢就可以调用detail完成我们需要的操作了那我们在create的部分呢其实能够得到我们当前动态路由当中的ID参数那这个参数呢可以借助类似点我们叫做dollar route r-o-u-t-e.p-r-a-m-sp-m-s.id
[06:04] 那这样一来就能得到我们的地址参数比如说就叫做哇ID好了接下来把ID传进到我们的Detail方法里面A即可好了那在这边呢我们可以先把这个数据给它打印出来我们看一下能不能够发送请求获取到数据console.log这玩意儿这些都比较简单OK好了当然了这个ID呢其实我们也可以打印出来console.logID
[06:40] 好了那接下来呢打开我们的页面打开F2刷新一把好像没有打印是吧好了刷新一把好了好像没有打印任何内容是吧那我们一起检查一下我们的代码哦各位来看这个create方法呢detail我们在create地方要调用detail里面的内容的话前面要加listok好了我们再来试一下刷新好了各位来看这边呢返回的类型不太对啊不太对
[07:20] 我们呢现在要关注的是得到的应该是我们的这个企业的详情而不是这个列表而不是列表那我们可以看一下为什么会有这个问题为什么会有这个问题首先呢我们能够验证当前传递的地址参数10已经拿到了已经拿到了打印出来了那接着来这是form date那这form date应该是详情那其实呢大致的想一下问题应该出现在我们模拟数据ezmoke这边
[07:47] 那模拟数据EasyMode的时候呢这边的配置的请求接口是company那其实在这个company进行配置的过程当中它内部接收的是政策表达式的形式来做的那所以对于我们现在呢它请求的地址啊请求到后端的地址恰巧呢就叫做-compy这种方式只不过后面加了一个十几一个数字是这样请求的但是对于这个政策表达式来说它其实也认为是
[08:17] 得到list集合了那接下来呢我们要做的事情很简单换一下顺序那接下来呢对这边的上边呢给它来一个我们的一个匹配好了这样一来代表的是杠后面任意加点内容加内容那它两个其实就已经不一样了不一样了底下这个上面这个其实代表的就是查询详情底下这个其实查询就是列表了好了我们一起来看一下修改了之后看一下企业列表没问题那看详情
[08:51] 来打印这回对象我们也已经就拿到了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Vue.js 和 Element UI 的 SaaS 企业管理系统前端页面的开发与调试过程，包括页面跳转、组件使用、代码编辑和浏览器开发者工具的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 SaaS 企业管理系统首页，左侧导航栏选中“SaaS企业”，页面显示“企业信息”、“账户信息”、“交易记录”三个标签页，当前选中“企业信息”，表单字段包括“公司名称”、“公司地区”等。
画面2：切换到 Element UI 官网，展示 Tabs 组件的代码示例，其中 `el-tabs` 标签被选中，代码中包含 `v-model="activeName"` 和 `@tab-click` 事件。
画面3：回到 SaaS 系统，鼠标悬停在“交易记录”标签上，页面显示交易记录列表，包含“操作类型”、“操作人”、“执行结果”、“操作时间”、“备注”等列。
画面4：切换到 Element UI 官网，展示 Tabs 组件的配置管理代码，包含 `el-tab-pane` 标签的 `label` 和 `name` 属性，以及 `v-model` 绑定。
画面5：回到 SaaS 系统，鼠标悬停在“交易记录”标签上，页面显示“交易记录”标签页，但内容为空。
画面6：切换到 Visual Studio Code，显示 `detail.Vue` 文件内容，包含 `el-tabs` 组件的模板和脚本部分，`import {list} from '@/api/base/saasClient'`，`name: 'saas-clients-detail'`，`data() { return { activeName: 'first' } }`。
画面7：回到 SaaS 系统，页面显示“SAAS企业”标签页，内容为空白，底部显示版权信息。
画面8：回到 SaaS 系统，鼠标悬停在“账户信息”标签上，页面显示“账户信息”标签页，表单字段包括“法人代表”、“公司电话”等。
画面9：切换到 Visual Studio Code，显示 `detail.Vue` 文件内容，`el-tabs` 组件的 `name` 属性被修改为“企业信息”、“账户信息”、“交易记录”。
画面10：切换到 Visual Studio Code，显示 `detail.Vue` 文件内容，`import {detail} from '@/api/base/saasClient'`，`name: 'saas-clients-detail'`，`data() { return { activeName: 'first' } }`。
画面11：回到 SaaS 系统，页面显示“SAAS企业”标签页，内容为空白，底部显示“[HRM] waiting for update signal from HDS...”。
画面12：切换到 Visual Studio Code，显示多个窗口，包括 `detail.Vue`、`SaaS-HRM-...`、`pages`、`api` 等文件夹，以及 `Microsoft Excel`、`SQLyog Ultimate` 等软件界面。
画面13：切换到 Visual Studio Code，显示多个窗口，包括 `detail.Vue`、`SaaS-HRM-...`、`pages`、`api` 等文件夹，以及 `Microsoft Excel`、`SQLyog Ultimate` 等软件界面。
画面14：回到 SaaS 系统，页面显示“SAAS企业”标签页，内容为空白，底部显示“[HRM] waiting for update signal from HDS...”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-tabs v-model="activeName" name="user">
        <el-tab-pane label="企业信息" name="first">
        </el-tab-pane>
        <el-tab-pane label="账户信息" name="second">
        </el-tab-pane>
        <el-tab-pane label="交易记录" name="third">
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import {list} from '@/api/base/saasClient'
export default {
  name: 'saas-clients-detail',
  data () {
    return {
      activeName: 'first'
    }
  },
  methods: {
  },
  created () {
  }
}
</script>
```

画面9：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-tabs v-model="activeName" name="user">
        <el-tab-pane label="企业信息" name="first">
        </el-tab-pane>
        <el-tab-pane label="账户信息" name="second">
        </el-tab-pane>
        <el-tab-pane label="交易记录" name="third">
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import {list} from '@/api/base/saasClient'
export default {
  name: 'saas-clients-detail',
  data () {
    return {
      activeName: 'first'
    }
  },
  methods: {
  },
  created () {
  }
}
</script>
```

画面10：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-tabs v-model="activeName" name="user">
        <el-tab-pane label="企业信息" name="first">
        </el-tab-pane>
        <el-tab-pane label="账户信息" name="second">
        </el-tab-pane>
        <el-tab-pane label="交易记录" name="third">
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import {detail} from '@/api/base/saasClient'
export default {
  name: 'saas-clients-detail',
  data () {
    return {
      activeName: 'first'
    }
  },
  methods: {
  },
  created () {
  }
}
</script>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

