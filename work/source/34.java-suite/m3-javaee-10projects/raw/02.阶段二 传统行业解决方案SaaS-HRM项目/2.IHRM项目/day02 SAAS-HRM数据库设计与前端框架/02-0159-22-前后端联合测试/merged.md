# 22-前后端联合测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\22-前后端联合测试_【海量资源尽在 ubkz.com】.mp4
- 时长 5分54秒（音频 355s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那其实到目前为止呢我们整个的这个前端的这两个页面呢咱们都已经构造出来了那都构造出来了之后呢接下来就是说前端构造好了那后端我代码其实也开发完成了那咱们接下来就要完成最后一件事情就是把这些代码前端和后端给它联系到一起看一下能不能使用那在这边呢我先打开我的idea好了先打开我的idea它消费有点点慢好了打开我们的工程
[00:42] 那打开工程之后呢我把我们昨天写好的那个企业微服务让它运行起来好了企业微服务找到它的闷方法启动类找到闷方法来执行好了这边让它去慢慢启动那接下来呢我需要跟各位来说一下如果想要做到前后端的连条我应该怎么办这边呢有一个简单的配置过程闸胎SRC那这回呢不管你不管你
[01:21] 怎么去做咱们应该想方设法的就告头我现在不能走我这边的测试数据了不能走MOOC了那不能走MOOC怎么办找到index.js把底下这两个我们访问企业的全部给他注释掉那全部给他注释掉那这个时候呢他开始发送请求那发送请求我们一起来试一下他能不能用啊各位打开F12刷新你发现这边
[01:51] 报了一个错误叫做404的这么一个错误大家会发现你当前所有发送请求都发送到了当前这个工程下的APM目录下的一个company-10ID等于10包括企业这边它都是报404错误那这个就是我想跟各位要来聊的最后我们如何前端和后端整到一起让它联合测试好了其实在我们的
[02:20] 前端工程当中我们这个时候要想去进行测试的话我们要做一个简单的配置找到config找到index在这里面要做一个简单的配置因为我们v服务会比较多那我们要统一测试的时候其实就不太方便那在EleMUI和VUE这套工程当中它可以对不同的接口单独去进行配置那我们要配置的点是什么注意来看
[02:47] 默认他已经把所有的请求都发送到当前他自己这个工程当中localhostAPIcompany上面也是APIcompany等等等等他默认的就发送到自己这个地址当中了那其实他内部会借助他请求转发的这么一个机制帮你去转发到你的微服务上那接下来呢有这么两个点需要各位要知道第一个API是怎么回事怎么就多了一个API
[03:16] 那第二个点就是说如何把这个地址转发到我们这边的微服务上面那第一个点我们来看一下API从哪构造的那这个API其实是我们DEV这边有一个base APIbase API那这个时候如果就想说了你就不想让它发送到自己这边那你这边可以写一个完整的请求地址写一个完整的请求地址比如说我这边要请求到
[03:48] 比如说我这边要请求到localhost 9001这个是我的请求地址就要请求到当前这个工程上那接下来我们一起来看一下刷新我这边没有修改吗哦抱歉如果修改了这个配置的话我们需要重启一下服务啊重启一下服务Ctrl Cok 我看一下服务重启了吗啊没有这个就比较尴尬了这个
[04:38] 我这个又出问题了抱歉我把这个工程关掉再打开吧这回应该就停掉了好了已经停掉了npm run dv好了我这个工程呢已经启动成功了我们一起刷新一下页面来看一下效果哎各位来看效果其实已经展示出来了已经展示出来了这边有哎这这几个值都是我数据库里面的内容并且呢
[05:19] 我随便点击一个查看一下这些基本的内容其实也都已经给我展示到我们的界面上了OK好了那这样一来呢我们的前后端其实就已经全部都联系起来了那全部都联系起来呢并且呢这些数据是真正的发送请求发送到后端从后端把数据给我获取到的那这样一来我们的前后端就已经联系到一起了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 SaaS 企业管理系统前端页面的开发与调试过程，涉及在 Visual Studio Code 和 IntelliJ IDEA 中操作代码、查看页面效果及处理接口错误。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Visual Studio Code 中，用户右键点击文件“detail.Vue”，弹出菜单，选择“在浏览器中打开”选项，准备预览页面。
画面 2: 切换到 IntelliJ IDEA，显示“Welcome to IntelliJ IDEA”界面，选中项目“ihm_parent”准备打开。
画面 3: IntelliJ IDEA 加载项目，界面显示“Pre-generating IntelliJ bootstrap caches”状态，等待初始化完成。
画面 4: 浏览器打开 SaaS 企业管理系统页面，显示“江苏传智播客教育科技股份有限公司”的企业详情表单，包含公司地址、状态、法人代表等字段。
画面 5: 浏览器中显示“SAAS企业”页面，但页面内容为空，控制台报错“Request failed with status code 404”，提示接口未找到。
画面 6: Visual Studio Code 中打开“indexs.config”文件，显示多个并排的窗口，包括项目代码、数据库、设计工具等，用于多任务开发。
画面 7: 浏览器中“SAAS企业”页面仍为空，控制台持续报错“Request failed with status code 404”，同时显示“indexs - project-saas-hrm...”的终端窗口。
画面 8: 浏览器中“SAAS企业”页面仍为空，控制台报错信息与画面 7 相同。
画面 9: 浏览器中“SAAS企业”页面显示“SAAS企业”标签，但内容区域为空。
画面 10: 浏览器中“SAAS企业”页面内容区域为空，控制台报错信息与之前相同。
画面 11: Visual Studio Code 窗口空白，可能为初始化或切换后状态。
画面 12: 浏览器中“SAAS企业”页面显示数据列表，包含序号、企业名称、版本、联系电话、状态等字段，数据为“传智播客”和“zhangsan”。
画面 13: 浏览器中“SAAS企业”页面切换到“企业信息”标签页，显示“企业名称”和“公司地址”输入框。
画面 14: 浏览器中“SAAS企业”页面显示数据列表，新增一条记录“江苏传智播客教育科技股份有限公司”，状态为关闭。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```Vue
<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="基本信息" name="first">
        <el-form ref="form" :model="formData" :rules="formRules" label-width="120px">
          <el-form-item label="公司地址" prop="address">
            <el-input v-model="formData.address" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="审核状态" prop="status">
            <el-input v-model="formData.status" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="营业执照" prop="license">
            <el-input v-model="formData.license" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="法人代表" prop="legalPerson">
            <el-input v-model="formData.legalPerson" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="公司电话" prop="phone">
            <el-input v-model="formData.phone" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="formData.email" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="公司规模" prop="scale">
            <el-input v-model="formData.scale" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="所属行业" prop="industry">
            <el-input v-model="formData.industry" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item label="备注" prop="remark">
            <el-input v-model="formData.remark" style="width:250px" disabled></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm">提交</el-button>
            <el-button @click="resetForm">取消</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="客户信息" name="second">
        <!-- 客户信息内容 -->
      </el-tab-pane>
      <el-tab-pane label="交易记录" name="third">
        <!-- 交易记录内容 -->
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { detail } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-detail',
  data() {
    return {
      formData: {
        address: '',
        status: '',
        license: '',
        legalPerson: '',
        phone: '',
        email: '',
        scale: '',
        industry: '',
        remark: ''
      },
      formRules: {
        address: [{ required: true, message: '请输入公司地址', trigger: 'blur' }],
        status: [{ required: true, message: '请输入审核状态', trigger: 'blur' }],
        license: [{ required: true, message: '请输入营业执照', trigger: 'blur' }],
        legalPerson: [{ required: true, message: '请输入法人代表', trigger: 'blur' }],
        phone: [{ required: true, message: '请输入公司电话', trigger: 'blur' }],
        email: [{ required: true, message: '请输入邮箱', trigger: 'blur' }],
        scale: [{ required: true, message: '请输入公司规模', trigger: 'blur' }],
        industry: [{ required: true, message: '请输入所属行业', trigger: 'blur' }],
        remark: [{ required: true, message: '请输入备注', trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.$message.success('提交成功')
        } else {
          this.$message.error('请填写完整信息')
        }
      })
    },
    resetForm() {
      this.$refs.form.resetFields()
    }
  }
}
</script>
```

画面 6:
```javascript
// indexs.config
'use strict';
// Template version: 1.1.1
```

画面 13:
```javascript
// detail.Vue
export default {
  name: 'saas-clients-detail',
  data() {
    return {
      formData: {
        address: '',
        status: '',
        license: '',
        legalPerson: '',
        phone: '',
        email: '',
        scale: '',
        industry: '',
        remark: ''
      }
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

