# web_1-CLICKcat - клиент-серверное приложение 
Представленный проект содержит файлы: Server.py и Client.py. Данные файлы представляют собой два оконных приложения, запускающихся на разных устройствах и непостредственно связанных друг с другом. 
При запуске Server.py появляется оконное приложение с картинкой, которое будет меняться при нажатии кнопки в выскочившем оконном приложении при запуске Client.py. 

## Требования 
Для запуска проекта нам необходимо обладать следующими библиотеками:
  * PIL
  * socket
  * tkinter
  * threading
    
**Также следует учитывать наличие на компьютере компилятора Python и подключение двух задействованных устройств к одной локальной сети.**

## Руководство по запуску:
1. Следует подключить устройства к одной локальной сети.
2. Откройте и запустите Server.py, у вас должно открыться окошко с картинкой. 
3. Скопируйте с терминала появившийся IP адрес сервера в вашей локальной сети.
4. Откройте Client.py вставьте IP полученный на первом устройстве в 5 строку файла Client.py.
5. Запустите Client.py и нажмите на кнопку в выскочившемся окне.
   
## Автор 
Баширова Камилла (Б9122-01.03.02сп1)