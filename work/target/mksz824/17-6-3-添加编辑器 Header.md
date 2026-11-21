# 17-6-3-添加编辑器 Header

作品已经能完整展示在页面中了，下一步添加头部 header。这个任务相对轻松，先明确需求：

- 最左侧是 logo，点击跳转首页，用 router-link 实现；
- 旁边展示作品标题，即 page 上的 title 属性；注意 title 点击后要变成可编辑的 input，直接复用写好的 InlineEdit 组件；
- 中间是三个按钮：预览和设置、保存、发布，行为暂时不实现；
- 最右侧是"我的账户"加下拉菜单，里面是账户相关操作。

由于功能简单，大部分代码直接照现有样式书写。在 ALayout 里嵌套一个新的 layout，加上对应的 header。

## 左侧：logo 与可编辑标题

左边是 router-link 到首页（放了一个简单的图片 logo），右边是 InlineEdit。创建 class 为 page-title 的容器，display: flex，两栏自动左右分布。

InlineEdit 要编辑的是 PageData 中的 title。value 直接绑定 page.title；更新逻辑新建一个函数 titleChange，接受新标题（string），执行 `store.commit('updatePage', { key: 'title', value: newTitle })`，更新的是配置根上的数据。

```ts
const titleChange = (newTitle: string) => {
  store.commit('updatePage', { key: 'title', value: newTitle, isRoot: true })
}
```

查看 editor.ts 里的 updatePage mutation，发现它目前只能更新 props，更新不了 page 一级的属性。于是参照 updateProps 的处理多加一个 isRoot 参数：判断要更新的是否是根属性，是的话执行 `state.page[key as keyof PageData] = value`。调用侧传 `isRoot: true`，把 titleChange 返回出去，绑到 InlineEdit 上。

页面检查：header 渲染出来了，点击标题、修改、回车，更新成功。左侧完成。

## 右侧：按钮菜单与用户信息

右侧用 Ant Design Vue 的导航菜单做一个横向导航；不使用组件、直接用 ul 设成横向也完全可以，看个人意愿。在 editorView 文件中，加到 page-title 外侧：

```html
<a-menu :selectable="false" theme="dark" mode="horizontal">
  <a-menu-item key="preview">预览和设置</a-menu-item>
  <a-menu-item key="save">保存</a-menu-item>
  <a-menu-item key="publish">发布</a-menu-item>
</a-menu>
```

selectable 设为 false 表示不可选中，theme 是 dark，mode 是 horizontal，三个 key 对应预览和设置、保存、发布。

最后添加第四项 UserProfile 下拉框。它接受一个 user，所以要补上数据：新建 userInfo 变量，computed 返回 `store.state.user`。保存后查看布局：标题、按钮、用户名和操作菜单都完整出现，组件复用正常。

header 至此实现完毕，样式和两个简单交互都有了，剩下的就是三个按钮背后的页面操作，接下来逐个完成。
