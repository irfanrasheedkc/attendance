#!python 3
file = open(r'C:\users\asus\desktop\attendance.txt', 'a')
while 1:
    subject = input("Enter subject : ")
    total = int(input("Enter total number of class : "))
    attend = int(input("Enter total number of attended class : "))
    current_percentage = attend / total * 100
    print("Current percentage is : {:.2f}".format(current_percentage))
    file.write('* {}     {}    {}    {:.2f} \n'.format(subject,total,attend,current_percentage))
    test=0
    while current_percentage<90:
        current_percentage=(attend+test)/(total+test)*100
        if (current_percentage<90):
            test=test+1
        else:
            break
    file.write('     {} more class is required for getting attendance above 90%  \n\n'.format(test))
    cont=input('Continue Y/N :')
    if(cont=='N' or cont=='n'):
        break
file.close()
