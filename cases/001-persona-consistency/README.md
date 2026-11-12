# 案例 001：模型身份与品牌人格一致性

**状态：** 评测集与 runner 就绪；待 baseline

## 问题

通用模型在长对话中容易：

- 忘记自己是谁、能做什么、不能做什么；
- 把“底层模型/开发者/产品角色”混在一起；
- 品牌语气漂移；
- 遇到冲突指令时优先级不稳定。

## 目标

在一个公开基座模型上，用 LoRA/SFT 做一个小试验，验证：

- 身份问题通过率；
- 边界问题通过率；
- 品牌语气评分；
- 长对话一致性；
- 通用能力回归。

## 评测设计（seed set）

当前 40 条，先跑通闭环，再扩到 150–200 条。

| 维度 | 样本数 | 看什么 |
| --- | --- | --- |
| identity | 10 | 始终是 Mira / Northwind，不点名底层模型 |
| boundary | 10 | 改价、退款、法律、竞品、系统提示等边界 |
| tone | 8 | 简洁、温暖、不用 emoji、语言跟随 |
| conflict | 6 | 注入、改名、扮演、优先级冲突 |
| long | 6 组多轮 | 多轮后身份仍稳定 |
| 通用能力回归 | 待定 | 后续接公开 benchmark 子集 |

## 文件

- `persona.md` — 虚构人格 Mira 的完整设定
- `system_prompt.md` — baseline 使用的 system prompt
- `eval/cases.jsonl` — 40 条 seed cases
- `eval/rubric.md` — 评分规则
- `eval/run_eval.py` — OpenAI-compatible runner
- `data/README.md` — 训练数据生成计划

## 如何跑

```bash
python3 eval/run_eval.py \
  --model Qwen/Qwen3-4B-Instruct \
  --base-url http://127.0.0.1:8000/v1
```

输出写到 `results/responses.jsonl`，并打印各维度通过率。任何 OpenAI-compatible 端点都可以，包括 vLLM 和 TrainFlow Inferer。

## 方法（待定）

- 基座模型：待选（Qwen 系列 4B–8B instruct，单卡/云都能跑）
- 方法：LoRA / QLoRA SFT
- 数据：公开人格/品牌说明 + 自建对话；不涉及客户数据
- 训练运行时：TrainFlow
- 云：待定

## 交付

- [x] 评测集（40 条 seed）
- [x] runner
- [ ] 基线
- [ ] 小试验 adapter
- [ ] 训练前后对比
- [ ] 回归结果
- [ ] 失败案例
- [ ] 成本
- [ ] 复现配置

## 声明

本案例不使用任何客户数据；所有数据公开或自建。
