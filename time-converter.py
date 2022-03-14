print('''
#############TIME CONVERTER BY YAHIA OUALI#######
#                                               #
#                version 0.0 bla bla            #
#             Enter help to see commands        #
#                                               #
#################################################
''')


data = ""
while data.lower() != 'quit':
    data = input('> ')

    if data.lower() == 'help':
        print('''
    If you want to convert days to seconds enter : dts
    If you want to convert hours to days enter : htd
    If you want to convert seconds to days enter : std
    If you want to convert minutes to days enter : mtd
    If you want to convert seconds to hours enter : hts
    
    Type QUIT to quit the program!

       ''')
    elif data.lower() == 'dts':
         dts = int(input('Please enter the number of days : '))
         res = int(dts * 24 * 60 * 60)
         print(dts, ' Days Converted to : ', res, 'seconds')

    elif data.lower() == 'std':
        std = int(input('Please enter the amount of seconds : '))
        std1= float(std / (24 * 3600))
        print(std , 'Seconds Converted to days : ' , "{:.2f}".format(std1) , 'Days')
    elif data.lower() == 'mtd':
        mtd = int(input('Please enter the amount of minutes : '))
        mtd1 = float(mtd / (24 * 60))
        print(mtd , 'Minutes converted to days : ' , "{:.2f}".format(mtd1), 'Days')
    elif data.lower() == 'htd':
        htd = int(input('Please enter the amount of hours : '))
        htd1 = float(htd / 24)
        print(htd , 'Hours converted to : ', "{:.2f}".format(htd1), 'Days')
    elif data.lower() == 'sth':
        sth = int(input('Please enter the amount of seconds : '))
        sth1 = float(sth / 3600)
        print(sth, 'Seconds converted to : ', "{:.2f}".format(sth1) , 'Hours')
    elif data.lower() == quit :
        break

