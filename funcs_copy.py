import openai
import secret
import PySimpleGUI as sg

openai.api_key = secret.api_key

def upload_file_train(path):
    path = path.replace('"', '')
    # ファイルアップロード（学習）
    upload_file_train = openai.File.create(
                                        file=open(path, "rb"), # ファイル（JSONL）
                                        purpose='fine-tune',             # ファイルのアップロード目的
                                                )

    # 出力
    print(upload_file_train)
    path = 'history.txt'
    with open(path, mode='a',encoding='utf-8') as f:
        f.write("学習用データ\n")
        f.write("train_data=")
        f.write(path)
        f.write("\n")
        f.write(str(upload_file_train))
        f.write("\n\n")
    return upload_file_train.id

def upload_file_val(path):
    path = path.replace('"', '')
    # ファイルアップロード（学習）
    upload_file_train = openai.File.create(
                                        file=open(path, "rb"), # ファイル（JSONL）
                                        purpose='fine-tune',             # ファイルのアップロード目的
                                                )

    # 出力
    print(upload_file_train)
    path = 'history.txt'
    with open(path, mode='a',encoding='utf-8') as f:
        f.write("検証用データ\n")
        f.write("val_data=")
        f.write(path)
        f.write("\n")
        f.write(str(upload_file_train))
        f.write("\n\n")
    return upload_file_train.id
        
def create_model(values):
    # トレーニングファイルの情報無かったらエラー表示
    if not values['train_file']:
        sg.popup_error('トレーニングファイルは必須です。')
        return
    
    # ファイルのパスまたはidの取得
    if values['-is_file_path0-']:
        ok_cancel = sg.popup_ok_cancel('ファイルのアップロードを行い、その後fine-tuningを実行します。よろしいですか？\n(既にアップロード済みのファイルの場合重複します)')
        train_file_path = values['train_file']
    else:
        train_file_id = values['train_file']
    if values['-is_file_path1-']:
        if not ok_cancel: # ポップアップの表示は一度だけになるように
            ok_cancel = sg.popup_ok_cancel('ファイルのアップロードを行い、その後fine-tuningを実行します。よろしいですか？\n(既にアップロード済みのファイルの場合重複します)')
        val_file_path = values['val_file']
    else:
        val_file_id = values['val_file']
    
    # ポップアップ確認でokだった場合ファイルのアップロード、file_idの取得。その他の場合処理終了    
    if ok_cancel == 'OK':
        if train_file_path:
            train_file_id = upload_file_train(train_file_path)
        if val_file_path:
            val_file_id   = upload_file_val(val_file_path)
    else:
        return
        
    # モデルの取得
    model = values['MODEL']
        
    if train_file_id:
        FineTune = openai.FineTune.create(training_file   = train_file_id,
                                            model         = model,) 
        if val_file_id:
            FineTune = openai.FineTune.create(training_file = train_file_id,    
                                            validation_file = val_file_id,          
                                            model           = model,) 
    
    path = 'history.txt'
    with open(path, mode='a',encoding='utf-8') as f:
        f.write("finetuning\n")
        f.write(f"{str(FineTune)}")
        f.write("\n\n")
        