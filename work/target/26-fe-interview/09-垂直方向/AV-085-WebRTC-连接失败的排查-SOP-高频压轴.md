---
title: [AV-085] WebRTC 连接失败的排查 SOP。（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-085：WebRTC 连接失败的排查 SOP。（高频压轴）
**答**：
- SOP 六步：① 确认 HTTPS 与浏览器兼容；② 信令是否通（offer/answer 是否互换成功）；③ SDP 是否合法（方向/编码交集）；④ ICE 状态走到哪（checking/failed）；⑤ 候选类型与 NAT 环境（强制 relay 测试）；⑥ DTLS/证书指纹与防火墙端口。
- 快速分诊表：connectionState=failed + 无 relay 候选 → TURN 未配/凭证错；有 relay 仍 failed → 端口被防火墙封（换 443/tcp）；never beyond checking → SDP 不匹配或候选未交换。
- 工具：chrome://webrtc-internals 看 createOffer/setRemoteDescription 报错与候选配对；ICE restart 验证网络瞬断；对端 getStats 对比双向候选。
- 日志采集：每次失败上报 signalingState/connectionState/iceConnectionState/候选摘要 + webrtc-internals dump，形成可回放的现场。
- 典型案例：企业内网封 UDP → 必须 turn tcp/443；华为部分机型 VP9 硬解不支持 → SDP 编码集合裁剪。

```javascript
// 连接失败诊断器：自动输出 SOP 结论
class WebrtcDiagnostic {
  async diagnose(pc, sigLog) {
    const report = { sig: {}, ice: {}, sdp: {} };
    // 1. 信令
    report.sig.offerSent = sigLog.some((m) => m.type === 'offer');
    report.sig.answerGot = sigLog.some((m) => m.type === 'answer');
    report.sig.candidatesExchanged = sigLog.filter((m) => m.type === 'candidate').length;
    // 2. 状态
    report.ice.state = pc.iceConnectionState;         // failed?
    report.ice.conn = pc.connectionState;
    // 3. 候选与选路
    const stats = await pc.getStats();
    const cands = [], pairs = [];
    stats.forEach((r) => {
      if (r.type === 'local-candidate') cands.push(r.candidateType);
      if (r.type === 'candidate-pair') pairs.push(r);
    });
    report.ice.hasRelay = cands.includes('relay');
    report.ice.bestPair = pairs.find((p) => p.state === 'succeeded')?.nominated ? 'ok' : 'none';
    // 4. 结论
    let verdict = 'unknown';
    if (!report.sig.answerGot) verdict = 'signaling-broken';
    else if (!report.ice.hasRelay && report.ice.state === 'failed') verdict = 'need-turn-or-credential';
    else if (report.ice.hasRelay && report.ice.state === 'failed') verdict = 'firewall-blocked-ports';
    else if (report.ice.state === 'failed' && report.sig.candidatesExchanged === 0) verdict = 'candidates-not-exchanged';
    return { verdict, report };
  }
}
```
