# 17-4-1-使用 AForm 完成表单验证

上一节课简单了解了 action 的概念和用法。这节课开始攻克用户权限的第一部分编码。获取权限从登录页面开始，它就是出发的地方。

先把整个登录页面弄进来。样式代码我就不带着写了，直接把美化后的页面放在这里。Login 模板大家都还记得，它是一个特殊布局的模板，没有 header 和 footer，样式直接复制我的源代码即可。

## 表单结构

页面里有一个重要内容：表单。表单在任何应用中都是非常重要的部分，自然要完成表单验证。这里使用 Ant Design Vue 提供的 Form 组件，它自带验证，详细信息可以在文档里了解。

按组件格式创建表单，两项分别是手机号码和验证码。父组件是 `a-form`，`layout` 属性设为 `vertical` 就是纵向表单；子选项每一项是 `a-form-item`，`label` 生成上面的文字，加上 `required` 会出现红色的必填标识；内容是 `a-input`，我加了自定义 template，会渲染出带图标的格式。这就是 a-form 的整体结构。

## 获取表单的值

第一步任务是拿到表单的值。创建响应式对象存放数据：

```ts
const form = reactive({
  cellPhone: '',
  verifyCode: '',
})
```

两项都是空字符串，创建后把它 return 出去。然后把整个 form 对象添加到 a-form 的特殊属性 `model` 上，并用 `v-model` 绑到两个 a-input 上：手机号是 `v-model:value="form.cellPhone"`，验证码是 `v-model:value="form.verifyCode"`。这样响应式对象的值就会随 input 的改变同步更新。

## 添加验证规则

第二步是添加验证。查文档可知 a-form 接受一个名为 `rules` 的属性，在里面添加各种验证条件：

```ts
const rules = {
  cellPhone: [
    { required: true, message: '手机号码不能为空', trigger: 'blur' },
  ],
  verifyCode: [
    { required: true, message: '验证码不能为空', trigger: 'blur' },
  ],
}
```

每一项规则里：`required: true` 表示必填；`message` 是校验不通过时的错误信息；`trigger` 是触发时机，这里是 `blur`，即 input 失去焦点时触发。rules 也 return 出去，加到 a-form 的 rules 属性上。

特别注意：要让规则生效，a-form-item 上的 `name`（cellPhone、verifyCode）必须和 rules 里的 key 一一对应，才能匹配上产生效果。

保存后测试：什么都不填直接 blur，会出现对应的错误提示，验证码也一样，验证已经生效。

## 用正则添加格式校验

我们希望手机号只能符合特定格式。Ant Design Vue 的底层实现用的是 async-validator，这是一个非常好用、支持异步的验证库。它的 rules 每项对应不同的验证规则：`type` 是期望的数据类型，`required` 是必选，`pattern` 可以接受一个正则（必须通过正则才算验证通过），还有 range、len 等一系列丰富的支持。

给 cellPhone 再添加一条规则，用 `pattern` 写手机号正则：

```ts
{
  pattern: /^1[3-9]\d{9}$/,
  message: '手机号码格式不正确',
  trigger: 'blur',
}
```

正则解读：`^` 和 `$` 是开始和结束符号；第一位是 1，第二位是 3 到 9，`\d` 是数字重复九位，组成一个十一位的手机号。测试：随便输入一个错误的手机号码，会跳出「手机号码格式不正确」。这样就有了一个字段多规则的做法。

## 自定义异步验证器

对于比较难搞定的验证，async-validator 还支持自定义写法。手机号有时需要发送远程请求验证结果，所以这里用 setTimeout 模拟一个异步过程，它支持返回 Promise。创建 `cellNumberValidator`：

```ts
const cellNumberValidator = async (
  rule: RuleObject,
  value: string,
): Promise<void> =>
  new Promise<void>((resolve, reject) => {
    const passed = /^1[3-9]\d{9}$/.test(value.trim())
    setTimeout(() => {
      if (passed) {
        resolve()
      } else {
        reject(new Error('手机号码格式不正确'))
      }
    }, 500)
  })
```

validator 有特殊的格式：两个参数，第一个是 rule（当前这条规则），第二个是 value（传入的值）。想拿 rule 的详细类型，可以从 Ant Design Vue 暴露出来的 `RuleObject` 类型取，不过这里不使用它。value 是 string 类型。它返回一个 Promise，两个参数 resolve 和 reject。内部还是用正则的 `test` 方法判断，返回布尔值，value 先 `trim` 一下。setTimeout 模拟异步，延时设为 500（0.5 秒）：if passed 就 resolve 空值出去；否则 reject，里面的信息最后会显示到错误提示的那行红字上。

然后替换规则：把原来的 pattern 规则注释掉，新加一项用 `asyncValidator` 属性指定 `cellNumberValidator`，trigger 同样是 blur。测试：输入一个错误的手机号码，短暂的延时后错误信息弹出，显示「手机号码格式不正确」。自定义验证器生效了。

这是一个非常强大的工具。以后有复杂验证相关的需求，我建议都使用 async-validator 这个库来完成，很多知名的第三方库都用它作为底层验证工具。

表单验证的过程就完成了，这节课的第一个任务到此结束。下节课继续完成验证剩余的工作。
