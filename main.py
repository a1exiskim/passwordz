import secrets
     
def generate_password(choice):
    passwords = []
    password_chrs = [] 
    rough_password = []
    
    if choice == 'b':
            infile = open('basic.txt', 'r')
            read = infile.readline().strip()
            passwords.append(read)
            while read != '':
                read = infile.readline().strip()
                passwords.append(read)
            infile.close()
            password = secrets.choice(passwords)
       
    if choice == 'c': 
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
