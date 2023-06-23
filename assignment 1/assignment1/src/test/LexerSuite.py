import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    def test_id(self):
        self.assertTrue(TestLexer.test("___________", "___________,<EOF>", 105))

    def test_id1(self):
        self.assertTrue(TestLexer.test("asdf____12312321______", "asdf____12312321______,<EOF>", 106))

    def test_id2(self):
        self.assertTrue(TestLexer.test(": =", ":,=,<EOF>", 107))

    def test_intlit(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 108))

    def test_intlit1(self):
        self.assertTrue(TestLexer.test("000000000", "000000000,<EOF>", 109))

    def test_intlit2(self):
        self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 110))

    def test_floatlit(self):
        self.assertTrue(TestLexer.test("102e3", "102e3,<EOF>", 111))

    def test_floatlit1(self):
        self.assertTrue(TestLexer.test("102e-3", "102e-3,<EOF>", 112))

    def test_floatlit3(self):
        self.assertTrue(TestLexer.test("0.33E-1", "0.33E-1,<EOF>", 113))

    def test_floatlit4(self):
        self.assertTrue(TestLexer.test(".12", ".,12,<EOF>", 114))

    def test_floatlit5(self):
        self.assertTrue(TestLexer.test("12e", "12,e,<EOF>", 115))

    def test_floatlit7(self):
        self.assertTrue(TestLexer.test("""12.3E10""", """12.3E10,<EOF>""", 122))

    def test_floatlit8(self):
        self.assertTrue(TestLexer.test("""00000012E+10""", """00000012E+10,<EOF>""", 123))

    def test_floatlit9(self):
        self.assertTrue(TestLexer.test("""00000012E-0""", """00000012E-0,<EOF>""", 124))

    def test_boollit(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 116))

    def test_boollit1(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 117))

    def test_comment(self):
        self.assertTrue(TestLexer.test("#aaaa", "<EOF>", 118))

    def test_comment1(self):
        self.assertTrue(TestLexer.test("#aaa##a", "<EOF>", 119))

    def test_comment2(self):
        self.assertTrue(TestLexer.test("#aaa/*a", "<EOF>", 120))

    def test_comment3(self):
        self.assertTrue(TestLexer.test("#aa/*a*/a", "<EOF>", 121))

    def test_comment4(self):
        self.assertTrue(TestLexer.test("/*This is ... so # ..*/", "<EOF>", 125))

    def test_comment5(self):
        self.assertTrue(TestLexer.test("/*This is ...*/ abc", "abc,<EOF>", 126))

    def test_comment6(self):
        input = """
            /* This is the
            many line
            comment
            */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_stringlit(self):
        self.assertTrue(TestLexer.test("\"abc\"", """"abc",<EOF>""", 128))

    def test_stringlit1(self):
        input = "\" \\naaa\\t\""
        expect = """" \\naaa\\t",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_130(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: \"", 130))

    def test_31(self):
        input = """"He asked me: \\"Where is John?\\"" """
        expect = """"He asked me: \\"Where is John?\\"",<EOF>"""
        self.assertTrue(
            TestLexer.test(input, expect, 131))

    def test_32(self):
        self.assertTrue(TestLexer.test("\"He asked me: ", "Unclosed String: \"He asked me: ", 132))

    def test_33(self):
        input = """class Triangle extends Shape {
                        float getArea(){
                            return this.length*this.width / 2;
                        }
                }"""
        expect = "class,Triangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_34(self):
        input = "+-*/>>=$"
        expect = "+,-,*,/,>,>=,Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("\"He", "Unclosed String: \"He", 135))

    def test_36(self):
        input = "static final int numOfShape = 0;"
        expect = "static,final,int,numOfShape,=,0,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_37(self):
        input = "abc?abc"
        expect = "abc,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_38(self):
        input = "boolean break class continue do else extends float if int new string then for return true false void nil this final static to downto"
        expect = "boolean,break,class,continue,do,else,extends,float,if,int,new,string,then,for,return,true,false,void,nil,this,final,static,to,downto,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_39(self):
        input = "A a new () {?}"
        expect = "A,a,new,(,),{,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_40(self):
        input = "ox128 + 1258.e8"
        expect = "ox128,+,1258.e8,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_41(self):
        input = "a := true, b = false"
        expect = "a,:=,true,,,b,=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_42(self):
        self.assertTrue(TestLexer.test(""" "This contains a tab\t" """, """"This contains a tab\t",<EOF>""", 142))

    def test_43(self):
        self.assertTrue(TestLexer.test("int[5] a", "int,[,5,],a,<EOF>", 143))

    def test_43(self):
        input = "\"abc\\e def\""
        expect = "Illegal Escape In String: \"abc\\e"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_44(self):
        input = "~!^^^^!"
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_45(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_46(self):
        input = """a= \"He said: \" Im Super'Man\" s \" testtt \" \"; __world = 5; imple = 8;"""
        expect = """a,=,"He said: ",Im,Super,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_47(self):
        input = """a= \"He said: \" Hello \" \n \";"""
        expect = """a,=,"He said: ",Hello,Unclosed String: " """
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_48(self):
        input = "{2.3, 4.2, 102e3}"
        expect = "{,2.3,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_49(self):
        input = "a[4] = {1, 2,  3, 4}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_50(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_51(self):
        input = "a[3 + x.foo(2)] := a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_52(self):
        input = "s:=r*r*this.myPI;"
        expect = "s,:=,r,*,r,*,this,.,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_53(self):
        input = "1/2"
        expect = "1,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_54(self):
        input = "\" \\h \""
        expect = "Illegal Escape In String: \" \h"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_55(self):
        self.assertTrue(TestLexer.test("final static int x = 5", "final,static,int,x,=,5,<EOF>", 155))

    def test_56(self):
        self.assertTrue(TestLexer.test("{1,2,3,4}", "{,1,,,2,,,3,,,4,},<EOF>", 156))

    def test_57(self):
        self.assertTrue(TestLexer.test("+ - * /", "+,-,*,/,<EOF>", 157))

    def test_58(self):
        self.assertTrue(TestLexer.test("new X()", "new,X,(,),<EOF>", 158))

    def test_59(self):
        self.assertTrue(TestLexer.test("== != >= <=", "==,!=,>=,<=,<EOF>", 159))

    def test_60(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.n()[3]", "x,.,b,[,2,],:=,x,.,n,(,),[,3,],<EOF>", 160))

    def test_61(self):
        self.assertTrue(TestLexer.test("this.method", "this,.,method,<EOF>", 161))

    def test_62(self):
        self.assertTrue(TestLexer.test("a[0] := s", "a,[,0,],:=,s,<EOF>", 162))

    def test_63(self):
        self.assertTrue(TestLexer.test("value := x.foo(5)", "value,:=,x,.,foo,(,5,),<EOF>", 163))

    def test_64(self):
        self.assertTrue(TestLexer.test("if x> 5 then x:=x+1;", "if,x,>,5,then,x,:=,x,+,1,;,<EOF>", 164))

    def test_65(self):
        self.assertTrue(TestLexer.test("if then else", "if,then,else,<EOF>", 165))

    def test_66(self):
        self.assertTrue(TestLexer.test("for x:=1 to 2 do writeln(x);", "for,x,:=,1,to,2,do,writeln,(,x,),;,<EOF>", 166))

    def test_67(self):
        self.assertTrue(TestLexer.test("\"        \"", """"        ",<EOF>""", 167))

    def test_68(self):
        self.assertTrue(
            TestLexer.test("io.writeIntLn(this.factorial(x));", "io,.,writeIntLn,(,this,.,factorial,(,x,),),;,<EOF>",
                           168))

    def test_69(self):
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 169))

    def test_70(self):
        self.assertTrue(TestLexer.test("break continue nil", "break,continue,nil,<EOF>", 170))

    def test_71(self):
        self.assertTrue(TestLexer.test("return x*5;", "return,x,*,5,;,<EOF>", 171))

    def test_72(self):
        self.assertTrue(TestLexer.test("a `= b", "a,Error Token `", 172))

    def test_73(self):
        self.assertTrue(TestLexer.test(""" "1"  abc "2" """, """"1",abc,"2",<EOF>""", 173))

    def test_74(self):
        self.assertTrue(TestLexer.test(""" "Ligal\\f" """, """"Ligal\\f",<EOF>""", 174))

    def test_75(self):
        self.assertTrue(TestLexer.test(""" "Ligal\\\ " """, """"Ligal\\\ ",<EOF>""", 175))

    def test_76(self):
        self.assertTrue(TestLexer.test(""" "jasonmamoa \\k """, """Illegal Escape In String: "jasonmamoa \\k""", 176))

    def test_77(self):
        self.assertTrue(TestLexer.test(""" "asdfa ' escaasdfasdpe """, """Unclosed String: "asdfa ' escaasdfasdpe """, 177))

    def test_78(self):
        self.assertTrue(TestLexer.test("a*3+afdsfb   - 1", "a,*,3,+,afdsfb,-,1,<EOF>", 178))

    def test_79(self):
        self.assertTrue(TestLexer.test("a3%dasfdb2b", "a3,%,dasfdb2b,<EOF>", 179))

    def test_80(self):
        self.assertTrue(TestLexer.test("a =f(2+b[3])", "a,=,f,(,2,+,b,[,3,],),<EOF>", 180))

    def test_81(self):
        self.assertTrue(TestLexer.test("string a := ~b", "string,a,:=,Error Token ~", 181))

    def test_82(self):
        self.assertTrue(
            TestLexer.test(""" "Illegal \\b escape \\l" """, """Illegal Escape In String: "Illegal \\b escape \\l""",
                           182))

    def test_83(self):
        self.assertTrue(TestLexer.test("5.2e-30", "5.2e-30,<EOF>", 183))

    def test_84(self):
        input = """
             void main(){
                 int x;
                 x:= io.readInt();
             }
        """
        expect = """void,main,(,),{,int,x,;,x,:=,io,.,readInt,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_85(self):
        self.assertTrue(TestLexer.test("io.readBool();", "io,.,readBool,(,),;,<EOF>", 185))

    def test_86(self):
        self.assertTrue(TestLexer.test("Shape.getNum();", "Shape,.,getNum,(,),;,<EOF>", 186))

    def test_87(self):
        inputs = """
            class Shape {
                float length, width;
                float getArea() {

                }
            }
        """
        expect = "class,Shape,{,float,length,,,width,;,float,getArea,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(inputs, expect, 187))

    def test_88(self):
        inputs = """
        Shape(float length, width) {
                this.length := length;
                this.width := width;
        }
        """
        expect = "Shape,(,float,length,,,width,),{,this,.,length,:=,length,;,this,.,width,:=,width,;,},<EOF>"
        self.assertTrue(TestLexer.test(inputs, expect, 188))

    def test_89(self):
        input = """
            class Rectangle extends Shape {
                float getArea() {
                    float return this.length*this.width;
                }
            }
        """
        expect = "class,Rectangle,extends,Shape,{,float,getArea,(,),{,float,return,this,.,length,*,this,.,width,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_90(self):
        input = """
            class Triangle extends Shape {
                float getArea() {
                    float return this.length*this.width/2;
                }
            }
        """
        expect = "class,Triangle,extends,Shape,{,float,getArea,(,),{,float,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_91(self):
        input = """
            class Ex2 {
                void main() {
                    Shape s;
                    s:= new Rectangle(3,4);
                }
            }
        """
        expect = "class,Ex2,{,void,main,(,),{,Shape,s,;,s,:=,new,Rectangle,(,3,,,4,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_92(self):
        self.assertTrue(TestLexer.test("bool x = true;", "bool,x,=,true,;,<EOF>", 192))

    def test_93(self):
        self.assertTrue(TestLexer.test("x || X", "x,||,X,<EOF>", 193))

    def test_94(self):
        self.assertTrue(TestLexer.test("a =f(2+b[3])", "a,=,f,(,2,+,b,[,3,],),<EOF>", 194))

    def test_95(self):
        input = """
            for x:= 5 downto 2 do 
            io.writeIntLn(x);
        """
        expect = "for,x,:=,5,downto,2,do,io,.,writeIntLn,(,x,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_96(self):
        self.assertTrue(TestLexer.test("a >= b <c", "a,>=,b,<,c,<EOF>", 196))

    def test_97(self):
        self.assertTrue(TestLexer.test("asfm@c34;", "asfm,Error Token @", 197))

    def test_98(self):
        self.assertTrue(TestLexer.test(""" "Illegal \\k" """, """Illegal Escape In String: "Illegal \\k""", 198))

    def test_99(self):
        self.assertTrue(TestLexer.test(""" "Ok I am fine ~" """, """"Ok I am fine ~",<EOF>""", 199))

    def test_100(self):
        self.assertTrue(TestLexer.test(""" "asdfasdfasdf\r " """, "Unclosed String: \"asdfasdfasdf", 200))


