# AI 人物设计 Skill（juese-sheji）

> 你没说出来的部分，模型替你做主。

给 AI 短片、AI 漫剧、生图 / 生视频做人物前期设计的 Agent Skill，[Claude Code](https://claude.com/claude-code)、Codex、claude.ai 都能用。

你手上通常只有一个**模糊的感觉**：「一个轻佻的男性」「一个温柔的大块头」「一个老年人」「民国的教书先生」。这个 skill 帮你把它 **articulate** 出来：拆成脸、发型、配饰、服装、体态、生活痕迹、微表情、说话方式、精神状态九个维度，每个维度写成模型能直接执行的**名词和动作**；用**刚柔光谱**查各部位统不统一、反差落在哪；给这个人写一套**不夸张的表情谱**，专治 AI 味最重的「表演脸」；最后交付成能直接粘进 prompt 的锁定段。

人物前期的其余部分也在里面：122 张影视人物原型卡、47 种服装风格和 30 多个时代 / 类型世界的风格库、服化道总表和连戏表、群像拉开、出图后的漂移检查和评测。形容词是请模型猜，名词是给模型下单。

[English summary](#english)

---

## 它解决什么问题

描述人物时，大家手上通常只有一个形容词。把形容词直接写进 prompt，模型会在每个你没说清的维度上取**众数**：一张磨过皮、五官标准、左右对称的 AI 平均脸，一身电商爆款。

问题不在模型，在于这个人还停在你脑子里的一个感觉，没有被 **articulate** 出来。这个 skill 做的就是这一步：顺着维度一项项问、一项项写，把「轻佻」「清冷」「苦相」「温柔的大块头」这种说不清的感觉，变成发型名、款式名、材质、穿法、肌肉动作。拿不准的地方给出备选，告诉你「换成它会变成什么样」，让你在挑的过程里把感觉对准。

> **你能把要求说到多细，就能控制到多细；没说出来的维度，模型全部用默认值替你填。形容词是请模型猜，名词是给模型下单。**

同一个起点，两种写法：

**直接写形容词**

```
A frivolous, flirtatious young East Asian man.
```

**经过这个 skill 具体化**（节选，完整版见 [`examples/轻佻的男性.md`](juese-sheji/examples/轻佻的男性.md)）

| 维度 | 层 | 选定写法 | 备选（换成它会变成什么样） |
|---|---|---|---|
| 发型 | 造型 | 中分帘发，长到下巴，深棕，发尾微卷，湿发感，右侧一缕刘海总挂到眉尾 | ① 侧分油头、梳齿痕清楚（→ 老派的花花公子）② 狼尾挑染一缕灰（→ 乐队气、更野） |
| 配饰 | 身份 / 造型 | 一颗黑珍珠单颗吊坠穿在细的做旧银链上，从解开的衬衫领口露出来；右手食指做旧银图章戒 | ① 巴洛克式粗锁链金项链（→ 更张扬、港风）② 左耳一只银色小圈耳环（→ 更痞、更年轻） |
| 上装 | 造型 | 黑底小白花古巴领人造丝短袖衬衫，解到第三颗扣子，前塞后不塞 | ① 白色亚麻衬衫袖子挽到小臂（→ 度假浪子） |
| 静态姿态 | 身份（习惯） | 重心压在左腿，胯微歪，右手插裤兜，头向左微歪，下巴略抬 | ① 靠墙、肩膀抵着墙（→ 在看戏） |
| 生活痕迹 | 身份 | 调酒师：右手食指侧面被吧勺磨出的薄茧；左手背两道玻璃划过的浅白细疤 | |

```
A 28-year-old East Asian man, 7.5 heads tall, slim with narrow shoulders and long fingers.
Narrow long face, clean jawline, low cheekbones. Straight brows; peach-blossom eyes with
inner double lids and slightly downturned outer corners; mouth corners naturally upturned.
Center-parted chin-length curtain hair, dark brown, slightly wavy ends, wet-look wax, one
strand falling over the right brow tail. A single black pearl pendant on a thin oxidized
silver chain, visible at the open collar … Black short-sleeved Cuban-collar rayon shirt with
a small off-white floral print, unbuttoned to the third button, front tucked in and back
left out … Weight on the left leg, hip cocked, right hand in trouser pocket, head tilted
slightly left. Keep all of the above identical in every shot.
```

整篇没有一个「轻佻」：轻佻被拆到了发型、穿法、戴法、姿态和说话方式里。每一行都是一个可以单独拧的旋钮：出图不对时只换一行，就知道是哪一项的问题。

**再看一个有反差的人：「温柔的大块头」**（完整版见 [`examples/温柔的大块头.md`](juese-sheji/examples/温柔的大块头.md)）

反差感也能拆。这个 skill 把每个部位放到一条**刚柔光谱**上（常说的男性气质 ↔ 女性气质，但和性别无关）：骨架、脸、眼睛是**底色**，改不了；衣服是**推向**，可以往刚推，也可以往柔推；姿态和说话是**习惯**。

| 层 | 刚柔（1 柔 – 5 刚） | 落在哪里 |
|---|---|---|
| 底色 | 5，只有眼睛是 2 | 185cm、约 100kg，肩宽、斜方肌隆起，方下颌、手大指节粗、摔跤留下的饺子耳；眼睛却是眼梢微垂、黑眼珠大、有卧蚕 |
| 推向 | 往柔推到 2 | 燕麦色粗针落肩开衫只扣中间两颗木扣，雾蓝圆领旧棉 T，奶咖灯芯绒裤，米白旧德训鞋；低对比，身上没有金属、没有尖角 |
| 习惯 | 1–2 | 含胸，和人说话先蹲下，手永远放在对方看得见的地方，语速慢、声音压小 |
| 反向的那一处 | | 整套柔软的衣服里，留着饺子耳和一双指节粗大、带猫抓痕的手 |

读出来是「怕吓到别人的大块头」。这就是一个具体的人，不是「gentle giant」这个词在模型那里的平均画面。

**表情也一样，而且更容易出 AI 味**

模型的表情普遍偏夸张：写「开心」就露两排牙，写「惊讶」就张成 O 形嘴，写「难过」就挂眼泪。真实的人和好的表演，大多数时候表情都很小。所以这个 skill 给每个人写一套**表情谱**：同样是开心，在不同的人脸上不是同一张脸。每个表情都写成肌肉动作 + 强度级 + **不动的部位**：

| 表情 | 直接写情绪名 | 大山的表情谱（强度上限 B） |
|---|---|---|
| 开心 | `He is happy.` → 咧嘴大笑、露两排牙 | 先低一下头；眼睛眯起来、卧蚕鼓起，嘴角微微提起；**嘴唇合着，不露牙** |
| 悲伤 | `He is sad.` → 皱成一团、挂眼泪 | 眼眶微红、眼睛湿；嘴唇抿紧，下巴往里收；**眉毛几乎不动，五官不皱成一团** |
| 惊讶 | `He is surprised.` → O 形嘴、眉毛顶到发际线 | 眉毛微抬，眼睛睁开一点，身体先往后让半步；**嘴合着** |

## 适合谁

- **做 AI 短片、AI 漫剧的人**：要让同一个角色在每个镜头里长得一样、穿得一样，还要有辨识度，而不是一张 AI 平均脸。
- **用 AI 出角色图的设计师和编剧**：脑子里有一个人物，但说不清他具体长什么样、该穿什么。
- **写 prompt 写到瓶颈的人**：想知道「形容词为什么不管用」，以及怎么把感觉翻译成模型听得懂的描述。

不需要会画画，也不需要懂服装。装上之后用中文说出你想要的人就行；产出的锁定段是英文，可以直接粘进任何生图 / 生视频模型。

## 能做什么

五个模式，可以单独用，也可以连着用（最常见：E → B → C → A）：

| 模式 | 干什么 | 你可以这样说 |
|---|---|---|
| **E 具体化**（入口） | 模糊感觉 / 一类人 / 一种风格 → 九个维度的精细描述：每个维度一个选定写法 + 2–3 个备选；刚柔定位；表情谱；生活痕迹和不完美；形容词残留检查；输出**生图锁定段**（主设定 + 特写细节）、**视频动作段**、**表演说明**、**说话方式参考**、**表情谱**五段 | 「把『一个轻佻的男性』写具体」「一个温柔的大块头长什么样」「设计一个有绅士感的中年律师」 |
| **D 人物原型** | 122 张影视经典人物原型卡（家庭、校园、职场、犯罪、底层、动作、奇幻科幻恐怖、爱情、东亚与短剧、喜剧配角，外加慎用清单），按「原型 + 一处具体 + 一处反转」本土化 | 「给我一个霸道总裁那种人，但别那么俗」「配角 / 群演怎么设计」 |
| **B 创意风暴** | 用反差、物件叙事、时间痕迹、色彩隐喻等方法发散 4–6 个真正不同的造型方向，再收敛推荐 | 「这个角色穿什么好，给我几个方向」 |
| **C 设计落地** | 把剧本 / 分镜拆成造型卡（Look）、妆发卡、道具卡、场次 × 角色总表和连戏表，写成每个镜头都能拼的锁定段 | 「出服化道表」「做连戏」 |
| **A 检验** | 六个维度打分：时代与环境、身份与处境、性格与弧光、记忆点、可生成性、具体化程度；时代考据不确定就联网查；拿到生成的图后按**漂移清单**逐项审 | 「看看这身对不对」「有没有穿帮」「这张图哪里不像」 |

### 几个关键设计

- **九个维度词库**（[`references/dimensions/`](juese-sheji/references/dimensions/)）：脸与五官、发型、配饰（材质 × 款式 × 戴法）、服装（款式、面料组织、褶、穿法、做旧）、身体与姿态、**生活痕迹**、**微表情**（按 FACS 面部动作单元写，带幅度和时长）、说话方式、**精神状态**。每一项都给中文写法、英文写法和**可见距离**（全景 / 中景 / 特写可见）。
- **表情谱 + 防夸张补丁**（[`references/expression-restraint.md`](juese-sheji/references/expression-restraint.md)）：每个人写自己的表达方式（外放还是压着、强度上限、压不住时哪里先露馅）、默认表情、六个基础情绪和 1–2 个专属表情。按 FACS 的 A–E 强度分级，写实默认只到 A–B；每个表情写出不动的部位；换词表把 `big smile` `crying` `shocked` 换成小一号的肌肉写法；现成的写实影像收尾句；审图时的夸张征兆（露两排牙、O 形嘴、挂眼泪、全脸同时动、做表情时换了脸）和按顺序的修法。
- **精神状态**（[`09-精神状态.md`](juese-sheji/references/dimensions/09-精神状态.md)）：疲惫、焦虑、低落、哭过、亢奋、紧绷、麻木、松弛、病中、宿醉，分轻 / 中 / 重三档，落到眼周、气色、头发、衣服打理、姿态和说话，不写状态名。属于状态层，写进镜头和连戏表；有弧光的主角可以出一张状态板。
- **精细程度跟模型和景别走**：表现力一般的模型会把脸上的细节吞掉，全景镜头里老茧和痣本来就看不见。「一般」只写全景、中景可见的；「深入」再加一段只在特写镜头拼进去的特写细节。
- **身份 / 造型 / 状态三层**：骨相、痣、饺子耳、常年的老茧是身份，跨场不变；衣服、发型的打理是造型，可以换；淋湿、受伤、疲惫是状态，只写进生效的镜头。换装时只换造型层。
- **生活痕迹**：拳击手的饺子耳、农民虎口的老茧、外卖骑手手腕上一圈晒痕、健身的人脸颊脂肪少而体态挺。一句台词不说，观众已经知道这个人过的是什么日子。
- **风格库**（[`references/styles/`](juese-sheji/references/styles/)），三块叠着用：
  - **服装风格**（47 个，一个人*选择*怎么穿）：绅装、知识分子风、cityboy、老钱、工装、阿美咔叽、哥特、Y2K、Hedi Slimane……，带经典单品、配色 HEX、要当心的地方和风格档案。
  - **时代与类型**（30 多个，时代和故事世界*替人决定*怎么穿）：民国、五六十年代、八十年代、九十年代港风；1920s–1980s 欧美；嘻哈、机车、西部牛仔、杀马特、精神小伙、JK / DK；军警、空乘、保安、流水线、消防；武侠古装（按唐宋明分开写）、港片江湖、黑色电影、赛博朋克、蒸汽朋克、太空科幻、中世纪奇幻。每条都有「容易出错」（常见的时代穿帮和 AI 默认值）和「写给模型」的英文关键词。
  - **人群与身份**（生活观察）：城市老年人：鞋面落了一层灰的黑色老布鞋、凹了的不锈钢保温杯、老花镜插在衬衫口袋、双手背在身后走路；还有外卖骑手、老派教授、菜市场摊主、全职妈妈、小镇青年等 20 多类人。
- **刚柔光谱**（[`references/soft-hard-axis.md`](juese-sheji/references/soft-hard-axis.md)）：把肩线（落肩 / 垫肩）、眼梢（下垂 / 上扬）、眼的温润感、骨架大小、脸部棱角、面料（垂坠 / 挺括）、配色对比、姿态占不占空间等几十项，放到同一条刚 ↔ 柔光谱上，分底色、推向、习惯三层。用来查各维度统不统一，说清反差落在哪里（温柔的大块头、穿垫肩西装硬撑的娃娃脸），写弧光（黑化往刚、卸下防备往柔），也用来拉开群像。和性别脱钩，不默认女柔男硬。
- **群像拉开**：多个主要角色同场时，按剪影、主色、发型轮廓、标志性单品、材质、姿态、说话、刚柔位置八个轴两两比较（至少 4 轴不同，剪影和主色必须不同），做远景测试和黑白测试，放进「冷暖 × 复杂度」视觉领地，再用一处共同点表达关系。观众分得清谁是谁，模型也不容易把两个人画串。
- **漂移清单 + 评测**：出图后逐项看哪些写了的东西被模型改回了平均值、怎么修；[`evals/`](juese-sheji/evals/) 带 6 个现成用例，对比「直接写形容词」和「具体化」，测每个模型能保住哪一层细节、会把表情放大几级，结果记进模型能力笔记。

## 安装

**Claude Code**（推荐）：

```bash
git clone https://github.com/MatsuriMW/ai-character-design-skill.git
cd ai-character-design-skill
./install.sh                 # 装到 ~/.claude/skills，所有项目都能用
```

```bash
./install.sh ~/my-film-project   # 只装到某个项目：<项目>/.claude/skills
```

```bash
./install.sh --codex         # Codex：~/.codex/skills
```

或者手动把 `juese-sheji/` 文件夹复制到 `~/.claude/skills/`（或项目的 `.claude/skills/`）。装好后重开 Claude Code 会话。

**claude.ai**：在[最新的 Release](https://github.com/MatsuriMW/ai-character-design-skill/releases/latest) 下载 `juese-sheji.zip`，到 设置 → Capabilities → Skills 上传。

**SkillHub / 其他要求 SKILL.md 在 zip 根目录的平台**：同一个 Release 里下载 `juese-sheji-skillhub.zip`。也可以直接在 [SkillHub](https://skillhub.cn/skills/user_1e879f9b/juese-sheji) 安装。每次更新都会自动发一个新版本，下载[最新的 Release](https://github.com/MatsuriMW/ai-character-design-skill/releases/latest) 就行，说明里写着这一版改了什么。

不需要装任何依赖。只有 `scripts/sync-styles.py`（换成你自己的风格库时用）需要 Python 3。

## 怎么用

装好以后直接说人话，skill 会按你说的内容自己选模式：

- 「帮我把『一个轻佻的男性』写具体，用深入档」
- 「设计一个 73 岁的退休机修工，要有生活感」
- 「我要一个有绅士感的律师，参考绅装里的乡绅」
- 「民国上海的一个教书先生」「八十年代的一个轻佻青年」「赛博朋克世界里的廉价义体雇佣兵」
- 「一个清冷的女生，只出全景，用一般档」
- 「这是我的剧本（贴进来），帮我把三个主角都具体化，再出服化道表和连戏」
- 「这三个主角怎么拉开，别让观众分不清」
- 「这几张是生成出来的图，按漂移清单帮我看哪里不像」
- 「给他写一套表情谱，别做得太夸张」「这张表情图 AI 味太重，帮我看看哪里演过了」
- 「她连熬了一周，状态怎么写」「这个主角从意气风发到崩溃，出一张状态板」
- 「把发型换成备选 ②」（只改那一行，版本号加一）

有项目时，产出默认存在 `shorts/<项目>/`（人物精细描述、服化道、检验报告都按版本号迭代，不覆盖旧版）；你的项目有自己的目录结构就按你的来，没有项目就直接在对话里给。

**可以配合的其他 skill**（都是可选的）：
- 上游分镜 / 导演：比如 [DirectorSKILL](https://github.com/wuwangzhang1216/DirectorSKILL)
- 下游角色设定板：比如 [character-sheet](https://github.com/MatsuriMW/aigc-skills-and-agents/tree/main/skills/character-sheet)（直接用这里的锁定段；表情板用这里的表情谱，状态板用精神状态）
- 按模型写生图 / 生视频 prompt：比如 [visual-skills](https://github.com/smixs/visual-skills)

## 目录

```
juese-sheji/
├── SKILL.md                     入口：五个模式的流程
├── references/
│   ├── articulate-rules.md      写法规则（整个 skill 的底层）
│   ├── dimensions/              九个维度词库 + 索引（气质词 → 常用切口）
│   ├── styles/                  风格库：服装风格（生成）+ 时代与类型 + 人群与身份（手写）+ 索引
│   ├── archetypes/              122 张人物原型卡 + 慎用清单
│   ├── soft-hard-axis.md        刚柔光谱（男性气质 ↔ 女性气质）
│   ├── expression-restraint.md  表情防夸张：强度分级、不动的部位、换词表、审图征兆
│   ├── ensemble.md              群像拉开
│   ├── drift-checklist.md       审出图用的漂移清单
│   ├── model-notes.md           各模型能保住 / 吞掉哪些细节（评测后填）
│   ├── review-checklist.md      检验的六个维度
│   ├── design-principles.md     服化道设计原则与中英词表
│   ├── ai-lock.md               锁定段怎么写
│   ├── brainstorm-methods.md    创意风暴的方法库
│   └── archetype-methods.md     原型 → 本土化的方法
├── templates/                   人物精细描述、群像对照表、人物原型、创意风暴、服化道总表、检验报告
├── examples/                    模式 E 的完整示例：轻佻的男性、温柔的大块头（刚柔反差）
├── evals/                       评测流程、6 个用例（含表情防夸张）、记录模板
└── scripts/sync-styles.py       从 Obsidian 风格库生成 服装风格.md
```

## 扩充

这个 skill 的价值主要在词库和参考库，越用越厚：

- **维度词库**：直接往 `references/dimensions/` 对应文件的表格里加行（中文写法、英文、可见距离、带出的感觉）。
- **气质词**：在 `references/dimensions/索引.md` 的「气质词 → 常用切口」加一节。
- **人群与身份**：在 `references/styles/人群与身份.md` 按格式加一类人。
- **时代与类型**：在 `references/styles/时代与类型.md` 按格式加一个时代、圈子、制服或故事世界。
- **服装风格**：用你自己的 Obsidian 风格库生成（每个风格一篇笔记，frontmatter 写 `type: 审美风格`），格式和命令见 [`references/styles/索引.md`](juese-sheji/references/styles/索引.md) 的「用你自己的风格库」：

  ```bash
  python3 juese-sheji/scripts/sync-styles.py "<你的风格文件夹>"
  ```

- **模型能力**：跑一次 [`evals/`](juese-sheji/evals/README.md)，把结果写进 `references/model-notes.md`。欢迎把你的实测结果提 PR。

## 来源与致谢

- 写法规则来自作者的口播稿《你没说出来的部分，模型替你做主》（articulate 与提示词）。
- 微表情按 Ekman & Friesen 的面部动作编码系统（FACS）整理；平均脸的说法参考 Langlois & Roggman (1990)。
- 风格库来自作者在 Obsidian 里整理的风格笔记；品牌只作风格参照，锁定段里一律写款式、不写品牌和 logo。

## License

[MIT](LICENSE) © 马自立（[@MatsuriMW](https://github.com/MatsuriMW)）

---

<a id="english"></a>

## English

**juese-sheji** (角色设计, "character design") is an Agent Skill for Claude Code, Codex and claude.ai that helps you articulate a vague impression of a character ("a flirtatious man", "a gentle giant", "an old man", "someone gentlemanly") into a precise, model-executable description for AI image and video generation.

Core idea: *whatever you leave unsaid, the model fills in with its default — the statistical average.* Adjectives ask the model to guess; nouns place an order. The skill breaks a character into nine dimensions (face, hair, accessories as material × style × way of wearing, clothing, body & posture, **life traces** such as calluses or cauliflower ears, **micro-expressions** written as FACS muscle actions with amplitude and duration, speech, and **mental state** such as exhaustion or anxiety, shown through the eyes, skin, hair, clothes and posture), gives one chosen option plus 2–3 alternatives per dimension, tags each line as identity / look / state, places every feature on a hard ↔ soft spectrum (often called masculine ↔ feminine, but decoupled from gender) to check consistency and design deliberate contrast, marks how close the camera must be to see it, and outputs a ready-to-paste English lock prompt, a video motion prompt, acting notes, speech notes and an **expression set**.

The expression set targets one of the most obvious tells of AI imagery: exaggerated, theatrical faces (two rows of teeth for "happy", an O-shaped mouth for "surprised", tears for "sad"). Each character gets their own resting face, six basic emotions and one or two signature expressions, written as muscle actions with FACS intensity grades (A–B by default for realism), with the features that stay still spelled out, plus a word-swap table, a restraint suffix, and a checklist of exaggeration tells for reviewing results. It plugs into a companion character-sheet skill to produce 3×3 facial-study boards and state boards.

A style library backs it up: 47 fashion aesthetics, 30+ eras / subcultures / uniforms / genre worlds (Republican-era China to 1990s Hong Kong, 1920s–1980s West, hip-hop, bikers, cowboys, uniforms, wuxia by dynasty, film noir, cyberpunk, steampunk, sci-fi, medieval fantasy — each with common anachronisms and English prompt keywords), and everyday observations of 20+ kinds of people.

It also covers the rest of character pre-production for AI short films: 122 film archetype cards, ensemble differentiation (silhouette, key color, hair outline, signature item, material, posture, speech, hard ↔ soft position), costume brainstorming, wardrobe/props/continuity breakdowns, period-accuracy review, a drift checklist for reviewing generated images, and an evaluation kit for measuring which details each model keeps. The content is written in Chinese; lock prompts are in English.

Install: `git clone` this repo and run `./install.sh` (Claude Code, global), `./install.sh <project-dir>` (one project), or `./install.sh --codex`; or upload `juese-sheji.zip` from Releases to claude.ai.
