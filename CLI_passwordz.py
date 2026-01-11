import secrets
import time 
import sys

def basic_or_creative(b_or_c):
    if b_or_c == 'b':
        warning_msg = 'warning: our basic passwords are quite weak'
        for chr in warning_msg: 
             sys.stdout.write(chr)
             sys.stdout.flush()
             time.sleep(0.05)
        time.sleep(1)
        print('\n')
        
        change_msg = 'would you like to switch to a creative password? '
        for chr in change_msg: 
             sys.stdout.write(chr)
             sys.stdout.flush()
             time.sleep(0.05)
        
        time.sleep(0.25)
    
        change = input('type y or n: ')
        while change != 'n' and change != 'y':
            change = input('please input y or n: ')
            
    else: 
         change = 'y'
    
    password = generate_password(change)
         
    txt_out = f'your password is: {password} \n'
    
    for chr in txt_out:
        sys.stdout.write(chr)
        sys.stdout.flush()
        time.sleep(0.05)
    
def new_pass_input():
    new_pass = 'would you like a new password? '
    for chr in new_pass:
        sys.stdout.write(chr)
        sys.stdout.flush()
        time.sleep(0.05)
    
    new_pass_ans = input('type y or n: ')

    while new_pass_ans != 'y' and new_pass_ans != 'n':
         new_pass_ans = input('please type y or n: ')

    if new_pass_ans == 'y':
        gen_new_password(new_pass_ans)
    else:
        txt_out = 'see ya next time!'
        for chr in txt_out:
            sys.stdout.write(chr)
            sys.stdout.flush()
            time.sleep(0.05)

def gen_new_password(new_pass_ans):
    b_or_c = 'would you like a basic or creative password? '
    for chr in b_or_c:
         sys.stdout.write(chr)
         sys.stdout.flush()
         time.sleep(0.05)
    
    input_b_c = input('type b or c: ')

    while input_b_c != 'b' and input_b_c != 'c':
         input_b_c = input('please type b or c: ')
    if input_b_c == 'b':
         change = 'n'
    else:
         change = 'y'
    
    new_pass = generate_password(change)
    pass_stmt = f'your new password is {new_pass}'
    for chr in pass_stmt:
        sys.stdout.write(chr)
        sys.stdout.flush()
        time.sleep(0.05)
    
     
def generate_password(change):
    passwords = []
    password_chrs = [] 
    rough_password = []
    
    if change == 'n':
            infile = open('basic.txt', 'r')
            read = infile.readline().strip()
            passwords.append(read)
            while read != '':
                read = infile.readline().strip()
                passwords.append(read)
            infile.close()
            password = secrets.choice(passwords)
       
    if change == 'y': 
        infile = open('creative.txt', 'r')
        read = infile.readline().strip()
        passwords.append(read)
        while read != '':
            read = infile.readline().strip()
            password_chrs.append(read)
        infile.close()
        
        for i in range(12): # Canadian Centre for Cyber Security recommends a min. of 12 characters for passwords
            chr = secrets.choice(password_chrs)
            rough_password.append(chr)
        seperator = ''
        password = seperator.join(rough_password)
    
    return password

def main():
        intro_msg = 'would you like a basic or creative password? \n'
        for chr in intro_msg: 
             sys.stdout.write(chr)
             sys.stdout.flush()
             time.sleep(0.05)
        b_or_c = input('please type b or c: ')
        basic_or_creative(b_or_c)
        time.sleep(0.75)
        new_pass_input()
        
main()
