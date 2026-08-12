# Dylan Cover Generator

> 把中文选题变成一张手机上也能读懂的高冲击竖版封面：先突出价值点，再让主标题完成判断。
>
> 3:4 竖版 · 价值点 + 主标题 · 高冲击构图 · 可复用角色 · Codex Skill

[English](README.en.md) · 中文

## 它解决什么问题

很多社交媒体封面只有一个标题，却没有把“为什么值得点开”说清楚。时间、效率、结果或收益被塞进小字里，主标题和价值承诺也容易互相争抢。

Dylan Cover Generator 为封面建立清晰的双文本层级：

- `value_point`：独立的价值点，例如 `1分钟`、`省下3小时` 或 `直接看结果`。
- `title`：唯一的主问题或主张，例如 `如何判断需求价值？`。

价值点不是弱化的副标题，而是一个需要在缩略图中立即读到的视觉承诺。Skill 会结合保存的构图参考、角色身份锚点和主题隐喻，生成 3:4 竖版社交媒体封面。

## 核心设计原则

### 1. 价值点 + 主标题

默认优先使用两个独立文本元素。价值点使用更醒目的强调色、徽章、丝带或描边面板；主标题保持大字号、强对比和清晰的问题张力。

例如：

```text
1分钟
如何判断需求价值？
```

主标题限制为 12 个可见字符；独立的价值点不计入主标题字数，但应该简短、明确、适合手机阅读。默认不添加副标题、平台按钮、点赞数或其他额外文字。

### 2. 只选一种主构图

Skill 提供六种构图骨架，根据主题选择最接近的一种，不把所有布局混在一起：

| 构图 | 适合主题 | 视觉骨架 |
| --- | --- | --- |
| `impact-explosion` | 挑战、转型、强承诺 | 人物从中心突破，标题巨大，主题物件飞散 |
| `skill-battle` | 技能差距、技术掌握 | 人物位于下半部，暗色径向背景，一个工具线索 |
| `choice-ui` | 问题、选择、需求判断 | 人物思考，周围浮动窗口和对比卡片 |
| `versus-comparison` | A 对 B、产品竞争 | 人物居中，两侧放置对立对象 |
| `tutorial-hand-off` | 教程、流程、脚本、数据 | 设备或面板向前推，前景卡片承接信息 |
| `reveal-board` | 展示、结果、前后变化 | 人物指向一侧，屏幕或证据板承载结果 |

### 3. 角色必须保持可识别

生成时优先使用角色注册表中的身份锚点，保留脸部、发型、比例和标志性服装；只根据主题改变姿势和表情。生成结果不会替代原始角色参考图。

### 4. 主题要有具体视觉隐喻

把抽象选题落到一两个看得见的物件上，例如应用窗口、结果卡、设备、文档、图表、屏幕或时钟。时间价值可以用时钟、倒计时、时间卡或明确的效率结果来支撑，但不要凭空发明数字或收益承诺。

### 5. 缩略图优先

画面使用近黑或深海军蓝底色、方向性轮廓光和有限的发光元素；标题区预留在顶部 28%–38%，人物脸部不要被文字遮住。生成后按手机缩略图检查价值点、主标题、人物动作和主题物件是否仍然清楚。

## 安装

克隆仓库后，将仓库内容复制到 Codex 的 Skill 目录。macOS / Linux：

```bash
git clone https://github.com/xDylanLong/dylan-cover-generator.git
cd dylan-cover-generator

skill_root="${CODEX_HOME:-$HOME/.codex}/skills/dylan-cover-generator"
mkdir -p "$skill_root"
rsync -a --exclude='.git' --exclude='outputs' ./ "$skill_root/"
```

Windows PowerShell：

```powershell
git clone https://github.com/xDylanLong/dylan-cover-generator.git
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills/dylan-cover-generator" } else { Join-Path $HOME ".codex/skills/dylan-cover-generator" }
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
Copy-Item -Recurse -Force .\dylan-cover-generator\* $skillRoot
```

安装后，在 Codex 中调用：

```text
Use $dylan-cover-generator 生成一张中文社媒封面。

value_point: 1分钟
title: 如何判断需求价值？
topic: 教用户快速判断一个需求是否值得做
archetype: choice-ui
```

如果没有提供价值点，Skill 只会在用户语境中已经存在明确价值表达时使用非量化短语；不会擅自编造时长、数字、结果或收益。

## 角色注册

仓库自带默认角色 `dylan-main`。查看、添加和切换角色：

```bash
python3 scripts/character_registry.py list
python3 scripts/character_registry.py add \
  --id my-character \
  --image /path/to/reference.png \
  --name "My Character" \
  --set-default
python3 scripts/character_registry.py use my-character
```

原始上传图会被保留为身份锚点；生成的封面不会覆盖角色资料。

## 仓库结构

```text
.
├── README.md
├── README.en.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── characters/
│   │   ├── dylan-main/
│   │   └── registry.json
│   └── style-references/
│       ├── style-01.jpg ... style-06.jpg
├── references/
│   └── style-anatomy.md
└── scripts/
    └── character_registry.py
```

## 使用边界

- 适合抖音、小红书等中文社交媒体的 3:4 竖版封面，不适合完整海报、商业 KV 或高密度数据图。
- 用户提供的价值点和主标题应视为确定文案；超过长度限制时，只压缩主标题，不擅自改写核心承诺。
- 图像模型可能生成错别字；如果文字不准确，应重新生成干净文字区，必要时再单独排版。
- 不生成点赞数、评论数、分享按钮、用户名、进度条、水印或信息流边框等平台界面元素。

## 相关文件

- [Skill instructions](SKILL.md)
- [English README](README.en.md)
- [Style anatomy](references/style-anatomy.md)
