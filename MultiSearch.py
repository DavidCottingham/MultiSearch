import sys
import json
import webbrowser
import re
from msmessages import messages, print_help

#filename for loading and saving
save_file = "ms.json"

def main(args):
    # regular expression with 2 capture groups: any repeating chars surrounded
        # by quotes and any repeating non-space chars
    reg = r"\"(.+)\"|(\S+)"
    # if already has args, script run by CLI, so only run once
    if args:
        runCommand(args)
    # repeat asking commands if not run with commandline args
    while not args:
        print()
        # ask for user input and regex match that. Matches will be a list of
            # tuples with 1 empty match and one match.
        matches = re.findall(reg, input(messages["input"]))
        for tup in matches:
            for s in tup:
                if s:
                    # pull strings out of the tuples out of the list. if non-empty,
                        # add it to args and break loop since only 1 will match
                    args.append(s)
                    break
        if args:
            runCommand(args)
            # reset args so can ask again for user input
            args = []

# helper function; pulls string from args and sees if in allowed commands list
# if it is, call that function, passing remaining args
def runCommand(args):
    if args[0].lower() in commands.keys():
        commands[args[0].lower()](args[1:])
    else:
        print(messages["unknown_cmd"])

# insert search terms into all URLs in a category and open all in browser
def search(args):
    search_data = load_json()
    if search_data and len(args) > 1:
        category = args[0].lower()
        # create a single string of remaining args after category
        terms = " ".join(args[1:])
        if category in search_data.keys():
            print(messages["search"].format(category, terms))
            for url in search_data[category]:
                # using simple string.replace to insert search terms
                url = url.replace("%s", terms)
                webbrowser.open(url, new=2)
        else:
            print(messages["cat_not_found"].format(category))
    else:
        print(messages["cat_req"])

# add a category to saved dict
def addcat(args):
    search_data = load_json()
    if len(args) > 0:
        print(messages["addcat"].format(args[0]))
        # adds the category name to the dict as key with an empty list as the value
        search_data[args[0].lower()] = []
        save_json(search_data)
    else:
        print(messages["cat_req"])

# remove a category from a saved dict
def remcat(args):
    search_data = load_json()
    if search_data and len(args) > 0:
        category = args[0].lower()
        if category in search_data.keys():
            num_urls = len(search_data[category])
            # remove the matching category from the dict
            search_data.pop(category)
            print(messages["remcat"].format(category, num_urls))
            save_json(search_data)
        else:
            print(messages["cat_not_found"].format(category))
    else:
        print(messages["cat_req"])

# add a URL to a category in the saved dict
def addurl(args):
    search_data = load_json()
    if search_data and len(args) > 1:
        category = args[0].lower()
        url = args[1]
        if category in search_data.keys():
            search_data[category].append(url)
            save_json(search_data)
            print(messages["addurl"].format(url, category))
        else:
            print(messages["cat_not_found"].format(category))
    else:
        print(messages["addurl_req"])

# remove a URL from a category in the saved dict
def remurl(args):
    search_data = load_json()
    if search_data and len(args) > 1:
        category = args[0].lower()
        url = args[1]
        if category in search_data.keys():
            if url in search_data[category]:
                search_data[category].remove(url)
                save_json(search_data)
                print(messages["remurl"].format(url, category))
            else:
                try:
                    url_idx = int(url)
                    url = search_data[category][url_idx]
                    del search_data[category][url_idx]
                    save_json(search_data)
                    print(messages["remurl"].format(url, category))
                except ValueError:
                    print(messages["url_not_found"].format(url, category))
                except IndexError:
                    print(messages["bad_index"].format(url_idx))
        else:
            print(messages["cat_not_found"].format(category))
    else:
        print(messages["remurl_req"])

# print out all the categories saved in the dict
def listcats(args):
    search_data = load_json()
    if search_data:
        print(messages["listcats"])
        for cat in search_data.keys():
            print(cat)
    else:
        print(messages["nocats"])

# print out all the saved URLs in a saved category in the dict
def listurls(args):
    search_data = load_json()
    if search_data and len(args) > 0:
        category = args[0].lower()
        if category in search_data.keys():
            if search_data[category]:
                print(messages["listurls"].format(category))
                for index, url in enumerate(search_data[category]):
                    print(str(index) + ": " + url)
            else:
                print(messages["nourls"].format(category))
        else:
            print(messages["cat_not_found"].format(category))
    else:
        print(messages["cat_req"])

# displays help; calls the function found in msmessages.py that displays help
def help(args):
    print_help()

# save the dict as JSON to file
def save_json(json_data):
    try:
        with open(save_file, "w") as saved_data:
            json.dump(json_data, saved_data)
    except IOError:
        print(messages["save_err"])

# load the dict as JSON from file
def load_json():
    # load file. if empty or non-existent, tell user
    try:
        with open(save_file, "r") as saved_data:
            json_data = json.load(saved_data)
            return json_data
    except IOError:
        print(messages["load_err"])
    except json.decoder.JSONDecodeError:
        print(messages["json_read_err"])

# Exit the script execution (used when repeating asking user input and user is done)
def exit(args):
    sys.exit()

# allowed commands / arguments and matching function to call
commands = {"search" : search,
            "multisearch" : search,
            "ms" : search,
            "s" : search,
            "addcat" : addcat,
            "addcategory" : addcat,
            "ac" : addcat,
            "rc" : remcat,
            "remcat" : remcat,
            "removecat" : remcat,
            "removecategory" : remcat,
            "remcategory" : remcat,
            "add" : addurl,
            "addurl" : addurl,
            "a" : addurl,
            "r" : remurl,
            "remurl" : remurl,
            "removeurl" : remurl,
            "rem" : remurl,
            "remove" : remurl,
            "categories" : listcats,
            "cats" : listcats,
            "listcats" : listcats,
            "listcategories" : listcats,
            "lc" : listcats,
            "list" : listurls,
            "listurls" : listurls,
            "l" : listurls,
            "exit" : exit,
            "quit" : exit,
            "q" : exit,
            "help" : help,
            "h" : help,
            "?" : help }

if __name__ == "__main__":
    # if run from CLI, will be more than 1 arg in argv. pass those args
        #(after script name) to main
    # Otherwise, pass the empty arg list to main and main will handle it
    args = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    main(args)
