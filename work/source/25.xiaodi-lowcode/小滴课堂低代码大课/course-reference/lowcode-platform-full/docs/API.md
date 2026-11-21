# API 接口文档

> Base URL(Nginx 网关):`http://<host>:5000/api`
> 统一响应:`{ "code": 0, "data": ..., "msg": "..." }`(成功) / `{ "code": -1, "data": null, "msg": "..." }`(失败)
> 鉴权方式:请求头 `Authorization: Bearer <token>`(标注 🔒 的接口需要)

## 一、用户模块 `/user`

| # | 方法 | 路径 | 鉴权 | 说明 | 关键入参 |
|---|---|---|---|---|---|
| 1 | POST | `/user/captcha` | - | 图形验证码(SVG),Redis 60s;key=MD5(ip+ua) 自动生成 | body: `{type: "register"\|"login"}` |
| 2 | POST | `/user/send_code` | - | 短信验证码(60s 防重 + 图形码前置校验) | `{phone, captcha, type}` |
| 3 | POST | `/user/register` | - | 注册(短信码校验+双密码+MD5),成功即登录返回 token | `{phone, sendCode, password, confirm}` |
| 4 | POST | `/user/password_login` | - | 密码登录 | `{phone, password}` |
| 5 | POST | `/user/phone_login` | - | 验证码登录 | `{phone, sendCode}` |

## 二、微信扫码登录 `/wechat_login`

| # | 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|---|
| 6 | GET | `/wechat_login/callback` | - | 微信服务器接入验证(SHA1 签名比对,返回 echostr) |
| 7 | GET | `/wechat_login/login` | - | 获取扫码二维码(返回 qrcodeUrl + ticket),Redis 记 `{isScan:"no"}` 120s |
| 8 | POST | `/wechat_login/callback` | - | 微信推送回调(XML):解析 open_id → 未注册自动建号 → 签发 token → 更新 `{isScan:"yes"}` → 回复欢迎 XML |
| 9 | GET | `/wechat_login/check_scan` | - | 前端轮询(ticket),已扫码返回 token |

## 三、低代码编辑模块 `/low_code`

| # | 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|---|
| 10 | POST | `/low_code/release` | 🔒 | **发布页面**(事务):首次创建 / 重复发布整体替换(页面+组件+问卷数据) |
| 11 | GET | `/low_code/release_with_user` | 🔒 | 编辑器进入:按用户取组件配置(带 componentIds 顺序) |
| 12 | GET | `/low_code/release?id=` | - | C 端发布页:按页面 id 取组件配置 |

发布接口入参结构:

```json
{
  "page_name": "页面标题",
  "desc": "页面简介",
  "tdk": "SEO 关键词",
  "components": [
    { "type": "swiper", "options": { "images": [ /* ... */ ] } },
    { "type": "input", "options": { "title": "姓名" } }
  ]
}
```

## 四、发布页问卷 `/low_code`

| # | 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|---|
| 13 | GET | `/low_code/is_question_data_posted` | - | 是否已提交问卷(依据:服务端 MD5(ip+ua) 匿名标识) |
| 14 | POST | `/low_code/question_data` | - | 提交问卷(服务端二次查重防重复) |

提交入参:`{ page_id: 1, props: [{ "id": 13, "value": "老王" }, { "id": 16, "value": ["optId1"] }] }`

## 五、资源模块 `/resources`

| # | 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|---|
| 15 | POST | `/resources/upload` | 🔒 | 上传图片/视频(multipart 字段 `file`)→ OSS → 资源表登记 |
| 16 | DELETE | `/resources?id=` | 🔒 | 删除资源(先删 OSS 对象再删记录) |
| 17 | GET | `/resources?type=image\|video` | 🔒 | 当前用户资源列表(资源面板复用) |

## 六、数据统计 `/low_code`

| # | 方法 | 路径 | 鉴权 | 说明 |
|---|---|---|---|---|
| 18 | GET | `/low_code/question_components` | 🔒 | 当前用户全部问卷组件(input/textArea/radio/checkbox) |
| 19 | GET | `/low_code/question_data` | 🔒 | 全部问卷明细(表格数据) |
| 20 | POST | `/low_code/get_question_data_by_id` | 🔒 | 按组件 id 取单题数据(饼图/柱状图/文本平铺) |

## 七、错误约定

| code | 场景 | 示例 msg |
|---|---|---|
| -1 | 业务校验失败 | "60秒内请勿重复获取验证码" / "该手机号已被注册" / "图形验证码不正确" |
| -1 | DTO 校验失败 | 字段级提示数组(如 "id限制为number类型!") |
| 401 | token 缺失/过期 | 走 HttpException,过滤器统一包装 |
| 500 | 发布等事务失败 | "发布失败,..." |

## 八、部署端口映射

| 入口 | 端口 | 容器 | 内部 |
|---|---|---|---|
| API 网关 | 5000 | backend_nginx | → 宿主 5001 → backend:3000 |
| 发布页网关 | 4000 | frontend_nginx | → 宿主 4001 → release:3000 |
