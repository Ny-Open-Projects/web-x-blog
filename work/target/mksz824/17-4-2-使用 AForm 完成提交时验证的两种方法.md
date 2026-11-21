# 17-4-2-使用 AForm 完成提交时验证的两种方法

上节课借助 AForm 和 async-validator，我们已经能对每个表单项单独验证，但触发时机还停留在 input blur。真正需要的是表单提交时的整体校验，也就是点击登录按钮的那一刻验证整个表单的结果。AForm 为此提供了两种方式，这节就分别实现一遍。本章后面还会回到 AForm 的源码，看看它内部是怎么完成这些工作的。

## 方式一：通过实例方法 validate

AForm 组件的实例上挂着一系列方法，比如 `validate`、`validateFields`，都是实例方法。要拿到实例，最直接的办法就是加一个 ref。

先创建一个 ref，命名为 `loginForm` 并返回出去，再把对应的 ref 绑到模板的 AForm 上。接着写一个函数来执行验证过程：

```ts
const login = () => {
  loginForm.value.validate().then(() => {
    alert('pass')
  })
}
```

问题马上出现了：`loginForm.value.` 后面点不出任何方法，因为这个 ref 目前是空的 `Ref<any>`，没有类型信息。解决办法是自己定义一个 `RuleFormInstance` 接口，Ant Design Vue 并没有暴露现成的实例类型。接口里先声明一个 `validate`，返回 `Promise<any>`；如果后面要用到 `validateFields` 等其他方法，再逐个补上即可。

然后给 ref 做类型断言，指定为 `Ref<RuleFormInstance>`。注意这里必须是大写的 `Ref` 类型，和小写的 ref 函数不是一回事：

```ts
const loginForm = ref<RuleFormInstance>()
```

`validate` 返回的是一个 Promise，成功分支的 then 里能拿到验证通过的结果；如果想在验证失败时做处理，可以再补一个 catch。把 login 绑到登录按钮的点击事件上，点击触发验证。

运行验证一下：直接点击登录，表单项会被依次 validate，验证不通过的状态被标记出来；把验证码随便填上四位再点登录，页面弹出 pass，说明整体验证通过了。第一种方式到此完成。

## 方式二：使用 useForm 钩子

另一种方式来自 Ant Design Vue 官方另行维护的一个 hooks 仓库，里面提供了一批常用钩子，比如 useClickAway、useDraggable，还有处理表单的 useForm。这套设计把表单功能从组件里剥离出来独立存在，很符合逻辑与界面分离的思想。建议有空看看其他 hook 的实现，和项目里自己写的 hooks 对比一下异同。

从 `@ant-design/use` 引入 useForm 之前，需要先把 rules 改成响应式对象。useForm 接受两个参数：第一个是表单数据的响应式对象 form，第二个是 rules 的响应式对象。拿到返回值后，可以解构出一系列方法，最常用的就是 `validate`，另外再演示一个 `resetFields`。

有了 useForm，就可以直接调用 validate，不再依赖组件实例。把之前的调用替换成 `validate().then(...)`，运行后同样弹出 pass，功能完全一致。顺便试试 resetFields：在验证成功的回调里调用它，点击 alert 的确定后，表单里的值被清空，reset 的本质就是把 fields 恢复到初始状态，也就是清空。

## 小结

这节完成了 Ant Design Vue 中 Form 的动态验证：实例方法和 useForm 钩子是两条完全不同的路径，效果等价。至此表单验证功能收尾，下一节开始实现发送验证码等登录流程。
