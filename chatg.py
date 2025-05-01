#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import readline
from  credentials import gpt_api_key
from rich.console import Console
from rich.markdown import Markdown

from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=gpt_api_key,
)

def format_rich(text, role="ChatGPT"):

    formatted_text = Markdown(text)

    return formatted_text
 
conversation_history = []

prefix = ""


def ask_chatgpt(question):
    # Добавление сообщения пользователя в историю
    conversation_history.append({"role": "user", "content": f"{prefix}{question}"})

    # Запрос к API ChatGPT с контекстом
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history
    )

    # Получение ответа от модели
    answer = response.choices[0].message.content

    # Добавление ответа модели в историю
    conversation_history.append({"role": "assistant", "content": answer})

    return answer


def start_new_topic():
    """
    Сброс истории и начало новой темы.
    """
    global conversation_history
    conversation_history = []
    print("Новая тема начата. Вы можете задать свой вопрос.")


def start():
    info = "Добро пожаловать в ChatGPT!\nq - выйти\nn - новая тема\n0 - сбросить префикс \n00 - сбросить префикс и начать новую тему \n\
e - первести на англизский\np - первести на польский\nrv - первести на русский и привести примеры использования\n\
r - перевести на русский\nc - clear\nh - вывести справку"
    print(info)
    global  prefix
    while True:
        user_input = input("\033[1;32mВы:\033[0m ")

        if user_input.lower() == "n":
            start_new_topic()
            continue
        elif user_input.lower() == "q":
            break
        elif user_input.lower() == "r":
            prefix = "Переведи на Русский: "
            start_new_topic()
            print("""Я буду переводить всё на Русский язык\nдля выхода из режима набeрите - 00\nдля смены темы без смены \
режима - 0\nсправка  - h""")
            continue
        elif user_input.lower() == "e":
            prefix = "Translate into English: "
            start_new_topic()
            print("""Я буду переводить всё на АНГЛИЗСКИ язык\nдля выхода из режима набeрите - 00\nдля смены темы без смены \
режима - 0\nсправка  - h""")
            continue
        elif user_input.lower() == "0":
            prefix = ""
            continue
        elif user_input.lower() == "c":
            os.system('clear')
            continue
        elif user_input.lower() == "00":
            start_new_topic()
            prefix = ""
            continue
        elif user_input.lower() == "p":
            prefix = "Переведи на Польский: "
            start_new_topic()
            print("""Я буду переводить всё на ПОЛЬСКИЙ язык\nдля выхода из режима набeрите - 00\nдля смены темы без смены \
режима - 0\nсправка  - h""")
            continue
        elif user_input.lower() == "rv":
            prefix = "Переведи  и объясни смысл и приведи примеры на англизском языке с переводами: "
            start_new_topic()
            print("""Я буду переводить всё на Русский язык и приводить примеры использования\nдля выхода из режима набeрите - 00\nдля смены темы без смены \
режима - 0\nсправка  - h""")
            continue
        elif user_input.lower() == "h":
            print(info)
            continue

        response = ask_chatgpt(user_input)

        console = Console()
        print("\033[1;32mChatGPT:\033[0m")
        console.print(format_rich(response))
        print("")


# Пример использования
if __name__ == "__main__":
    start()
# sudo cp chatg.py /usr/bin/chatg
