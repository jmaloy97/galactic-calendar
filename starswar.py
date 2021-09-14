# starswar.py
# @auth: Asami T.
# @desc: Fanfiction calendar systems are cool, bro.

months = ["Quietsun", "Frostwane", "Newgrowth", "Dayrise", "Sweltersurge", "Hopewatch", "Sunpeak", "Amberfall", "Skyshine", "Chillfall"]
days = ["Dawnday", "Sunsday", "Moonday", "Triday", "Forceday", "Midweek", "Hexday", "Soilday", "Duskday", "Restday"]

day = 0
rawday = 0
monthval = 0
yearval = 0
weekday = ""
monthname = ""
debugmode = 0
eraname = ""
explanation = "There is no historical information about this year implemented yet."
emptyvar = ""

print("Asami's Star Wars Calendar - Informational Python Program")
print("======================")
print("For the sake of quick mathematics when it comes to determining day/month")
print("in my Star Wars fanfics, I have decided to make a quick utility")
print(" to help with that.\n")

def dayDeclaration():
    global rawday
    while True:
        try:
            rawday = int(input("What day do you want to see? (1-99): "))
            break
        except:
            print("NOT A NUMBER - ID 10T ERROR")

def monDec():
    global monthval
    while True:
        try:
            monthval = int(input("What month do you want? (1-10): "))
            break
        except:
            print("NOT A NUMBER")

def yrDec():
    global yearval
    while True:
        try:
            yearval = int(input("Enter a year value: "))
            break
        except:
            print("NOT A NUMBER")

def dayChk():
    while rawday <= 0 or rawday >= 100:
        dayDeclaration()

def monChk():
    while monthval <= 0 or monthval > 10:
        monDec()

def date_and_time():
    global rawday
    dayDeclaration()
    dayChk()
    weekdayGeneration()
    monDec()
    monChk()
    monthGeneration()
    yrDec()

def weekdayGeneration():
    global weekday
    global dayTwo
    dayTwo = rawday%10
    weekday = days[dayTwo]

def monthGeneration():
    global monthval
    global monthname
    monthname = months[monthval-1]

while rawday > 99 or rawday < 1:
    date_and_time()

if yearval < 0:
    eraname = "AE"
else:
    eraname = "ME"

yearval = abs(yearval)

if eraname == "AE":
    emptyvar = ".-"
    if yearval == 478:
        explanation = "478 AE marks the Ruusan Reformation and the beginning of the Ruusan Republican era."

if eraname == "ME":
    emptyvar = "."
    if yearval == 0:
        explanation = "Year Zero in the Galactic Calendar is marked as the promulgation of the modern Galactic constitution, not the Ruusan Reformation."
    if yearval == 500:
        explanation = "500 ME marked the beginning of the Clone Wars."
    elif yearval == 503:
        explanation = "503 ME marked the end of the Clone Wars and the rise of the first Galactic Empire."
    elif yearval == 546:
        explanation = "546 ME marks the rise of the nouveau Sith under the rule of Harry Potter."

print("\n" + weekday + ", " + monthname + " " + str(rawday) + " " + str(yearval) + " " + str(eraname))
print(str(rawday) + "." + str(monthval) + emptyvar + str(yearval))
print("==============")
print(explanation)

while debugmode == 1:
    print(weekday + ", " + monthname + " " + str(rawday))
    date_and_time()