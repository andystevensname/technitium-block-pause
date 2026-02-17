
from datetime import timedelta
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from .const import DOMAIN

class TechnitiumBlockPauseDataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, api, update_interval=30):
        super().__init__(
            hass,
            logging.getLogger(__name__),
            name="Technitium Block Pause Data Coordinator",
            update_interval=timedelta(seconds=update_interval),
        )
        self.api = api

    async def _async_update_data(self):
        data = await self.api.get_status()
        if data is None or data.get("ad_blocking_status") is None:
            # Mark entity unavailable if API call failed
            from homeassistant.helpers.update_coordinator import UpdateFailed
            raise UpdateFailed("Failed to fetch Technitium status")
        return data
