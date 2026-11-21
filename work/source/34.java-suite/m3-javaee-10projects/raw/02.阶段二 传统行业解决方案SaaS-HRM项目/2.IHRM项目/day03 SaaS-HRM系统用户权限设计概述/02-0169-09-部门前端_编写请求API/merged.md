# 09-部门前端：编写请求API

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\09-部门前端：编写请求API_【海量资源尽在 ubkz.com】.mp4
- 时长 7分6秒（音频 426s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 模块构造成功之后并且可以访问了那我们接下来要完成的事情就是可以编写API那编写好了API之后呢我们就可以根据API去发送查询看一下能不能有数据了所以接下来呢我们完成一个API编写的这么一个操作找到我们的这个VS Code
[00:25] 那接下来呢API我们之前都说过了统一的放到SRC的API目录下当然了你放到哪个目录下其实无所谓只要能找到就可以我们约定俗成一般放到API目录下那我呢就把这个部门的API放到API base下边了好了那我在这边呢新建一个文件比如说我就叫DEPT.js好了那这个代码应该怎么写呢其实可以参照我们之前的逻辑来做Ctrl C Ctrl V Copy过来
[00:55] 好了这个没用到我们只用第一个create API就可以了当然这个create API是我们这个框架给我们封装好的我们直接使用即可当然如果有朋友有兴趣的话可以参照一下他的源码这边也有路径那好了那对于我们来说呢我们要完成的是基本增删改查的一个API编写那首先第一个呢我们叫做查询部门列表的API好了这边来一个保存部门的
[01:28] 部门的好了还来一个就是查根据ID查询部门的那好了继续根据ID删除部门的好了接着再来根据IDID更新A部门的那首先呢第一个查询部门列表就叫list
[01:52] 好了它等于Data什么Create API注意Create API三个参数我们昨天介绍过首先第一个参数应该是你的请求路径当然了我们的请求路径现在只关注后面的部分就可以了因为我们在Config当中DEV里面已经给它指定了前缀那所以呢我们部门请求的路径拿到列表就叫做Company我们刚才做过一个演示就Company那请求方式是Get
[02:21] Data我们不关注注意这个Data指的是你的请求参数有就有没有就没有当然了看你调用方法传递的情况好了那接下来呢就是保存部门写法基本上差不多Ctrl C拿过来Ctrl V那我这边叫做C5那C5的时候呢注意这个Data也有注意那我们保存部门这个时候的Data是不是就应该符合我们API的编写规范那我们保存部门
[02:52] 新增是不是就应该有ID等等等等等等所以我们这个Data它应该是一个对象里面有ID等等等等一大堆内容OK那我们这回的请求方式Post那好了继续根据ID查询部门那根据ID查询部门的写法的基本上跟它是一模一样的还是来一Data
[03:13] 那这个Data里面它的数据只有ID一个属性那上边呢可能还有Name属性等于什么等等等等一大堆但是我这边根据ID查询只要ID就可以了那只要ID的话注意我们请求方式是Get那注意了我们现在抱歉这边刚才这个路径考错了Department再回来Company下的Department才对这边同样的Company的Department才对好了这边Company的Department
[03:46] 那接下来注意那接下来我们还需要把ID以地址参数的形式给它拼接到后边那我这边呢借助一个模板走创模板走创打个号把这个Data里面的内容拼接出来Data.ID即可当然了我这种写法呢是EXC下边这个右屏右屏
[04:12] 这种呢可以在字符串之间直接拼写但你如果不想这样写你其实在后面加上department的iddata.id是一样的意思一样的意思ok好了那第三个我们也写好了接着第四个根据id删除那根据id删除跟上面这个基本上是一样的fine好了这边呢就叫delete那delete这个写法delete by id吧
[04:47] 因为delete是一个关键字我就叫delete by id好了data那传递过来没问题都没问题好了这边请求方式那同样的我们这边data里面只包含一个属性id即可那好了还有最后一个根据id更新就叫update那update呢这回呢update的内容data里面有id全部都封装到data里面比如说你想改部门名称改name比如说想改code
[05:24] 放到code里面那接下来呢我们这个data里面呢这回传递的传递的我们的API接口一起简单的再来看一下put的方式提交地址参数那地址参数是不是就是data.id这个没问题那我们的请求方式是不是叫做put所以我这边put那data里面有什么内容继续往后台传递是不是就可以了OK那这样一来我们的所有的
[05:51] 都写好了但是我想跟各位声明一点呢其实啊你会发现我这个save方法和这update方法大同小异只不过呢一个有id一个是不是就没有id啊所以对于我这边呢我可以再去构造一个就是保存或更新的方法比如说呢就叫做exportsaveorupdateupdate那saveorupdate的同样呢你也需要给我传递一个data过来
[06:28] 好了同样的借助create API同样的借助create API来做只不过我这回呢是调用一下sale或者update的方法是不是就可以了所以呢我这里面的代码写法就比较简单了比如说returnreturn data.id如果你出现了id这个参数那我就认为你是在做update把data传过去如果没有我就认为是在做sale方法把data传过去
[06:57] OK那这样一来呢其实我这个C5update的方法已经写好OK那这样一来我整个的API咱们就已经编写完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Vue.js 项目中，为 SaaS-HRM 系统的部门模块编写 API 请求函数，同时在浏览器中查看对应的 API 文档。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 SaaS-HRM 系统的“组织架构”页面，同时在任务栏预览了代码编辑器窗口。
画面 2: 在 Visual Studio Code 中，编辑 `src/api/depts.js` 文件，定义了获取部门列表的 API 函数 `list`。
画面 3: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 4: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 5: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 6: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 7: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 8: 在浏览器中打开了 API 文档页面，显示了 `/department` 路径下 POST、GET、PUT、DELETE 四种 HTTP 方法的接口。
画面 9: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 10: 在浏览器中，SaaS-HRM 系统的“组织架构”页面显示了“企业名称”输入框。
画面 11: 在 API 文档页面，点击了 POST 方法，查看了请求参数和示例值。
画面 12: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 13: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。
画面 14: 在 `depts.js` 文件中，为 `list` 函数添加了注释“空部门列表”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 3:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 4:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 5:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 6:
```javascript
import { createAPI } from '@/utils/request'

//空部门列表
export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 7:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 9:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
//空部门列表
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
```

画面 12:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
```

画面 13:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
```

画面 14:
```javascript
import { createAPI } from '@/utils/request'

export const list = data => createAPI('/company', 'get', data)
export const save = data => createAPI('/company', 'post', data)
export const detail = data => createAPI('/company/${data.id}', 'get', data)
export const deleteById = data => createAPI('/company/departments/${data.id}', 'delete', data)
export const update = data => createAPI('/company/${data.id}', 'put', data)
export const saveDuplicate = data => createAPI('/company', 'post', data)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: API 文档页面，显示了 `/department` 路径下 POST、GET、PUT、DELETE 四种 HTTP 方法的接口。
画面 11: API 文档页面，显示了 POST 方法的请求参数和示例值。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

