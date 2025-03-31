!pip install python-dotenv

import os
from dotenv import load_dotenv

# .env 파일의 환경변수 로드
load_dotenv()

# 환경변수 사용
api_key = os.getenv('API_KEY')
db_password = os.getenv('DB_PASSWORD')

print(api_key)  # 'your-api-key-here'
print(db_password)  # 'supersecretpassword'
