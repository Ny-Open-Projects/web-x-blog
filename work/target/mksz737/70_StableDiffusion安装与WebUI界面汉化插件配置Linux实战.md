# 70. Stable Diffusion 安装与 WebUI 界面、汉化、插件配置（Linux 实战）

## 纲要

- **安装路径**：Windows/macOS 有集成包直装；Linux 手动：git 环境 + Miniconda（python 3.10.6 推荐，conda 管版本）+ git clone 仓库切 dev 分支 + requirements 安装（国内源约 10 分）+ `python launch.py`（Windows `webui-user.bat`；`--port` 改端口）。
- **首次启动**：自动下基础模型 ~3.x G，后续启动快（实测进程启动 ~18.8s，慢在下载/加载模型）。
- **硬件坑**：主板/搭配没跟上，显卡性能发挥不出；环境不熟选 Windows 整合包。
- **WebUI 界面**：模型位置 / VAE / clip 跳过 / SD unit 加速 / 正向反向提示词 / 批次设置。
- **批次要点**：迭代步数 20–30（中位 24–25，30+ 费时优化有限）；每批数量别太高防爆显存，批次设 1、生成批次 4–8 多生几次。
- **必装扩展**：汉化包（localization 搜 chinese → ZH-CN）、infinite image browsing（图片浏览右键删/收藏）、openpose controlnet（姿态）、SD WebUI prompt translate（中文提示词自动翻译，百度/ChatGPT API，水龙头申请 $1 用量）；反向提示词用默认模板（C站可抄）。

> 本章按课程口径重构；产品名已规范化（Stable Diffusion/ComfyUI/ControlNet）；合并原 13-8 安装与 13-9 界面插件两节；剥离营销与课程群引流。

## 一、Linux 手动安装

- 准备：git（Ubuntu/Debian/macOS 自带）、Miniconda（python 3.10.6 推荐，版本管理避冲突）。
- 流程：`git clone` → 切 dev 分支 → `requirements.txt` 安装（国内源约 10 分）→ `python launch.py` 自动装 torch/torchvision 并下基础模型。
- 端口：`python launch.py --port 7888` 改端口；Windows 双击 `webui-user.bat`。

## 二、首次启动与硬件坑

- 首次下基础模型 ~3.x G，之后启动快（进程 ~18.8s，慢在模型下载/加载）。
- 硬件坑：主板/搭配拖后腿，显卡性能发挥不出；不熟 Linux 直接 Windows 整合包。

## 三、WebUI 界面与批次

- 顶部：模型/VAE/clip 跳过/SD unit 加速；中部：正向提示词（期望）+ 反向提示词（不期望，如多腿/花/成人内容）。
- 批次：迭代步数 20–30（中位 24–25）；每批数量别太高防爆显存，批次设 1、生成批次 4–8。
- 版本：1.7 RC 界面按钮多；低版本按钮少，建议 dev 分支。

## 四、必装插件

- 汉化包：localization 搜 chinese → settings 选 ZH-CN → 保存重启。
- infinite image browsing：图片浏览右键删/CTRL 多选收藏。
- openpose controlnet：姿态控制必装。
- SD WebUI prompt translate：中文提示词自动翻译（百度/ChatGPT API，水龙头 $1 用量长期够用）。
- 反向提示词：默认模板，C站模型页可抄他人 negative prompt。

## 五、FAQ

**Q1：Linux 安装 SD 关键步骤？**
git + Miniconda(3.10.6) + clone 切 dev + requirements + launch.py（首下模型~3.x G）。

**Q2：每批数量设太高会怎样？**
爆显存；建议批次 1、生成批次 4–8。

**Q3：迭代步数多少合适？**
20–30，中位 24–25；30+ 费时且优化有限。

**Q4：中文提示词怎么用？**
装 SD WebUI prompt translate 插件自动翻译，或手动译。

## 六、面试高频问答

**1. SD 安装的环境要点？**
Miniconda 管 python 3.10.6；clone 切 dev；launch.py 首下模型。

**2. 批次与显存的关系？**
每批数量高占显存多易爆；批次 1 + 生成批次 4–8 更稳。

**3. 必装哪些插件？**
汉化、infinite image browsing、openpose controlnet、prompt translate。

**4. 反向提示词作用？**
排除不想要的元素（多腿/花/成人内容），可用默认模板。

## 七、ops 提示（增效）

> **dev 分支追新**：界面/功能更新快，但注意依赖冲突与版本升级。
>
> **显存优先**：每批数量别贪高，爆显存比慢更废。
>
> **汉化+翻译插件省心**：ZH-CN 界面 + 中文提示自动译，降上手门槛。

