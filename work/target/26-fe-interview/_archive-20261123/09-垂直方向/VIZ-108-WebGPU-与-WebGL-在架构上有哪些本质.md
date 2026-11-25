---
title: [VIZ-108] WebGPU 与 WebGL 在架构上有哪些本质差异？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-108：WebGPU 与 WebGL 在架构上有哪些本质差异？
**答**：① **命令模型**——WebGL 是即时隐式状态机（改 uniform 全局生效），WebGPU 是显式命令编码器（CommandEncoder 录制、批量 submit），驱动开销极低；② **管线对象化**——WebGL 的着色器/混合/深度状态散落全局，WebGPU 打包成不可变 GPURenderPipeline，切换零成本；③ **资源绑定**——WebGL 靠 bindTexture 等副作用，WebGPU 用声明式 BindGroup；④ **多线程**——device/queue 可配合 OffscreenCanvas 在 Worker 使用；⑤ **Compute Shader** 原生支持。一句话：WebGL 像逐条发指令，WebGPU 像提交批处理任务。

```javascript
// 同一件事：设置 uniform 并画一个三角形——两代 API 的心智模型对比
// WebGL：全局状态机，状态散落且隐式生效
gl.useProgram(prog);
gl.uniformMatrix4fv(mvpLoc, false, mvp);
gl.bindTexture(gl.TEXTURE_2D, tex);
gl.bindVertexArray(vao);
gl.drawArrays(gl.TRIANGLES, 0, 3);
// WebGPU：录制命令 -> 一次性提交，管线与绑定都是显式对象
const encoder = device.createCommandEncoder();
const pass = encoder.beginRenderPass({ colorAttachments: [view] });
pass.setPipeline(pipeline);            // 不可变管线：着色器+混合+深度已打包
pass.setBindGroup(0, bindGroup);       // 声明式资源绑定
pass.draw(3);
pass.end();
device.queue.submit([encoder.finish()]); // 批量提交，驱动开销低
```
