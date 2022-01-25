import os
import pandas as pd
import plotly_express as px
import whats_app_data as wad
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

hex_colors = wad.hex_colors()

chat = wad.txt_file_to_list('_chat.txt')  # reading .txt file

wad.remove_cryptography_line(chat)

users = wad.get_users_automatically(chat)
excel_file_name = f"chat_prety - {users['user_1']['name']} - {users['user_2']['name']}.xlsx"

df = wad.organize_data(chat, users, excel_file_name = excel_file_name, save_in_excel=True)
df = pd.DataFrame(df)
df = pd.read_excel(excel_file_name, engine='openpyxl')
df.reset_index(level=None, drop=False, inplace=True, col_level=0, col_fill='')

graph_folder = f"Graphs {users['user_1']['name']} - {users['user_2']['name']}"
if not os.path.exists(graph_folder):
    os.makedirs(graph_folder)  # creating folder to store the graphs

df["datetime"]= pd.to_datetime(df["datetime"])
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
df['hour'] = df['datetime'].dt.hour

df_d = df.groupby(by=["date", "who_send"], sort=False).count()['index']
df_d = df_d.reset_index(drop=False)
df_d = pd.DataFrame(df_d)

# 1º - Graph
new_order = list(df_d['date'].unique())
fig = px.line(df_d, x='date', y="index", title='Number of messages per day',
              labels={
                  'date':'Date',
                  'who_send':'Who sended',
                  'index':'Number of messages',
              },
              category_orders={'date': new_order},
              color='who_send')
fig['data'][1]['line']['color'] = hex_colors['yellow']
fig['data'][0]['line']['color'] = hex_colors['light pink']
fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x")
fig.update_xaxes(type='category')
fig.write_html(f"{graph_folder}/# of messages per day.html")

# 2º - Graph
df_d = df.groupby(by=['type']).count()['index']
df_d = df_d.reset_index(drop=False)
fig = px.bar(df_d.sort_values(by=['index'], ascending=False), x='type', y='index',
             labels={
                  'index':'Number of messages',
                  'type':'Type of messsage',
              },
             color='type', text='index', title='Number of type of messages',
             hover_name="type", hover_data=["index"])
try:
    fig['data'][0]['marker']['color'] = hex_colors['light red']
    fig['data'][1]['marker']['color'] = hex_colors['light orange']
    fig['data'][2]['marker']['color'] = hex_colors['light yellow']
    fig['data'][3]['marker']['color'] = hex_colors['light green']
    fig['data'][4]['marker']['color'] = hex_colors['lighter green']
    fig['data'][5]['marker']['color'] = hex_colors['lighter pink']
except Exception:
    pass
fig.update_traces(texttemplate='', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.write_html(f"{graph_folder}/# of type of messages.html")

# 3º - Graph
df_d = df.groupby(by=["who_send", "type"]).count()["index"]
df_d = df_d.reset_index(drop=False)
fig = px.bar(df_d, x="who_send", y="index", color='type',
             title='Number type of messasge per user',
             labels={
                  'index':'Number of type messages',
                  'who_send':'Who sended',
                  'type':'Type'
              },
              hover_name="type", hover_data=["index"])
try:
    fig['data'][0]['marker']['color'] = hex_colors['light red']
    fig['data'][1]['marker']['color'] = hex_colors['light orange']
    fig['data'][2]['marker']['color'] = hex_colors['light yellow']
    fig['data'][3]['marker']['color'] = hex_colors['light green']
    fig['data'][4]['marker']['color'] = hex_colors['lighter green']
    fig['data'][5]['marker']['color'] = hex_colors['lighter pink']
except Exception:
    pass
fig.write_html(f"{graph_folder}/# type of messasge per user.html")

# 4º - Grah
df_d = df.groupby(by=["hour"]).count()['index']
df_d = df_d.reset_index(drop=False)
df_d = df_d.sort_values('hour', ascending=True)
fig = px.bar(df_d, x='hour', y='index',
             text='index',
             color="hour",
             title='Number of messages per hour',
             labels={
                  'index':'Number of messages',
                  'hour':'Hour'
              }
            )
fig.update_traces(texttemplate='', textposition='outside')
fig.update_xaxes(
    showgrid=True,
    ticks="outside",
    tickson="boundaries",
    ticklen=20
)
fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = df_d['hour'].tolist(),
        ticktext = df_d['hour'].tolist()
    )
)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.write_html(f"{graph_folder}/# of messages per hour.html")

# 5º - Word Cloud
df_f = df[df['type'] == 'Text']
summary = df_f['message']
all_summary = " ".join(str(s) for s in summary)
stopwords = set(STOPWORDS)
stopwords.update(['mas', 'da', 'meu', 'em',
                  'de', 'ao', 'os', 'que', 'eu',
                  'ma', 'pra', 'para',
                  'uma', 'um', 'Ma', 'e',
                  'você', 'o', 'não', 'sim',
                  'se', 'mano', 'ta', 'tá',
                  'só', 'é'])

wordcloud = WordCloud(stopwords=stopwords,
                      background_color='black', width=1600,
                      height=800).generate(all_summary)
fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file(f'{graph_folder}/WorldCloud.png')
