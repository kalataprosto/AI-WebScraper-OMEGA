from openai import OpenAI

class AIScraper:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def analyze_page(self, html: str) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{
                "role": "system",
                "content": "Analyze this HTML and extract structured data"
            }, {
                "role": "user", 
                "content": html[:15000]
            }],
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
