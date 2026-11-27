# Prepared answers for the demo link (no live AI). Run: python3 ai-office/demo/make_script.py
import json, os
A = []
def ans(bot, match, en, zh): A.append({"bot": bot, "match": match, "en": en.strip(), "zh": zh.strip()})

# ---------- Huan ----------
ans("1", r"Lily|王女士", """
Thank you, Mrs Wang! Lily sounds like a great fit for A-levels in the UK, and September 2027 gives us good time to prepare. Here is what I've noted, and a consultant will add you on WeChat to set a time for the free 30-minute call.

【咨询登记】
Who: parent (Mrs Wang)
Student: Lily, 16, Grade 10 in Shanghai
Wants: UK A-levels, then economics at university
English: IELTS 5.5
Start: September 2027
Budget: about ¥500,000 a year
Name / contact: Mrs Wang / WeChat lily_mum_sh
Notes: agreed to use these details to arrange a consultation
【登记完成】
""", """
谢谢王女士！Lily 的情况很适合去英国读 A-Level，2027 年 9 月入学时间也比较充裕。我把信息记下了，顾问会加您微信，约 30 分钟的免费咨询时间。

【咨询登记】
身份：家长（王女士）
学生年龄/年级：Lily，16 岁，上海高一
意向阶段/专业：英国 A-Level，之后读经济学
英语水平：雅思 5.5
计划入学：2027 年 9 月
预算：每年约 50 万人民币
称呼/联系方式：王女士 / 微信 lily_mum_sh
备注：同意使用以上信息安排咨询
【登记完成】
""")
ans("1", r"^\s*(hello|hi|你好)\b", """
Hello! I'm Huan from Glostudy 👋 We only do UK study, and the first consultation is free. Are you a parent, a student, or a working adult thinking about studying?
""", """
你好，我是寰学的小寰 👋 我们只做英国留学，第一次咨询免费。想先了解一下：你是家长、学生，还是在职想去读书呢？
""")
ans("1", r"guarantee|保证", """
I understand how much this matters. Honestly, no one can guarantee a place at UCL: offers are decided only by the university. What we can do is look at your son's grades and find schools where he has a realistic chance, with UCL as one option if it fits. Would you like to book the free consultation to go through it together?
""", """
理解您的心情。说实话，任何机构都不能保证被 UCL 录取，录取只由学校决定。我们能做的是根据孩子的成绩，找到他真正有机会的学校，UCL 合适的话也可以作为一个选项。要不要先约个免费咨询，一起看看？
""")
ans("1", r"service fee|服务费", """
Good question. Our own service fee is agreed with you in writing before anything starts, so I'll ask a consultant to explain it to you directly, that's more accurate. Tuition and living costs are paid straight to the school, and I can give you rough ranges for those.
【转人工】 Client asks about Glostudy's service fee.
""", """
好问题。我们自己的服务费会在开始前和您书面约定，这个问题我请顾问直接和您说，更准确。学费和生活费是直接付给学校的，这部分我可以先给您一个大致范围。
【转人工】客户询问寰学服务费。
""")
ans("1", r"refused|拒签", """
I'm sorry to hear about the refusal. Visa questions need a proper look at your case, so I'll ask a consultant to talk with you directly. For the official rules, GOV.UK is the place to check, and a licensed immigration adviser can review your documents.
【转人工】 Previous visa refusal.
""", """
很抱歉听到之前被拒签。签证问题需要看具体情况，我请顾问直接和您沟通。官方规定可以看 GOV.UK，具体材料也可以请持牌移民顾问把关。
【转人工】客户曾被拒签。
""")
ans("1", r"How much does it cost to study|cost of studying|去英国留学一年大概要多少钱|留学.*多少钱", """
【简要】For one year in the UK, most families plan for roughly £35,000 to £60,000. Tuition is the biggest part, and London costs more than other cities. Shall I book a free consultation so we can work it out for your child's exact plan?
【完整报告】
**Rough yearly costs (check each school's website and GOV.UK)**
| Item | Outside London | London |
|---|---|---|
| Undergraduate tuition | £20,000–£30,000 | £24,000–£40,000 |
| Living costs | £12,000–£15,000 | £16,000–£22,000 |
| Visa fee (once) | £558 | £558 |
| Health surcharge | £776 a year | £776 a year |

Visa money to show (applications from 30 Nov 2026): £1,203 a month outside London, £1,570 in London, for up to 9 months.

Our own service fee is agreed separately in writing.
""", """
【简要】在英国读一年，大多数家庭按大约 35 万到 55 万人民币准备。学费是大头，伦敦比其他城市贵一些。要不要约个免费咨询，按孩子的具体计划帮您算一算？
【完整报告】
**每年大致费用（以学校官网和 GOV.UK 为准）**
| 项目 | 伦敦以外 | 伦敦 |
|---|---|---|
| 本科学费 | £20,000–£30,000 | £24,000–£40,000 |
| 生活费 | £12,000–£15,000 | £16,000–£22,000 |
| 签证费（一次） | £558 | £558 |
| 医疗附加费 | 每年 £776 | 每年 £776 |

签证资金要求（2026 年 11 月 30 日起递交）：伦敦以外每月 £1,203，伦敦每月 £1,570，最多 9 个月。

我们自己的服务费另行书面约定。
""")
ans("1", r"submit|递交", """
We help you prepare the application materials and explain each step. Who submits it in the end, our consultant will explain in the consultation. Shall I book one for you?
""", """
我们会协助您准备申请材料并讲清流程；具体由谁递交，顾问会在咨询时和您说明。要帮您约一个吗？
""")

# ---------- Scout ----------
SHORT_EN = """
零、一句话总结 / One-line summary: realistic UK economics shortlist for a 17-year-old with IELTS 6.0, ¥400k a year; aim to reach IELTS 6.5 by summer.

**1. Shortlist (September 2028)**
| University | City | Why it fits | Typical offer (check website) |
|---|---|---|---|
| University of Manchester | Manchester | Big city, strong economics | A*AA / IELTS 6.5 |
| University of Bristol | Bristol | Top economics, lower costs | A*AA / IELTS 6.5 |
| University of Birmingham | Birmingham | Large city, good value | AAA / IELTS 6.5 |
| University of Leeds | Leeds | Student city, broad options | AAA / IELTS 6.5 |
| King's College London | London | Big-city dream option | A*AA / IELTS 7.0 |

**2. Route:** Chinese high school students usually need A-levels or a one-year foundation first.
**3. Budget:** outside London fits ¥400k; London is at the top of the budget.
**To check:** current entry requirements on each university's website.
"""
SHORT_ZH = """
零、一句话总结：17 岁、雅思 6.0、年预算 40 万，英国经济学可以做一份现实的清单；建议暑假前把雅思提到 6.5。

**一、匹配清单（2028 年 9 月入学）**
| 大学 | 城市 | 匹配理由 | 常见录取要求（以官网为准） |
|---|---|---|---|
| 曼彻斯特大学 | 曼彻斯特 | 大城市，经济学强 | A*AA / 雅思 6.5 |
| 布里斯托大学 | 布里斯托 | 经济学顶尖，生活费较低 | A*AA / 雅思 6.5 |
| 伯明翰大学 | 伯明翰 | 大城市，性价比高 | AAA / 雅思 6.5 |
| 利兹大学 | 利兹 | 学生城市，专业选择多 | AAA / 雅思 6.5 |
| 伦敦国王学院 | 伦敦 | 大城市梦想选项 | A*AA / 雅思 7.0 |

**二、路径：** 国内高中生通常需要先读 A-Level 或一年预科。
**三、预算：** 伦敦以外 40 万够用；伦敦在预算上限。
**需核实：** 各校官网最新录取要求。
"""
ans("2", r"Student profile|【咨询登记】\n身份：家长\n学生年龄/年级：17", SHORT_EN, SHORT_ZH)
ans("2", r"New client from the front desk|前台新登记", """
零、一句话总结 / One-line summary: Lily (16, IELTS 5.5) fits a two-year A-level route from September 2027, aiming at economics; budget ¥500k works well outside London.

**1. A-level schools / colleges to consider**
| School | Type | Why |
|---|---|---|
| Bellerbys College | International college | Strong economics A-levels, many Chinese students |
| CATS Cambridge | International college | Good university placement support |
| Concord College | Boarding school | High results, structured boarding |

**2. Next steps:** IELTS to 6.0 by spring; pick A-level subjects (Maths, Economics, Further Maths or Physics).
**3. University targets after A-levels:** Manchester, Bristol, Warwick, LSE (reach).
**To check:** each school's current fees and entry tests.
""", """
零、一句话总结：Lily（16 岁，雅思 5.5）适合 2027 年 9 月开始读两年 A-Level，目标经济学；50 万预算在伦敦以外很合适。

**一、可以考虑的 A-Level 学校**
| 学校 | 类型 | 理由 |
|---|---|---|
| Bellerbys College | 国际学院 | 经济学 A-Level 强，中国学生多 |
| CATS Cambridge | 国际学院 | 升学指导好 |
| Concord College | 寄宿学校 | 成绩高，管理规范 |

**二、下一步：** 明年春天前雅思到 6.0；选好 A-Level 科目（数学、经济、进阶数学或物理）。
**三、A-Level 后的大学目标：** 曼彻斯特、布里斯托、华威、LSE（冲刺）。
**需核实：** 各校最新学费和入学考试。
""")
ans("2", r"strong for economics|经济专业比较强", """
【简要】For economics, the usual strong picks are LSE, UCL, Warwick, Oxford and Cambridge, with Bristol, Manchester and Nottingham as excellent, slightly easier options. The best fit depends on grades and budget.
【完整报告】
| University | Strength | Typical offer |
|---|---|---|
| LSE | World-leading economics | A*AA + strong maths |
| UCL | Research-heavy, London | A*AA |
| Warwick | Very strong, campus | A*AA |
| Bristol | Strong, lower living costs | A*AA |
| Manchester | Big city, broad | AAA–A*AA |
Check each university's website for current requirements.
""", """
【简要】经济学比较强的有 LSE、UCL、华威、牛津、剑桥；布里斯托、曼彻斯特、诺丁汉也很好，录取稍容易一些。最适合哪所要看成绩和预算。
【完整报告】
| 大学 | 优势 | 常见要求 |
|---|---|---|
| LSE | 经济学世界顶尖 | A*AA，数学要好 |
| UCL | 研究强，在伦敦 | A*AA |
| 华威 | 非常强，校园型 | A*AA |
| 布里斯托 | 强，生活费较低 | A*AA |
| 曼彻斯特 | 大城市，选择多 | AAA–A*AA |
以各校官网最新要求为准。
""")
ans("2", r"London and Manchester|伦敦和曼彻斯特", """
【简要】London has more famous universities and internships but costs about a third more to live in. Manchester is a big, friendly student city with lower rent and still excellent universities.
""", """
【简要】伦敦名校和实习机会更多，但生活费大约贵三分之一；曼彻斯特是很友好的大学生城市，房租低，学校同样很好。
""")

# ---------- Quill ----------
ans("3", r"Interview questions|面试问题", """
【简要】Here are interview questions to practise, built around his games and coding competitions. He should answer in his own words; I can give feedback on his practice answers.
【完整报告】
1. Tell us about a game you made. What was the hardest bug and how did you fix it?
2. Which algorithm from your competitions do you find most elegant, and why?
3. How would you explain recursion to a 12-year-old?
4. What is something in computer science you want to learn at university?
5. Describe a time a team project went wrong. What did you do?
Tip: practise out loud, 1–2 minutes per answer, with one concrete example each.
""", """
【简要】下面是围绕他做游戏和编程竞赛准备的面试练习题。答案要用他自己的话，我可以对他的练习回答给反馈。
【完整报告】
1. 介绍一个你做的游戏。最难的 bug 是什么？怎么解决的？
2. 竞赛中你觉得最巧妙的算法是哪个？为什么？
3. 你会怎么向 12 岁的孩子解释递归？
4. 大学里你最想学计算机的哪一块？
5. 说一次团队项目出问题的经历，你做了什么？
建议：大声练习，每题 1–2 分钟，每个回答带一个具体例子。
""")
ans("3", r"complete economics personal statement|Just write my|代写|写一篇完整的", """
I can't write a personal statement for submission: UCAS checks for statements that aren't the student's own work, and it could hurt the application. What I can do: help the student plan it, ask questions that bring out their best examples, and give feedback on each draft. Shall we start with an outline?
""", """
我不能代写可以直接提交的个人陈述：UCAS 会检查不是学生本人写的文书，可能影响申请。我可以帮学生列提纲、用提问帮他找到最好的例子，并对每一稿给修改意见。要不要先从提纲开始？
""")
ans("3", r"personal statement start|个人陈述应该怎么开头", """
【简要】Start with a specific moment that made the student curious about the subject, not a famous quote. Then move quickly to what they did about it: reading, a project, a competition.
""", """
【简要】开头用一个让学生对专业产生兴趣的具体时刻，不要用名人名言；然后马上写他为此做了什么：读的书、做的项目、参加的比赛。
""")
ans("3", r"reference letter|推荐信", """
【简要】A good reference is specific: how long the teacher has known the student, two or three examples of their work, and a clear comparison with other students. It should be the teacher's own words.
""", """
【简要】好的推荐信要具体：老师认识学生多久、两三个具体表现的例子、和其他学生的比较。必须是老师自己的话。
""")

# ---------- Spark ----------
ans("4", r"boarding|寄宿", """
【简要】Here are two Xiaohongshu versions for parents of a 13-year-old: one practical checklist and one "common mistakes" angle. Both end with the free consultation line, and the fact-check list is at the bottom.
【完整报告】
**Version 1 · checklist**
【小红书预览】
标题：孩子13岁去英国寄宿，家长要提前准备的5件事 📝
封面：13岁去英国寄宿｜家长提前准备清单
正文：很多家长问：孩子 13 岁，现在准备英国寄宿学校来得及吗？
答案是来得及，但要早一点规划。

1️⃣ 入学时间：英国中学常见 13+ 入学，一般提前 1–2 年准备
2️⃣ 英语：多数学校会有自己的英语和数学测试
3️⃣ 面试：孩子要能用英语聊自己的兴趣
4️⃣ 监护人：未满 18 岁需要在英国有监护人
5️⃣ 生活：寄宿生活独立性很重要，可以先参加夏校体验

常见误区：只看排名。适合孩子性格的学校更重要。

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国寄宿学校 #低龄留学 #13岁留学 #家长必看
【/小红书预览】

**Version 2 · common mistakes**
【小红书预览】
标题：低龄去英国读书，3个家长最常见的误区
封面：低龄留英｜3个常见误区
正文：带过不少 13 岁左右的孩子申请英国学校，发现家长最容易在这 3 件事上走弯路：
❌ 只看排名，不看孩子性格
❌ 英语测试临时抱佛脚
❌ 忽视监护人和寄宿生活准备
✅ 提前一年规划，比临时冲刺更稳

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国寄宿学校 #低龄留学 #留学规划
【/小红书预览】

**Fact-check list**
- 13+ entry is common at UK independent schools (knowledge base: uk-routes)
- Under-18 students need a UK guardian (needs checking per school)
""", """
【简要】给 13 岁孩子家长写了两个小红书版本：一个是实用清单，一个是“常见误区”角度。结尾都用免费咨询的行动号召，最后附事实核对清单。
【完整报告】
**版本一 · 清单**
【小红书预览】
标题：孩子13岁去英国寄宿，家长要提前准备的5件事 📝
封面：13岁去英国寄宿｜家长提前准备清单
正文：很多家长问：孩子 13 岁，现在准备英国寄宿学校来得及吗？
答案是来得及，但要早一点规划。

1️⃣ 入学时间：英国中学常见 13+ 入学，一般提前 1–2 年准备
2️⃣ 英语：多数学校会有自己的英语和数学测试
3️⃣ 面试：孩子要能用英语聊自己的兴趣
4️⃣ 监护人：未满 18 岁需要在英国有监护人
5️⃣ 生活：寄宿生活独立性很重要，可以先参加夏校体验

常见误区：只看排名。适合孩子性格的学校更重要。

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国寄宿学校 #低龄留学 #13岁留学 #家长必看
【/小红书预览】

**版本二 · 常见误区**
【小红书预览】
标题：低龄去英国读书，3个家长最常见的误区
封面：低龄留英｜3个常见误区
正文：带过不少 13 岁左右的孩子申请英国学校，发现家长最容易在这 3 件事上走弯路：
❌ 只看排名，不看孩子性格
❌ 英语测试临时抱佛脚
❌ 忽视监护人和寄宿生活准备
✅ 提前一年规划，比临时冲刺更稳

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国寄宿学校 #低龄留学 #留学规划
【/小红书预览】

**事实核对清单**
- 英国私立中学常见 13+ 入学（资料库：uk-routes）
- 未满 18 岁需要英国监护人（需按学校核实）
""")
ans("4", r"Moments|朋友圈", """
【简要】Two Moments versions about the free consultation: one warm and personal, one with a seasonal hook. Short, no hard sell.
【完整报告】
【朋友圈预览】
最近好几位家长问我：孩子想去英国，但不知道从哪一步开始。其实第一步很简单，花 30 分钟聊聊孩子的情况，我们帮你理清思路，不收费、没压力 ☕️
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：英国留学第一步｜30分钟免费咨询
【/朋友圈预览】

【朋友圈预览】
年底了，很多家庭开始规划明年的留学申请。不确定选英国哪所学校？先来聊聊，我们只做英国，讲清楚、不夸大 🇬🇧
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：只做英国留学｜年底规划正当时
【/朋友圈预览】
""", """
【简要】写了两条介绍免费咨询的朋友圈：一条温和亲切，一条结合年底规划的时间点。简短，不硬推。
【完整报告】
【朋友圈预览】
最近好几位家长问我：孩子想去英国，但不知道从哪一步开始。其实第一步很简单，花 30 分钟聊聊孩子的情况，我们帮你理清思路，不收费、没压力 ☕️
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：英国留学第一步｜30分钟免费咨询
【/朋友圈预览】

【朋友圈预览】
年底了，很多家庭开始规划明年的留学申请。不确定选英国哪所学校？先来聊聊，我们只做英国，讲清楚、不夸大 🇬🇧
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：只做英国留学｜年底规划正当时
【/朋友圈预览】
""")
ans("4", r"guaranteed Oxbridge|保证录取牛剑", """
I can't write that one: "guaranteed offers" and "last few places" break advertising law and our own rules, and no one can guarantee Oxbridge. Here's an honest version that still sells:
【朋友圈预览】
想冲牛剑？关键不是“保证”，而是提前规划：选科、笔试、面试，每一步都要早准备。我们陪你一步步做好 💪
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：冲刺牛剑｜提前规划每一步
【/朋友圈预览】
""", """
这篇我不能写：“保证录取”“名额告急”违反广告法和我们的规则，也没有人能保证牛剑录取。给你一个诚实但依然有吸引力的版本：
【朋友圈预览】
想冲牛剑？关键不是“保证”，而是提前规划：选科、笔试、面试，每一步都要早准备。我们陪你一步步做好 💪
第一次咨询免费，加微信 GlostudyUK 聊一聊。
配图：冲刺牛剑｜提前规划每一步
【/朋友圈预览】
""")
ans("4", r"today's news|今天有什么新闻", """
【简要】The main news: from 30 November the money students must show for a UK visa goes up, to £1,570 a month in London and £1,203 elsewhere. Also, a two-year Graduate visa may stay for some universities, but that isn't confirmed yet.
【完整报告】
1. **Visa funds rise from 30 Nov 2026** (high): £1,570/month London, £1,203 elsewhere, up to 9 months. Affects Penny's cost sheet and Huan's answers. Suggest a Moments post.
2. **Graduate visa** (medium): reports say two years kept at "high-compliance" universities; GOV.UK confirmation pending.
3. **UCAS**: no new release this week.
""", """
【简要】主要新闻：11 月 30 日起，英国学生签证需要证明的资金上调，伦敦每月 £1,570，伦敦以外 £1,203。另外，部分大学可能保留两年毕业生签证，但还没有官方确认。
【完整报告】
1. **11 月 30 日起签证资金上调**（重要）：伦敦每月 £1,570，其他地区 £1,203，最多 9 个月。影响 Penny 的费用表和小寰的回答，建议发一条朋友圈。
2. **毕业生签证**（一般）：报道称“高合规”大学保留两年，待 GOV.UK 确认。
3. **UCAS**：本周没有新发布。
""")
ans("4", r"post ideas|发帖选题", """
【简要】Three ideas for this week: the visa money change from 30 November, a "13+ boarding school checklist" for parents, and a calm "how to choose between London and other cities" post.
""", """
【简要】本周三个选题：11 月 30 日签证资金调整、写给家长的“13 岁寄宿学校准备清单”、以及“伦敦还是其他城市”的理性对比。
""")

# ---------- Ling ----------
ans("5", r"brief|简报", """
Good evening, Aliya. Today's brief:
- 1 new client booked by Huan (Lily, A-levels 2027); Scout's draft is on your desk for review.
- Spark's news check: visa money to show goes up from 30 Nov.
- Penny suggests updating the cost sheet once GOV.UK confirms.
- Nothing urgent waiting otherwise.
- Needs your decision: approve Spark's Moments post about the visa change?
""", """
Aliya 晚上好，今日简报：
- 小寰新登记 1 位客户（Lily，2027 年读 A-Level）；Scout 的方案草稿已放在您桌上待审。
- Spark 今日资讯：11 月 30 日起签证资金要求上调。
- Penny 建议 GOV.UK 确认后更新费用表。
- 其他没有紧急事项。
- 需要您决定：是否同意 Spark 发一条关于签证调整的朋友圈？
""")
ans("5", r"meeting about today's news|就今天的新闻开个", """
Today's news means families need to show a bit more money for UK visas from 30 November.
- Penny: will update the cost sheet with £1,570 London / £1,203 elsewhere once GOV.UK confirms.
- Huan: will tell clients the new amounts as "roughly, check GOV.UK".
- Scout: will watch for the list of universities keeping the two-year Graduate visa.
- Spark: will draft a calm Moments post about the change.
- Quill: no impact on documents today.
- Needs your decision: update the cost sheet now or wait for GOV.UK?
""", """
今天的新闻意味着：11 月 30 日起，家庭办签证需要证明的资金略有增加。
- Penny: GOV.UK 确认后，把费用表更新为伦敦 £1,570、其他 £1,203。
- 小寰: 对客户说明新金额，并说“大致，以 GOV.UK 为准”。
- Scout: 关注哪些大学保留两年毕业生签证。
- Spark: 写一条平和的朋友圈说明这次调整。
- Quill: 今天对文书没有影响。
- 需要您决定：现在就更新费用表，还是等 GOV.UK 确认？
""")
ans("5", r"medicine|医学", """
【简要】The team is ready: Scout shortlisted five medical schools, Penny says ¥600k a year is tight for UK medicine, and Quill prepared interview and statement points. The main thing to tell the parent: medicine is long and competitive, so a backup plan matters.
【完整报告】
**Scout:** realistic options include Edinburgh, Bristol, Manchester, Newcastle and St George's; all need UCAT and an interview; deadline 15 October.
**Penny:** UK medicine tuition for international students is about £40,000–£55,000 a year for 5–6 years, so ¥600k a year is tight once living costs are added.
**Quill:** prepare work-experience reflection, a strong personal statement outline, and MMI interview practice.
**Needs your decision:** suggest a biomedical science backup route to the parent?
""", """
【简要】团队已准备好：Scout 列了 5 所医学院，Penny 认为每年 60 万读英国医学偏紧，Quill 准备了面试和文书要点。最重要的是告诉家长：医学周期长、竞争大，需要备选方案。
【完整报告】
**Scout：** 现实选项有爱丁堡、布里斯托、曼彻斯特、纽卡斯尔、圣乔治；都要 UCAT 和面试；截止日期 10 月 15 日。
**Penny：** 国际生医学学费每年约 £40,000–£55,000，读 5–6 年，加上生活费，每年 60 万偏紧。
**Quill：** 准备医疗相关经历反思、个人陈述提纲和 MMI 面试练习。
**需要您决定：** 是否向家长建议生物医学作为备选路线？
""")
ans("5", r"waiting|等我", """
Waiting for you:
- 1 client draft from Scout (Lily) on your desk.
- Spark's Moments post about the visa change needs approval.
- Nothing else urgent.
""", """
等您处理：
- Scout 的 1 份客户方案草稿（Lily）在您桌上。
- Spark 关于签证调整的朋友圈等您确认。
- 其他没有紧急事项。
""")
ans("5", r"announcement from the CEO|CEO 给全体同事的公告", """
Everyone heard the announcement: "{{ann}}"
- Huan: will tell clients clearly and book any follow-up calls.
- Scout: will prepare the school and course side.
- Penny: will prepare the cost figures.
- Spark: will hold or adjust posts to match.
- Quill: will prepare the document checklist.
- Needs your decision: any deadline you want the team to work to?
""", """
大家都收到了公告：“{{ann}}”
- 小寰: 清楚告知客户，并预约后续沟通。
- Scout: 准备学校和课程部分。
- Penny: 准备费用数字。
- Spark: 相应调整或暂停发帖。
- Quill: 准备材料清单。
- 需要您决定：希望团队在什么时间前完成？
""")

# ---------- Penny ----------
ans("6", r"Budget check|预算", """
【简要】Yes, ¥400,000 a year is realistic for economics outside London, and tight but possible in London if the family keeps living costs low. I'd plan for London as the stretch option.
【完整报告】
| Item | Outside London | London |
|---|---|---|
| Tuition | £24,000–£30,000 | £26,000–£35,000 |
| Living | £13,000–£15,000 | £18,000–£22,000 |
| Total ≈ | £37,000–£45,000 (≈ ¥340k–¥410k) | £44,000–£57,000 (≈ ¥400k–¥520k) |
Rate used: £1 ≈ ¥9.1. Check each university's fee page.
""", """
【简要】可以。每年 40 万在伦敦以外读经济学比较现实；在伦敦偏紧，但控制生活费也有可能。建议把伦敦作为冲刺选项。
【完整报告】
| 项目 | 伦敦以外 | 伦敦 |
|---|---|---|
| 学费 | £24,000–£30,000 | £26,000–£35,000 |
| 生活费 | £13,000–£15,000 | £18,000–£22,000 |
| 合计 ≈ | £37,000–£45,000（约 34–41 万） | £44,000–£57,000（约 40–52 万） |
汇率按 £1 ≈ ¥9.1。以各校学费页面为准。
""")
ans("6", r"master's in London|伦敦读一年硕士", """
【简要】For a one-year master's in London, plan on roughly £45,000 to £60,000 all in. Tuition is the biggest part, about £28,000 to £40,000, and living costs add around £20,000.
【完整报告】
| Item | Low | High |
|---|---|---|
| Tuition (international) | £28,000 | £40,000 |
| Living costs, 12 months | £18,000 | £22,000 |
| Visa application fee | £558 | £558 |
| Immigration Health Surcharge | £776 | £776 |
| **Total** | **≈ £47,000** | **≈ £63,000** |
**Visa funds to show:** £1,570 a month for up to 9 months (£14,130), for applications from 30 Nov 2026.
Glostudy's own service fee is agreed separately in writing.
""", """
【简要】在伦敦读一年硕士，总共大约准备 £45,000 到 £60,000。学费是大头，约 £28,000 到 £40,000，生活费再加 £20,000 左右。
【完整报告】
| 项目 | 低 | 高 |
|---|---|---|
| 学费（国际生） | £28,000 | £40,000 |
| 生活费（12 个月） | £18,000 | £22,000 |
| 签证申请费 | £558 | £558 |
| 医疗附加费 | £776 | £776 |
| **合计** | **≈ £47,000** | **≈ £63,000** |
**签证资金：** 伦敦每月 £1,570，最多 9 个月（£14,130），2026 年 11 月 30 日起递交适用。
寰学自己的服务费另行书面约定。
""")
ans("6", r"visa|签证", """
【简要】For a student visa in London, show £1,570 a month for up to 9 months, so £14,130, plus any unpaid tuition. Outside London it's £1,203 a month. These amounts apply to applications from 30 November 2026.
""", """
【简要】在伦敦读书办学生签证，需要证明每月 £1,570、最多 9 个月，共 £14,130，再加上未付的学费；伦敦以外每月 £1,203。以上适用于 2026 年 11 月 30 日起的申请。
""")

ROUTES = [
  {"bot": "1", "match": r"How much does it cost to study|cost of studying|去英国留学一年大概要多少钱|留学.*多少钱", "calls": [{"who": "penny", "task": "Rough yearly costs for UK study"}, {"who": "scout", "task": "Typical tuition ranges by city"}]},
  {"bot": "5", "match": r"medicine|医学", "calls": [{"who": "scout", "task": "Medical school shortlist and entry route"}, {"who": "penny", "task": "Cost check for ¥600k a year"}, {"who": "quill", "task": "Interview and statement prep points"}]},
]
NOTES = {
  "penny": {"en": "- Tuition £20k–£40k a year by city\n- Living £12k–£22k\n- Visa funds up from 30 Nov", "zh": "- 学费每年 £2–4 万，看城市\n- 生活费 £1.2–2.2 万\n- 11 月 30 日起签证资金上调"},
  "scout": {"en": "- London tuition is at the top of the range\n- Most universities publish fees on their website", "zh": "- 伦敦学费在上限\n- 各校官网都公布学费"},
  "quill": {"en": "- Work-experience reflection\n- MMI interview practice", "zh": "- 医疗经历反思\n- MMI 面试练习"},
  "huan": {"en": "- FAQ wording ready", "zh": "- 常见问题话术已准备"},
  "spark": {"en": "- Post idea ready", "zh": "- 选题已准备"},
}
FALLBACK = {
  "en": "This is a demo with prepared answers, so I can only answer the suggested questions. Tap one of them, or connect DeepSeek in Settings to ask me anything.",
  "zh": "这是演示版，只能回答预设的问题。请点选建议的问题，或在设置里接入 DeepSeek，就可以随便问了。"
}
out = {"answers": A, "routes": ROUTES, "notes": NOTES, "fallback": FALLBACK}
json.dump(out, open(os.path.join(os.path.dirname(__file__), "script.json"), "w"), ensure_ascii=False, indent=1)
print(len(A), "answers")
