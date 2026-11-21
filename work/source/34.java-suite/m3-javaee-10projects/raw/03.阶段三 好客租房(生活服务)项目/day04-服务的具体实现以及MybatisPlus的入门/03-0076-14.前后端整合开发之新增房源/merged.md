# 14.前后端整合开发之新增房源

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\14.前后端整合开发之新增房源【海量资源尽在 ubkz.com】.mp4
- 时长 13分43秒（音频 824s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来整合我们的前端系统做一个新增房源的这个开发那么我们先来打开我们这个工程然后我在这个位置呢去open一个工程就是我们之前写的这个manage web这个工程然后呢我们去在一个新窗口把它打开好,这个就是前面我们所讲的这个工程那么这个工程呢我就不去重新去做这样的一个
[00:29] 创建讲解了那么我们在这个基础之上去做一个讲解主要是做一个讲解那么来看一下首先第一个内容就是我们增加一个房源的标题这个是什么意思就是我们这样吧先把这个工程我们先启动起来我们来说一下那么我们需要启动一个命令通过一个命令来启动叫t什么样对吧startartstart来启动
[01:00] 那么等待它的一个启动那这样我先把这个视频呢先启动先暂停一下等待它这个启动好那么现在呢我们这个服务呢就已经跑起来了哎OK那么接下来呢我们来看一下这个新增房源的这个页面啊在这个页面中呢我们在这儿有一个叫房源的标题那么其实我们之前的是没有这一项的啊
[01:25] 没有这个项那么我们去整这个页面的时候当时把这个房源的标题这一项给漏掉了所以呢我们现在再把它补回来那么它的代码呢就在这啊那么回头也会把代码发给大家啊所以呢也可以从代码中也可以找到它啊效果呢其实这样的一个效果OK然后呢我们想要去实现的效果呢是点击这个提交的时候是不是去把这个数据提交到我们刚刚所写的rest4的这个接口就是这个接口下面对吧
[01:54] 这个结果下面那么应该怎么去做啊咱们就一点一点的来看一下啊那么怎么去做呢那么首先第一个呢是我们需要添加一个这个model添加一个model这个model在哪里呢我们来找一下model呢是在我们的这个找到我们的一个这个host啊host下面呢就是hook下面有个host下面然后呢有一个这个models之前是没有这个models的然后呢我们拷贝一个拷贝
[02:22] 拷贝原来的什么呢原来它有一个叫做form原来有一个form拷贝这个下面的一个modus拷贝它把它拷贝过来我们做一些这个改造那么这个里面呢我们写了一些什么内容呢我们来看一下那么我们在这个里面其实我们定义了一个方法是不是submit这个host这样的一个form这样的一个方法然后呢我们去调用这个通过一个这个调用我们这个方法吧这个方法是在
[02:51] 这个里面对吧稍微的有一个好客那么也就是说我们需要在Service下面再来定义我们的一个好客找到一个Service下面有一个好客这个点解释然后在这个里面我们去定义这样的一个方法当然了这个里面他又会去引入这个requestrequest就是一个通用的一个请求的一个工具包对吧然后我们通过他是不是去请求请求我们的地址ok
[03:20] 在这儿有同学会发现这个地址好像跟我们刚刚所请求这个地址是不一样的一会儿我们再说这个问题那我们先来继续梳理刚刚的一个内容那我们是不是写了一站那个model对吧引用了我们的一个Service那么当我们提交成功之后我们就提醒提醒怎么的提醒我们的用户就是说提交成功了OK这样的一个实现那我们就回到这个Service中我们来看一下Service中的一个实现
[03:48] 那么在Service里面hawk中呢是不是就去做一个请求然后呢发起是一个pose请求ok好就是这样的一个逻辑至于这个url为什么是这样我们一会儿再解释好那么我们回到我们这个我们那个新增啊新增房源的这个页面中在这个页面中呢我们要注意的一点是那么我们提交的请求是不是在这对吧提交啊提交请求在这那么我们所要调用的是不是就是我们这个
[04:18] house下面的submit的方法那么是吧找到下面的一个name space命名空间是house下面的一个submit的方法是不是找到他做一个提交然后他把这个数据他把这个数据是不是就能够提交到我们这个方法中对吧values做一个数据的提交ok那么在这个里面他是不是已经收集到数据了对吧收集到数据然后提交到这个方法中
[04:46] 那么在这个里面我们做了几个操作需要大家注意一下第一个就是楼盘ID以前是没有做一个添加的我们现在给它添加一个楼盘的ID还有一个就是刚刚我们所提到的楼房源的标题Title标题OK好那么这样的话我们新增房源的JS基本就搞定了对吧前端就搞定了那么我们是不是调用它
[05:14] 就是去把数据传递过去了但是大家想一想我们调用他是不是把数据传到这个里面来然后他呢又去调用这个Service中的一个这个方法Service方法在到好客这个下面然后呢请求这个地址那么如果我在这个位置把这个地址拷过来大家想一想啊我假设啊拷到这里大家想一想他能不能提交他同样是不是也是需要上这个地址去post提交我们的数据啊但是大家想一想那么我们现在这个
[05:44] 这个地址它所在的是不是就是log house下面的8000这个端口而我们所要提交的是18080这个端口那么显然呢这不是在同一个域下面是不是那么它一定会有一个什么呢跨域问题一定会有跨域问题这个大家也能够理解吧那么跨域问题呢我在这呢就不展开了啊我相信大家呢在学这个课程既然你现在学这个课程那么应该是
[06:10] 对这个跨域问题应该是比较熟悉也比较了解的那么它一定存在是跨域问题那么这个跨域问题怎么解决呢OK那么在这个pro系统就是我们安德迪尔这样的一个pro系统中呢它呢有一个解决方案是这样一个解决方案就是通过一个代理去做一个解决就是反向代理做一个解决那么怎么样去定义这个反向代理呢我先把这个代码呢先返回啊
[06:38] 那么我们需要在config下面去定义一个代理去哪了在下面在63行的这个位置我们定义一个代理这个代理的意思就是说我们定义一个以后客请求为开头的这样的一个代理如果我们的请求是以后客开头的请求我们就会直接指向到他的目标到这个里面来
[07:07] 并且呢我们去真正做请求的时候是不是就是我们18080这个请求啊真正做请求的时候啊那么我们就需要把它前面这个浩克的这个请求就给他去掉啊这个什么意思呢来看一下我们的讲义啊那么我们通过这个6.5这个内容啊来看一下那我们添加一个这个代理添加个代理然后呢我们请求的是localhost下面的浩克和host下面的resource就是我们刚刚
[07:37] 所看到的这个我们的这个serviceservice下面写的这个地址是不是这个地址那么他请求这个地址那么就会被我们这个代理做一个拦截那么他实际真正请求的就变成什么呢就是这个地址注意啊就是这个地址然后呢后面加一个你请求的这个地址请求后面这个地址然后把前面的号客给你什么的给你替换掉替换成一个空看到了吗
[08:06] 替换成空实际请求地址变成这样那么这个实际请求这个地址是不是就是我们真正的这个接口的一个地址啊OK就这样的地址啊好那么现在呢我们在那请求呢就可以搞定了对吧OK当然了更多的一些这个配置呢大家可以去参考这个5米下面的一个这个代理啊这个里面也有一些这个讲解啊OK好那么这个我们就不详细去展开了好嘞
[08:35] 那么接下来呢我们就来做一个测试看他是否能够去把数据提交到我们的后台啊那我们来搜一下这样我们为了测试呢我们这样咱们把这个控制台呢打开来看一下他的一个请求啊好然后呢我们在这个地方搜一下上海比如说康城然后呢标呃房源的标题呢就啊康城啊康城这个
[09:04] 这个不能叫现房了那就有个三室三室三室两厅三室两厅的一个一位一位这样的一个这样的我们的一个房源那么他的楼栋是几栋呢就是一栋二单元三号然后呢租金呢是2000然后呢这个支付的方式呢我们选择负三加一然后呢
[09:37] 三室两厅三室两厅然后呢一卫一卫一厨一阳台建筑面积呢是100平方然后呢使用面积呢是80平方然后呢楼层呢是第两层总共呢是20层然后呢我们随便勾打内容啊就随便写了房间的描述呢就写一个拎包入住拎包入住啊然后呢图片呢我们先不做上传
[10:05] 后面呢我们会专门去有一节呢去讲这个图片的上传联系人呢张三然后呢手机号18888啊写这么多吧好嘞那么物业费呢是一块五一个月然后呢我们看房时间呢是全天都可以点击这个提交啊重点我们来看这个提交的一些这个信息啊走那么可以看到是不是已经提交成功了对吧那么我们可以看一下他的请求注意那么他的请求地址注意是什么呢本机的一个
[10:35] 8000这个端口是不是还在这个下面那么提交的请求是不是浩克这个下面那么这个地址是不是就会被我们刚刚所讲的这个呃代理是不是做一个拦截找到config下面是不是有个代理做拦截那么他就会真正请求到的是我们18080这个1270.0.118080这个下面的这个什么的house下面的resource然后呢并且他是一个什么呢post的请求
[11:02] 然后呢我们可以看到响应的状态码是不是201201代表的数据是不是创建成功了那么下面的这个呢就是我们请求的一个数据json数据那么ok那么json数据跟我们刚才所看到数据其实是一样的啊好那么我们来看一下数据库关键的看一下数据库了有没有数据的提交过来呢哎ok你发现数据是不是已经就提交到我们的这个数据库了对吧好那么到这里呢我们是不是就已经完成了前端跟我们后端的一个
[11:32] 整合对吧好那我们把这个内容呢再来过一下那么刚刚我们讲的第一个内容呢是增加了这个房源的这个标题的这个数据这个内容好那么这个就也没什么好说的好那么刚刚添加到这个效果就可以了那么我们添加了一个这个model在model中呢我们需要去注意这么几个内容那么我们在这个位置引入了一个Service中的一个方法是我们Hawk这个里面的一个andhouse results这样的一个方法
[12:01] 那么我们就可以去去执行它执行成功之后就去提醒提醒我们说提交成功了ok然后我们去增加一个Service在我们的Service目录下面去增加一个浩克.js的这样的一个文件然后在这个里面我们去定义一个这样的一个方法定义这样的一个方法然后我们去做这样的一个请求调用我们request去做这样的一个请求这个请求注意
[12:30] 他并不是我们真正的去做一个并不是我们真正的我们的这个实际的一个地址而是呢需要做一个代理做一个处理为什么需要做这样的处理呢其实我们后面也会讲到就是说我们因为有一个跨越的一个问题所以我们做需要做这样的一个处理然后呢我们那个表单提交地址要改成我们自己的这个地址做一个提交那么我们刚刚是不是讲过通过这个
[12:56] 反向代理的方式解决了跨域的问题就是我们前端系统的和我们后端系统端口是不同的会导致跨域的问题对吧那我可以通过这个UMI所提供的一个反向代理功能然后呢去做一个解决哎呀OK好那么这个我们刚刚是不是就讲过了通过我们的一个测试那么其实会发现我们的一个数据是不是就已经提交成功了对吧OK在我们的数据库里面是不是也有这样的一个数据了OK那么可以看到
[13:24] 那么整个流程是不是就已经跑通了那么现在我们虽然说只跑通了一个流程那么我相信其他的流程就非常的相像了那么开发起来就非常的快速了对不对好那么关于前后端的整合的开发开发这个新增房源的功能呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

