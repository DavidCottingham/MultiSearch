# MultiSearch
MultiSearch searches multiple websites given a single search term.
First the user is asked for a search category. If the category is listed in the text file, Multisearch opens the URLs specified in a text file under that category

The user must create the text file before the script will work. The script will replace "%s" in the URL with the given search term. The format of the text file is as follows:
```
category1:
http://example.com/search?q=%s
https://www.google.com/search?q=%s

category2:
http://www.duckduckgo.com/q=%s
http://search.yahoo.com/search?p=%s
```
###Notes:
* The category name must be followed by a colon(:) and are currently case-sensitive
* Empty lines are ignored. They can be given for readability or omitted
* There is no limit on the number of URLs that will be attempted to be opened, however some web browsers may have a problem with opening too many at once
* The format of the text file is not checked, nor is the URL construction. It is the user's responsibility to ensure they are formatted correctly.
* This is a work in progress
