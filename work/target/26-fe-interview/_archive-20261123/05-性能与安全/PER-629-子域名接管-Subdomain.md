---
title: [PER-629] 子域名接管（Subdomain Takeover）是什么？前端项目怎么排查和预防？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-629：子域名接管（Subdomain Takeover）是什么？前端项目怎么排查和预防？

**答**：
- 机制：子域名 CNAME 指向的云资源已注销（如删了 GitHub Pages/Aliyun OSS/S3），但 DNS 记录还在——攻击者在原平台上重新注册同名资源，即可完全控制该子域名（种 cookie 到父域、窃取 OAuth 回调、挂钓鱼页）。
- 前端常见触发点：营销活动页用完即弃（活动域名 CNAME 到静态托管后资源下线）、废弃的 CDN 加速域名、测试环境域名忘记回收。
- 排查：全量子域名清单（DNS 记录导出）-> 逐个检测 CNAME 目标是否可注册（访问返回 404/NXDOMAIN 且页面带云商特征文案）-> 清理 dangling 记录。
- 预防制度：域名生命周期进 CMDB，活动页下线 SOP 必须包含回收 DNS + 注销托管资源两步；关键子域（sso、api、files）禁止活动用途复用。

```javascript

// 子域名接管检测器：访问 dangling CNAME 并识别云商特征
const PROVIDER_SIGS = [
  { host: 'github.io', sig: /There isn't a GitHub Pages site here/ },
  { host: 'aliyuncs.com', sig: /NoSuchBucket|The specified bucket does not exist/ },
  { host: 'amazonaws.com', sig: /NoSuchBucket/ },
  { host: 'azurewebsites.net', sig: /404 Web Site not found/ },
  { host: 'herokuapp.com', sig: /No such app/ },
];
async function checkTakeover(sub) {
  const url = `https://${sub}`;
  try {
    const res = await fetch(url, { mode: 'cors' }).catch(() => null);
    const text = res ? await res.text().catch(() => '') : '';
    const hit = PROVIDER_SIGS.find(p => url.includes(p.host) && p.sig.test(text));
    return hit ? { sub, risk: 'high', verdict: `CNAME 指向 ${hit.host} 且资源可接管` }
               : { sub, risk: 'low', verdict: '正常' };
  } catch {
    return { sub, risk: 'warn', verdict: '无法访问（可能已挂也可能 NXDOMAIN，需 DNS 侧确认）' };
  }
}
// SOP：活动页下线 checklist 增加回收 DNS 记录 + 注销托管资源必选项
```
