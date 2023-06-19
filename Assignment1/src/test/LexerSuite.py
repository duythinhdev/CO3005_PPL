import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_LS101(self):
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 101))

    def test_LS102(self):
        self.assertTrue(TestLexer.test("12234", "12234,<EOF>", 102))

    def test_LS103(self):
        self.assertTrue(TestLexer.test("2131234_12342134_1", "2131234123421341,<EOF>", 103))

    def test_LS104(self):
        self.assertTrue(TestLexer.test("bruh bruh lmeo", "bruh,bruh,lmeo,<EOF>", 104))

    def test_LS105(self):
        self.assertTrue(TestLexer.test("asdfsdafasdfdsfasdf", "asdfsdafasdfdsfasdf,<EOF>", 105))

    def test_LS106(self):
        self.assertTrue(TestLexer.test("ab_sdfsd_sdfc_", "ab_sdfsd_sdfc_,<EOF>", 106))

    def test_LS107(self):
        self.assertTrue(TestLexer.test("test_LS 8 asdasdq123 DSF dsfsdq213ASF 2saf2kalutyIUOY","test_LS,8,asdasdq123,DSF,dsfsdq213ASF,2,saf2kalutyIUOY,<EOF>",107))

    def test_LS108(self):
        self.assertTrue(TestLexer.test("abc dasd 98asd  JKUG gjhg12 [sad] sadukjh]", "abc,dasd,98,asd,JKUG,gjhg12,[,sad,],sadukjh,],<EOF>", 108))

    def test_LS109(self):
        self.assertTrue(TestLexer.test("1+1=3", "1,+,1,=,3,<EOF>", 109))

    def test_LS110(self):
        self.assertTrue(TestLexer.test("asdf +f dshj+sa g-sadw21 hga*", "asdf,+,f,dshj,+,sa,g,-,sadw21,hga,*,<EOF>", 110))

    def test_LS111(self):
        self.assertTrue(TestLexer.test("i<3u", "i,<,3,u,<EOF>", 111))

    def test_LS112(self):
        self.assertTrue(TestLexer.test("ewrw<wq.QWE>eqw", "ewrw,<,wq,.,QWE,>,eqw,<EOF>", 112))

    def test_LS113(self):
        self.assertTrue(TestLexer.test("1_234_128765e+1632", "1234128765e+1632,<EOF>", 113))

    def test_LS114(self):
        self.assertTrue(TestLexer.test(":a:ghje34:,dsfeiewqo.", ":,a,:,ghje34,:,,,dsfeiewqo,.,<EOF>", 114))

    def test_LS115(self):
        self.assertTrue(TestLexer.test("{please give me the bezt score}", "{,please,give,me,the,bezt,score,},<EOF>", 115))

    def test_LS116(self):
        self.assertTrue(TestLexer.test(""" 1_3.987235e123 """, """13.987235e123,<EOF>""", 116))

    def test_LS117(self):
        self.assertTrue(TestLexer.test(""" "abc" """, """abc,<EOF>""", 117))

    def test_LS118(self):
        self.assertTrue(TestLexer.test(""" "abc\t" """, """abc\t,<EOF>""", 118))

    def test_LS119(self):
        input = """ "hjhasdfasdk\n" """
        expect = """Unclosed String: hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect,119))

    def test_LS120(self):
        self.assertTrue(TestLexer.test(""" "hi jghadsf qwyu3iter" """, """hi jghadsf qwyu3iter,<EOF>""", 120))

    def test_LS121(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 121))

    def test_LS122(self):
        self.assertTrue(TestLexer.test("+-*/", "+,-,*,/,<EOF>", 122))

    def test_LS123(self):
        self.assertTrue(TestLexer.test("auto break do else", "auto,break,do,else,<EOF>", 123))

    def test_LS124(self):
        self.assertTrue(TestLexer.test(""" abc \" def """, """abc,Unclosed String:  def """, 124))

    def test_LS125(self):
        self.assertTrue(TestLexer.test("abc + -", "abc,+,-,<EOF>", 125))

    def test_LS126(self):
        self.assertTrue(TestLexer.test("! == ^ & != && * % $ ... ","!,==,Error Token ^",126))

    def test_LS127(self):
         self.assertTrue(TestLexer.test(""" % erty == ! @ ksmdk ""","""%,erty,==,!,Error Token @""",127))
    
    def test_LS128(self):
         self.assertTrue(TestLexer.test("! == & != && * % $ ... ","!,==,Error Token &",128)) 
    
    def test_LS129(self):
        self.assertTrue(TestLexer.test(""" 1+1>=2+2 \"**dfshg324+\\^ def\" ""","""1,+,1,>=,2,+,2,Illegal Escape In String: **dfshg324+\^""",129))
    
    def test_LS130(self):
        self.assertTrue(TestLexer.test("""  \"\\!asdgqwetrew\" ""","""Illegal Escape In String: \!""",130))
    
    def test_LS131(self):
        self.assertTrue(TestLexer.test("!a!=%53245&&b||a123+*", "!,a,!=,%,53245,&&,b,||,a123,+,*,<EOF>", 131))

    def test_LS132(self):
        self.assertTrue(TestLexer.test("c==h==12341!=dfsg1234<>!", "c,==,h,==,12341,!=,dfsg1234,<,>,!,<EOF>", 132))

    def test_LS133(self):
        self.assertTrue(TestLexer.test("*%<=>&&<//<=", "*,%,<=,>,&&,<,<EOF>", 133))

    def test_LS134(self):
        self.assertTrue(TestLexer.test("/*lmeo lmeo give me the bezt score*/", "<EOF>", 134))

    def test_LS135(self):
        self.assertTrue(TestLexer.test("#dzFdadsf/*mai huu nghia he he */", "Error Token #", 135))

    def test_LS136(self):
        self.assertTrue(TestLexer.test("?hello my friend \n asda", "Error Token ?", 136))

    def test_LS137(self):
        self.assertTrue(TestLexer.test("/*go away my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 137))

    def test_LS138(self):
        self.assertTrue(TestLexer.test("asdfasd asdfas dfghwerty ", "asdfasd,asdfas,dfghwerty,<EOF>", 138))

    def test_LS139(self):
        self.assertTrue(TestLexer.test("im wanna go study abroad", "im,wanna,go,study,abroad,<EOF>", 139))

    def test_LS140(self):
        self.assertTrue(TestLexer.test("he he", "he,he,<EOF>", 140))

    def test_LS141(self):
        self.assertTrue(TestLexer.test(" 7E-10 ", "7E-10,<EOF>", 141))

    def test_LS142(self):
        self.assertTrue(TestLexer.test("1320.3e+9 0.332e5","1320.3e+9,0.332e5,<EOF>", 142))

    def test_LS143(self):
        self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>", 143))

    def test_LS144(self):
        self.assertTrue(TestLexer.test(" same format as", "same,format,as,<EOF>", 144))

    def test_LS145(self):
        self.assertTrue(TestLexer.test("ExpoWeanaSFSst part ", "ExpoWeanaSFSst,part,<EOF>", 145))

    def test_LS146(self):
        self.assertTrue(TestLexer.test(""" ",cxvbcvb\\12" """, """Illegal Escape In String: ,cxvbcvb\\1""", 146))

    def test_LS147(self):
        input = "F88 + nha - 40 > 12"
        expect = "F88,+,nha,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_LS148(self):
        input = "sdfgh<.>rtyui"
        expect = "sdfgh,<,.,>,rtyui,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_LS149(self):
        input = "[;]sdfghsdfgwaDSFGHEWdsfg\t"
        expect = "[,;,],sdfghsdfgwaDSFGHEWdsfg,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_LS150(self):
        input = ":12:dfgh:,dfgh 213"
        expect = ":,12,:,dfgh,:,,,dfgh,213,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_LS151(self):
        input = "function a inherit B {}"
        expect = "function,a,inherit,B,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_LS152(self):
        input = "123_123"
        expect = "123123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_LS153(self):
        input = "function ABC { }"
        expect = "function,ABC,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_LS154(self):
        input = "function ABC inherit { }"
        expect = "function,ABC,inherit,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_LS155(self):
        input = "function { }"
        expect = "function,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_LS156(self):
        input = "main : function void () {}"
        expect = "main,:,function,void,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_LS157(self):
        input = "3e.x() sdfg.dfg.dfsg().adsa"
        expect = "3,e,.,x,(,),sdfg,.,dfg,.,dfsg,(,),.,adsa,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_LS158(self):
        input = "getDepressed: function integer() {return dePressed;}"
        expect = "getDepressed,:,function,integer,(,),{,return,dePressed,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_LS159(self):
        input = """x: integer = 65;
                    fact: function integer (n:integer){
                        if ( n == 0) return 1;
                        else return n * fact(n-1);
                    }"""
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_LS160(self):
        input = """ main : function void ( ) {
                        delta:integer=fact(3);
                        inc(x,delta);
                        printInteger(x);
                    }
                    """
        expect = "main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_LS161(self):
        input = "a = true, b != false"
        expect = "a,=,true,,,b,!=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_LS162(self):
        input = """ \"dsfg\\e def\" """
        expect = """Illegal Escape In String: dsfg\\e"""
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_LS163(self):
        input = """ "abc\\n def" """
        expect = """abc\\n def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_LS164(self):
        input = """:3"""
        expect = ":,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_LS165(self):
        input = ":3?"
        expect = ":,3,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test_LS166(self):
        input = """a= "He said: " Im Super?Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,He said: ,Im,Super,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_LS167(self):
        input = """a= "No one said: " Hello " \n ";"""
        expect = """a,=,No one said: ,Hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_LS168(self):
        input = """aa = "Hello \n world !";"""
        expect = """aa,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_LS169(self):
        input = "{1,2,3}"
        expect = "{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_LS170(self):
        input = "{12.12, 14.12, 112e13}"
        expect = "{,12.12,,,14.12,,,112e13,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_LS171(self):
        input = "a[5] = {1, 1,  1, 41}"
        expect = "a,[,5,],=,{,1,,,1,,,1,,,41,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_LS172(self):
        input = "!=!%&&||"
        expect = "!=,!,%,&&,||,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_LS173(self):
        input = "int[5]array;"
        expect = "int,[,5,],array,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_LS174(self):
        input = "a, b: array [5] of int;"
        expect = "a,,,b,:,array,[,5,],of,int,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_LS175(self):
        input = "s=r*r*this.myPI;"
        expect = "s,=,r,*,r,*,this,.,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_LS176(self):
        input = "a[0] = s;"
        expect = "a,[,0,],=,s,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_LS177(self):
        input = """ " \\wqe " """
        expect = """Illegal Escape In String:  \w"""
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_LS178(self):
        input = """ " \\naaa\\t" """
        expect = """ \\naaa\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_LS179(self):
        input = "{<><><>}"
        expect = "{,<,>,<,>,<,>,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_LS180(self):
        input = """>">"""
        expect = """>,Unclosed String: >"""
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_LS181(self):
        input = "({False,})"
        expect = "(,{,False,,,},),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_LS182(self):
        input = "//{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_LS183(self):
        input = "/* abcxyz ??asdf`12~12{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_LS184(self):
        input = "// this is a line comment /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_LS185(self):
        input = "{/* this is a BLOCK comment */ 123, 123}"
        expect = "{,123,,,123,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_LS186(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """\\"aadadddldld\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_LS187(self):
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_LS188(self):
        input = """ {/*"*/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_LS189(self):
        input = """vbnm"-a)
                    " """
        expect = """vbnm,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_LS190(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_LS191(self):
        input = """ "\\n\\ " """
        expect = """Illegal Escape In String: \\n\\ """
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_LS192(self):
        input = """ "   vb     " """
        expect = """   vb     ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_LS193(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_LS194(self):
        input = "cba"
        expect = "cba,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_LS195(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_LS196(self):
        input = "int x;"
        expect = "int,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_LS197(self):
        input = """{                   1,             2     ,               3                }"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
    
    def test_LS198(self):
        input = """ a:array [5] of integer;
        /*
                    a = {1,2,3,4,5};"""
        expect = """a,:,array,[,5,],of,integer,;,/,*,a,=,{,1,,,2,,,3,,,4,,,5,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
    
    def test_LS199(self):
        self.assertTrue(TestLexer.test(""" "He asked me: Where is Mai Huu Nghia?" """, """He asked me: Where is Mai Huu Nghia?,<EOF>""", 199))    

    def test_LS200(self):
        self.assertTrue(TestLexer.test(""" "abvc\bcd" """, """abvc\bcd,<EOF>""", 200))    