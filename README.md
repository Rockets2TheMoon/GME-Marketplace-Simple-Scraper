﻿# GME-Marketplace-Simple-Scraper
Basic Selenium web scraper to collect price and availability of a list of NFTs on the GameStop NFT Marketplace.

How to Run.
1) Install Python
2) Open the project in Visual Studio Code
3) In the terminal type: python -m pip install selenium
4) In the same terminal type: python '.\Scrape GME NFT Data.py'
5) Should print out the data

How to edit list
1) Open 'Scrape GME NFT Data.py'
2) Go to line 40.
3) Add/Remove lines to the list
3a) Remember to put the link between quotation marks and add a comma after the quotation mark for each line except the last.

Example:
ListofURLS = [
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x1d328a70404b88d4572ee6c06a568a205fecc44e442d836b96026a67fcfeaf57',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0xa834df3d51f13f68d1e9b1fc2d4180e50db3c6d21ff52837703392dad925f982',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x93a2f573a439462f830346f09180cf7720677103854a2b43c7286152540d2369',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x20329c270e75f8b3a7685d16acac49027f2d5531b78f26ad9803eba358ef5c9f'
]
