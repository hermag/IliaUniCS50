#შევიტანოთ სტრიქონი ბრძანებათა ველიდან (კონსოლიდან) და დავბეჭდოთ უკუმიმდევრობით
S1=input()
length=len(S1)
#S2 არის ცვლადი, რომელშიც შევინახავთ სტრიქონს უკუმიმდევრობით
S2=""
#C-ში ან C++-ში ჩაწერილი ციკლიfor (i=length; i>=0; i--)
i=length
#I გზა
#ანალოგიური ციკლი, ჩაწერილი პითონში
# while (i>0):
#     S2=S2+S1[i-1]
#     i=i-1
# print(S2)

#range() პითონში ჩაშენებული ფუნქციაა რომელიც მიბრუნებს რიცხვით მიმდევრობას 0-დან მოცემულ რიცხვამდე,
#მაგალითად range(5) დამიბრუნებს მიმდევრობას 0,1,2,3,4
#თუ range() ფუნქციაში მივუთითებთ მეორე პარამეტრად ბიჯს, მაგალითად
#range(5,0,-1) range ფუნქცია დაგვიბრუნებს რიცხვების უკუმიმდევრობას, ანუ 4,3,2,1,0
#სტრიქონის უკუმიმდევრობით ბეჭდვის კიდევ ერთი გზა
#II გზა
# for i in range(length-1,-1,-1):
#     S2=S2+S1[i]
# print(S2)

#III გზა
print(S1[::-1])

