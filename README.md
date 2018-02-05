# BYTES-Book-Your-Tickets-Extremely-Superfast-

When was the last time you tried to book a Tatkal ticket but failed to do so owing to its high demand? Well, no worries BYTES is there to help you out. It's a Python script that lets you book tatkal tickets within a minute. Selenium is used here for scraping and form-filling. 


Now let's come to the good part. In order to speedily book your tickets, all you gotta do is input all the data like source, destination, date of journey, passenger details, etc. The user input part is the most important part of the script. If you fill up the data in perfect accordance with the steps given below, your ticket will be booked for sure. And please make sure that all the input is entered within inverted commas. 


These are the following fields you'll have to enter as user input in the script. The order given here is the same as the order in the script.

1. username : Your IRCTC username
2. password : Your IRCTC password (Your login credentials remain safe. You can have the script proofread from someone who knows Python and               Selenium.)
3. source : Source station code (No need to enter the exact station code. For eg., if you are departing from Delhi, then DEE, DLI, NDLS,               NZM, ANVT, etc., any of the station codes will work. The script will auto-accept the alert box if we have a differing station             code.)
4. destination : Destination station code (Both source and destination to be entered in uppercase only.)
5. DOJ : Date of Journey (Strictly to be entered as dd-mm-yyyy.)
6. train_no : Travelling train number. For eg. 12952 is the train number for New Delhi - Mumbai Rajdhani Express.
7. travelling_class : Your travelling class. (1A = AC First Class, 2A = AC 2 - Tier, 3A = AC Three Tier, FC = First Class, CC = AC Chair                         Car, SL = Sleeper, 2S = Second Sitting. For eg. if you are going via chair car, enter CC in the travelling_class                           field.)
8. boarding_station : The station where you will board the train. Leave it blank if your source station and boarding station are the same.
9. quota : Your booking quota. (GN = General, PT = Premium Tatkal, HP = Physically handicapped, LD = Ladies, TQ = Tatkal, SS = Senior                Citizen. For eg. if you are booking in Tatkal quota, enter TQ in the field.)

Now comes the passenger details. For a general quota ticket, maximum of 6 adults and 2 children can be booked on a single PNR. While for a tatkal ticket, the figures are 4 adults and 2 children. The details of each passenger consist of 6 records. They are mentioned below in the same order as the script.

