# 💬 WhatsApp chat to data 💬
- - - - 
- creator: João Pedro Longo Zucoloto
- email: joaozuco@gmail.com
- linkedin: https://www.linkedin.com/in/jo%C3%A3o-pedro-longo-zucoloto-169638182/
- - - - 
### This project was developed for you user to have a data view of your Whats App conversations.

#### Features

- 📝 Save your .txt chat file to an excel file having:
    - 📅 date from the message
    - 🕗 time that message was sent
    - 👫 which user sended the message
    - 💬 message
    - 🔊 type (text, audio, image...) 🖼️
- 📊 Creates Graphs for you visualize data from chat

### How to use
----
    1 - You need to download the chat
        1.1 - Open WhatsApp on your mobile 📱
        1.2 - Go to the chat that you want to download 🤔
        1.3 - Touch on the name up top ☝
        1.4 - Scroll until you find "Export Chat" ("Exportar conversa" em português) 👇
        1.5 - Download the second option "Without Media" ("Sem mídia" em português) 👌
    
#### The "code" folder has this files:
file  | type | description | can_delete
------------- | ------------- | ------------- | -------------
Graphs user_1 - user_2_example  | folder | folder that generates automatically with name from users and stores Graphs  | ✅
_chat_example.txt  | .txt | example from what your chat file should be like  | ✅
chat_prety - user_1 - user_2_example.xlsx | .xlsx | example from what will be generated from your chat | ✅
create_visuualization.py | python script |scrpit to read your chat, create a excel file and graphs | ❌
whats_app_data.py | python script | module with the used functions | ❌
requirements | .txt | libaries used to run code | ❌
    2 - Installing requirements
        2.1 - open cmd and type:
            pip install -r /path/to/requirements.txt
    3 - Paste your file downloaded from chat like this "_chat.txt"
    4 - Finally, run "run.py"


