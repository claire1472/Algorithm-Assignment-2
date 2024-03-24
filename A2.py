counter = 0


def MergeSort(Product_ID):
    global counter

    if len(Product_ID) > 1:

        print(Product_ID, "\n")
        M = len(Product_ID) // 2  # identifies the center element of the list
        L_side = Product_ID[:M]  # takes the left part of the list
        print("L_side: ", L_side, "\n")
        R_side = Product_ID[M:]  # takes the right part of the list
        print("R_side: ", R_side, "\n")

        #
        MergeSort(L_side)
        # Sorts both the left and right segments of the list separately using the same algorithm
        MergeSort(R_side)
        #

        i = j = k = 0

        print("R_side:  =", R_side, "\n")
        print("L_side: ", L_side, "\n")

        while j < len(R_side) and i < len(L_side):
            if L_side[i] <= R_side[j]:
                counter += 1
                print("step",counter ,":\n\nMerging " , L_side[i], " from Left\n")
                print(L_side[i], "<=", R_side[j],"\n")
                Product_ID[k] = L_side[i]
                i += 1
            else:
                counter += 1
                print("step",counter ,":\n\nMerging " , R_side[j], " from Right\n")
                print(L_side[i], ">", R_side[j],"\n")
                Product_ID[k] = R_side[j]
                print("swap left and right\n")
                j += 1

            k += 1

        # Copy any remaining elements from the left side, if present
        while i < len(L_side):
            Product_ID[k] = L_side[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right side, if present
        while j < len(R_side):
            Product_ID[k] = R_side[j]
            j += 1
            k += 1

    return Product_ID


if __name__ == '__main__':
    usr_input =[]
    temp = []
    try:
        usr_input = str(input("Enter an array seperated by commas ',': "))
        usr_input = usr_input.split(",")
    except ValueError:
        pass
    for element in usr_input:
        temp.append(int(element))

    usr_input = temp.copy()
    MergeSort(usr_input)
    print("Unsorted List: ", temp)
    print("Soted List: ", usr_input)
