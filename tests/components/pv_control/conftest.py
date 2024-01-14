"""Common fixtures for the pv-island-consumer-control tests."""
from collections.abc import Generator
from unittest.mock import AsyncMock, patch

import pytest


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock, None, None]:
    """Override async_setup_entry."""
    with patch(
        "homeassistant.components.pv_control.async_setup_entry", return_value=True
    ) as mock_setup_entry:
        yield mock_setup_entry
