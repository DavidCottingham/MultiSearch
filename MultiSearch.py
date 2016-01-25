import webbrowser

dic = {}
filename = "multisearch test.txt"

def initialize():
    current_key = ""
    file = open(filename)
    if (file == ""):
        print("File was empty")
        exit()
    for line in file:
        if (len(line) >= 2):
            if (line[-2] == ":"):
                current_key = line[:-2]
                dic[current_key] = []
            else:
                dic[current_key].append(line)

def user_input():
    u_cat = input("Enter the search category\n")
    for cat in dic:
        if (u_cat == cat):
            #category found
            u_search = input("Enter the search key\n")
            #open each URL
            for url in dic[cat]:
                url = url.replace("%s", u_search)
                webbrowser.open(url, new=2)

initialize()
user_input()
