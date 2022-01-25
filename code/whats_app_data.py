from typing import Dict
import pandas as pd


def txt_file_to_list(file: str) -> list:
    """
    Recives:
        - .txt file an
    Returns:
        - list, each item is a line from the .txt file
    """

    data = open(file, 'r', encoding='utf-8')
    reader = data.read()
    content = reader.splitlines()
    return content


def remove_cryptography_line(chat: list()) -> None:
    """
    check if the first line is the cryptography warning
    """
    if 'cryptography' in chat[0]:
        del chat[0]
        print('Cryptography warning message removed :)')


def find_end_of_name(line: str, double_dots: str(':'), occuurence: int) -> int:
    start = line.find(double_dots)
    while start >= 0 and occuurence > 1:
        start = line.find(double_dots, start + len(double_dots))
        occuurence -= 1
    return start


def get_users_automatically(chat: list()) -> dict():
    """
    Get the name from the users.

    Recives:
        - the chat in list format

    Returns:
        - a dict with the name and data from the users colectd in the .txt file
        - example:
                users = {'user_1':
                            {
                                'name':Name from one of the users,
                                'beginning_of_the_name': This will be used later to collect data,
                                'end_of_the_name':This will be used later to collect data
                            },
                         'user_2':...
                            }
    """
    users = {'user_1': {
        'name': '',
        'beginning_of_the_name': 0,
        'end_of_the_name': 0},
            'user_2': {
        'name': '',
        'beginning_of_the_name': 0,
        'end_of_the_name': 0}
                }

    while True:
        for line in chat:
            if line[0] == '[':
                beginning_of_the_name = (line.find(']') + 2)
                end_of_the_name = find_end_of_name(line, ':', 3)

                user_name = line[beginning_of_the_name:end_of_the_name]
                if users['user_1']['name'] == '':
                    users['user_1']['name'] = user_name
                    users['user_1']['beginning_of_the_name'] = beginning_of_the_name
                    users['user_1']['end_of_the_name'] = end_of_the_name
                    continue
                if users['user_2']['name'] == '' and user_name != users['user_1']['name']:
                    users['user_2']['name'] = user_name
                    users['user_2']['beginning_of_the_name'] = beginning_of_the_name
                    users['user_2']['end_of_the_name'] = end_of_the_name

            if users['user_1']['name'] != '' and users['user_2']['name'] != '':
                break
        break

    return users


def organize_data(chat: list(), user_data: dict(), save_in_excel: bool,
                  excel_file_name: str()) -> pd.DataFrame:
    """
    Recives:
        - a list with all the rows from chat
        - a dict with the names from the 2 users
        - bool value if user wants to save excel file

    Returns: a Dataframe having:
        - datetime: date and time that the message was sent
        - who_send: person who sended the message
        - message: message (really?)
        - type: we have different types of messages:
            - audio
            - video
            - photo
            - sticker
            - written
    """

    df = {'datetime': [],
          'who_send': [],
          'message': [],
          'type': []
          }

    user_1_name = user_data['user_1']['name']
    user_1_b = user_data['user_1']['beginning_of_the_name']
    user_1_e = user_data['user_1']['end_of_the_name']

    user_2_name = user_data['user_2']['name']
    user_2_e = user_data['user_2']['end_of_the_name']

    for line in chat:

        line = line.replace('\u200e', '')  # replacing trash data from messages

        # in order to collect date time is simple, this rule never changes

        if len(line) != 0:
            if line[0] == '[':

                try:
                    df['datetime'].append(datetime)
                    df['who_send'].append(who_send)
                    df['message'].append(message)
                    df['type'].append(type)
                except Exception:
                    pass

                datetime = line[1:20]

                if line[user_1_b:user_1_e] == user_1_name:
                    who_send = user_1_name
                    message = line[user_1_e + 2:]
                else:
                    who_send = user_2_name
                    message = line[user_2_e + 2:]

                if message == 'áudio ocultado' or message == 'audio omitted':
                    type = 'Audio'
                elif message == 'vídeo omitido' or message == 'video omitted':
                    type = 'Video'
                elif message == 'imagem ocultada' or message == 'image omitted':
                    type = 'Foto'
                elif message == 'figurinha omitida' or message == 'sticker omitted':
                    type = 'Sticker'
                elif message == 'GIF omitido' or message == 'GIF omitted':
                    type = 'GIF'
                else:
                    type = 'Text'

            else:   # This condition is for messages wich has breakline, so we can concat them
                new_message = line
                message = message + ' ' + new_message

    df['datetime'].append(datetime)
    df['who_send'].append(who_send)
    df['message'].append(message)
    df['type'].append(type)

    if save_in_excel:
        df = pd.DataFrame(df)
        df.to_excel(excel_file_name, index=False)

    return df


# def hour(x):
#     return x[0:2]


def hex_colors() -> Dict:
    _hex = {
        'yellow': '#fff700',
        'light pink': '#ff5efc',
        'light red': '#dd614a',
        'light orange': '#ff9b71',
        'light yellow': '#ffdc7c',
        'light green': '#6ba292',
        'lighter green': '#e4fde1',
        'lighter pink': '#bf7ebd',
        '# of messages per hour': {
            '0':'#04020d',
            '1':'#0a051f',
            '2':'#0b0524',
            '3':'#0a0324',
            '4':'#0a0324',
            '5':'#17275c',
            '6':'#5264a1',
            '7':'#7c8fcc',
            '8':'#9aace6',
            '9':'#cccc62',
            '10':'#e8e858',
            '11':'#e8e83a',
            '12':'#ffff00',
            '13':'#ffc400',
            '14':'#ffbb00',
            '15':'#ffae00',
            '16':'#ffa200',
            '17':'#ff8c00',
            '18':'#111521',
            '19':'#101424',
            '20':'#0a1026',
            '21':'#04091a',
            '22':'#01040d',
            '23':'#000000',
        }
    }
    return _hex
