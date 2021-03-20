main: hello clean scrape study 
	echo Done!
study:
	clear
	python3 study_buddy.py
scrape: clean
	scrapy runspider faq_scraper.py -o faqs.csv
clean:
	if [ -f *.csv ]; then rm *.csv; fi

hello:
	echo Hello!
