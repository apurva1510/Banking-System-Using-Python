import pickle,os,random
class newacc:
    def __init__(self):
        self.user="null"
        self.password="null"
        self.acctype=0
        self.accno=0
        self.name="null"
        self.gender="null"
        self.income=0
        self.email="null"
        self.dob="null"
        self.address="null"
        self.desig="null"
        self.company="null"
        self.telno="null"
        self.mobno="null"
        self.balance=0

    def uspas(self):
        digits=' 0123456789 '
        us=' '
        while True:
            try:
                length=Exception("Maximum no: of char = 10 .")
                num=Exception("Should contain digits ." )
                dig=0
                us=raw_input("Enter the username you wish to use (maximum 10 characters and should contain numeric characters) : ")
                if len(us)>10:
                    raise length
                else:
                    for i in us:
                        if i.isdigit():
                            dig=1
                            break
                    if dig ==0:
                        raise num
            except Exception, length:
                print length.message
            except Exception, num:
                print num.message
            else:
                self.user=us
                break
        while True:
            try:
                length=Exception("Maximum no: of char = 10 .")
                num=Exception("Should contain digits ." )
                pas=raw_input("Enter the password (Your password must contain Base 10 digits (0 through 9) and a minimum length of 10 characters :")
                dig=0
                for i in pas:
                    if i in digits:
                        dig+=1
                        break
                z=len(pas)
                if dig==0:
                    raise num
                elif z<10:
                    raise length
            except Exception, num:
                print num.message
            except Exception, length:
                print length.message
            else:
                cpd=raw_input("Confirm your password: ")
                if pas==cpd:
                    print "Your account has been created."
                    self.password=pas
                    break
                else:
                    print "Passwords do not match."

    def getdata(self):
        print "At OOEHS we offer three types of accounts depending on your day to day needs"
        print "1)Savings Account \n2) Current Account \n3) Fixed Deposit Account"
        self.acctype=input ("For Savings Account , Press 1. \nFor Current Account , Press 2. \nFor Fixed Deposit Account, Press 3. \nYour choice: ")
        if self.acctype==1:
            self.balance=8000
        elif self.acctype==2:
            self.balance=4000
        elif self.acctype==3:
            self.balance=10000
        self.income=input("Monthly Income: ")
        if self.income <5000:
            print "You are not eligible for creating a call deposit account as your monthly income is less than 5000. "
            self.getdata()
        self.accno=random.randint(111111,999999)
        self.name=raw_input("Name: ")
        self.gender=raw_input("Gender (M/F): ")
        self.email=raw_input("Email ID: ")
        self.dob=raw_input("Date of Birth (dd/mm/yyyy): ")
        self.address=raw_input("Residence Address: ")
        self.desig=raw_input("Designation: ")
        self.company=raw_input("Company Name: ")
        self.telno=raw_input("Telephone Number: ")
        self.mobno=raw_input("Mobile Number: ")
        self.uspas()
        print "PLS NOTE DOWN YOUR ACCOUNT NUMBER: ",self.accno
    def update(self,c):
        print "NOTE: Account Type, Account Number and Balance cannot be updated. \n Only personal details can be updated. "    
        self.acctype,self.balance,self.accno=c.acctype,c.balance,c.accno
        ch=raw_input("Do you want to change the name? ")
        if ch.lower()=='y' or ch.lower()=='yes':
            self.name=raw_input("Name:")
        else:
            self.name=c.name
        ch=raw_input("Do you want to change the income?")
        if ch.lower()=='y' or ch.lower()=='yes':
            self.income=raw_input("Income: ")
        else:
            self.income=c.income
        ch=raw_input("Do you want to update the gender information?")
        if ch.lower()=='y' or ch.lower()=='yes':
            self.gender=raw_input("Gender(M/F): ")
        else:
            self.gender=c.gender
        ch=raw_input("Do you want to change the email id?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.email=raw_input("Email ID: ")
        else:
            self.email=c.email
        ch=raw_input("Do you want to change the date of birth?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.dob=raw_input("Date of Birth (dd/mm/yyyy):  ")
        else:
            self.dob=c.dob
        ch=raw_input("Do you want to change the Residence Address?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.address=raw_input("Residence Address: ")
        else:
            self.address=c.address
        ch=raw_input("Do you want to change the designation?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.desig=raw_input("Designation:  ")
        else:
            self.desig=c.desig
        ch=raw_input("Do you want to change the company?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.company=raw_input("Company Name : ")
        else:
            self.company=c.company
        ch=raw_input("Do you want to change the telephone number?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.telno=raw_input("Telephone Number: ")
        else:
            self.telno=c.telno
        ch=raw_input("Do you want to change the mobile number?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.mobno=raw_input("Mobile Number: ")
        else:
            self.mobno=c.mobno
        ch=raw_input("Do you want to change the username and password?")
        if ch.lower()=='y'or ch.lower()=='yes':
            self.uspas()
        else:
            self.user=c.user
            self.password=c.password
        print "Your Personal details have been updated successfully"
    def display(self):
            print "Personal Details"
            print "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            print "%10s\t%4s\t%6s\t%13s\t%10s\t%8s\t%8s\t%8s\t%9s\t%9s\t"%(self.name,self.gender,self.income,self.email,self.dob,self.address,self.desig,self.company,self.telno,self.mobno)
            print
            print "Account Details"
            print "------------------------------------"
            print "%8s\t%10s\t%6s\t" %(self.accno,self.acctype,self.balance)
            print
class LOANS:
    def __init__(self):
        self.accno=0
        self.name="null"
        self.Type=0
        self.r=0
        self.p=0
        self.ty=0
        self.tm=0
        self.repay="null"
        self.amt=0
    def loans(self,c):
        self.accno=c.accno
        self.name=c.name
        print "OOEHS Banking provides a wide range of loan options to choose from. \nThis quality of utility gives you the decision of selecting the type of loan you wish to use depending on your purpose. \n And as responsible bankers, your satisfaction is our priority ."
        self.Type=input("1.Home Equity \n2.Education \n3.Personal \n4.Buisness \n5.Vehicle \n6.Farming \nEnter the type of loan you wish to take: ")
        if self.Type==1:
            self.r=random.randint(14,17)
            print self.r, "% is the interest rate per annum."
        elif self.Type==2:
            self.r=random.randint(6,9)
            print self.r, "% is the interest rate per annum."
        elif self.Type==3:
            self.r=random.randint(5,8)
            print self.r, "% is the interest rate per annum."
        elif self.Type==4:
            self.r=random.randint(10,13)
            print self.r, "% is the interest rate per annum."
        elif self.Type==5:
            self.r=random.randint(8,12)
            print self.r, "% is the interest rate per annum."
        elif self.Type==6:
            self.r=random.randint(3,5)
            print self.r, "% is the interest rate per annum."
        asset=raw_input("Do you have an asset(y/n)? ")
        if asset=='n':
            print 'Without an asset, you do not have the permission to take the loan.'
        elif asset=='y':
            self.p=input("Total amount required: ")
            self.ty=input("Total number of years: ")
            self.tm=input("Remaining number of months: ")
            T=self.ty+(self.tm/12.0)
            si=(self.p*self.r*T)/100.0
            L=si+self.p
            print '\nHow do you wish to repay your loan?'
            self.repay=input("1.One-time \n2.Monthly \n3. 6 Months \nEnter your choice: ")
            if self.repay==1:
                self.amt=L
                print "\nAmount to be paid in exactly ", self.ty, "years and  ",self.tm, " months is ", self.amt, "."
            elif self.repay==2:
                self.amt=L/float((self.ty*12.0)+self.tm)
                print "\nAmount to be paid monthly is ",self.amt
            elif self.repay==3:
                self.am=L/float((self.ty*12.0)+self.tm)
                self.amt=self.am*6.0
                print '\nYou have to pay' , self.amt , 'for every six months.'
def newaccount():
    c=newacc()
    c.getdata()
    f=open("account1.dat","ab")
    pickle.dump(c,f)
    f.close()
def existaccount():
    ano=input("\nEnter your account number: ")
    f=open("account1.dat","rb")
    c=newacc()
    validuser=0
    try:
        while True:
            c=pickle.load(f)
            if c.accno==ano:
                uname=raw_input("\nEnter username: ")
                pas=raw_input("\nEnter password")
                if uname==c.user and pas==c.password:
                    validuser=1
                    break
    except EOFError:
        ano=0
    if validuser==1:
        print "\n\n\t\tWELCOME  ",  c.name.upper()
    f.close()
    return ano
def deposit(r,amt):
    f=open("account1.dat","rb")
    f1=open("temp.dat","wb")
    try:
        while True:
            c=pickle.load(f)
            if c.accno==r:
                c.balance+=amt
                print "\nYour Account balance is updated. \nCurrent Balance is: ", c.balance
            pickle.dump(c,f1)
    except EOFError:
        pass
    f.close()
    f1.close()
    os.remove("account1.dat")
    os.rename("temp.dat","account1.dat")
def withdraw(r,amt):
    f=open("account1.dat","rb")
    f1=open("temp.dat","wb")
    try:
        while True:
            c=pickle.load(f)
            if c.accno==r:
                if c.balance-amt>=500:
                    c.balance-=amt
                    print "\nAccount balance is updated.\nCurrent Balance is: ",c.balance
                else:
                    print "\nMinimum balance should be AED 500.\n You cannot withdraw this much amount."
            pickle.dump(c,f1)
    except EOFError:
        pass
    f.close()
    f1.close()
    os.remove("account1.dat")
    os.rename("temp.dat","account1.dat")
def custoptions(r):
    while True:
        os.system('cls')
        print
        ch=input("1.View Account details.\n\n2.Deposit.\n\n3.Withdraw.\n\n4.Update personal information \n\n5.Apply for a loan \n\nEnter your choice: ")
        if ch==1:
            f=open("account1.dat","rb")
            try:
                while True:
                    c=pickle.load(f)
                    if c.accno==r:
                        c.display()
                        break
            except EOFError:
                pass
            f.close()
        elif ch==2:
            amt=input("\nEnter the amount to be deposited: ")
            deposit(r,amt)
        elif ch==3:
            amt=input("\nEnter the amount to be withdrawn: ")
            withdraw(r,amt)
        elif ch==4:
            flag=0
            f=open("account1.dat","rb")
            f1=open("temp.dat","wb")
            c=newacc()
            d=newacc()
            try:
                while True:
                    c=pickle.load(f)
                    if c.accno==r:
                        d.update(c)
                        pickle.dump(d,f1)
                        print "\nPlease login again with the new credentials."
                        flag=1
                    else:
                        pickle.dump(c,f1)
            except EOFError:
                pass
            f.close()
            f1.close()
            os.remove("account1.dat")
            os.rename("temp.dat","account1.dat")
            if flag==1:
                break
        elif ch==5:
            n=LOANS()
            c=newacc()
            f=open("account1.dat","rb")
            try:
                while True:
                    c=pickle.load(f)
                    if c.accno==r:
                        n.loans(c)
                        break
            except EOFError:
                pass
            f.close()
            lo=open('loans.dat','ab')
            pickle.dump(n,lo)
            lo.close()
        opt=raw_input("\nDo you want to do some other transactions")
        if opt.lower()=='no' or opt.lower()=='n':
            break
def viewallcust():
    f=open("account1.dat","rb")
    print "------------------------------------------------------------------------------------------------------------------------------"
    print "Account Number| Customer Name | Account Type | Balance | Loan Type| Loan EMI  |"
    print "-------------------------------------------------------------------------------------------------------------------------------"
    try:
        while True:
            c=pickle.load(f)
            f1=open("loans.dat","rb")
            try:
                while True:
                    l=pickle.load(f1)
                    if c.accno==l.accno:
                        print "%20s|%24s|%21d|%11d|%15d|%14d |\n\n" %(c.accno,c.name,c.acctype,c.balance,l.Type,l.amt)
                        break
            except EOFError:
                print "%20s|%24s|%21d|%11d|\t|\t|\n\n" %(c.accno,c.name,c.acctype,c.balance)
            f1.close()
    except EOFError:
        pass
    f.close()
def closeacc(r):
        flag=0
        accexist=0
        f1=open("loans.dat","rb")
        try:
            while True:
                l=pickle.load(f1)
                if l.accno==r:
                    ch=raw_input("\nWould you like to payoff the loan amount? ")
                    if ch.lower()=='n' or ch.lower()=='no':
                        print "\nAccount cannot be closed."
                        flag=1
                        break
                    else:
                        break
        except EOFError:
            print "\nNo such account number."
            accexist=1
            pass
        f1.close()
        if accexist==0 or flag==0:
            f=open("account1.dat","rb")
            t=open("temp.dat","wb")
            try:
                while True:
                    c=pickle.load(f)
                    if c.accno!=r:
                        pickle.dump(c,t)
            except EOFError:
                f.close()
                t.close()
                os.remove("account1.dat")
                os.rename("temp.dat","account1.dat")
            f=open("loans.dat","rb")
            t=open("temp.dat","wb")
            try:
                while True:
                    c=pickle.load(f)
                    if c.accno!=r:
                        pickle.dump(c,t)
            except EOFError:
                f.close()
                t.close()
                os.remove("loans.dat")
                os.rename("temp.dat","loans.dat")
            print "\nYour account has been closed."
##  Check Indentations
while True:
    os.system('cls')
    print
    print
    mainmenu=input("_______ OOEHS BANKING _______ \n\n\n1.ADMIN\n\n2.CUSTOMER\n\nEnter your option as 1 or 2: ")
    print
    if mainmenu==1:
        while True:
            os.system('cls')
            print"\n\n"
            passkey=raw_input("Enter the passkey: ")
            if passkey=="admin123":
                print "\n------------ADMIN MENU------------\n\n"
                adminopt=input("1.VIEW ALL CUSTOMERS DATA BANK.\n\n2.CLOSE AN ACCOUNT . \n\n Enter your choice: ")
                print
                if adminopt==1:
                    viewallcust()
                elif adminopt==2:
                    accno=input("\nEnter the account number: ")
                    print
                    closeacc(accno)
                else:
                    print "\n"
            else:
                print "\nWrong Passkey."
            opt1=raw_input("\nDo you wish to try again? ")
            if opt1.lower()=="no" or opt1.lower()=="n":
                break
    if mainmenu==2:
        while True:
            os.system('cls')
            print "\n\n--------------CUSTOMER MENU--------------\n\n"
            custopt=input("1.NEW ACCOUNT.\n\n2.EXISTING ACCOUNT.\n\nPlease enter 1 or 2: ")
            print
            if custopt==1:
                newaccount()
            elif custopt==2:
                r=existaccount()
                if r:
                    custoptions(r)
                else:
                    print "\nThis account number does not exist."
            else:
                print "\nInvalid Choice."
            opt2=raw_input("\nDo you wish to return to Customer Menu? ")
            if opt2.lower()=='no' or opt2.lower()=='n':
                break
    else:
        print "\nInvalid Choice"
    opt3=raw_input("\nDo you wish to go to the Main Menu? ")
    if opt3.lower()=='no'or opt3.lower()=='n':
        break
