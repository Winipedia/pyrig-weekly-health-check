"""Test module."""

from pyrig_weekly_health_check.rig.configs.version_control.remote.workflows import (
    health_check,
)


class TestHealthCheckWorkflowConfigFile:
    """Tests for the health check workflow configuration."""

    def test_cron_schedule(self) -> None:
        """Test function."""
        workflow = health_check.HealthCheckWorkflowConfigFile.I

        assert workflow.cron_schedule() == (0, 1, "*", "*", 1)

    def test_workflow_triggers(self) -> None:
        """Test function."""
        workflow = health_check.HealthCheckWorkflowConfigFile.I
        triggers = workflow.workflow_triggers()

        assert triggers["schedule"] == [{"cron": "0 1 * * 1"}]
        assert "workflow_dispatch" in triggers
        assert "pull_request" in triggers
        assert "workflow_call" in triggers
