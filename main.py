from preprocessing import preprocess_mail
import pandas as pd
from openai import OpenAI
from train_your_fine_tuned_model import fit_fine_tuned

api_key = "api-key"
client = OpenAI(api_key=api_key)

"""
Kaynakça:
    
    https://platform.openai.com/docs/overview
    https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models
    https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus

"""


########################################## .txt dosyasından .csv dosyasına

synthetic_data_size = 1 # Sentezlemek istediğimiz data sayısı

text = preprocess_mail.reading_txt_file("fradulent_emails.txt") # .txt dosyasının içindeki veriyi stringe atıyor
mails = preprocess_mail.split_store_list(text, "From r") # Bütün mail bloklarını bir listeye atıyoruz.
tabular_data = [] 
for mail in mails[1:len(mails) - 2]:
    tabular_data.append(preprocess_mail.taking_feature(mail)) # Her mail bloğu için feature extracting metodlarımızı uyguluyoruz.

tabular_data = pd.DataFrame(tabular_data) # .csv formatında verimizi geri almak için pd.DataFrame 

tabular_data.to_csv("data.csv") # data.csv dosyası olarak çıktı aldık.
print(tabular_data.head()) # Nasıl görünüyor bakıyoruz.


########################################## .jsonl dosyasını çıkarmak için kullanıcıyla ortaklaşa çalışıyoruz

"""
Bu kod bloğunun görevi
1. Maili kullanıcıya gösteriyoruz.
2. Kullanıcıdan input alıyoruz bu aldığımız inputu user content için kullanıyoruz.
3. Daha sonra maili JSON formatına çeviriyoruz.

"""

number_of_fitted_fine_tuned_data = 1 # Kaç datayı JSON formatına çevireceğiz 

data = pd.read_csv("data.csv", index_col=0)  # Tabular data'yı okuyoruz
mails = data.loc[:, "Mail"] # Mailleri ayrı bir objeye atıyoruz.

with open("last_pos.txt", "r+") as f: # Okuduğumuz datayı tekrar okumamak için son pozisyonumuzu last_pos.txt dosyasına atıyoruz.
    if not f.read():
        f.write("0")
    f.seek(0)
    last_pos = int(f.read())

for i in range(last_pos, last_pos + number_of_fitted_fine_tuned_data): # Kaç adet maili dolduracağız.

    print(mails[i]) # Mail
    assistant_content = str(input("What should be assistant content?\n")) # User content

    conversations = [
        {
            "messages": [
            {"role": "system", "content": "You represent an organization that engages in e-mail fraud for academic purposes."},
            {"role": "user", "content": f"{assistant_content}"},
            {"role": "assistant", "content": f"{mails[i]}"}
            ]
        }]
    
    preprocess_mail.write_data_to_jsonl("data.jsonl", conversations)

    with open("last_pos.txt", "r+") as f:
        f.truncate(0)
        f.write(str(i))

########################################## Fit fine-tunned model
        
fit_fine_tuned(api_key).fit(jsonl_data="data.jsonl") # Sitede modelin fit olduğundan emin olun ve use_your_fine_tuned_model.py programından yeni verileri sentezleyebilirsiniz.
