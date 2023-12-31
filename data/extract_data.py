import pandas as pd

# CSV 파일을 읽어오기
file_path = './data/지역별_상품군별_해외직접판매액.csv'

df = pd.read_csv(file_path, header=None)

# 첫 번째 행을 인덱스로 설정
df.columns = df.iloc[0]

# 컬럼명 변경
new_columns = ['지역별1', '지역별2', '지역별3', '상품군별1', '상품군별2', '판매유형별1', '2019년 1분기', '2019년 2분기', '2019년 3분기', '2019년 4분기', '2020년 1분기', '2020년 2분기', '2020년 3분기', 
               '2020년 4분기', '2021년 1분기', '2021년 2분기', '2021년 3분기', '2021년 4분기', '2022년 1분기', '2022년 2분기', '2022년 3분기', '2022년 4분기', '2023년 1분기', '2023년 2분기', '2023년 3분기']
df.columns = new_columns

#첫 번째 행 제거
df = df[1:]

# '의류 및 패션 관련 상품'과 '음반·비디오·악기'에 해당하는 행 추출
filtered_df = df[(df['지역별1'].isin(['합계', '아시아', '북미', '유럽', '대양주', '중남미', '아프리카', '기타'])) & (df['상품군별1'].isin(['의류 및 패션 관련 상품', '음반·비디오·악기']))]

# 결과 출력
filtered_df.to_csv('./data/extract.csv', index=False, encoding='utf-8-sig')