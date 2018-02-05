# Author
# Praneet Kumar, B.Tech CSE
# NIT Silchar, Class of 2019

from selenium import webdriver as driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------  USER INPUT -------------------- #

username = ''
password = ''

source = ''
destination = ''
DOJ = ''

train_no = ''
travelling_class = ''
boarding_station = ''
quota = ''

''' ADULT PASSENGER DETAILS '''

passenger_1 = ''
age_1 = ''
gender_1 = ''
berth_1 = ''
meal_1 = ''
concession_preference_1 = ''
bed_roll_1 = ''

passenger_2 = ''
age_2 = ''
gender_2 = ''
berth_2 = ''
meal_2 = ''
concession_preference_2 = ''
bed_roll_2 = ''

passenger_3 = ''
age_3 = ''
gender_3 = ''
berth_3 = ''
meal_3 = ''
concession_preference_3 = ''
bed_roll_3 = ''

passenger_4 = ''
age_4 = ''
gender_4 = ''
berth_4 = ''
meal_4 = ''
concession_preference_4 = ''
bed_roll_4 = ''

passenger_5 = ''
age_5 = ''
gender_5 = ''
berth_5 = ''
meal_5 = ''
concession_preference_5 = ''
bed_roll_5 = ''

passenger_6 = ''
age_6 = ''
gender_6 = ''
berth_6 = ''
meal_6 = ''
concession_preference_6 = ''
bed_roll_6 = ''

''' CHILD PASSENGER DETAILS (Less than age 5) '''

child_passenger_1 = ''
child_age_1 = ''
child_gender_1 = ''

child_passenger_2 = ''
child_age_2 = ''
child_gender_2 = ''

''' MISCELLANEOUS OPTIONS '''

auto_upgrade = ''
confirm_berths = ''

all_berths = ''
one_lb = ''
two_lb = ''

preferred_coach_id = ''
coach_id = ''
mobile_no = ''

''' PAYMENT OPTIONS '''

auto_payment = ''
auto_payment_option = ''
auto_payment_suboption = ''
eWallet_password = ''

card_id = ''
card_validity_month = ''
card_validity_year = ''
card_name = ''


# --------------------  ADD ALL THE ADULT PASSENGER DETAILS IN A LIST  ------------------- #

adults_detail = [[] for i in range(6)]
adults_detail[0].extend([passenger_1, age_1, gender_1, berth_1, meal_1, concession_preference_1, bed_roll_1])
adults_detail[1].extend([passenger_2, age_2, gender_2, berth_2, meal_2, concession_preference_2, bed_roll_2])
adults_detail[2].extend([passenger_3, age_3, gender_3, berth_3, meal_3, concession_preference_3, bed_roll_3])
adults_detail[3].extend([passenger_4, age_4, gender_4, berth_4, meal_4, concession_preference_4, bed_roll_4])
adults_detail[4].extend([passenger_5, age_5, gender_5, berth_5, meal_5, concession_preference_5, bed_roll_5])
adults_detail[5].extend([passenger_6, age_6, gender_6, berth_6, meal_6, concession_preference_6, bed_roll_6])
# print(adults_detail)                   # Uncomment to see all the adult passengers' details.


# --------------------  ADD ALL THE CHILD PASSENGER DETAILS IN A LIST  --------------------- #

children_detail = [[] for i in range(2)]
children_detail[0].extend([child_passenger_1, child_age_1, child_gender_1])
children_detail[1].extend([child_passenger_2, child_age_2, child_gender_2])
# print(children_detail)                 # Uncomment to see all the child passengers' details.


# ----------------  CHECK NO. OF PASSENGERS TRAVELLING  --------------- #

val1, val2, pax = 0, 0, 0
for i in range(0, 6):
    if adults_detail[i][0] == '':
        val1 += 1
    if adults_detail[i][6] == '':
        val2 += 1
    if len(adults_detail[i][0]) != 0:
        pax += 1
print("\nNo. of passengers travelling : " + str(pax))


# ---------------------  INITIALIZE CHROMEDRIVER  ---------------------- #

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"                     # Enable explicit wait.
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')             # Start Chrome maximized.
url = 'http://www.irctc.co.in'
driver = webdriver.Chrome('E:\Python\chromedriver.exe', desired_capabilities=capa, chrome_options=options)  # Arguments
driver.get(url)


# --------------------  LOGIN PAGE  ----------------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.CLASS_NAME, "labeltxt")))

username_box = driver.find_element_by_id('usernameId')                         # Get username box.
password_box = driver.find_element_by_class_name('loginPassword')              # Get password box.
username_box.send_keys(username)                                               # Fill in username.
password_box.send_keys(password)                                               # Fill in password.


# --------------------  FUNCTION TO WAIT FOR A PARTICULAR URL  -------------------- #


def wait_for_url(desired_url):
    WebDriverWait(driver, 150).until(lambda driver: driver.current_url == desired_url)

desired_url = 'https://www.irctc.co.in/eticketing/home'
wait_for_url(desired_url)                                        # Wait for successful login.
print("\nLogin successful!\n")


# ----------------------  CHECK FOR PREVIOUS ACTIVE SESSION  ---------------------- #

try:
    WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Services ']")))
    forward = driver.find_elements_by_tag_name('input')     # Store all 'input' elements.

    for i in range(0, len(forward)):
        att = forward[i].get_attribute('value')             # Get 'value' attribute of all 'input' elements.
        if att == 'Continue':
            print("Previous active session found.\n")
            forward[i].click()                              # Auto click 'Continue' if session exists.
except:
    pass


# ------------------  JOURNEY DETAILS PAGE  --------------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, "jpform:jpsubmit")))     # Explicit wait

source_box = driver.find_element_by_id('jpform:fromStation')                 # Get source station box.
destination_box = driver.find_element_by_id('jpform:toStation')              # Get destination station box.
DOJ_box = driver.find_element_by_id('jpform:journeyDateInputDate')           # Get date of journey box.
submit_button = driver.find_element_by_id('jpform:jpsubmit')                 # Get submit button box.

source_box.send_keys(source)                                                 # Enter source station code.
source_box.send_keys(Keys.RETURN)
destination_box.send_keys(destination)                                       # Enter destination station code.
destination_box.send_keys(Keys.RETURN)
DOJ_box.send_keys(DOJ)                                                       # Enter date of journey.
submit_button.click()                                                        # Click submit button.


# ---------------------  CHECK IF TRAIN RUNS ON GIVEN DAY  ------------------------- #

try:
    WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.LINK_TEXT, train_no)))     # Explicit wait
    print("Train found.\n")
except:
    print("Sorry, train does not exist or does not run on the given day.\n")


# -------------------  SELECT TRAVELLING QUOTA  ------------------------ #

for i in driver.find_elements_by_name('quota'):               # Get all available quotas.
    quota_box = i.get_attribute('value')                      # Get 'value' of all quotas.
    if quota == quota_box:
        i.click()
        break


# ----------------------  ALERT BOX HANDLING FOR HANDICAPPED QUOTA  ----------------------- #

if quota == 'HP':
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),                     # Wait for alert box to appear.
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert                                            # Change driver to alert box mode.
        alert.accept()                                                            # Auto - accept alert.
        print("Handicapped quota alert accepted.\n")
    except:
        pass


# ---------------------  FIND THE TRAIN FROM THE TRAIN LIST  ----------------------- #

default_id = 'cllink-' + train_no + '-' + travelling_class + '-'

for i in driver.find_elements_by_xpath('//*[contains(@id, "cllink")]'):      # Search using partial id.
    full_id = i.get_attribute('id')                                          # Get full id.
    if default_id in full_id:
        new_id = full_id

        class_link = driver.find_element_by_id(new_id)                        # Find travelling class link.
        driver.execute_script("arguments[0].scrollIntoView()", class_link)    # Bring link in view.
        class_link.click()                                                    # Auto - click link.
        break

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.LINK_TEXT, 'Book Now')))       # Explicit wait.

book_now = str(train_no) + '-' + str(travelling_class) + '-' + quota + '-0'        # ID of 'Book now' link.
availability_link = driver.find_element_by_id(book_now)                            # Get ID.

'''
Normal 'link.click()' doesn't work here and throws an element not clickable exception. Hence we use browser controls
to click on the link.
'''
driver.execute_script("arguments[0].click();", availability_link)


# ----------------------  ALERT BOX HANDLING FOR DIFFERING STATION CODES  ----------------------- #

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),                        # Wait for alert box to appear.
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert                                               # Change driver to alert box mode.
    alert.accept()                                                               # Auto - accept alert.
    print("Differing station code alert accepted.\n")
except:
    pass


# -------------------  AVAILABILITY IN OTHER TRAINS EXCEPTION HANDLING  ------------------------ #

try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'altavlfrm:continue')))   # Explicit wait.

    click = driver.find_element_by_id('altavlfrm:continue')                     # Get id of 'Continue'.
    click.click()                                                               # Click on 'Continue'.
except:
    pass


# ----------------------  PASSENGER DETAILS PAGE  --------------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.input-style1.psgn-name')))

if source == boarding_station:                      # Check if source and boarding station are same.
    pass
else:
    bs_option = driver.find_element_by_id('addPassengerForm:boardingStation')     # Get all available boarding stations.
    for option in bs_option.find_elements_by_tag_name('option'):
        scode = option.get_attribute('value')                                     # Get value of each boarding station.
        if scode == boarding_station:                                             # Select the corresponding station.
            option.click()
            break


# ------------------------  FILL IN PASSENGER NAMES  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.psgn-name'):
    i.send_keys(adults_detail[count][0])
    count += 1


# ------------------------  FILL IN PASSENGER AGES  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.psgn-age.only-numeric'):
    i.send_keys(adults_detail[count][1])
    count += 1

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.psgn-gender'):
    count += 1

# ------------------------  FILL IN PASSENGER GENDERS  ---------------------- #

''' The reason this block of code is different from other passenger information filling codes is that I was constantly 
getting an Element not Visible exception here. Even after applying all the workarounds mentioned on stackoverflow and 
other websites, the problem persisted. The following way is another hack which I accidentally discovered. Though it's
not the best method, but still works.'''

for i in range(0, pax):
    actions = ActionChains(driver)
    age_id = 'addPassengerForm:psdetail:' + str(i) + ':psgnAge'
    print(age_id)
    tab_id = driver.find_element_by_id(age_id)
    if adults_detail[i][2] == 'F':
        tab_id.send_keys(Keys.TAB + Keys.ARROW_RIGHT)
    elif adults_detail[i][2] == 'M':
        tab_id.send_keys(Keys.TAB + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT)
    elif adults_detail[i][2] == 'T':
        tab_id.send_keys(Keys.TAB + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT)


# ------------------------  FILL IN BERTH CHOICES  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.psgn-berth-choice'):
    for berth_options in i.find_elements_by_tag_name('option'):
        berth = berth_options.get_attribute('value')
        if adults_detail[count][3] == berth:
            berth_options.click()
            count += 1
            break


# ------------------------  FILL IN MEAL CHOICES (IF ANY)  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.psgn-foodChoice'):
    for meal_options in i.find_elements_by_tag_name('option'):
        meal = meal_options.get_attribute('value')
        if adults_detail[count][4] == meal:
            meal_options.click()
            count += 1
            break


# ------------------------  FILL IN CONCESSION OPTIONS (IF ANY)  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.psgn-concopt'):
    for concession_options in i.find_elements_by_tag_name('option'):
        concession = concession_options.get_attribute('value')
        if adults_detail[count][5] == concession:
            concession_options.click()
            count += 1
            break


# ------------------------  FILL IN BED ROLL CHOICES (IF ANY)  ---------------------- #

for i in range(0, 6):
    if adults_detail[i][6] == 'Y':
        string = 'addPassengerForm:psdetail:' + str(i) + ':bedRollOpt'
        br_option = driver.find_element_by_id(string)
        br_option.click()


# ------------------------  FILL IN CHILD PASSENGER NAMES  ---------------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.input-style1.infant-name')))

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.infant-name'):
    i.send_keys(children_detail[count][0])
    count += 1


# ------------------------  FILL IN CHILD PASSENGER AGES  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.infant-age'):
    for child_age_options in i.find_elements_by_tag_name('option'):
        child_age = child_age_options.get_attribute('value')
        if children_detail[count][1] == child_age:
            child_age_options.click()
            count += 1
            break


# ------------------------  FILL IN CHILD PASSENGER GENDERS  ---------------------- #

count = 0
for i in driver.find_elements_by_css_selector('.input-style1.infant-gender'):
    for child_gender_options in i.find_elements_by_tag_name('option'):
        child_gender = child_gender_options.get_attribute('value')
        if children_detail[count][2] == child_gender:
            child_gender_options.click()
            count += 1
            break


# ------------------------  FILL IN MISCELLANEOUS DETAILS  ---------------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, 'validate')))   # Explicit wait

try:
    auto_upgrade_box = driver.find_element_by_id('addPassengerForm:autoUpgrade')        # Get 'auto - upgrade' element.
    if auto_upgrade == 'Y':
        driver.execute_script("arguments[0].scrollIntoView()", auto_upgrade_box)        # Bring element in view.
        auto_upgrade_box.click()                                                        # Auto - click element.
except:
    pass

try:
    confirm_berths_box = driver.find_element_by_id('addPassengerForm:onlyConfirmBerths')  # Get 'confirm berth' element.
    if confirm_berths == 'Y':
        confirm_berths_box.click()                                                        # Auto - click element.
except:
    pass

try:
    all_berths_box = driver.find_element_by_id('addPassengerForm:bookingCond:1')          # Get 'condition 1' element.
    one_lb_box = driver.find_element_by_id('addPassengerForm:bookingCond:2')              # Get 'condition 2' element.
    two_lb_box = driver.find_element_by_id('addPassengerForm:bookingCond:3')              # Get 'condition 3' element.

    if all_berths == 'Y':                                                            # Select the appropriate element.
        all_berths_box.click()
    elif one_lb == 'Y':
        one_lb_box.click()
    elif two_lb == 'Y':
        two_lb_box.click()

    preferred_coach_id_box = driver.find_element_by_id('addPassengerForm:prefCoachOpt')  # Get 'coach id' element.
    preferred_coach_id_details = driver.find_element_by_id('addPassengerForm:coachID')  # Get 'coach id detail' element.

    if preferred_coach_id == 'Y':                               # Fill in given coach id.
        preferred_coach_id_box.click()
        preferred_coach_id_details.send_keys(coach_id)
except:
    pass

mobile_no_box = driver.find_element_by_id('addPassengerForm:mobileNo')         # Get 'mobile no' element.
mobile_no_box.clear()                                                          # Clear the field of any previous value.
mobile_no_box.send_keys(mobile_no)                                             # Fill in contact number.


# ------------------------  HANDLE BED ROLL ALERT EXCEPTION  ---------------------- #

flag = 0
try:
    driver.find_element_by_class_name('psgn-bedRollChoice')     # Check if bed roll service exists for the given train.
    flag = 1
except:
    pass

if flag == 1 and val1 != val2:       # If it exists and all passengers have not opted for it, handle alert.
    WebDriverWait(driver, 150).until(EC.alert_is_present(),                     # Wait for alert box to appear.
                                     'Timed out waiting for PA creation ' +
                                     'confirmation popup to appear.')

    alert = driver.switch_to.alert                                              # Change driver to alert box mode.
    alert.accept()                                                              # Auto - accept alert.
    print("Bed roll alert exception handled.\n")

    WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-button-text')))

    yn = driver.find_elements_by_class_name('ui-button-text')                   # Check for lower berth anomaly.
    for i in range(0, len(yn)):
        if yn[i].text == 'Yes':
            yn[i].click()


# -----------------------  PAYMENT OPTIONS PAGE  ------------------------- #

desired_url = 'https://www.irctc.co.in/eticketing/jpInput.jsf?cid=1'
wait_for_url(desired_url)                                                              # Wait for payment options page.
WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, 'validate')))  # Explicit wait


# -----------------------  SELECT APPROPRIATE PAYMENT METHOD  ------------------------- #

if auto_payment == 'Y':
    if auto_payment_option == '1':                                 # If 'preferred banks' is the payment option.
        count = 1

        for i in driver.find_elements_by_name('PREFERRED'):        # Get list of all preferred banks.
            if count == int(auto_payment_suboption):               # Select the appropriate bank.
                driver.execute_script("arguments[0].scrollIntoView()", i)       # Bring element in view.
                i.click()                                                       # Auto - click element.
                break
            else:
                count += 1

    elif auto_payment_option == '2':                               # If 'eWallet' is the payment option.
        eWallet_tab = driver.find_element_by_id('E_WALLET')        # Get 'eWallet' element.
        driver.execute_script("arguments[0].scrollIntoView()", eWallet_tab)      # Bring element in view.
        eWallet_tab.click()                                                      # Click on element.

        password_field = driver.find_element_by_id('jpBook:rdsTxnPswd')          # Get 'eWallet password' element.
        password_field.send_keys(eWallet_password)                               # Fill in the password.

make_payment = driver.find_element_by_id('validate')                             # Get 'Make Payment' element.
driver.execute_script("arguments[0].scrollIntoView()", make_payment)             # Bring element in view.
make_payment.click()                                                             # Auto - click element.


# ----------------------  HANDLE ANY PAYMENT ALERT EXCEPTION  ----------------------- #

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.accept()
    print("Payment alert accepted.\n")
except:
    pass


# ----------------------  AUTO FILL CARD DETAILS (ONLY FOR SBI DEBIT CARD) ------------------ #

if auto_payment_option == '1' and len(card_id) != 0:
    WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, 'debitCardNumber')))   # Explicit wait.

    # ----------------------  AUTO FILL CARD NUMBER  ------------------- #

    card_id_box = driver.find_element_by_id('debitCardNumber')
    card_id_box.send_keys(card_id)

    # ----------------------  AUTO FILL CARD VALIDITY MONTH  ------------------- #

    month_option = driver.find_element_by_id('debiMonth')
    for option in month_option.find_elements_by_tag_name('option'):
        month = option.get_attribute('value')
        if month == card_validity_month:
            option.click()
            break

    # ----------------------  AUTO FILL CARD VALIDITY YEAR  ------------------- #

    year_option = driver.find_element_by_id('debiYear')
    for option in year_option.find_elements_by_tag_name('option'):
        year = option.get_attribute('value')
        if year == card_validity_year:
            option.click()
            break

    # ----------------------  AUTO FILL CARDHOLDER NAME  ------------------- #

    name_box = driver.find_element_by_id('debitCardholderName')
    name_box.send_keys(card_name)


# -----------------------  FUNCTION TO CHECK FOR SUCCESSFUL BOOKING  -------------------- #


def wait_for_title(desired_title):
    WebDriverWait(driver, 150).until(lambda driver: driver.title == desired_title)

desired_title = 'Booking Confirmation'
wait_for_title(desired_title)                                        # Wait for successful booking.

print("Ticket booked successfully!")