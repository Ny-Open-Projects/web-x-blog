# 画面线理解：21-企业详情：完成企业详情展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\21-企业详情：完成企业详情展示_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:45, 01:15, 01:37, 02:12, 02:41, 03:09, 03:54, 04:31, 04:52, 05:28, 06:02, 07:01, 07:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:20:37

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 项目中使用 Element UI 组件库构建一个 SaaS 企业信息管理页面，包括表单结构、数据绑定、标签页切换和 API 接口调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 SaaS 企业信息管理页面的前端界面，包含公司地址、状态、法人代表等输入字段，以及“审核”和“取消”按钮。
画面 2: 展示了 Element UI 官网的“表单内组件尺寸控制”文档页面，说明如何通过设置 Form 的 size 属性来控制表单内组件的尺寸。
画面 3: 展示了 Element UI 官网的“表单”组件示例代码，包含 <el-form>、<el-form-item>、<el-input>、<el-button> 等标签的结构和 script 部分的 data 对象。
画面 4: 展示了 Visual Studio Code 编辑器中的 detail.vue 文件，代码中包含 <el-tabs>、<el-form>、<el-form-item> 等 Element UI 组件，用于构建表单和标签页。
画面 5: 展示了 detail.vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 6: 展示了浏览器开发者工具 Console 中的错误信息，提示“Invalid handler for event 'click' got undefined”，并显示了错误堆栈。
画面 7: 展示了 SaaS 企业信息管理页面，企业名称已填写为“江苏传智播客教育科技股份有限公司”，页面显示“SAAS企业”标签。
画面 8: 展示了 detail.vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 9: 展示了 API 文档页面，显示了 Company 资源的 POST、GET、PUT 等 API 接口。
画面 10: 展示了 detail.vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 11: 展示了 Element UI 官网的“表单”组件示例代码，与画面 3 相同。
画面 12: 展示了 detail.vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。
画面 13: 展示了 SaaS 企业信息管理页面，企业名称已填写为“江苏传智播客教育科技股份有限公司”，页面显示“SAAS企业”标签。
画面 14: 展示了 detail.vue 文件中 <el-form> 标签的代码，其中包含 v-model 绑定和点击事件 @click="onSubmit"。

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
