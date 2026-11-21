# 画面线理解：14.前后端整合开发之新增房源

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\14.前后端整合开发之新增房源【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:01, 01:45, 02:22, 03:52, 04:22, 05:07, 06:43, 07:44, 08:41, 10:55, 11:42, 12:37, 13:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:48:29

1) 这一组画面整体在讲如何通过反向代理解决前端与后端服务间的跨域问题，并实现房源信息的增删改查功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示后端控制器代码，包含保存房源资源的 POST 接口和获取 "ok" 的 GET 接口。
画面2：展示前端配置文件中设置反向代理规则，将 /haoke/ 路径代理到后端服务。
画面3：展示前端页面，用户正在填写房源信息表单。
画面4：展示前端配置文件中设置本地资源路径的逻辑。
画面5：展示前端服务层代码，封装了向后端 POST 请求的函数。
画面6：展示前端 Redux store 中的 effects，用于提交表单并处理成功提示。
画面7：展示前端表单布局代码，定义了表单项的样式和数据源。
画面8：展示前端配置文件中设置 umi-plugin-ga 插件和目标环境。
画面9：展示 PDF 文档中关于反向代理配置的说明，包含配置地址和 proxy 对象。
画面10：展示 PDF 文档中关于反向代理配置的说明，包含配置地址和 proxy 对象。
画面11：展示浏览器开发者工具 Network 面板，显示 POST 请求成功返回 201。
画面12：展示 PDF 文档中关于表单字段的配置示例。
画面13：展示浏览器开发者工具 Network 面板，显示 POST 请求成功返回 201。
画面14：展示 PDF 文档中数据库查询结果，显示新插入的房源数据。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
public ResponseEntity<Void> save(@RequestBody HouseResources houseResources) {
    try {
        boolean bool = this.houseResourcesService.save(houseResources);
        if (bool) {
            return ResponseEntity.status(HttpStatus.CREATED).build();
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}

// test
@GetMapping
@ResponseBody
public ResponseEntity<String> get() {
    return ResponseEntity.ok("ok");
}
```

画面2：
```javascript
'/haoke': {
    target: 'http://127.0.0.1:18080',
    changeOrigin: true,
    pathRewrite: { '^/haoke': '' }
},
ignoreMomentLocale: true,
lessLoaderOptions: {
    javascriptEnabled: true,
    disableRedirectHoist: true,
    cssLoaderOptions: {
        modules: true,
        getLocalIdent: (context, localIdentName, localName) => {
            if (context.resourcePath.includes('node_modules') ||
                context.resourcePath.includes('ant.design.pro.less') ||
                context.resourcePath.includes('global.less')) {
                return localName;
            }
            const match = context.resourcePath.match(/src(.*)/);
            if (match && match[1]) {
                const antdProPath = match[1].replace('.less', '');
                const arr = antdProPath.split('/');
                .map(a => a.replace(/([A-Z])/g, '_$1'))
            }
        }
    }
}
```

画面4：
```javascript
const match = context.resourcePath.match(/src(.*)/);
if (match && match[1]) {
    const antdProPath = match[1].replace('.less', '');
    const arr = antdProPath.split('/');
    .map(a => a.replace(/([A-Z])/g, '_$1'))
}
```

画面5：
```javascript
import request from '@/utils/request';

export async function addHouseResource(params) {
    return request('/haoke/house/resources', {
        method: 'POST',
        body: params
    });
}
```

画面6：
```javascript
import { routerRedux } from 'dva/router';
import message from 'antd';
import addHouseResource from '@/services/haoke';

export default {
    namespace: 'house',
    state: {},
    effects: {
        *submitHouseForm({ payload }, { call }) {
            yield call(addHouseResource, payload);
            message.success('提交成功');
        },
    },
    reducers: {
        saveStepFormData(state, { payload }) {
            return {
                ...state,
            };
        },
    },
};
```

画面7：
```javascript
const submitFormLayout = {
    wrapperCol: {
        xs: { span: 24 },
        sm: { span: 10, offset: 7 }
    }
};

return (
    <PageHeaderWrapper>
        <Form onSubmit={this.handleSubmit} hideRequiredMark style={{}}>
            <Card bordered={false} title="房源名称" label="楼盘名称">
                <FormItem
                    {...formItemLayout}
                    label="楼盘名称"
                    dataSource={this.state.estateDataSource}
                    placeholder="搜索楼盘"
                    onSelect={(value, option) => {
                        // ...
                    }}
                >
                    {/* ... */}
                </FormItem>
            </Card>
        </Form>
    </PageHeaderWrapper>
);
```

画面8：
```javascript
default: 'zh-CN', // default zh-CN
baseNavigator: true, // default true, when it is true, will use navigator
dynamicImport: {
    loadingComponent: './components/PageLoading/index',
},
{
    dll: {
        include: ['dva', 'dva/router', 'dva/saga', 'dva/fetch'],
        exclude: [['Babel/runtime']],
        hardSource: true,
    }
},
'umi-plugin-ga',
code: 'UA-72788897-6',
judge: () => process.env.APP_TYPE === 'site',
targets: {
    ie: 11,
}
```

画面9：
```javascript
proxy: {
    '/haoke': {
        target: 'http://127.0.0.1:18080',
        changeOrigin: true,
        pathRewrite: { '^/haoke': '' }
    },
}
```

画面12：
```html
<FormItem {...formItemLayout} label="房源标题">
    {getFieldDecorator('title', {
        rules: [{ required: true, message: '此为必填项' }],
        initialValue: '',
    })(
        <Input style={{ width: '100%' }} />
    )}
</FormItem>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面9：PPT 标题为“6.5、通过反向代理解决跨域问题”，表格数据为：
- 配置地址：https://umijs.org/zh/config#proxy
- proxy 对象：
  - '/haoke': { target: 'http://127.0.0.1:18080', changeOrigin: true, pathRewrite: { '^/haoke': '' } }

画面12：PPT 标题为“6.2、增加model”，表格数据为：
- 表单字段：房源标题
- 默认值：东方曼哈顿 3室2厅 16000元

5) 无
