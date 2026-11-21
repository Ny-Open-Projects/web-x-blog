# 5-19-Vuex 添加 mutations 和 getters

上节课让 Vuex 和整个应用完成了结合，现在任何组件都可以用 useStore 钩子函数取得 store 中的值，并响应式地显示。这节课完成任务清单上的下一项：更新 store 中的值。

## UserProfile 组件

我给应用添加了一个组件 UserProfile，放在 header 右侧，用来显示用户信息。它有一个 user 属性，类型定义和 store 中的 UserProps 完全一致，直接复用了 store 导出的类型。界面有两个状态：未登录时用 user.isLogin 判断，显示一个登录按钮；已登录则显示 userName，并且有一个下拉菜单，菜单里目前只有一个"登出"选项，用的是 Ant Design Vue 提供的 DropdownButton 组件，不熟悉可以去文档看。

要完成的任务：点击登录切换到登录成功的界面；点击登出切换回未登录界面，并把页面导航到首页。

## 添加 mutations

mutation 的写法我们已经很熟悉了。在 store 里创建两个 mutation：

```typescript
mutations: {
  login(state) {
    state.user = { ...state.user, isLogin: true, userName: 'viking' };
  },
  logout(state) {
    state.user = { ...state.user, isLogin: false };
  },
},
```

login 的参数是 state，先把原 user 展开，再覆盖：isLogin 变成 true，添加一个 userName。logout 更简单，把 isLogin 置回 false 即可。

## 在组件中提交

在 UserProfile 中创建两个函数，点击时调用。login 做的事是用 commit 方法提交 login 这个 mutation，提交后显示一条成功消息。消息用 Ant Design Vue 提供的 message，它是类似方法的调用：第一个参数是信息内容，第二个是 message 在界面上停留的时长：

```typescript
const login = () => {
  store.commit('login');
  message.success('登录成功', 2);
};

const logout = () => {
  store.commit('logout');
  message.success('退出登录成功', 2);
  setTimeout(() => {
    router.push('/');
  }, 2000);
};
```

logout 提交 mutation 后同样提示信息，再添加一个 setTimeout 延时跳转。跳转用什么？已经学过了：router.push 加上想跳转的路由，这里跳到首页。两个方法都 return 出去，登录按钮点击时调用 login，下拉菜单的登出调用 logout。

验证：点击登录，提示登录成功，界面切换到已登录状态；点击登出，状态切换回来，两秒后跳转到了首页。mutation 成功了。

## Getter

数据获取和更新都完成了，有了这两个前提，学习 Vuex 的另一个概念：getter。有时需要从 store 的 state 派生出一些状态，这非常类似 Vue 中的 computed。

比如 TemplateDetail 要获取对应的 template：需要在 store.state.templates 这个数组上用 find 查找，匹配当前页面的 params.id。如果多个页面都要用这段逻辑，就得把这一长串数组方法拷来拷去，不太理想。

Vuex 允许在 store 中定义 getter，可以认为是 store 的计算属性。像计算属性一样，getter 的返回值会根据它的依赖被缓存起来，只有依赖值发生改变才会重新计算：

```typescript
getters: {
  getTemplateById: (state) => (id: number) => {
    return state.templates.find((t) => t.id === id);
  },
},
```

它和 mutation 很类似，也是一个函数。因为要传入另一个参数（查找哪个 template），所以让 getter 返回一个函数，函数里接受 id 参数，类型是 number，然后 return find 的结果。

## 使用 getter

现在用 getter 替换那一长串写法，computed 保留：

```typescript
const template = computed(() =>
  store.getters.getTemplateById(Number(currentId))
);
```

特别注意：路由参数 currentId 是 string 类型，而 getter 需要的是 number，要做一个小转换。刷新页面点击模板，没问题，获得了 template 一的内容；再看另一个，获得了 template 二的内容。

## 补上类型

还有一个问题：看一下 TemplateDetail 里 template 的类型，是 computed 的 Ref<any>，没有正确的类型。我获取类型的心又开始激荡，必须让它也获得类型。手动指定一下，想到泛型。computed 接受泛型吗？没问题，它接受一个泛型，默认值 any。把 TemplateProps 导进来传给 computed：

```typescript
const template = computed<TemplateProps | undefined>(() =>
  store.getters.getTemplateById(Number(currentId))
);
```

传入后 template 就获取类型了。在模板上尝试：把 author 删除再输入，所有属性都自动补全出来，非常方便。

## 小结

这节课讲了怎样在应用中提交 mutations，还学习了用 getter 完成 store 中类似 computed 计算属性的操作。
