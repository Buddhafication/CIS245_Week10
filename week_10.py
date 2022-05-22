# -*- coding: utf-8 -*-
"""

Adam Eckert
CIS 245: Week_10
22 May 2022

"""

import pandas as pd
import os
import time

#%%

def collect_and_write(x):
    
    print('What would you like to name your file?')
    time.sleep(1)
    file_name = input('ENTER HERE: ')
    print()
    time.sleep(1)
    
    
    print('Okay. Now I need to gather some of your details to add to your file.')
    print()
    time.sleep(1)
    
    
    print('What is your name?')
    time.sleep(1)
    user_name = input('ENTER HERE: ')
    time.sleep(1)
    print()
    
    
    print('Gotcha. What is your address?')
    user_address = input('ENTER HERE: ')
    print()
    time.sleep(1)
    
    print('Sweet. Finally, what is your phone number?')
    user_number = input('ENTER HERE: ')
    print()
    time.sleep(1)
    
    print('Creating your file now')
    time.sleep(2)
    df = pd.DataFrame({'Name': user_name, 'Address': user_address, 'Phone Number': user_number}, index=[0])
    
    global write_name
    write_name = f'{x}/{file_name}.csv'
    
    df.to_csv(write_name, index = False)

#%%



time.sleep(.5)
print()
print(f'Default working directory of this program is: {os.getcwd()}')

time.sleep(.5)

print()
print('What\'s the name of the folder you\'d like to work in?')
time.sleep(.5)
folder = input('ENTER HERE: ')
print()

time.sleep(.5)

if '\\' not in folder:
    folder = '\\' + folder
    
path = str(os.getcwd() + folder)

time.sleep(.5)
print('Okay, checking if that folder exists. \n')

time.sleep(1)

#%%

if os.path.isdir(path) == True:
    print('This folder exists! Moving into it now \n')
    os.chdir(path)
    
    collect_and_write(path)
    time.sleep(1)
    print()
    print('Success! Now I\'ll list the files in the folder, then read back to you the contents of your file.')
    print()
    time.sleep(1)
    
    print('Here are the files in the folder: ')
    time.sleep(1)
    print(os.listdir(path))
    print()
    
    data = pd.read_csv(write_name)
    print(f'Here are the contents of your file "{write_name}": ')
    time.sleep(1)
    print()
    print(data.to_string(index = False))
    print()
    time.sleep(1)
    
    print('Looks like everything worked. Goodbye!')
        
else:
    print('That folder doesn\'t already exist in our current working directory. Enter "Yes" if you\'d like to create it, "No" if you\'d like to exit. ')
    user_status = input('ENTER HERE: ').title()
    
    if user_status == 'Yes':
        os.mkdir(path)
        os.chdir(path)
        print()
        
        collect_and_write(path)
        time.sleep(1)
        print()
        print('Success! Now I\'ll list the files in the folder, then read back to you the contents of your file.')
        print()
        time.sleep(1)
        
        print('Here are the files in the folder: ')
        time.sleep(1)
        print(os.listdir(path))
        print()
        
        data = pd.read_csv(write_name)
        print(f'Here are the contents of your file "{write_name}": ')
        time.sleep(1)
        print()
        print(data.to_string(index = False))
        print()
        time.sleep(3)
        
        print('Looks like everything worked. Goodbye!')
        
    else:
        print()
        print('Okay! Goodbye.')