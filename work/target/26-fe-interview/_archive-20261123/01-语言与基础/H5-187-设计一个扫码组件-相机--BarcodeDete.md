---
title: [H5-187] 设计一个扫码组件（相机 + BarcodeDetector）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-187：设计一个扫码组件（相机 + BarcodeDetector）
**答**：
- 链路：`getUserMedia` 后置摄像头 → video 播放 → 周期性把帧画到离屏 canvas → `BarcodeDetector.detect()` 解码。
- 兼容红线：`BarcodeDetector` 在 iOS 缺失——必须 jsQR/ZXing 库兜底（`getImageData` 传入解析）。
- 性能：解码耗 CPU，150~200ms 节流轮询；取景框裁剪只解码框内区域；识别成功立即 `clearInterval` + `track.stop()` 释放摄像头。
- 体验细节：安卓可用 `track.applyConstraints({advanced:[{torch:true}]})` 开手电筒；权限拒绝降级为"手动输入/上传图片识别"（图片走同一 detect 流程）。

```html
<video id="cam" autoplay playsinline muted style="width:320px"></video>
<button id="scan">开始扫码</button>
<p id="result"></p>
<script>
document.getElementById('scan').onclick = async () => {
  // 能力探测：BarcodeDetector 在 iOS 缺失，必须 jsQR 兜底
  let detector = null;
  if ('BarcodeDetector' in window) {
    detector = new BarcodeDetector({ formats: ['qr_code', 'ean_13'] });
  }

  const stream = await navigator.mediaDevices.getUserMedia({
    video: { facingMode: { ideal: 'environment' },        // 后置摄像头
             width: { ideal: 1280 }, height: { ideal: 720 } },
  });
  const video = document.getElementById('cam');
  video.srcObject = stream;
  await video.play();

  // 取景框只解码框内区域：减少解码面积提升速度
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d', { willReadFrequently: true });

  // 节流轮询：解码耗 CPU，150~200ms 一次足够
  const timer = setInterval(async () => {
    if (video.readyState < 2) return;
    canvas.width = video.videoWidth; canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    try {
      let text = null;
      if (detector) {
        const codes = await detector.detect(canvas);      // 直接支持 canvas 源
        text = codes[0]?.rawValue;
      } else {
        const img = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const r = jsQR(img.data, img.width, img.height);  // iOS 兜底库
        text = r?.data;
      }
      if (text) {
        clearInterval(timer);                             // 成功立刻停轮询
        stream.getTracks().forEach((t) => t.stop());      // 释放摄像头
        document.getElementById('result').textContent = text;
      }
    } catch { /* 单帧解码失败忽略，下轮重试 */ }
  }, 150);

  // 体验细节：
  // 安卓开手电筒：track.applyConstraints({ advanced: [{ torch: true }] })
  // 权限拒绝降级：手动输入 / 上传图片识别（图片文件走同一 detect 流程）
};
</script>
```
