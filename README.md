# MultiSearch
**MultiSearch** searches multiple websites given a search term.

The user creates categories and adds search URLs to them before searching with the commands "addcategory" and "addurl".
The URLs must contain "%s" where the search terms should be inserted.

The script can be run with command-line arguments and will be run only once - useful for a quick search, or run without command-line arguments to run in a loop such that the user can run multiple commands before exiting - useful for adding many categories and URLs such as on the first run.

Use the command "help" for the following printout of available commands and a short description of each.

### Commands
**addcategory**

>Aliases: addcat, ac

>A category is a name of a group of URLs that will be used to complete your search. The category must be a single word or enclosed in quotation marks ( " ).
>Eg.: A category called 'shopping' might include the search URLs for Amazon.com and Thinkgeek.com

>Usage: 'addcategory' followed by the name of the category.

>Example: addcategory shopping")

**addurl**

>Aliases: add, a

>Search URLS must be added to an existing category. The URL must include '%s' where the search term will be placed. '%s' can be in the URL only once or only the first will be  replaced. A URL without '%s' will still be opened but will be ineffective for searching the website for your terms. If running the script with command-line arguments, the URL is recommended to be enclosed in quotation marks ( " )

>Usage: 'addurl' followed by the category name followed by the URL

>Example: addurl general "https://www.google.com/search?q=%s"

**removecategory**

>Aliases: removecat, remcategory, remcat, rc

>Remove a category and all associated URLs. If the category name is more than one word, the words must be enclosed in quotation marks ( " ).

>Usage: 'removecategory' followed by the name of the category.

>Example: removecategory shopping

**removeurl**

>Aliases: remurl, remove, rem, r

>Remove a URL from a category. You can provide the full URL or the number shown when using the 'listurls' command. If using the URL and running the script with command-line arguments, it is recommended to enclose it in quotation marks ( " ).

>Usage: 'removeurl' followed by the category followed by the full URL or the corresponding index number.

>Example 1: removeurl general "https://www.google.com/search?q=%s"

>Example 2: removeurl shopping 2

**listcategories**

>Aliases: categories, cats, listcats, lc

>Lists all the stored categories of URLs.

>Usage: 'listcategories' with no additional arguments

**listurls**

>Aliases: list, l

>Lists all the URLs stored in a given category. If the category name is more than one word, the words must be enclosed in quotation marks ( " ).

>Usage: 'listurls' followed by the name of a category.

>Example: listurls shopping

**search**

>Aliases: multisearch, s, ms

>Search the web using the URLs in a given category. If the category name is more than one word, the words must be enclosed in quotation marks ( " ).

>Usage: 'search' followed by the name of a category followed by search terms.

>Example: search shopping 3.5 inch floppy disks

**exit**

>Aliases: quit, q

>Exits the script when not running with command-line arguments.

>Usage: 'exit' with no additional arguments


**help**

>Aliases: h, ?

>Display this help screen.

>Usage: 'help' with no additional arguments
