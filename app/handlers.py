from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import app.keyboard as kb

r = Router()

@r.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(text=f'Привет, {message.from_user.full_name}, этот бот умеет играть в слова. И знает более 40к слов! Выбирите кто будет ходить первым',
                         reply_markup=kb.start)
    
@r.callback_query(F.data == 'firstpl')
async def firstpl(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.edit_text(text='Окей, пишите первое слово',
                               reply_markup=kb.exit)
    
@r.callback_query(F.data == 'firstbt')
async def firstpl(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.edit_text(text='Окей, отвечайте на первое слово',
                               reply_markup=kb.exit)
    
@r.callback_query(F.data == 'exit')
async def firstpl(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.edit_text(text='Выбирите снова',
                               reply_markup=kb.start)