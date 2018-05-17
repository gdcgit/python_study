# -*- coding: utf-8 -*-

import os
import zipfile
import time
# python 打包压缩文件


def begin_fun():
    g = os.walk("此处为要打包的文件所在的路径")
    stand_port_list = ["1", "4", "6", "9", "12", "15"]

    injection_date = ''
    port = ''
    sampletype = ''
    device_type = ''
    calibration_number = ''
    calibration_start_time = str(int(time.time()))
    calibration_end_time = str(int(time.time()))
    bottle_number = ""

    for path, dir, file in g:
        for f1 in file:
            bottle_number = "20180101"
            if f1.endswith(".TXT"):
                # print(path)
                temp_p_arr = path.split(os.sep)
                # print(temp_p_arr)
                calibration_number = temp_p_arr[len(temp_p_arr)-3]
                device_type = temp_p_arr[len(temp_p_arr)-2]
                fp = os.path.join(path, f1)
                # print(fp)
                with open(fp, 'r', encoding='utf-16') as f:
                    # i = 1
                    for line in f.readlines():
                        # print("i" + str(i) + "数据： " + line)
                        # i = i+1
                        if line.startswith("Injection Date"):
                            # print(line)
                            # print(line.split(" "))
                            param_list = line.split(" ")
                            injection_date = get_injection_date(param_list[4], param_list[5], param_list[6])
                            # print(datetime)
                        if line.startswith("Method"):
                            # print(line)
                            method_list = line.split("\\")
                            temp_m = method_list[len(method_list)-1]
                            tem_m_arr = temp_m.split("-")
                            port = tem_m_arr[len(tem_m_arr)-1].split(".")[0]
                            if int(port) < 10:
                                bottle_number = "0"+str(port)+str(bottle_number)
                            else:
                                bottle_number = str(bottle_number)
                            # print(port)
                            if port in stand_port_list:
                                sampletype = "W"
                            else:
                                sampletype = "A"
                # print(device_type)
                # print(injection_date)
                # print(port)
                # print(sampletype)
                # path 要压缩的文件夹路径
                file_news = "D:\\"+"GC_"+calibration_number+"_"+bottle_number+"_"+calibration_start_time+"_"+calibration_end_time+'_'+device_type+"_"+injection_date+"_"+port+"_"+sampletype+".zip"  # 压缩后文件夹的名字
                z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
                for dirpath, dirnames, filenames in os.walk(path):
                    fpath = dirpath.replace(path, '')  # 这一句很重要，不replace的话，就从根目录开始复制
                    fpath = fpath and fpath + os.sep or ''  # 这句可以让当前要压缩的目录中包含的文件夹也压缩，而不是把文件夹下的文件提取出来
                    for filename in filenames:
                        z.write(os.path.join(dirpath, filename), fpath+filename)
                        # print("压缩成功")
                z.close()


def get_injection_date(date, time, sign):
    s_date = ""
    s_time = ""
    if date:
        datelist = date.split("/")
        if int(datelist[0]) < 10:
            s_month = str(0)+datelist[0]
        else:
            s_month = datelist[0]
        s_date = datelist[2]+s_month+datelist[1]
    if time:
        timelist = time.split(":")
        s_hour = ""
        if sign == "AM":
            if int(timelist[0]) < 12:
                s_hour = timelist[0]
                if int(timelist[0]) < 10:
                    s_hour = "0"+timelist[0]
            else:
                s_hour = str(12+int(timelist[0]))
                if s_hour == "24":
                    s_hour = "00"
        elif sign == "PM":
            if int(timelist[0]) < 12:
                s_hour = str(12 + int(timelist[0]))
            else:
                s_hour = timelist[0]
        s_time = s_hour+timelist[1]+timelist[2]
    return s_date+s_time


if __name__ == '__main__':
    start = time.time()
    begin_fun()
    end = time.time()
    print("运行时间：" + str(end-start))
