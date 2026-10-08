# 人物原型：怎么用

原型（stock character / 刻板印象里的经典角色）是**观众脑子里已经有的那张图**。穿羊毛开衫、双手抱胸、脸色发白的金发妻子一出场，观众三秒就知道：这个家有问题，她是被忽视的那个。原型帮你省掉介绍，代价是人物容易显得廉价。

图鉴在 `archetypes/`，先看 `archetypes/索引.md` 找候选，再打开对应分类读整张卡。

## 一条规矩：1 + 1 + 1

**一个原型 + 一处具体 + 一处反转。**

- **原型**：借它让观众秒懂（剪影、配色、姿态）。
- **具体**：一个只属于这个人、这个年代、这个地方的细节（开衫是她妈织的，袖口补过）。
- **反转**：一处和原型对不上的地方，让观众多看一眼（她抱胸不是在防御，是在藏手上的伤 / 在藏偷来的东西）。

主角三样都要有；配角、群演、一场戏的人可以只用原型，越快读懂越好。

## 六种用法

| 用法 | 怎么做 | 例子 |
|---|---|---|
| **直接用** | 原样拿来，给功能性角色 | 警局里的老探长、酒吧里的女招待，一个镜头交代完 |
| **本土化** | 把原型翻译到具体的年代、城市、阶层，换掉每一件单品 | 被忽视的郊区妻子 → 2023 年杭州某新小区的全职太太：燕麦色羊绒开衫、瑜伽裤、站在开放式厨房里看手机上的家长群 |
| **叠加** | 两个原型合成一个人，取 A 的外形、B 的行为 | 绝望的母亲 × 黑色电影侦探 = 自己查案的母亲（《三块广告牌》用的就是这个思路） |
| **错位** | 把原型放进不属于它的类型片或年代 | 黑长直 JK 少女出现在西部片的小镇；霸道总裁在 1983 年的国营厂 |
| **逆行（弧光）** | 角色从一个原型走到另一个，服化道跟着换 | 被忽视的妻子 → 蛇蝎美人；苦命人 → 小丑；赘婿 → 战神 |
| **拆零件** | 只借原型的一两个零件，其他全部重来 | 只要「开衫 + 抱胸」，不要金发、不要郊区 |

## 每张卡里哪些是零件

卡片按 **人 / 服 / 妆发 / 道具 / 姿态 / 场与光** 拆开，每一栏都是可以单独借走的零件。设计时常见的组合：

- 剪影来自「服」，情绪来自「姿态」，阶层来自「道具」。
- 只换「场与光」就能让同一个原型换类型：同一个抱胸的妻子，冷白日光是家庭剧，绿色荧光灯是惊悚片。

## 姿态与小动作词表

原型最容易被忽略的部分是**身体**。同一身衣服，抱胸和叉腰是两个人。写镜头 prompt 时把姿态也锁进去。

| 姿态 | 读出来的意思 | prompt |
|---|---|---|
| 双手抱胸（手掌夹在腋下） | 防御、冷、拒绝 | arms crossed tightly, hands tucked under armpits |
| 抱住自己的手臂 | 不安、自我安慰、被忽视 | hugging her own arms, shoulders drawn in |
| 把开衫 / 外套往身上裹紧 | 冷、想缩起来 | pulling her cardigan tight around herself |
| 缩肩低头 | 自卑、怕被看见 | hunched shoulders, head lowered |
| 站在门框里 / 窗边 | 局外人、旁观 | standing in the doorway, half in shadow |
| 手插口袋、背靠墙 | 漫不经心、冷 | leaning against the wall, hands in pockets |
| 单手插兜站在落地窗前 | 掌控、权力 | one hand in pocket, standing at a floor-to-ceiling window |
| 叉腰 | 强势、挑衅、不耐烦 | hands on hips |
| 双手握拳 / 举拳 | 热血、决心 | clenched fists, fist raised |
| 蹲着（脚跟着地） | 街头、混混、底层 | squatting flat-footed |
| 咬拇指 / 咬指甲 | 焦虑 | biting her thumbnail |
| 双手捂嘴 | 惊恐、不敢哭出声 | both hands pressed over mouth |
| 攥着一张纸 / 手机不放 | 绝望、等消息 | clutching a crumpled flyer to her chest |
| 夹烟不抽 | 疲惫、思考、强撑 | holding an unlit cigarette between fingers |
| 托腮、看窗外 | 走神、渴望别处 | chin in hand, staring out the window |
| 侧身扭头、下巴抬高 | 傲娇、骄傲 | turned away, chin raised, glancing sideways |
| 歪头、甜笑 | 天真或伪装的天真 | head tilted, sweet smile |
| 慢慢转过身 | 揭示、压迫感 | slowly turning to face the camera |
| 并排慢动作走过来 | 团体、权力 | walking side by side in slow motion |
| 弯腰驼背扛东西 | 劳动、负担 | stooped under a heavy woven sack |
| 坐在床边 / 车里不进门 | 逃避、中年的沉默 | sitting alone in the parked car, engine off |

## 用原型时的底线

- 原型借的是**观众的共同记忆**，不是某个演员的脸。参考电影只学方法，不复制具体角色的整套造型。
- 涉及种族、民族、性取向、残障、地域的原型，很多已经是冒犯性的套路。看 `archetypes/11-慎用.md`，要用就重新写，给这个人自己的动机和细节。
- 卡里写的人种、发色是**这个原型在影视里最常见的样子**，不是规定。本土化时大胆换。
