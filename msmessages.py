# Messages displayed to user
messages = {
            "howto": "Use command-line arguments to use this script. Use the 'help' argument to see a list of all commands.",
            "input": "Enter a command (use 'help' to learn more): ",
            "unknown_cmd": "Command unknown. Use the 'help' command to see a list of commands.",
            "cat_req": "Category name required. Use the 'help' command for more information.",
            "addcat": "Added category '{}'.",
            "remcat": "Removed category '{}' and its {} URLs.",
            "cat_not_found": "Category '{}' not found. Use the 'listcategories' command to see all saved categories.",
            "addurl": "Added URL '{}' to category '{}'.",
            "addurl_req": "Adding a URL requires the category name followed by the URL. Use the 'help' command for more information.",
            "remurl": "Removed URL '{}' from category '{}'.",
            "url_not_found": "URL '{}' not found in category '{}'.",
            "bad_index": "Incorrect URL number ({}) given. Use the 'listurls' command to see a list of the URLs in a category.",
            "remurl_req": "Removing a URL requires the category name followed by the URL or number for the URL. Use the 'help' command for more information.",
            "listcats": "Saved categories:",
            "nocats": "No categories saved. Add one using the 'addcategory' command.",
            "listurls": "URLs in category '{}':",
            "nourls": "No URLS saved in category '{}'. Add one using the 'addurl' command.",
            "search": "Searching category '{}' using the search terms '{}'",
            "help_cmds": "Available commands:",
            "save_err": "I/O error saving the file.",
            "load_err": "Save file may not exist. Add your first category with the 'addcategory' command to create the save file.",
            "json_read_err": "Error reading JSON from file. If save file edited manually, ensure proper syntax is used."
}

def print_help():
    print()
    print(messages["help_cmds"], "\n")
    print("addcategory")
    print("\tAliases:", "addcat", "ac")
    print("\n\tA category is a name of a group of URLs that will be used to")
    print("\t\tcomplete your search. The category must be a single word")
    print("\t\tor enclosed in quotation marks ( \" ).")
    print("\t\tEg.: A category called 'shopping' might include the search")
    print("\t\tURLs for Amazon.com and Thinkgeek.com")
    print("\n\tUsage: 'addcategory' followed by the name of the category.")
    print("\n\tExample: addcategory shopping")
    print()
    print("addurl")
    print("\tAliases:", "add", "a")
    print("\n\tSearch URLS must be added to an existing category. The URL")
    print("\t\tmust include '%s' where the search term will be placed.")
    print("\t\t'%s' can be in the URL only once or only the first will")
    print("\t\tbe replaced. A URL without '%s' will still be opened but")
    print("\t\twill be ineffective for searching the website for your")
    print("\t\tterms. If running the script with command-line arguments,")
    print("\t\tthe URL is recommended to be enclosed in quotation")
    print("\t\tmarks ( \" ).")
    print("\n\tUsage: 'addurl' followed by the category name followed by the URL")
    print("\n\tExample: addurl general \"https://www.google.com/search?q=%s\"")
    print()
    print("removecategory")
    print("\tAliases:", "removecat", "remcategory", "remcat", "rc")
    print("\n\tRemove a category and all associated URLs. If the category name")
    print("\t\tis more than one word, the words must be enclosed in")
    print("\t\tquotation marks ( \" ).")
    print("\n\tUsage: 'removecategory' followed by the name of the category.")
    print("\n\tExample: removecategory shopping")
    print()
    print("removeurl")
    print("\tAliases:", "remurl", "remove", "rem", "r")
    print("\n\tRemove a URL from a category. You can provide the full URL or")
    print("\t\tthe number shown when using the 'listurls' command. If")
    print("\t\tusing the URL and running the script with command-line")
    print("\t\targuments, it is recommended to enclose it in quotation")
    print("\t\tmarks ( \" ).")
    print("\n\tUsage: 'removeurl' followed by the category followed by the")
    print("\t\tfull URL or the corresponding index number.")
    print("\n\tExample 1: removeurl general \"https://www.google.com/search?q=%s\"")
    print("\tExample 2: removeurl shopping 2")
    print()
    print("listcategories")
    print("\tAliases:", "categories", "cats", "listcats", "lc")
    print("\n\tLists all the stored categories of URLs.")
    print("\n\tUsage: 'listcategories' with no additional arguments")
    print()
    print("listurls")
    print("\tAliases:", "list", "l")
    print("\n\tLists all the URLs stored in a given category. If the category")
    print("\t\tname is more than one word, the words must be enclosed in")
    print("\t\tquotation marks ( \" ).")
    print("\n\tUsage: 'listurls' followed by the name of a category.")
    print("\n\tExample: listurls shopping")
    print()
    print("search")
    print("\tAliases:", "multisearch", "s", "ms")
    print("\n\tSearch the web using the URLs in a given category. If the")
    print("\t\tcategory name is more than one word, the words must be")
    print("\t\tenclosed in quotation marks ( \" ).")
    print("\n\tUsage: 'search' followed by the name of a category followed")
    print("\t\tby search terms")
    print("\n\tExample: search shopping 3.5 inch floppy disks")
    print()
    print("exit")
    print("\tAliases:", "quit", "q")
    print("\n\tExits the script when not running with command-line arguments.")
    print("\n\tUsage: 'exit' with no additional arguments")
    print("help")
    print("\tAliases:", "h", "?")
    print("\n\tDisplay this help screen.")
    print("\n\tUsage: 'help' with no additional arguments")
