# 08.更新房源数据的与服务端交互的实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\08.更新房源数据的与服务端交互的实现【海量资源尽在 ubkz.com】.mp4
- 时长 9分46秒（音频 586s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就来实现与服务端的这种交互啊那我们来看一下这个点击这个提交这个按钮就在下面这个位置有一个确定当我们点击这个确定的时候啊那么我们来看以他的逻辑是什么样的逻辑那么当我们点击这个确定那我们可以看到是不是就unok这个函数调用的是hander c5啊这个方法那么在这个方法中呢我们首先肯定是需要
[00:27] 对我们这个form表单就下面我们这个form表单是不是去做一个校验做一个校验然后呢如果没有这个错误就是全部通过的话那我们执行下面这个逻辑我们来看一下在这个里面呢首先去判断一下这个图片是不是大于0如果是大于0的当然这个PICS是一个set集合所以拿的是它的一个set的一个属性
[00:52] 大于0如果大于0的话对它去做一个这样的处理OK然后呢这个一定要注意那么这个呢是不是我们就是我们的房源的ID因为我们在底层去做数据更新的时候我们要根据ID是不是作为我们更新条件去做更新这条数据所以这个ID一定要有别把这个丢了然后呢我们调用什么dispatch就调用我们的这个服务对吧就更新了这个服务
[01:19] 有一个update这个服务当然了我们现在还没有那么我们一会儿来把它写一下然后呢我们这个payload那就是我们的一些这个数据那我们拿到上面这个values这个数据然后呢当我们调用完成之后呢在下面这个位置我们做一个这个定时器在500毫秒之后呢我们去做两件事情第一件事情呢就是把这个弹出框给它cancel掉就是给它关闭掉那么第二件事情呢就是我们去调用
[01:49] 这个pubst reload那么这个reload的方法是哪来的呢其实我们来点一下它你发现这个里面其实并没有这个reload的这个方法而这个reload在哪里呢其实是在我们外面的这个里面它要定义一个reload的这个方法定义一个它那么定义它的一个意义是什么呢就是当我们去关闭这个窗口的时候是不是需要去重新去加载我们这个外面的一个房源的一个列表
[02:16] 这样的一个效果那么这个reload怎么样传递过去呢我们是不是需要给他传递一下ok那么是不是就需要在上面在上面这个位置是不是给他做一个传递对不对那么在这呢我们就需要给他去设置一个什么呢reload啊reload等于什么呢等于是不是race.race.reload然后reload的点什么呢点bondbond什么的race去把这个指向改变掉
[02:44] 那么这样的话我们就把这个函数是不是给他传递过去了然后在我们的这个editor这个里面是不是就可以直接去通过propstool去调用我们的这个reload的这个方法OK好那么这些逻辑的我们都已经搞明白了那么接下来我们来看一下这个就是我们数据的一个分发这一块那么这个怎么玩我们来看一下那么就需要我们在提交逻辑我们来看一下在这个位置就是我们这个
[03:13] 在这个下面有一个models下面有一个form那么之前呢我们是不是只有一个submit这个提交就是我们那个新增对吧那我们再给他添加一个什么呢update把它拷贝过来拷贝到这儿再新增一个这个updateupdate form这个方法然后呢在这个里面我们将调用的是update host resource而这个是哪来的呢它其实是要在Service下面是不是在定义这样的一个方法
[03:43] 可以看到是不是定义这样的方法我们找到我们这个Service就在Service下面有一个好客点解释我们来找一下serviceservice是在这里有一个好客点解释在这个下面我们再给他新增这样的一个方法是不是新增一个update这个方法把它扣过来那么要注意的是那么在这个方法中在
[04:13] 这个不能往这儿丢往下面这个位置在这儿丢就这样的一个方法update的方法那么这个方法它需要去调用我们的是不是刚刚我们所开发的那个接口就是hawk这个house resource下面的然后通过一个pool的请求去做一个请求对吧做这个请求ok那么这样的话我们是不是就基本上把这个是不是就搞定了对吧那么这个逻辑是不是就搞定了下面我们就可以来做一个测试了
[04:41] 看他是否能够去修改成功呢那么我们在我们的这个位置就是我们的这个服务这个位置那我们给他去加一个断点在哪里加呢是不是找到我们这个更新这个服务我们来看一下是在我们这个controllercontroller去哪呢找一下是在这个下面找一个Controller然后呢house resourcecontroller下面呢这个位置打一个断点我们来看一下他提交的数据是怎么样的一个数据那么我们点击这个编辑
[05:10] 那我们给他修改一个房源我们写一个1然后呢租金改成2000那个建筑面积改成80然后呢图片原有是不是有这两张图片啊我们再给他添加一张红色的一个图片啊那么这样好我们好近一点啊然后点击这个确定我们来看一下这个效果走那么点击这个确定之后呢我们来看一下他的请求有没有去提交到我们的这个服务端呢发现了并没有去
[05:39] 哎提交但是我们这个这个断点是失效的啊没有去加上一个断点那么这样我们来看一下他这个数据有没有修改掉的发现是不是也没有修改啊那来看一下有没有报错呢有没有报错有没有报错呢呃是不是有报错啊有这个报错对吧那么报的是这个update这个错误对吧那我们来找一下这个
[06:08] 错误看看哪个位置是不是我们扫了一些什么内容扫了一些这个逻辑我们来看一下那么在这个里面它将调用的house update form然后是在这个form下面有这样的一个定义是不是有这样的定义然后在我们的这个里面有这样的一个定义没有问题有这样的一个定义没有问题然后在hook这个下面再有这样的一个定义那么应该是没有问题的对吧
[06:37] 那么是不是并是不是没有编译编译完成呢好那么我刚刚呢把这个服务呢重新启动了一下就是我们这个manage web这个服务以及我们的这个API这个服务重启了一下呢我们再来测试一下发现它应该就好了我们来看一下代码是没有问题的我们再来去刷新一下看一下它这个效果那么是重新刷新一下
[07:09] 然后呢我们再点击这个编辑啊再点击这个编辑然后呢我们去设置1然后呢这个租金设置200然后呢这个改成80我们再来上传一张红色的这个图然后呢我们点击这个确定走那么可以看到断点是不是就已经来了对吧那么我们其实可以看到拿到的数据是不是就是我们的house resource它里面的数据其中它的ID呢是1那么房源的这个标题就是它
[07:35] 然后呢图片哎这么多哎OK我们就让他通过吧把这个断点拿掉我们就不去打断点了然后呢提交成功之后呢我们来看一下呃提交成功之后但是发现好像并没有修改成功啊并没有修改成功来看一下呃到底是什么情况
[07:59] 刚刚我不小心点了这个重启我就等待他重启好那么现在这个服务就重新启动起来了那我们再来看一下刚刚的我测了一下是没有问题的其实是刚刚可能是缓存的问题那我再去编辑一下改成这个2我们来看一下这个租金改成这个3000然后我们图片给他扫一张图片看一下会怎么样保留两张点击这个确定是不是就提交成功了那么你看这个数据是变成了2
[08:27] 然后呢数据库里面我们来看你刷新一下是不是这个变成了2没有问题然后呢我们点击这个编辑查看这个图吧图是不是就有两张图片了对吧原来是不是有三张图片现在是不是变成了两张哎呀OK那么我们再来编辑一下那么比如说我再来再加一张然后呢我再去把它删掉一张看怎么样啊然后呢点击这个提交然后呢我们查看这个图片变成了这张图和这张图片
[08:56] OK那么说明我们这个图片上传的这块逻辑是没有问题的OK那么这样的话呢我们其实就已经是不是实现了跟我们服务端的一个数据的一个交互OK实现了这样的一个交互通过这么几个修改对吧OK好那么到目前为止呢我们是不是就已经实现了我们的一个更新对吧更新当然了对于这个房源数据的更新呢我们只更新他们
[09:26] 这几个这个几个这个字段或者几个这个内容当然了我们把这个能够做出来那么其他的也就都一样了都一样了我们只要把整个流程能够跑通那么就都一样了OK好那么关于这个房源数据的更新的一个这个具体功能呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个房屋资源管理系统的前端编辑功能实现，包括图片上传、表单提交、后端接口调用及数据更新的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF讲义目录，当前位于“4.1.3. 修改Antd组件”章节，右侧代码为React组件中处理图片上传的逻辑，包含`handleSave`函数和`pics`状态管理。
画面2：在IntelliJ IDEA中，展示`EditResource.js`文件中`handleSave`函数的实现，其中对上传的图片数组进行拼接并调用`dispatch`更新数据。
画面3：在IntelliJ IDEA中，展示`Resource.js`文件中`reload()`函数和`componentDidMount`生命周期方法，用于触发数据获取。
画面4：展示PDF讲义中“操作”组件的代码，包含`<a onClick={...}>查看</a>`和`<EditResource record={record}/>`等元素。
画面5：展示PDF讲义中`House.js`文件的代码，包含`import { message } from 'antd';`和`effects`中的`submitHouseForm`与`updateHouseForm`函数。
画面6：在IntelliJ IDEA中，展示`haoke.js`文件中`addHouseResource`和`updateHouseResource`两个异步函数，用于发起HTTP请求。
画面7：展示前端页面“房源管理”中“编辑”弹窗，包含租金、面积、图片上传等表单字段。
画面8：在浏览器开发者工具中，展示`EditResource`组件的网络请求，包括`POST`和`PUT`请求。
画面9：在IntelliJ IDEA中，展示`haoke.js`文件中`updateHouseResource`函数的代码。
画面10：展示前端页面“房源管理”列表，包含房源编号、标题、面积、操作等字段。
画面11：在IntelliJ IDEA中，展示`HouseResourcesController.java`文件中`@PutMapping`注解的`update`方法，用于处理PUT请求。
画面12：展示前端页面“房源管理”列表，其中一条记录“222”被选中，页面顶部显示“提交成功”提示。
画面13：展示前端页面“房源管理”中“编辑”弹窗，显示两张房源图片。
画面14：展示前端页面“房源管理”列表，其中一条记录“222”被选中，页面顶部无提示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
pics: new Set()
showModal () => {
  this.setState({
    visible: true
  });
};
handleCancel () => {
  this.setState({
    visible: false,
  });
}
handleSave () => {
  const { dispatch, form, record } - this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
      return;
    }
    values.pic = [...this.state.pics].join(',');
    values.id = record.id;
    dispatch({
      type: 'house/updateHouseForm',
      payload: values,
    });
    setTimeout(() => {
      this.handleCancel();
      this.props.reload();
    }, 500);
  });
}

画面2：
handleSave () => {
  const { dispatch, form, record } - this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
      return;
    }
    values.pic = [...this.state.pics].join(',');
    values.id = record.id;
    dispatch({
      type: 'house/updateHouseForm',
      payload: values,
    });
    setTimeout(() => {
      this.handleCancel();
      this.props.reload();
    }, 500);
  });
}

画面3：
reload () {
  const { dispatch } = this.props;
  dispatch({
    type: 'rule/fetch',
  });
}
componentDidMount () { //当组件加载完成后执行加载数据
  const { dispatch } = this.props;
  dispatch({
    type: 'rule/fetch',
  });
}

画面4：
{
  title: '操作',
  render: (text, record) => (
    <Fragment>
      <a onClick={() => {}}>查看</a>
      <Divider type="vertical" />
      <EditResource record={record} reload={this.reload.bind(this)}/>
      <Divider type="vertical" />
      <a href="">删除</a>
    </Fragment>
  ),
}

画面5：
import { message } from 'antd';
import { addHouseResource, updateHouseResource } from '/services/haoke';
export default {
  namespace: 'house',
  state: {
  },
  effects: {
    submitHouseForm (payload, { call }) {
      yield call(addHouseResource, payload);
      message.success('提交成功');
    },
    updateHouseForm (payload, { call }) {
      yield call(updateHouseResource, payload);
      message.success('提交成功');
    },
  },
  reducers: {
    saveStepFormData(state, { payload }) {
      return {
        ...state,
        ...payload,
      };
    },
  },
}

画面6：
import request from '@/utils/request';

export async function addHouseResource (params) {
  return request('/haoke/house/resources', {
    method: 'POST',
    body: params
  });
}

export async function updateHouseResource (params) {
  return request('/haoke/house/resources', {
    method: 'PUT',
    body: params
  });
}

画面11：
@RequestMapping(value = "/house/resources", method = RequestMethod.PUT)
@ResponseBody
public ResponseEntity<Void> update(@RequestBody HouseResources houseResources) {
  try {
    boolean bool = this.houseResourcesService.update(houseResources);
    if (bool) {
      return ResponseEntity.ok().build();
    } else {
      return ResponseEntity.badRequest().build();
    }
  } catch (Exception e) {
    return ResponseEntity.badRequest().build();
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：PPT标题为“操作”，内容包含“查看”、“删除”等操作按钮。
画面5：PPT标题为“House.js”，内容包含“import”语句和“effects”、“reducers”等模块。
画面11：架构图显示“前端”指向“后端”，后端包含“Controller”和“Service”。
画面12：表格数据包含“房源编号”、“房源标题”、“面积”、“操作”等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

