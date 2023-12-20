print("შემოიტანეთ სტრიქონი")
S1=input()
print("შემოიტანეთ ქვესტრიქონი, რომლის მოძებნაც გინდათ პირველად შემოტანილ სტრიქონში")
S2=input()

if len(S2)>len(S1):
    print("ოე ოეეეე")
    exit(2)
else:
    counter=0
    for i in range(len(S1)-(len(S2)-1)):
        if S1[i:i+len(S2)]==S2:
            counter=counter+1
        else:
            continue
    print(counter)

