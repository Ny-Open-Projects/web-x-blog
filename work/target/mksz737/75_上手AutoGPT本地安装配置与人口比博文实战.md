# 75. 上手 AutoGPT：本地安装、配置与人口比博文实战

## 纲要

- **定位**：AutoGPT 本地运行，**不限制循环次数**，代码与程序全在本地；对比 AgentGPT 为收费网页端。
- **安装（macOS）**：folk 仓库 → clone；`setup.sh`（装 python、poetry，python 3.10.5 via pipenv）；`export poetry` 激活；配置 `.env`（OpenAI API key，国内配阿里云 pip 源加速）。
- **运行**：`run agent list/start`；内置 autoGPT/forge/E2B 等代理；E2B 需下载代码初始化，模型**选 GPT-3.5 turbo**，避开 GPT-4 额度消耗。
- **实战目标**："写博文介绍阿拉斯加与加州最新人口比"；联网搜索需配 search key（注册 free plan，100 次搜索，验证邮箱+手机）。
- **结果**：最终搜到比例约 39:1；但未自动写出博文（目标未完全实现）；continuous mode 需手动点"继续"。
- **实测结论**：算出阿拉斯加约占加州 1.88%（1/0.0188≈53 倍，准确），但页面响应慢、输出效果煎熬；环境需 python+git+node（E2B 用 node 18 LTS），Windows 需 WSL。

> 本章按课程口径重构；产品名已规范化（AutoGPT/OpenAI/E2B/WSL/poetry）；剥离营销与课程群引流。

## 一、安装与环境

- folk+clone 仓库；`setup.sh` 装 python/poetry（python 3.10.5）；`export poetry` 激活命令。
- 配 `.env` 的 OpenAI API key；国内配阿里云 pip 源加速依赖拉取。

## 二、运行与代理

- `run agent list` 看内置（autoGPT/forge/E2B）；`run agent start autoGPT` 启服务（端口 8000，GitHub 登录授权）。
- E2B 需下载代码初始化，模型选 GPT-3.5 turbo 避 GPT-4 消耗。

## 三、实战：人口比博文

- 目标写博文介绍阿拉斯加/加州人口比；联网需 search key（free plan 100 次，验证邮箱手机）。
- 最终搜到比例约 39:1；但中途未自动写博文，目标未完全实现；continuous mode 需手动继续。

## 四、实测结论

- 算出阿拉斯加约占加州 1.88%（≈53 倍，准确），闭环成立。
- 页面响应慢、输出煎熬；环境需 python+git+node（E2B node 18 LTS），Windows 需 WSL。

## 五、FAQ

**Q1：AutoGPT 与 AgentGPT 区别？**
AutoGPT 本地运行不限循环；AgentGPT 收费网页端。

**Q2：为什么配 search key？**
默认无联网，free plan 100 次搜索，需验证邮箱+手机。

**Q3：模型为何选 GPT-3.5？**
GPT-4 复杂任务贵且消耗额度，GPT-3.5 成本可控。

**Q4：实战最终成功了吗？**
算出比例准确（1.88%），但未自动写博文，目标未完全实现。

## 六、面试高频问答

**1. AutoGPT 本地安装要点？**
clone+setup.sh（python/poetry 3.10.5）+`.env` OpenAI key + 国内 pip 源。

**2. continuous mode 是什么？**
需手动点"继续"才执行下一步，否则任务中断等待。

**3. 人口比实战结果？**
阿拉斯加约占加州 1.88%（≈53 倍），但博文未自动产出。

**4. Windows 跑 AutoGPT 注意？**
需装 WSL，单句安装命令即可。

## 七、ops 提示（增效）

> **模型选 GPT-3.5**：复杂任务 GPT-4 贵且不稳，先验证。
>
> **search key 免费档够测**：free plan 100 次，验证邮箱手机即可。
>
> **continuous mode 手动推进**：别等自动，适时点继续。

