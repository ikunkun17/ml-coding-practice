import pandas as pd

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample.csv'
sample = pd.read_csv(file_url)

print(sample.head())
print(sample.tail())

sample.info()
sample.describe()

sample_dic = {'name': ['David','John','Isaac'], 'age': [24,25,27]}
a = pd.DataFrame(sample_dic)

a.info()

pd.DataFrame([[2,3],[4,5],[6,7],[8,9]])
pd.DataFrame([[2,3],[4,5],[6,7],[8,9]], columns = ['var_2','var_3'], index=['b','c','d','e'])

import pandas as pd
file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample_df.csv'

sample_df = pd.read_csv(file_url, index_col=0)
print(sample_df.head())

print(sample_df['var_5'])

# print(sample_df['var_1', 'var_2'])   # [ ] 안에는 하나의 값만 들어갈 수 있음
print(sample_df[['var_1', 'var_4']])   # [ [] ]를 사용하면 [] 가 하나의 값으로 인식됨

# loc 는 location의 앞글자
print(sample_df.loc['b'])              # 행 기준으로 인덱싱
print(sample_df.loc[['b','d','f']])
print(sample_df.loc['b':'d'])

# iloc: integer location의 약자
print(sample_df.iloc[[1,2,3]])
print(sample_df.iloc[0:3])
print(sample_df.iloc[0:4])
print(sample_df.iloc[0:4, 1:5])        # 컬럼까지 동시에 인덱싱

print(sample_df.drop(['var_2','var_3'], axis=1))     # 컬럼을 제거하려면 axis = 1
print(sample_df.drop(['var_2','var_3'], axis=1))
print(sample_df.drop(['d','e','f'], axis=0))         # 행을 제거하려면 axis = 0 또는 디폴트로 사용

netflix = pd.read_csv('2.1.1.netflix.csv')
print(netflix.head())

print(netflix['release_year'])
print(netflix['release_year'] > 2015)

more2015 = netflix[netflix['release_year'] > 2015]
print(more2015.head(7))

print(~(netflix['release_year'] > 2015))
less2015 = netflix[~(netflix['release_year'] > 2015)]
print(less2015.head())

print((netflix['release_year'] > 2015) & (netflix['type'] == 'Movie'))

more2015_tv = netflix[(netflix['release_year'] > 2015) & (netflix['type'] == 'Movie')]
print(more2015_tv.head())

more2015_or_tv = netflix[(netflix['release_year'] > 2015) | (netflix['type'] == 'Movie')]
print(more2015_or_tv.head())

data = {
    'name': ['Ally', 'Brian', 'Charles', 'Dawin', 'Eve', 'Frankey', 'Gloria', 'Johan'],
    'comment_length': [200, 250, 100, 200, 150, 170, 55, 155],
    'likes': [40, 20, 30, 55, 10, 45, 7, 29],
    'is_spam': [True, False, False, False, False, True, False, False],
    'has_image': [True, False, True, True, False, False, True, True]
}
df = pd.DataFrame(data)
print(df.head())

# 필터링 조건 설정
condition = (
  (df['comment_length'] >= 50) &       # 댓글 길이 100자 이상
  (df['likes'] >= 30) &                 # 좋아요 20개 이상
  (~df['is_spam']) &                    # 스팸 댓글이 아니어야 함
  (df['has_image'])                     # 이미지가 포함된 댓글이어야 함
)

# 조건을 만족하는 행들 필터링
winner_df = df[condition]
print(winner_df)

print(sample_df.reset_index())

print(sample_df.reset_index(drop=True))          # 기존 인덱스는 제거하기

print(sample_df.set_index('var_2'))


print(sample_df.describe())
print(sample_df.std())
print(sample_df.agg(['mean','count', 'min', 'max', 'std']))

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/iris.csv'
iris = pd.read_csv(file_url)

print(iris.head())

print(iris.groupby('class').std())

print(iris.drop('class', axis=1).agg(['sum','mean', 'std']))

# print(iris.agg(['sum','mean', 'std']))    # class 컬럼으로 인해 에러 발생


print(iris['class'].unique())
print(iris['class'].nunique())
print(iris['class'].value_counts())

# 예제 데이터 생성
data = {
    'name': ['Ally', 'Johan', 'Charles', 'Isaac', 'Ellis'],
    'age': [30, 35, 40, 27, 45],
    'salary': [80000.00, 90000.00, 60000.00, 50000.00, 85000.00]
}

# Dataframe 생성
df = pd.DataFrame(data)
print(df.head())

# 나이가 30 이상인 직원의 이름과 급여 반환
result = df[df['age'] >= 40][['name', 'salary']]
print(result)

# 예제 데이터 생성
data = {
    'name': ['Ally', 'David', 'Charles', 'Isaac', 'Evan'],
    'math': [87, 90, 87, 67, 96],
    'science': [84, 86, 85, 94, 87],
    'english': [92, 84, 83, 82, 95]
}

# Dataframe 생성
df = pd.DataFrame(data)
print(df.head())

# 개인별 과목 점수의 평균값 계산 (axis=1)
df['average'] = df[['math', 'science', 'english']].mean(axis=1)
print(df)

# 이름과 평균값만을 포함하는 새로운 데이터프레임 생성
average_df = df[['name', 'average']]
print(average_df)

# 2.2 넘파이
import numpy as np

print(np.array([2,3,4]))

print(np.array([[2,3,4],
                [5,6,7],
                [8,9,10]]))

print(np.array([[[2,3,4],
                [5,6,7],
                [8,9,10]],
                [[2,3,4],
                [5,6,7],
                [8,9,10]],
                [[2,3,4],
                [5,6,7],
                [8,9,10]]]))

print(np.array([2,3,4,5,6]))
print(np.array(sample_df))

sample_np = np.array(sample_df)
print(pd.DataFrame(sample_np))      # 컬럼명이 0, 1, 2, 3, 4

print(sample_df.columns)            # 기존 프레임워크에서 컬럼명 가져오기

print(pd.DataFrame(sample_np, columns = sample_df.columns))      # 새 프레임워크에 컬럼명 붙이기

print(sample_np)
print(sample_np[2])
print(sample_np[2,3])
print(sample_np[2:4,3:5])
print(sample_np[:,3])

np_a = np.array([[2,3], [1,-3]])
print(np_a)
print(np_a + 10)
print(np_a - 5)
print(np_a * 2)
print(np_a+10 / 3)

np_b = np.array([[1,0], [0,1]])
print(np_b)
print(np_a + np_b)
print(np_a - np_b)
print(np_a * np_b)
print(np_a @ np_b)

print(np.random.randint(11))
print(np.random.randint(50, 71))
print(np.random.randint(50, 71, 10))
print(np.random.choice(['red', 'green','white','black','blue'],size=3))
print(np.random.choice(['red', 'green','white','black','blue'],size=3, replace=False))

print(np.arange(1,11))
print(np.arange(1,11,2))
print(np.linspace(1,100,10))       # 1부터 10까지 균등한 간격의 값을 4개 추출

A = np.array([4, 16, 25])
print(np.sqrt(A))

print(np.arange(8).reshape(2, 4) + 10)

# 0부터 8 미만까지 출력하고 (2, 4) 크기로 재가공 후, 제곱하여 출력
a = np.arange(8).reshape(2, 4) ** 2
print(a)

print(a.sum())     # 모든 요소의 합
print(a.mean())    # 모든 요소의 평균
print(a.mean(axis = 0))    # 열을 기준으로 연산

print(a.min())    # 모든 요소 중 최솟값
print(a.max())    # 모든 요소 중 최댓값

print(a.max(axis=1))
print(a.cumsum())        # 모든 요소의 누적합
print(a.argmax())        # 모든 요소 중 최댓값의 인덱스