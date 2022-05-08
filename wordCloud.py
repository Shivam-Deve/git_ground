# import wordcloud
# frequencies={"Apple":10,"Nokia":3,"Samsung":5,"Moto":7,"Realme":8,"Redmi":4}
# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies(frequencies)
# cloud.to_file("myfile.jpg")
f=open("read.txt","r")
def countFreq(lsts):
    dct={}
    for lst in lsts:
        for elm in lst:
            if elm in dct:
                dct[elm]+=1
            else:
                dct[elm]=1
    return dct
def cleanTxt(f):
    ls=["is","the","for","a","this","will","into","have","in","it","of","all","as"]
    result=[]
    for line in f:
        words=line.split()
        lst=[]
        for word in words:
            new=""
            for char in word:
                if char.isalpha():
                    new+=char
            if new.lower() not in ls:
                lst.append(new)
        result.append(lst)
    return result
# result is list of lists
result=cleanTxt(f)
fresult=countFreq(result)
print(fresult)
