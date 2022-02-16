# 파일을 찾아주는 glob

import glob

# csv 파일을 sub_folder 라는 이름의 폴더에서 찾고 싶을 때

csv_files = glob.glob('/folder/sub_folder/*.csv')

# csv 파일을 하위 폴더에서 모두 찾고 싶을 때

csv_files = glob.glob('/folder/**/*.csv', recursive=True)
