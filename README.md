# pyrig-weekly-health-check

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-weekly-health-check/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-weekly-health-check/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-weekly-health-check/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-weekly-health-check/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-weekly-health-check/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-weekly-health-check)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/j178/prek)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/CI/CD--security-zizmor-yellow)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/j178/prek)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/j178/prek)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/j178/prek)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/j178/prek)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/j178/prek)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/j178/prek)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/j178/prek)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://github.com/j178/prek)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Winipedia/pyrig/main/docs/assets/badge.json)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-weekly-health-check?style=social)](https://github.com/Winipedia/pyrig-weekly-health-check)
[![VersionControlHookManager](https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge.svg)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-weekly-health-check)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-weekly-health-check?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-weekly-health-check)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-weekly-health-check)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-weekly-health-check)](https://github.com/Winipedia/pyrig-weekly-health-check/blob/main/LICENSE)

---

> A pyrig plugin that runs the health check weekly.

---

## Overview

A [pyrig](https://github.com/Winipedia/pyrig) plugin that changes the Health
Check workflow's scheduled run from daily to every Monday at 01:00 UTC. Manual
dispatch, pull request, and reusable-workflow triggers remain unchanged.

## Usage

```bash
uv add pyrig-weekly-health-check --dev
uv run pyrig sync
```

Pyrig discovers the plugin automatically. Sync regenerates
`.github/workflows/health_check.yml` with the weekly schedule (`0 1 * * 1`).

See the [documentation](https://Winipedia.github.io/pyrig-weekly-health-check)
for the full schedule details and API reference.
