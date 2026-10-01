"""GitHub Actions workflow generator for the health check CI stage."""

from typing import Literal

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Health check workflow scheduled to run weekly."""

    def cron_schedule(self) -> tuple[int, int, Literal["*"], Literal["*"], int]:
        """Return the weekly Monday schedule at 01:00 UTC.

        Returns:
            Cron fields for minute, hour, day, month, and weekday.
        """
        return 0, 1, "*", "*", 1
