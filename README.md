#BBDC TPDS WEB SCRAPER 
***

###Problem Statement
Many individuals who sought to obtain their driving license from BBDC (Bukit Batok Driving Centre)
can relate to the woes of booking the three mandatory 
TPDS (Traffic Police Driving Simulator). With the systems currently in place, one can expect to take up to more than
six months to complete the three simulators. As of April 18 2022, the earliest slot is on 27 July - something that 
sounds illegal but isn't.

###The Solution
Hence, I came up with this python script the scrape the webpage for open slots that anyone might have returned to the pool. 
With this script, you can use Telegram on your phone to send a request to scrape the webpage for the earliest slots that may be available.

![Sample of interaction with bot.](/message.PNG)

###Install and Run
- Creating your Telegram bot.
  1. On Telegram, search for Telegram's official BotFather bot.
  2. Enter /newbot to create your own bot.
  3. Follow the instructions given by the bot to set up your bot.
  4. Be sure to take down the HTTP API that is linked to your bot. You will have to use it later.
- Set up the script.
  1. Clone this repository to your local machine using git clone.
  2. Rename the example.env.example file to a .env file.
  3. Enter your details as stated in the file.
  4. Run the script locally. Your Telebot will now be online.
  
  
     USERNAME=YOUR_BBDC_USERNAME
     PASSWORD=YOUR_BBDC_PASSWORD
     TELEBOT_TOKEN=YOUR_TELEBOT_HTTP_API

###Disclaimer
1. BBDC has implemented a limit to the number of times an individual can visit the site. I am not too sure 
of the limit, but that means that the bot can't scrape the website too often.
2. This is a barebones script, ie there is no error checking involved (may be implemented in the future). Which means 
that there is no logging when your credentials are wrong, when you have scraped the maximum limit for the day etc.
3. I am relatively new to this, any feedback/help is welcomed!