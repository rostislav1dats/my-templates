import aiohttp

from typing import Optional, Any
from config import EXTERNAL_API_URL

# async def get_data_from_api(item_id: int):
#     async with aiohttp.ClientSession() as session:
#         url = f'{EXTERNAL_API_URL}/items/{item_id}'
#         async with session.get(url) as response:
#             if response.status == 200:
#                 return await response.json()
#             return None

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

        async def_make_request(self, endpoint: str, params: Optional[dict] = None) -> Optional[dict]:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/{endpoint}"
                try:
                    async with session.get(url, params=params, timeout=10) as response:
                        if response.status == 200:
                            return await response.json()
                        return None
                except Exception as e:
                    print(f"API Error: {e}")
                    return None
        
        async def get_proxies(self, proxy_type: Optional[str] = None):
            """Запрос списка прокси с опциональным фильтром типа"""
            params = {}
            if proxy_type:
                params["type"] = proxy_type
            return await self._make_request("proxies", params=params)


    # async def _make_request(self, endpoint: str) -> Optional[dict]:
    #     """ Universal private method for requests"""
    #     async with aiohttp.ClientSession() as session:
    #         url = f"{self.base_url}/{endpoint}"
    #         try:
    #             async with session.get(url) as response:
    #                 if response.status == 200:
    #                     return await response.json()
    #                 return None
    #         except Exception as e:
    #             print(f'error in request {url}: {e}')
    #             return None
            
    # # Methods for each request
    # async def get_items(self):
    #     return await self._meka_request('items')
    
    # async def get_users(self):
    #     return await self._make_request('users')
    
    # async def get_stats(self):
    #     return await self._make_request('stats')
    
api_client = APIClient()