# 18-企业列表：构造序号和专改列

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\18-企业列表：构造序号和专改列_【海量资源尽在 ubkz.com】.mp4
- 时长 6分5秒（音频 365s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 其实我们的数据列表呢已经构造出来了但是这个样式还是有点丑其中重点其实就是这每一列它的一个宽度那在这边呢我们可以做一个宽度的一个调整好了比如说就调整到150OK那好了我们这回再来看一下页面那会发现这回就相对来说好看一点了那其实呢对于我们来说呢我们的页面原型还有很多的内容比如说本月有多少这边还有搜索的框框等等这些内容我们还没做
[00:33] 如果各位有兴趣的话自己去把它补充完整就可以了那我们要说的是对于这个页面来说还有比如说下面有序号那这边呢还有一个这种状态的一个展示这是一种比较友好的一种方式那这两个点呢我们也把它构造出来首先看序号那对于序号来说呢它是在企业名称之前有这么一个一列有这么一列那这个列的名称呢我就叫序号了那这个序号应该怎么去做呢其实
[01:06] 不难其实比较简单只需要我们在这个列上呢给它指定一个type属性这个属性给它改成index集合这个是Elemy UI它提供的一种机制一改你一刷新立马就好使当然了这个宽度呢也可以给它指定一下width50OK那好了那序号搞定了之后呢还有一个状态那对于状态来说呢1这个看起来太丑了
[01:35] 那我们可以用更加良好的一些插件那比如说呢这边我们用的插件是一个选择器这是一个能够左右选择的跟我们手机其实差不多那其实这个选择器呢也在Elemen UI当中有体现我们一起找到Elemen UI找到选择器你会发现叫做Switch开关抱歉Switch开关找到这个开关你会发现这个和我们的案例其实就有点像那只不过呢我们这个案例是出来之后呢这个可以不让点击嘛
[02:06] 那不让点击那我们可以从其中一个拿过来拿过来Ctrl C准备替换那替换替换的就是我们这个状态那这个状态如何让它替换呢我先call过来我先call过来那接着就是说如何从一个table中向我们从一个column当中向我们的一个组件当中传递值其实底下就有一个案例你发现这边有一个行叫操作里面可以用一个template
[02:37] 包括你要添加的一些其他组件这都是固定的一个写法那Template注意里面传递的这个值呢叫做scope那我这边需要声明一把这个scope呢其实是一个我们叫做作用域啊那这个scope里面可以传递当前行的所有数据你当前这一行的所有数据那所有数据呢
[03:09] 我们怎么去传递呢其实scope里面都有那对于我们来说对于我们来说我们关注的其实是scope当中打点肉代表是这一行那么关注的其实是里面这个state这个属性state这个属性那好了这边构造好了之后我们再来看一下我们的页面你会发现状态现在就变了状态现在就变了那接着我想说呢对于这一个按钮来说
[03:40] 对于这一个按钮来说底下呢有很多的属性有很多的属性比如说呢我们还有一个属性叫做inactive value0还有active value1那这个0跟1代表什么意思这边简单的做一个说明好了这个作为说明这个是我们的开关组件那对于这个开关组件来说active value指的是
[04:20] 选中或者我们激活的数据值当你传递的这个数据值State如果等于你指定的咱们叫1那它就激活了那还有一个InactiveValue就是未激活也就是未选中那还有一个ActiveColor这个就是激活的颜色你会发现这颜色它不一样颜色那当然了还有一个就是InactiveValue
[04:58] Inactive Color这个就是未激活的颜色未来未激活好了那接着呢我们可以刷新一下页面打开F2好了我们一起来看现在呢其实就是一个绿色绿色其实代表的就是一个激活的一个状态那为什么是一个绿色激活的状态呢是因为我们在这边配置Moke.js的时候我们的数据是不是都是1是一个激活的状态
[05:34] OK那这样一来呢我们这个按钮其实也已经构造好了只不过现在还有点点小小的问题就是这个数据显示的时候这个按钮我们一般不让它点击不让它点击找到我们的恶劳门UI继续往里面去找一个案例这边就是金融状态金融状态加一个属性disable即可好了把这个disable加入到我们这个开关上面OK刷新一把你发现它已经不可点击了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Vue 项目中使用 Element UI 的 Switch 组件来控制表格中“状态”字段的显示，并通过代码修改实现动态切换。

2) 按时间顺序列出每张画面的要点：
画面1：在 Visual Studio Code 中编辑 `index.Vue` 文件，展示表格列定义和操作按钮的代码，其中包含 `el-table-column` 和 `el-button` 组件。
画面2：浏览器中显示 SaaS 企业列表页面，展示企业信息表格，包含序号、企业名称、当前版本、联系人、联系电话、所在地区、申请时间、操作列。
画面3：浏览器中继续展示企业列表，滚动显示更多企业记录，序号从 8 到 17。
画面4：浏览器中切换到“体验版”页面，显示“江苏传智播客教育科技股份有限公司”的企业列表，顶部有“体验版”标签。
画面5：浏览器中切换到“SaaS企业”页面，显示企业列表，其中第4行“常州新北区”企业被选中，状态为“正常”。
画面6：浏览器中打开 Element UI 官网的 Switch 组件页面，展示其用法和代码示例。
画面7：在 Visual Studio Code 中编辑 `index.Vue` 文件，添加 `el-switch` 组件，并设置 `v-model="scope.row.state"`。
画面8：在 Visual Studio Code 中编辑 `index.Vue` 文件，继续修改 `el-switch` 组件的属性，设置 `active-color="#f56c6c"` 和 `inactive-color="#fff999"`。
画面9：在 Visual Studio Code 中编辑 `index.Vue` 文件，修改 `el-switch` 组件的 `active-value` 和 `inactive-value` 属性。
画面10：在 Visual Studio Code 中编辑 `index.Vue` 文件，将 `el-switch` 组件的 `active-value` 设置为“1”，`inactive-value` 设置为“0”。
画面11：在 Visual Studio Code 中编辑 `index.Vue` 文件，修改 `el-switch` 组件的 `active-value` 为“是”，`inactive-value` 为“否”，并调整 `el-switch` 的位置。
画面12：浏览器中显示 SaaS 企业列表页面，其中第1行“企业0”和第2行“企业1”的状态开关为“开”。
画面13：在 Visual Studio Code 中编辑 `index.Vue` 文件，修改 `el-switch` 组件的 `active-value` 为“是”，`inactive-value` 为“否”，并调整 `el-switch` 的位置。
画面14：浏览器中显示 SaaS 企业列表页面，表格中显示“暂无数据”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```Vue
<el-table :data="dataList" border style="width: 100%">
  <el-table-column fixed prop="index" label="序号" width="50"></el-table-column>
  <el-table-column fixed prop="name" label="企业名称" width="200"></el-table-column>
  <el-table-column fixed prop="version" label="当前版本" width="150"></el-table-column>
  <el-table-column fixed prop="companyphone" label="联系电话" width="150"></el-table-column>
  <el-table-column fixed prop="expirationDate" label="截止时间" width="150"></el-table-column>
  <el-table-column fixed prop="state" label="状态" width="150"></el-table-column>
  <el-table-column fixed="right" label="操作" width="150">
    <template slot-scope="scope">
      <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
    </template>
  </el-table-column>
</el-table>
```

画面7：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面8：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面9：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="1"
    inactive-value="0"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面10：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="1"
    inactive-value="0"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面11：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="是"
    inactive-value="否"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

画面13：
```Vue
<template slot-scope="scope">
  <el-switch
    v-model="scope.row.state"
    active-value="是"
    inactive-value="否"
    active-color="#f56c6c"
    inactive-color="#fff999">
  </el-switch>
</template>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

