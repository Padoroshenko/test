from pytesseract import image_to_string
from PIL import Image
import enchant

i=70
strText=""
strPrev=""
strRes=""
while True:
    i = i + 1
    filename = 'frames/frame'+str(i)+'.png'
    image = Image.open(filename)
    if not Image:
        break
    strList = image_to_string(image, lang='rus').split(' ')
    strPrev=strRes
    strRes=""
    d = enchant.Dict("ru_RU")
    for j in range(1, len(strList)-1):
        if not d.check(strList[j]):
            if len(d.suggest(strList[j])):
                a = d.suggest(strList[j])[0]
            else:
                a = strList[j]
        else:
            a = strList[j]
        strRes = strRes+a+' '
    while len(strRes) != 0:
        space = strRes.find(" ",0,len(strRes))
        if space != -1:
            ind = strPrev.find(strRes[0:space-1],0,len(strRes))
            if ind != -1:
                print (strRes[ind:len(strRes)])
                break
            else:
                strRes = strRes[space+1:len(strPrev)]


