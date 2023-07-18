import PySimpleGUI as sg

#テーマを決めます。
#テーマの種類は、sg.preview_all_look_and_feel_themes()で確認できます。
sg.theme("DarkBlue")

tab_file_layout =  [
    [sg.Text('現在のファイル')],
    [sg.Output(s=(40,15))],
]

tab_model_layout = [
    [sg.Text('現在のモデル')],
    [sg.Output(s=(40,15))],
]

tab_upload_file_layout =  [
    [sg.Text('トレーニングデータのファイルパス')],
    [sg.Input(key='train_file_path')],
    [sg.Text('検証データのファイルパス')],
    [sg.Input(key='val_file_path')],
    [sg.Button('upload')]
]

radio_train_dic = {
    '-1-': 'file_path',
    '-2-': 'file_id',
}
radio_val_dic = {
    '-1-': 'file_path',
    '-2-': 'file_id',
}

tab_create_model_layout = [
    [sg.Text('トレーニングデータ')],
    [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_train_dic.items()],
    [sg.Input(key='train_file')],
    [sg.Text('検証データ')],
    [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_val_dic.items()],
    [sg.Input(key='val_file')],
    [sg.Text('ベースモデル')],
    [sg.Combo(values=['ada', 'babbage','curie','davinci'], size=(20, 1), key='MODEL')],
    [sg.Button('create')]
]

#表示する画面の設定をします。
layout= [
        [sg.TabGroup([[sg.Tab('file',tab_file_layout), sg.Tab('model', tab_model_layout)]]), sg.TabGroup([[sg.Tab('uploadfile',tab_upload_file_layout), sg.Tab('create_model', tab_create_model_layout)]])],
        ]

window=sg.Window("GPTfine_tuning",layout)

#無限ループで画面を表示させます。×ボタンで無限ループを抜けます。
while True:
    event,values=window.read()
    if event == sg.WIN_CLOSED:
        break

#画面を閉じます。
window.close()