# -*- coding:Utf-8 -*-
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class CodeCesar(object):
    # ASCII #alph=(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
    alph=("éèëàùï !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
    def code(self,clef,entree):
        sortie=""
        for car in entree:
            n=0
            while n < len(CodeCesar.alph) :
                if car==CodeCesar.alph[n]:
                    sortie=sortie+CodeCesar.alph[(n+clef)%len(CodeCesar.alph)]
                    break
                n=n+1
            if n==len(CodeCesar.alph):
                sortie=sortie+car
        return(sortie)
    def decode(self,clef,entree):
        sortie=""
        for car in entree:
            n=0
            while n < len(CodeCesar.alph) :
                if car==CodeCesar.alph[n]:
                    sortie=sortie+CodeCesar.alph[(n-clef)%len(CodeCesar.alph)]
                    break
                n=n+1
            if n==len(CodeCesar.alph):
                sortie=sortie+car
        return(sortie)
    def getClefMax(self):
        return(int(len(CodeCesar.alph)))


if __name__ == '__main__':
    machine=CodeCesar()
    message="marc:ésmerit@gmaïl*com"
    clef=12
    messagec=machine.code(clef,message)
    print("test : " ,messagec)
    messaged=machine.decode(clef,messagec)
    print("test : " ,messaged)
    clefMax=machine.getClefMax()
    print(clefMax)
