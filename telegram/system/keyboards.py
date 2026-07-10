from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню (Full режим)"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("📅 Встречи"),
        KeyboardButton("🌤 Погода"),
        KeyboardButton("📝 Заметки")
    )
    keyboard.add(
        KeyboardButton("👥 Друзья"),
        KeyboardButton(" Статистика"),
        KeyboardButton("⚙️ Настройки")
    )
    return keyboard


def lite_menu_keyboard() -> ReplyKeyboardMarkup:
    """Упрощенное меню (Lite режим)"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("📅 Встречи"),
        KeyboardButton("🌤 Погода")
    )
    return keyboard


def help_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для справки"""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("ℹ️ О проекте", callback_data="help_about"),
        InlineKeyboardButton(" Команды", callback_data="help_commands")
    )
    return keyboard
