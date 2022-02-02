from lxml import etree
import requests
def trans(k1,k,k3):
    htmlreg = requests.get("http://www.ot76.ru/mob/getroutestr.php?vt="+k1+"&nmar=" + k)
    parser = etree.HTMLParser()
    doc = etree.HTML(htmlreg.text)
    xp = etree.XPath("//html/body/table/tr")
    i = 0
    avtob = []
    for r in xp(doc):
        if r.get("align") != "center":
            avtob.append([r[0].text, r[2].text])
            ost = requests.get("http://www.ot76.ru/mob/" + r[5][0].get('href'))
            doc1 = etree.HTML(ost.text)
            xp1 = etree.XPath("//html/body/table/tr")
            for r1 in xp1(doc1):
                if r1[0].get("colspan") == None:
                    if r1[0].text == avtob[len(avtob) - 1][1]:
                        continue
                    else:
                        avtob[len(avtob) - 1].append(r1[0].text)
                        avtob[len(avtob) - 1].append(r1[1].text)
                        break
    if len(avtob) == 0:
        print("В данный момент "+k3+" не ездит")
    else:
        for i in range(len(avtob)):
            if len(avtob[i]) < 4:
                print(k3, ":", k.upper() + "(" + avtob[i][0] + ") сейчас на остановке:",  avtob[i][1] + "; Информации о следующей остановке нет!")
            else:
                print(k3,":", k.upper() + "(" + avtob[i][0] + ") сейчас на остановке:",avtob[i][1] + "; Будет на остановке:", avtob[i][2], "- в", avtob[i][3])
print("1-Автобус")
print("2-Троллейбус")
print("3-Трамвай")
print("4-Маршрутное такси")
k1=input("Введите цифру нужного транспорта из предложеных:")
k3=""
if k1=="1":
    k3="автобуса"
elif k1=="2":
    k3="троллейбуса"
elif k1=="3":
    k3="трамвая"
elif k1=="4":
    k3="маршрутного такси"
else:
    exit("Нет такого транспортного средства!")

k=input("Введите номер "+k3+":").lower()
if k1=="1":
    k3="Автобус"
elif k1=="2":
    k3="Троллейбус"
elif k1=="3":
    k3="Трамвай"
elif k1=="4":
    k3="Маршрутное такси"
trans(k1,k,k3)
# k=input("Введите номер автобуса:").lower()
# htmlreg = requests.get("http://www.ot76.ru/mob/getroutestr.php?vt=1&nmar="+k)
# parser = etree.HTMLParser()
# doc = etree.HTML(htmlreg.text)
# xp = etree.XPath("//html/body/table/tr")
# i = 0
# avtob = []
# for r in xp(doc):
#     if r.get("align") != "center":
#         avtob.append([r[0].text, r[2].text])
#         ost = requests.get("http://www.ot76.ru/mob/" + r[5][0].get('href'))
#         doc1 = etree.HTML(ost.text)
#         xp1 = etree.XPath("//html/body/table/tr")
#         for r1 in xp1(doc1):
#             if r1[0].get("colspan") == None:
#                 if r1[0].text == avtob[len(avtob) - 1][1]:
#                     continue
#                 else:
#                     avtob[len(avtob) - 1].append(r1[0].text)
#                     avtob[len(avtob) - 1].append(r1[1].text)
#                     break
# print(avtob)