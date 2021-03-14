from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Food
from .forms import food_form
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def index(request) :

    if request.method == 'POST' :
        print('its post')





        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        def count_day(day) :
            count = 0
            for dic in data:
                if dic['day'] == day :
                    count += 1
            return count

        def each_days_total(day, which) :
            if dic['day'] == day:
                which[food] += dic[food]
            return which

        def average(day, count) :
            for food in food_items :
                av = day[food] / count
                string = str(av)
                slice = string[:4]
                if len(slice) == 3 : # makes each output 4 characters
                    slice = slice + '0'
                day[food] = slice
            return day

        def output(full_weekday, day_dic) :
            print('  ' + full_weekday + ' - ')
            print('    ', end='')
            for k,v in day_dic.items() :
                print(k + ':', v, '| ', end='')
            print('\n')


        # connect to google sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)


        stores = ['test1']

        # store = input('Store name (lower case): ')
        # if store == '' :
        #     name = 'testing2'
        # else :
        #     name = store + ' food waste log'

        for store in stores :

            print('Running for:', store)

            name = store + ' food waste log'

            try :
                sheet = client.open(name).sheet1
            except :
                print('Problem opening spreadsheet')
                quit()

            # month/year for file names
            month_year = sheet.acell('A1').value

            # print(month_year)
            # print(type(month_year))

            raw_data = sheet.get_all_records(empty2zero=True, head=2)
            # print('=================================')
            # print('=================================')
            # print('RAW DATA')
            # print(raw_data)
            # print('==============')
            # print('==============')

            data = []
            index = -1 # keeps track of index to delete any accidental extra rows
            for dic in raw_data :
                index = index + 1

                try :
                    dic.pop('number')
                except :
                    print('Problem removing number column from dataset')
                    quit()

                if '' in dic.keys() : # deletes accidental extra columns
                    dic.pop('')

                if dic['day'] != 0 : # creates new dictionary without accidental extra rows
                    data.append(dic)
            # print(data)

            # error checks for non-numbers in dataset
            for dic in data :
                for key, value in dic.items() :
                    if key != 'day' : # excludes key 'day'/weekday values from int(v)
                        try :
                            value = int(value)
                        except :
                            print('Spreadsheet values should be numbers only')
                            quit()

            #Calculations
            food_items = []

            sun = {} # turn these into objects to loop later rather than repeating code down below, array mapping?
            mon = {}
            tue = {}
            wed = {}
            thu = {}
            fri = {}
            sat = {}

            # gets food items in list
            for key,value in data[0].items() :
                food_items.append(key)
            food_items.pop(0)

            # sets up dictionaries for each day with correct food items set to zero
            for food in food_items :
                sun.update({food: 0}) # loop through ojects mentioned above?
                mon.update({food: 0})
                tue.update({food: 0})
                wed.update({food: 0})
                thu.update({food: 0})
                fri.update({food: 0})
                sat.update({food: 0})

            sun_count = count_day('sun')
            mon_count = count_day('mon')
            tue_count = count_day('tue')
            wed_count = count_day('wed')
            thu_count = count_day('thu')
            fri_count = count_day('fri')
            sat_count = count_day('sat')

            for food in food_items :
                for dic in data :
                    each_days_total('sun', sun)
                    each_days_total('mon', mon)
                    each_days_total('tue', tue)
                    each_days_total('wed', wed)
                    each_days_total('thu', thu)
                    each_days_total('fri', fri)
                    each_days_total('sat', sat)

            average(sun, sun_count) # could probably make this into loop if sun/mon/tue etc were in an object
            average(mon, mon_count)
            average(tue, tue_count)
            average(wed, wed_count)
            average(thu, thu_count)
            average(fri, fri_count)
            average(sat, sat_count)

            # calculates total waste
            total_waste = 0
            for dic in data:
                for key,value in dic.items():
                    try:
                        num = int(value)
                    except:
                        continue
                    total_waste = total_waste + num

            # outputs
            print('======================')
            print('Total Waste:', total_waste, 'items')
            print('======================')

            print('Averages: \n')
            output('Sunday', sun) # same as above, could make loop if sun/mon etc were in an object
            output('Monday', mon)
            output('Tuesday', tue)
            output('Wednesday', wed)
            output('Thursday', thu)
            output('Friday', fri)
            output('Saturday', sat)





        context = {
        'total_waste' : total_waste,
        'month_year' : month_year,
        'sun' : sun,
        'mon' : mon,
        'tue' : tue,
        'wed' : wed,
        'thu' : thu,
        'fri' : fri,
        'sat' : sat,
        }
        return render(request, 'tacoapp/index.html', context)


    else :
        print('not post')
        context = {
            'context' : 'no post',
        }
        return render(request, 'tacoapp/index.html', context)


    return render(request, 'tacoapp/index.html')

@login_required
def reset(request) :
    if request.method == 'POST' :
        print('post yes')

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        import time

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        # this gets the month number successfully
        import datetime
        from datetime import date

        today = datetime.date.today()
        str_today = str(today)
        month = str_today[5:7]
        if month[0] == '0' : # makes one digit if first number is 0
            month = month[1:2]

        current_month = int(month)
        current_year = int(str_today[:4])
        month_year_for_email = str_today[5:8] + str_today[:4]
        # print(current_month)
        # print(current_year)

        stores = ['test1']
        sheet_count = 0

        # store = input('Store name (lower case): ')
        # if store == '' :
        #     name = 'testing2'
        # else :
        #     name = store + ' food waste log'

        for store in stores :

            sheet_count = sheet_count + 1
            print('Sheet number:', sheet_count)
            print('Running for:', store)

            name = store + ' food waste log'

            try :
                sheet = client.open(name).sheet1
            except :
                print('Problem opening spreadsheet, check store name spelling and case.')
                quit()

            month_year = sheet.acell('A1').value
            print(month_year)

            # data_file_name = store + '-files/' + store + '_data_' + month_year + '.txt'
            # calcs_file_name = store + '-files/' + store + '_calcs_' + month_year + '.txt'

            # try :
            #     check_if_file = open(data_file_name)
            # except :
            #     print('Stopped clearing sheets, data files not present')
            #     continue

            # name = 'westlake food waste log'
            # sheet = client.open(name).sheet1
            # data = sheet.get_all_records(empty2zero=True, head=2)
            # print(data)

            import calendar
            from calendar import monthrange

            month_range = monthrange(current_year, current_month)
            how_many_month_days = month_range[1]

            # clears last day nums for month
            cell_list = sheet.range('A31:A33')
            for cell in cell_list:
                cell.value = ''

            sheet.update_cells(cell_list)

            # updates day nums for current month
            day_nums = 29
            row = 31
            while day_nums <= how_many_month_days :
                sheet.update_cell(row, 1, day_nums)
                row = row + 1
                day_nums = day_nums + 1
            print('Day numbers updated')

            # gets correct weekdays for month in list
            weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
            month_days = []
            start_total = 0
            end_total = 0
            cal = calendar.Calendar(firstweekday=0)

            for day in cal.itermonthdays(current_year, current_month) :
                # print(day)
                if day == 0 :
                    start_total = start_total + 1
                elif day == 1 :
                    break

            for day in cal.itermonthdays(current_year, current_month) :
                if day > 0 :
                    end_total = end_total + 1
            start_day = weekdays[start_total]

            # starts loop midweek on correct day
            day_num = 1
            for each in weekdays[start_total:] :
                month_days.append(each)
                day_num = day_num + 1

            # gets correct number of days for the month
            days_already = 7 - start_total
            while days_already < end_total :
                if days_already > end_total - 7 :
                    for each in weekdays[:end_total] :
                        if day_num > end_total : # stops weekday loop at correct end day
                            break
                        month_days.append(each)
                        day_num = day_num + 1
                else :
                    for each in weekdays :
                        month_days.append(each)
                        day_num = day_num + 1

                days_already = days_already + 7

            # update month/year cell
            sheet.update_acell('A1', month_year_for_email)
            print('Month/year updated')

            # update day cells
            row = 3
            month_day = 0
            if len(month_days) < 31 : # turn leftover days into blanks
                diff = 31 - len(month_days)
                while len(month_days) < 31 :
                    month_days.append('')
            # print('month days with extras', month_days)

            while row < 34 :
                sheet.update_cell(row, 2, month_days[month_day])
                row = row + 1
                month_day = month_day + 1

            print('Weekday cells updated')

            # clear all input cells
            cell_list = sheet.range('C3:AZ36') # can't figure out variable end column, for now it clears up to 50 item columns/items

            for cell in cell_list:
                cell.value = ''

            sheet.update_cells(cell_list)
            print('Cells cleared out')

            if sheet_count < len(stores) :
                print('Waiting 100 seconds..')
                time.sleep(100)

        return render(request, 'tacoapp/reset.html')

    else :
        print('post no')
        return render(request, 'tacoapp/reset.html')



# Old index and manager

# @login_required
# def index(request) :
#
#     today = str(datetime.date.today())
#     if request.method == 'POST' :
#         form = food_form(request.POST or None)
#
#         if form.is_valid() :
#             form.save()
#             all_items = Food.objects.all
#             messages.success(request, ('Item has been logged'))
#             return redirect('tacoapp:index')
#     else :
#         context = {
#             'today' : today,
#         }
#         return render(request, 'tacoapp/index.html', context)
#
# @login_required
# def manager(request) :
#
#     total = 0
#
#     if not request.user.username == 'sarah' :
#         messages.success(request, ('You sir do not have access to that page!'))
#         return redirect('tacoapp:index')
#
#     else :
#         today = str(datetime.date.today())
#         thirty = str(datetime.date.today() - datetime.timedelta(30))
#
#         all_items = Food.objects.filter(date__gte=thirty).order_by('date')
#
#         # should make these calculations later so not so many lists created
#         all_tacos_lists = [[i.potato for i in all_items], [i.bean for i in all_items],
#             [i.migas for i in all_items], [i.vegan for i in all_items]]
#
#         total = sum(map(sum, all_tacos_lists))
#
#
#         sun = Food.objects.filter(weekday='Sunday').filter(date__gte=thirty)
#         mon = Food.objects.filter(weekday='Monday').filter(date__gte=thirty)
#         tue = Food.objects.filter(weekday='Tuesday').filter(date__gte=thirty)
#         wed = Food.objects.filter(weekday='Wednesday').filter(date__gte=thirty)
#         thu = Food.objects.filter(weekday='Thursday').filter(date__gte=thirty)
#         fri = Food.objects.filter(weekday='Friday').filter(date__gte=thirty)
#         sat = Food.objects.filter(weekday='Saturday').filter(date__gte=thirty)
#
#
#         # Sunday
#         sun_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         sun_dic['pot'] = [i.potato for i in sun]
#         sun_dic['bean'] = [i.bean for i in sun]
#         sun_dic['migas'] = [i.migas for i in sun]
#         sun_dic['vegan'] = [i.vegan for i in sun]
#
#         l = len(sun_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             sun_dic['pot'] = sum(sun_dic['pot']) // l
#             sun_dic['bean'] = sum(sun_dic['bean']) // l
#             sun_dic['migas'] = sum(sun_dic['migas']) // l
#             sun_dic['vegan'] = sum(sun_dic['vegan']) // l
#             mes = ''
#
#
#         # Monday
#         mon_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         mon_dic['pot'] = [i.potato for i in mon]
#         mon_dic['bean'] = [i.potato for i in mon]
#         mon_dic['migas'] = [i.migas for i in mon]
#         mon_dic['vegan'] = [i.vegan for i in mon]
#
#         l = len(mon_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             mon_dic['pot'] = sum(mon_dic['pot']) // l
#             mon_dic['bean'] = sum(mon_dic['bean']) // l
#             mon_dic['migas'] = sum(mon_dic['migas']) // l
#             mon_dic['vegan'] = sum(mon_dic['vegan']) // l
#             mes = ''
#
#         # Tuesday
#         tue_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         tue_dic['pot'] = [i.potato for i in tue]
#         tue_dic['bean'] = [i.bean for i in tue]
#         tue_dic['migas'] = [i.migas for i in tue]
#         tue_dic['vegan'] = [i.vegan for i in tue]
#
#         l = len(tue_dic['pot'])
#         print(l, 'this is l baby 2/21!')
#         if l == 0 :
#             mes = ''
#         else :
#             tue_dic['pot'] = sum(tue_dic['pot']) // l
#             tue_dic['bean'] = sum(tue_dic['bean']) // l
#             tue_dic['migas'] = sum(tue_dic['migas']) // l
#             tue_dic['vegan'] = sum(tue_dic['vegan']) // l
#             mes = ''
#
#
#         # Wednesday
#         wed_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         wed_dic['pot'] = [i.potato for i in wed]
#         wed_dic['bean'] = [i.bean for i in wed]
#         wed_dic['migas'] = [i.migas for i in wed]
#         wed_dic['vegan'] = [i.vegan for i in wed]
#
#         l = len(wed_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             wed_dic['pot'] = sum(wed_dic['pot']) // l
#             wed_dic['bean'] = sum(wed_dic['bean']) // l
#             wed_dic['migas'] = sum(wed_dic['migas']) // l
#             wed_dic['vegan'] = sum(wed_dic['vegan']) // l
#             mes = ''
#
#
#         # Thursday
#         thu_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         thu_dic['pot'] = [i.potato for i in thu]
#         thu_dic['bean'] = [i.bean for i in thu]
#         thu_dic['migas'] = [i.migas for i in thu]
#         thu_dic['vegan'] = [i.vegan for i in thu]
#
#         l = len(thu_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             thu_dic['pot'] = sum(thu_dic['pot']) // l
#             thu_dic['bean'] = sum(thu_dic['bean']) // l
#             thu_dic['migas'] = sum(thu_dic['migas']) // l
#             thu_dic['vegan'] = sum(thu_dic['vegan']) // l
#             mes = ''
#
#
#         # Friday
#         fri_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         fri_dic['pot'] = [i.potato for i in fri]
#         fri_dic['bean'] = [i.bean for i in fri]
#         fri_dic['migas'] = [i.migas for i in fri]
#         fri_dic['vegan'] = [i.vegan for i in fri]
#
#         l = len(fri_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             fri_dic['pot'] = sum(fri_dic['pot']) // l
#             fri_dic['bean'] = sum(fri_dic['bean']) // l
#             fri_dic['migas'] = sum(fri_dic['migas']) // l
#             fri_dic['vegan'] = sum(fri_dic['vegan']) // l
#             mes = ''
#
#
#         # Saturday
#         sat_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}
#
#         sat_dic['pot'] = [i.potato for i in sat]
#         sat_dic['bean'] = [i.bean for i in sat]
#         sat_dic['migas'] = [i.migas for i in sat]
#         sat_dic['vegan'] = [i.vegan for i in sat]
#
#         l = len(sat_dic['pot'])
#         if l == 0 :
#             mes = ''
#         else :
#             sat_dic['pot'] = sum(sat_dic['pot']) // l
#             sat_dic['bean'] = sum(sat_dic['bean']) // l
#             sat_dic['migas'] = sum(sat_dic['migas']) // l
#             sat_dic['vegan'] = sum(sat_dic['vegan']) // l
#             mes = ''
#
#         context = {
#             'all_items' : all_items,
#             'total' : total,
#             'sun_dic' : sun_dic,
#             'mon_dic' : mon_dic,
#             'tue_dic' : tue_dic,
#             'wed_dic' : wed_dic,
#             'thu_dic' : thu_dic,
#             'fri_dic' : fri_dic,
#             'sat_dic' : sat_dic,
#             'mes' : mes,
#             'today' : today,
#             'thirty' : thirty,
#         }
#
#         return render(request, 'tacoapp/manager.html', context)
