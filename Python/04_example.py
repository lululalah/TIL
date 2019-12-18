#print() happy hacking!
hphk = "해피해킹"

print(hphk)
print(hphk)
print(hphk)
print(hphk)
print(hphk)

print("happy hacking!")
print("happy hacking!")
print("happy hacking!")
print("happy hacking!")
print("happy hacking!")


#점심메뉴판!
menus1 = "순남시래기"
menus2 = "양자강"
menus3 = "20층..."

print(menus1)
print(menus2)
print(menus3)

#List
menus = ["순남시래기","양자강","20층..."]
print(menus) #['순남시래기', '양자강', '20층...']로 출력됨.
print(menus[0])

#전화번호부 저장하기
phone_nums = ["02-111-1111","02-222-2222","02-333-3333"]
print(phone_nums[0])

#Dictionary
dict_nums= {
    "순남시래기":"02-111-1111"
     ,"양자강":"02-222-2222"
     ,"20층": "02-333-3333"
     }

print(dict_nums["순남시래기"]) #[]key값 틀리면 null아무것도
print(dict_nums.get("희희")) #정확히 key값 모를때는 ()사용. none이 출력되기 때문
print(dict_nums.get("순남시래기"))