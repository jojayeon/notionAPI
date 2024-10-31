import requests
import json

# 노션 API 토큰 설정
NOTION_TOKEN = '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'   # 여기에 실제 API 토큰을 입력하세요
DATABASE_ID = '1274d9dd-1326-80ed-9a5a-f97a80bfac55'  # 여기에 실제 데이터베이스 ID를 입력하세요

# API 요청에 필요한 헤더 설정
headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

# JSON 파일에서 데이터를 읽어오는 함수
def read_plain_texts(filename='plain_texts.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# 데이터를 데이터베이스에 삽입하는 함수
def insert_into_database(data):
    url = f'https://api.notion.com/v1/pages'
    for text in data:
        page_data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Name": {  # 여기에 속성 이름을 맞게 수정하세요
                    "title": [
                        {
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }
            }
        }
        response = requests.post(url, headers=headers, json=page_data)
        print(response.json())

# 실행
if __name__ == "__main__":
    plain_texts = read_plain_texts()
    insert_into_database(plain_texts)
