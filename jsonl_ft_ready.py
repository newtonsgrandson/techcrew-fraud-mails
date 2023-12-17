import pandas as pd
from openai import OpenAI
import json
from preprocessing import preprocess_mail

client = OpenAI(api_key="api_key")

def main():

    data = pd.read_csv("data.csv", index_col=0)
    mails = data.loc[:, "Mail"]

    with open("last_pos.txt", "r+") as f:
        if not f.read():
            f.write("0")
        f.seek(0)
        last_pos = int(f.read())

    for i in range(last_pos, len(mails)):
        print(mails[i])

        assistant_content = str(input("What should be assistant content?\n"))

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
            

def main2():
    # Generate example conversations
    conversations = [
    {
        "messages": [
        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "What's the best way to avoid traffic?"},
        {"role": "assistant", "content": "Leave before dawn... or after everyone else arrives at work. You choose."}
        ]
    },
    {
        "messages": [
        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "Tell me something funny."},
        {"role": "assistant", "content": "Sure, why don't I tell you about my love life? Oh wait, that's just a single life."}
        ]
    },
    {
        "messages": [
        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "What's the meaning of life?"},
        {"role": "assistant", "content": "The meaning of life? To avoid existential crises, obviously."}
        ]
    }
    ]

    # Write data to a ".jsonl" file
    preprocess_mail.write_data_to_jsonl("sarcastic_bot_data.jsonl", conversations)

    print("Sarcastic bot data written to 'sarcastic_bot_data.jsonl'")

            


    



if __name__ == "__main__":
    main()