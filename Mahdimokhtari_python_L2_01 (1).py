import getpass

print(' ')
print(40 *'=')
print('((password sterenght checker))')
print(40 *'=')
print(' ')

score = 0
failed_checked = []
pass_checked = []
sterength_pass = []
commen_password = ["123456", "12345678", "qwerty", "password", "admin", "welcome"]

while True:
    username = input('please enter your user name : ')
    password = getpass.getpass('please enter your password : ')
    birth_year = input('please enter your birth year (e.g  1999): ')
    if username.strip() == '' or password.strip() == '' or birth_year.strip() == '' :
        print('username can not be emty or only space! try again')
        print('password can not be emty or only space! try again')
        print('birth_year can not be emty or only space! try again')
        continue
    break

try:
    birth_year=int(birth_year)
    if 1900 <= birth_year <=2026:
        if str(birth_year) in password:
        
            failed_checked.append('password must not contain your birth year. ')
        else:
            pass_checked.append('password does not contain your birth year.')
            sterength_pass.append('password is safe from your birth year.')
            emtiaz+=1
    else:
        print('\nbirth year is out of range(1900-2026).')
except ValueError:
    print('\n birth year must be a number:')

#بررسی طول رمز -حداقل هشت کارکتر
if len(password) >=8:
    emtiaz+=1
    pass_hecked.append('password lenght  is good. ')
    sterength_pass.append('good password lenght. ')
else:
    failed_checked.append('password lenght must be at least 8 charcters. ')
    
#بررسی داشتن عدد-حداقل دارای یک عدد باشد
has_digit = False
for  i in password:
    if i in "0123456789":
        has_digit = True
        break
if has_digit:
    emtiaz+=1
    pass_checked.append('password contain digit. ')
    sterength_pass.append('your password contain digit. ')  
else:
    failed_checked.append('password must be contain at least one digit. ')
    
#بررسی حروف بزرگ و کوچگ-حداقل داری یک حروف بزرگ و کوچگ باشد
has_upper=False
has_lower=False
for i in password:
    code = ord(i)
    if 65 <= code <= 90:
        has_upper=True
        break
    for i in password:
        code = ord(i)
    if 97 <= code <= 122:
        has_lower=True
        break
if has_upper and has_lower:
    emtiaz+=1
    pass_checked.append('password contain at least one upper and lower letters.')
    sterength_pass.append('password contain a lower and upper case letter. ')
else:
     failed_checked.append('password must contain both  lower and upper case letters. ')
     
#بررسی داشتن کارکتر خاص-حداقل دارای یک کارکتر خاص باشد
has_special=False
for i in password:
    if i in "!@#$%^&*?=+/":
        has_special=True
        break
if has_special:
    emtiaz+=1
    pass_checked.append('password contain at least one special letter. ')
    sterength_pass.append('password contain special letter. ')        
else:
    failed_checked.append('password must be contain a special letter.')
    
#برابر نبودن پسورد با یوزرنیم-حروف کوچک را بررسی میکنیم
if password.lower() != username.lower():
    emtiaz+=1
    pass_checked.append('password is diffrent from username. ')
    sterength_pass.append('diffrent from username. ')
else:
    failed_checked.append('password must be diffrent from username. ')
#پسورد جرو رمز های رایج نباشد-حروف کوچک را بررسی میکنیم
if password.lower() not in commen_password:
    emtiaz+=1
    pass_checked.append('password is not  commen password. ')
    sterength_pass.append('password is not commen. ')
else:
    failed_checked.append('password must not be a commen password. ')
#مشخص کردن سطح رمز
if emtiaz <= 2:
    level= 'weak'
elif emtiaz <= 4:
    level='medium'
elif emtiaz <=6:
    level='strong'
else:
    level=' very strong'
# نمایش نتایج
print(80 * '=')
print(f'password sternght :{emtiaz} /7' )
print(80 *"=")
print(f'level :{level}')
print(80 *'=')
print('\npass_checked : ')
if len(pass_checked) > 0:
    for item in pass_checked:
        print('-',item)
print(80*'=')
print('\nfialed checked : ')
if len(failed_checked) > 0:
    for eror in failed_checked:
        print('-' ,eror  )
else:
    print('none!perfect password.')
print(80 *'=')
print('\nsterenght : ')
if len(pass_checked) > 0:
    for sterenght in sterength_pass:
        print('-' , sterenght)
else:
     print('none')
print(80 *"=")
print('remember: a strong password keeps your account safe.')
print('thank for using')
print(80 * '=')