# Major - automation of the crypto game “Major”

A program that automates actions in the crypto game “Major”

# Quick Start

*  Download [latest version from Releases page](https://github.com/Argona7/Major/releases), and **run the program as administrator**.

# How does it work 

**The program does automation with post queries, the actions it automatically performs:**

* Get daily reward
* Start game **"coins"**
* Start game **"roulette"**
* Start game **"swipe"**

The program sends requests using an authorization token that is different for each account, and thanks to the token the authorization takes place.
[How to get "query"](#how-to-get-query)

# How to track a request

In order to trace the request you need to run Major in the telegram web. With the help of the ***DevTools*** in the ***Network*** section you will be able to find  the request **"tg"** that the Major sends

###

# How to use

Download [latest version from Releases page](https://github.com/Argona7/Major/releases) and run.
After that, the program will create a json document called **diamore** which must be filled in manually on the path **“C:\Users\ Your user.“**

* ### How the json file should be filled in:
```
{
    "accounts": {
        "@YouTelegramAccountName": {
            "query":"",
            "user-agent":""
        },
        "@YouTelegramAccountName": {
            "query":"",
            "user-agent":""
        },
        "@YouTelegramAccountName": {
            "query":"",
            "user-agent":""
        },
        "@YouTelegramAccountName": {
            "query":"",
            "user-agent":""
        }
    }
}
```
You should also record a different **user-agent** for each account for better security

## How to get "query"

You have to follow the same pattern as in [How to track a request](#how-to-track-a-request) . You need to track down the **"tg"** request. After that you just need to copy the body of the request:
```
{
"init_data" : "YOUR_QUERY_HERE"
}
```

After that, once you have properly modified the file, restart the application
You will be prompted to exclude accounts from the automation list, simply type the account name or account names with a space.  
Enjoy the app!

**Who's not registered**: https://t.me/major/start?startapp=1087108725
