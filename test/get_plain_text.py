import requests
import json

# 노션 API 토큰 설정
NOTION_TOKEN = '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'  # 여기에 실제 API 토큰을 입력하세요
PAGE_ID = '1274d9dd132680ed9a5af97a80bfac55'  # 여기에 실제 페이지 ID를 입력하세요

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

# 모든 plain_text를 추출하는 함수
def extract_plain_text(blocks):
    plain_texts = []
    for block in blocks.get('results', []):
        if 'paragraph' in block:
            for text in block['paragraph']['rich_text']:
                plain_texts.append(text['plain_text'])
    return plain_texts

# 실행
if __name__ == "__main__":
    # 페이지 내용 가져오기
    page_content = get_page_content()
    print("현재 페이지 내용:")
    
    # plain_text 추출
    plain_texts = extract_plain_text(page_content)
    print("추출된 plain_text:")
    print(plain_texts)

    # JSON 파일로 저장하기
    with open('plain_texts.json', 'w', encoding='utf-8') as f:
        json.dump(plain_texts, f, ensure_ascii=False, indent=4)
    print("데이터가 'plain_texts.json' 파일로 저장되었습니다.")
