# 5-10-安装 ant-design-vue 组件库

上周总体架构设计时，我们已经选择了第三方组件库。对大型项目来说，第三方组件库必不可少，有了它可以大大节省开发时间。大型公司有时会选择自研组件库；中小型公司使用第三方组件库并做二次开发，是事半功倍的事情。这节课对有经验的同学来说是轻车熟路，简单过一下。

## 两大解决方案

对 Vue3 来说，组件库有两大方案。第一个是 Ant Design Vue：用 React 的同学肯定听说过 Ant Design，它是阿里出品的大型组件库，Ant Design Vue 是它的 Vue3 姐妹版本，也是本项目的选择。第二个是 Element Plus，录课前几天刚刚发布。用 Vue2 的同学都知道 Element 这个横行 Vue2 时代的组件库，但由于后期一直没人维护，很多人担心它是否还会支持 Vue3。经过一段等待，Element Plus 在原名基础上加了个 Plus 推出，让很多人惊喜。

这里不对比两者的异同，它们使用起来都很相似，差别就是组件丰富度、可定制化程度和整体样式，全看偏好。做课时只有 Ant Design Vue 可选，就先入为主地选了它，建议同学们也选一样的。如果实在想用 Element Plus 也可以，但后面的开发可能有坑，要自己扛。

## 安装方式

现代前端工程一般有两种安装方式。第一种是 NPM 安装，推荐方式，可以配合打包工具使用。特别注意，安装 Ant Design Vue 要加 @next 标记，因为它最新的 2.x 版本还是 RC 版本，需要这种方式获取最新版本：

```bash
npm i ant-design-vue@next --save
```

同时记得之前讲的 Git Flow：我已经创建了一个新的分支 feature-initial-structure，用来完成初步架构工作。

另一种方式是直接引入 js 和 css 文件，这是上古的浏览器引入方式：把整个库打包成 UMD 格式的 js 和单独的 css，通过 script 和 link 标签引入。强烈不推荐，官方文档也写明：使用已构建文件无法按需加载，而且难以获得底层依赖模块 bug 的快速修复。Element Plus 的文档也一样有 npm 安装和 CDN 两种方式，所以打包生成多种格式是共识，我们后面打包业务组件库时会讲这些格式是怎样生成的。

## 全局引用

安装完毕后做完整引用。引用提供两种方式：全部引用（一次性引入所有组件）和局部引用（用哪些引哪些），文档写得很清楚，这里暂时不做配置，用全部引用。在 main.ts 中引入组件库和样式文件：

```typescript
import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import App from './App.vue';

const app = createApp(App);
app.use(Antd);
```

## 回顾全局 API 的变化

引入时正好回顾一下讲 Vue3 和 Vue2 区别时说的全局 API 问题。Vue2 时代没有 app 的概念，应用只是通过 new Vue 创建的根实例，从同一个 Vue 构造函数创建的每个根实例都共享相同的全局配置，组件、指令都挂在 Vue 这个全局变量上，比如 Vue.component、Vue.directive。这有两个问题：一是测试期间全局配置容易意外污染其他测试用例，用户要仔细储存原始配置并在每次测试后恢复，有些 API 如 Vue.use、Vue.mixin 甚至连恢复的方法都没有，非常棘手；二是同一页面上多个 app 共享同一个 Vue 副本非常困难，一个 mixin 会同时影响 app1 和 app2。

Vue3 推出了 createApp，可以创建多个应用实例，任何全局改变 Vue 行为的 API 都移到了应用实例上，冲突情况不再存在。自从有了 TS，我很喜欢去翻库的定义文件，看它究竟有哪些属性和方法，建议大家也常这样做，有时都不用看文档。实例上把原来全局变量 Vue 的内容都拿过来了，文档里也有体现，Global API 和 Instance API 几乎一一对应。

最后在 App.vue 中引入一个 Ant Design Vue 的组件 a-button 验证：

```html
<a-button type="primary">Primary Button</a-button>
```

打开 localhost:8080，组件完美出现，说明第三方组件库安装成功。

课下建议大家好好浏览一下 Ant Design Vue 现有的所有组件，先做到心里有数。
