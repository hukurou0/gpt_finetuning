# カレントディレクトリをconsole.pyのある場所に移動
import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)

import PySimpleGUI as sg
import funcs_copy

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
    [sg.Button('upload', key='file_upload')]
]

tab_create_model_layout = [
    [sg.Text('トレーニングデータ')],
    [sg.Radio('file-path', key='-is_file_path0-', group_id='0', default=True), sg.Radio('file-id', key='-is_file_id0-', group_id='0')],
    [sg.Input(key='train_file')],
    [sg.Text('検証データ')],
    [sg.Radio('file-path', key='-is_file_path1-', group_id='1', default=True), sg.Radio('file-id', key='-is_file_id1-', group_id='1')],
    [sg.Input(key='val_file')],
    [sg.Text('ベースモデル')],
    [sg.Combo(values=['ada', 'babbage','curie','davinci'], size=(20, 1), key='MODEL')],
    [sg.Button('create',key='create_model')]
]

layout= [
        [sg.TabGroup([[sg.Tab('file',tab_file_layout), sg.Tab('model', tab_model_layout)]]), sg.TabGroup([[sg.Tab('uploadfile',tab_upload_file_layout), sg.Tab('create_model', tab_create_model_layout)]])],
        ]

window=sg.Window("GPTfine_tuning",layout)


while True:
    event,values=window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == "file_upload":
        path = values['train_file_path']
        try:
            if path:
                funcs_copy.upload_file_train(path)
            path = values['val_file_path']
            if path:
                funcs_copy.upload_file_val(path)
            sg.popup('アップロード完了しました')
        except Exception as e:
            sg.popup(f'{e}')
        window['train_file_path']. Update('')
        window['val_file_path']. Update('')
        
    elif event == "create_model":
        try:
            funcs_copy.create_model(values)
        except Exception as e:
            sg.popup(f'{e}')

#画面を閉じます。
window.close()