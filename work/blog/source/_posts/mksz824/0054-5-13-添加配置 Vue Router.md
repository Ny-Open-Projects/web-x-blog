---
disableNunjucks: true
title: 5-13 添加配置 Vue Router
date: 2026-11-17 12:54:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课一起使用 Vue Router 创建应用的路由系统。先安装：做课时 Vue Router 已经有完美支持 Vue3 的版本但还没正式发布，最新版本是 v4.0.1，npm 包名是 vue-router-next。安装命令：

```bash
npm install vue-router@next --save
```

安装完毕后查看 package.json，确认版本是 4.0 以上，就说明装了最新版。

## 分析页面结构

从页面上观察，不难发现页面有两种结构。一种是有通用块：首页、模板详情页、我的作品页，header 和 footer 都会出现。另一种不是通用结构：编辑器页面没有 footer，header 也完全不一样，上面有更多的按钮和功能；登录页面则更特别，完全不规则，没有 header 也没有 footer。

用图描述：第一种布局有 header 和 footer，中间一块内容区域随路由变化而变化，比如根目录加载 Home.vue，template/:id 加载 TemplateDetail 等等。第二种没有固定的头尾，对应路由直接加载 view 组件，头尾可能写在组件里，login 甚至没有任何头尾。这一点之后要特别注意，现阶段先不管，先添加路由。

## 调整页面结构

请大家先修改页面结构：原来每个 view 的内容（头尾）都写在组件里面，现在把头和尾直接挪到 App.vue 中，各 view 里把这些删除。启动后，App.vue 里头尾都在了，接下来要把不同路由的区域添加到中间。

## 创建路由

所有路由信息都放在 routes 文件夹中。在 routes 下新建 index.ts，先从新版 Vue Router 导出需要的函数，并把三个页面的 view 都导进来。用 createRouter 创建实例，参数 object 中第一个必填项是 history，它决定采用哪种路由类型：

```typescript
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Editor from '../views/Editor.vue';
import TemplateDetail from '../views/TemplateDetail.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/editor',
      name: 'editor',
      component: Editor,
    },
    {
      path: '/template/:id',
      name: 'template',
      component: TemplateDetail,
    },
  ],
});

export default router;
```

上节课讲过两种路由：HTML5 的 history API 用 pushState 实现路由变化；另一种是 URL hash，在 URL 后面添加哈希内容实现改变，是为了兼容不支持 HTML5 history 的旧实现，从哈希到哈希的转换同样不会引起刷新，但它有诸多缺点，唯一优点是支持旧版浏览器。这里采用 history 方式，从 vue-router 导入 createWebHistory。导入时可以看到还有 createMemoryHistory、createWebHashHistory 等多种模式可选。

注意这是新版 Vue Router 的 breaking change：Vue Router 3 时代这个参数叫 mode，接受的是一个字符串，现在完全不同了。

routes 接受一个数组，每一项定义 path（访问路径）、name（别名，TS 会自动提示）和 component。注意 template 那项要加 :id，它是动态路由，:id 代表这里可以传入任何参数，因为模板有不同的 id。

## 挂载路由

导出 router 实例后，在 main.ts 中使用：

```typescript
import router from './router';

createApp(App).use(router).mount('#app');
```

use 用于调用插件，和 use(Antd) 是一个意思，还可以链式调用。

Vue Router 被添加进应用后，内置两个组件帮我们完成任务。第一个是 router-view，相当于路由的占位符：在 layout content 里添加 router-view，内容就会动态渲染在那里。

验证路由规则：path 为 / 时渲染 Home 组件；跳到 editor 渲染 Editor；访问 template 并带上 id，TemplateDetail 就出现了。路由匹配不同的 path，对应组件的内容就渲染出来了。

## 小结

这节课给整个应用添加了 router 配置，现在可以完美展示几个页面了。下节课解决其他的问题。
