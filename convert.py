import pdftotext
f=open("Stu-1-74834121628.pdf", "rb")
pdf = pdftotext.PDF(f)
a=list(pdf)
o=open('langarudi_to_farsi.txt','w+')
for page in a:
    page = page.replace('\u202b','').replace('\u202a','').strip()
    #print(page)
    lines=page.split('\n')
    for line in lines:
        w=line.split(':')
        if len(w) >= 2:
            langarudi = w[0].strip()
            farsi = w[1].strip()
            #print(langarudi, ":",farsi)
            o.write(langarudi+':'+farsi+'\n')

o.close()
f.close()

