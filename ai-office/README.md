# 寰学 AI 办公室 · Glostudy AI Office

四个 AI「员工」的完整设计：提示词、知识库、模板和测试。可以直接搬到国内平台（扣子 Coze、Dify），
用 DeepSeek、Kimi 或通义千问运行，在中国大陆正常使用。

Four AI "employees" for Glostudy, designed here and run on Chinese platforms and models (DeepSeek, Kimi, Qwen),
so they work in mainland China. Claude designs and updates them; the bots run on their own.

| # | 员工 | 用户 | 作用 |
|---|---|---|---|
| 1 | 前台客服「小寰」 | 客户 | 回答常见问题，收集信息，转给顾问 |
| 2 | 院校资料员 | 内部 | 根据学生情况出匹配清单草稿 |
| 3 | 文书助理 | 内部 | 访谈提纲、文书结构、润色（不代写） |
| 4 | 营销文案 | 内部 | 小红书、公众号、朋友圈、抖音文案 |

```
agents/      每个机器人的系统提示词（复制「---」以下的内容）
knowledge/   知识库：公司资料、英国升学路径、55 所学校与大学（含 QS / 卫报排名）
templates/   文书访谈提纲、各平台文案格式
tests/       客服机器人的测试问题（含刁钻问题）
tools/       export-knowledge.js：从官网重新导出学校数据；try_bot.py：在电脑上试聊和测试
```

## 上线前必须做 · Before going live
1. 打开 `knowledge/company.md`，处理所有【待确认】：服务价格、申请由谁递交（官网两处说法不一致）。
2. 用下面的方法试聊，跑一遍测试，逐条读回复。

## 方法 A：扣子 Coze（推荐，不用写代码）
1. 打开 **coze.cn**，用手机号或抖音登录。
2. 「创建智能体」→ 名字填「小寰」。
3. 模型选 **DeepSeek**（或豆包、Kimi）。温度调低一点（约 0.3），回答更稳定。
4. 把 `agents/1-customer-service.md` 中「---」以下的全部内容，粘贴到「人设与回复逻辑」。
5. 「知识库」→ 新建文本知识库 → 上传 `knowledge/` 里文件名列出的 .md 文件（学校数据也可以用 .csv 建表格知识库）。
6. 在右侧预览窗口，用 `tests/customer-service-tests.json` 里的问题逐条测试。
7. 「发布」→ 选择 **企业微信** 或 **微信公众号（服务号/订阅号）**，按页面提示授权。
   ⚠️ 不要把机器人接到个人微信号（GlostudyUK）上，违反微信规则，可能被封号。
8. 机器人 2–4 只给自己用：同样创建，发布到「扣子商店」时设为仅自己可见，或者直接在扣子里用。

平台界面会更新，步骤名称可能略有不同。

## 方法 B：在电脑上直接试（DeepSeek / Kimi API）
适合改完提示词后快速测试。只需要 Python 3，不用装任何东西。
```bash
export DEEPSEEK_API_KEY=sk-...                      # 在 platform.deepseek.com 申请，充值几元即可
python3 ai-office/tools/try_bot.py chat 1            # 和客服机器人聊天
python3 ai-office/tools/try_bot.py test              # 跑全部客服测试
python3 ai-office/tools/try_bot.py chat 4 --provider kimi   # 用 Kimi（MOONSHOT_API_KEY）
```

## 方法 C：Dify（自己部署，数据完全在自己服务器上）
Dify 开源，可以部署在阿里云 / 腾讯云服务器上，接 DeepSeek API。适合以后客户量大、对数据要求高时再考虑。

## 分工 · Who does what
- **Claude（设计）**：写和改提示词、知识库、模板、测试；官网数据变了就重新导出（`node ai-office/tools/export-knowledge.js`）。
- **你（运营）**：注册平台账号、上线、审核所有输出、对接客户和订单；把机器人答错的对话发给 Claude 修改。

## 注意 · Notes
- 机器人的输出都是草稿，发给客户前要人工审核（客服机器人除外，但它只答常见问题，其余都转人工）。
- 文书：UCAS 会检测 AI 生成的个人陈述，文书助理只做提纲、引导和润色。
- 个人信息：未成年学生的信息要请家长同意；不要把客户资料贴到境外工具里。
