import openai
import os

# model = 'gpt-4-turbo'


def ask_gpt(message, model='gpt-4o'):
    url = 'https://api.chatanywhere.tech/v1/'
    ai = openai.OpenAI(base_url=url)
    rsp = ai.chat.completions.create(
        model=model, messages=[{'role': 'user', 'content': message}])
    print(rsp.choices[0].message.content)


def ask_gpt_math(message, model='gpt-4o'):
    url = 'https://api.chatanywhere.tech/v1/'
    ai = openai.OpenAI(base_url=url)
    rsp = ai.chat.completions.create(
        model=model, messages=[{'role': 'system', 'content': '我是一名数学教授,有什么可以帮助你的在数学上'}, {'role': 'user', 'content': message}])
    print(rsp.choices[0].message.content)


def ask_gpt_math_his(message, history, model='gpt-4o'):
    url = 'https://api.chatanywhere.tech/v1/'
    ai = openai.OpenAI(base_url=url)
    if not history:
        history.append(
            {'role': 'system', 'content': '我是一名数学教授,有什么可以帮助你的在数学上'})
    history.append({'role': 'user', 'content': message})
    rsp = ai.chat.completions.create(
        model=model, messages=history)
    print(rsp.choices[0].message.content)
    history.append(
        {'role': 'system', 'content': rsp.choices[0].message.content})


def ask_gpt_picture(image_path, message, p=False):
    import base64
    import requests
    # OpenAI API Key
    api_key = os.getenv('OPENAI_API_KEY')

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{message}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    }
    response = requests.post(
        "https://api.chatanywhere.tech/v1/chat/completions", headers=headers, json=payload)
    if p:
        print(response.json()['choices'][0]['message']['content'])
    return response.json()['choices'][0]['message']['content']
