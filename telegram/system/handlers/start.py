from aiogram import types
from aiogram.dispatcher import Router
from aiogram.filters import CommandStart
from config import DEFAULT_UI_MODE
from ..keyboards import main_menu_keyboard, lite_menu_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    username = message.from_user.username or "Пользователь"
    
    # Определяем режим (можно сохранить в БД)
    ui_mode = DEFAULT_UI_MODE
    
    text = f"""👋 Привет, {username}!

🌟 <b>Gatherly Life OS v2</b> — твоя персональная операционная система для жизни.

📌 <b>Что умею:</b>
• 📅 Организовывать встречи и события
• 🌤 Показывать погоду и прогнозы
• 📝 Вести заметки и календарь
• 👥 Управлять контактами и друзьями
• 📊 Анализировать твою активность

Выбери режим интерфейса:
• <b>Full</b> — все функции (25+ модулей)
• <b>Lite</b> — только основное

Режим: <b>{ui_mode.upper()}</b>
"""
    
    # Выбираем клавиатуру в зависимости от режима
    keyboard = main_menu_keyboard() if ui_mode == "full" else lite_menu_keyboard()
    
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")
