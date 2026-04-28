# BIM Software Dev Plugin Marketplace

This repository is a Claude Code plugin marketplace for BIM software development.

It provides the `bim-software-dev-plugin`, which adds a Claude Code skill for Revit API, Unity BIM tools, IFC/OpenBIM workflows, BIM data engineering, BIM automation, model validation, XR, digital twins, AI/ML datasets, robotics, graph databases, and BIM integration work.

## Install From GitHub

In Claude Code, add this GitHub repository as a plugin marketplace:

```text
/plugin marketplace add isaddiq/Claude-BIM-development-skill
```

Then install the BIM plugin from that marketplace:

```text
/plugin install bim-software-dev-plugin@bim-dev-marketplace
```

If you prefer the full Git URL, this is equivalent:

```text
/plugin marketplace add https://github.com/isaddiq/Claude-BIM-development-skill.git
```

![alt text](image.png)

## Use The Skill

After installation, run the BIM software development skill from Claude Code:

```text
/bim-software-dev-plugin:bim-software-dev create a C# Revit add-in that exports BIM metadata to CSV
```

More examples:

```text
/bim-software-dev-plugin:bim-software-dev create a C# Revit add-in that exports ElementId, UniqueId, category, family, type, level, and parameters to CSV
/bim-software-dev-plugin:bim-software-dev create Unity C# scripts to bind BIM metadata from CSV to imported GameObjects and show properties on object selection
/bim-software-dev-plugin:bim-software-dev debug why my Revit-exported OBJ objects appear in Unity but metadata does not bind
/bim-software-dev-plugin:bim-software-dev design an IFC to graph database pipeline for BIM semantic queries
/bim-software-dev-plugin:bim-software-dev create a BIM-to-robotics semantic scene graph pipeline
```

Some Claude Code versions may expose plugin skill shortcuts differently. If the command name differs, check the available plugin and skill commands:

```text
/plugin
/skills
```

## What This Plugin Helps With

- C# Revit API add-ins and metadata exporters
- C# Unity BIM viewers, metadata binding, and object selection
- IFC/OpenBIM extraction, validation, and transformation
- BIM-to-database and BIM-to-graph workflows
- BIM web APIs, dashboards, and viewer integrations
- BIM model validation and mapping reports
- XR, digital twin, robotics, and AI/ML BIM data pipelines

## Local Development

If you cloned this repository and want to test the plugin locally without installing it from the marketplace, run:

```bash
claude --plugin-dir ./plugins/bim-software-dev-plugin
```

You can also add the cloned repository root as a local marketplace:

```text
/plugin marketplace add .
/plugin install bim-software-dev-plugin@bim-dev-marketplace
```

## Repository Structure

```text
.claude-plugin/
  marketplace.json

plugins/
  bim-software-dev-plugin/
    .claude-plugin/
      plugin.json
    skills/
      bim-software-dev/
        SKILL.md
        references/
        templates/
        snippets/
        scripts/
```

The root `.claude-plugin/marketplace.json` makes this repository a Claude Code plugin marketplace. The plugin-level `.claude-plugin/plugin.json` defines the installable BIM plugin.

## Updating

When releasing a new version, bump the version in both files:

- `plugins/bim-software-dev-plugin/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`

## Official Marketplace Submission

This repository can be installed directly by adding it as a Claude Code plugin marketplace. Listing it in any official Claude or Anthropic marketplace is separate and requires following the official plugin submission process.
