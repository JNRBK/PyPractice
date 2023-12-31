def open_file(filename):
    dict_it = {}
    with open(filename) as file:
        for line in file:
            indx_1 = line.split(":")[0].lower()
            indx_2 = line.split(":")[1].strip()
            dict_it[indx_1] = indx_2
    return dict_it
def main():
    open_it = open_file('flowers.txt')
    get_input = input("Enter FirstName[Space]LastName only-->> ")
    word = get_input[0].lower()
    letter = word[0]
    if letter in open_it:
        print(f"flower name with the first letter: {open_it[letter]}")
main()