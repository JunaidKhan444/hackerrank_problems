if __name__ == '__main__':
    N = int(input())
    list_number = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(list_number)
        elif ip[0] == "insert":
            list_number.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            list_number.remove(int(ip[1]))
        elif ip[0] == "pop":
            list_number.pop();
        elif ip[0] == "append":
            list_number.append(int(ip[1]))
        elif ip[0] == "sort":
            list_number.sort();
        else:
            list_number.reverse()
