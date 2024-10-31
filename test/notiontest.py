import requests
import json

# 노션 API 토큰 설정
NOTION_TOKEN = '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'  # 여기에 실제 API 토큰을 입력하세요

# 페이지 ID
PAGE_ID = '1274d9dd132680ed9a5af97a80bfac55'

# API 요청에 필요한 헤더 설정
headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

# 페이지 내용을 가져오는 함수
def get_page_content():
    url = f'https://api.notion.com/v1/blocks/{PAGE_ID}/children/'
    response = requests.get(url, headers=headers)
    return response.json()

# JSON 파일로 저장하는 함수
def save_to_json(data, filename='page_content.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 실행
if __name__ == "__main__":
    # 페이지 내용 가져오기
    page_content = get_page_content()
    print("현재 페이지 내용:")
    print(page_content)

    # JSON 파일로 저장하기
    save_to_json(page_content)
    print("데이터가 'page_content.json' 파일로 저장되었습니다.")
