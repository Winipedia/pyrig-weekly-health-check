"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_weekly_health_check.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile,
)

_CONFIG_FILE_OVERRIDES = (BaseHealthCheckWorkflowConfigFile.cron_schedule,)
_CONFIG_FILES = (HealthCheckWorkflowConfigFile,)
