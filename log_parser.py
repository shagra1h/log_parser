import sys
import os.path


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
        out_uniq_steamids = open('join_log_uniq_steamids.txt', 'w')
        out_uniq_ips = open('join_log_uniq_ips.txt', 'w')
        out_uniq_ips_and_steamids = open('join_log_uniq_ips_and_steamids.txt', 'w')
        steams = []
        ips = []
        input_file.readline()
        for line in input_file:
            line1, ip, steamid = line.split(" | ", maxsplit=2)
            steamid = steamid[9:]
            ip = ip[4:]
            if (steamid not in steams) and (ip not in ips):
                out_uniq_ips_and_steamids.write(line)
            if steamid not in steams:
                steams.append(steamid)
                out_uniq_steamids.write(line)
            if ip not in ips:
                ips.append(ip)
                out_uniq_ips.write(line)
        out_uniq_steamids.close()
        out_uniq_ips.close()
        out_uniq_ips_and_steamids.close()
        input_file.close()
    else:
        print("Ошибка! Введите корректный путь и попробуйте еще раз!")
        sys.exit(0)
