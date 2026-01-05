from aiogram.filters.callback_data import CallbackData

class ProxyPaginator(CallbackData, prefix="proxy_list"):
    page: int

class ProxyDetail(CallbackData, prefix="proxy_view"):
    proxy_id: str