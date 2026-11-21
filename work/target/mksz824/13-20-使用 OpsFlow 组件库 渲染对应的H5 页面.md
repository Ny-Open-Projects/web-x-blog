# 13-20-使用 OpsFlow 组件库 渲染对应的H5 页面

这节课完成 SSR 页面的初步渲染，需要用数据库中的数据，也就是拿到 work 对应的 components，渲染到对应的页面上。我创建了一个模板文件叫 page.nj，里面需要几部分数据，都来自作品信息：第一个是 title（work 的 title），第二个是 desc（description），第三个是 html，它应该是通过 Vue server-renderer 返回的一串字符串。目的就是拿到这三方面内容然后渲染。

## Service：renderToPageData

为了更好地分层，把使用 Vue 渲染的逻辑写到了 service 中。方法叫 renderToPageData，输入参数是 query（要查 id 和 uuid），返回我们需要的一系列数据。

第一步查询对应的 work：`const work = await this.ctx.model.work.findOne(query).lean()`，使用传进来的参数，并且希望它返回一个普通的 object，所以加 lean。拿到数据后先判断存在与否，不存在说明输入的 id 和 uuid 有误，直接 `throw new Error('work not exist')`。

work 存在的话，把需要的数据取出来：title、desc，还有 content（上节课介绍的，里面有 components 和 props 两部分数据）。

## 创建 Vue App 与 template

现在使用上节课学的 createSSRApp 创建 Vue app：`const vueApp = createSSRApp({...})`。data 要特别注意，它是一个回调函数，返回需要的 components。写法上要做防御：content 有可能是 undefined，所以先判断有 content 再拿 content.components；如果 content 本身就是 undefined，给默认值一个空数组。

有了 data 就写 template。template 是一个字符串，使用 OpsFlow 组件库提供的 FinalPage 组件（组件库我已安装好，大家自行安装即可）：`<FinalPage :components="components" />`，把拿到的 components 传入它的 components 属性。

还有一步很重要、千万不要忘记：把 OpsFlow 组件库导入并在全局使用其中的组件。方法大家还记得：用 vueApp 上的 use 方法，以插件的方式把全局 components 添加上去：`vueApp.use(OpsFlow)`。这和浏览器端使用组件库是同样的方法。

之后就可以渲染了：`const html = await renderToString(vueApp)`，和上节课的知识一样。有了 html 就可以返回三项：html、title、desc。

## Controller：拆分 id 和 uuid

接下来完成 controller 中的逻辑。第一步把参数拿下来，参数是 id-uuid 的形式。大家想到的方法肯定是使用 split，但有一个问题：uuid 当中可能含有横线，比如 aabbcc-... 这种形式，直接 split 的话 uuid 可能获得得不完整。所以正确的方法是查找第一个横线的位置，然后用 slice 把字符串分割成两部分。

写一个简单的方法 splitIdAndUuid(str: string)。先准备最终结果 result（query 的形式）；如果 str 不存在，直接返回 result。然后用 `str.indexOf('-')` 查找第一个 dash 的位置 firstDashIndex；极端条件：它小于零（不存在）时，也把 result 返回，说明 query 有问题。最后解析：`result.id = str.slice(0, firstDashIndex)`；`result.uuid = str.slice(firstDashIndex + 1)`，从横线的下一个位置到末尾。处理完成，返回 result。

在 controller 里拿 ctx 和 app，取出参数 idAndUuid（来自 ctx.params），生成 query：`const query = this.splitIdAndUuid(idAndUuid)`。然后调用 service，外面套 try/catch，因为 service 里抛出了错误：`const { html, title, desc } = await this.service.utils.renderToPageData(query)`。

有了数据就可以渲染：`ctx.render('page.nj', pageData)`，第一个参数是模板名称 page.nj，第二个参数直接把 html、title、desc 打包成 pageData 放进去。catch 里出现错误时弹出对应的错误信息，我在 helper 里添加了一个，大家自己添加即可：`ctx.helper.error(ctx, 'h5WorkNotExistError')`。

## 测试与转义问题

测试：拿一个作品访问，9 是它前面的 id，后面是对应的 uuid，是我创建的一个作品。结果页面出现了转义后的字符串，也就是说它直接把 string 转义了。这需要在对应字段上添加一个指令。Nunjucks 有对应的指令 safe，文档里写了：如果开启了自动转译（autoescaping），所有输出都会自动转义。我们希望它输出 HTML 标签，所以要在变量后面加上 `| safe` 指令。保存后看结果：页面正常输出了，上面的元素都存在，位置也渲染到了对应的地方，第一步工作完成。

## 遗留的三个问题

虽然看上去可以完成最基本的任务（把元素渲染到页面），但还面临几个问题：

1. 页面全体的 props 没有添加上去，props 里有背景图，所以背景图并没有显示；
2. 样式可能出问题：这些偏移量的单位都是 px，在手机上浏览势必会出现误差，页面样式可能和原来不一致；
3. 组件库的 CSS 样式文件没有添加：组件库需要一个对应的 CSS，是整个组件的一系列样式，需要一个方法在模板中添加对应的样式文件。从 node_modules 直接拷贝一份放到 public 中，明显不是好方法。

这节课就讲到这里，留下三个有待改进的点，下节课继续改进，让它最终显示出一个完美的效果。
