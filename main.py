def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        lower_contents = file_contents.lower()
        letters = {}
        for l in lower_contents:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        letters_lst = []

        for key, value in letters.items():
            if key.isalpha():
                letters_lst.append({"letter": key, "num": value})
        
        letters_lst.sort(reverse=True, key=sort_on)

        print("----- Begin report on frankenstien.txt ------")
        print(f"""{len(lower_contents.split())} words found in this document
              """)
        for dic in letters_lst:
            print(f"The {dic['letter']} was found {dic['num']} times")
        print("""
               ----- End of report -----""")
        



def sort_on(dict):
    return dict["num"]




main()