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
        res = dts * 24 * 60 * 60
        res1 = dts * 24 * 60
        res2 = dts * 24
        print(dts, ' Days Converted to : ', str(res), ' seconds , Which is ' + str(res1) + ' minutes ,Which is ' + str(res2) + ' Hours')

    elif data.lower() == 'std':
        std = int(input('Please enter the amount of seconds : '))
        std1 = std // (24 * 3600)
        std2 = (std - std1 * 3600 * 24) // 3600
        std3 = (std - std1 * 3600 * 24 - std2 * 3600) // 60
        print(std, 'Seconds Converted to days : ', str(std1), 'Days And ' + str(std2) + ' Hours And ' + str(std3) + ' Minutes')
    elif data.lower() == 'mtd':
        mtd = int(input('Please enter the amount of minutes : '))
        mtd1 = mtd // (24 * 60)
        mtd2 = (mtd - mtd1 * 24 * 60 ) // 60
        mtd3 = (mtd - mtd1 * 24 * 60 - mtd2 * 60)
        print(mtd, 'Minutes converted to days : ', str(mtd1), 'Days And ' + str(mtd2) + ' Hours And ' + str(mtd3) + ' Minutes '  )
    elif data.lower() == 'htd':
        htd = int(input('Please enter the amount of hours : '))
        htd1 = htd // 24
        htd2 = (htd - htd1 * 24)
        print(htd, 'Hours converted to : ', str(htd1), 'Days And ' + str(htd2) + ' Hours ')
    elif data.lower() == 'sth':
        sth = int(input('Please enter the amount of seconds : '))
        sth1 = float(sth / 3600)
        sth2 = (sth - sth1 * 3600 ) // 60
        print(sth, 'Seconds converted to : ', str(sth1), 'Hours And ' + str(sth2) + ' Minutes')
    elif data.lower() == quit:
        break

