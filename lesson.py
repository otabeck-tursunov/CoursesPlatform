import collections

matn = "Salom Codial. Salom Hammaga"
print(collections.Counter(matn))

matn = ["Asadbek", "Nizomiddin", "Shukurjon", "Umida"]
matn_deque = collections.deque(matn)
matn_deque.appendleft("Mirjalol")
print(matn_deque)




import bisect

ismlar = ["Otabek", "Shaxzodbek", "Asadbek", "Javoxir", "Islombek", "Aziz", "Ali"]
ismlar.sort()
print(ismlar)
print(bisect.bisect(ismlar, "Mansur"))

ballar = [0, 30, 55, 71, 85, 100]
print(bisect.bisect(ballar, 75))
