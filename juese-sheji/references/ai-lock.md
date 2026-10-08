# 锁定段写法与常见翻车

锁定段的作用：同一个 Look / 妆发 / 道具，在几十个镜头的 prompt 里**一字不改**地重复出现，模型才会每次给出同一个东西。

## 写法

结构固定，从大到小、从外到里：

```
WARDROBE LOCK — SS-A (commute):
- Outer: charcoal grey #3A3D42 nylon shell hooded parka, relaxed fit, hip length,
  two-way front zip, two flap pockets at the hem, lived-in wrinkles.
- Top: heather grey #9A9C9E cotton crew-neck sweatshirt, collar visible at the neck.
- Bottom: black #1E1E22 tapered cotton chinos, ankle length, slightly faded at the knees.
- Shoes: off-white #EDEAE2 canvas low-top sneakers, scuffed toes.
- Accessories: black backpack worn on both shoulders; light blue surgical mask
  pulled down to the chin. No visible logos or text on any clothing.
Keep this outfit identical in every shot.
```

规则：
1. **每件一行**，顺序固定：外套 → 上衣 → 下装 → 鞋 → 配饰。漏写的部位模型会自己发挥。
2. **颜色 = 普通词 + HEX**。只写 HEX 模型看不懂，只写普通词会漂。
3. **写数量和位置**：几颗扣子、几个口袋、口罩挂在哪、包背在哪边。配饰最容易丢，要写得最具体。
4. **写状态**：新旧、褶皱、湿不湿。状态变了就是新的锁定段（`SS-A` 状态 2），不要在同一段里写「有时候皱」。
5. **固定加否定**：`No visible logos or text on any clothing.` 除非剧情需要，需要时写成 `printed text "XXX" in white on the chest`。
6. **不写形容词**：cinematic、stylish、high-end、vintage vibe 一律不要，它们只会让模型自由发挥。
7. **同一段在所有镜头里逐字相同**。改了一个词，就当成新版本（`SS-A v2`），总表同步改。

## 拼装顺序

一个镜头的完整 prompt：

```
[镜头描述：景别、机位、构图、动作]
[CHARACTER LOCK — 来自角色设定板或模式 E 生图锁定段的身份层，只取长相部分]
[WARDROBE LOCK — 本场 Look]
[MAKEUP & HAIR LOCK — 本场妆发状态]
[PROP LOCK — 本镜出现的重点道具，最多 2 个]
[场景与光线]
[负面 / 约束]
```

特写镜头可以只拼看得见的部分（脸部特写不拼鞋），但**不要改写**，只删整行。

和角色设定板一起用：设定板里的服装就是这个角色的 Look A。角色换装后，**不要**重做设定板，而是在镜头 prompt 里用新 Look 的锁定段替换服装部分，并加一句 `Same person as the reference image, wearing a different outfit as described below.`

## 常见翻车与对策

| 症状 | 原因 | 对策 |
|---|---|---|
| 衣服上冒出乱码字母、假 logo | 模型默认给衣服加品牌感 | 锁定段加 `No visible logos or text`；面料写纯色，少用 streetwear、brand 之类的词 |
| 配饰时有时无（口罩、围巾、手表） | 配饰写得太含糊或放在最后被截断 | 写清位置和状态；放进 Accessories 行而不是散落在描述里；关键配饰在镜头描述里再提一次 |
| 颜色每个镜头不一样 | 光线描述压过了服装颜色 | 写 HEX；场景光线写成「光的颜色」而不是「画面是橙色的」；色偏大的场景加 `garment colors stay true to the lock` |
| 换了个场景就换了身衣服 | 场景词（office、bedroom）带出默认服装 | 锁定段放在场景描述之前 |
| 层次丢失（只剩外套，内搭不见） | 没写内搭在哪里露出来 | 写明「衬衫领从毛衣领口翻出，袖口露 1cm」 |
| 道具数量不对、变形 | 数量和形状没写，或者道具太复杂 | 写数字；道具简化；特写时单独生成道具再合成 |
| 手里的东西和手指穿插 | 模型的老毛病 | 手持动作写简单（握住杯身、单手拿手机），复杂交互改成剪辑：先拍手、再拍物 |
| 时代穿帮（2022 年的戏出现全面屏以外的东西 / 出现未来感设备） | 模型默认当代或未来 | 锁定段写明年代特征（`2022-era smartphone, plain black case`）；陈设写「不能有」 |
| 妆发状态漂（胡子一镜有一镜没有） | 妆发没有单独的锁定段 | 每个状态一段，逐字重复；胡子写毫米数 |

## 负面提示（按需选，不要整段照抄）

```
logos, brand names, readable text on clothing, extra accessories, missing accessories,
changed outfit, different clothing colors, extra pockets, mismatched shoes,
futuristic devices, anachronistic objects
```
