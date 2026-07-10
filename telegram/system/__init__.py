from aiogram import Dispatcher
from .handlers.start import router as start_router
from .handlers.help import router as help_router


def register_system_handlers(dp: Dispatcher):
    """Регистрация хендлеров модуля System"""
    dp.include_router(start_router)
    dp.include_router(help_router)
