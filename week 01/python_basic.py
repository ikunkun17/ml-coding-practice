a = 4
b = 7

# 지수승
print(a ** b)
print(a ** 4)

# 나머지 연산
print(a % b)
print(7 % 3)

# 나눗셈 몫 구하기
print(a // b)
print(6 // 4)

s1 = 'Bye Python'
print(s1)

s3 = '''Bye 
Python'''
print(s3)

head = "I"
tail = "am happy"
print(head + tail)

# 문자열 곱하기
print(head * 3)
print("=" * 6)

# 문자열 인덱싱
a = "Today is a gift"
print(a[1])
print(a[3])
print(a[-2])
print(a[-3])

# 문자열 슬라이싱
b = a[1] + a[2] + a[3]
print(b)

print(a[5:6])
print(a[18:])
print(a[:4])
print(a[6:-12])

# 문자 개수 계산
a = "World"
print(a.count('d'))

# 문자 위치 확인
print(a.find('o'))
print(a.find('r'))
print(a.index('l'))
# print(a.index('p')) # 오류 발생

# 문자 삽입
b = "."
c = b.join('DEFG')
print(c)

# 대소문자 변환
print(a.upper())
print(a.lower())

# 공백 제거
d = "              ly           "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# 문자열 수정 (불가능)
a = "Wirld"
# a[1] = 'y'    # 오류 발생

# 문자열 바꾸기
a = "Math is easy."
print(a.replace("easy", "hard"))
print(a)

# 문자열 나누기
print(a.split())

b = "d. e. f. g"
print(b)
print(b.split('.'))

# 리스트 만들기
a = [1, 2, 3]
b = ['Work', 'is', 'too', 'hard']
c = [1, 2, 'Work', 'is']
d = [1, 2, [3, 4], ['Work', 'is']]

# 리스트 인덱싱
print(d[1])
print(d[3])
print(d[4][-2])

# 리스트 슬라이싱
print(d[1:4])

# 리스트 연결
print(a + b)
print(b[0] + " bye~ ^^;")
# print(a[0] + " hi~ ^^;")    # 오류 발생

# 리스트 반복
print(a * 4)

# 리스트 수정
a[2] = 88
print(a)

a[2:3] = ['d', 'e', 'f']
print(a)

a[-2] = ['g', 'h', 'i']
print(a)

# 삭제
del a[-2]
print(a)

# 원소 추가
a.append(6)
print(a)

# 원소 정렬
b.sort()
print(a)

# 원소 순서 뒤집기
a = [5, 3, 2, 8]
a.reverse()
print(a)

# 원소 위치 확인
print(a.index(2))

# 원소 삽입
a.insert(1, 88)
print(a)

# 원소 삭제
a.remove(88)
print(a)

b = [4, 5, 6]
print(b.pop())
print(b)

print(b.pop(0))
print(b)

# 특정 원소값의 개수
a = [1, 2, 4, 4, 2, 3, 3, 1]
print(a.count(3))

# 튜플 만들기
t1 = (4, )
t2 = (4, 5, 6)
t3 = 4, 5, 6
t4 = (4, 5, (6, 7), ('Work', 'is'))

# 튜플 인덱싱
print(t4[1])
print(t4[2][-2])

# 튜플 슬라이싱
t4[1:4]

# 튜플 연결
print(t1 + t2)
# print(t1 + "hi~ ^^;")   # 오류 발생

# 튜플 반복
t2 * 7

# 튜플 수정(불가능)
# t2[2] = 99      # 오류 발생

# 딕셔너리 만들기
dic = {'Name':'Lee', 'phnum':'01023456789', 'Birth':'0117'}

# 원소 추가
dic[2] = 'b'
print(dic)

dic['pet'] = 'cat'
print(dic)

# 원소 삭제
del dic[1]
print(dic)

# 원소의 value 구하기
print(dic['phnum'])
print(dic['Name'])

# key의 리스트 만들기
print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
  print(dic[key])

# value의 리스트 만들기
print(dic.values())
print(list(dic.values()))

# key, value 쌍 구하기
print(dic.items())

for key, value in dic.items():
  print(key + ":" + value)

# 원소 삭제
dic.clear()
print(dic)

# 집합 만들기
s1 = {4, 5, 'b', 7}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

# 교집합 연산
print(s2 & s3)
print(s2.intersection(s3))

# 합집합 연산
print(s2 | s3)
print(s2.union(s3))

# 차집합 연산
print(s2 - s3)
print(s3 - s2)
print(s2.difference(s3))
print(s3.difference(s2))

# 원소 한 개 추가
s2.add(7)
print(s2)

# 원소 여러 개 추가
s2.update([7, 8, 9, 10, 11])
print(s2)

# 특정 원소 제거
s2.remove(8)
print(s2)

s2 = set([2, 4, 5, 6, 2, 4, 2, 3, 5])
print(s2)

# 비교 연산자
x = 4
y = 3
print(x == y)
print(x != y)
print(x >= y)

# 조건의 연결
money = 1500
if money >= 1300 and money < 4500:
  print('버스를 탈 수 있습니다.')

# 그룹 자료형의 원소인지 검사하기
print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2, 3])
print('d' in ['c', 'd', 'e', 'f'])
print('g' not in 'World')

# 아무 것도 하지 않게 설정
if money >= 10:
  pass
else:
  print('저축하자!')

"""# 4. 반복문"""

# for 반복문1
test_list = ['five', 'six', 'seven']
for b in test_list:
  x = b + '?'
  print(x)

# for 반복문2
number = 0
for score in [80, 37, 54, 60, 85]:
  number += 1

  if score > 70:
    print("%d번 학생은 합격입니다." % number)
  else:
    print("%d번 학생은 불합격입니다." % number)

# while 문
i = 0
while i < 5:
  i += 1
  print('*' * i)

# 함수 정의
def sum1(a, b):
  x = a + b
  return x

def sum2(*args):
  x = 0
  for i in args:
    x += i
  return x

# 함수 호출
a = 6
b = 4
print(sum1(a, b))
print(sum1(4, 6))
print(sum2(2, 4, 5, 6, 7))
print(sum2(3, 4.5, 11))

"""## 내장 함수"""

# 숫자 x의 절대값을 반환
print(abs(-4.5))

# 그룹 자료형의 변수 x의 모든 원소가 참(0이 아닌 값)이면 True 반환
print(all([4, 5, 6, 7]))
print(all([5, -4, 0.0, 6]))

# 그룹 자료형의 변수 x의 원소 중 하나라도 참이면 True 반환
print(any([4, 5, 6, 7]))
print(any([5, -4, 0.0, 6]))

# 아스키코드 값에 대한 문자 출력
print(chr(87))
print(chr(56))

# 문자에 대한 아스키코드 값 출력
print(ord('b'))
print(ord('0'))

# 객체 x가 가진 멤버 변수와 멤버 함수 보여주기
print(dir([3, 4, 5]))
print(dir({'3':'a'}))
print(dir(3))

print(int('4'))                # x를 정수 형태로 반환
print(str(4))                  # x를 문자열 형태로 반환

# x를 리스트로 반환
print(list("World"))
print((1, 2, 3))

# x를 튜플로 반환
print(tuple("World"))
print(tuple([1, 2, 3]))

# x의 자료형을 반환
print(type("def"))
print(type(a))

# 간단한 삽입형 함수 생성
sum = lambda a, b: a + b

print(sum(6, 7))

# 최대, 최소값 반환
print(max([2, 5, 4, 7, 8]))
print(max("World"))

print(min([2, 5, 4, 7, 8]))
print(min("World"))

# x의 y제곱 결과값 반환
print(pow(3, 5))

# 사용자 입력으로 받은 값을 문자열로 반환1
c = input("값을 입력하세요:")
print(c)

# 사용자 입력으로 받은 값을 문자열로 반환2
c = input("정수를 입력하세요: ")
print(c)

# 입력 받은 숫자에 해당되는 범위의 값을 반환
print(range(5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))

for i in range(5, 20, 3):
  print(i)

# 입력값 s의 길이를 반환
len('Python')

print(sorted([3, 0, 2, 1]))
print(sorted('Python'))

# 패키지, 모듈 사용
# Request('http://www.sunmoon.ac.kr')   # 오류 발생

import urllib.request
urllib.request.Request('http://www.sunmoon.ac.kr')

import pandas
pandas.DataFrame()

from datetime import datetime
datetime.now()

# 파일 객체 생성
f = open('example.txt', 'w')
print(f)

# 파일 닫기
f.close()

# 파일 쓰기
f = open('example.txt', 'w')
for i in range(1, 6):
  data = '%d번째 줄입니다. \n' % i
  f.write(data)
f.close()

# 파일에 내용 추가하기
f = open('example.txt', 'w')
for i in range(6, 11):
  data = '%d번째 줄 추가입니다. \n' % i
  f.write(data)
f.close()

# 파일 모드 'r' - readline()
f = open('example.txt', 'r')


while True:
  line = f.readline()
  if not line: break
  print(line)

f.close()

# 파일 모드 'r' - readlines()
f = open('example.txt', 'r')
lines = f.readlines()
print(lines)

for line in lines:
  print(line)

f.close()

# 파일 모드 'r' - read()
f = open('example.txt', 'r')
data = f.read()
f.close()
data

# with open() as 파일 객체
with open('example.txt', 'w') as f:
  f.write("Now is better than never.")
# data = f.read()       # 오류 발생