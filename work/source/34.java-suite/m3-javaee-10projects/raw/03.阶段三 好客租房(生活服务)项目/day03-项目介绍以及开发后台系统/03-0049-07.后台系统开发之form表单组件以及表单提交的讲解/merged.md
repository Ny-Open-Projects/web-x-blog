# 07.后台系统开发之form表单组件以及表单提交的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\07.后台系统开发之form表单组件以及表单提交的讲解【海量资源尽在 ubkz.com】.mp4
- 时长 13分50秒（音频 831s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下form组件form组件呢也是按照底下中的比较常用的组件我们来说一下前面我们这个没有讲过我们给大家来说一下那么首先呢我们先打开form组件这个官方的文档我们来看一下是在这那么这个呢是说看一下它官方的一个描述就是具有数据的搜集教验以及提交功能的这个表单
[00:29] 包含什么复选框呢单选框的输入框的下拉选择框的等元素也就是说他呢不仅仅是说做了一个表单而且把这个什么呢教验是不是也做进去了也就是说我教验这个也OK了对吧我们也可以直接去使用好那我们来看一下他的一些这个使用的方法那么下面是不是就是一些代码的一些演示那么可以看一下他效果比如说一个username和password点击这个提交对吧
[00:59] 大家输入一些内容好是不是就可以点击这个提交了就这样的一个效果那么这个就是它的一些这个原码对吧原码实现这个原码OK好那么它的实现的有很多包括有这种什么的教验的这种这种情况有教验教验说你必须不能为空不能为空必须要输入什么等等等等OK那么这个呢也是一种教验是吧比较做一些这种高级的这种搜索OK
[01:29] 然后呢我们这个就不看了就是说一些这个使用方法就不看了那我们就看一下它下面的一些这个API那么API的操作呢我们重点要关注的是这个form.create这个方法那我们来看一下下面呢它其实有一个描述我们来看一下在这它说经过什么呢form.create这个包装之后的组件呢将会自带一个race.purp stone
[01:56] 然后的点form属性那么有了这个form属性之后或者说有了这个form对象之后那么它将提供了下面这么一堆的这些方法一堆的方法那我们来看一下下面这个方法有很多那么这样的话我们就可以非常灵活的去操作我们这个表单好那我们来看一下在我们页面中的一个使用那么我们可以看到在这个位置是不是有一个我们定义了一个类叫做
[02:25] 按的resource就是新增房源这个页面然后呢我们在上面是不是添加了一个修饰符叫做form.create那么是不是就是调用了它的一个form.create对吧那么通过这种方式之后啊那么就在我们的propos中就会有一个form对象那么我们拿到这个form对象之后啊就可以做下面一系列的这个操作一系列操作包括你可以看到在这个位置是不是也会去做一个validator field去做一个校验
[02:53] 那么也可以呢是看一下他的文章啊也可以呢去一系列下面一些内容包括像这个啊比较常用这个呢是指什么呢和表单做一个双向的一个绑定啊还可以去获取这个failed的一些error的信息然后呢可以去做一些set值set failed值对吧等等那么所以说我们通过他之后呢就可以做一些这个操作了那么但是大家要注意的是
[03:21] 那么如果我们想要通过下面什么getFilledValue什么FilledFilledValueFilledValue
[03:30] 以什么set field value的操作的时候我们必须要保证必须要保证什么要保证我们的 field已经被get field decorator这个方法注册过了那么也就是说我们必须要给它做一个什么数据的双向绑定之后才能够去做下面的一系列操作我们来看一下在我们的页面中我们也是这样去做的
[03:56] 怎么做呢来找一下找一下我们form中的这个元素你可以看到你比如说像这个租金吧以这个为例一个租金为例那么这个form item显然是form中的一个元素然后呢在下面呢我们是不是就可以看到它的一个这个input curve当然了这个是把这个放大一点来看一下在后面这个位置是不是有input的标签是不是就我们的输入你看比如说多少元每月你看一下
[04:26] 是不是我们的一个页面啊呃多少元啊多少元每月那么就在这个位置那么我们通过什么呢通过这个get field的decreator那么通过它呢就可以把我们的这个影铺的标签的做一个双向的数据绑定那么我们就可以把我们的数据和我们的这个对象啊和这个和这个
[04:50] 去哪了和这个值去做一个绑定我们就可以通过它来获取我们的值也可以去设置这个值那么也可以去通过我们官方所提供的一些这种API去做一些相关的操作OK好那么这个就是它的一个基本的用法那么一定要切记的是我们要通过getfielddecorate它去做一个数据的双向绑定那么才能够获取它的一些值
[05:18] 那么在官方的也有这样的一个描述啊大家可以来看一下就是我们经过这个双向数据绑定的一个绑定之后啊那么我们的这个空间的会自动添加这个value以及这个onChange这样的一些属性那么我们呢就不用再给他添加一些什么呢这个trigger呀
[05:39] 什么value, purpose, name等等一些属性值了那么我们这个呢已经就被我们的这个它的数据同步已经被这个form做一个接管那么我们也不需要也不应该由这个onChange来做同步但是我们可以还是用这个onChange事件去监听它的一些数据的一些变化等等那么还要注意的是我们不要给这个空间再设置什么叫deferred value这个属性
[06:05] 而是通过他这个方法中有一个参数有个叫init有init value来设置这个值OK那么我们来看一试这个里面我们也有一些这个设置来找一下比如说你看像这个位置是不是有一个叫支付方式那么在支付方式中它是不是也有一个init的一个value对吧这个就给他做一个初始化值而不要在这个位置再给他设置什么default value
[06:32] 你看有个deferred value不要再这样去设置如果这样设置的话他到时候会有个警告的错误OK他就讲的就是这个意思好那么同样的我们也可以给他去增加一个教验那么也是在这个degrader中去他的属性添加一个教验规则那么怎么样去添加呢我们来看一下
[06:52] 那么是不是通过我们这个方法然后呢第一个就是我们这个自断然后呢后面是添加一些参数那我们可以看到参数中有一个教验规则那么在这个教验规则中呢是不是有一些这个内容不是required to代表这个是必须的然后呢match则就是说如果你没有去填写的话那么违反了这个规则的话它会提示什么ok做了这样的一个教验规则的一个填写
[07:19] 当然了他也支持一些其他的教验规则我们来看一下教验规则往下面找一下你看在这个位置是不是支持有这么多的教验规则包括我们可以去教验他的一些长度最大支段长度和最大长度以及什么呢通过这个也可以通过这个表达式正着表达式去做一个这个教验还可以呢去做一些这个什么呢是
[07:47] 我看一下还可以去校验它的一些有这个有个内建的教研这个内建教研什么意思我们点开来看一下那么点这个可选项点击一下它那么点击它它就会打开一个GitHub上面的一个地址那么这个type就是说它可以去教研我们这个里面的数据的值那么比如说是不是我们的number
[08:13] 那么教验的值必须是这个never类型就是你输的这个数据它必须是这个数字类型OK通过这个type来做一个这个教验那么它所支持的一些type类型呢有这么多大家点击点击这个可选项就可以找到它是不是有这么多的一些可教验的一些这个选项OK好那么这个呢就是对于这个表单的基本的一个讲解那么下面我们来看一下表单这个提交
[08:43] 表单提交它也是通过一个submit按钮来完成然后我们通过一个unsubmit的方法进行拦截处理我们来找一下我们找到在最下面有一个提交的按钮找到最下面在最下面这个位置我们可以看到你可以看到在这个位置是不是有一个button然后它的类型是一个submit那么通过submit提交那么我们需要在我们的form中给它添加一个
[09:09] onSubmit这样的一个属性来指定一个函数我们去拦截这个提交那么拦截的意义呢就是我们在提交之前是不是可以做一些这种处理在处理完成之后呢去真正向我们的服务端去提交数据去是不是OK那我们来找到this.handleSubmit来看一下那么是不是在这个位置我们去定义了一个
[09:30] 我们这个函数或者这个方法通过一个箭头函数做一个定义在这需要提醒大家的是我们这个方法并不入在外部的定义而是在我们的class内部所以我可以通过这个this点直接去调用它那么在内部定义方法也可以直接去操作我们的propos或者是我们的一些state这样的一些内置的一些对象OK好那么我们可以看到
[09:58] 在这个里面呢我们是不是就做了一些这个业务逻辑的处理那么这个大家基本应该能够看懂啊就是我们对他呢去做一些这个form的一个validating教验那么教验完成之后呢如果是说没有错误的话那就代表着我们教验全部都通过了比如说我现在点击这个点击他啊点击他走那么显然教验是不是没有通过啊那么没有通过那么是不是就不会去做一个提交
[10:24] 对吧等到我们教验通过之后呢我们才去做一个这样的一个提交OK好那么我们来看一下这个里面的一些处理逻辑啊那么有些逻辑是什么意思呢来看一下那么我们看一下比如说我就拿他他为例吧这个是什么意思呢我们来找一下搜索一下搜搜搜搜你可以看到在这个位置呢在这个位置我们的所写的这个数据呢是一些我们的
[10:54] 这个租房中的一些房屋的这个配套的设施比如有水有电有煤气等等一些的话那我们就需要在对应的页面中是不是去打勾啊对吧那么我们最终提交到我们后台的或者提交我们后端服务的数据它长什么样呢我们可以来找一下找一下我们那个文档来看一下这个文档那么在这个文档中呢我们来找一下它的一些配套的数据
[11:21] 那么配套的数据呢其实可以看到是不是在找一下在这你看这个里面是不是配套的设施我们所提交的数据呢是一逗号二逗号三是不是这样的一种形式而在我们的页面中呢是不是它是一个一个的这个checkbox那么我们是不是去提交的时候就可以拿到多个对不对但是呢我们提交的时候我们并不能够
[11:45] 多个去提交而我们要提交的是一个这副串然后呢他以逗号分割的这样的一种方式那么我们应该怎么处理呢我们可以往上面找来看一下他处理的方法是不是就是我们拿到这个值他是一个素组然后呢做一个连接用逗号做一个连接是不是生成一个这副串然后呢给他做一个覆盖那么覆盖之后呢最终提交的是不是就是这样一个这副串那么继续往下面看这个位置也是一样啊那我们来搜一下这个
[12:14] 来搜一下我们看它是什么意思早早早早那么在这个位置是不是我们可以看到它是一个楼层的数据对吧那么总和第几层总共第几层那么来看一下这个页面中的一个情况那么是不是你楼层是第几层总共几层对吧那么在我们的后台的这个数据中它要求是一个什么结构来看一下
[12:37] 那么他要求是这样的一个结构是不是就是比如说8斜杠26就代表着我这栋楼总共有26层那么你现在这层的房源是在8楼这样的一个表示那么我们就需要拿到这个数据之后然后在上面这个位置给他去做一个数据的一个处理那处理之后是不是就去做一个提交对吧新增一个这样的一个制段
[13:02] 那么注意我们原来的这两个字段是不是就没用了所以我们给它做一个delete把它删掉,做了一个逻辑那么下面的也是一样了那么也就是说我们可以在unsubmit的方法中是不是拦截我们提交然后对我们的数据做一些处理处理完成之后是不是再做一个真正的提交我相信这个代码大家就能看懂了disperse是不是可以调用我们model中的一些方法OK好,我们接着继续往下面看
[13:30] 那么这个呢是不是就是我们表单的一个这个提交啊哎OK那么我们在我们的这个validate这个方法中呢通过一个values就可以去拿到我们的一个提交的一个表单的一个数据啊哎OK好那么关于这个表单的一个使用以及它的一个表单的提交呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Ant Design 的 Form 组件在 React 项目中的使用，包括表单域的结构、验证状态、自定义表单以及与 Redux 的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Ant Design 官网的 Form 组件文档，介绍表单的两种排列方式（水平排列、垂直排列、行内排列）和表单域的组成。
画面 2: 展示 Form 组件的验证状态示例，包括成功、警告、失败和错误状态，以及日期选择器的验证。
画面 3: 展示 Form.create() 包装组件后提供的 API，包括 getFieldDecorator、getFieldError、getFieldValue、isFieldsTouched、isFieldValidating 等方法。
画面 4: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中使用了 Form.Item 和 Input 组件，并通过 getFieldDecorator 进行表单字段的装饰。
画面 5: 展示 Form.create() 的 API 文档，包括 mapPropsToFields、validatMessages、onFieldsChange、onValuesChange 等方法。
画面 6: 展示 Typora 中的 markdown 文档，内容是关于 getFieldDecorator 的使用说明，包括其特性、注意事项和相关 GitHub 链接。
画面 7: 浏览器地址栏显示正在访问 GitHub 上的 async-validator-type 仓库。
画面 8: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中使用了 Select 组件和 getFieldDecorator 进行表单字段的装饰。
画面 9: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中定义了 formItemLayout 和 submitFormLayout 的样式配置。
画面 10: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中定义了 handleSearch 函数，用于处理搜索逻辑。
画面 11: 展示 Word 文档中的表格，列出了房源信息的字段，包括 id、name、province、city、area、address、year、type、propertyCost、propertyCompany、developers、created、updated。
画面 12: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 facilities 和 floor 字段的值，并在提交前进行拼接和清理。
画面 13: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 houseType 字段的值，并在提交前进行拼接和清理。
画面 14: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 houseType 字段的值，并在提交前进行拼接和清理。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```jsx
<Form.Item {...props}>
  {children}
</Form.Item>
```

画面 2:
```jsx
Validating: I'm the content is being validated!
Success: I'm the content
Warning: Warning
Fail: unavailable codes
Should be combination of numbers & alphabets
Success: 请选择日期
Warning: 请选择时间
Error: Option 1
Validating: The information is being validated...
Success: 请选择日期
```

画面 3:
```jsx
const EnhancedForm = Form.create()(CustomizedForm);
this.form // => The instance of CustomizedForm
```

画面 4:
```jsx
this.setState({
  estateAddress: v.substring(v.indexOf('') + 1),
  estateId: v.substring(0, v.indexOf(''))
})
onSearch={(this.handleSearch)
filterOption=(inputValue, option) => option.props.children.to
<Form.Item {...formItemLayout} label="楼盘地址">
  <Input
    prefix={<Icon type="environment" style={{ color: 'rgba(0,0,0,25%)' }} />}
    value={this.state.estateAddress}
    defaultValue={this.state.estateAddress}
  />
</Form.Item>
<Form.Item {...formItemLayout} label="楼栋">
  <InputGroup>
    {getFieldDecorator('buildingNum', {rules: [{ required: true, message: '楼栋号必填' }]})(
      <Input />
    )}
    {getFieldDecorator('buildingFloorNum', {rules: [{ required: true, message: '楼层号必填' }]})(
      <Input />
    )}
  </InputGroup>
</Form.Item>
<Form.Item {...formItemLayout} label="租金">
  <Form.Item compact>
    {getFieldDecorator('rent', {rules: [{ required: true, message: '此项为必填项' }]})(
      <Input />
    )}
  </Form.Item>
</Form.Item>
<Form.Item {...formItemLayout} label="支付方式">
  {getFieldDecorator('paymentMethod', {initialValue: '1', rules: [{ required: true, message: '此项为必填项' }]})(
    <Select style={{ width: '100%' }}>
      <Option value="1">付一押一</Option>
      <Option value="2">付三押一</Option>
      <Option value="3">付六押一</Option>
      <Option value="4">年付押一</Option>
      <Option value="5">其它</Option>
    </Select>
  )}
</Form.Item>
```

画面 5:
```jsx
mapPropsToFields
validatMessages
onFieldsChange
onValuesChange
```

画面 6:
```jsx
{getFieldDecorator('paymentMethod', {initialValue: '1', rules: [{ required: true, message: '此项为必填项' }]})(
  <Select style={{ width: '100%' }}>
    <Option value="1">付一押一</Option>
    <Option value="2">付三押一</Option>
    <Option value="3">付六押一</Option>
    <Option value="4">年付押一</Option>
    <Option value="5">其它</Option>
  </Select>
)}
```

画面 8:
```jsx
<Select style={{ width: '100%' }}>
  <Option value="1">付一押一</Option>
  <Option value="2">付三押一</Option>
  <Option value="3">付六押一</Option>
  <Option value="4">年付押一</Option>
  <Option value="5">其它</Option>
</Select>
```

画面 9:
```jsx
const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 7 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 12 },
    md: { span: 10 },
  },
};
const submitFormLayout = {
  wrapperCol: {
    xs: { span: 24, offset: 0 },
    sm: { span: 10, offset: 7 },
  },
};
```

画面 10:
```jsx
dispatch({
  type: 'form/submitRegularForm',
  payload: values,
});
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateList.forEach((y, k) => {
      if(y.startsWith(value)) {
        arr.push(k);
      }
    });
  }
};
```

画面 11:
```markdown
| id | Long | 楼盘id |
| --- | --- | --- |
| name | String | 楼盘名称 |
| province | String | 所在省 |
| city | String | 所在市 |
| area | String | 所在区 |
| address | String | 具体地址 |
| year | String | 建筑年代 |
| type | String | 建筑类型 |
| propertyCost | String | 物业费 |
| propertyCompany | String | 物业公司 |
| developers | String | 开发商 |
| created | datetime | 创建时间 |
| updated | datetime | 更新时间 |
```

画面 12:
```jsx
e.preventDefault();
console.log(this.state.fileList);
form.validateFieldsAndScroll((err, values) => {
  if (err) {
    if (values.facilities) {
      values.facilities = values.facilities.join(",");
    }
    if (values.floor_1 && values.floor_2) {
      values.floor = values.floor_1 + "/" + values.floor_2;
    }
  }
  values.houseType = values.houseType_3 + "室" + values.houseType_2 + "厅" + values.houseType_4 + "阳台";
  delete values.floor_1;
  delete values.floor_2;
  delete values.houseType_1;
  delete values.houseType_2;
  delete values.houseType_3;
  delete values.houseType_4;
  delete values.houseType_5;
  dispatch({
    type: 'form/submitRegularForm',
    payload: values,
  });
});
```

画面 13:
```jsx
values.houseType = values.houseType_3 + "室" + values.houseType_2 + "厅" + values.houseType_4 + "阳台";
delete values.floor_1;
delete values.floor_2;
delete values.houseType_1;
delete values.houseType_2;
delete values.houseType_3;
delete values.houseType_4;
delete values.houseType_5;
```

画面 14

