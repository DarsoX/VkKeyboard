from vk_api.utils import sjson_dumps
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


vk = vk_api.VkApi(token = "TOKEN_GROUPS") #Тут вводим токен группы, токен должен быть строкой.
longpoll = VkBotLongPoll(vk, ID_GROUPS) #Тут вводим ID группы, ид группы должен быть числом. Без club или public
upload = vk_api.VkUpload(vk) #Загрузка

IDS_GROUP = 'IDS_GROUPS' #Ид Группы, должен быть строкой. Без club или public
IDName_GROUP = 'КОРОТКОЕ ИМЯ' #КОРОТКОЕ ИМЯ ГРУППЫ/, должно быть строкой. Если нету, не трогаем.
Name_GROUP = 'Название_Группы' #Название группы, в нижнем регистре.
activ = 0 #АнтиФлуд


while True: #Цикл.
    try: 
    	if IDName_GROUP == 'КОРОТКОЕ ИМЯ': #Проверка вводили ли вы короткое имя
    		IDName_GROUP = 'club' + str(ID_GROUP) #Если нет, создает нужное для работы.

    	if event.obj.text.lower() == 'команда': #Замените "Команда" на свою команду, обязательно без больших слов.
            activ = 0 #Обнуляем наш АнтиФлуд
            if activ == 0: #Проверяем или АнтиФлуд обнулеван
                tzt5 = 'привет' #Надпись на кнопке
                color = VkKeyboardColor.NEGATIVE #Колор кнопки
                keyboard = VkKeyboard() #Сама клавиатура
                keyboard.add_button(tzt5, color) #Добавляем кнопку с надписью и цветом.
                keyboard.add_line() #Добавляем переход на нижнюю полосу/Если хотите что бы кнопки были в один ряд убираем эту строку
                keyboard.add_button('команда2', color = VkKeyboardColor.PRIMARY) #Добавляем вторую кнопку.
                vk.method('messages.send', {'peer_id':event.obj.peer_id,'random_id': random.randint(0, 2**64), 'message': 'Клавиатура Открыта' ,'keyboard': sjson_dumps({**keyboard.keyboard, 'inline': True})}) #Отправляем сообщение и клавиатуру

            
            if event.obj.text.lower() == '[club' +str(IDS_GROUP) +'|@' +str(IDName_GROUP) +'] команда' or event.obj.text.lower() == '[club' +str(IDS_GROUP) +'|'+str(Name_GROUP)+'] команда':
                if activ == 0: #Проверяет, обнулен ли наш АнтиФлуд
                	activ = 1 #Активирует АнтиФлуд
                    vk.method('messages.send',{'peer_id':event.obj.peer_id,'message':'Ответ'}) #Отправляет ответ на вашу команду.    

            if event.obj.text.lower() == '[club' +str(IDS_GROUP) +'|@' +str(IDName_GROUP) +'] команда2' or event.obj.text.lower() == '[club' +str(IDS_GROUP) +'|'+str(Name_GROUP)+'] команда2':
                if activ == 0: #Проверяет, обнулен ли наш АнтиФлуд
                	activ = 1 #Активирует АнтиФлуд
                    vk.method('messages.send',{'peer_id':event.obj.peer_id,'message':'Ответ на вторую кнопку'}) #Отправляет ответ на вашу кнопку2.           
    except Exception as e:
        print(e)
