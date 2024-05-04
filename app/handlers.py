from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import random
import json

import app.keyboard as kb

r = Router()

@r.message(Command('start'))
async def cmd_start(message: Message):
    add_data = {
        'start_move': 'pl',
        'using_words_pl': [
            
        ],
        'using_words_bt': [
            
        ]
    }
    with open('app/socia.json', 'w') as file:
        json.dump(add_data, file, indent='', ensure_ascii=False)
    await message.answer(text=f'Привет, {message.from_user.full_name}, этот бот умеет играть в слова. И знает более 40к слов! Выбирите кто будет ходить первым',
                         reply_markup=kb.start)
    
@r.message(Command('stop'))
async def stop_game(message: Message):
    add_data = {
        'start_move': 'pl',
        'using_words_pl': [
            
        ],
        'using_words_bt': [
            
        ]
    }
    with open('app/socia.json', 'w') as file:
        json.dump(add_data, file, indent='', ensure_ascii=False)
    with open('app/socia.json', 'r') as file:
        data = json.loads(file)
        await message.answer(f"Игра окончена, если хотите продолжить то выберайте режим\nКоличество слов: {data['using_words_pl']}",
                            reply_markup=kb.start)
    
@r.callback_query(F.data == 'firstpl')
async def firstpl(cb: CallbackQuery):
    add_data = {
        'start_move': 'pl',
        'using_words_pl': [
            
        ],
        'using_words_bt': [
            
        ]
    }
    with open('app/socia.json', 'r') as file:
        socia_data = json.load(file)
        new_data = {**socia_data, **add_data}
    with open('app/socia.json', 'w') as file:
        json.dump(new_data, file, indent='', ensure_ascii=False)
        
    await cb.answer('')
    await cb.message.edit_text(text='Игра начинается, пишите первое слово\n(что бы закончить пишите /stop)',
                               reply_markup=kb.exit)
    
@r.callback_query(F.data == 'firstbt')
async def firstbt(cb: CallbackQuery):
    add_data = {
        'start_move': 'pl',
        'using_words_pl': [
            
        ],
        'using_words_bt': [
            
        ]
    }
    with open('app/socia.json', 'r') as file:
        socia_data = json.load(file)
        new_data = {**socia_data, **add_data}
    with open('app/socia.json', 'w') as file:
        json.dump(new_data, file, indent='', ensure_ascii=False)
        
    await cb.answer('')
    await cb.message.edit_text(text='Игра начинается, отвечайте на первое слово\n(что бы закончить пишите/stop)',
                               reply_markup=kb.exit)
    
@r.callback_query(F.data == 'exit')
async def exit(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.edit_text(text='Выберайте снова',
                               reply_markup=kb.start)
    
@r.message(F.text)
async def firstpl_game(message: Message):
    with open('words_Russian.json', 'r') as file:
        Russian_words = json.load(file)
    
    print(message.text[0].upper())
    print(message.text.upper())
    try:
        Russian_words[f'{message.text[0].upper()}'].index(message.text.upper())
        
        with open('app/socia.json', 'r') as file:
            data = json.load(file)
            if message.text.upper() in data['using_words_pl']:
                await message.answer('Ты уже это слово изпользовал')
                return 0
            try:
                if message.text.upper()[0] != last_letter(data['using_words_bt'][-1]):
                    await message.answer('Не та буква')
                    return 0
            except:
                pass
        with open('app/socia.json', 'r') as file:
            while True:
                word_answer = Russian_words[f'{last_letter(message.text.upper())}'][random.randint(0,len(Russian_words[f'{last_letter(message.text.upper())}']))]
                data = json.load(file)
                if word_answer in data['using_words_bt']:
                    continue
                else:
                    break
        add_data = {
            'using_words_pl': [
                message.text.upper()
            ],
            'using_words_bt': [
                word_answer
            ]
        }
        with open('app/socia.json', 'r') as file:
            socia_data = json.load(file)
            new_data = {
                'using_words_pl': [*socia_data['using_words_pl'], *add_data['using_words_pl']],
                'using_words_bt': [*socia_data['using_words_bt'], *add_data['using_words_bt']]
            }
        with open('app/socia.json', 'w') as file:
            json.dump(new_data, file, indent='', ensure_ascii=False)
        await message.answer(text=f'{word_answer},\nВам на {last_letter(word_answer)}')
        
    except ValueError or KeyError:
        word_answer = 'Нет такого слова'
        await message.answer(text=f'{word_answer}')

def last_letter(word):
    last_l = word[-1]
    for i in range(1,len(word)):
        if word[-i] == 'Ь' or word[-i] == 'Ъ' or word[-i] == 'Ё' or word[-i] == 'Й' or word[-i] == 'Ы':
            last_l = word[-(i+1)]
        else:
            break
    return last_l