
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
"""
from docopt import docopt
from colorama import init,Fore
import requests
import stations
import json
import prettytable
init()
def main():

	arguments = docopt(__doc__, version="tickets.1.0")
	from_station = stations.getCodeByName(arguments.get('<from>'))
	to_station = stations.getCodeByName(arguments.get('<to>'))
	date = arguments.get('<date>')
	
	url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}"+\
	"&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT"
	url = url.format(date,from_station,to_station)
	r = requests.get(url,verify=False)
	requests.packages.urllib3.disable_warnings() 
	print(arguments,type(arguments))
	options = ''.join([key for key,value in arguments.items() if value == True])
	raw_trains = r.json()["data"]["result"]
	pt = prettytable.PrettyTable(["车次" ,"车站" ,"时间", "历时", "一等", "二等", "软卧", "硬卧", "硬座", "无座"])
	for raw_train in raw_trains:
		data_list = raw_train.split("|")
		train_no = data_list[3]
		train_no_first = train_no[0].lower()
		if not options or train_no_first in options:
			from_station_code = data_list[6]
			to_station_code = data_list[7]
			from_station_name = stations.getNameByCode(from_station_code)
			to_station_name = stations.getNameByCode(to_station_code)
			start_time = data_list[8]
			arrive_time = data_list[9]
			time_duration = data_list[10]
			first_class_seat = data_list[31] or "--"
			second_class_seat = data_list[30] or "--"
			soft_sleep = data_list[23] or "--"
			hard_sleep = data_list[28] or "--"
			hard_seat = data_list[29] or "--"
			no_seat = data_list[33] or "--"
			pt.add_row([
				train_no,
				"\n".join([Fore.GREEN + from_station_name + Fore.RESET , Fore.RED + to_station_name + Fore.RESET]),
				"\n".join([Fore.GREEN + start_time + Fore.RESET , Fore.RED +arrive_time + Fore.RESET]),
				time_duration,
				first_class_seat,
				second_class_seat,
				soft_sleep,
				hard_sleep,
				hard_seat,
				no_seat
			])
	print(pt)
	
if __name__ == "__main__":
	main()
	