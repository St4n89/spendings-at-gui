#!/usr/bin/env python
import csv
import re
import os
import datetime
import calendar

gettime = datetime.datetime.now() #getting times-dates for filenames
month_now = calendar.month_abbr[gettime.month]
timestamp = str(str(gettime.day)+"-"+str(month_now)+"-"+str(gettime.year))
out_filename = str("Spendings "+timestamp+".csv")

if os.path.isfile('unknown.csv'): #removing old files if exist
    os.remove('unknown.csv')

if os.path.isfile(out_filename): #removing old files if exist
    os.remove(out_filename)


def dictionarize(file, dictionary): #this creates dictionaries out of files
    dictfile = open(file)
    with dictfile as input_file:
        for line in input_file:
            key, value = line.split(":")
            dictionary[key] = value.strip()


def parsing_alfa(dictionary,nameline):
    expenses_lines = [] #array for csv processing
    removals = [] #storage for the removed entries

    with open('output_alfa.csv') as input_file: #get input from formatted csv
        read = csv.reader(input_file, delimiter=';')
        fin_file = open(out_filename,'a')

        fin_file.write(nameline) #writing category name to output file
        fin_file.write("\n")

        for row in read: #creating 2D array of expenses
            expenses_rows = [row[0],row[1],row[2]]
            expenses_lines.append(expenses_rows)

        for str_num in range(len(expenses_lines)):
            sms = expenses_lines[str_num][1]
            for word in dictionary:
                found = sms.count(word) #search for word from dictionary
                if found:
                    store = dictionary.get(word)
                    realdate = ((re.search('[0-9][\s][0-9][0-9].[0-9][0-9].[0-9][0-9]', sms)).group(0)) #read date from sms line
                    expdate = str((re.search('[0-9][0-9].[0-9][0-9].[0-9][0-9]', realdate).group(0)).replace('.', '/')) #getting actual date
                    cost = int(round(float(expenses_lines[str_num][2].replace(',', '.'))))
                    fin_file.write((expdate+"20"+";"+store+";"+str(cost)+"\n"))
                    removals.append(str_num) #adding the found entry to the list for removals

    removals.sort(reverse=True) #reversing, so that the last entries popped out first
    expenses_copy = list(expenses_lines) #copying the list to tamper with the copy

    for rem_str_num in range(len(removals)): #this is needed to get the list of unprocessed entries
        expenses_copy.pop(removals[rem_str_num]) #popping out found entries

    os.remove('output_alfa.csv')
    temp_file = open('output_alfa.csv','a')
    for fin_str_num in range(len(expenses_copy)): #here will be the unprocessed entries
        tempdate = str(expenses_copy[fin_str_num][0].replace('.', '/')) #correcting the date format
        temp_file.write((tempdate+";"+expenses_copy[fin_str_num][1]+";"+expenses_copy[fin_str_num][2]+"\n"))


def parsing_alfa_single(dictionary,nameline):
    expenses_lines = [] #array for csv processing
    removals = [] #storage for the removed entries

    with open('output_alfa.csv') as input_file: #get input from formatted csv
        read = csv.reader(input_file, delimiter=';')
        fin_file = open(out_filename,'a')

        fin_file.write(nameline) #writing category name to output file
        fin_file.write("\n")

        for row in read: #creating 2D array of expenses
            expenses_rows = [row[0],row[1],row[2]]
            expenses_lines.append(expenses_rows)

        for str_num in range(len(expenses_lines)):
            sms = expenses_lines[str_num][1]
            for word in dictionary:
                found = sms.count(word) #search for word from dictionary
                if found:
                    store = dictionary.get(word)
                    realdate = ((re.search('[0-9][\s][0-9][0-9].[0-9][0-9].[0-9][0-9]', sms)).group(0)) #read date from sms line
                    expdate = str((re.search('[0-9][0-9].[0-9][0-9].[0-9][0-9]', realdate).group(0)).replace('.', '/')) #getting actual date
                    cost = int(round(float(expenses_lines[str_num][2].replace(',', '.'))))
                    fin_file.write((expdate+"20"+";"+store+";"+str(cost)+"\n"))
                    removals.append(str_num) #adding the found entry to the list for removals

    removals.sort(reverse=True) #reversing, so that the last entries popped out first
    expenses_copy = list(expenses_lines) #copying the list to tamper with the copy

    for rem_str_num in range(len(removals)): #this is needed to get the list of unprocessed entries
        expenses_copy.pop(removals[rem_str_num]) #popping out found entries

    os.remove('output_alfa.csv')
    temp_file = open('output_alfa.csv','a')
    for fin_str_num in range(len(expenses_copy)): #here will be the unprocessed entries
        tempdate = str(expenses_copy[fin_str_num][0].replace('.', '/')) #correcting the date format
        temp_file.write((tempdate+";"+expenses_copy[fin_str_num][1]+";"+expenses_copy[fin_str_num][2]+"\n"))

    fin_file.write("\n")


def parsing_tinky(dictionary,nameline):
    expenses_lines = []
    removals = []

    with open('output_tinky.csv') as input_file:
        read = csv.reader(input_file, delimiter=';')
        fin_file = open(out_filename,'a')

        fin_file.write(nameline) #writing category name to output file
        fin_file.write("\n")

        for row in read:
            expenses_rows = [row[0],row[1],row[2]]
            expenses_lines.append(expenses_rows) #building the 2D list of transactions

        for str_num in range(len(expenses_lines)):
            sms = expenses_lines[str_num][1]
            for word in dictionary:
                found = sms.count(word)
                if found:
                    store = dictionary.get(word)
                    expdate = expenses_lines[str_num][0]
                    cost = int(round(float(expenses_lines[str_num][2].replace('-', ''))))
                    fin_file.write((expdate+";"+store+";"+str(cost)+"\n"))
                    removals.append(str_num) #adding the found entry to the list for removals

    removals.sort(reverse=True) #reversing, so that the last entries popped out first
    expenses_copy = list(expenses_lines)

    for rem_str_num in range(len(removals)):
        expenses_copy.pop(removals[rem_str_num]) #popping out found entries

    os.remove('output_tinky.csv')
    temp_file = open('output_tinky.csv','a')
    for fin_str_num in range(len(expenses_copy)): #here will be the unprocessed entries
        temp_file.write((expenses_copy[fin_str_num][0]+";"+expenses_copy[fin_str_num][1]+";"+expenses_copy[fin_str_num][2]+"\n"))

    fin_file.write("\n")

def parsing_tinky_mute(dictionary):
    expenses_lines = []
    removals = []

    with open('output_tinky.csv') as input_file:
        read = csv.reader(input_file, delimiter=';')
        fin_file = open(out_filename,'a')

        for row in read:
            expenses_rows = [row[0],row[1],row[2]]
            expenses_lines.append(expenses_rows) #building the 2D list of transactions

        for str_num in range(len(expenses_lines)):
            sms = expenses_lines[str_num][1]
            for word in dictionary:
                found = sms.count(word)
                if found:
                    store = dictionary.get(word)
                    expdate = expenses_lines[str_num][0]
                    cost = int(round(float(expenses_lines[str_num][2].replace('-', ''))))
                    fin_file.write((expdate+";"+store+";"+str(cost)+"\n"))
                    removals.append(str_num) #adding the found entry to the list for removals

    removals.sort(reverse=True) #reversing, so that the last entries popped out first
    expenses_copy = list(expenses_lines)

    for rem_str_num in range(len(removals)):
        expenses_copy.pop(removals[rem_str_num]) #popping out found entries

    os.remove('output_tinky.csv')
    temp_file = open('output_tinky.csv','a')
    for fin_str_num in range(len(expenses_copy)): #here will be the unprocessed entries
        temp_file.write((expenses_copy[fin_str_num][0]+";"+expenses_copy[fin_str_num][1]+";"+expenses_copy[fin_str_num][2]+"\n"))

    fin_file.write("\n")


def formatcsv_alfa(filename): #formatting alfabank csv files
    with open(filename) as input_file:
        read = csv.reader(input_file, delimiter=';')
        with open('output_alfa.csv','w', newline='') as output:
            next(read)
            write = csv.writer(output, delimiter=';')
            for row in reversed(list(read)):
                hold_status = row[4] #processing unfinished transactions in the log
                found_hold = hold_status.count("HOLD")
                if found_hold: #if the transaction is in HOLD status
                    write.writerow((row[3]+"20", ("00 "+str(row[3])+" "+str(row[5])), row[7])) #add date to sms line
                else:
                    if row[7] != "0": #if the transaction is an expense
                        write.writerow((row[3]+"20", row[5], row[7])) #do not change the sms line
                    else: #if it is not an expense
                        write.writerow((row[3]+"20", ("00 "+str(row[3])+" "+str(row[5])), row[6])) #add date to sms line


def formatcsv_tinky(filename): #formatting tinkoff csv files
    with open(filename) as input_file:
        read = csv.reader(input_file, delimiter=';')
        with open('output_tinky.csv','w', newline='') as output:
            next(read)
            write = csv.writer(output, delimiter=';')
            for row in reversed(list(read)):
                realdate = ((re.search('[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]', row[0])).group(0).replace('.', '/'))
                cost = int(round(float(str(row[4]).replace(',', '.').replace('-',''))))
                write.writerow((str(realdate), row[11], cost))


def execute_alfa(path):
        groceries = {} #creating the dictionaries
        transport = {}
        entertainment = {}
        others = {}
        cars = {}
        living = {}
        clarifications = {}
        medicine = {}
        restaurants = {}

        dictionarize('groceries.dic', groceries) #dictionarizing them
        dictionarize('transport.dic', transport)
        dictionarize('entertainment.dic', entertainment)
        dictionarize('others.dic', others)
        dictionarize('cars.dic', cars)
        dictionarize('living.dic', living)
        dictionarize('clarifications.dic', clarifications)
        dictionarize('medicine.dic', medicine)
        dictionarize('restaurants.dic', restaurants)

        formatcsv_alfa(path) #formatting the input files

        parsing_alfa_single(groceries, "Products")  # parsing the temp-output files
        parsing_alfa_single(transport, "Transport")  # it is needed for correct processing
        parsing_alfa_single(entertainment, "Entertainment")
        parsing_alfa_single(others, "Others")
        parsing_alfa_single(cars, "Cars")
        parsing_alfa_single(living, "Living")
        parsing_alfa_single(medicine, "Medicine")
        parsing_alfa_single(restaurants, "Restaurants")
        parsing_alfa_single(clarifications, "For review")


def execute_tinky(path):
    groceries = {}  # creating the dictionaries
    transport = {}
    entertainment = {}
    others = {}
    cars = {}
    living = {}
    clarifications = {}
    medicine = {}
    restaurants = {}

    dictionarize('groceries.dic', groceries)  # dictionarizing them
    dictionarize('transport.dic', transport)
    dictionarize('entertainment.dic', entertainment)
    dictionarize('others.dic', others)
    dictionarize('cars.dic', cars)
    dictionarize('living.dic', living)
    dictionarize('clarifications.dic', clarifications)
    dictionarize('medicine.dic', medicine)
    dictionarize('restaurants.dic', restaurants)

    formatcsv_tinky(path)

    parsing_tinky(groceries, "Products")  # parsing the temp-output files
    parsing_tinky(transport, "Transport")  # it is needed for correct processing
    parsing_tinky(entertainment, "Entertainment")
    parsing_tinky(others, "Others")
    parsing_tinky(cars, "Cars")
    parsing_tinky(living, "Living")
    parsing_tinky(medicine, "Medicine")
    parsing_tinky(restaurants, "Restaurants")
    parsing_tinky(clarifications, "For review")

def execute_both(path1, path2):
    groceries = {}  # creating the dictionaries
    transport = {}
    entertainment = {}
    others = {}
    cars = {}
    living = {}
    clarifications = {}
    medicine = {}
    restaurants = {}

    dictionarize('groceries.dic', groceries)  # dictionarizing them
    dictionarize('transport.dic', transport)
    dictionarize('entertainment.dic', entertainment)
    dictionarize('others.dic', others)
    dictionarize('cars.dic', cars)
    dictionarize('living.dic', living)
    dictionarize('clarifications.dic', clarifications)
    dictionarize('medicine.dic', medicine)
    dictionarize('restaurants.dic', restaurants)

    formatcsv_alfa(path1) #formatting the input files
    formatcsv_tinky(path2)

    parsing_alfa(groceries,"Products") #parsing the temp-output files
    parsing_tinky_mute(groceries)
    parsing_alfa(transport,"Transport") #it is needed for correct processing
    parsing_tinky_mute(transport)
    parsing_alfa(entertainment,"Entertainment")
    parsing_tinky_mute(entertainment)
    parsing_alfa(others,"Others")
    parsing_tinky_mute(others)
    parsing_alfa(cars,"Cars")
    parsing_tinky_mute(cars)
    parsing_alfa(living,"Living")
    parsing_tinky_mute(living)
    parsing_alfa(medicine,"Medicine")
    parsing_tinky_mute(medicine)
    parsing_alfa(restaurants,"Restaurants")
    parsing_tinky_mute(restaurants)
    parsing_alfa(clarifications,"For review")
    parsing_tinky_mute(clarifications)


def csvmerge(): #merging two temp-output files into one
    if (os.path.isfile('output_alfa.csv') and os.path.isfile('output_tinky.csv')):
        readalfa = open('output_alfa.csv') #so that it has unknown transactions
        readtink = open('output_tinky.csv') #from both input files

        writecsv = open('unknown.csv','a')

        for line in readalfa:
            writecsv.write("ALFBANK;"+(line)) #ALFA to know if the line is from alfabank

        for line in readtink:
            writecsv.write("TINKOFF;"+line) #CITI to know if the line is from citibank

        readalfa.close()
        readtink.close()
        writecsv.close()

        os.remove('output_tinky.csv')
        os.remove('output_alfa.csv')
    else:
        if os.path.isfile('output_alfa.csv'):
            os.rename('output_alfa.csv','unknown.csv')
        else:
            if os.path.isfile('output_tinky.csv'):
                os.rename('output_tinky.csv', 'unknown.csv')