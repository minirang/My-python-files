ClubA = {'단군', '계백', '이황'}
ClubB = {'김유신', '단군', '최영'}

ClubC = ClubA.union(ClubB)
print(ClubC)

print(ClubA.intersection(ClubB))
    
print(ClubA.difference(ClubB))

print(ClubB.difference(ClubA))

ClubA.add('이이')
print(ClubA)

ClubB.remove('김유신')
print(ClubB)

print(f'\nA 동아리 : {ClubA}\nB 동아리 : {ClubB}')
