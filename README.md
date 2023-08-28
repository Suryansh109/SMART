# freelance
This is placeholder for all the freelance supporting code

#SMART
SMART is Stock Monitering and Reporting Tool used to capture market transaction happenning on daily basis.
This will work as batch process and insight will be build from T-1 day data.

Implemented:
  - Smart.py to dump csv files from NSE site using stock_moniter_links.json
  - run_query to Load and do some DMLs and find the net Transaction done by any company, this  is saved in ClientPortFolio.csv

TODO:
  - Page Links to be added for all these Companies to understand the behaviour/domain.
  - Email utility to send report every day.
  - Reconcilation methods to keep the final data updated.

Avi's TODO:
  - Idenitfy if there is any day linked pattern.
      - We have data of last 6 months with Date, link day of week and create a day wise dributions chart for Buy/Sell.
      - This would be as per Securities and as Client Name.   
