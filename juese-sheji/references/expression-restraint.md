# 表情防夸张

写表情谱、表情板、任何带表情的镜头 prompt 之前读这份。审图时也用它（第 6 节）。

生图 / 生视频模型的表情普遍偏夸张：一笑就露出两排牙，一惊讶就张成 O 形嘴，一难过就五官皱成一团、挂着眼泪。这是 AI 味最重的地方之一，比皮肤磨皮更容易一眼认出来。真实的人、好的表演，大多数时候表情都很小。

## 1. 为什么会夸张

- **情绪名指向峰值**：模型学到的「开心」「惊讶」大多来自图库照片、表情包、演员定妆照、动漫表情设定图，都是情绪最满的那一帧。写一个情绪名，它就给你峰值。
- **全脸同时动**：真实的表情常常只动一个区域（嘴角提了、眼睛没动）。模型给的是教科书式的完整组合：眉、眼、嘴、脸颊一起动，而且左右对称。
- **「表情设定」本身就是夸张的语境**：「expression sheet」「emotions」「expressive」这些词，会把模型带到动漫和卡通的表情设定图上，那里的表情本来就是演给后排观众看的。
- **没说的部位不会自己保持静止**：写了「微笑」没写眼睛，模型就按「笑」的平均值把眼睛也弯起来、眉毛也抬起来。

## 2. 强度分级

按 FACS 的强度分级（A–E），写表情时每一处肌肉动作都标级别：

| 级 | 名称 | 看起来 | 英文写法 | 什么时候用 |
|---|---|---|---|---|
| A | 痕迹 | 不仔细看看不出来，只是比默认脸多一点 | barely / a trace of / almost imperceptibly | 克制的人、压着情绪、写实片的大多数镜头 |
| B | 轻微 | 看得出来，但脸基本还是默认的样子 | slightly / faintly / a little | **写实短片的默认上限** |
| C | 明显 | 一眼看出情绪，但还在日常范围里 | clearly / noticeably | 情绪戏的高点、外放型的人 |
| D | 强烈 | 五官明显变形 | strongly / deeply | 崩溃、狂喜、暴怒这种剧情节点，一部片没几次 |
| E | 极限 | 到头了 | — | 尖叫、嚎哭；写实片基本不用 |

- **写实默认 A–B，最多到 C**。D、E 只给剧情真的到了那一步的镜头，并且要在分镜里写清是哪一镜。
- 半写实、动漫、IP 风格可以整体往上提一级。
- 每个角色有自己的**强度上限**（表情谱里的「表达方式」）：外放的人上限 C，压着的人上限 B，冷的人上限 A。同一句「他笑了」，对三个人是三种强度。
- 模型实际出的会比写的大一到两级：**想要 B 就写 A，想要 C 就写 B**。

## 3. 七条写法

1. **不写情绪名，写肌肉动作 + 强度级**。`smiling` → `the corners of his mouth lift slightly (B), lips stay together`。写法表见 `dimensions/07-微表情.md`。
2. **锚定默认脸**：先说「脸基本保持默认表情」，再说哪里变了。`His face stays close to his resting expression; only the corners of his mouth lift slightly.`
3. **写出不动的部位**。这是最有效的一条。它是对状态的正向描述，不是否定指令：`his eyes stay relaxed` `brows stay level` `lips stay together` `jaw stays loose`。笑写清眼睛怎样，难过写清嘴怎样，惊讶写清嘴怎样。
4. **一次只动一个区域**：上半脸（眉、眼）或下半脸（嘴、下巴）选一个为主。真实的情绪常常是一个区域先露馅，另一个区域在控制。
5. **允许不对称**：`the left corner lifts a little more than the right`。完全对称是假笑和 AI 脸的特征。
6. **嘴的开合和牙齿写死**：A–B 级的笑写 `lips together`，C 级写 `lips slightly parted, upper teeth just visible`。惊讶写 `lips part a few millimetres`，不写 `mouth open`。
7. **换成写实影像的语境**：不用 `expression sheet`、`emotions`、`expressive`、`dramatic`；改用 `subtle facial variations` `like frames from an understated live-action film` `candid documentary still`。说「他在努力保持平静」（`trying to keep a neutral face`）比说「他很难过」小得多，也更有戏。

视频另加三条：

- **写时长和回落**：`holds for about a second, then relaxes back to his resting face`。
- **写速度**：`slowly` 比默认的「瞬间做到位」小。
- **一个镜头一处变化**（`articulate-rules.md` 第 4 节）。

## 4. 换词表

左边的词写进 prompt，模型会给出峰值表情；右边是同一个意思的小一号写法。

| 别写 | 改成 |
|---|---|
| big smile / grinning / beaming / laughing | the corners of the mouth lift slightly, lips together; faint creases at the outer eye corners |
| crying / in tears / sobbing | eyes slightly glossy, the rims a little red; inner brows faintly raised; lips pressed together |
| shocked / astonished / jaw drop | brows lift slightly, eyes open a little wider than resting, lips part a few millimetres |
| terrified / horrified / screaming | eyes open slightly wider, brows faintly drawn together and raised, lips tightened and pulled back a little |
| furious / enraged / snarling | brows drawn down slightly, lips pressed thin, jaw set, masseter tightened |
| disgusted | upper lip lifts faintly on one side, a slight wrinkle at the bridge of the nose |
| happy / sad / angry / surprised（只写情绪名） | 按第 3 节写肌肉动作 + 强度 + 不动的部位 |
| expressive / dramatic / emotional / intense | subtle / understated / restrained, like a film still |
| expression sheet / emotion chart | facial study / subtle facial variations |

## 5. 现成的收尾句

每一格表情、每一个带表情的镜头，在肌肉动作后面接一句（英文直接用）：

```
Subtle, naturalistic expression at low intensity, like a frame from an understated live-action film. The rest of the face stays at his resting expression; facial proportions and features unchanged.
```

（女性角色把 his 换成 her。表情板整张的收尾句见 `templates/人物精细描述.md` 的 ⑤ 表情谱，以及 character-sheet 的表情板模板。）

## 6. 审图：夸张的征兆

出图后逐格看（并入 `drift-checklist.md` 第 4 节），出现任何一条都算夸张：

- 露出上下两排牙；笑的时候牙龈露出来
- 惊讶以外的表情，眉毛整体高抬、额头起横纹
- 眼睛睁圆、上眼睑上方露出眼白
- 眉、眼、嘴、脸颊同时在动；左右完全对称
- 难过就挂眼泪、嘴张开；惊讶就嘴张成 O 形；生气就露牙
- 歪头、手托腮、手捂嘴之类的摆拍动作
- 看起来像表情包、像定妆照、像在对着镜头演
- **脸变了**：做表情时下颌变尖、眼睛变大、换了一个人（表情越大，身份越容易漂）

**怎么修**，按顺序试：

1. 降一级强度（B → A），或者干脆写成「努力保持平静」
2. 补上不动的部位（眼睛、眉毛、嘴分别怎样）
3. 删掉 prompt 里所有情绪名和第 4 节左栏的词
4. 换写实影像语境的收尾句
5. 加默认脸的参考图，用「在这张图上只改一处」的图生图 / 编辑方式出，不重新生成整张脸
6. 表情板格子太多导致漂移时，拆成单格生成，或减到 6 格

同一个模型反复做大的表情（比如某模型的「开心」永远露齿），记进 `model-notes.md`。
