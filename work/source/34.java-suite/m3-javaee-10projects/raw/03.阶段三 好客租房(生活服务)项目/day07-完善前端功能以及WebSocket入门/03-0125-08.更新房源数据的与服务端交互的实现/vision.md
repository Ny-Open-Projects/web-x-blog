# 画面线理解：08.更新房源数据的与服务端交互的实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\08.更新房源数据的与服务端交互的实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:38, 02:13, 03:03, 03:43, 04:31, 05:11, 05:55, 06:39, 07:10, 07:47, 08:25, 08:58, 09:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:23:13

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
