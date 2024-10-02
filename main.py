import requests 

cmc_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=f8463724-f500-44c5-8f91-6a6819c5ddd7' #CoinMarketCap API URL where information about Ethereum can be accessed
response = requests.get(cmc_api) #Sends an HTTP GET request to the API, and stores the response
response_json = response.json() #Store the latest listings from CoinMarketCap

eth_info = None 

if 'data' in response_json: #check if response has data
    for i in response_json['data']: #loop through the currencies 
        if i['id'] == 1027: #check if the currency's ID matches Ethereum's ID
            eth_info = i #stores Ethereum's info, in case we want to access something other than price
            eth_price = i['quote']['USD']['price']
            break
else:
    print("Error: " + response_json) #if the response doesn't contain data, there was an error


pushover_url = "https://api.pushover.net/1/messages.json"
pushover_parameters = {
    "token": "azh7gau64gh3zo2f18efhfieizdbtq", #my API token
    "user": "urgwnhpdt6s5zp22wguvt97bj79bku", #my user key
    "title": "Ethereum Price Alert", #title of notification
    "message": "Current Ethereum price: " + str(round(eth_price,2)) #text content in the notification
}

requests.post(pushover_url, pushover_parameters) #Sends an HTTP POST request to Pushover, which will then notify the user of ETH's current price
