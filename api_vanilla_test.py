import requests # Импорт модуля requests
print("Это специальная программа для того, чтобы получить какие-то данные Vanilla!") # Приветствие
while True: # Бесконечный цикл
	get = input("Данные получения: ") # Запрос данных...
	user = input("Имя пользователя: ")
	res = requests.get(f"http://my.vanillame.ml/api?get={get}&user={user}") # ...и отправка их на сервер
	print("Сервер отправил: " + res.text) # Здесь ответ сервера
