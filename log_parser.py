import sys
import os.path
import os
import datetime


def check_path(filepath):
    if os.path.exists(filepath):
        return 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:
        print("Необходимо указать путь к файлу!")
        sys.exit(0)
    if check_path(path_to_file):
        input_file = open(path_to_file, 'r')
        uniq_steamids = 0
        uniq_ips = 0
        uniq_ips_and_steamids = 0
        steams = []
        ips = []
        input_file.readline()
        for line in input_file:
            line1, ip, steamid = line.split(" | ", maxsplit=2)
            steamid = steamid[9:]
            ip = ip[4:]
            if (steamid not in steams) and (ip not in ips):
                uniq_ips_and_steamids += 1
            if steamid not in steams:
                steams.append(steamid)
                uniq_steamids += 1
            if ip not in ips:
                ips.append(ip)
                uniq_ips += 1
        input_file.close()
        output_filename = 'results_' + datetime.datetime.now().strftime("%d_%m_%Y") + '.txt'
        output_file = open(output_filename, 'w')
        output_file.write(" Уникальных steamid : " + str(uniq_steamids) + '\n')
        output_file.write(" Уникальных ip : " + str(uniq_ips) + '\n')
        output_file.write(" Уникальных комбинаций steamid + ip : " + str(uniq_ips_and_steamids))
        output_file.close()
        print("Успешно! результаты в файле", output_filename)
    else:
        print("Ошибка! Введите корректный путь и попробуйте еще раз!")
        sys.exit(0)
