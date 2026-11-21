# 21-8-添加 VeeValidate 第二部分

这节课继续验证任务：把 VeeValidate 和之前用 Zod 定义的 schema 结合起来，并完成表单提交时的统一验证。

## 对接 Zod

求助文档可以看到，VeeValidate 可以接各种各样的验证库，文档里列了三种流行的方案：Yup、我们用的 Zod，还有 Valibot。它们都是独立的库，所以需要再安装一个对接用的包：`npm install @vee-validate/zod`。

装好后回到代码，导入 `toTypedSchema` 函数。转换很简单，用它包裹我们自己定义的 `userLoginSchema`，然后替换掉 useForm 里手写的 validationSchema：

```ts
import { toTypedSchema } from '@vee-validate/zod'

const validationSchema = toTypedSchema(userLoginSchema)
```

到这里两者就结合起来了。为了验证效果，把 password 也接上：到 password 的 input 上，加 `v-model` 和 `v-bind="passwordAttrs"`，并让它即时验证。到登录页面输入任意值，invalid email 立即出现；输入 password 后，超过六位再补几位，第二个错误就消失了。Zod 里定义的两条规则完美运行起来。

## handleSubmit 统一验证

下一个任务是处理表单提交。现在是在单个 input blur 或 change 时验证，我们需要在点击 sign in 时做统一验证。VeeValidate 提供了 `handleSubmit` 方法，从 `useForm` 返回值里解构出来，用它包裹提交函数：

```ts
const onSubmit = handleSubmit(async (values) => {
  console.log(values)
})
```

修改后它会多出一个参数 values，就是提交后通过验证的值。原来的手动验证逻辑都不需要了，`login` 里的 safeParse 调用可以删掉，只保留最后一部分。这里 `handleSubmit` 内部的回调只在验证通过后才被调用。

还要修改一点：之前在 submit 事件上加了 `.prevent` 阻止默认行为，包裹以后它自动处理了这个问题，画蛇添足反而会影响行为，要删掉。

接着修改错误绑定，换回新做法：直接在 errors 里取值。`errors.email` 存在时边框换成红色，不存在用原始的。特别注意后面错误文本部分直接写即可，它会自动处理，现在 errors 里的值是 string 而不是之前的数组了。password 一样改成 `errors.password`，错误信息同样修改。把不再需要的变量删掉，保存看结果。

目前没有任何值，点击 sign in，required 系列的错误都显示出来了，而且 console.log(values) 没有触发，因为没通过验证；改了几个值但仍不合规，再点还是不触发。

这里有个浏览器默认行为的坑：input 上有个 `type="email"`，浏览器会自带一套验证。把它改成普通的 `type="text"`，去掉浏览器的默认验证，这样更贴合我们的流程。

现在把所有字段填合规，点击 sign in，email 和 password 都打印出来了，功能完成。

## meta 与提交状态

完成表单后，`useForm` 还返回很多和提交相关的变量。其中有一个总的变量 meta，存放一系列表单提交相关的状态信息。还有一些以 is 开头的判断变量，最常用的是 `isSubmitting` 和 `isValidating`：前者表示表单正在提交（提交可能是异步过程），后者表示表单正在验证。

把 meta 输出看看。刷新回到初始状态，meta 里有一系列代表表单当前状态的变量：initialValues 是最初始的值（现在全空所以为空），touched 是否被修改过，pending 是否正在验证，valid 是否合法，dirty 值有没有变化。随意输入几个值，它们都会实时变化，都是响应式对象。全部填对后，valid 就变成 true 了。

再试 `isSubmitting`，它代表表单提交正在处理、等待响应。特别常见的场景是：提交时发送异步请求，此时把按钮设为 disabled，防止用户多次点击发出多个请求。为了模拟这个场景，在提交回调里手动加一个两秒延时：

```ts
await new Promise((resolve) => setTimeout(resolve, 2000))
```

让最终返回延迟两秒执行。然后调用真正的后端接口，也就是上节课写过的逻辑：

```ts
const result = await $fetch('/api/login', {
  method: 'post',
  body: values
})
```

URL 是 login，body 直接传 values，method 用 post。result 返回值在这里能被完全推断出来，因为后端的 schema 也是同一个 Zod 定义，前后端写在一块非常方便。顺便把返回数据修改得更真实一点，返回 username。

## 按钮禁用与 loading 态

有了异步发送后，修改 button 状态：在 `isSubmitting` 为 true 时给它加 disabled 属性。再加一个状态样式，正好用 Tailwind 提供的 disabled 前缀，表示 button 禁用时附加的样式：加 `disabled:opacity-75`，透明度 75%，看起来浅一点，是禁用的感觉。

按钮文字也改一下：`isSubmitting` 时显示 loading，代表正在提交，普通情况显示 sign in。

所有代码修改完毕，验证一遍：填一个正常的 email，填一个六位的 password，点击 sign in，按钮显示 loading，两秒后成功跳转，说明 `isSubmitting` 成功运作了。

通过这两节课，我们成功改造了表单验证，把 VeeValidate 和 Zod 完美结合。这也是表单验证的通用解决方案，可以更灵活地完成验证工作。希望大家以后的项目里用上这对完美拍档，它们是现在最流行的方案。这节课到这里。
