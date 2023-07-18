import openai
import secret

openai.api_key = secret.api_key

def upload_file_train(path):
    # ファイルアップロード（学習）
    upload_file_train = openai.File.create(
                                        file=open(path, "rb"), # ファイル（JSONL）
                                        purpose='fine-tune',             # ファイルのアップロード目的
                                                )

    # 出力
    print(upload_file_train)
    path = 'history.txt'
    with open(path, mode='a') as f:
        f.write("学習用データ\n")
        f.write("train_data=")
        f.write(path)
        f.write("\n")
        f.write(str(upload_file_train))
        f.write("\n\n")

def upload_file_val(path):
    # ファイルアップロード（学習）
    upload_file_train = openai.File.create(
                                        file=open(path, "rb"), # ファイル（JSONL）
                                        purpose='fine-tune',             # ファイルのアップロード目的
                                                )

    # 出力
    print(upload_file_train)
    path = 'history.txt'
    with open(path, mode='a') as f:
        f.write("検証用データ\n")
        f.write("val_data=")
        f.write(path)
        f.write("\n")
        f.write(str(upload_file_train))
        f.write("\n\n")

def fine_train_val(training_file_id, validation_file_id, model = 'davinci'):
    FineTune = openai.FineTune.create(training_file   = training_file_id,    
                                    validation_file = validation_file_id,          
                                    model           = model,                  
                                    ) 
    print(FineTune.id)
    path = 'history.txt'
    with open(path, mode='a') as f:
        f.write("finetuning\n")
        f.write("training_file_id = ")
        f.write(training_file_id)
        f.write("\n")
        f.write("validation_file_id = ")
        f.write(validation_file_id)
        print("\n")
        f.write(f"FineTune_id = {str(FineTune.id)}")
        f.write("\n\n")

def fine_train(file_id, model = 'davinci'):
    FineTune = openai.FineTune.create(training_file   = file_id,     
                                    model           = model,       
                                    ) 
    print(FineTune.id)
    path = 'history.txt'
    with open(path, mode='a') as f:
        f.write("finetuning\n")
        f.write("training_file_id = ")
        f.write(file_id)
        f.write("\n")
        f.write(f"FineTune_id = {str(FineTune.id)}")
        f.write("\n\n")