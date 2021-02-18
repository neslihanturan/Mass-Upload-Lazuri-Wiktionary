# Mass-Upload-Lazuri-Wiktionary
This project is how we (with [@ooguz](https://github.com/ooguz)) created several Wiktionary items in Lazuri Incubator from a .json file. If you have a sorted dictionary data, this project can help you to donate your data to Wiktionary.

## Steps
1. Parse current source json file (lazuri.json) with "parser.py" script.
2. Create a text file output ready to be used by PyWikiBot pagefromfile script
3. Create pages from output (lazuriTargetTr.txt) file with PyWikiBot (before this step make sure you know what you are doing, be careful since you will be editing Wiktionary and you wouldn't prefer to vandalize it):

PyWikiBot is a rich tool to make several operations on wikis. We will be using "pagefromfile" tool. Here is the [documentation](https://www.mediawiki.org/wiki/Manual:Pywikibot) (you may be needed to set your configuration settings first according to your account information and the Wiktionary you will be editing)

For out specific purpose create input files in form of:
```
{{-start-}}
'''WikiProject:WomenInRedInYourLanguage/RedListInYourLanguage/Academician''' and here the content of file (ie. list of women who is academician) should be added. You can use exampleWikitextUsingListeria.txt file as a template for this content.
{{-stop-}}
{{-start-}}
'''WikiProject:WomenInRedInYourLanguage/RedListInYourLanguage/Musician''' and here the content of file (ie. list of women who is academician) should be added. You can use exampleWikitextUsingListeria.txt file as a template for this content.
{{-stop-}}
...
...
```
Where everything between {{-start-}} and {{-stop-}} will be a single page content which should be written according to wikitext format. The first item between triple quotes ( \'\'\'  \'\'\' ) will be the name of the page. To run the script you simply run this command from terminal:
```
python pwb.py pagefromfile -showdiff -file:lazuriTargetTr.txt
