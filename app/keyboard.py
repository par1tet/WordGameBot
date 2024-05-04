from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ходить первым👾', callback_data='firstpl'),InlineKeyboardButton(text='Ходит бот🤖', callback_data='firstbt')]])

exit = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад↩', callback_data='exit')]])