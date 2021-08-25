# Almanac
# By Clok Much
# Target json:
#       忌/宜: http://www.51wnl.com/YJData/2021.json
#       其他命理: http://www.51wnl.com/moreLumarData/2015.json
# Ref: icalics, By hxgz : https://github.com/hxgz/icalics
import datetime

import config
import xingzuoer
def sd():
    now_time = datetime.datetime.now()
    d = datetime.datetime.now().strftime('%Y%m%d')
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
    with open(file=d+"xinzuo.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + config.Default.name + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+d+"星座运势\n"
        file_object.write(start_string)
        body = xingzuoer.tomorrow()
        body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                       "END:VEVENT\n")
        for item in body:
            body0 = body_string[0]
            body1 =   item[0] + 'almanac_in_' + config.Default.year + "\n"
            body2 = "DTSTART;VALUE=DATE:" + item[0] + "\nDTEND;VALUE=DATE:" + item[0] + "\n"
            beizhu = "DESCRIPTION:" + item[2] +"\n"
            body3 = "SUMMARY:" + item[1] + "\n"
            body4 = body_string[1]
            full_body = body0 + body1 + body2 +beizhu+ body3 + body4
            file_object.write(full_body)
        end_string = "END:VCALENDAR"
        file_object.write(end_string)




#
if __name__ == '__main__':
    a=sd()
    print(a)