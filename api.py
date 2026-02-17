class TechnitiumApi:
    def __init__(self, host, api_key, session, timeout=10):
        self._host = host
        self._api_key = api_key
        self._timeout = timeout
        self._session = session

    async def get_status(self):
        url = f"{self._host}/api/status"
        headers = {"Authorization": f"Bearer {self._api_key}"}
        try:
            async with self._session.get(url, headers=headers, timeout=self._timeout) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return {"ad_blocking_status": data.get("adBlockingEnabled")}
        except Exception as e:
            # Error fetching status, return None
            import logging
            logging.getLogger(__name__).error(f"Error fetching Technitium status: {e}")
            return {"ad_blocking_status": None}

    async def pause_ad_blocking(self, seconds):
        url = f"{self._host}/api/pause"
        headers = {"Authorization": f"Bearer {self._api_key}"}
        payload = {"duration": seconds}
        try:
            async with self._session.post(url, headers=headers, json=payload, timeout=self._timeout) as resp:
                resp.raise_for_status()
                return await resp.json()
        except Exception as e:
            # Error pausing ad blocking, return None
            import logging
            logging.getLogger(__name__).error(f"Error pausing ad blocking: {e}")
            return None

    async def close(self):
        # No need to close Home Assistant's managed session
        pass
