import pandas as pd
import json

class preprocess_mail:

    def write_data_to_jsonl(filepath, data): 
        """
        JSON formatında oluşturulan veriyi ".jsonl" formatındaki dosyaya kaldığı yerden devam edecek şekilde ekliyoruz

        Args:
            filepath: ".jsonl" formatındaki dosyanın yolu
            data: İçinde JSON formatında oluşturulan verilerin liste hali. Datatipi Python List'dir.

        JSON formatındaki verinin şablonu:
            {
            "messages": [
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {"role": "user", "content": "What's the best way to avoid traffic?"},
            {"role": "assistant", "content": "Leave before dawn... or after everyone else arrives at work. You choose."}
                ]
            }


        """  
        with open(filepath, "a") as f:
            for conversation in data:
                json.dump(conversation, f)
                f.write("\n")

    def reading_txt_file(path):
        """
        ".txt" dosya tipinin içerisindeki veriyi string formatında döndüren fonksiyon

        Args:
            path: Dosya Yolu
        
        """
        with open(path, "r") as f:
            txt = f.read()
        return str(txt)
    
    def split_store_list(text, sub_string):
        """
        string kütüphanesinin içerisindeki .split fonksiyonunu input parametrelerine göre kullanıp listeye döndüren fonksiyon

        Args:
            text: .split fonksiyonunu kullanacağımız string tipi obje
            sub_string: Ayırmak için referans olarak aldığımız alt string

        """
        pure_list = text.split(sub_string)
        return [part for part in pure_list]
    
    def taking_feature(mail):
        """
        ".txt" formatındaki indirilen veri setinin içerisindeki bloklar halinde bulunan mailleri feature'larına ayırmak için kullanılan fonksiyon

        Args:
            mail: ".txt" formatındaki maillerden oluşan veri setinin içerisindeki bir block mail
        
        """

        def control_feature_in_list(sentence, feature_types, double_dot=True):
            """
            Bir stringin içerisinde bulunan substringlerin varlığıyla ve aynı substringlerin verilen listenin içerisinde olup olmadığını test eden fonksiyon

            Args:
                sentence: substringlerin bulunma ihtimali olan string
                feature_types: aradığımız substringler
                double_dot: Verinin içerisinde bazı feature'ların sonlarında iki nokta üstüste oluyordu (":"). Aradığımız veri tipi o ise True olacak şekilde fonksiyonu formatlıyoruz.
            
            """
            for i in feature_types:
                if double_dot == True and i + ":" in sentence:
                    return i
                elif i in sentence:
                    return i
            return 0
        
        def char_before_after(char, sentence):
            """
            string'in içerisinde bulunan belli bir char'ın öncesini ve sonrasını liste olarak veren fonksiyon

            Args:
                char: O belirli olan char
                sentence: 2'ye bölmek istediğimiz string
            
            """ 

            for i in range(len(sentence)):
                if char == sentence[i]:
                    return [sentence[0:i], sentence[i+2:len(sentence)]]
            
            return 0

        
        def taking_header_feature(sentence):
            """
            Kaggle'dan indirilen verisetinin içerisinde bulunan maili tanımlayan header featurelarını yakalayan fonksiyon

            Args:
                sentence: mail bloğunun içerisinde bulunan "\n" ile ayrılan substring

            """

            feature_types = ["Return-Path", "X-Sieve", "Return-Path", "Message-Id", "From", "Reply-To",
                             "To", "Date", "Subject", "X-Mailer", "MIME-Version", "Content-Type", "Content-Transfer-Encoding",
                             "X-MIME-Autoconverted", "Status"]
            if control_feature_in_list(sentence, feature_types):
                feature = control_feature_in_list(sentence, feature_types)
                splitted_sentence = char_before_after(":", sentence)
                key = feature
                value = splitted_sentence[1]
                row_value = [key, value]
                return row_value
            else:
                return 0

        sentence_list = [part for part in mail.split("\n")]
        tabular_data_row_dict = {"Mail" : ""}
        months = ["Jan ", "Feb ", "Mar ", "Apr ", "May ", "Jun ", "Jul ", "Aug ", "Sep ", "Oct ", "Nov ", "Dec "]
        for sentence in sentence_list:
            if ":" in sentence and taking_header_feature(sentence):
                feature = taking_header_feature(sentence)
                tabular_data_row_dict[feature[0]] = feature[1]
            elif "\n" == sentence or "" == sentence:
                pass
            elif sentence == "None":
                pass
            else:
                if control_feature_in_list(sentence, months, False):
                    tabular_data_row_dict["Date_F"] = sentence[2:len(sentence)]
                else:
                    tabular_data_row_dict["Mail"] += sentence
                    tabular_data_row_dict["Mail"] += "\n"
            
        return tabular_data_row_dict

def main():

    text = preprocess_mail.reading_txt_file("fradulent_emails.txt")
    mails = preprocess_mail.split_store_list(text, "From r")
    tabular_data = []
    for mail in mails[1:len(mails) - 2]:
        tabular_data.append(preprocess_mail.taking_feature(mail))

    tabular_data = pd.DataFrame(tabular_data)

    tabular_data.to_csv("data.csv")
    print(tabular_data.head())

    
    
    

if __name__ == "__main__":
    main()