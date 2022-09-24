240922 - DPC - cpsizeme_to_graphs

I wrote this to try and visualise some of the data inside of a Check Point cpsizeme bundle.

There's two scripts;

- ReadAlignedCSV.py / reads and processes the "aligned.csv" file.
- ReadFullStats.py / reads and processes the "fullstats.csv" file

This may or may not work for you, I spent the most amount of time on "ReadAlignedCSV.py" as that has the most summarised data in it without doing lots of joins or pivoting between Pandas dataframes.

Put the two files in the base folder with the scripts. Should throw up a web-page (through panel) to visualise some of the data.
