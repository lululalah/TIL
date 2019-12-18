'''
String 조작하기

1.글자합체
string + string

2.글자삽임(수술)

3.글자 자르기

'''
#1.글자합체
hphk ="happy" + "hacking"
print(hphk)

#2.글자삽입
name="hj"
age=27

text="안녕하세요. 제이름은 {}입니다. 나이는 {}세 입니다.".format(name, age)
print(text)

f_text= f"제이름은 {name}입니다. 나이는 {age}세 입니다."
print(f_text)

#3. 글자자르기
#string> "어떠한 글자들"[start:end]
text_name = text[:17] #처음부터 17까지
print(text_name)

text_age = text[19:] #19부터 끝까지
print(text_age)

text_split = text.split()
print(text_split)