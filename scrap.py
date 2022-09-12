from lxml import html
import requests

path1 = '//*[@id="meteorologi-geofisika"]/div/div/div[2]/div[2]/div/div[2]/ul/li[2]'
path2 = '//*[@id="meteorologi-geofisika"]/div/div/div[2]/div[2]/div/div[2]/ul/li[3]'
path3 = '//*[@id="meteorologi-geofisika"]/div/div/div[2]/div[2]/div/div[2]/ul/li[4]'
path4 = '//*[@id="meteorologi-geofisika"]/div/div/div[2]/div[2]/div/div[2]/ul/li[5]'
path5 = '//*[@id="meteorologi-geofisika"]/div/div/div[2]/div[2]/div/div[2]/ul/li[6]'
path = '//*[@id="meteorologi-geofisika"]/div/div/div[1]/div[1]/div[2]'
url = ('https://www.bmkg.go.id/')
while True:
    pilih = input("input: ")
    if pilih == 'cuaca':
        response = requests.get(url)
        byte_data = response.content
        source_code = html.fromstring(byte_data)
        tree = source_code.xpath(path)
        tr = tree[0].text_content()
        print("perkiraan cuaca saat ini: \n",tr)
    elif pilih == 'info':
        response = requests.get(url)
        byte_data = response.content
        source_code = html.fromstring(byte_data)
        tree = source_code.xpath(path1) #Magnitudo
        rt = tree[0].text_content()
        rw = source_code.xpath(path2) #Kedalaman
        ry = rw[0].text_content()
        rx = source_code.xpath(path4) #lokasi
        rc = rx[0].text_content()
        rv = source_code.xpath(path5)
        rb = rv[0].text_content()
        print("info gempa terkini")
        print("Magnitudo: ",rt, "\nKedalaman: ", ry, "\nLokasi: ", rc, "\nPotensi: ", rb)