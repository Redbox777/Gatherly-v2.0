from aiogram import types
from aiogram.dispatcher import Router
from aiogram.filters import CommandHelp
from ..keyboards import help_keyboard

router = Router()


@router.message(CommandHelp())
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    text = """ℹ️ <b>Справка по Gatherly Life OS</b>

📚 <b>Основные команды:</b>
/start — Запустить бота
/help — Показать эту справку
/settings — Настройки бота
/stats — Статистика использования

📅 <b>Встречи:</b>
/create_meet — Создать встречу
/my_meets — Мои встречи
/rsvp — Подтвердить участие

 <b>Погода:</b>
/weather — Текущая погода
/forecast — Прогноз на неделю
/running — Погода для бега
/fishing — Погода для рыбалки

📝 <b>Заметки:</b>
/note — Создать заметку
/notes — Мои заметки

👥 <b>Друзья:</b>
/friends — Список друзей
/add_friend — Добавить друга
/profile — Мой профиль

💡 <b>Совет:</b>
Используй кнопки в главном меню для быстрого доступа!
"""
    
    await message.answer(text, reply_markup=help_keyboard(), parse_mode="HTML")
