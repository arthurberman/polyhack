import subprocess

def tess_img(receipt_name):
    subprocess.call('tesseract ' + receipt_name + ' output.txt' + ' -l eng', shell=True)

def parse_txt(file_name):
    fp = open(file_name, 'r')
    meal_list = [];
    for line in fp:
        if line.find('$') != -1 and line.find('%')==-1:
            raw_dat = line.rpartition('$')
            meal_name = raw_dat[0]
            price = raw_dat[2]
            meal_tup = (meal_name, float(price))
            meal_list.append(meal_tup)
    return meal_list

if __name__ == '__main__':
    tess_img('mel_receipt.jpg')
    meal_list = parse_txt('output.txt')
    print meal_list
