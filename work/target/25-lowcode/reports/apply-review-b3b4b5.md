# 批3/批4/批5 审核修正落地记录（2026-11-19）

## 批3（02 第二期 26 篇，review-b3-p2.md）
P1×8 全落地：6-4 component_data 三列口径（page_id/user=MD5(ip+ua)/props）、8-5 unbuild rollup.emitCJS+externals、8-6/9-4 `pnpm run:client`、9-3 异常结构 {code,-1,data:null,msg}、9-4 ESM export default、10-5 form→phone、10-8 标题与 3 处引用拉平。
P2：resource→resources、xdclass-lowcode.sql、5173 端口、getConnection 弃用口径、sharedText→xd、docker rmi 表述、pnpm-workspace 锁定文件说法、9-3 类名/覆盖面/校验提示、10-1 前置与下一步篇名。
未采纳：8-5 tsconfig 三处出入（创建期快照可保留）。

## 批4（03 第三期 23 篇，review-b4-p3.md）
P1×26 全落地：11-7 `register:code:` Redis key、`sign({id})`、save 字段 username/head_img/open_id；11-8 password_login/phone_login 服务与 DTO 名；11-6 send_code、key 分层、删短信验证码对象、randomName；11-3 生产不返回 text、captche() 拼写；12-2/12-4/12-5/12-6 isScan 'no'/'yes' 字符串统一、callback 路径、getAccessToken 返回 json、WechatDataTool/getXMLStr、scene_id 123、wechat-login-tool.module forRootop；12-6 兜底分支注明；13-2 makeAutoObservable + auth 拼写 + computed 直引 store；13-5 删 mapped-types、IUser 字段、storeAuth 单例、无 I 前缀类型、.env baseURL；13-6/13-8/13-10 manual:true + Bearer 前缀 + /editor；13-7 useSendCode(form,'login')、子组件不收 setActiveKey；13-9 wechatLoading/activeQrcode；13-10 防抖注释。
S1 断链实况复核：11-2 标题与全部引用已一致（报告前提过时，未改）。S2 标点拉平、S3 build:share 已落。

## 批5（04 第四期 24 篇，review-b5-p4.md）
P1×23 全落地：14-2 IComponent 字段、14-3 /low_code/release + ILowCode/snake_case、14-4 保留问卷数据口径、14-5 release_with_user/codeId→account_id、14-8 poster、14-9 fillComponentPropsByConfig、15-1/15-2 handleClicked+FormPropLabel、15-3 autoPlay 默认 true、15-4 updateCurrentCompConfigWithArray、15-5 coverImg、15-6 TBasicComponentConfig+标题、15-8 dashed+Empty 三属性、16-1 DOMPurify 表述、16-3 title/showClose+FormContainer、16-4 标题、16-5 transcript 清除+onUpdate/text。
P2：Edit*→Editor* 系、localXxx→LowCodeXxx 簇、build 脚本、controls 恒展示、itemsExpandIndex 语义、antd List.Item 三要素、ColorFactory、onValuesChangeAfter 等。
标题批量规整：24 篇 title/h1 全部对齐文件名（数字前缀已剥离）。

同步：target 02/03/04 → blog `diff -rq` 校验（见下）。
