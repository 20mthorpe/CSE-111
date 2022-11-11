import csv

def main():
    students_dict = read_dict("students.csv")
    #print(students_dict)

    i_number = input("What is your i_number? ")

    if i_number in students_dict:
        print(students_dict[i_number])
    else:
        print("No such student")

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    students_dict = {}

    with open(filename) as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            #print(row_list)

            person = {row_list[0]: row_list[1]}
            students_dict.update(person)

    return students_dict

if __name__ == "__main__":
    main()