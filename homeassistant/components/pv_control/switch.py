"""Platform for switch integrations."""
from typing import Any

from homeassistant.components.switch import SwitchEntity


class PvAutostart(SwitchEntity):
    """Autostart switch."""

    _attr_has_entity_name = True
    _state = False

    def turn_on(self, **kwargs: Any) -> None:
        """Turn on the switch."""
        _state = True

    def turn_off(self, **kwargs: Any) -> None:
        """Turn off the switch."""
        _state = False
