# aws_study_buddy
Cli based flashcards simulator for AWS FAQs. This light weight application contains 2 parts:

1. A web scraper that collects FAQs from AWS' documentation.
2. A flash card simulator that uses the data collected from the web scraper.

## Usage
A makefile with common macros has been created for convenience. To use this application, navigate to the repository's root and type the commands given by the following scenarios.

### Compile the FAQs data and start studying
This can be used the first time you ever run the program to create the faqs.csv that study_buddy gets its data from.<br>
`make`

### Study using existing faqs.csv
Once the web scraper has run once, you will have a faqs.csv file. You do not need to run the web scraper every you want to study.<br>
`make study`

## Dependencies
This application will work on any MACOS or Linux based system provided it has the following python packages.

1. [scrapy](https://scrapy.org/)<br>`pip install scarpy`
2. [pandas](https://pandas.pydata.org/)<br>`pip install pandas`
