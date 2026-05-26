# Bottleneck Alpha Framework

> 一个用于研究 AI、半导体、光通信、存储、电力基础设施、国防科技和关键材料等超级周期中“结构性瓶颈”的开源研究框架。

**Bottleneck Alpha Framework** 的目标不是追逐热门股票，而是帮助研究者系统化回答一个问题：

> 某家公司是否处在一个不可绕开的供应链瓶颈上，并且这个瓶颈能否转化为收入、毛利率、经营利润和估值重估？

本项目把一套“Serenity-style Bottleneck Alpha”研究方法整理成可复用的开源工具，包括：

- 一套中文研究框架文档
- 一个 0-50 分评分体系
- 可复制的分析模板
- 可直接喂给大模型的 prompt
- 一个轻量 CLI 打分工具
- 示例案例与 watchlist YAML
- 开源发布、贡献和风险披露文件

> **Important**：本项目只用于研究和教育，不构成投资建议。任何股票、行业或公司示例都不代表推荐买卖。

---

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/<your-name>/bottleneck-alpha-framework.git
cd bottleneck-alpha-framework
```

### 2. 安装 CLI

```bash
pip install -e .
```

### 3. 运行示例评分

```bash
bottleneck-alpha score examples/sample_score.yaml
```

你会得到类似输出：

```text
Bottleneck Alpha Score
----------------------
Ticker: RGTI
Total: 31.0 / 50
Category: Watchlist / small satellite only
```

---

## Repo 结构

```text
bottleneck-alpha-framework/
├── README.md
├── LICENSE
├── DISCLAIMER.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── pyproject.toml
├── Makefile
├── docs/
│   ├── FRAMEWORK.zh-CN.md
│   ├── RUBRIC.zh-CN.md
│   ├── SKILL_PROMPT.zh-CN.md
│   ├── CASE_STUDY_TEMPLATE.zh-CN.md
│   ├── CASE_STUDY_RGTI.zh-CN.md
│   └── OPEN_SOURCE_PUBLISH_GUIDE.zh-CN.md
├── prompts/
│   ├── system_prompt_zh.md
│   └── analyst_prompt_zh.md
├── templates/
│   ├── analysis_template.md
│   └── scoring_sheet.csv
├── examples/
│   ├── sample_score.yaml
│   └── sample_watchlist.yaml
├── src/bottleneck_alpha/
│   ├── __init__.py
│   ├── rubric.py
│   └── cli.py
└── tests/
    └── test_rubric.py
```

---

## 核心理念

### 1. 不买故事，买瓶颈

一个公司“重要”不等于股票会涨。真正重要的是：

- 它是否处在下游无法绕开的环节？
- 它是否有供应紧张、backlog、price hike、客户 forecast、战略投资、政府 funding 等验证？
- 它是否能把供应链重要性转化为 revenue、gross margin、operating income？

### 2. 架构迁移产生新瓶颈

AI 基建的瓶颈往往按顺序轮动：

```text
Compute / GPUs → Memory / HBM / NAND / DRAM → Interconnect / Networking → CPO / Silicon Photonics → Power / Grid → Materials / Testing / Packaging
```

真正的 alpha 往往出现在新瓶颈周期的早期。

### 3. 资本结构是核心变量

巨额 ATM、warrants、convertibles、lockup、SBC、authorized share increase 都可能摧毁再好的 thesis。

---

## 评分体系

每个标的按 10 个维度打分，每项 0-5 分，总分 0-50 分：

| 维度 | 问题 |
|---|---|
| 大周期强度 | 是否处在 AI / memory / photonics / power / national security 等大周期？ |
| 瓶颈强度 | 下游是否无法绕开？替代供应是否不足？ |
| 验证程度 | 是否有 backlog、sold out、price hikes、客户 forecast、战略投资？ |
| 财务转化 | 是否能转成 revenue / margin / operating income？ |
| 估值错配 | 与 peers / future revenue / TAM 相比是否明显低估？ |
| 市场未发现程度 | 是否机构覆盖少、冷门、非美上市、信息不透明？ |
| 扩产 / 技术路径 | 是否有 foundry / OSAT / capex / partner 支持 volume ramp？ |
| 资本结构 | 是否没有巨额 ATM / dilution overhang？ |
| 催化剂密度 | 是否有 GTC、OFC、earnings、CHIPS、customer ramp 等催化？ |
| 风险可控性 | 执行、竞争、宏观、监管、客户集中是否可接受？ |

---

## 适合分析的方向

- AI compute / ASIC / CPU / GPU
- Memory / HBM / NAND / DRAM
- Optical interconnect / Photonics / CPO / Silicon Photonics
- Power infrastructure / Transformers / Switchgear / Grid
- Advanced packaging / Testing / Inspection / Yield
- National security / CHIPS Act / DoD / Quantum
- Robotics / Space / Critical materials / Rare earths
- Stablecoins / Platform monetization / Retail networks

---

## 不适合本框架的情况

这个框架不适合纯粹分析：

- 没有供应链位置的 meme stock
- 只靠技术分析的短线交易
- 无法转化为收入和利润的“概念重要性”
- 没有基本面验证的单日新闻行情
- 已经被巨大稀释 overhang 摧毁的股票

---

## 贡献

欢迎贡献：

- 新行业供应链 mapping
- 评分案例
- 风险清单
- 数据源整理
- 英文版文档
- CLI 功能增强

请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## License

MIT License. See [LICENSE](LICENSE).
