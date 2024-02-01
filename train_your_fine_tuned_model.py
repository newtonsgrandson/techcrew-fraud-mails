from openai import OpenAI

class fit_fine_tuned:
    def __init__(self, api_key):
        """
        Sınıf constructor'ı
        
        Args:
            api_key: OpenAI API key
        
        """
        self.api_key = api_key
        self.client = OpenAI(api_key="api-key")
        
    def fit(self, jsonl_data):
        """
        Fine tunne modeli fit etmek için OpenAI apisini kullanıyoruz

        Args:
            jsonl_data: Fit edeceğimiz .jsonl data

        
        """
        file = self.client.files.create(
            file = open(jsonl_data, "rb"),
            purpose="fine-tune"
        )

        self.client.fine_tuning.jobs.create(
            training_file=file.id,
            model="gpt-3.5-turbo"
        )