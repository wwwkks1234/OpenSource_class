def findMax(a,b,c,):
	if a>b:
	   big=a
	else:
	   big=b
	   if c>big:
               big=c
               return biggest
            a= int(input("첫번째숫자입력:"))
            b= int(input("두번째숫자입력:"))
            c= int(input("세번째숫자입력:"))
            biggest=findMax(a,b,c)
            print(a,b,c,"중가장큰수는",biggest,"입니다.")
