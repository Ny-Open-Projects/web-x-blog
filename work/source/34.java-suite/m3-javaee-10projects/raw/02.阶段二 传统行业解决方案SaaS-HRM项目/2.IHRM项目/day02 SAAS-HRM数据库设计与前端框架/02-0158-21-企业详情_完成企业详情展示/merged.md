# 21-企业详情：完成企业详情展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\21-企业详情：完成企业详情展示_【海量资源尽在 ubkz.com】.mp4
- 时长 8分1秒（音频 481s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那到目前为止呢我们已经获取到了它的这个数据那数据获取到了之后我们先来就构造出它这一个一个的框框那对于它这一个框框构造的过程当中呢很简单只要设一道页面组件我们使用的就是Elemen UI它提供的内容那么可以来找一下Elemen UI它提供的内容里面其中有一个叫做form好了我们来找一下有一个叫做form表单
[00:29] 那放表单其实就是这样的一个类型有很多有很多那其实呢根据我们的页面原型你会发现其实用一个最基础的最基本的一个一个的往下构造其实就可以了那我们在这边呢其实随意找几个就行随意找几个我们用一个最基础的吧嗯从上面拖一个搞一个表单出来我就用最低的好了那接下来在这边来一表单把里面的所有内容Ctrl C
[01:07] call到我的detail页面里面好了注意我现在要call到哪呢我们要call到注意我们要call到我们页面部分当中的这句话这个位置那是企业信息把这企业信息现在就可以删掉了好了call过来OKcall过来之后呢做一个简单的格式上的一个修改那这个里面的内容实在是有点多实在是有点多我就以一个为例
[01:39] 我们来看一下如何去用当然了我留了俩底下这个是绑定了一些按钮上面呢是我们的一行那好了我们来看一下如何去做好了这边呢需要跟各位简单的来介绍一下这个是我们的form表单那form表单其中有一个modelmodel指的是我们数据双向绑定的数据对象那对于我们来说绑定的其实就是这个form date拿过来
[02:19] 那比如说呢我们这个不叫活动名称label指的是你这个标签叫什么名字啊我们这边不叫活动名称了我们叫做企业名称那企业名称我关注的其实就是form这个表单这个数据它里面的name属性OK那这样一来我第一行就构造好我们来看一下就叫做测试企业
[02:47] 其实第一行呢已经出来了只不过呢现在我们的页面呢还有一些问题啊比如说这里面呢它会有一个unsummit这个方法我先删掉不影响我使用再去刷新OK这个就没啥问题了好了那接下来呢其实我们现在写的跟人家这一套啊还是不太一样是因为我们这边没有加一些样式如果加上样式的话其实也比较好看了就好了那除了企业名称之外在这边呢我们
[03:22] 除了企业名称之后呢我们可能还有一些比如说呢地区公司地址和审核状态等等等等这一堆那这些内容其实都是一个大同小异的这么一个过程直接呢从上面靠一份过来就可以当然了我们可以简单的来设置一下设置不了我不设置了那除了企业名称之后呢可能还有公司地区公司地址那除了公司地址之外呢还有比如说呢这边叫做
[04:04] 我随便写两个吧公司电话那还有我们的比如说呢邮箱我就写这么多了剩下的我就不再一个一个写了其实都大同小异那这里面呢我们VModel其实绑定的就是我们数据模型里面的一些元素这些元素我们可以参照一下我们的API接口根据ID查询API接口里面返回的比如说呢公司地址company address属性名公司电话company phone
[04:43] 公司邮箱mailboxOK好了那接下来呢还有比如说呢这边还有一项叫做备注叫做备注备注呢叫做remark好了那接下来我们来看一下我们构造好的这个页面OK那基本的这些内容其实都已经有了那只不过呢人家这边呢其实对于这些内容来说像这些内容全都不能够选择都不能写只有一个能修改
[05:19] 所以对于我们来说呢剩下的这个内容呢需要做一个简单的处理也就是说把这个每一个框框给它搞定搞成不可选择好了那接下来呢我们一起往下来看一起往下来看这个里面有自己的一个属性叫做disable是否这里面的内容能够改动好了我们的名称不能改disable就叫disable就可以了地址电话邮箱
[06:03] 好了我们这边再来刷新一下那各位来看就这样一来说呢我们这个效果其实就好看很多了当然就是我们这个样式啊现在还是有点难看啊我们简单的做一个调整做一个调整那在企业名称这边呢对这个放表单的做一个样式的一个调整首先我们可以给他指定一下就是你这个label的一个宽度比如说给他指定成200OK那好了这样一来你会发现这边挪了一点点
[06:34] 那剩下就是说每一个input呢咱们可以给它指定一个style比如说呢这边呢可以指定width指定下它的宽度比如说呢就是255px好了每一个给它指定这么宽这个实在是太难看了所以决定改一下好了那这样一来其实看起来就好看多了
[07:05] 就好看多了当然了我这边是因为时间有限我只写了这么几个其实都是一些重复的一些劳动那这样一来呢我们就已经把企业详情相关的内容就已经给它构造出来了当然了底下两个菜单我们在这边呢其实是有一个叫做审核和拒绝的一个过程比如说审核比如说呢这边有一个叫做拒绝那不管是审核或者是拒绝其实都要
[07:36] 发送到我们的后端其实说白了就是更新一下我们企业的详情的信息就是更新一下的状态如果审核了就可用拒绝了就不可用没错吧当然了我们更新的时候其实除了这个备注还有这两个状态要做一个统一的修改其实就可以了OK当然了这两个我们可以留给各位当成作业自己去完成就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 项目中使用 Element UI 组件库构建一个 SaaS 企业信息管理页面，包括表单结构、数据绑定、标签页切换和 API 接口调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 SaaS 企业信息管理页面的前端界面，包含公司地址、状态、法人代表等输入字段，以及“审核”和“取消”按钮。
画面 2: 展示了 Element UI 官网的“表单内组件尺寸控制”文档页面，说明如何通过设置 Form 的 size 属性来控制表单内组件的尺寸。
画面 3: 展示了 Element UI 官网的“表单”组件示例代码，包含 <el-form>、<el-form-item>、<el-input>、<el-button> 等标签的结构和 script 部分的 data 对象。
画面 4: 展示了 Visual Studio Code 编辑器中的 detail.Vue 文件，代码中包含 <el-tabs>、<el-form>、<el-form-item> 等 Element UI 组件，用于构建表单和标签页。
画面 5: 展示了 detail.Vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 6: 展示了浏览器开发者工具 Console 中的错误信息，提示“Invalid handler for event 'click' got undefined”，并显示了错误堆栈。
画面 7: 展示了 SaaS 企业信息管理页面，企业名称已填写为“江苏传智播客教育科技股份有限公司”，页面显示“SAAS企业”标签。
画面 8: 展示了 detail.Vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 9: 展示了 API 文档页面，显示了 Company 资源的 POST、GET、PUT 等 API 接口。
画面 10: 展示了 detail.Vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 11: 展示了 Element UI 官网的“表单”组件示例代码，与画面 3 相同。
画面 12: 展示了 detail.Vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 13: 展示了 SaaS 企业信息管理页面，企业名称已填写为“江苏传智播客教育科技股份有限公司”，页面显示“SAAS企业”标签。
画面 14: 展示了 detail.Vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```html
<el-radio-group>
  <el-form-item label="活动名称">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-radio-group>
```
```javascript
export default {
  data() {
    return {
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: '',
        resource: '',
        desc: ''
      }
    }
  }
}
```

画面 4:
```html
<div class="dashboard-container">
  <div class="app-container">
    <el-card shadow="never">
      <el-tabs v-model="activeName" name="first">
        <el-tab-pane label="企业信息" name="first">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="活动名称">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="活动区域">
              <el-select v-model="form.region" placeholder="请选择活动区域">
                <el-option label="上海" value="shanghai"></el-option>
                <el-option label="北京" value="beijing"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="活动时间">
              <el-date-picker type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="活动性质">
              <el-radio-group v-model="form.type">
                <el-radio label="线上活动">线上活动</el-radio>
                <el-radio label="线下活动">线下活动</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="特殊资源">
              <el-checkbox-group v-model="form.resource">
                <el-checkbox label="线上视频"></el-checkbox>
                <el-checkbox label="线下讲座"></el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm">立即创建</el-button>
              <el-button>取消</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="客户信息" name="second">客户信息</el-tab-pane>
        <el-tab-pane label="交易记录" name="third">交易记录</el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</div>
```

画面 5:
```html
<el-tab-pane label="企业信息" name="first">
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="活动名称">
      <el-input v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="活动区域">
      <el-select v-model="form.region" placeholder="请选择活动区域">
        <el-option label="上海" value="shanghai"></el-option>
        <el-option label="北京" value="beijing"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-date-picker type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"></el-date-picker>
    </el-form-item>
    <el-form-item label="活动性质">
      <el-radio-group v-model="form.type">
        <el-radio label="线上活动">线上活动</el-radio>
        <el-radio label="线下活动">线下活动</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="特殊资源">
      <el-checkbox-group v-model="form.resource">
        <el-checkbox label="线上视频"></el-checkbox>
        <el-checkbox label="线下讲座"></el-checkbox>
      </el-checkbox-group>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">立即创建</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</el-tab-pane>
```

画面 8:
```html
<el-tab-pane label="企业信息" name="first">
  <el-form ref="form" :model="formData" label-width="80px">
    <el-form-item label="企业名称">
      <el-input v-model="formData.name"></el-input>
    </el-form-item>
    <el-form-item label="公司地址">
      <el-input v-model="formData.companyAddress"></el-input>
    </el-form-item>
    <el-form-item label="公司电话">
      <el-input v-model="formData.companyPhone"></el-input>
    </el-form-item>
    <el-form-item label="邮箱">
      <el-input v-model="formData.mailBox"></el-input>
    </el-form-item>
    <el-form-item label="备注">
      <el-input v-model="formData.remark"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">立即提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</el-tab-pane>
```

画面 10:
```html
<el-tab-pane label="企业信息" name="first">
  <el-form ref="form" :model="formData" label-width="80px">
    <el-form-item label="企业名称">
      <el-input v-model="formData.name"></el-input>
    </el-form-item>
    <el-form-item label="公司地址">
      <el-input v-model="formData.companyAddress"></el-input>
    </el-form-item>
    <el-form-item label="公司电话">
      <el-input v-model="formData.companyPhone"></el-input>
    </el-form-item>
    <el-form-item

