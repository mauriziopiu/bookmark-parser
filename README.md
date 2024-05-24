# bookmark-parser

A simple parser to parse Firefox bookmarks (exported as JSON "Backup") into individual markdown files. Data about the individual bookmark is stored in YAML frontmatter. Frontmatter contents and format can obviously be adjusted for individual needs.

## Usage

1. Export your Firefox Bookmarks as .json file
2. Place that file in the data folder
3. Add the filename of your .json file in main.py line 5
4. Run the script: `$ python3 main.py`
5. You find your generated markdown files in the folder 'out'

## Roadmap & Feature Ideas

-   Customise frontmatter properties used
-   Export from folder with bookmarks into Browser-Importable Structe

## Warning

Take care when parsing data. Before you use the script and especially before you make any changes to it - make a backup/safety-copy of your bookmark data. I will not take responsibility in any data loss, caused by this script.

## License

This code is published under the GNU AGPLv3 License. Look into that if you want to use this in a commercial or non-private context.
