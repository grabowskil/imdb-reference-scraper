# IMDB Reference Scraper

#### documentation (for v0.7-beta)
1. download and unzip the source-code into a path of choice
2. open the terminal and navigate to the chosen path
3. run the scraper by `$python3 imdbRefScraper.py [-args, ...]`
4. run the analyzer by `$python3 imdbRefAnalyzer.py [-args, ...]`

##### list of arguments

######imdbRefScraper.py
condition | argument (short) | argument (long) | comment
--------- | ---------------- | --------------- | -------
optional | `-h`| `--help` | show documentary
mandatory | `-d n`| `--levelDepth`| how deep (depth = n) should the crawler follow the link-tree? (run time increases exponentially)
optional | `-iL` | `--initialLink`| seed-link, from which the crawler starts scraping. Format: `'title/tt0000000'` (default: Matrix)
optional | `-t` | `--time` | how many seconds should the scraper wait between each request? (default: 5)
optional | `-a` | `--all` | if parsed: tv shows, videos and games get crawled
optional | `-r`| `--recursive`| if parsed: crawler tries five additional times to call scraper in case of urllib Error -3

######imdbRefAnalyzer.py
condition | argument (short) | argument (long) | comment
--------- | ---------------- | --------------- | -------
optional | `-h`| `--help` | show documentary
optional | `-p n` | `--print` | prints the top n movies, with the most connections in descending order
