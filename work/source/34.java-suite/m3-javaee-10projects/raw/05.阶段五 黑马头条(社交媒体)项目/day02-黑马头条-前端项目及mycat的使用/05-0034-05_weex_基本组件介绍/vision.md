# 画面线理解：05_weex_基本组件介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\05_weex_基本组件介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:53, 02:27, 02:40, 04:02, 04:40, 05:58, 06:21, 07:09, 08:01, 08:21, 09:31, 10:26, 11:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:48:57

1) 这一组画面整体在讲 Weex 框架中内置组件（如 text、image、list）的使用方法和相关文档查阅。

2) 按时间顺序列出每张画面的要点：
画面 1: 查看 Weex 官方文档，介绍 Weex 页面上下文中的 JS 实例和其属性类型。
画面 2: 在 Weex Playground 中编写一个包含按钮和文本的简单页面，预览效果为“去士会场”。
画面 3: 在 WebStorm 中查看项目结构，终端显示构建过程，正在编译模块。
画面 4: 继续在 WebStorm 中查看构建日志，模块编译进度更新。
画面 5: 在 Weex Playground 中预览一个包含广告和视频的复杂页面。
画面 6: 在 WebStorm 中编辑代码，为按钮添加 href 属性，终端显示应用已运行。
画面 7: 在 WebStorm 中修改代码，将 href 属性值改为 "http://www.itcast.cn"。
画面 8: 在 WebStorm 中继续编辑代码，为 text 标签添加“传智播客”文本。
画面 9: 查看 Weex 官方文档中关于 <text> 组件的说明，包括警告和样式支持。
画面 10: 在 WebStorm 中编辑代码，为 image 标签添加样式和 src 属性。
画面 11: 在 WebStorm 中继续编辑代码，为 image 标签添加样式和 src 属性。
画面 12: 查看 Weex 官方文档中关于 <image> 组件的说明，包括基本用法和注意事项。
画面 13: 在 Weex Playground 中预览一个包含“传智播客”和 logo 的页面。
画面 14: 查看 Weex 官方文档中关于 <list> 组件的说明，包括基本用法和示例。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```typescript
declare type Weex = {
  config: WeexConfigAPI;
  document: WeexDocument;
  requireModule: (name: string) => Object | void;
  supports: (condition: string) => boolean | void;
}
```

画面 2:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://g.tbcdn.cn/amte-resource/0.0.8/fast/show_1.js">
      <text class="text">去士会场</text>
    </a>
  </div>
</template>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}

button {
  width: 350px;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 4px;
}

.text {
  font-size: 40px;
  color: #fff;
  text-align: center;
}
</style>
```

画面 3:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://g.tbcdn.cn/amte-resource/0.0.8/fast/show_1.js">
      <text class="text">去士会场</text>
    </a>
  </div>
</template>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}

button {
  width: 350px;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 4px;
}

.text {
  font-size: 40px;
  color: #fff;
  text-align: center;
}
</style>
```

画面 6:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://www.itcast.cn">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 7:
```html
<template>
  <div class="wrapper">
    <a class="button" :href="image_url">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
    image_url: "http://www.itcast.cn"
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 10:
```html
<template>
  <div class="wrapper">
    <a class="button" :href="image_url">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
    image_url: "http://www.itcast.cn"
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 12:
```html
<image style="width:500px;height:500px" src="https://vuejs.org/images/logo.png"/>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 9: 文档标题为“<text>”，内容包括“简介”、“样式”、“属性”等部分。
画面 12: 文档标题为“<image>”，内容包括“基本用法”、“子组件”、“样式”等部分。
画面 14: 文档标题为“<list>”，内容包括“简介”、“子组件”、“属性”、“扩展”、“示例”等部分。

5) 无。
