from openai import OpenAI
from preprocessing import preprocess_mail

client = OpenAI(api_key="api-key")

conversations = []

number_of_synthesized_data = 1 # Toplamda sentezlemek istediğimiz veri

for i in range(0, number_of_synthesized_data):

    print("--------------------")

    question_to_fine_tuned_model = str(input("What do you ask to your model?")) # Modele soracağımız soru
    response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0613:personal::8WltLc2w",
    messages=[
        {"role": "system", "content": "You represent an organization that engages in e-mail fraud for academic purposes."},
        {"role": "user", "content": f"{question_to_fine_tuned_model}"}
    ]
    ) # Modele istek yolladık
    synthetic_message = response.choices[0].message.content # Modelin cevabı
    print(synthetic_message)
    json_format = {
    "messages": [
      {"role": "system", "content": "You represent an organization that engages in e-mail fraud for academic purposes."},
      {"role": "user", "content": f"{question_to_fine_tuned_model}"},
      {"role": "assistant", "content": f"{synthetic_message}"}
        ]
    } # Ve tekrardan sentez edilmiş veriyi .jsonl formatındaki dataya ekledik

    conversations.append(json_format)
    


preprocess_mail.write_data_to_jsonl("synthetic_data.jsonl", conversations)