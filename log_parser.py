import sys
import os.path
import os
from datetime import datetime


def write_to_file(uniqIps, uniqSteamids, uniqIpsAndSteamids):
    output_filename = 'results_' + datetime.now().strftime("%d_%m_%Y") + '.txt'
    output_file = open(output_filename, 'w')
    output_file.write(" Уникальных steamid : " + str(uniqSteamids) + '\n')
    output_file.write(" Уникальных ip : " + str(uniqIps) + '\n')
    output_file.write(" Уникальных комбинаций steamid + ip : " + str(uniqIpsAndSteamids))
    output_file.close()
    print("Успешно! результаты в файле", output_filename)


if __name__ == '__main__':
    input_file = open('join_log.log', 'r')
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
    write_to_file(uniq_ips, uniq_steamids, uniq_ips_and_steamids)
