"""A simple sample program that accumulates tweets for the query \"#haiku\"
"""

import twitterpastcrawler

crawler = twitterpastcrawler.TwitterCrawler(query="33982105",
                                        output_file="fcpsnews.csv"
                                        )

crawler.crawl()
