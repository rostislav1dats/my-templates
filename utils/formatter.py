# def format_item_mesasge(data: dict) -> str:
#     """ Formating data from API in readable HTML"""
#     name = data.get('data', 'Unknown')
#     price = data.get('price', 0)
#     description = data.get('description', 'Description unknown')

#     return (
#         f"📦 <b>Товар:</b> {name}\n"
#         f"💰 <b>Цена:</b> {price} руб.\n\n"
#         f"📝 <i>{description}</i>"
#     )

# def format_api_ids(response_json: dict) -> str:
#     items = response_json.get('data', {}).get('list', [])

#     if not items:
#         return '📭 Object list is empty.'
    
#     ids_text = '\n'.join([f'<code>{item.get('id')}</code>' for item in items if 'id' in item])
#     return f'<b>Found IDs:</b>\n\n{ids_text}'

def format_proxy_list(proxies: list, filter_name: str = None) -> str:
    header = f"🌐 <b>Список прокси ({filter_name or 'Все'}):</b>\n\n"
    
    lines = []
    for p in proxies:
        # Используем тег <code> для удобного копирования ID кликом
        lines.append(f"🔹 <code>{p.id}</code> | {p.type}")
    
    return header + "\n".join(lines)