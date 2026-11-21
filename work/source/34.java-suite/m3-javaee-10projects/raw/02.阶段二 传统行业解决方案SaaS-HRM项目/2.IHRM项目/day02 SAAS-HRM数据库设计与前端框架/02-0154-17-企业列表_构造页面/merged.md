# 17-企业列表：构造页面

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\17-企业列表：构造页面_【海量资源尽在 ubkz.com】.mp4
- 时长 10分30秒（音频 630s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那目前呢我们的数据呢其实已经拿到了那拿到了之后呢接下来我们就需要把数据绑定到模型上那绑定到模型上之后去动态的影响我们页面相关的内容那怎么绑定到模型上呢这个也比较简单这个也比较简单我们可以在data部分定义这么一个数据模型比如说呢我叫做data例子当然了我只关注
[00:31] 我们查询之后的这个list集合或者list的数组那我这边就可以往里面绑直绑数组list.data list等于注意res.data.data它不是数组注意它不是数组res.data是这些我们关注的是里面的继续data里面是不是才有数组啊所以我这边继续打点dataOK那这样一来那这样一来我的data list里面就已经
[01:00] 有值了那有值了之后我们就可以去构造上面了那构造上面的时候呢我们先来一个最简单的比如说我来一个DIV来一个DIV在DIV当中呢我们可以借助VUE的语法去循环Data List好了叫做Vegan4那Vegan4里面的代码基本上都是比较固定的ITEM逗号IndexInDataListDataList
[01:35] 好了接下来呢冒号K指定索引好了接下来呢这里面就开始循环这个呢我简单的说一下它究竟代表什么意思啊这个代表的是我要去循环这个数组那循环数组的时候呢我这边声明这个数组里面有一个索引那我从根据索引从数组里面拿每一个元素拿到元素之后起一个名字叫做ITM所以呢在这个DIV当中我们ITM得到的其实就是数组当中的每一个元素也就是每一个起因信息
[02:06] 那我们可以借助Vue的语法两个大括号item.id加上两个大括号item.name当然了这个id和name是我们接口规范里面声明好的一些内容节列表id和name它都有嘛所以我这边拼接出来看一下能不能够展示到我们的页面上好了各位来看id有name是不是也有啊
[02:38] 那这样一来呢我们其实就已经拿到了数据并且把它展示到我们的面板上但是呢你会发现我们这回展示展示的太丑了但是我们这个原型展示的还不错但是我可以告诉各位啊这个原型构造起来极其简单为什么呢因为我们这套系统是用Vue结合恶冷门UI来搞定的那我在这边呢打开恶冷门UI的官方我们可以一起百度一下
[03:09] Element UI这个就是Element公司开源的一套产品它重点是为了构造页面的一些比较优美的一些组件的这个打开的稍微有点点慢各位耐心等待一下好了现在这个网站已经打开了打开了各位来看它其实是一套网站快速成型的一套工具我们其实就是把这套工具给它封装到我们的教授家工程里了
[03:37] 那我们关注的是Elema UI它里面的一些组件我们直接看组件其实就可以了那这个组件呢有很多左边都是它支持的一些组件比如说有布局比如说呢有它的一些容器的一些特征那除了这些特征之外呢还有一些比如说表格那这个表格里面的内容就比较多了就比较多了那我想看这不就是一个表格好了底下还有表格那还有表格那我们看一下我们的原型其实
[04:06] 跟好像跟Eleven UI这套差不多没错吧差不多差不多所以对于我们来说呢咱们可以借助人家的这个表格来完成操作即可那各位来看我们的原型当中我们的原型当中有这么还有这么一个列叫做查看叫做操作那我们找一个差不多组件的其实就可以了嗯往下找嗯找一个吧就这个固定列
[04:48] 那好了咱们来看一下它的代码是怎么实现的其实这个代码实现起来比较简单把里面的内容Ctrl C全拷过来注意拷的叫做EL TableEL Table拿过来那我们这边就不去自己循环了EL Table好了那接下来呢这个是我们的一个Table组件我先对这个代码呢做一个简单的格式化的一个处理OK好了接着呢这些基本上都差不多啊我就只留一个咱们举例说明问题就可以了好了那在这边
[05:31] 我想跟各位来聊的首先呢这是使用Elemen UI的table组件UI的table组件那这个Elemen UI这个table组件其中它有一个叫做data这个属性这个属性指的就是我们的数据模型所以对于我们而言这边不叫table data而叫做datalistCtrl C拷过来Ctrl VOK那接下来呢就是说呢在这个里面它有每一列
[06:09] 那每一列用什么表示呢我们可以用它里面提供的一个标签这个标签叫做EL table column它是用来构造表格当中的每一列的OK那接着呢在这个每一列当中呢它有一个prop那这个prop究竟代表的什么意思注意这个prop指的是你是不是要这边有三条数据那三条数据就应该构造这边打开原型来说明
[06:49] 三条数据就要够到三行那比如说呢这边我们有一个联系人那这个联系人是不是应该是用每一行数据或者每一个对象里面的某一个属性啊所以对于POP它其实指的是我们数组中每个元素对象属性名比如说呢我们这边呢想要展示它这个企业名称那我们用的其实就是数组当中的
[07:22] 注意是数组API是数组当中的数组当中每一个元素它的属性名这边用NameOK那这样一来咱们就已经构造好了一个表格我们可以刷新一下我们的页面给我来看0 1 2 3个其实就已经都出来了好了这个现在呢只是出现了一列啊那接下来呢我们就可以根据我们这边
[07:53] 原型上的一些配置我们可以一列一列的添加比如说企业名称还有当前版本联系人等等那配置的思路是差不多的那在这边每一个每一列呢我们用的是一个EL table column来几个能说明问题就可以了比如说这边有版本好了除了版本之外呢还有联系电话联系电话还有一些时间吧我这边简单的来几个联系电话
[08:34] 还有我们的叫做联系人还有我们的叫做截止时间那接下来再来一个叫叫叫什么所在地区OK再来一个叫状态好了我们剩下的事情就是可以改prop代表的是版本那版本我们用的是API当中我们规定的一个字段叫做washing所以我这边替换Ctrl C拿过来washing
[09:11] 那联系电话同样的找到我们的API联系电话呢叫做phone什么什么phonecompany phoneOK好了抱歉这个API呢今天不小心我做了一个修正啊就是我把这个下滑线不小心给搞出来了所以注意对于各位来说要注意这边呢没有什么下滑线全部都是中文大写啊抱歉好了接下来还有联系人联系人呢我们叫做联系人
[09:52] 没找到没找到这个不要了还有一个时间嗯data好了就来这两个吧当然了还有一个叫做状态状态stateok好了我们可以刷新一下页面那各位来看基本的这个页面呢其实也已经给它构造出来了已经给它构造出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Vue.js 和 Element UI 框架开发一个 SaaS 企业管理系统，重点展示表格组件的使用、数据绑定和 API 接口调用。

2) 按时间顺序列出每张画面的要点：
画面1：展示 SaaS 企业管理系统登录后的首页，包含“SAAS企业”管理模块，下方是浏览器开发者工具，显示了页面加载的网络请求和响应数据。
画面2：在 Visual Studio Code 中打开 Vue 项目，展示 `index.Vue` 文件的模板部分，使用 `v-for` 循环渲染数据列表。
画面3：在百度搜索框中输入“echarts”，展示搜索建议。
画面4：在 Element UI 官网展示“带边框表格”组件，表格包含“日期”、“姓名”、“地址”等列。
画面5：在 Element UI 官网展示“流体高度”表格，表格列包含“日期”、“姓名”、“省份”、“市区”、“地址”、“操作”。
画面6：在 Element UI 官网展示“固定列”表格示例，代码中使用 `fixed` 属性固定列。
画面7：在 Visual Studio Code 中编辑 `index.Vue` 文件，添加 Element UI 的表格组件，并设置列的 `prop` 和 `label`。
画面8：在 Element UI 官网展示“固定列”表格的代码示例，包含 `border`、`style`、`fixed` 等属性。
画面9：展示 SaaS 企业管理系统中的“客户”列表页面，包含“当前版本”、“联系人”、“联系电话”、“所在地区”、“申请时间”、“状态”、“操作”等列。
画面10：展示“客户”列表页面的滚动条，显示数据列表。
画面11：展示“客户”列表页面，包含“序号”、“企业名称”、“当前版本”、“联系人”、“联系电话”、“所在地区”、“申请时间”、“状态”、“操作”等列。
画面12：在 Visual Studio Code 中编辑 `index.Vue` 文件，添加 Element UI 的表格组件，并设置列的 `prop` 和 `label`。
画面13：展示 SaaS 企业管理系统中的“API 文档”页面，包含 GET、PUT、DELETE 三个 HTTP 方法的接口。
画面14：展示 SaaS 企业管理系统中的“企业”列表页面，包含“企业名称”、“版本”、“联系电话”、“截至时间”、“状态”、“操作”等列。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <div v-for="(item, index) in dataList" :key="index">
          <el-card>
            {{item.name}}
          </el-card>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面6：
```Vue
<template>
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="地址">
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  },
  methods: {
    handleClick(row) {
      console.log(row)
    }
  }
}
</script>
```

画面7：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <el-table :data="dataList" border style="width: 100%">
          <el-table-column fixed prop="name" label="企业名称" width="150"></el-table-column>
          <el-table-column fixed prop="phone" label="联系电话" width="150"></el-table-column>
          <el-table-column fixed prop="address" label="所在地区" width="150"></el-table-column>
          <el-table-column fixed prop="applyTime" label="申请时间" width="150"></el-table-column>
          <el-table-column fixed prop="status" label="状态" width="150"></el-table-column>
          <el-table-column fixed prop="operation" label="操作" width="150"></el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面12：
```Vue
<template>
  <div class="dashboard-container">
    <div class="app-container">
      <el-card shadow="never">
        <el-table :data="dataList" border style="width: 100%">
          <el-table-column fixed prop="name" label="企业名称" width="150"></el-table-column>
          <el-table-column fixed prop="phone" label="联系电话" width="150"></el-table-column>
          <el-table-column fixed prop="address" label="所在地区" width="150"></el-table-column>
          <el-table-column fixed prop="applyTime" label="申请时间" width="150"></el-table-column>
          <el-table-column fixed prop="status" label="状态" width="150"></el-table-column>
          <el-table-column fixed prop="operation" label="操作" width="150"></el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    getList() {
      list().then(res => {
        this.dataList = res.data
      })
    }
  }
}
</script>
```

画面13：
```json
{
  "success": true,
  "message": "string",
  "data": [
    {
      "id": "string",
      "name": "string",
      "manager_id": "string",
      "regional_date": "string",
      "expiration_date": "string",
      "company_code": "string",
      "business_license_id": "string",
      "legal_representation": "string",
      "company_phone": "string",
      "mail_box": "string",
      "company_site": "string",
      "industries": "string",
      "rewards": "string",
      "audit_status": "string",
      "state": "string",
      "balances": "string",
      "create_time": "string"
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：无 PPT 内容。
画面2：无 PPT 内容。
画面3：无 PPT 内容。
画面4：无 PPT 内容。
画面5：无 PPT 内容。
画面6：无 PPT 内容。
画面7：无 PPT 内容。
画面8：无 PPT 内容。
画面9：无 PPT 内容。
画面10：无 PPT 内容。
画面11：无 PPT 内容。
画面12：无 PPT 内容。
画面13：无 PPT 内容。
画面14：无 PPT 内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

