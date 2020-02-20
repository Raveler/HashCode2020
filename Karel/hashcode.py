import math


def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()



def analyzeLibrary(library):

    # count the library sign up time, added by the time it takes to read all the books
    bookDays = math.ceil(library["nBooksInLibrary"] / library["dailyShipment"])
    library["totalTime"] = bookDays + library["signUpTime"]

def solve(input_list, out_file_name):

    header = input_list[0]
    splitHeader = header.split(" ");
    nBooks = int(splitHeader[0])
    nLibraries = int(splitHeader[1])
    nDays = int(splitHeader[2])
    print("Analyze ",nBooks," books in ",nLibraries," libraries on ",nDays," days")

    bookString = input_list[1].split(" ")
    bookScores = []
    for bookScoreString in bookString:
        bookScores.append(int(bookScoreString))

    libraries = []
    for i in range(0, nLibraries):
        libHeader = input_list[i*2+2].split(" ")
        nBooksInLibrary = int(libHeader[0])
        librarySignUp = int(libHeader[1])
        dailyShipment = int(libHeader[2])

        libBookHeader = input_list[i*2+3].split(" ")
        libBookIds = []
        for j in range(0, len(libBookHeader)):
            libBookIds.append(int(libBookHeader[j]))

        library = {
            "nBooksInLibrary": nBooksInLibrary,
            "signUpTime": librarySignUp,
            "dailyShipment": dailyShipment,
            "books": libBookIds
        };

        analyzeLibrary(library)
        libraries.append(library)
        print("Library ",i,":")
        print(libraries[len(libraries)-1])








    print("Book scores: ", bookScores)

    # do something
    with open(out_file_name, 'w+') as out_file:
        for list in input_list:
            out_file.write(list)


def main():
    input_files = ['a_example.txt']
    for input_file in input_files:
        file, ext = input_file.split('.')
        input_list = get_input(input_file)
        solve(input_list, file + '_out.' + ext)


if __name__ == "__main__":
    main()