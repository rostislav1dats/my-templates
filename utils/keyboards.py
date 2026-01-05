from aiogram.utils.keyboard import InlineKeyboardBuilder
from api.schemas import ProxyItem
from utils.callbacks import ProxyPaginator, ProxyDetail

def get_proxy_list_kb(proxies: list[ProxyItem], page: int = 0):
    builder = InlineKeyboardBuilder()
    
    # Пагинация: допустим по 5 прокси на страницу
    items_per_page = 5
    start = page * items_per_page
    end = start + items_per_page
    current_items = proxies[start:end]

    for proxy in current_items:
        # Каждая кнопка ведет на детализацию прокси
        builder.button(
            text=f"📍 {proxy.id[:10]}... ({proxy.type})", 
            callback_data=ProxyDetail(proxy_id=proxy.id)
        )
    
    builder.adjust(1) # Кнопки прокси в один столбец

    # Кнопки навигации (Назад / Вперед)
    nav_buttons = []
    if page > 0:
        nav_buttons.append(builder.button(text="⬅️", callback_data=ProxyPaginator(page=page-1)))
    if end < len(proxies):
        nav_buttons.append(builder.button(text="➡️", callback_data=ProxyPaginator(page=page+1)))
    
    return builder.as_markup()

def get_back_to_list_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Назад к списку", callback_data=ProxyPaginator(page=0))
    return builder.as_markup()