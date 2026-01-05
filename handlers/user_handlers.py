# from aiogram import Router, types
# from aiogram.filters import Command
# from api.client import get_data_from_api
# from utils.formatter import format_item_message

# router = Router()

# @router.message(Command('start'))
# async def cmd_start(message: types.Message):
#     await message.answer('Input /help to see list of commands')

# @router.message()
# async def handle_item_request(message: types.Message):
#     if message.text.isdigit():
#         data = await get_data_from_api(int(message.text))
#         if data:
#             text = format_item_message(data)
#             await message.answer(text, parse_mode='HTML')
#         else:
#             await message.answer('❌ Product didn`t found')
#     else:
#         await message.answer('Plese input numeric id')

# @router.message(Command('items'))
# async def show_items(message: types.Message):
#     raw_data = await api_client.get_items() # Получаем dict

#     if raw_data:
#         # Pydantic сам "прокусит" вложенность {"data": {"list": [...]}} 
#         # если правильно настроить модели (см. выше)
#         data = ItemsResponse(**raw_data["data"]) 
        
#         # Теперь у тебя есть список объектов с автодополнением
#         response_text = "\n".join([f"ID: {item.id}" for item in data.items])
#         await message.answer(f"Список товаров:\n{response_text}")
#     else:
#         await message.answer("Ошибка связи с API")

# @router.message(Command("proxies"))
# async def cmd_proxies(message: types.Message, command: CommandObject):
#     # Извлекаем аргумент (например, STABLE или DINAMIC)
#     proxy_type = command.args.upper() if command.args else None
    
#     raw_data = await api_client.get_proxies(proxy_type)
    
#     if not raw_data:
#         return await message.answer("❌ Ошибка при получении данных от API")

#     # Валидируем данные через Pydantic
#     try:
#         data_model = ProxyResponse(**raw_data)
#         proxies = data_model.data.list
#     except Exception:
#         return await message.answer("❌ Ошибка парсинга данных")

#     # Дополнительная фильтрация на стороне кода (если API вернул всё)
#     if proxy_type:
#         proxies = [p for p in proxies if proxy_type in p.type.upper()]

#     if not proxies:
#         return await message.answer(f"Ничего не найдено по фильтру: {proxy_type}")

#     # Отправляем форматированный результат
#     text = format_proxy_list(proxies, proxy_type)
#     await message.answer(text, parse_mode="HTML")


from aiogram import Router, F, types
from aiogram.filters import Command
from api.client import api_client
from api.schemas import ProxyResponse
from utils.keyboards import get_proxy_list_kb, get_back_to_list_kb
from utils.callbacks import ProxyPaginator, ProxyDetail

router = Router()

@router.message(Command("proxies"))
async def cmd_proxies(message: types.Message):
    raw_data = await api_client.get_proxies()
    if raw_data:
        data_model = ProxyResponse(**raw_data)
        kb = get_proxy_list_kb(data_model.data.list, page=0)
        await message.answer("Выберите прокси из списка:", reply_markup=kb)

# Обработка переключения страниц
@router.callback_query(ProxyPaginator.filter())
async def process_pagination(callback: types.CallbackQuery, callback_data: ProxyPaginator):
    raw_data = await api_client.get_proxies()
    data_model = ProxyResponse(**raw_data)
    
    kb = get_proxy_list_kb(data_model.data.list, page=callback_data.page)
    
    # Редактируем старое сообщение, чтобы не спамить
    await callback.message.edit_text("Выберите прокси из списка:", reply_markup=kb)
    await callback.answer()

# Обработка клика на конкретный прокси (детализация)
@router.callback_query(ProxyDetail.filter())
async def process_proxy_view(callback: types.CallbackQuery, callback_data: ProxyDetail):
    # В идеале тут запрос к API по ID: api_client.get_proxy_detail(callback_data.proxy_id)
    # Для примера просто выведем инфо
    proxy_id = callback_data.proxy_id
    
    text = (
        f"📄 <b>Детальная информация</b>\n\n"
        f"<b>ID:</b> <code>{proxy_id}</code>\n"
        f"<b>Статус:</b> Online ✅\n"
        f"<b>Доп. инфо:</b> Здесь могут быть данные из API"
    )
    
    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=get_back_to_list_kb())
    await callback.answer()
