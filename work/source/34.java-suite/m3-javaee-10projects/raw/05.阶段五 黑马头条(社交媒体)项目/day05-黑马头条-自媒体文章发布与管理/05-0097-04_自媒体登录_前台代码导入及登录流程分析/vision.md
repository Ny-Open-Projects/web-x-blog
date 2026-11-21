# 画面线理解：04_自媒体登录_前台代码导入及登录流程分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\04_自媒体登录_前台代码导入及登录流程分析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 02:58, 03:37, 04:28, 04:56, 06:07, 07:20, 09:20, 10:10, 11:16, 11:46, 12:31, 13:30, 14:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:41:39

1) 这一组画面整体在讲一个前后端分离的用户登录系统，从前端Vue组件的表单验证、API接口定义，到后端Java的Controller和Service层实现，最后展示登录成功后的前端页面。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目文件夹，包含一个名为“heima-leadnews-wemedia.zip”的压缩包，位于“资料”目录下，暗示这是项目源码包。
画面2：在WebStorm中打开Vue项目，展示`login/index.vue`文件，其中包含表单验证逻辑，如`validateName`和`validatePass`。
画面3：继续展示`login/index.vue`，聚焦于表单元素，如`<el-input type="password"`和`<el-button type="primary"`，以及导入的组件和脚本。
画面4：展示`login/index.vue`的脚本部分，定义了`validateName`和`validatePass`函数，用于表单验证。
画面5：展示`login/index.vue`的脚本部分，高亮显示了`validateName`和`validatePass`函数的逻辑。
画面6：在WebStorm中打开`/api`目录，展示`constants.js`文件，其中定义了多个API常量，如`API_LOGIN`、`API_USERAUTH`等。
画面7：在WebStorm中打开`login.js`文件，展示`loginByUserName`函数，该函数调用`API_USERAUTH`进行登录请求。
画面8：继续展示`login.js`文件，高亮显示了`if (result.code !== 0)`条件判断，用于处理登录响应。
画面9：在IntelliJ IDEA中打开`LoginController.java`，展示`@RequestMapping("/in")`注解和`login`方法，用于处理登录请求。
画面10：在WebStorm中打开`router.js`文件，展示路由配置，其中`path: '/login'`指向`login/index.vue`。
画面11：在Navicat for MySQL中打开`user`表，展示用户数据，如`name: 'zhangsan'`，`password: '123456'`。
画面12：展示前端登录成功后的页面，显示“黑马头条”网站，包含文章列表和数据统计图表。
画面13：在IntelliJ IDEA中打开`UserLoginServiceImpl.java`，展示`login`方法的实现，包括数据库查询和密码比对逻辑。
画面14：再次展示前端登录成功后的页面，与画面12相同，确认登录流程完成。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```javascript
if (value === '') {
  callback(new Error('请输入密码'));
} else {
  callback();
}
return {
  checked: true,
  ruleForm: {
    name: '',
    password: '',
  },
  rules: {
    name: {
      validator: validateName, trigger: 'blur'
    },
    password: {
      validator: validatePass, trigger: 'blur'
    }
  },
  components: {
  },
  computed: {
  },
  methods: {
    async submitForm() {
    }
  }
}
```

画面3：
```html
<template>
  <div class="login">
    <div class="user-avatar">
      <img src="/assets/logo_index.png" class="status-icon" ref="ruleForm" class="login-ruleForm">
      <el-form-item prop="name">
        <el-input type="text" v-model="ruleForm.name" autocomplete="off" placeholder="请输入账户名"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="请输入密码"></el-input>
      </el-form-item>
      <div id="myCode"></div>
      <el-checkbox v-model="checked" @change="change">已阅读并同意《用户协议》和《隐私条款》</el-checkbox>
      <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
    </div>
  </div>
</template>

<script>
import { } from '@/components/gt'; // 人机交互验证码
import { loginByUsername, getMobileCode, getCaptcha } from '@/api/login'
export default {
  data() {
    var validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        callback();
      }
    }
  }
}
</script>
```

画面4：
```javascript
<script>
import { } from '@/components/gt'; // 人机交互验证码
import { loginByUsername, getMobileCode, getCaptcha } from '@/api/login'
export default {
  data() {
    var validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        callback();
      }
    }
  }
}
</script>
```

画面5：
```javascript
<script>
import { } from '@/components/gt'; // 人机交互验证码
import { loginByUsername, getMobileCode, getCaptcha } from '@/api/login'
export default {
  data() {
    var validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        callback();
      }
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        callback();
      }
    }
  }
}
</script>
```

画面6：
```javascript
export const API_LOGIN = '/login'; // 登录
export const API_USERAUTH = '/user/auth'; // 用户认证
export const API_CAPTCHAS = '/captcha'; // 验证码
export const API_IMAGES_UPLOAD = '/api/v1/media/material/upload_picture'; // 上传图片
export const API_CHANNEL_LIST = '/api/v1/channel/channels'; // 获取频道列表
export const API_ARTICLES_LIST = '/api/v1/media/news/list'; // 获取文章列表
export const API_ARTICLES_SUBMIT = '/api/v1/media/news/submit'; // 提交文章
export const API_ARTICLES_DELETE = '/api/v1/media/news/del_news'; // 删除文章
export const API_ARTICLES_UPDATE = '/api/v1/media/news/update'; // 更新文章
export const API_COMMENTS_LIST = '/api/v1/media/comment/list'; // 获取评论列表
export const API_COMMENTS_DELETE = '/api/v1/media/comment/delete'; // 删除评论
export const API_COMMENTS_SUBMIT = '/api/v1/media/comment/submit'; // 提交评论
export const API_COMMENTS_UPDATE = '/api/v1/media/comment/update'; // 更新评论
export const API_COMMENTS_STATUS = '/api/v1/media/comment/status'; // 修改评论状态
export const API_COMMENTS_LIKES = '/api/v1/media/comment/likes'; // 获取评论点赞
export const API_COMMENTS_LIKES_CANCEL = '/api/v1/media/comment/likes/cancel'; // 取消评论点赞
export const API_COMMENTS_LIKES_COLLECT = '/api/v1/media/comment/collect'; // 收藏评论
export const API_COMMENTS_LIKES_UNCOLLECT = '/api/v1/media/comment/uncollect'; // 取消收藏评论
export const API_COMMENTS_LIKES_REPORT = '/api/v1/media/comment/report'; // 举报评论
export const API_COMMENTS_LIKES_REPORT_CANCEL = '/api/v1/media/comment/report/cancel'; // 取消举报评论
export const API_COMMENTS_LIKES_REPORT_LIST = '/api/v1/media/comment/report/list'; // 获取举报评论列表
export const API_COMMENTS_LIKES_REPORT_DETAIL = '/api/v1/media/comment/report/detail'; // 获取举报评论详情
export const API_COMMENTS_LIKES_REPORT_HANDLE = '/api/v1/media/comment/report/handle'; // 处理举报评论
export const API_COMMENTS_LIKES_REPORT_HANDLE_LIST = '/api/v1/media/comment/report/handle/list'; // 获取处理举报评论列表
export const API_COMMENTS_LIKES_REPORT_HANDLE_DETAIL = '/api/v1/media/comment/report/handle/detail'; // 获取处理举报评论详情
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS = '/api/v1/media/comment/report/handle/status'; // 获取处理举报评论状态
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_LIST = '/api/v1/media/comment/report/handle/status/list'; // 获取处理举报评论状态列表
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_DETAIL = '/api/v1/media/comment/report/handle/status/detail'; // 获取处理举报评论状态详情
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_UPDATE = '/api/v1/media/comment/report/handle/status/update'; // 更新处理举报评论状态
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_UPDATE_LIST = '/api/v1/media/comment/report/handle/status/update/list'; // 获取更新处理举报评论状态列表
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_UPDATE_DETAIL = '/api/v1/media/comment/report/handle/status/update/detail'; // 获取更新处理举报评论状态详情
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_UPDATE_STATUS = '/api/v1/media/comment/report/handle/status/update/status'; // 更新处理举报评论状态
export const API_COMMENTS_LIKES_REPORT_HANDLE_STATUS_UPDATE_STATUS_LIST =
