# 打印2033年 12月整个月的日历
#已知 1800年1月1日是星期三
def get_a_month_calender(input_month, input_year):
	# 想打印给定月份的日历，我们需要知道这个月份是多少天
	total_days = 3
	month_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	for year in range(1800, input_year):
		if is_leap_year(year):
			total_days += 366
		else:
			total_days += 365
	# 下面计算当前年份中每个月的天数
	for month in range(1, input_month):
		total_days += get_days_of_month(month, input_year)
	# 下面的结果是几，说明当前月份的1号就是星期几
	first_day = count = total_days % 7
	print("{: ^30}{: ^30}".format(month_english[input_month - 1], input_year))
	print("{:-^65}".format("-"))
	print("{: ^9}{: ^9}{: ^9}{: ^9}{: ^9}{: ^9}{: ^9}".format("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
	for days in range(1, get_days_of_month(input_month, input_year) + 1):
		if days == 1:
			if first_day == 0:
				print("{: ^9}".format(days), end="")
			elif first_day >= 1 and first_day <= 5:
				for d in range(1, first_day + 1):
					print("{: ^9}".format(" "), end="")
				print("{: ^9}".format(days), end="")
			else:
				for d in range(1, first_day + 1):
					print("{: ^9}".format(" "), end="")
				print("{: ^9}".format(days))
			count += 1

		else:
			if count % 7 == 0:
				print("{: ^9}".format(days), )
			else:
				print("{: ^9}".format(days), end="")
		count += 1
	print()

# 获取给定的月份有多少天
def get_days_of_month(input_month, input_year):
	leap_year = is_leap_year(input_year)
	if input_month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	elif input_month in (4, 6, 9, 11):
		return 30
	elif is_leap_year(input_year):
		return 29
	else:
		return 28

# 获取给定的年份是不是闰年
def is_leap_year(input_year):
	if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
		return True
	else:
		return False

get_a_month_calender(9,2018)