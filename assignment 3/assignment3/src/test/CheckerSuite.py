# import unittest
# from TestUtils import TestChecker
# from AST import *

# class CheckerSuite(unittest.TestCase):
#     def test00(self):
#         """
#         successful test series
#         """
#         input_text = """class Test {
#             int a = "addmaximum",b = 0001.18;
#             static Test2 abc;
#             Test2 abcc(Test2 a,a){
#                 Test2 an;
#                 for i := 1 to 100 do 
#                 {
#                     io.writeIntLn(i);
#                     Intarray[i] := i + 1;
#                 }
#             }
#             void aneue,onichann= 1213;
#         }
#         """
#         expect = "Redeclared Parameter: a"
#         # Neu muon check class truoc check param thi sao
#         self.assertTrue(TestChecker.test(input_text, expect, 400)) 

#     def test01(self):
#         """
#         successful test series
#         """
#         input_text = """class Test {
#             int a = "addmaximum",b = 0001.18;
#             static Test2 abc;
#         }
#         class Test {
#             int a = "addmaximum",b = 0001.18;
#             Test abc;
#             void aneue,onichann= 1213;
#         }"""
#         expect = "Redeclared Class: Test"
#         # Neu muon check class truoc check param thi sao
#         self.assertTrue(TestChecker.test(input_text, expect, 401)) 

#     def test02(self):
#         """
#         successful test series
#         """
#         input_text = """class A {
#             final int a = true;
#         }
#         """
#         expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BooleanLit(True))"
#         # Neu muon check class truoc check param thi sao
#         self.assertTrue(TestChecker.test(input_text, expect, 402)) 

#     def test03(self):
#         """
#         successful test series
#         """
#         input_text = """class Test {
#             int a = "addmaximum",b = 0001.18;
#             static Test2 abc;
#             static Test2 abcc(Test2 a){
#                 Test2 an;
#                 for i := 1 to 100 do 
#                 {
#                     Test3 an;
#                     io.writeIntLn(i);
#                     Intarray[i] := i + 1;
#                 }
#             }
#             void aneue,onichann= 1213;
#         }
#         class Test2 {
#             int a = "addmaximum",b = 0001.18;
#             Test abc;
#             void aneue,onichann= 1213;
#         }"""
#         expect = "Undeclared Class: Test3"
#         # Neu muon check class truoc check param thi sao
#         self.assertTrue(TestChecker.test(input_text, expect, 403)) 
    
#     def test04(self):
#         """
#         successful test series
#         """
#         input_text = """
#         class Shape {
#             float length,width;
#             float getArea() {

#             }
#             Shape(float length,width){
#                 this.length := length;
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Shape {
#             float getArea(){
#                 return this.length*this.width;
#             }
#         }
#         class Triangle extends Shape {
#             float getArea(){
#                 return this.length*this.width / 2;
#             }
#         }
        
#         """
#         expect = """['Valid']"""
#         # Neu muon check class truoc check param thi sao
#         self.assertTrue(TestChecker.test(input_text, expect, 404)) 

#     def test05(self):
#         input = """
#             class Ex {
#                 final int val = 10 \\ true;
#                 final int a = 1 + 2 * 4;
#                 int b = 10 + 20 * 30;
#             }
#             """
#         expect = 'Type Mismatch In Expression: BinaryOp(\,IntLit(10),BooleanLit(True))'
#         self.assertTrue(TestChecker.test(input, str(expect), 405))


#     def test06(self):
#         input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),FieldAccess(Id("Ex"),Id("a"))))])])
#         expect = 'Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))'
#         self.assertTrue(TestChecker.test(input, str(expect), 406))

#     def test07(self):
#         input = """
#         class A {
#             int a;
#             void main() {
#             int b = A.a;
#             }
#         }
#         """
#         expect = 'Illegal Member Access: FieldAccess(Id(A),Id(a))'
#         self.assertTrue(TestChecker.test(input, str(expect), 407))
#     def test08(self):
#         input = """
#         class Ex extends Ey{
#         int a = 10 + 20;
#         Ey classY = new Ey();
#         static int c = 100;
#         void foo () {
#             Ey classEY = new Ey();
#             int value = this.classY.classC.a;
#         }
#         }
#         class Ey {
#             float a = 10.0;
#             Ec classC = new Ec();
#             static int b = 10;
#             static void foo () {

#             }
#         }
#         class Ec {
#             float a = 10.0;
#         }
#         """
#         expect = """['Valid']"""
#         self.assertTrue(TestChecker.test(input, str(expect), 408))

#     def test09(self):
#         input = """
#         class Ex extends Ey{
#         static Ey classY = new Ey();
#         void foo () {
#             int value = Ex.classC.a;
#         }
#         }
#         class Ey {
#             static Ec classC = new Ec();
#         }
#         class Ec {
#             static float a = 10.0;
#         }
#         """
#         expect = 'Illegal Member Access: FieldAccess(FieldAccess(Id(Ex),Id(classC)),Id(a))'
#         self.assertTrue(TestChecker.test(input, str(expect), 409))

#     def test10(self):
#         input = """
#         class A {
#         int a = 90;
#         void foo () {
#             int b = 100;
#             if (this.a > b) then {
#                 int c;
#                 if (this.a > c) then {
#                     int d = c + b;
#                 }
#             }
#             if (c > b) then {
                
#             }
#         }
#     }
#         """
#         expect = 'Undeclared Identifier: c'
#         self.assertTrue(TestChecker.test(input, str(expect), 410))

#     def test11(self):
#         input = """
#         class A {
#             final int value = 10;
#         }
#         class B extends A {
#             void foo(int a) {
#                 int b = 10;
#                 A classA = new A();
#                 if (b > this.value) then {
#                     int b;
#                     {
#                         boolean b;
#                         {
#                             if b then {
#                                 float b = classA.value;
#                             }
#                         }
#                         {
#                             boolean d = b;
#                             final int a = d + 1;
#                         }
#                     }
#                 }
#             }
#         }
#         """
#         expect = 'Illegal Constant Expression: BinaryOp(+,Id(d),IntLit(1))'
#         self.assertTrue(TestChecker.test(input, str(expect), 411))

#     def test12(self):
#         input = """
#         class A {
#             final float value = 10;
#         }
#         class B extends A {
#             A classA_global = new A();
#             void foo(int a) {
#                 int b = 1;
#                 A classA = new A();
#                 if (b > this.value) then {
#                     int i = 0;
#                     for i := 1 to this.value do {
#                         int c = this.classA_global;
#                     }
#                 }
#             }
#         }
#         """
#         expect = 'Type Mismatch In Statement: For(Id(i),IntLit(1),FieldAccess(Self(),Id(value)),True,Block([VarDecl(Id(c),IntType,FieldAccess(Self(),Id(classA_global)))],[])])'
#         self.assertTrue(TestChecker.test(input, str(expect), 412))
    
#     def test13(self):
#         input = """
#         class A {
#         final int value = 10;
#         }
#         class B extends A {
#             A classA_global = new A();
#             void foo(int a) {
#                 int b = 1;
#                 A classA = new A();
#                 if (b > this.value) then {
#                     int i = 0;
#                     for i := 1.0 to this.value do {
#                         int c = this.classA_global;
#                     }
#                 }
#             }
#         }
#         """
#         expect = 'Type Mismatch In Statement: For(Id(i),FloatLit(1.0),FieldAccess(Self(),Id(value)),True,Block([VarDecl(Id(c),IntType,FieldAccess(Self(),Id(classA_global)))],[])])'
#         self.assertTrue(TestChecker.test(input, str(expect), 413))

#     def test14(self):
#         input = """
#         class A {
#         final float value = 10;
#         }
#         class B extends A {
#             A classA_global = new A();
#             void foo(int a) {
#                 int b = 1;
#                 A classA = new A();
#                 for b := 0 to 10 do {
#                     {
#                         break;
#                     }
#                 }
#                 continue;
#             }
#         }
#         """
#         expect = 'Continue Not In Loop'
#         self.assertTrue(TestChecker.test(input, str(expect), 414))


#     def test15(self):
#         input = """
#         class A {
#             int a;
#             void main() {
#             final int b = this.a;
#             }
#         }
#         """
#         expect = 'Illegal Constant Expression: FieldAccess(Self(),Id(a))'
#         self.assertTrue(TestChecker.test(input, str(expect), 415))

    
#     def test16(self):
#         input = """
#         class A {
#             void main() {
#             final int b = 10.0;
#             }
#         }
#         """
#         expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,FloatLit(10.0))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 416))

#     def test17(self):
#         input = """
#         class A {
#             void main() {
#             final int b = 10;
#             b := 5;
#             }
#         }
#         """
#         expect = """Cannot Assign To Constant: AssignStmt(Id(b),IntLit(5))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 417))

#     def test18(self):
#         input = """
#         class A {
#             void main() {
#             final int[6] b = {1,2,3,4,5};
#             b := 5;
#             }
#         }
#         """
#         expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(b),ArrayType(6,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])"""
#         self.assertTrue(TestChecker.test(input, str(expect), 418))

#     def test19(self):
#         input = """
#         class A {
#             void main() {
#             final int[5] b = {1,2,3,4,5};
#             b := 5;
#             }
#         }
#         """
#         expect = """Cannot Assign To Constant: AssignStmt(Id(b),IntLit(5))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 419))

#     def test20(self):
#         input = """
#         class A {
#             final int[5] b = {1,2,3,4,5};
#             void main() {
#             this.b := 5;
#             }
#         }
#         """
#         expect = """Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(b)),IntLit(5))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 420))
    
#     def test21(self):
#         input = """
#         class A {
#             float main() {
#                 int a = 5;
#                 {
#                     {
#                         for a:=0 to 1 do {
#                             for a:=0 to 1 do {
#                                 for a := 0 to 1 do {
#                                     float a;
#                                 }
#                                 if true then {
#                                     {
#                                         {
#                                             float a = 5;
#                                         }
#                                         return a;
#                                     }
#                                 }
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#         """
#         expect = """['Valid']"""
#         self.assertTrue(TestChecker.test(input, str(expect), 421))

    
#     def test22(self):
#         input = """
#         class A {
#             final int[5] b = {1,2,3,4,5};
#             void main() {
#                 int a;
#                 final int b = 1+ a; 
#             }
#         }
#         """
#         expect = """Illegal Constant Expression: BinaryOp(+,IntLit(1),Id(a))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 422))

    
#     def test23(self):
#         input = """
#         class A {
#             int foo2;
#             float[5] foo (int _var1) {
#                 final float[5] a = {1.0,2.0,3.0,4.0,5.0};
#                 return a;
#             }
#             int foo1 () {
                
#             }
#             void main () {
#                 int a;
#                 final float c = this.foo(1)[0];
#             }
#         }
#         """
#         expect = """Illegal Constant Expression: ArrayCell(CallExpr(Self(),Id(foo),[IntLit(1)]),IntLit(0))"""
#         self.assertTrue(TestChecker.test(input, str(expect), 423))


import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_401(self):
        input = """
        class main{
            int foo(){
                final main[4] arr = {nil, this, this, nil};
            }
        }

        class main{
            static int foo(int a; main b){

            }
        }
        """
        expect = "Redeclared Class: main"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_402(self):
        input = """
        class main extends main1{
            int main2(int a, b; float c){
                int d;
                final string s = "abc";
            }

            int a = 1;
            static string b = "abc";
        }

        class main1{
            void foo(){
                final float c;
            }

            final static float c, c;
            boolean flag = true;
        }
        """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_403(self):
        input = """
        class main extends main1{
            int main2(int a, b; main1 c){
                d := 3;
            }
            float f = 1.5;
            static string b = "abc";
        }

        class main1{

        }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        input = """
        class main extends main1{
            int main2(int a, b; main1 c; int[5] arr){
                int[5] ar;
                a := 3;
                main1.x := 1 % 2;
                c := new main1();
                c.y := 3;
                arr := {1, true};
            }

            X(){

            }
            float f = 1.5;
            static string b = "abc";
        }

        class main1{
            static int x;
            int y;
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_405(self):
        """Simple program: int main() {} """
        input = """
        class main{
            static int x = 1;
        }

        class main2 extends main{
            int main(){
                return main.x;
            }

            int foo(){
                return main;
            }
        }
        """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        """Simple program: int main() {} """
        input = """
        class main{
            int main() {
                final int i = 2;
                for i := 0 to 10 do
                    return 0;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(i),IntLit(0))"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_406(self):
        """Simple program: int main() {} """
        input = """
        class main{
            int main() {
                int i = 2;
                for i := 0 to 10 do
                    return 0;
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        """Simple program: int main() {} """
        input = """
        class main{
            int main() {
                final int x = 2;
                int i;
                for i := 0 to 5 do{
                    final int x = x;
                }
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,407))
    

    def test_407(self):
        """Simple program: int main() {} """
        input = """
        class main{
            int i;
            int main() {
                for i := 0 to 5 do{
                    final int x = x;
                }
                continue;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_408(self):
        """Simple program: int main() {} """
        input = """
        class main extends ABC{
            int main() {
                final int x = 2;
                int i;
                for i := 0 to 5 do{
                    final int x = x;
                    {
                        {
                            break;
                        }
                    }
                    {
                        continue;
                    }
                    break;
                }
            }
        }

        class ABc{

        }
        """
        expect = "Undeclared Class: ABC"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_408(self):
        """Simple program: int main() {} """
        input = """
        class main extends ABC{
            int main() {
                final int x = 2;
                int i;
                for i := 0 to 5 do{
                    final int x = x;
                    {
                        {
                            break;
                        }
                    }
                    {
                        continue;
                    }
                    break;
                }
            }
        }
        """
        expect = "Undeclared Class: ABC"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_409(self):
        """Simple program: int main() {} """
        input = """
        class main extends main{
            main() {
                
            }

            int foo(){
                main x = new main(1);
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(main),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        '''Redeclared Class'''
        input = """
        class main{
            int foo(){
                return 1;
            }
        }

        class io{
            int foo(io a, b){

            }
        }
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        '''Redeclared Att'''
        input = """
        class main{
            static int a;
            int foo(){
                int i;
                for i := 0 to 5 do
                    io.writeInt(1 + this.a);
            }
        }

        class D{
            static int a;
            int foo(io a, b){

            }
            final float a = 1;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_412(self):
        '''Redeclared Att'''
        input = """
        class ABC extends DEF{
            final int a = 1;
            final int b = DEF.abc.a;

            ABC foo(){
                ABC obj;
                return obj;
            }
        }

        class DEF{
            final static ABC abc = nil;
            int abc = 1;
            int main(){
                return 0;
            }
        }
        """
        expect = "Redeclared Attribute: abc"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        '''Redeclared Variable'''
        input = """
        class ABC extends DEF{
            final int a = 1;
            final int b = this.abc.a;
        }

        class DEF{
            int main(){
                if true then {
                    {
                        final int x = 0;
                        int x;
                        return x;
                    }
                }
            }
            final ABC abc = nil;
        }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_414(self):
        '''Redeclared Constant'''
        input = """
        class ABC extends DEF{
            int[5] arr;
            void foo(string str){
                io.writeStr(str);
            }

            void main(){
                string str;
                this.foo(str);
            }
        }

        class DEF{
            int main(){
                if true then {
                    void flag;
                    final boolean flag = true;
                    {
                        float f = true;
                        int y;
                        return x + y;
                    }
                }
            }
            final ABC abc = nil;
        }
        """
        expect = "Redeclared Constant: flag"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        '''Redeclared Parameter'''
        input = """
        class ABC extends DEF{
            final int[5] arr = {1, 2, 5, 3, 2};
            boolean foo(string str){
                boolean flag = true && false || true;
                io.writeStrLn(str);
                return flag;
            }

            void main(){
                string str;
                this.foo(str);
            }
        }

        class DEF extends io{
            int main(){
                
            }
            main(int a, b; float c, a, d){
                io.writeBool(true);
            }
            final ABC abc = nil;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_416(self):
        '''Undeclared Identifier'''
        input = """
        class ABC extends DEF{
            static int[5] arr = {1, 2, 5, 3, 2};
            int[5] goo(){
                int i;
                for i := 4 downto 0 do {
                    ABC.arr[i] := i;
                }
            }
        }

        class DEF extends io{
            int main(){
                
            }
            main(ABC abc; ABC def){
                int i;
                DEF.writeIntLn(i);
                for i := n downto 0 do {
                    int[5] arr = abc.arr;
                }
            }
            final ABC abc = nil;
        }
        """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_417(self):
        '''Undeclared Method'''
        input = """
        class DEF extends ABC{
            int n = 5.;
            void main(){
                
            }
            goo(string str1, str2){
                int i;
                DEF.writeIntLn(i);
                {
                    
                    for i := this.n downto 0 do {
                        string str1 = str1 ^ str2;
                    }
                }
            }
            final ABC abc = nil;
        }

        class ABC extends io{
            final DEF def = nil;
            int foo(){
                this.def.main();
                this.def.goo("str", "");
            }
        }
        """
        expect = "Undeclared Method: goo"
        self.assertTrue(TestChecker.test(input,expect,417))
    

    def test_418(self):
        '''Undeclared Identifier'''
        input = """
        class DEF extends ABC{
            int n = 5.;
            int main(){
                return this.n;
            }
            goo(string str1, str2){
                int i;
                DEF.writeFloat(i*1/this.n);
                {
                    if this.n >= 0 then{
                        this.n := i;
                    }
                }
            }
        }

        class ABC extends io{
            final DEF def = nil;
            int foo(){
                float f = this.def.main() - 1e-3;
                {
                    int i;
                }
                {
                    ABC.writeFloatLn(f);
                    if i > 5 then{
                        /*pass*/
                    }
                }
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_419(self):
        '''Undeclared Identifier'''
        input = """
        class DEF{
            static int DEF = 1 % 2 \\ 3;
            void main(){
                int fofo;
                final float pi = 3.14;
                if pi >= pi then {

                } 
                else
                {

                }
            }
        }

        class ABC extends io{
            final DEF def = nil;
            foo(){
                float f = this.def.main() - DEF.DEF;
                {
                    int i;
                }
                {
                    ABC.writeFloatLn(f);
                    if i > 5 then{
                        /*pass*/
                    }
                }
            }
            foo(){
                string str = "this is a string :V";
            }
        }
        """
        expect = "Redeclared Method: <init>"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_420(self):
        '''Undeclared Attribute: instance att visible only its class or subclass'''
        input = """
        class DEF extends ABC{
            static int DEF = 1 % 2 \\ 3;
            void main(){
                int fofo;
                final float pi = 3.14;
                if pi - 1 >= pi + 1 then {

                } 
            }
            string field;
        }
        class ABC extends DEF{
            final DEF def = nil;
            string foo(){
                string str = "Ho xuan Huong" ^ "Vo Thi Sau" ^ str ^ this.def.field;
                return str;
            }
            string main() {
                string res = this.foo();
                return res ^ "hello";
            }
        }

        class MNP{
            string[1] goo(){
                DEF def;
                string str = def.main() ^ def.field;    /*  <===== sai day moi dung!*/
            }
        }
        """
        expect = "Undeclared Attribute: field"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_421(self):
        '''Undeclared Identifier'''
        input = """
        class DEF{
            static string str = "Ba Huyen Thanh Quan";
            boolean flag = false;
            final DEF abc = nil;
            static DEF blu;
        }
        class ABC extends DEF{
            final DEF def = this.abc;
            string foo(){
                string str = "Ho xuan Huong" ^ "Vo Thi Sau" ^ str ^ DEF.str;
                return str;
            }
            string main() {
                if this.flag then{
                    string res = this.foo();
                    return res ^ "hello";
                }
                else{
                    this.flag := !this.flag;
                    return this.main();
                }
            }
        }

        class IO extends ABC{
            /*pass*/
        }

        class MNP extends IO{
            boolean goo(){
                DEF abc = this.abc;
                return abc.flag == true;
            }
        }

        class BLABLA{
            boolean main(){
                DEF abc;
                return abc.flag != false;
            }
        }
        """
        expect = "Undeclared Attribute: flag"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_422(self):
        '''Undeclared Identifier'''
        input = """
        class ABC extends DEF{
            int abc;
            int main(){
                DEF def;
                MNP mnp;
                int res = def.def + mnp.mnp;
                return res;
            }
        }

        class DEF extends MNP{
            int def;
            int main(){
                ABC abc;
                MNP mnp;
                int res = abc.abc + mnp.mnp;
                return res;
            }
        }

        class MNP extends ABC{
            int mnp;
            int main(){
                DEF def;
                ABC abc;
                int res = def.def + abc.abc;
                return res;
            }
        }

        class Bla{
            ABC abc;
            final DEF def = nil;
            static MNP mnp;
            int main(){
                int res = this.abc.abc + this.def.def + Bla.mnp.mnp;
            }
        }
        """
        expect = "Undeclared Attribute: abc"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_422(self):
        '''Undeclared Identifier'''
        input = """
        class ABC extends DEF{
            int abc;
            int main(){
                DEF def;
                MNP mnp;
                int res = def.def + mnp.mnp;
                return res;
            }
        }

        class DEF{

        }
        """
        expect = "Undeclared Class: MNP"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_423(self):
        '''Undeclared Identifier'''
        input = """
        class DEF extends io{
            void main(){
                io.writeBoolLn(!false || true || !true && false);
            }
        }

        class ABC extends DEF{
            int abc;
            bla(ABC abc; DEF def; io IO; bla Bla){
                /**/
            }
        }
        """
        expect = "Undeclared Class: bla"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_424(self):
        '''Undeclared Identifier'''
        input = """
        class DEF extends io{
            void main(){
                this.main();
                io.writeBoolLn(!false || true || !true && false);
            }
        }

        class ABC extends DEF{
            int abc;
            bla(ABC abc; DEF def; io IO, bla){
                this.Bla();
            }
        }
        """
        expect = "Undeclared Method: Bla"
        self.assertTrue(TestChecker.test(input,expect,424))


    def test25(self):
        input = """
        class A {
            static final int a = 10;
        }
        class B extends A {
            
        }
        class C extends B {
            
        }
        class D extends C {
            
        }
        class E {
            final int a = D.a;
        }
        """
        expect = """['Valid']"""
        self.assertTrue(TestChecker.test(input, str(expect), 425))

    def test_91(self):
        input = """
        class A {
            static final int a = 10;
        }
        class B extends A {
            
        }
        class C extends B {
            
        }
        class D extends C {
            
        }
        class E {
            final int a = D.a;
            final int e = nil;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(e),IntType,NullLiteral())"
        self.assertTrue(TestChecker.test(input, str(expect), 491))