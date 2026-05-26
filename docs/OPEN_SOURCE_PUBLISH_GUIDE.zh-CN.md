# 开源发布指南

## 1. 推荐 repo 名称

可选：

- `bottleneck-alpha-framework`
- `bottleneck-alpha`
- `supply-chain-bottleneck-alpha`
- `ai-infra-bottleneck-research`

推荐：`bottleneck-alpha-framework`

## 2. 推荐 GitHub 描述

```text
A research framework for identifying structural bottlenecks across AI infrastructure, photonics, memory, power grid, national security, and critical materials cycles.
```

中文：

```text
用于识别 AI 基建、光通信、存储、电力、国防科技和关键材料周期中结构性瓶颈的开源研究框架。
```

## 3. 推荐 topics

```text
investing research-framework ai-infrastructure semiconductors photonics memory supply-chain quantum-computing critical-materials
```

## 4. 创建 GitHub 仓库

```bash
cd bottleneck-alpha-framework
git init
git add .
git commit -m "Initial release: Bottleneck Alpha Framework"
git branch -M main
git remote add origin git@github.com:<your-name>/bottleneck-alpha-framework.git
git push -u origin main
```

## 5. 发布 v0.1.0 release

```bash
git tag v0.1.0
git push origin v0.1.0
```

Release title:

```text
v0.1.0 - Initial open-source release
```

Release notes:

```text
Initial release of Bottleneck Alpha Framework:

- Chinese framework documentation
- 0-50 scoring rubric
- reusable analysis prompt
- case study template
- RGTI example case
- CLI scoring tool
- sample YAML files
- disclaimer and contribution guide
```

## 6. 推荐置顶声明

建议在 GitHub README 顶部保留：

> This project is for research and education only. Nothing here is investment advice.

## 7. 后续路线图

- [ ] 英文版 README
- [ ] 更多 case studies
- [ ] Web-based scoring UI
- [ ] Industry supply-chain maps
- [ ] Data-source registry
- [ ] LLM agent mode
- [ ] Export to PDF / Markdown report
