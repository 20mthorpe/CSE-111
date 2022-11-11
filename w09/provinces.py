def main():

    text_list = read_list("provinces.txt")

    print(text_list)

    text_list.pop(0)
    text_list.pop()

    alberta_quantitiy = 0

    for i in text_list:

        if i == "AB":

            i = "Alberta"
            alberta_quantitiy += 1
        
        elif i == "Alberta":

            alberta_quantitiy += 1

    print("The amount of times 'Alberta' is in the list is", alberta_quantitiy)


def read_list(filename):

    text_list = []

    with open(filename, "rt") as text_file:


        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list

if __name__ == "__main__":
    main()