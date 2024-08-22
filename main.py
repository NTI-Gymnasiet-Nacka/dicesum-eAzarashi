# Dice sum probability calculator
# Författare: Azarashi Fuu
# Datum: 2024-08-22

def main():
    user_input = input().split(" ")
    List=[]
    N=int(user_input[0])
    M=int(user_input[1])
    count=0
    Result=[]
    Result2=[]
    for i in range(1,N+1):
        for j in range(1,M+1):
            List.append(j+i)
    for i in List:
        freq=List.count(i)
        if freq > count:
            count=freq
            Result.clear()
            Result.append(i)
        elif freq == count:
            Result.append(i)
    for i in Result:
        if i not in Result2:
            Result2.append(i)
    for i in Result2:
        print(i)


if __name__ == "__main__":
    main()