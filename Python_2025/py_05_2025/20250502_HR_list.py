if __name__ == '__main__':
    N = int(input())
    
    l = list()
    
    for i in range(N):
        # command, number= input("Enter command with attributes(e.g., insert 5): ").split()
        user_input = input("Enter command: ").split()
        command = user_input[0]

        if command == "insert":
            # Insert the number into the set
            index = int(user_input[1])
            val = int(user_input[2])
            l.insert(index, val)
            pass
        elif command == "print":
            # Print the set
            print(l)
            pass
        elif command == "remove":
            # Remove the number from the set
            a = int(user_input[1])
            l.remove(a)
            pass
        elif command == "append":
            # Append the number to the set
            number = int(user_input[1])
            l.append(number)
            pass
        elif command == "sort":
            # Sort the set
            l.sort()
            pass
        elif command == "pop":
            # Pop the last number from the set
            l.pop()
            pass
        elif command == "reverse":
            #   Reverse the set
            l.reverse()
            pass
    

