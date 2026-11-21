# 07.更新房源的交互页面实现讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\07.更新房源的交互页面实现讲解【海量资源尽在 ubkz.com】.mp4
- 时长 15分23秒（音频 924s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们就来实现这个修改房源的这个前端的一个页面啊那我们来看一下页面的是在这个位置有在这个下面的是不是有一个房源管理啊我们点击房源管理呢,会查询房源的个列表然后呢,在后面这个操作这个位置啊我们可以看到原来是不是只有这个查看和删除这两个操作,对吧所以呢,我们需要在这个位置给它添加一个
[00:27] 修改或者说编辑OK那么我们来看这个应该怎么去做那我们可以简单的分析一下就是我们在这个位置想要去添加一个修改其实我们是要把这个修改这个逻辑是不是作为一个组件去做一个这样的一个实现所以我们需要去单独去写一个这个修改的一个组件然后把它导入进来就可以了所以接下来我们需要在我们这个代码这个位置
[00:55] 在我们这个house这个目录下面然后我们创建一个文件创建一个文件我们来创建一个editor的一个页面我们来找一下这个讲义在讲义中是不是有一个edit resource这个js那么咱们把这个文件创建出来把它丢到这个里面来然后有个editor resource然后js然后我们可以看到
[01:19] 在这个里面呢我们需要去写一个React组件啊怎么写呢还记得吗是不是写一个import然后导入一个re什么呢actor然后呢from所以呢是不是reactor啊reactor然后呢导入之后呢下面我们是不是写一个classclass然后呢我们写一个editorresource然后呢是不是要继承reactor.component然后呢我们下面是会把它导出export
[01:49] 导出一个defaultdefault然后呢再写一个editoreditorresource好那么然后呢在这个里面我们是不是要去写一个render方法做一个渲染OK那么这个里面我们是不是returnreturn一个什么内容呢其实我们是不是return的就需要去显示的是一个编辑编辑这样的一个链接对吧那么这个呢我们就参考我们的讲义
[02:18] 我们来去一点一点去写一下这个页面啊然后呢我们可以看到在这个位置呢我们写一个这个A标签是不是就是我们这个页面对吧写这个编辑这个按钮然后呢这个位置呢有一个这个方法有一个这个售这个方法那么这样我们先把这个方法呢我们先定义出来先定义出来
[02:39] 秀在这儿然后我们先做一个定义然后内容我们一会儿再说那么我们把它定义到是在我们的下面对吧类这个里面来然后这个里面的内容先给它注释掉我们先定义这样的一个空的方法OK先保证它编译不报错然后我们是不是有了这个JS之后我们就可以在我们的房源列表页面中是不是引入我们这个JS对吧OK那么在我们找到下面的一个位置
[03:08] 找到那个操作的位置我们找一下这个操作的位置然后操作是在下面找一下然后resource我找一下看一下是在是在这个位置你看在这个位置是不是有个查看对吧然后呢我们跟着这个查看的下面我们给它添加一个什么呢首先我们加一个这个分割符就是我们看到了这样的一个分割符
[03:38] 然后呢在这个里面呢我们去引入我们的editorresource引入这个组件那么引入这个组件之后呢它是不是就会出现这样的效果可以看到在这个位置爆错啊为什么会爆错呢那么我们来看一下那么在这个里面呢它是缺少可以看到这个有一个错误啊这个错误呢是我们刚刚写这个一道问题这个不是大括号啊这个是小括号啊
[04:09] OK把这个小括号拿过来得到账好那么我们来看一下这个效果刷新一下那么我们可以看到在这个位置它是不是就已经引入了这个编辑对吧编辑这个按钮OK那我们点击这个编辑是不是就应该去触发一个事件对吧触发一个事件然后呢去做一些这个编辑的一些功能对吧OK那么接下来我们是不是重点
[04:35] 就需要是在我们的这个editor这个JS里面去做一些功能的一些这个完善哎OK好那么我们接着来看一下这个里面的功能怎么去做啊怎么去做那么当我们去点击这个编辑的时候我们是不是希望他啊注意当我们点击这个编辑的时候我们希望他什么呢是不是应该在这个位置给我们弹出一个页面对吧在这个页面中呢再有一些这个内容让我们去做一个输入让我们做一个输入然后呢我们去点击这个提交的一个按钮
[05:05] 去做一个这个提交提交之后呢然后呢把这个窗口是不是给他关掉然后呢把数据是不是提交到我们的后端服务端对吧提交我们的服务端然后呢这个窗口关掉提交到服务端哎呀OK那么这样然后呢还需要的是当这个当这个窗口关掉之后呢我们这个表格就这个列表页面是不是还需要做一个重新刷新哎呀OK那么大致需要做以下的一些这个功能
[05:33] 那么我们来看一下这个应该怎么去做我们还是参考我们的这个讲义中的这个实现我们来一点一点来去写一下它的一个功能那么下面我们给它定义一个这个model就是我们的一个弹出框弹出框咱们来给它定义一下把这个拷贝一下拷贝一下出来这样为了拷贝方便到我们那个资料中在我们这个资料里面找一下在这个资料里面我们找到
[06:01] 找到它下面有这样的个解写文件那么我们来看一下我们参考这个解写文件的一些内容去做一些这个修改然后我们来看一下在这个里面呢我们把它拿过来这个就是什么呢一个弹出框弹出框那把它拿过来当然了我们把这个整个拿过来因为在React的组件中它是不是只能有一个节点对吧哎呀ok所以呢我们把它丢过来然后呢它需要有一些这个标签的引入
[06:29] 那么引入呢我们把上面这个代码也贴过来那么从这到这一直都贴过来咱们到这吧一直都把它贴过来OK好那么贴到这里这样的话呢我们相关的一些这个组件的引用是不是都已经就导入进来了对吧但是呢我们可以看到在这个位置呢我们设置了这个就是我们这个弹出框
[06:52] 它的一个可显示的状态是一个需要从通过我们states中的一个状态去拿到它的一个显示状态那么显然是不是应该默认是什么默认是false不显示对不对应该当我们点击编辑的时候我们让这个状态是不是显示出来设置为chew它是不是做一个显示就可以了所以我们需要做两件事情第一件事情就是需要给它一个初始值第二件事情我们就需要去通过这个方法去修改它的一个
[07:20] 这个显示对吧OK好那么我们来看一下它的一个初始值的一个设置那么咱们把它拷过来然后拷贝到这个位置来放大帐那么通过我们的构造方法去做一个初始化然后我们初始值是不是就是一个False对吧FalseOK然后当我们点击当我们去点击这个编辑的时候我们希望它去帮我们去做一个显示做一个显示OK好那么
[07:50] 我们还需要去做一些这个处理因为有些这个函数还没有他可能会报错所以我们把一些函数也抠过来把这个函数我们抠过来一会我们来讲一下讲一下这个函数OK那么把它丢到下面来好那么我们来看一下它的一个效果那么当然了我们可以看到在这个页面中它可能会有一个编译的错误来看一下什么编译的错误呢
[08:25] 这个我们还是去查看一下查看一下它的控制台的输出看一下有什么错误吗OK那么可以看到在这个位置呢其实我们刚才就看到了它是缺少一个这个方法对吧这个方法是不是我们在前面是不是说过这个是关于Foam的一个方法原因是呢我们没有给它去添加一个这两个啊这两个这个修饰器修饰服然后呢把它丢过来丢到这儿
[08:56] 那么只有去通过这个form create之后是不是才有这个包装的一个方法才能把我们这个form这个元素是不是做一个包装OK好那么我们来看一下这个应该应该是OK应该是OK当然了这个里面应该好像还缺点东西吧缺点东西那么缺什么呢我们来看一下这个里面的还缺的是在下面这个位置是在这
[09:26] 在这个run的这个里面我们需要去做一件事情就是需要做什么事情这样的把它丢过来那么这个是什么意思就是首先我们来看一下这个方法下面这个方法需要通过我们的publess中去拿到这个方法因为当我们通过这个form.create之后它就会再把这个方法是不给我们去绑定到这个publess中所以我们需要去通过它去拿到这个方法
[09:56] 这是第一个第二个呢就是大家可以想一下那么在我们点击这个编辑的时候那么我需要它显示的是不是什么呢显示的是不是就是当前这一行数据啊所以我需要把这个recall的这个数据是不是再拿过来那么这个recall的这个数据怎么怎么去拿呢是不是就应该在我们引用的这个位置对吧在引用这个位置我们recall的等于什么呢等于是不是我们上面这个recall的就是你编辑的这个数据对吧编辑这个数据
[10:25] 然后呢他传递过去那么就可以在这个位置是不是拿到这个数据然后呢做一个数据的一个回显OK那我们再来刷新一下看一下有没有问题了那么基本上应该没什么问题了点击这个编辑我们来看一下效果走那么点击这个编辑呢我们会发现在这个页面中呢是不是已经有一些数据是不是已经做了回显对吧OK点击这个取消点击它那么数据是不是说不一样的对吧那么来看一下这个房源的标题呢是
[10:52] 最新修改的房源我们点击这个编辑看一下效果是不是最新修改的房源OK然后呢下面的像这个康城精品房二房源二那么点击编辑那么对的就是这个这个标题的数据编辑图片是不是也做了一些回显OK那么我们基本上可以看到刚刚我们所写的这个JS文件是不是基本上我们已经就把这个数据是不是回显出来了
[11:17] 当然了我们现在回遣的数据呢只有这么几个啊那么我只是去拿了几其中的几个数据做一些回遣做一些这个修改其他的呢我们先保持默认啊先不做这个修改OK好那么到这里呢我们基本上呢就把这个交互是不是就做完了对吧把交互就做完了那么在这个里面呢还有一些这个小这个细节啊我们简单的来说一下啊那么这个细节是在哪里呢首先第一个呢是这个图片啊这个图片
[11:46] 那么这个图片的之前的我们是在新增房源这个位置在新增房源这个位置呢是不是有这样的一个效果点击它是不是做一个图片的上传OK这样的一个效果但是呢我们在修改房源的这个位置呢其实是我们需要对我们的一个已有的一个图片是不是做一个回显啊那么这个回显怎么做呢我们来看一下那么回显的话呢我们需要去调用我们这个图片上传这个组件的时候呢传递一个属性给它叫fail list
[12:15] 把这个传递给他然后呢我们把VCode的PIC给他然后呢我们去找到我们这个图片上传组件在这个里面呢我们对他去做一些这个处理怎么处理呢就是我们需要给他去设置一个fail list然后呢去对我们传入的一个这个fail list做一个分割然后呢去拿到他的这样的一个对象OK然后呢我们在下面的这个去设置一个上传组件的时候呢我们给他去设置一个fail list
[12:43] OK那么这样的话呢它就可以实现一个图片的一个回显那么当我们点击这个上传完成之后呢它是不是有一个叫做hand field list的一个处理那么又回到我们的editor这个里面hand field list中那么就需要去处理我们新上传的图片跟我们原有图片的一个处理那么在这个里面呢我们设置它是一个set集合
[13:09] 去做一个去重的一个操作哎呀OK那么当然了对于在我们初始化的时候也要设置它的PICS呢也是一个new一个set就是一个初始的一个空的一个set哎呀OK好那么最后在我们做一些按钮操作的时候比如说我们点击这个取消的时候点击取消的时候呢我们就需要把这个窗口是不是给它关闭掉哎呀OK那么点击这个取消我们来看一下啊点击这个取消
[13:36] on这个console是不是就调用this.handleconsole那么就可以做一个关闭这关闭就可以了那么在这个里面还有一个小的细节点需要大家注意的就是在这个位置在这个位置那么在这个位置我们需要设置我们的弹出框当我们的窗口在做一个关闭的时候需要把我们这个组件什么destruct就是做一个销毁把它销毁掉
[14:02] 那么为什么要做销毁呢原因是如果你不做销毁的话那么他就有可能去记录了你上一次所修改的这个数据那么就不能够保证每一次点击都是你这一行的这个数据哎呀ok那么这个点一定要注意所以一定要把它设置为true那么他的默认的是false哎呀ok那么到这里呢我们可以看到这个页面中的一些基本的显示逻辑呢哎呀ok那么就这么多那么我们接下来我们要做的事情呢就是需要
[14:32] 当我们点击这个修改之后啊那么我们就需要点击这个确定点击确定那么我们把数据需要提交到我们的一个服务端让他去做一个数据的一个修改哎呀OK好那么关于我们的一个这个交互呢我们在下面的一个视频呢来做一个讲解OK那么关于这个页面中的一些这个一些交互的一些逻辑包括一些页面的一些编写呢我们基本就讲到这里因为时间的关系呢我们不可能一行一行代码去挑这个
[15:00] 这个实现也希望大家都去逐行的去阅读一下这个代码然后去看一下每一个代码为什么这样去写需要去思考一下OK那么也建议大家可以是你从零开始去构建这样的一个页面然后去一点一点去实现里面的一些功能OK好那么关于这个功能的一些交互我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 React 项目中实现房源信息的编辑功能，包括前端界面、状态管理、表单验证和图片上传处理。

2) 按时间顺序列出每张画面的要点：
画面1：展示房源管理页面，包含房源列表和编辑、删除操作按钮。
画面2：在 IntelliJ IDEA 中打开 EditResource.js 文件，正在编写组件的 render 方法。
画面3：在 Resource.js 文件中，定义了 handleFormReset 函数，用于重置表单状态并触发数据获取。
画面4：在 Resource.js 文件中，定义了列的渲染函数，包括“面积”、“楼层”和“操作”列。
画面5：在 Adobe Reader 中查看 PDF 文档，内容涉及 React 表单和装饰器的使用。
画面6：在 EditResource.js 文件中，编写了 showModal 函数和 Modal 组件的结构。
画面7：在 EditResource.js 文件中，定义了组件的 state 和 showModal 函数。
画面8：在浏览器开发者工具中，显示了 ReferenceError: getFieldDecorator is not defined 的错误信息。
画面9：在 EditResource.js 文件中，定义了 FormItem 组件的属性，包括 label 和 rules。
画面10：在浏览器中，显示了房源编辑弹窗，包含房源标题、租金、建筑面积和图片上传区域。
画面11：在 EditResource.js 文件中，编写了 handleFileList 函数，用于处理上传的图片。
画面12：在 PicturesWall.js 文件中，定义了 handleCancel、handlePreview 和 handleChange 函数。
画面13：在 EditResource.js 文件中，编写了 handleSave 函数，用于保存表单数据。
画面14：在 Adobe Reader 中查看 PDF 文档，内容涉及 EditResource.js 文件中的 state 和函数定义。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```javascript
import React from 'React';
class EditResource extends React.Component{
  render() {
    return (
      <div>
        <a onClick={() => this.props.reload()}>刷新</a>
      </div>
    );
  }
}
```

画面3：
```javascript
type: 'rule/fetch',
payload: params,
});
handleFormReset () => {
  const { form, dispatch } = this.props;
  form.resetFields();
  this.setState({
    formValues: {},
  });
  dispatch({
    type: 'rule/fetch',
    payload: [],
  });
};
```

画面4：
```javascript
title: '面积',
dataIndex: 'useArea',
render: (text, record, index) => {
  return text + "平方"
},
title: '楼层',
dataIndex: 'floor'
,
title: '操作',
render: (text, record) => (
  <Fragment>
    <a onClick={() => {}}>查看</a>
    <Divider type="vertical" />
    <a href="">删除</a>
  </Fragment>
);
```

画面5：
```javascript
<React.Fragment>
  <a onClick={() => { this.showModal() }}>编辑</a>
  <Modal
    title="编辑"
    width={640}
    visible={this.state.visible}
    onOk={() => this.handleSave()}
    onCancel={() => this.handleCancel()}
    destroyOnClose={true}
  >
    <div style={{ overflowY: 'auto' }}>
      <Form hideRequiredMark style={{ marginTop: 8 }}>
        <FormItem {...formItemLayout} label="房源标题">
          {getFieldDecorator('title', {
            initialValue: record.title,
            rules: [{
              required: true,
              message: '房源标题为必填项'
            }]
          })(<Input style={{ width: '100%' }} />)}
        </FormItem>
        <FormItem {...formItemLayout} label="租金">
          {getFieldDecorator('rent', {
            initialValue: record.rent,
            rules: [{
              required: true,
              message: '租金为必填项'
            }]
          })(<InputNumber style={{ width: '100%' }} />)}
        </FormItem>
      </Form>
    </div>
  </Modal>
</React.Fragment>
```

画面6：
```javascript
import React from 'React';
class EditResource extends React.Component{
  showModal = () => {
    this.setState({
      visible: true
    });
  };
  render() {
    return (
      <React.Fragment>
        <a onClick={() => this.showModal()}>编辑</a>
        <Modal
          title="编辑"
          width={640}
          visible={this.state.visible}
          onOk={() => this.handleSave()}
          onCancel={() => this.handleCancel()}
          destroyOnClose={true}
        >
          <div style={{ overflowY: 'auto' }}>
```

画面7：
```javascript
super(props);
this.state = {
  visible: false,
  pics: new Set()
};
showModal = () => {
  this.setState({
    visible: true
  });
};
render() {
  return (
    <React.Fragment>
      <a onClick={() => this.showModal()}>编辑</a>
      <Modal
        title="编辑"
        width={640}
        visible={this.state.visible}
        onOk={() => this.handleSave()}
        onCancel={() => this.handleCancel()}
        destroyOnClose={true}
      >
        <div style={{ overflowY: 'auto' }}>
```

画面8：
```javascript
ReferenceError: getFieldDecorator is not defined
```

画面9：
```javascript
<FormItem {...formItemLayout} label="房源标题">
  {getFieldDecorator('title', {
    initialValue: record.title,
    rules: [{
      required: true,
      message: '房源标题为必填项'
    }]
  })(<Input style={{ width: '100%' }} />)}
</FormItem>
<FormItem {...formItemLayout} label="租金">
  {getFieldDecorator('rent', {
    initialValue: record.rent,
    rules: [{
      required: true,
      message: '租金为必填项'
    }]
  })(<InputNumber style={{ width: '100%' }} />)}
</FormItem>
```

画面10：
```html
房源标题：最新修改房源
租金：1000 元/月
建筑面积：100 平米
上传室内图：
[图片预览]
[上传按钮]
```

画面11：
```javascript
handleFileList = (obj) => {
  let pics = new Set();
  obj.forEach((v, k) => {
    if (v.response) {
      pics.add(v.response.name);
    }
    if (v.url) {
      pics.add(v.url);
    }
  });
  this.setState({
    pics: pics
  });
};
```

画面12：
```javascript
this.state = {
  previewVisible: false,
  previewImage: '',
  fileList: filelist
};
handleCancel = (file) => {
  this.setState({
    previewImage: file.url || file.thumbUrl,
    previewVisible: true,
  });
};
handleChange = (fileList) => {
```

画面13：
```javascript
handleSave = () => {
  const { dispatch, form, record } = this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
      if (this.state.pics.size > 0) {
        values.pic = [...this.state.pics].join(',');
      }
      values.id = record.id;
      dispatch({
        type: 'house/updateHouseForm',
        payload: values,
      });
      setTimeout(() => {
        this.handleCancel();
      }, 500);
    }
  });
};
```

画面14：
```javascript
pics: new Set()
showModal = () => {
  this.setState({
    visible: true
  });
};
handleCancel = () => {
  this.setState({
    visible: false,
  });
};
handleSave = () => {
  const { dispatch, form, record } = this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：
PPT标题：React 表单和装饰器的使用
表格数据：
- 2.1. 表单中传递参数
- 2.2. 设置参数
- 2.3. 设置默认值
- 2.4. 测试
- 3. 公共类装饰器
- 3.1. 修饰器的使用
- 3.2. 修饰器的使用
- 3.3. 测试
- 4. 实现数据存储
- 4.1. 新增接口（REST）
- 4.2. 修改接口
- 4.3. 删除接口
- 4.4. 修改接口
- 4.5. 修改接口
- 5. 为接口添加请求方法
- 5.1. 使用 Decorator
- 5.2. 使用 Axios
- 5.3. 使用 Axios
- 5.4. 导入数据
- 5.5. 导入数据

画面14：
PPT标题：EditResource.js 文件中的 state 和函数定义
表格数据：
- 1. state: { visible: false, pics: new Set() }
- 2. showModal = () => { this.setState({ visible: true }) }
- 3. handleCancel = () => { this.setState({ visible: false }) }
- 4

