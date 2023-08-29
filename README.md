# QuantProjects
Backend of a quantitative investment project using yahoo finance

## Current form

Still very much a "testing ground", not yet progressed to a singular app or full product MVP. 

Much is still sketched in Jupyter notebooks and packages yet to be connected in order to minimise technical debt.

Data can be patched for tests but as there's a live database, the backend and functionality for the frontend while still progressing with features, many things are breaking then being removed or abstracted out.
Priority is on building a version with meaningful functionality to test rather than testing if Json data is recieved from pre-built packages.

Originally there was going to be a Vite frontend build into the app as a singular full-stack repo attempt but the cost of keeping everything in one place rather than decoupling as much as possible.

## Planned sketch

The goal would be to run the server from an online backend from the cloud also connected to a database. [Mostly achieved].

The backend scrapes data from Yahoo finance and wikipedia then uploads that data to the database. [scraping achieved, upload possible and trialed but not yet connected/automated in implementation].

The backend (or frontend) calculates ideal times to buy/sell from historic data like stock price, ask/bid spread. [Black-Scholes is a solved problem essentially, hardest part is impletementing into the backend and database].

Have a frontend that can: display each stock, search stocks, request new stocks, keep track of user's virtual investments somewhat. [Currently believe a seperate Next.js repo is best for this to decople local user logic from global stock logic].
