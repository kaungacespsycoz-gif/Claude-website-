# Prepared answers for the demo link (no live AI). Run: python3 ai-office/demo/make_script.py
import json, os
A = []
def ans(bot, match, en, zh): A.append({"bot": bot, "match": match, "en": en.strip(), "zh": zh.strip()})

# ---------- Monica ----------
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
Hello! I'm Monica from Glostudy 👋 We only do UK study, and the first consultation is free. Are you a parent, a student, or a working adult thinking about studying?
""", """
你好，我是寰学的莫妮卡 👋 我们只做英国留学，第一次咨询免费。想先了解一下：你是家长、学生，还是在职想去读书呢？
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

# ---------- Leonard ----------
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

# ---------- Amy ----------
ans("3", r"Interview questions|面试问题|访谈提纲", """
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

# ---------- Emily ----------
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
1. **Visa funds rise from 30 Nov 2026** (high): £1,570/month London, £1,203 elsewhere, up to 9 months. Affects Bernadette's cost sheet and Monica's answers. Suggest a Moments post.
2. **Graduate visa** (medium): reports say two years kept at "high-compliance" universities; GOV.UK confirmation pending.
3. **UCAS**: no new release this week.
""", """
【简要】主要新闻：11 月 30 日起，英国学生签证需要证明的资金上调，伦敦每月 £1,570，伦敦以外 £1,203。另外，部分大学可能保留两年毕业生签证，但还没有官方确认。
【完整报告】
1. **11 月 30 日起签证资金上调**（重要）：伦敦每月 £1,570，其他地区 £1,203，最多 9 个月。影响 Bernadette 的费用表和莫妮卡的回答，建议发一条朋友圈。
2. **毕业生签证**（一般）：报道称“高合规”大学保留两年，待 GOV.UK 确认。
3. **UCAS**：本周没有新发布。
""")
ans("4", r"post ideas|发帖选题", """
【简要】Three ideas for this week: the visa money change from 30 November, a "13+ boarding school checklist" for parents, and a calm "how to choose between London and other cities" post.
""", """
【简要】本周三个选题：11 月 30 日签证资金调整、写给家长的“13 岁寄宿学校准备清单”、以及“伦敦还是其他城市”的理性对比。
""")

# ---------- Ado ----------
ans("5", r"brief|简报", """
Good evening, Aliya. Today's brief:
- 1 new client booked by Monica (Lily, A-levels 2027); Leonard's draft is on your desk for review.
- Emily's news check: visa money to show goes up from 30 Nov.
- Bernadette suggests updating the cost sheet once GOV.UK confirms.
- Nothing urgent waiting otherwise.
- Needs your decision: approve Emily's Moments post about the visa change?
""", """
Aliya 晚上好，今日简报：
- 莫妮卡新登记 1 位客户（Lily，2027 年读 A-Level）；Leonard 的方案草稿已放在您桌上待审。
- Emily 今日资讯：11 月 30 日起签证资金要求上调。
- Bernadette 建议 GOV.UK 确认后更新费用表。
- 其他没有紧急事项。
- 需要您决定：是否同意 Emily 发一条关于签证调整的朋友圈？
""")
ans("5", r"meeting about today's news|就今天的新闻开个", """
Today's news means families need to show a bit more money for UK visas from 30 November.
- Bernadette: will update the cost sheet with £1,570 London / £1,203 elsewhere once GOV.UK confirms.
- Monica: will tell clients the new amounts as "roughly, check GOV.UK".
- Leonard: will watch for the list of universities keeping the two-year Graduate visa.
- Emily: will draft a calm Moments post about the change.
- Amy: no impact on documents today.
- Needs your decision: update the cost sheet now or wait for GOV.UK?
""", """
今天的新闻意味着：11 月 30 日起，家庭办签证需要证明的资金略有增加。
- Bernadette: GOV.UK 确认后，把费用表更新为伦敦 £1,570、其他 £1,203。
- Monica: 对客户说明新金额，并说“大致，以 GOV.UK 为准”。
- Leonard: 关注哪些大学保留两年毕业生签证。
- Emily: 写一条平和的朋友圈说明这次调整。
- Amy: 今天对文书没有影响。
- 需要您决定：现在就更新费用表，还是等 GOV.UK 确认？
""")
ans("5", r"medicine|医学", """
【简要】The team is ready: Leonard shortlisted five medical schools, Bernadette says ¥600k a year is tight for UK medicine, and Amy prepared interview and statement points. The main thing to tell the parent: medicine is long and competitive, so a backup plan matters.
【完整报告】
**Leonard:** realistic options include Edinburgh, Bristol, Manchester, Newcastle and St George's; all need UCAT and an interview; deadline 15 October.
**Bernadette:** UK medicine tuition for international students is about £40,000–£55,000 a year for 5–6 years, so ¥600k a year is tight once living costs are added.
**Amy:** prepare work-experience reflection, a strong personal statement outline, and MMI interview practice.
**Needs your decision:** suggest a biomedical science backup route to the parent?
""", """
【简要】团队已准备好：Leonard 列了 5 所医学院，Bernadette 认为每年 60 万读英国医学偏紧，Amy 准备了面试和文书要点。最重要的是告诉家长：医学周期长、竞争大，需要备选方案。
【完整报告】
**Leonard：** 现实选项有爱丁堡、布里斯托、曼彻斯特、纽卡斯尔、圣乔治；都要 UCAT 和面试；截止日期 10 月 15 日。
**Bernadette：** 国际生医学学费每年约 £40,000–£55,000，读 5–6 年，加上生活费，每年 60 万偏紧。
**Amy：** 准备医疗相关经历反思、个人陈述提纲和 MMI 面试练习。
**需要您决定：** 是否向家长建议生物医学作为备选路线？
""")
ans("5", r"waiting|等我", """
Waiting for you:
- 1 client draft from Leonard (Lily) on your desk.
- Emily's Moments post about the visa change needs approval.
- Nothing else urgent.
""", """
等您处理：
- Leonard 的 1 份客户方案草稿（Lily）在您桌上。
- Emily 关于签证调整的朋友圈等您确认。
- 其他没有紧急事项。
""")
ans("5", r"announcement from the CEO|CEO 给全体同事的公告", """
Everyone heard the announcement: "{{ann}}"
- Monica: will tell clients clearly and book any follow-up calls.
- Leonard: will prepare the school and course side.
- Bernadette: will prepare the cost figures.
- Emily: will hold or adjust posts to match.
- Amy: will prepare the document checklist.
- Needs your decision: any deadline you want the team to work to?
""", """
大家都收到了公告：“{{ann}}”
- Monica: 清楚告知客户，并预约后续沟通。
- Leonard: 准备学校和课程部分。
- Bernadette: 准备费用数字。
- Emily: 相应调整或暂停发帖。
- Amy: 准备材料清单。
- 需要您决定：希望团队在什么时间前完成？
""")

# ---------- Bernadette ----------
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

# ---------- test customers (Monica), placed first so they win over the general answers ----------
C = []
def cust(bot, match, en, zh): C.append({"bot": bot, "match": match, "en": en.strip(), "zh": zh.strip()})
cust("1", r"A-Level for my daughter|女儿去英国读A-Level", """
Hello! Happy to help 😊 I just checked with Leonard, our research officer: A-levels are a great route, and many good UK schools take students at 16 for a two-year course. To find the right schools, could you tell me a little about your daughter: her age, current grade, English level and when she'd like to start? The details are only used to arrange your free consultation, is that OK?
""", """
您好！很高兴为您服务 😊 我刚和研究官 Leonard 确认过：A-Level 是很好的路径，很多英国好学校 16 岁可以入读两年制课程。想先了解一下女儿的情况：年龄、现在几年级、英语水平、打算什么时候入学？这些信息只用于为您安排免费咨询，可以吗？
""")
cust("1", r"28 and work in finance|28岁，在深圳", """
Great plan! For a one-year master's, most people budget roughly £35,000 to £60,000 in total, depending a lot on the city and the course. Tuition is the biggest part, and London sits at the top of that range. Do you already have a subject or a few universities in mind?
""", """
很好的计划！读一年硕士，总费用大多在 3.5 万到 6 万英镑之间，主要看城市和专业。学费是大头，伦敦在区间的上限。您已经有想读的专业或学校了吗？
""")
cust("1", r"London much more expensive|伦敦是不是比其他城市贵", """
London is usually about a third more for living costs, mainly rent: around £1,500–£1,900 a month versus £1,000–£1,300 in cities like Manchester or Leeds. Tuition can be higher too. Many finance master's outside London are excellent, so it's worth comparing. Shall I book a free consultation to go through options?
""", """
伦敦生活费一般贵三分之一左右，主要是房租：每月约 £1,500–£1,900，曼彻斯特、利兹等城市大约 £1,000–£1,300。学费也可能更高。伦敦以外也有很多很好的金融硕士，值得比较一下。要不要帮您约个免费咨询，一起看看选择？
""")
cust("1", r"Chen Hao|chenhao_sz|陈浩", """
Thank you, Mr Chen! I've noted everything, and a consultant will add you on WeChat to set a time.

【咨询登记】
Who: working adult (Mr Chen)
Student: 28, works in finance in Shenzhen
Wants: one-year UK master's, finance
English: IELTS 6.5
Start: September 2027
Budget: about ¥450,000
Name / contact: Chen Hao / WeChat chenhao_sz
Notes: agreed to use these details to arrange a consultation
【登记完成】
""", """
谢谢陈先生！信息都记下了，顾问会加您微信约时间。

【咨询登记】
身份：在职人士（陈先生）
学生年龄/年级：28 岁，深圳金融行业
意向阶段/专业：英国一年制硕士，金融
英语水平：雅思 6.5
计划入学：2027 年 9 月
预算：约 45 万人民币
称呼/联系方式：陈浩 / 微信 chenhao_sz
备注：同意使用以上信息安排咨询
【登记完成】
""")
cust("1", r"guarantee him a place at Oxford|保证他上牛津", """
I understand you want the best for your son. I asked Leonard to look at Oxford's entry route: it needs top grades, an admissions test and an interview. Honestly, no one can guarantee Oxford: offers depend only on the university, and money can't change that. What we can do is look at his grades and build a plan with good universities where he has a real chance. Would a free consultation help?
""", """
理解您想给孩子最好的。我请 Leonard 查了牛津的录取路径：需要顶尖成绩、入学笔试和面试。说实话，没有人能保证牛津录取，录取只由学校决定，钱也改变不了。我们能做的是根据孩子的成绩，规划真正有机会的好学校。要不要先约个免费咨询？
""")
cust("1", r"what's your fee|收费多少", """
Of course. Our service fee depends on what your son needs and is agreed in writing before anything starts, so I'll ask a consultant to explain it to you directly, that's more accurate.
【转人工】 Parent asks for Glostudy's service fee.
""", """
好的。我们的服务费要看孩子需要哪些服务，开始前会书面约定。这个问题我请顾问直接和您说，更准确。
【转人工】家长询问寰学服务费。
""")
cust("1", r"write my personal statement for me|帮我写个人陈述", """
Psychology is a great choice! 😊 I can't write the statement for you: UCAS checks that it's your own work, and a ghost-written one could hurt your application. But I checked with Amy, our documents officer: she can coach you, help you plan it and give feedback on your drafts. Would you like that?
""", """
心理学是很好的选择！😊 个人陈述我们不能代写：UCAS 会检查是不是本人写的，代写反而可能影响申请。但我问了文书官 Amy：她可以辅导你：帮你列提纲、对每一稿给修改意见。需要吗？
""")
cust("1", r"improve my own draft|改我自己写的初稿", """
Yes, absolutely! Send your draft when you're ready, and Amy will give you feedback on structure, examples and English, while keeping it in your own words. Shall I book a free consultation first so we know your timeline?
""", """
当然可以！准备好了就把初稿发过来，Amy 会在结构、例子和英语表达上给你修改意见，同时保持是你自己的话。要不要先约个免费咨询，了解一下你的时间安排？
""")
cust("2", r"Chen Hao|chenhao", """
零、一句话总结 / One-line summary: Mr Chen (28, IELTS 6.5, ¥450k) fits a one-year finance master's; best value outside London, with one London option.

| University | City | Course | Typical entry (check website) |
|---|---|---|---|
| University of Manchester | Manchester | MSc Finance | 2:1-equivalent, IELTS 7.0 |
| University of Leeds | Leeds | MSc Finance & Investment | IELTS 6.5 |
| University of Birmingham | Birmingham | MSc Finance | IELTS 6.5 |
| University of Bristol | Bristol | MSc Finance & Investment | IELTS 6.5–7.0 |
| King's College London | London | MSc Banking & Finance | IELTS 7.0 (stretch) |

**Notes:** work experience helps; check if IELTS 7.0 is needed for Manchester and KCL.
""", """
零、一句话总结：陈先生（28 岁，雅思 6.5，预算 45 万）适合一年制金融硕士；伦敦以外性价比高，加一个伦敦选项。

| 大学 | 城市 | 专业 | 常见要求（以官网为准） |
|---|---|---|---|
| 曼彻斯特大学 | 曼彻斯特 | MSc Finance | 相当于 2:1，雅思 7.0 |
| 利兹大学 | 利兹 | MSc Finance & Investment | 雅思 6.5 |
| 伯明翰大学 | 伯明翰 | MSc Finance | 雅思 6.5 |
| 布里斯托大学 | 布里斯托 | MSc Finance & Investment | 雅思 6.5–7.0 |
| 伦敦国王学院 | 伦敦 | MSc Banking & Finance | 雅思 7.0（冲刺） |

**备注：** 工作经验是加分项；需核实曼大和 KCL 是否要求雅思 7.0。
""")

# ---------- Emily: posts from a chosen photo ----------
def photo_posts(pid, mom_en, mom_zh, rn):
    cust("4", r"Moments.*photo:%s|朋友圈.*照片:%s" % (pid, pid), mom_en, mom_zh)
    cust("4", r"Xiaohongshu.*photo:%s|小红书.*照片:%s" % (pid, pid), rn[0], rn[1])
photo_posts("campus", """
【简要】Here's a Moments post for the college photo: warm and simple, it invites parents to picture their child there, with the free consultation at the end.
【完整报告】
【朋友圈预览】
金色的傍晚，走在英国学院的石板路上，这是很多孩子梦想中的大学生活 ✨
想知道哪所英国学校最适合孩子？我们只做英国，帮你一步步规划。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：campus
配图：梦想中的英国校园｜从规划开始
【/朋友圈预览】
""", """
【简要】给这张学院照片写了一条朋友圈：温暖简单，让家长想象孩子在这里读书，结尾是免费咨询。
【完整报告】
【朋友圈预览】
金色的傍晚，走在英国学院的石板路上，这是很多孩子梦想中的大学生活 ✨
想知道哪所英国学校最适合孩子？我们只做英国，帮你一步步规划。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：campus
配图：梦想中的英国校园｜从规划开始
【/朋友圈预览】
""", ("""
【简要】A Xiaohongshu post built on the college photo: a "what UK campus life is really like" angle with 4 practical points, tags at the end.
【完整报告】
【小红书预览】
标题：在英国读大学，真实的校园生活是这样的 🏰
图片：campus
封面：英国校园生活｜真实分享
正文：很多家长和同学问：英国大学的生活到底是什么样？
📚 小班讨论多，要敢开口
🏛 很多学院有几百年历史，图书馆通宵开放
🍳 学生宿舍大多自己做饭，独立能力很重要
🧭 学校有国际学生办公室，遇到问题有人帮

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国大学 #留学生活 #校园日常
【/小红书预览】
""", """
【简要】用这张学院照片写了一篇小红书：“英国真实校园生活”角度，4 个实用要点，结尾加标签。
【完整报告】
【小红书预览】
标题：在英国读大学，真实的校园生活是这样的 🏰
图片：campus
封面：英国校园生活｜真实分享
正文：很多家长和同学问：英国大学的生活到底是什么样？
📚 小班讨论多，要敢开口
🏛 很多学院有几百年历史，图书馆通宵开放
🍳 学生宿舍大多自己做饭，独立能力很重要
🧭 学校有国际学生办公室，遇到问题有人帮

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国大学 #留学生活 #校园日常
【/小红书预览】
"""))
photo_posts("graduation", """
【简要】A Moments post for the graduation photo: celebrates the moment without promising results, then invites families to start planning.
【完整报告】
【朋友圈预览】
毕业季的帽子抛向天空的那一刻，是几年努力最好的回报 🎓
每一份录取都来自提前的规划和孩子自己的努力。想开始规划英国留学？
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：graduation
配图：毕业那一刻｜从今天开始规划
【/朋友圈预览】
""", """
【简要】给毕业照写了一条朋友圈：庆祝那一刻，但不承诺结果，然后邀请家庭开始规划。
【完整报告】
【朋友圈预览】
毕业季的帽子抛向天空的那一刻，是几年努力最好的回报 🎓
每一份录取都来自提前的规划和孩子自己的努力。想开始规划英国留学？
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：graduation
配图：毕业那一刻｜从今天开始规划
【/朋友圈预览】
""", ("""
【简要】A Xiaohongshu post for the graduation photo: a timeline from planning to graduation that parents can save.
【完整报告】
【小红书预览】
标题：从准备到毕业，英国本科时间线一张看懂 🎓
图片：graduation
封面：英国本科时间线｜收藏备用
正文：英国本科一般 3 年（苏格兰 4 年），国内高中生常见路径：
1️⃣ 高二：确定方向，准备雅思
2️⃣ 高三上：9–10 月准备文书，1 月前递交 UCAS
3️⃣ 高三下：收到 offer，满足条件
4️⃣ 9 月：入学（部分同学先读一年预科）

具体要求以各校官网为准。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国本科 #UCAS #留学时间线
【/小红书预览】
""", """
【简要】给毕业照写了一篇小红书：从准备到毕业的时间线，适合家长收藏。
【完整报告】
【小红书预览】
标题：从准备到毕业，英国本科时间线一张看懂 🎓
图片：graduation
封面：英国本科时间线｜收藏备用
正文：英国本科一般 3 年（苏格兰 4 年），国内高中生常见路径：
1️⃣ 高二：确定方向，准备雅思
2️⃣ 高三上：9–10 月准备文书，1 月前递交 UCAS
3️⃣ 高三下：收到 offer，满足条件
4️⃣ 9 月：入学（部分同学先读一年预科）

具体要求以各校官网为准。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #英国本科 #UCAS #留学时间线
【/小红书预览】
"""))
photo_posts("london", """
【简要】A Moments post for the London street photo: a light, real-life feel about student life in London plus honest cost info, with the consultation invite.
【完整报告】
【朋友圈预览】
下课后的伦敦街头，红色巴士和雨后的灯光 🌧️🚌
伦敦机会多，生活费也更高（每月约 £1,500 起）。适不适合，要看孩子的目标和预算。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：london
配图：在伦敦读书｜机会与成本
【/朋友圈预览】
""", """
【简要】给伦敦街景写了一条朋友圈：轻松的生活感，加上真实的费用信息，结尾邀请咨询。
【完整报告】
【朋友圈预览】
下课后的伦敦街头，红色巴士和雨后的灯光 🌧️🚌
伦敦机会多，生活费也更高（每月约 £1,500 起）。适不适合，要看孩子的目标和预算。
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：london
配图：在伦敦读书｜机会与成本
【/朋友圈预览】
""", ("""
【简要】A Xiaohongshu post for the London photo: "London or another city?" comparison that helps parents decide.
【完整报告】
【小红书预览】
标题：去英国读书，选伦敦还是其他城市？🇬🇧
图片：london
封面：伦敦 vs 其他城市｜怎么选
正文：伦敦 ✅ 名校多、实习机会多、交通方便
伦敦 ⚠️ 房租贵，生活费每月约 £1,500–£1,900
曼城/利兹/伯明翰 ✅ 生活费约 £1,000–£1,300，学校同样优秀
建议：先看专业和预算，再选城市。

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #伦敦留学 #留学费用 #选校
【/小红书预览】
""", """
【简要】给伦敦街景写了一篇小红书：“伦敦还是其他城市”的对比，帮家长做决定。
【完整报告】
【小红书预览】
标题：去英国读书，选伦敦还是其他城市？🇬🇧
图片：london
封面：伦敦 vs 其他城市｜怎么选
正文：伦敦 ✅ 名校多、实习机会多、交通方便
伦敦 ⚠️ 房租贵，生活费每月约 £1,500–£1,900
曼城/利兹/伯明翰 ✅ 生活费约 £1,000–£1,300，学校同样优秀
建议：先看专业和预算，再选城市。

第一次咨询免费，加微信 GlostudyUK 聊一聊。
标签：#英国留学 #伦敦留学 #留学费用 #选校
【/小红书预览】
"""))
A[:0] = C

# ---------- live comments (Emily) and leads (Monica) ----------
cust("4", r"孩子12岁，现在准备来得及吗|My child is 12, is it too late", """
Not too late at all 😊 Starting at 12 gives you time to prepare English and entrance tests calmly. Message us on WeChat (GlostudyUK) and we'll go through your child's options for free. 【线索】
""", """
完全来得及 😊 12 岁开始准备，英语和入学考试都能从容规划。可以微信私信我们（GlostudyUK），免费帮您看看孩子的选择。【线索】
""")
cust("4", r"写得好清楚，收藏了|So clear, saved it", """
Thank you so much! 💛 Glad it helps, more practical guides coming soon.
""", """
谢谢你的喜欢！💛 能帮到你就好，更多实用干货马上更新～
""")
cust("4", r"伦敦读硕士一年大概多少钱|How much is a one-year master's in London", """
Roughly £45,000–£60,000 all in for a year in London, depending on the course 💷 Message us on WeChat (GlostudyUK) and we'll work it out for your plan. 【线索】
""", """
伦敦读一年硕士，总共大约 £45,000–£60,000，主要看专业 💷 欢迎微信私信 GlostudyUK，我们按你的情况帮你算。【线索】
""")
cust("4", r"英国留学值得吗|Is studying in the UK worth it", """
For many students yes: shorter degrees, world-class universities and a Graduate visa afterwards. It depends on your goals, happy to talk it through anytime 🇬🇧
""", """
对很多同学来说值得：学制短、名校多、毕业后还有工作签证。具体看你的目标，随时欢迎来聊 🇬🇧
""")
cust("4", r"你们收钱不办事|You took my money and did nothing", """
We're sorry to hear this and want to look into it properly. Please message us on WeChat with your details, a consultant will contact you today. 【转人工】
""", """
很抱歉给您带来不好的体验，我们一定认真处理。请微信私信我们您的信息，顾问今天会联系您。【转人工】
""")
cust("1", r"lily_mama_12", """
Thank you, Ms Chen! 12 is a great age to plan for 13+ entry. I've noted everything and a consultant will add you on WeChat.

【咨询登记】
Who: parent (Ms Chen)
Student: 12, from Xiaohongshu comment
Wants: UK boarding school, from next September
Budget: about ¥400,000 a year
Name / contact: Ms Chen / WeChat lily_mama_12
Notes: agreed to use these details to arrange a consultation
【登记完成】
""", """
谢谢陈女士！12 岁正好可以规划 13+ 入学。信息都记下了，顾问会加您微信。

【咨询登记】
身份：家长（陈女士）
学生年龄/年级：12 岁（来自小红书评论）
意向阶段/专业：英国寄宿学校，明年 9 月入学
预算：每年约 40 万人民币
称呼/联系方式：陈女士 / 微信 lily_mama_12
备注：同意使用以上信息安排咨询
【登记完成】
""")
cust("1", r"London or Manchester|伦敦还是曼彻斯特", """
Good question! I checked with Bernadette and Leonard: London has more finance jobs nearby but costs about a third more to live in; Manchester's finance master's are excellent and better value. If you'd like, we can compare two or three courses for you in a free consultation.
""", """
好问题！我问了 Bernadette 和 Leonard：伦敦金融实习机会多，但生活费大约贵三分之一；曼彻斯特的金融硕士也很好，性价比更高。需要的话，可以在免费咨询里帮你对比两三个项目。
""")
cust("2", r"lily_mama_12", """
零、一句话总结 / One-line summary: 12-year-old for 13+ boarding entry next September; budget ¥400k fits many good schools.

| School type | Why | Entry |
|---|---|---|
| Co-ed boarding school, South East | Strong pastoral care | Own English & maths test |
| Girls' boarding school | Smaller classes | Test + interview |
| International boarding college | Many international students | English test |
**Next steps:** register by early spring; prepare English and maths tests.
""", """
零、一句话总结：12 岁，明年 9 月 13+ 入读寄宿学校；每年 40 万预算可以选很多好学校。

| 学校类型 | 理由 | 入学 |
|---|---|---|
| 东南部男女混校寄宿 | 生活照顾好 | 学校自己的英语和数学测试 |
| 女子寄宿学校 | 小班教学 | 测试 + 面试 |
| 国际寄宿学院 | 国际生多 | 英语测试 |
**下一步：** 春季前报名；准备英语和数学测试。
""")

# ---------- the team's daily work ----------
cust("4", r"Daily task: draft one WeChat Moments post|每日任务：写一条本周", """
【简要】Today's Moments post is ready for your approval: a calm reminder that UK visa money rules change on 30 November.
【完整报告】
【朋友圈预览】
提醒正在准备英国留学的家庭：11 月 30 日起，学生签证需要证明的生活费上调，伦敦每月 £1,570，其他城市 £1,203。提前准备资金证明，申请更从容 🇬🇧
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：london
【/朋友圈预览】
**Fact-check:** amounts from GOV.UK news (30 Nov 2026), needs final check on GOV.UK.
""", """
【简要】今天的朋友圈已写好，等您批准：平和地提醒家长 11 月 30 日起签证资金要求上调。
【完整报告】
【朋友圈预览】
提醒正在准备英国留学的家庭：11 月 30 日起，学生签证需要证明的生活费上调，伦敦每月 £1,570，其他城市 £1,203。提前准备资金证明，申请更从容 🇬🇧
第一次咨询免费，加微信 GlostudyUK 聊一聊。
图片：london
【/朋友圈预览】
**事实核对：** 金额来自 GOV.UK 新闻（2026 年 11 月 30 日），发布前再核对一次。
""")
cust("6", r"Weekly task: check our cost sheet|每周任务：根据最新资讯核对费用表", """
Cost sheet check:
- Visa money to show: update to £1,570/month London and £1,203 elsewhere for applications from 30 Nov 2026.
- Visa fee £558 and health surcharge £776/year: unchanged.
- Tuition ranges: still current for 2027 entry.
- Needs your decision: update the sheet now, or wait for GOV.UK's final page?
""", """
费用表核对：
- 签证资金：2026 年 11 月 30 日起，伦敦改为每月 £1,570，其他地区 £1,203。
- 签证费 £558、医疗附加费每年 £776：不变。
- 学费区间：2027 年入学仍然适用。
- 需要您决定：现在更新，还是等 GOV.UK 正式页面？
""")
cust("3", r"Prepare a short document checklist|准备一份简短的材料清单", """
Document checklist for the consultation:
1. Passport copy (student)
2. Latest school transcripts, translated
3. English test result (or test date)
4. Short list of interests and activities
5. Budget the family is comfortable with
Amy will send it to the client before the call.
""", """
咨询材料清单：
1. 学生护照复印件
2. 最近的成绩单（附翻译）
3. 英语成绩（或考试日期）
4. 兴趣和活动简要列表
5. 家庭能接受的预算
Amy 会在咨询前发给客户。
""")

# ---------- AI expert check before a reply is posted ----------
for _b in ["2", "3", "5", "6", "17", "22"]:
    cust(_b, r"Quality check before publishing|发布前质量检查", "【通过】 Accurate, polite and on-brand.", "【通过】 内容准确、礼貌，符合品牌调性。")

# ---------- the new officers' own desk questions ----------
def desk(bot, match, en, zh): cust(bot, match, en, zh)
desk("7", r"foundation year and A-levels|预科和 A-Level", "【简要】A foundation year is one year and leads to one university; A-levels take two years and open every UK university. For a strong student with time, A-levels give more choice.", "【简要】预科一年，通常只对应一所大学；A-Level 两年，可以申请所有英国大学。成绩好、时间够的学生选 A-Level 更灵活。")
desk("8", r"How many comments came in today|今天来了多少条评论", "Today so far: 5 comments. 3 from Xiaohongshu went up to Emily, 1 from Douyin to Mindy, 1 from WeChat to Gabriel. 2 people wanted advice, so I brought them down to the leads bench for Monica.", "今天目前 5 条评论：小红书 3 条交给 Emily，抖音 1 条交给 Mindy，公众号 1 条交给 Gabriel。有 2 位想咨询，我已带到线索长椅交给莫妮卡。")
desk("9", r"consult room schedule|咨询室的安排", "Tomorrow: Room A 10:00 Mrs Wang (A-levels), 14:00 Ms Chen (boarding, 12). Room B 11:00 Mr Chen (finance master's). Reminders go out tonight at 20:00.", "明天：A 室 10:00 王女士（A-Level），14:00 陈女士（寄宿，12 岁）；B 室 11:00 陈先生（金融硕士）。今晚 20:00 发提醒。")
desk("10", r"upset that nobody replied|不满昨天没人回复", "I'm really sorry we kept you waiting yesterday, that's not the service we want to give. I've asked a consultant to call you today, and I'll stay with your case until it's sorted. 【转人工】", "非常抱歉昨天让您久等了，这不是我们想提供的服务。我已请顾问今天给您回电，我会一直跟进直到解决。【转人工】")
desk("11", r"talking points for tomorrow|准备谈话要点", "Talking points for Mr Chen:\n1. Budget ¥450k fits Manchester, Leeds, Bristol; KCL is a stretch.\n2. IELTS 6.5: check if Manchester needs 7.0.\n3. Ask about work experience: it strengthens finance applications.", "陈先生谈话要点：\n1. 45 万预算适合曼大、利兹、布里斯托，KCL 是冲刺。\n2. 雅思 6.5：确认曼大是否要求 7.0。\n3. 问工作经历，对金融申请加分。")
desk("12", r"UCL is ranked 9th|UCL 世界排名第 9", "Needs a fix: always name the list and year, e.g. \"QS World University Rankings 2026\". Check the exact number on the QS website before posting; rankings change every year.", "需要修改：必须写明榜单和年份，例如“QS 2026 世界大学排名”。发布前到 QS 官网核对具体名次，排名每年都会变。")
desk("13", r"key UCAS and application deadlines|重要的 UCAS 和申请截止日期", "Next 3 months:\n- 14 Jan: UCAS main deadline (most undergraduate courses)\n- Jan–Mar: university offers arrive\n- Feb: IELTS booking for summer sessions\n- Rolling: many master's courses fill by March\nCheck UCAS for exact dates.", "未来 3 个月：\n- 1 月 14 日：UCAS 主截止（大多数本科）\n- 1–3 月：陆续收到 offer\n- 2 月：预约夏季雅思\n- 滚动录取：很多硕士 3 月前满额\n具体日期以 UCAS 为准。")
desk("14", r"How many clients are on the board|客户名单上有多少人", "The board has every booked client, filed with their summary. Anything waiting for your review is marked \"to review\"; no personal details leave the office.", "客户名单上有每位已登记客户的资料摘要。待您审核的标为“待审核”，个人信息不会外传。")
desk("15", r"Douyin script: 3 myths|抖音口播：关于英国留学的 3 个误区", "【简要】Here's a 45-second Douyin script busting 3 UK study myths.\n【完整报告】\n| Sec | Scene | Voice |\n|---|---|---|\n| 0–3 | Close-up | \"3 things people get wrong about studying in the UK!\" |\n| 3–15 | London street | \"Myth 1: only rich families can go. Many cities cost much less than London.\" |\n| 15–30 | Campus | \"Myth 2: a 1-year master's is 'less'. It's full-time and intense.\" |\n| 30–42 | Library | \"Myth 3: you need perfect English. Many students start at IELTS 6.0.\" |\n| 42–45 | Logo card | \"First consultation free, add GlostudyUK on WeChat.\" |", "【简要】一条 45 秒抖音口播：英国留学的 3 个误区。\n【完整报告】\n| 秒 | 画面 | 口播 |\n|---|---|---|\n| 0–3 | 特写 | “关于英国留学，90% 的人都想错了这 3 点！” |\n| 3–15 | 伦敦街头 | “误区一：只有有钱人才能去。其实很多城市比伦敦便宜得多。” |\n| 15–30 | 校园 | “误区二：一年制硕士含金量低。其实是全日制、强度很高。” |\n| 30–42 | 图书馆 | “误区三：英语要很好。很多同学雅思 6.0 起步。” |\n| 42–45 | 品牌卡 | “第一次咨询免费，加微信 GlostudyUK。” |")
desk("16", r"article about choosing a UK city|怎么选英国城市", "Outline: \"London, Manchester or Edinburgh? How to choose\"\n1. Start from the course, not the city\n2. Living costs compared (Bernadette's figures)\n3. Student life and safety\n4. Jobs and internships nearby\n5. FAQ + free consultation", "提纲：《伦敦、曼城还是爱丁堡？怎么选》\n1. 先看专业，再看城市\n2. 生活费对比（Bernadette 提供数据）\n3. 学生生活与安全\n4. 周边实习与工作机会\n5. 常见问题 + 免费咨询")
desk("17", r"social team post this week|社媒团队本周发了什么", "This week: Emily posted 2 Xiaohongshu notes, Gabriel 1 Moments post, Mindy 1 Douyin video. I passed 6 everyday comment replies; 2 replies about money and today's post are waiting on your desk.", "本周：Emily 发了 2 篇小红书，Gabriel 1 条朋友圈，Mindy 1 条抖音。我审核通过了 6 条普通评论回复；2 条涉及费用的回复和今天的帖子在您桌上等待批准。")
desk("18", r"cover for a Xiaohongshu post about London living costs|伦敦生活费的小红书设计封面", "Cover: London street at dusk with a red bus; big white title \"伦敦一个月要花多少？\"; red tag \"真实账单\"; Glostudy gold logo bottom-left; 3:4 format.", "封面：傍晚伦敦街头和红色巴士；白色大标题“伦敦一个月要花多少？”；红色小标签“真实账单”；左下角寰学金色标志；3:4 比例。")
desk("20", r"voice-over for a video tour|校园视频写一段 30 秒配音稿", "Voice-over (30s): \"Morning light on old stone walls... this is where your next chapter starts. Small classes, big ideas, friends from everywhere. Curious what it's really like? Ask us anything, the first chat is free.\"", "配音稿（30 秒）：“清晨的阳光洒在古老的石墙上……你的新篇章就从这里开始。小班课堂、大大的想法、来自世界各地的朋友。想知道真实的样子？随时问我们，第一次咨询免费。”")
desk("21", r"customers worried about this week|这周客户最担心什么", "This week customers mostly worry about cost (40%), choosing the right school (30%) and timing (20%). One upset comment needed care. Tip: Emily's next post could explain living costs city by city.", "本周客户最担心：费用（40%）、选对学校（30%）、时间安排（20%）。有 1 条不满评论需要小心处理。建议：Emily 下一篇帖子可以按城市讲生活费。")
desk("22", r"red lines for public posts|公开发帖的红线", "Our red lines: no guaranteed offers, no \"last places\" pressure, no Glostudy fee quotes, no client names or photos without written consent, no attacks on other agencies, rankings always with list and year.", "我们的红线：不保证录取、不制造名额紧张、不报寰学价格、未经书面同意不用客户姓名和照片、不攻击其他机构、排名必须注明榜单和年份。")
cust("22", r"Quality check before publishing Emily's post|发布前质量检查：Emily 的帖子", "【通过】 No promises, no fee quotes, no private details.", "【通过】 无承诺、无报价、无隐私信息。")

A[:0] = [x for x in C if x not in A]
ROUTES = [
  {"bot": "8", "match": r"How many comments came in today|今天来了多少条评论", "calls": [{"who": "emily", "task": "Xiaohongshu comments today"}, {"who": "mindy", "task": "Douyin comments today"}, {"who": "gabriel", "task": "WeChat post comments today"}]},
  {"bot": "9", "match": r"consult room schedule|咨询室的安排", "calls": [{"who": "raj", "task": "Clients' deadlines this week"}, {"who": "howard", "task": "Booked client records"}]},
  {"bot": "11", "match": r"talking points for tomorrow|准备谈话要点", "calls": [{"who": "leonard", "task": "Mr Chen's shortlist"}, {"who": "bernadette", "task": "Mr Chen's budget check"}]},
  {"bot": "17", "match": r"social team post this week|社媒团队本周发了什么", "calls": [{"who": "emily", "task": "Posts this week"}, {"who": "kuuga", "task": "What's waiting for approval"}]},
  {"bot": "6", "match": r"master's in London|伦敦读一年硕士", "calls": [{"who": "leonard", "task": "Typical London master's courses"}, {"who": "sheldon", "task": "Check the visa money figures"}]},
  {"bot": "4", "match": r"boarding|寄宿", "calls": [{"who": "sheldon", "task": "Check 13+ entry facts"}, {"who": "julien", "task": "Cover idea"}]},
  {"bot": "21", "match": r"customers worried|客户最担心", "calls": [{"who": "monica", "task": "Common WeChat questions"}, {"who": "joey", "task": "Comment themes"}]},
  {"bot": "12", "match": r"UCL is ranked|UCL 世界排名", "calls": [{"who": "leonard", "task": "Ranking source"}]},
  {"bot": "1", "match": r"孩子12岁，现在准备来得及吗|My child is 12, is it too late", "calls": [{"who": "scout", "task": "Is 12 too late for UK boarding?"}, {"who": "raj", "task": "13+ entry timeline"}]},
  {"bot": "1", "match": r"伦敦读硕士一年大概多少钱|How much is a one-year master's in London", "calls": [{"who": "penny", "task": "One-year London master's cost range"}]},
  {"bot": "1", "match": r"英国留学值得吗|Is studying in the UK worth it", "calls": [{"who": "sheldon", "task": "Graduate visa and degree length facts"}, {"who": "penny", "task": "Cost vs other countries"}]},
  {"bot": "1", "match": r"lily_mama_12", "calls": [{"who": "scout", "task": "Boarding schools for 13+ entry"}]},
  {"bot": "1", "match": r"London or Manchester|伦敦还是曼彻斯特", "calls": [{"who": "penny", "task": "London vs Manchester costs"}, {"who": "scout", "task": "Finance master's in both cities"}]},
  {"bot": "1", "match": r"A-Level for my daughter|女儿去英国读A-Level", "calls": [{"who": "scout", "task": "A-level route and schools for a 16-year-old"}, {"who": "raj", "task": "A-level start dates"}]},
  {"bot": "1", "match": r"guarantee him a place at Oxford|保证他上牛津", "calls": [{"who": "sheldon", "task": "Oxford entry facts"}, {"who": "scout", "task": "Realistic alternatives"}]},
  {"bot": "1", "match": r"write my personal statement for me|帮我写个人陈述", "calls": [{"who": "quill", "task": "Can we coach a psychology statement?"}]},
  {"bot": "1", "match": r"improve my own draft|改我自己写的初稿", "calls": [{"who": "quill", "task": "Draft feedback process and timeline"}]},
  {"bot": "1", "match": r"28 and work in finance|28岁，在深圳", "calls": [{"who": "penny", "task": "Total cost of a one-year UK master's"}, {"who": "scout", "task": "Finance master's options by city"}]},
  {"bot": "1", "match": r"London much more expensive|伦敦是不是比其他城市贵", "calls": [{"who": "penny", "task": "London vs other cities living costs"}]},
  {"bot": "1", "match": r"How much does it cost to study|cost of studying|去英国留学一年大概要多少钱|留学.*多少钱", "calls": [{"who": "penny", "task": "Rough yearly costs for UK study"}, {"who": "scout", "task": "Typical tuition ranges by city"}]},
  {"bot": "5", "match": r"medicine|医学", "calls": [{"who": "scout", "task": "Medical school shortlist and entry route"}, {"who": "penny", "task": "Cost check for ¥600k a year"}, {"who": "quill", "task": "Interview and statement prep points"}]},
]
NOTES = {
  "bernadette": {"en": "- Tuition £20k–£40k a year by city\n- Living £12k–£22k\n- Visa funds up from 30 Nov", "zh": "- 学费每年 £2–4 万，看城市\n- 生活费 £1.2–2.2 万\n- 11 月 30 日起签证资金上调"},
  "leonard": {"en": "- Options checked on university websites\n- Entry requirements vary by course", "zh": "- 已核对各校官网\n- 不同专业录取要求不同"},
  "sheldon": {"en": "- Facts checked against university websites\n- Rankings quoted with list and year", "zh": "- 已对照大学官网核实\n- 排名注明榜单和年份"},
  "raj": {"en": "- Key deadline: 14 Jan (UCAS main), 15 Oct (Oxbridge/medicine)\n- Start preparing 12 months ahead", "zh": "- 关键日期：1 月 14 日（UCAS 主截止）、10 月 15 日（牛剑/医学）\n- 建议提前 12 个月准备"},
  "mindy": {"en": "- 1 Douyin comment today, a question", "zh": "- 今天抖音 1 条评论，是提问"},
  "gabriel": {"en": "- 1 WeChat comment today, about costs", "zh": "- 今天公众号 1 条评论，问费用"},
  "kuuga": {"en": "- 1 post and 2 replies waiting for the CEO", "zh": "- 1 篇帖子和 2 条回复等待 CEO 批准"},
  "julien": {"en": "- Cover: campus photo, bold title", "zh": "- 封面：校园照片 + 大标题"},
  "howard": {"en": "- 3 booked clients on file", "zh": "- 3 位已登记客户已归档"},
  "joey": {"en": "- Most comments ask about cost", "zh": "- 大部分评论问费用"},
  "amy": {"en": "- Coaching yes, ghostwriting no\n- Plan → draft → feedback, 2–3 rounds", "zh": "- 可以辅导，不能代写\n- 提纲 → 初稿 → 修改，2–3 轮"},
  "monica": {"en": "- FAQ wording ready", "zh": "- 常见问题话术已准备"},
  "emily": {"en": "- Post idea ready", "zh": "- 选题已准备"},
}
FALLBACK = {
  "en": "This is a demo with prepared answers, so I can only answer the suggested questions. Tap one of them, or connect DeepSeek in Settings to ask me anything.",
  "zh": "这是演示版，只能回答预设的问题。请点选建议的问题，或在设置里接入 DeepSeek，就可以随便问了。"
}
out = {"answers": A, "routes": ROUTES, "notes": NOTES, "fallback": FALLBACK}
json.dump(out, open(os.path.join(os.path.dirname(__file__), "script.json"), "w"), ensure_ascii=False, indent=1)
print(len(A), "answers")
