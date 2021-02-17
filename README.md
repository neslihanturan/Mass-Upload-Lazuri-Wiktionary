# Mass-Upload-Lazuri-Wiktionary
This project is how we (with [@ooguz](https://github.com/ooguz)) created several Wiktionary items in Lazuri Incubator from a .json file. If you have a sorted dictionary data, this project can help you to donate your data to Wiktionary.

## Steps
1. Parse current source json file (lazuri.json) with "parser.py" script.
2. Create a text file output ready to be used by PyWikiBot pagefromfile script
3. Create pages from output (lazuriTargetTr.json) file
