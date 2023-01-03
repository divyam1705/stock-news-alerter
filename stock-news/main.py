STOCK = "TATAMOTORS.BSE"
COMPANY_NAME = "Tata Motors"
import requests
from twilio.rest import Client
api_key_alpha="" #addkeys
api_key_news=""
params={"function":"TIME_SERIES_DAILY","symbol":STOCK,"apikey":api_key_alpha}
response=requests.get("https://www.alphavantage.co/query",params=params)
response.raise_for_status()
data=response.json()
yest=float(list(data["Time Series (Daily)"].values())[0]["4. close"])
daybyest=float(list(data["Time Series (Daily)"].values())[1]["4. close"])
perdeviation=((yest-daybyest)/daybyest)*100
perdeviation=round(perdeviation,2)

#STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

headline="" 
desc=""
def getnews():
    global headline,desc
    parameter = {"q": COMPANY_NAME, "apiKey": api_key_news}
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameter)
    data1 = response.json()
    headline=data1["articles"][0]["title"]
    desc=data1["articles"][0]["description"]


account_sid=""# add sid
auth_token=""##addauth tok
decsym=""
if perdeviation >5:
    sym=f"🔺{perdeviation}%"
elif perdeviation<-5:
    sym=f"🔻{perdeviation}%"
print(perdeviation)
sym="TM"
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# if perdeviation >5 or perdeviation<-5:
getnews()

msg=f"{COMPANY_NAME}:{sym}\nHeadline:{headline}\nBrief:{desc}"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=msg,
    from_='whatsapp:'  ,#add number
    to='whatsapp:'
)
print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

