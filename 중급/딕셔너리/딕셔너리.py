menu = {"김밥" : 2500, "라면" : 3500, "떡볶이" : 4000}

print(menu["김밥"]) # 접근
menu["김밥"] = 3000;print(menu["김밥"]) # 값 수정
menu["어묵"] = 1000;print(menu) # 요소 추가

#######################################################

print(menu.keys()) # 키 반환
print(menu.values()) # 값 반환
print(menu.items()) # 키, 값을 튜플로 묶어서 반환
print(menu.get("어묵")) # 키로 요소 접근해서 값 반환
print(menu.get("어묵"), "없음")
del(menu["라면"]);print(menu) # 요소 삭제
menu.clear();print(menu) # 모든 요소 삭제
