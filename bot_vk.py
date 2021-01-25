import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

token = ""
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.text != '!sendnumber':
        print('Пользователь отправил сообщение')
        if event.from_user:
            vk.messages.send(user_id=event.user_id, message='Привет, я бот, который отправляет \
                                                           тебе рандомное число, чтобы я это сделал \
                                                           пропиши команду: !sendnumber',
                             random_id=0)
    elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            vk.messages.send(user_id=event.user_id, message='Вот тебе рандомное число:' + ' ' + str(random.randint(0, 100000)),
                             random_id=0)
