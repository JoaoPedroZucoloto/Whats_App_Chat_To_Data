# π¬ WhatsApp chat to data π¬
- - - - 
- creator: JoΓ£o Pedro Longo Zucoloto
- email: joaozuco@gmail.com
- linkedin: https://www.linkedin.com/in/jo%C3%A3o-pedro-longo-zucoloto-169638182/
- - - - 
### This project was developed for you user to have a data view of your Whats App conversations.

#### Features

- π Save your .txt chat file to an excel file having:
    - π date from the message
    - π time that message was sent
    - π§π§ which user sended the message
    - π¬ message
    - π type (text, audio, image...) πΌοΈ
- π Creates Graphs for you visualize data from chat

### How to use
----
    1 - You need to download the chat
        1.1 - Open WhatsApp on your mobile π±
        1.2 - Go to the chat that you want to download π€
        1.3 - Touch on the name up top β
        1.4 - Scroll until you find "Export Chat" ("Exportar conversa" em portuguΓͺs) π
        1.5 - Download the second option "Without Media" ("Sem mΓ­dia" em portuguΓͺs) π
    
#### The "code" folder has this files:
file  | type | description | can_delete
------------- | ------------- | ------------- | -------------
Graphs user_1 - user_2_example  | folder | folder that generates automatically with name from users and stores Graphs  | β β β β
_chat_example.txt  | .txt | example from what your chat file should be like  | β β β β
chat_prety - user_1 - user_2_example.xlsx | .xlsx | example from what will be generated from your chat | β β β β
create_visuualization.py | python script |scrpit to read your chat, create a excel file and graphs | β β β β
whats_app_data.py | python script | module with the used functions | β β β β
requirements | .txt | libaries used to run code | β β β β
    2 - Installing requirements
        2.1 - open cmd and type:
            pip install -r /path/to/requirements.txt
    3 - Paste your file downloaded from chat like this "_chat.txt"
    4 - Finally, run "create_visuualization.py.py"

---
π
