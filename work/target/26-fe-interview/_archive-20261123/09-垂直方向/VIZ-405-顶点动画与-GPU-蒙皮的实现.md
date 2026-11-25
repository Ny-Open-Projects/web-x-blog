---
title: [VIZ-405] 顶点动画与 GPU 蒙皮的实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-405：顶点动画与 GPU 蒙皮的实现

**答**：
- 蒙皮：每顶点 4 关节索引 + 4 权重，关节矩阵（预乘逆绑定矩阵）加权变换；矩阵从关节 uniform/纹理取。
- 成本：100 关节 100 实例 = 100×100 矩阵更新/CPU；GPU 蒙皮（compute/纹理矩阵）下沉。
- 简化：LBS（线性混合蒙皮）的"糖果纸"伪影用对偶四元数（DQ 蒙皮）解决。

```javascript
// GPU 蒙皮 shader
`in ivec4 aJoints; in vec4 aWeights;
uniform mat4 uJointMats[64];
void skin(inout vec4 pos, inout vec3 nrm) {
  mat4 m = uJointMats[aJoints.x] * aWeights.x +
           uJointMats[aJoints.y] * aWeights.y +
           uJointMats[aJoints.z] * aWeights.z +
           uJointMats[aJoints.w] * aWeights.w;
  pos = m * pos;
  nrm = mat3(m) * nrm;      // 非均匀缩放需法线矩阵，动画多为刚体可简化
}`
```
