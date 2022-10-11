import os 
from deta import Deta # pip install deta
from dotenv import load_dotenv #pip install python-dotenv

# Load the environment variables 
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("monthly_reports")

def insert_period(period, incomes, expenses, comment): # in order to insert the peirod we have to find the four parameters in the ()
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment}) # put the values in a dictionary 

def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """if not found, the function will return None"""
    return db.get(period)
