# 15-6-2-BackgroundProcesser 组件编码第一部分

上节课完成了背景设置的一部分展示，其中背景图片这个属性对组件有特殊要求。这节课来处理它。

## 需求：两种情形两种组件

背景图片属性是 background-image，它的值分为两类：

- **值为空**：要完成图片的上传，渲染一个上传组件，使用左侧用过的 StyleUploader。上传完毕一样发送 change 事件出去，发送一个新的地址。注意这里不发送纯图片地址，而是要用 `url(...)` 这种字符串进行包裹，这种格式才符合 background-image 的格式。
- **值不为空**：值是一个形如 `url("xxx")` 的字符串，需要用 ImageProcessor 进行处理。ImageProcessor 我们都知道，它可以重新上传图片、裁剪图片，这里还有可能多加一个按钮：删除图片，让它恢复到空的值。注意它接收的 value 不应该是带 URL 的完整值，需要把 URL 加括号这些内容去掉，取出来的才是真正要传入的 value。重新上传、裁剪完毕后它要发送新的这种格式值，删除后发送空值。

总结下来，就是在两种情形下渲染两种不同的组件，把它们组合起来，并且遵循表单处理属性的原则：传入 value，更新以后发射 changeEvent 事件并带着新的值。

## BackgroundProcessor 第一部分编码

现在完成 BackgroundProcessor 组件，本节课只做展示，在两种不同的情形下展示两种不同的组件。

新建 BackgroundProcessor，把 ImageProcessor 和 StyleUploader 两个组件导入进来。然后判断传入的 value：有值时选择 ImageProcessor 渲染。模板中：`v-if="!value"`（没有值）时使用 style-uploader 展示；`v-else` 时使用 image-processor 展示。很简单，这一步先管展示。

## 类型层面的修改

展示弄完以后，在 propsMap 中添加对应关系，添加到最后一位，输入想要的 background-image。但会发现有点问题：自动补全打不出 background-image，并且会爆出类型错误。

原因是 propsMap 的类型是 PropsToForm，它的键使用 `P in keyof AllComponentProps`，描述的是组件属性所有 key 的组合，现在不够准确了，我们在上面添加的是页面属性的设置，还需要给类型里添加更准确、更多的属性值。

来到 `editor.ts` 添加类型：之前我们把 PageData 的 props 设置成了 indexable type，现在看来不太准确，需要更精确地确定它的类型。添加一个 `PageProps`，和 AllComponentProps 类似，里面有五个属性。然后导出一个 `AllFormProps`，它是 PageProps 和 AllComponentProps 的交叉类型。

这样就能很精确地描述 propsMap 里一系列 key-value 的对应关系了。把 propsMap 的类型改过来。

关于给每种数据都添加类型，大家可能觉得繁琐，后期新添加值还可能要修改 PageProps 接口。我认为怎么做完全看自己的意愿和项目的需求。我对 TS 的使用态度是让它更准确地描述数据的类型，能准确的话一般都选择更准确的描述。如果你愿意直接使用 indexable type，更简单快捷，也没有问题，不需要定义这么多精确的类型。

## 添加对应关系与组件注册

完成类型修改后，回到 propsMap：从 `./store/editor` 导入新的类型 AllFormProps，做一个替换，提示就更精确了。在最下面添加 background-image 的对应项：添加一个默认的 handler，它特殊的内容是 component，即新建的 BackgroundProcessor。

添加完毕后，还要在 PropsTable 里再添加一下。记住：假如要引入一个新的属性，都需要在两处进行修改，第一处是 propsMap 里添加对应关系；第二处是 PropsTable，如果是新的 component，要在这里添加对应的引用，否则无法渲染。

这里同学们可能会想到一个可以优化的点：用来处理组件属性的表单特殊组件越来越多了，当多到一定程度时，是否能给这些组件单独发布一个组件库？这样就不需要每多加一个独特属性就在 PropsTable 里添加一次，而可以以插件的形式在 main.ts 里 use 整体使用。这是一个小的思索，这里还是先直接添加：把 BackgroundProcessor 添加到 components 中去。

## 界面验证

点击页面设置：当值为空时，显示 StyleUploader 上传组件，没问题（样式后期可能再修改）。现在把值换一下：来到 editor.ts，给它添加一个默认值，带 URL 的图片。添加完毕后，URL 已经添加到外面的 container 上，渲染出了背景图片。

但点击页面设置发现一个问题：虽然这里渲染出了 ImageProcessor，但左侧的图片还是一片空白。这是因为我们传入的 URL 是 `url("xxx")` 这样的字符串，并不是直接的图片地址，之前也分析过，需要在传入之前使用 initialTransformer 做一个对应的转换，把括号中的 URL 从字符串里取出来。这看起来是正则的工作，下节课完成对应的取值工作。
