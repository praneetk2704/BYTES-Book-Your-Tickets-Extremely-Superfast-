# BYTES-Book-Your-Tickets-Extremely-Superfast-

When was the last time you tried to book a Tatkal ticket but failed to do so owing to its high demand? Well, no worries BYTES is there to help you out. It's a Python script that lets you book tatkal tickets within a minute. Selenium is used here for scraping and form-filling. 


Now let's come to the good part. In order to speedily book your tickets, all you gotta do is input all the data like source, destination, date of journey, passenger details, etc. The user input part is the most important part of the script. If you fill up the data in perfect accordance with the steps given below, your ticket will be booked for sure. And please make sure that all the input is entered within inverted commas. 


These are the following fields you'll have to enter as user input in the script. The order given here is the same as the order in the script.

1. **username** : Your IRCTC username
2. **password** : Your IRCTC password (Your login credentials remain safe. You can have the script proofread from someone who knows                       Python and Selenium.)
3. **source** : Source station code (No need to enter the exact station code. For eg., if you are departing from Delhi, then DEE, DLI,                   NDLS, NZM, ANVT, etc., any of the station codes will work. The script will auto-accept the alert box if we have a                       differing station code.)
4. **destination** : Destination station code (Both source and destination to be entered in uppercase only.)
5. **DOJ** : Date of Journey (Strictly to be entered as dd-mm-yyyy.)
6. **train_no** : Travelling train number. For eg. 12952 is the train number for New Delhi - Mumbai Rajdhani Express.
7. **travelling_class** : Your travelling class. (**1A** = AC First Class, **2A** = AC 2 - Tier, **3A** = AC Three Tier, **FC** = First                           Class, **CC** = AC Chair Car, **SL** = Sleeper, **2S** = Second Sitting. For eg. if you are going via chair                             car, enter **CC** in this field.)
8. **boarding_station** : The station where you will board the train. Leave it blank if your source station and boarding station are the                           same.
9. **quota** : Your booking quota. (**GN** = General, **PT** = Premium Tatkal, **HP** = Physically handicapped, **LD** = Ladies, **TQ**                = Tatkal, **SS** = Senior Citizen. For eg. if you are booking in Tatkal quota, enter **TQ** in this field.)

Now comes the passenger details. For a general quota ticket, maximum of 6 adults and 2 children can be booked on a single PNR. While for a tatkal ticket, the figures are 4 adults and 2 children. The details of each passenger consist of 7 records. They are mentioned below in the same order as the script.

1. **passenger** : Name of the passenger. To be entered in uppercase.
2. **age** : Age of the passenger.
3. **gender** : Gender of the passenger. (**M** = Male, **F** = Female, **T** = Transgender. For eg. if the passenger is female, enter                   **F** in this field.)
4. **berth** : Berth preference (**LB** = Lower berth, **MB** = Middle berth, **UB** = Upper berth, **SL** = Side Lower, **SU** = Side                  Upper, **WS** = Window Side. For eg., if you want the upper berth, enter **UB** in this field). This field is not                        mandatory and can be skipped. Please note that WS is to be entered only for CC and 2S class.
5. **meal** : Meal preference (**V** = Veg, **N** = Non Veg, **D** = No Food. For eg., if you wish to eat non-veg, enter **N** in this                 field). To be entered only for Shatabdi, Rajdhani, Duronto or any such trains where food is served. Do note that this                   field is mandatory if food is served in your train. Else, you can leave it blank.
6. **concession_preference** : To be availed only if you are a senior citizen. For females, the age limit is 58 years and for males it                                  is 60 years. (**1** = Avail full concession, **2** = Forgo 50% concession, **3** = Forgo full concession.                                For eg., if you wish to avail the full concession (why wouldn't you :P), enter **1** in this field.)
7. **bed_roll** : Available only in Garib Rath trains and Duronto sleeper class at a charge of ₹25 per passenger. If you wish to avail                     this service, enter **Y** in this field, else leave it blank.

**IMPORTANT** <br />
Leave the credentials of the other passengers blank in case you are less than 6 people travelling. For eg, if you are 3 people travelling on general quota, fill up the credentials from passenger 1 to passenger 3 and keep the remaining credentials (4-6) blank.
Also in tatkal quota, the credentials of only the first 4 passengers (1-4) will be taken into account. <br /><br />

Now comes the child passenger details. At most 2 children can be booked on a single ticket. Three details exist for each child. These are mentioned in the same order as the script.
1. **child_passenger** : Name of the child. To be entered in uppercase.
2. **child_age** : Age of the child. (**0** = Below one year, **1** = One year, **2** = Two years, **3** = Three years, **4** = Four                        years. For eg., if the child is below one year, enter **0** in this field.)
3. **child_gender** : Gender of the child. (**M** = Male, **F** = Female. For eg., if the child is male, enter **M** in this field.)

Now we have the miscellaneous options. Filling these fields is not mandatory, though you can always choose. For all these options, enter **Y** if you wish to select it, else enter **N**. Again, these are mentioned in the same order as in the script. For the uninitiated, I'm talking about this secton. <br /><br />
![screenshot_3](https://user-images.githubusercontent.com/29803330/35811911-a6597d56-0ab5-11e8-9d0d-eeb64b7ccd66.jpg) <br />

1. **auto_upgrade** : Consider for auto-upgradation.
2. **confirm_berths** : Book only if confirm berths are allotted.

For the below 3 options, at max one of them is to be selected as **Y**. <br />
&nbsp; &nbsp; 3. **all_berths** : Book only if all berths are allotted in the same coach. <br />
&nbsp; &nbsp; 4. **one_lb** : Book only if at least one lower berth is allotted. <br />
&nbsp; &nbsp; 5. **two_lb** : Book only if at least two lower berths are allotted. <br />

6. **preferred_coach_id** : If yes, enter the coach id in the next field.
7. **coach_id** : To be entered only if the previous field is set to **Y**. For eg., if you are booking in sleeper class and ant your                     seat in S7 coach, enter **S7** in this field.
8. **mobile_no** : Contact number where your ticket will be sent. Mandatory field.

Now comes another important part, the payment section. At present, the script allows two methods of payment, 'IRCTC eWallet' and 'Preferred Banks'. The eWallet used to be the fastest mode of payment, until IRCTC introduced OTP for this feature. But still, you have the option to pay using this feature in the script. So, as of now, the fastest mode for payment is Debit Card, as it does not require OTP (for majority of the banks), but instead your ATM password, saving you those precious few seconds.
As there are close to 25 banks on the IRCTC website, it was not possible to provide auto-click option for each one of those. To overcome this problem, you can add your bank in the 'Preferred Banks' section. (At max 6 banks can be added to the preferred banks section).
If you have an SBI Debit Card, you can further save 4-5 seconds as the script provides you to auto-fill your card no, validity and name. Providing this feature for all other banks was not possible for obvious reasons. Also, the ATM password auto-fill is not added for security purposes. Long story short, an SBI debit card will be your best bet for booking your ticket, cause you'll only have to enter your ATM password and captcha.
Otherwise, if you have any other bank debit card, keep your card number and name already written somewhere, and at the time of booking, paste it in the respective fields.
Once you have added you bank in the 'Preferred Banks' section, let us take a look at using the auto-payment feature. These are the following field you'll have to enter.
1. **auto_payment** : Whether you want to use this feature or not. (Enter **Y** for yes and **N** for no.)
2. **auto_payment_option** : Which option so you want to choose for auto-payment? (**1** = Preferred Banks, **2** = IRCTC eWallet. For                                eg., if you want to use the eWallet feature for payment, enter **2** in this field.)
3. **auto_payment_suboption** : To be entered only if the **auto_payment_option** is set to **1**. This field can take only values from                                 1 to 6, and represents the order of your bank in the 'Preferred Banks' section. You'll understand it                                     better from the below image.
4. **eWallet_password** : Your IRCTC eWallet password. To be entered only if the **auto_payment_option** is set to **2**.

<br />![image](https://user-images.githubusercontent.com/29803330/35818504-46978f6e-0ac6-11e8-95dd-191b55ebe8bf.png)<br />

For eg., in the above image, if you want to select ICICI bank net banking as your payment method, the above 4 fields will look something like this.

<br />![image](https://user-images.githubusercontent.com/29803330/35818744-d07cd48c-0ac6-11e8-9963-d4af076d0482.png)<br />

Selecting **auto_payment_suboption** as **2** means the order of the bank in the sequence. If it were instead **1**, it will select SBI Debit card.

Now suppose, you wanted to use the eWallet method for booking, then the 4 fields will look something like this.

<br />![image](https://user-images.githubusercontent.com/29803330/35819000-811c1604-0ac7-11e8-9dc3-7860f41b2575.png)<br />

The last four input fields of this script are to be entered **ONLY IF YOU HAVE AN SBI DEBIT CARD**. Else, leave it blank.
1. **card_id** : Your debit card number.
2. **card_validity_month** : Enter in numeric form, i.e., **04** = April, **10** = October, etc.
3. **card_validity_year** : Enter in numeric form, for eg., **2012**, **2015**, etc.
4. **card_name** : Cardholder's name. To be entered in uppercase only.
