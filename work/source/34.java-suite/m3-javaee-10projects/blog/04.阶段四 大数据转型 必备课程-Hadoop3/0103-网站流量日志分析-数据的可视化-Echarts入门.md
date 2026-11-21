# 把统计结果画成图：ECharts 入门与最小可运行示例

Hive 里跑完统计、Sqoop 把结果导进 MySQL 的 `weblogview` 库之后，数据侧的活已经干完了。可业务方不会打开命令行查表，他们要看的是一张图：每天的页面平均访问量是多少，一周内访客怎么变化。数据可视化这一环节就是补上从「表里的数字」到「页面上的图」这一步，本课先把 ECharts 这个工具跑起来，画出一个不依赖任何后端的最小示例。

## 先给结论

- ECharts 是开源的 JavaScript 数据可视化库，画图的本质是组装一个 `option` 配置对象，调 `setOption` 之后图就渲染出来了。
- 固定三步：引入 `echarts.min.js`，准备一个带宽高的容器 `div`，用 `echarts.init(document.getElementById('main'))` 初始化实例再 `setOption`。
- `option` 的骨架只有六项：`title`、`tooltip`、`legend`、`xAxis`、`yAxis`、`series`；换柱状图还是折线图，只改 `series` 里的 `type`。
- 图例 `legend.data` 与系列 `series.name` 必须一一对应，对不上图例就空着。
- 静态数据跑通之后，把 `xAxis.data` 与 `series.data` 换成后端接口返回的数组，整个案例可视化就通了。

## 为什么是 ECharts：option 是一切的核心

ECharts 是一个把 JSON 配置画成图的前端库，官网对它的定位是开源 JavaScript 数据可视化库，折线图、柱状图、饼图、地图、热力图都在支持范围内。选它做报表有两个直接理由：图表种类全，配置就是纯 JSON，后端只要出数据就行。

官网的实例页是最快的学习入口：左侧一列图表模板，点开折线图，右边渲染出图，图旁边就是它的数据结构。把其中一个数字从 820 改成 900，图立刻跟着变。这说明一件事：图完全由数据结构驱动，下面这份就是折线图的最小配置（官网示例，按画面线抄录）：

```javascript
option = {
    title: {
        text: '折线图'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name: '销量',
        type: 'line',
        data: [820, 932, 901, 934, 1200, 1130, 1198]
    }]
};
```

`xAxis` 声明 `type: 'category'` 是类目轴，`data` 里是横轴上一个个刻度；`yAxis` 声明 `type: 'value'` 是数值轴，刻度由 ECharts 按数据范围自动生成；`series` 是数据系列，`type: 'line'` 画折线，改成 `'bar'` 同一份数据就变柱状图。一张图从配置到渲染的完整链路：

```mermaid
flowchart LR
    A["引入 echarts.min.js"] --> B["准备带宽高的容器 div"]
    B --> C["echarts.init 创建实例"]
    C --> D["组装 option 配置对象"]
    D --> E["setOption 渲染出图"]
```

关键路径只有一条：任何图表都收敛到 `option` 这一个对象上，`setOption` 是唯一的数据入口。理解了这点，后面所有图表类型都是换配置，不是换思路。

## 三步画出第一个柱状图

课程演示放在 Java Web 工程里：页面是 `webapp` 下的 `index.jsp`，引入库文件后部署到 Tomcat，访问首页就出图。练习时不必起 Tomcat，一个纯 HTML 文件双击就能跑。下面的最小示例为按本课写法补全，去掉了 JSP 头，页面结构、脚本与画面线上的代码一致：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <!-- 第一步：引入 echarts.min.js -->
    <script src="js/echarts.min.js"></script>
</head>
<body>
    <!-- 第二步：图表容器，必须给定宽高 -->
    <div id="main" style="width: 600px;height: 400px;"></div>
    <script type="text/javascript">
        // 基于准备好的 DOM，初始化 ECharts 实例
        var myChart = echarts.init(document.getElementById('main'));
        // 第三步：指定图表的配置项和数据
        var option = {
            title: {
                text: 'ECharts 入门示例'
            },
            tooltip: {},
            legend: {
                data: ['销量']
            },
            xAxis: {
                data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };
        myChart.setOption(option);
    </script>
</body>
</html>
```

对照三步走。**第一步，引入库文件。** 从官网下载 `echarts.min.js`，放进项目的 `js` 目录，用 `<script src="js/echarts.min.js"></script>` 引入，路径写错页面会直接报 `echarts is not defined`。

**第二步，准备容器。** 一个普通 `div`，`id` 取 `main`，行内样式定死宽度 600 像素、高度 400 像素。ECharts 在 `init` 时读取容器的实际尺寸来创建画布，容器没有宽高，画布就是 0，图自然不出现。

**第三步，初始化并传配置。** `echarts.init` 传进 DOM 元素拿到图表实例 `myChart`，再把组装好的 `option` 交给 `myChart.setOption(option)`。浏览器打开页面，六根柱子按 `[5, 20, 36, 10, 10, 20]` 的高度排开。鼠标悬浮在任意柱子上，tooltip 会弹出商品名与销量数字，这就是 `tooltip: {}` 默认开启的交互效果。

## option 六个关键配置项逐个拆

入门示例虽小，六个配置项一个不少，每个都值得单独说清楚：

```javascript
myChart.setOption({
    title: { text: '近一周访客数量变化趋势' },   // 主标题，副标题用 subtext
    tooltip: { trigger: 'axis' },               // 悬浮提示，axis 表示按轴线整列提示
    legend: { data: ['独立访客', '新独立访客'] }, // 图例，data 与 series 的 name 对齐
    xAxis: { data: ['20130913', '20130914', '20130915'] }, // 类目轴刻度
    yAxis: {},                                  // 数值轴，留空自动生成刻度
    series: [{ name: '独立访客', type: 'line', data: [120, 200, 150] }]
});
```

- `title.text` 是图的主标题，一段图上方的说明文字。
- `tooltip` 是交互入口，最简单的 `{}` 就有默认悬浮提示；`trigger: 'axis'` 会把同一横坐标下所有系列一起提示，做多系列折线图时常用。
- `legend.data` 里的每一项都必须能在 `series` 中找到同名 `name`，两边对齐图例才能点击切换系列显隐。
- `xAxis.data` 是横轴刻度数组，柱状图和折线图通常放日期或类目名。
- `yAxis` 留空对象即可，数值轴刻度自动计算；要人工封顶就补 `max`。
- `series` 是数组，一个元素一条数据系列；多系列折线图就是数组里多放几个元素。

把写死的数组换成动态数据，图就活了：`xAxis.data` 换成数据库里的日期列，`series.data` 换成统计值列。这正是下一课要做的，`weblogview` 库里那两张结果表（每天的页面平均访问量、一周内各页面的访问参数），最终都以这两条数组的形式喂给 `setOption`。

## 从静态示例到动态报表还差什么

静态 HTML 已经证明「给数据就出图」，动态报表要补的只有数据来源。ECharts 本身不知道 MySQL 的存在，它只认数组。所以链路天然分成两端：后端用三层架构把结果表查出来拼成 JSON（`dates` 一个数组、`data` 一个数组），前端用 ajax 拿到 JSON 后调 `setOption` 回填。中间隔着的，正是下一课「案例分析结果可视化」要完整搭出来的 Controller、Service、Mapper 三层加一段 `$.ajax`。

数据量大了以后还有两个提前值得记下的点：一是数据未返回前先用 `echarts.init` 画个空壳并调 `showLoading`，`success` 回调里 `setOption` 之后 `hideLoading`，避免页面先白一块；二是窗口尺寸变化时调 `myChart.resize()`，否则容器宽高变了图不会跟着缩放。

## 常见误区

- **容器不定宽高就 init。** ECharts 按 `init` 时刻的容器尺寸建画布，`div` 没有高度时画布为 0，页面只有一片空白还不报错；给容器显式 `width`、`height` 是铁律。
- **图例与系列名字对不上。** `legend.data` 写了「销量」，`series.name` 写成「销售额」，图例渲染出来是空的。图例靠 `name` 精确匹配系列，改名字要两处同改。
- **脚本写在容器前面直接执行。** `init` 找不到 DOM 就抛错；把 `<script>` 放在容器 `div` 之后，或包进 `window.onload`。
- **以为 JSP 才能用 ECharts。** ECharts 是纯前端库，静态 HTML、JSP、Vue 模板都能挂；它与后端技术毫无耦合，只要页面里有一个容器和一份数组。
- **改了数组不重新 `setOption`。** 数据驱动意味着改完数据必须再调一次 `setOption`，图表才会重绘；直接改 JavaScript 变量页面不会有任何变化。

## 面试可能被问到的问题

1. 面试官追问：「ECharts 底层是怎么把图画出来的？」
   答：它默认用 Canvas 绘制，也支持切换 SVG 渲染器。核心思想是数据驱动：`option` 描述「画什么」，渲染引擎根据配置把坐标轴、系列、图例逐层画到画布上。业务代码从不接触绘制 API，全部通过 `setOption` 与实例交互。
2. 面试官追问：「对同一个实例连续调用两次 setOption 会发生什么？」
   答：默认是合并模式，第二次的配置项与第一次按项合并，只更新变化的部分，适合局部刷新数据；传 `notMerge: true` 则全量替换旧配置。切换图表类型或整体改版式时用全量替换更安全。
3. 面试官追问：「init 为什么要求容器先有宽高，窗口变了怎么办？」
   答：初始化时按容器实际尺寸创建画布，尺寸为 0 就画不出来。窗口或容器尺寸变化后要手动调实例的 `resize()` 方法重新计算布局，常见做法是监听 `window` 的 resize 事件统一触发。
4. 面试官追问：「legend 和 series 是怎么联动的？」
   答：图例项与系列按 `name` 精确匹配。`legend.data` 里有而 `series` 中没有同名系列时图例不显示；反过来图例点击切换显隐，作用的就是对应 `name` 的那个系列。多系列图必须保证两边命名一致。
5. 面试官追问：「折线图数据点很多导致卡顿，你会怎么优化？」
   答：先在 `series` 上开 `sampling` 采样与 `large` 大数据模式，配合 `dataZoom` 只渲染可视区间；再考虑在后端或预处理阶段做降采样，按展示分辨率决定保留的点数。前端卡顿多数是点数过多，治本是减少参与绘制的点。

## 配套资料

- 代码：`materials/code/04/_散落资料/` 下的 `课程访问量-Hive-To-Mysql` NiFi 流程模板，统计结果进 MySQL 的真实工程对照，是本课与下一课图表数据的来源侧；源文件名带的推广后缀在正文一律略去。
- 讲义：`materials/docs/04/智慧学成Web业务后台搭建手册.md`，分析结果落地业务库后由 Web 后台出接口给前端展示的工程范式，与本课「表到图」的链路一致。
- 说明：官网折线 `option` 与入门柱状 `option` 按画面线抄录整理；最小可运行 HTML 为按本课写法补全（课程演示为 `index.jsp` 部署 Tomcat，本示例去掉 JSP 头改为纯 HTML，脚本内容一致）；`echarts.min.js` 需从官网下载后放入 `js` 目录。
