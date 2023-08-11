import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test1(self):
        input = """class main {
            final int a = 3;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),ConstDecl(Id('a'),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test2(self):
        input = """class main {
            final int a = 3;

            main(){}
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id('main'),[AttributeDecl(Instance(),ConstDecl(Id('a'),IntType(),IntLiteral(3))),MethodDecl(Instance(),Id('<init>'),[],None,Block([],[])),MethodDecl(Instance(),Id('<init>'),[],None,Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test3(self):
        input = """
        class Exam {
                        static int a = 5, b;
                    }
        """
        expect = str(Program(decl=[ClassDecl(classname=Id(name='Exam'), memlist=[AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='a'), varType=IntType(), varInit=IntLiteral(value=5))), AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='b'), varType=IntType(), varInit=None))], parentname=None)]))
        self.assertTrue(TestAST.test(input,expect,303))
     
    def test4(self):
        input = """
            class Shape {
                float length,width;
                float getArea() {
                }
                Shape(float length,width){
                    this.length := length;
                    this.width := width;
                }
            }
                class Rectangle extends Shape {
                float getArea(){
        
                return this.length * this.width;
                }
                }

        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[])),MethodDecl(Id(<init>),Instance,[param(Id(length),FloatType),param(Id(width),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 304)) 

    def test5(self):
        input = """
        class S {
            int[5] a = {1,2,3};
        }
        """
        expect = str(Program([ClassDecl(Id('S'),[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id('a'),varType=ArrayType(size=5,eleType=IntType()),varInit=ArrayLiteral(value=[IntLiteral(value=1),IntLiteral(value=2),IntLiteral(value=3)])))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test6(self):
        input = """
        class Rectangle extends Node {
                void name(){
                    (a.b[t0]).yt := 1;
                }
            }
        """
        expect = str(Program([ClassDecl(classname=Id("Rectangle"),parentname=Id('Node'),memlist=[MethodDecl(name=Id('name'),kind=Instance(),param=[],returnType=VoidType(),body=Block(decl=[],stmt=[Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),Id("b")),Id("t0")),Id("yt")),IntLiteral(1))]))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test7(self):
        input = """
            class Rectangle extends Shape {
                float getArea(){
                    ID.total[0] := ID.total[0] +1;
                }
            }

        """
        expect = str(Program(
        [
            ClassDecl(
                Id("Rectangle"),
                [
                MethodDecl(
                    Instance(),
                    Id("getArea"),
                    [],
                    FloatType(),
                    Block([],
                        [
                            Assign(
                                    ArrayCell(FieldAccess(Id("ID"),Id("total")),IntLiteral(0)),
                                    BinaryOp("+",ArrayCell(FieldAccess(Id("ID"),Id("total")),IntLiteral(0)),IntLiteral(1))
                            )
                        ]
                    )
                )
                ],
                Id("Shape")
            )
        ]
        ))
        self.assertTrue(TestAST.test(input,expect,307))

    def test8(self):
        input = """
            class Rectangle extends Node {
                void name(){
                    int[3] a;
                    a[1 + x.foo(2)] := a[a[1 + 1]];
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id("Rectangle"),
                [
                    MethodDecl(
                        Instance(),
                        Id("name"),
                        [],
                        VoidType(),
                        Block(
                            [
                                VarDecl(Id("a"),ArrayType(3,IntType()))
                            ],
                            [
                                Assign(
                                    ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),
                                    ArrayCell(Id("a"),ArrayCell(
                                        Id("a"),
                                        BinaryOp("+",IntLiteral(1),IntLiteral(1))
                                    )
                                    )
                                )
                            ]
                        )
                    )
                ],
                Id("Node")
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test9(self):
        input = """
        class Rectangle extends Node {
                void name(){
                    s := 1+2-(3*4)/5;
                }
            }
        """
        expect = """Program([ClassDecl(Id(Rectangle),Id(Node),[MethodDecl(Id(name),Instance,[],VoidType,Block([],[AssignStmt(Id(s),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5))))]))])])"""

        self.assertTrue(TestAST.test(input,expect,309))

    def test10(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void stepbrother= 1213;
            void imstuck() {

            }
        }"""
        expect = str(Program([ClassDecl(classname=Id('Test'),memlist=[AttributeDecl(Instance(),VarDecl(Id('a'),IntType(),StringLiteral('"addmaximum"'))),AttributeDecl(Instance(),VarDecl(Id('b'),IntType(),FloatLiteral(1.18))),AttributeDecl(Static(),VarDecl(Id('stepbrother'),VoidType(),IntLiteral(1213))),MethodDecl(name=Id('imstuck'),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input_text, expect, 310))

        
    def test11(self):
        input = """
        class Rectangle extends Node {
                void name(){
                    if i == 0 then
                        if a >= 0 
                            then a:= 0;
                        else 
                            return 0 + x.name();
                    else 
                        if !true 
                            then continue;
                        else 
                            if a == 1 then return this.name();
                }
            }

        """
        expect = """Program([ClassDecl(Id(Rectangle),Id(Node),[MethodDecl(Id(name),Instance,[],VoidType,Block([],[If(BinaryOp(==,Id(i),IntLit(0)),If(BinaryOp(>=,Id(a),IntLit(0)),AssignStmt(Id(a),IntLit(0)),Return(BinaryOp(+,IntLit(0),CallExpr(Id(x),Id(name),[])))),If(UnaryOp(!,BooleanLit(True)),Continue,If(BinaryOp(==,Id(a),IntLit(1)),Return(CallExpr(Self(),Id(name),[])))))]))])])"""

        self.assertTrue(TestAST.test(input,expect,311))

    def test12(self):
        input = """
            class Rectangle extends Node {
                void name(){
                    for a:= new A() + 5 to d do {
                        if flag then
                            for b:= 1 to c do {}
                        else if a!=5 then
                           for b:= 2 to c do {}
                        else
                            for b:= 3 to c do {}
                    } 
                }
            }
        """

        expect = """Program([ClassDecl(Id(Rectangle),Id(Node),[MethodDecl(Id(name),Instance,[],VoidType,Block([],[For(Id(a),BinaryOp(+,NewExpr(Id(A),[]),IntLit(5)),Id(d),True,Block([],[If(Id(flag),For(Id(b),IntLit(1),Id(c),True,Block([],[])]),If(BinaryOp(!=,Id(a),IntLit(5)),For(Id(b),IntLit(2),Id(c),True,Block([],[])]),For(Id(b),IntLit(3),Id(c),True,Block([],[])])))])])]))])])"""


        self.assertTrue(TestAST.test(input,expect,312))

    def test313(self):
        """Simple program: class main {} """
        input = """
        class main extends Main{

        }
        """
        expect = str(Program([ClassDecl(Id("main"),[], Id("Main"))]))
        self.assertTrue(TestAST.test(input,expect,313))
   
    def test14(self):
        """Simple program: class main {} """
        input = """
        class main extends main{
            static int a = 1;
        }
        """
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(1)))], Id("main"))]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test15(self):
        input = """
        class main{
            final static bool flag = True;
            final float f;
        }
        """
        expect = Program([ClassDecl(Id("main"), [AttributeDecl(Static(), ConstDecl(Id("flag"), ClassType(Id("bool")), Id("True"))), AttributeDecl(Instance(), ConstDecl(Id("f"), FloatType(), None))], None)])
        self.assertTrue(TestAST.test(input,str(expect),315))
    
    def test15(self):
        input = """
        class main extends ABC{
            static final boolean flag = false;
            float flag1 = true;
        }
        """
        expect = Program([ClassDecl(Id("main"),[AttributeDecl(Static(), ConstDecl(Id("flag"), BoolType(), BooleanLiteral(False))), AttributeDecl(Instance(), VarDecl(Id("flag1"), FloatType(), BooleanLiteral(True)))], Id("ABC"))])
        self.assertTrue(TestAST.test(input,str(expect),315))
    
    def test16(self):
        input = """
        class main{
            int main(){
                return 0;
            }
        }
        """
        expect = Program([ClassDecl(Id("main"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [Return(IntLiteral(0))]))], None)])
        self.assertTrue(TestAST.test(input,str(expect),316))
    
    def test18(self):
        input = """
        class ___ extends __{
            bool foo(string a,b){

            }

            static float pi = 1e9;
        }
        """
        method_decl = MethodDecl(Instance(), Id("foo"), [VarDecl(Id("a"), StringType(), None), VarDecl(Id("b"), StringType(), None)], ClassType(Id("bool")), Block([], []))
        expect = Program([ClassDecl(Id("___"),[method_decl, AttributeDecl(Static(), VarDecl(Id("pi"), FloatType(), FloatLiteral(1e9)))], Id("__"))])
        self.assertTrue(TestAST.test(input,str(expect),318))
    
    def test19(self):
        input = """
        class main extends __init__{
            main(int a; float b, c){
                {

                }
                break;
            }
        }
        """
        method_decl = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("a"), IntType(), None), VarDecl(Id("b"), FloatType(), None), VarDecl(Id("c"), FloatType(), None)], None, Block([], [Block([], []), Break()]))
        expect = Program([ClassDecl(Id("main"),[method_decl], Id("__init__"))])
        self.assertTrue(TestAST.test(input,str(expect),319))
    
    def test20(self):
        input = """
        class __init__ extends __init__{
            static int main(float a, c, _){
                continue;
                {
                    if flag then return 0;
                }
            }
        }
        """
        vardecls = [VarDecl(Id("a"), FloatType(), None), VarDecl(Id("c"), FloatType(), None), VarDecl(Id("_"), FloatType(), None)]
        block = Block([], [Continue(), Block([], [If(Id("flag"), Return(IntLiteral(0)))])])
        method_decl = MethodDecl(Static(), Id("main"), vardecls, IntType(), block)
        expect = Program([ClassDecl(Id("__init__"),[method_decl], Id("__init__"))])
        self.assertTrue(TestAST.test(input,str(expect),320))
    
    def test21(self):
        input = """
        class main{
            
        }

        class main1 extends main2{
            int a = 0;
            final static Final f = 0001.;
            static final Static s = false;
            static string x = "Hello\\t";
            final const pi = 3.14e-0;
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), IntLiteral(0)))
        a2 = AttributeDecl(Static(), ConstDecl(Id("f"), ClassType(Id("Final")), FloatLiteral(1.)))
        a3 = AttributeDecl(Static(), ConstDecl(Id("s"), ClassType(Id("Static")), BooleanLiteral(False)))
        a4 = AttributeDecl(Static(), VarDecl(Id("x"), StringType(), StringLiteral('"Hello\\t"')))
        a5 = AttributeDecl(Instance(), ConstDecl(Id("pi"), ClassType(Id("const")), FloatLiteral(3.14e-0)))
        expect = Program([ClassDecl(Id("main"),[], None), ClassDecl(Id("main1"),[a1, a2, a3, a4, a5], Id("main2"))])
        self.assertTrue(TestAST.test(input,str(expect),321))
    
    def test22(self):
        input = """
        class ABC{
            # empty class
            /* just a block comment*/
        }

        class XYZ extends ABC{
            int factorial(int n){
                if n <= 1 then return n;
                else return n * this.factorial(n - 1);
            }
        }
        """
        block = Block([], [If(BinaryOp("<=", Id("n"), IntLiteral(1)), Return(Id("n")), Return(BinaryOp("*", Id("n"), CallExpr(SelfLiteral(), Id("factorial"), [BinaryOp("-", Id("n"), IntLiteral(1))]))))])
        method_decl = MethodDecl(Instance(), Id("factorial"), [VarDecl(Id("n"), IntType(), None)], IntType(), block)
        expect = Program([ClassDecl(Id("ABC"),[], None), ClassDecl(Id("XYZ"), [method_decl], Id("ABC"))])
        self.assertTrue(TestAST.test(input,str(expect),322))
    
    def test23(self):
        input = """
        class XYZ extends ABC{
            int main(){
                for i := 0 to 10 do
                    sys.io.print(i);
                return 0;
            }
        }
        """
        for_stmt = For(Id("i"), IntLiteral(0), IntLiteral(10), True, CallStmt(FieldAccess(Id("sys"), Id("io")), Id("print"), [Id("i")]))
        block = Block([], [for_stmt, Return(IntLiteral(0))])
        method_decl = MethodDecl(Instance(), Id("main"), [], IntType(), block)
        expect = Program([ClassDecl(Id("XYZ"),[method_decl], Id("ABC"))])
        
        self.assertTrue(TestAST.test(input,str(expect),323))

    def test24(self):
        """Simple program: class main {} """
        input = """
        class main {}
        """
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,312))
    
    def test313(self):
        input = """
        class main{
            __init__(){
                sys.print("init");
            }
            static Num a = new Num();
        }
        """
        block = Block([], [CallStmt(Id("sys"), Id("print"), [StringLiteral('"init"')])])
        method_decl = MethodDecl(Instance(), Id("<init>"), [], None, block)
        a1 = AttributeDecl(Static(), VarDecl(Id("a"), ClassType(Id("Num")), NewExpr(Id("Num"), [])))
        expect = Program([ClassDecl(Id("main"), [method_decl, a1], None)])
        # print(str(expect))
        self.assertTrue(TestAST.test(input,str(expect),324))

    def test25(self):
        input = """
        class main{
            static Num a = new Num();
            int lower = sys.random().randint(1, 10);
            
            float calc(){
                string[5] lst = {"abc", 5};
                for i := 10 downto lower do
                    sys.print(lst[i % 2] ^ ".py");
            }
        }
        """
        a1 = AttributeDecl(Static(), VarDecl(Id("a"), ClassType(Id("Num")), NewExpr(Id("Num"), [])))
        a2 = AttributeDecl(Instance(), VarDecl(Id("lower"), IntType(), CallExpr(CallExpr(Id("sys"), Id("random"), []), Id("randint"), [IntLiteral(1), IntLiteral(10)])))
        for_stmt = For(Id("i"), IntLiteral(10), Id("lower"), False, CallStmt(Id("sys"), Id("print"), [BinaryOp("^", ArrayCell(Id("lst"), BinaryOp("%", Id("i"), IntLiteral(2))), StringLiteral('".py"'))]))
        block = Block([VarDecl(Id("lst"), ArrayType(5, StringType()), ArrayLiteral([StringLiteral('"abc"'), IntLiteral(5)]))], [for_stmt])
        method_decl = MethodDecl(Instance(), Id("calc"), [], FloatType(), block)
        expect = Program([ClassDecl(Id("main"),[a1, a2, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),325))
    
    def test26(self):
        input = """
                class Example1 {
                    int x=5,y,z=7;float a=8*b;
                    int factorial(int n){
                    if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                        int x;
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                    }
                }
        """
        expect = """Program([ClassDecl(Id(Example1),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Instance,VarDecl(Id(z),IntType,IntLit(7))),AttributeDecl(Instance,VarDecl(Id(a),FloatType,BinaryOp(*,IntLit(8),Id(b)))),MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """
            class Shape {
                float length,width;
                float getArea() {
                }
                Shape(float length,width){
                    this.length := length;
                    this.width := width;
                }
            }
                class Rectangle extends Shape {
                float getArea(){

                return this.length * this.width;
                }
                }

        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[])),MethodDecl(Id(<init>),Instance,[param(Id(length),FloatType),param(Id(width),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """
            class Triangle extends Shape {
            float getArea(){
            return this.length*this.width / 2;
            }
            }
                class Example2 {
                void main(){
                 Shape s;
                 s := new Rectangle(3,4);
                    io.writeFloatLn(s.getArea());
                    s := new Triangle(3,4);
                    io.writeFloatLn(s.getArea());
                }
            }
        """
        expect = "Program([ClassDecl(Id(Triangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))]))]),ClassDecl(Id(Example2),[MethodDecl(Id(main),Instance,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),Call(Id(io),Id(writeFloatLn),[CallExpr(Id(s),Id(getArea),[])]),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)])),Call(Id(io),Id(writeFloatLn),[CallExpr(Id(s),Id(getArea),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """
            class Triangle extends Shape {
                final int a;
            }
        """
        expect = 'Program([ClassDecl(Id(Triangle),Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """
            class Rectangle extends React {
                React name(){
                    for a:= 4.3 to ppl do {
                        if ppl == 1 then
                            for b:= 1 to c do {
                                if ppl != 1 then
                                    if ppl == 1 then
                                        ppl := 2;
                                    else if a != 3 then
                                        break;
                            }
                    } 
                }
            }
        """

        expect = """Program([ClassDecl(Id(Rectangle),Id(React),[MethodDecl(Id(name),Instance,[],ClassType(Id(React)),Block([],[For(Id(a),FloatLit(4.3),Id(ppl),True,Block([],[If(BinaryOp(==,Id(ppl),IntLit(1)),For(Id(b),IntLit(1),Id(c),True,Block([],[If(BinaryOp(!=,Id(ppl),IntLit(1)),If(BinaryOp(==,Id(ppl),IntLit(1)),AssignStmt(Id(ppl),IntLit(2)),If(BinaryOp(!=,Id(a),IntLit(3)),Break)))])]))])])]))])])"""

        self.assertTrue(TestAST.test(input,expect,330))
    
    def test31(self):
        input = """
        class people{
            string name;
            int age;
            static int count = 0;

            people(string name; int age){
                this.name := name;
                this.age := age;
            }

            string getName(){
                return this.name;
            }

            int getAge(){
                return this.age;
            }
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("name"), StringType(), None))
        a2 = AttributeDecl(Instance(), VarDecl(Id("age"), IntType(), None))
        a3 = AttributeDecl(Static(), VarDecl(Id("count"), IntType(), IntLiteral(0)))
        block = Block([], [Assign(FieldAccess(SelfLiteral(), Id("name")), Id("name")), Assign(FieldAccess(SelfLiteral(), Id("age")), Id("age"))])
        method_decl = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("name"), StringType(), None), VarDecl(Id("age"), IntType(), None)], None, block)
        block1 = Block([], [Return(FieldAccess(SelfLiteral(), Id("name")))])
        method_decl1 = MethodDecl(Instance(), Id("getName"), [], StringType(), block1)
        block2 = Block([], [Return(FieldAccess(SelfLiteral(), Id("age")))])
        method_decl2 = MethodDecl(Instance(), Id("getAge"), [], IntType(), block2)
        expect = Program([ClassDecl(Id("people"),[a1, a2, a3, method_decl, method_decl1, method_decl2], None)])
        self.assertTrue(TestAST.test(input,str(expect),331))
    
    def test32(self):
        input = """
        class XYZ extends Basic{
            float func(){
                res.o(o, o - _).field := this.foo() + arr[num.lower(s[i]) - 97] \ arr[num.lower(s[i]) - 96];
                return res || something; 
            }

            final boolean flag, fleg, flig;

            static float foo(){
                {
                    {

                    }
                }
            }

            void main = nil;
        }
        """
        ass_stmt = Assign(FieldAccess(CallExpr(Id("res"), Id("o"), [Id("o"), BinaryOp("-", Id("o"), Id("_"))]), Id("field")), BinaryOp("+", CallExpr(SelfLiteral(), Id("foo"), []), BinaryOp("\\", ArrayCell(Id("arr"), BinaryOp("-", CallExpr(Id("num"), Id("lower"), [ArrayCell(Id("s"), Id("i"))]), IntLiteral(97))),  ArrayCell(Id("arr"), BinaryOp("-", CallExpr(Id("num"), Id("lower"), [ArrayCell(Id("s"), Id("i"))]), IntLiteral(96))))))
        block1 = Block([], [ass_stmt, Return(BinaryOp("||", Id("res"), Id("something")))])
        method_decl1 = MethodDecl(Instance(), Id("func"), [], FloatType(), block1)
        a1 = AttributeDecl(Instance(), ConstDecl(Id("flag"), BoolType(), None))
        a2 = AttributeDecl(Instance(), ConstDecl(Id("fleg"), BoolType(), None))
        a3 = AttributeDecl(Instance(), ConstDecl(Id("flig"), BoolType(), None))
        block2 = Block([], [Block([], [Block([], [])])])
        method_decl2 = MethodDecl(Static(), Id("foo"), [], FloatType(), block2)
        a4 = AttributeDecl(Instance(), VarDecl(Id("main"), VoidType(), NullLiteral()))
        expect = Program([ClassDecl(Id("XYZ"),[method_decl1, a1, a2, a3, method_decl2, a4], Id("Basic"))])
        self.assertTrue(TestAST.test(input,str(expect),332))
    
    def test33(self):
        input = """
        class main{
            void call(int x, y; boolean[5] flags){
                for i := x to y do{
                    for j := i >= 1 * 128e+42 downto 0 do{
                        if (flags[i]).get().eval()[0] == true then
                            break;
                        else continue;
                    }
                }
            }
        }
        """
        if_stmt = If(BinaryOp("==", ArrayCell(CallExpr(CallExpr(ArrayCell(Id("flags"), Id("i")), Id("get"), []), Id("eval"), []), IntLiteral(0)), BooleanLiteral(True)), Break(), Continue())
        inner_for_block = Block([], [if_stmt])
        inner_for = For(Id("j"), BinaryOp(">=", Id("i"), BinaryOp("*", IntLiteral(1), FloatLiteral(128e+42))), IntLiteral(0), False, inner_for_block)
        for_block = Block([], [inner_for])
        for_stmt = For(Id("i"), Id("x"), Id("y"), True, for_block)
        block = Block([], [for_stmt])
        method_decl = MethodDecl(Instance(), Id("call"), [VarDecl(Id("x"), IntType(), None), VarDecl(Id("y"), IntType(), None), VarDecl(Id("flags"), ArrayType(5, BoolType()), None)], VoidType(), block)
        expect = Program([ClassDecl(Id("main"),[method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),333))
    
    def test34(self):
        input = """
        class Extends extends extend{ 
            static final arr[100] a = nil;
            Nil Nil(arr[100] a; arr[100] b){
                final boolean f = (call.fact(init) / 0.33E-3) ^ -1;
                return a || b || true && new Nil() && f; 
            }
        }
        """
        a1 = AttributeDecl(Static(), ConstDecl(Id("a"), ArrayType(100, ClassType(Id("arr"))), NullLiteral()))
        v1 = VarDecl(Id("a"), ArrayType(100, ClassType(Id("arr"))))
        v2 = VarDecl(Id("b"), ArrayType(100, ClassType(Id("arr"))))
        init = BinaryOp("^", BinaryOp("/", CallExpr(Id("call"), Id("fact"), [Id("init")]), FloatLiteral(0.33E-3)), UnaryOp("-", IntLiteral(1)))
        c1 = ConstDecl(Id("f"), BoolType(), init)
        return_stmt = Return(BinaryOp("&&", BinaryOp("&&", BinaryOp("||", BinaryOp("||", Id("a"), Id("b")), BooleanLiteral(True)), NewExpr(Id("Nil"), [])), Id("f")))
        block = Block([c1], [return_stmt])
        method_decl = MethodDecl(Instance(), Id("Nil"), [v1, v2], ClassType(Id("Nil")), block)
        expect = Program([ClassDecl(Id("Extends"),[a1, method_decl], Id("extend"))])
        self.assertTrue(TestAST.test(input,str(expect),334))
    
    def test35(self):
        input = """
        class Simple{
            string[5] get5String(){
                for i := sys.str2int("10") to 15 do
                    res := res.append(sys.getStr(i));
                return res; 
            }

            void clone(){
                # empty
            }
        }

        class middleClass{

        }

        class Complex extends Simple{
            static string callSimple(){
                /*/*
                    do nothing  :)
                */
            }
        }
        """
        ass_stmt = Assign(Id("res"), CallExpr(Id("res"), Id("append"), [CallExpr(Id("sys"), Id("getStr"), [Id("i")])]))
        for_stmt = For(Id("i"), CallExpr(Id("sys"), Id("str2int"), [StringLiteral('"10"')]), IntLiteral(15), True, ass_stmt)
        block1 = Block([], [for_stmt, Return(Id("res"))])
        method_decl1 = MethodDecl(Instance(), Id("get5String"), [], ArrayType(5, StringType()), block1)
        method_decl2 = MethodDecl(Instance(), Id("clone"), [], VoidType(), Block([], []))
        method_decl3 = MethodDecl(Static(), Id("callSimple"), [], StringType(), Block([], []))
        expect = Program([ClassDecl(Id("Simple"),[method_decl1, method_decl2], None), ClassDecl(Id("middleClass"),[], None), ClassDecl(Id("Complex"),[method_decl3], Id("Simple"))])
        self.assertTrue(TestAST.test(input,str(expect),335))
    
    def test36(self):
        input = """
        class ACS{
            float x = 2.e+2;
            float y = 123e-3, z;
            int main(){
                if v < 10 then
                    break;
                else
                    v := v <= d && true;
                v := 4 \ (2 * 3153e-3) * r * r* r;
            }
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("x"), FloatType(), FloatLiteral(2.e+2)))
        a2 = AttributeDecl(Instance(), VarDecl(Id("y"), FloatType(), FloatLiteral(123e-3)))
        a3 = AttributeDecl(Instance(), VarDecl(Id("z"), FloatType()))
        ass_stmt = Assign(Id("v"), BinaryOp("*", BinaryOp("*", BinaryOp("*", BinaryOp("\\", IntLiteral(4), BinaryOp("*", IntLiteral(2), FloatLiteral(3153e-3))), Id("r")), Id("r")), Id("r")))
        if_stmt = If(BinaryOp("<", Id("v"), IntLiteral(10)), Break(), Assign(Id("v"), BinaryOp("<=", Id("v"), BinaryOp("&&", Id("d"), BooleanLiteral(True)))))
        block = Block([], [if_stmt, ass_stmt])
        method_decl = MethodDecl(Instance(), Id("main"), [], IntType(), block)
        expect = Program([ClassDecl(Id("ACS"),[a1, a2, a3, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),336))

    def test37(self):
        input = """
        class ACS{
            float x = 2.e+2, y = 123e-3, z;
            int main(){
                v := 4 \ (2 * 3153e-3) * r * r* r;
                if v < 10 then
                    break;
                else
                    v := v <= d && true;
            }
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("x"), FloatType(), FloatLiteral(2.e+2)))
        a2 = AttributeDecl(Instance(), VarDecl(Id("y"), FloatType(), FloatLiteral(123e-3)))
        a3 = AttributeDecl(Instance(), VarDecl(Id("z"), FloatType()))
        ass_stmt = Assign(Id("v"), BinaryOp("*", BinaryOp("*", BinaryOp("*", BinaryOp("\\", IntLiteral(4), BinaryOp("*", IntLiteral(2), FloatLiteral(3153e-3))), Id("r")), Id("r")), Id("r")))
        if_stmt = If(BinaryOp("<", Id("v"), IntLiteral(10)), Break(), Assign(Id("v"), BinaryOp("<=", Id("v"), BinaryOp("&&", Id("d"), BooleanLiteral(True)))))
        block = Block([], [ass_stmt, if_stmt])
        method_decl = MethodDecl(Instance(), Id("main"), [], IntType(), block)
        expect = Program([ClassDecl(Id("ACS"),[a1, a2, a3, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),337))
    
    def test38(self):
        input = """
        class ABC{
            # pass
        }

        class DEF{
            /*  pass    */
        }

        class GHI{

        }

        class KLM{
            static Float foo(int a, b, c; float d, e, f; string g, h, i; boolean k, l, m; void n, o, p; float[1] q, r, s; Class t, u, v){
                # pass
            }
        }

        class NOP{
            
        }

        class QRS extends NOP{

        }

        class TUV{

        }
        """
        v1 = VarDecl(Id("a"), IntType(), None)
        v2 = VarDecl(Id("b"), IntType(), None)
        v3 = VarDecl(Id("c"), IntType(), None)
        v4 = VarDecl(Id("d"), FloatType(), None)
        v5 = VarDecl(Id("e"), FloatType(), None)
        v6 = VarDecl(Id("f"), FloatType(), None)
        v7 = VarDecl(Id("g"), StringType(), None)
        v8 = VarDecl(Id("h"), StringType(), None)
        v9 = VarDecl(Id("i"), StringType(), None)
        v10 = VarDecl(Id("k"), BoolType(), None)
        v11 = VarDecl(Id("l"), BoolType(), None)
        v12 = VarDecl(Id("m"), BoolType(), None)
        v13 = VarDecl(Id("n"), VoidType(), None)
        v14 = VarDecl(Id("o"), VoidType(), None)
        v15 = VarDecl(Id("p"), VoidType(), None)
        v16 = VarDecl(Id("q"), ArrayType(1, FloatType()), None)
        v17 = VarDecl(Id("r"), ArrayType(1, FloatType()), None)
        v18 = VarDecl(Id("s"), ArrayType(1, FloatType()), None)
        v19 = VarDecl(Id("t"), ClassType(Id("Class")), None)
        v20 = VarDecl(Id("u"), ClassType(Id("Class")), None)
        v21 = VarDecl(Id("v"), ClassType(Id("Class")), None)
        method_decl = MethodDecl(Static(), Id("foo"), [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21], ClassType(Id("Float")), Block([], []))
        class1 = ClassDecl(Id("ABC"),[], None)
        class2 = ClassDecl(Id("DEF"),[], None)
        class3 = ClassDecl(Id("GHI"),[], None)
        class4 = ClassDecl(Id("KLM"),[method_decl], None)
        class5 = ClassDecl(Id("NOP"),[], None)
        class6 = ClassDecl(Id("QRS"),[], Id("NOP"))
        class7 = ClassDecl(Id("TUV"),[], None)
        expect = Program([class1, class2, class3, class4, class5, class6, class7])
        self.assertTrue(TestAST.test(input,str(expect),338))
    
    def test39(self):
        input = """
        class main{
            res func(){
                string k = this;
                k := !-k;
                a[2 + 3] := calc.foo(2 + k, k, a[0]);
                m.n.p().q.k().l().o := a[k + b[2 + c[2]]];
                return m;
            }
            static string str = "str", str1;
        }
        """
        v1 = VarDecl(Id("k"), StringType(), SelfLiteral())
        ass1 = Assign(Id("k"), UnaryOp("!", UnaryOp("-", Id("k"))))
        lhs1 = ArrayCell(Id("a"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))
        rhs1 = CallExpr(Id("calc"), Id("foo"), [BinaryOp("+", IntLiteral(2), Id("k")), Id("k"), ArrayCell(Id("a"), IntLiteral(0))])
        ass2 = Assign(lhs1, rhs1)
        lhs = FieldAccess(CallExpr(CallExpr(FieldAccess(CallExpr(FieldAccess(Id("m"), Id("n")), Id("p"), []), Id("q")), Id("k"), []), Id("l"), []), Id("o"))
        rhs = ArrayCell(Id("a"), BinaryOp("+", Id("k"), ArrayCell(Id("b"), BinaryOp("+", IntLiteral(2), ArrayCell(Id("c"), IntLiteral(2))))))
        ass3 = Assign(lhs, rhs)
        return_stmt = Return(Id("m"))
        block = Block([v1], [ass1, ass2, ass3, return_stmt])
        method_decl = MethodDecl(Instance(), Id("func"), [], ClassType(Id("res")), block)
        a1 = AttributeDecl(Static(), VarDecl(Id("str"), StringType(), StringLiteral('"str"')))
        a2 = AttributeDecl(Static(), VarDecl(Id("str1"), StringType(), None))
        expect = Program([ClassDecl(Id("main"),[method_decl, a1, a2], None)])
        self.assertTrue(TestAST.test(input,str(expect),339))

    

    def test40(self):
        input = """
        class main{
            int[0] f(string s; void v){
                float[3] arr = {1, 2., true, ""};
                if n || m == true then
                    return (x + y);
                else
                    return (a % b \ c);
            }
        }
        """
        v1 = VarDecl(Id("arr"), ArrayType(3, FloatType()), ArrayLiteral([IntLiteral(1), FloatLiteral(2.), BooleanLiteral(True), StringLiteral('""')]))
        if_stmt = If(BinaryOp("==",BinaryOp("||", Id("n"), Id("m")), BooleanLiteral(True)), Return(BinaryOp("+", Id("x"), Id("y"))), Return(BinaryOp("\\", BinaryOp("%", Id("a"), Id("b")), Id("c"))))
        block = Block([v1], [if_stmt])
        method_decl = MethodDecl(Instance(), Id("f"), [VarDecl(Id("s"), StringType(), None), VarDecl(Id("v"), VoidType(), None)], ArrayType(0, IntType()), block)
        expect = Program([ClassDecl(Id("main"),[method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),340))
    
    def test41(self):
        input = """
        class main{
            static int i;
            float[3] main(){
                for i := n downto 0 do
                    c := arr[i] % arr[{1, 2}];
            }
        }
        """
        v1 = AttributeDecl(Static(), VarDecl(Id("i"), IntType(), None))
        ass_stmt = Assign(Id("c"), BinaryOp("%", ArrayCell(Id("arr"), Id("i")), ArrayCell(Id("arr"), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        for_stmt = For(Id("i"), Id("n"), IntLiteral(0), False, ass_stmt)
        block = Block([], [for_stmt])
        method_decl = MethodDecl(Instance(), Id("main"), [], ArrayType(3, FloatType()), block)
        expect = Program([ClassDecl(Id("main"),[v1, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),341))
    
    def test42(self):
        input = """
        class main{
            static string call(int x; int y; int z){
                c := arr[0];
                if c <= x ^ y ^ z then
                    c := call.foo({1} + {2});
            }
            void main(){
                final int x = 1, y = 2, z = 3;
                this.call(x, y, z);
            }
        }
        """
        ass_stmt = Assign(Id("c"), CallExpr(Id("call"), Id("foo"), [BinaryOp("+", ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2)]))]))
        if_stmt = If(BinaryOp("<=", Id("c"), BinaryOp("^", BinaryOp("^", Id("x"), Id("y")), Id("z"))), ass_stmt)
        block1 = Block([], [Assign(Id("c"), ArrayCell(Id("arr"), IntLiteral(0))), if_stmt])
        v1 = VarDecl(Id("x"), IntType(), None)
        v2 = VarDecl(Id("y"), IntType(), None)
        v3 = VarDecl(Id("z"), IntType(), None)
        method_decl1 = MethodDecl(Static(), Id("call"), [v1, v2, v3], StringType(), block1)
        v4 = ConstDecl(Id("x"), IntType(), IntLiteral(1))
        v5 = ConstDecl(Id("y"), IntType(), IntLiteral(2))
        v6 = ConstDecl(Id("z"), IntType(), IntLiteral(3))
        call_stmt = CallStmt(SelfLiteral(), Id("call"), [Id("x"), Id("y"), Id("z")])
        block2 = Block([v4, v5, v6], [call_stmt])
        method_decl2 = MethodDecl(Instance(), Id("main"), [], VoidType(), block2)
        expect = Program([ClassDecl(Id("main"),[method_decl1, method_decl2], None)])
        self.assertTrue(TestAST.test(input,str(expect),342))
    
    def test43(self):
        input = """
        class main{
            boolean sort(int[10] arr; int l; int r){
                for i := l + 1 to r do{
                    int tmp, j;
                    tmp := arr[i];
                    j := i - 1;
                    /*
                    bla bla
                    */
                    arr[j + 1] := tmp;
                }
            }
        }
        """
        ass1 = Assign(Id("tmp"), ArrayCell(Id("arr"), Id("i")))
        ass2 = Assign(Id("j"), BinaryOp("-", Id("i"), IntLiteral(1)))
        ass3 = Assign(ArrayCell(Id("arr"), BinaryOp("+", Id("j"), IntLiteral(1))), Id("tmp"))
        for_block = Block([VarDecl(Id("tmp"), IntType(), None), VarDecl(Id("j"), IntType(), None)], [ass1, ass2, ass3])
        for_stmt = For(Id("i"), BinaryOp("+", Id("l"), IntLiteral(1)), Id("r"), True, for_block)
        block = Block([], [for_stmt])
        v1 = VarDecl(Id("arr"), ArrayType(10, IntType()), None)
        v2 = VarDecl(Id("l"), IntType(), None)
        v3 = VarDecl(Id("r"), IntType(), None)
        method_decl = MethodDecl(Instance(), Id("sort"), [v1, v2, v3], BoolType(), block)
        expect = Program([ClassDecl(Id("main"),[method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),343))
    
    def test44(self):
        input = """
        class main extends class_{
            static void convert(string str){
                final boolean[100] arr;
                length := calc.length(str) - 1 - 2;
                return length;
            }
        }
        """
        v1 = ConstDecl(Id("arr"), ArrayType(100, BoolType()), None)
        ass1 = Assign(Id("length"), BinaryOp("-", BinaryOp("-", CallExpr(Id("calc"), Id("length"), [Id("str")]), IntLiteral(1)), IntLiteral(2)))
        block = Block([v1], [ass1, Return(Id("length"))])
        method_decl = MethodDecl(Static(), Id("convert"), [VarDecl(Id("str"), StringType(), None)], VoidType(), block)
        expect = Program([ClassDecl(Id("main"),[method_decl], Id("class_"))])
        self.assertTrue(TestAST.test(input,str(expect),344))
    
    def test45(self):
        input = """
        class main{
            _ func(){
                return this.foo()[1 / nil \ this];
            }
        }
        """
        return_stmt = Return(ArrayCell(CallExpr(SelfLiteral(), Id("foo"), []), BinaryOp("\\", BinaryOp("/", IntLiteral(1), NullLiteral()), SelfLiteral())))
        block = Block([], [return_stmt])
        method_decl = MethodDecl(Instance(), Id("func"), [], ClassType(Id("_")), block)
        expect = Program([ClassDecl(Id("main"),[method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),345))
    
    def test46(self):
        input = """
        class main{
            _ res;
            _(){
                for j := a[b[c[0]]] to n do
                {
                    {
                        # sys.print(i);
                    }
                }
                if nil then return 0; 
                else return 1;
            }
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("res"), ClassType(Id("_")), None))
        for_stmt = For(Id("j"), ArrayCell(Id("a"), ArrayCell(Id("b"), ArrayCell(Id("c"), IntLiteral(0)))), Id("n"), True, Block([], [Block([], [])]))
        if_stmt = If(NullLiteral(), Return(IntLiteral(0)), Return(IntLiteral(1)))
        block = Block([], [for_stmt, if_stmt])
        method_decl = MethodDecl(Instance(), Id("<init>"), [], None, block)
        expect = Program([ClassDecl(Id("main"),[a1, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),346))
    
    def test47(self):
        input = """
        class Shape {
            static final int numOfShape = 0;
            final int immuAttribute = 0;
            float length,width;
            static int getNumOfShape() {
                return numOfShape;
            }
        }
        """
        a1 = AttributeDecl(Static(), ConstDecl(Id("numOfShape"), IntType(), IntLiteral(0)))
        a2 = AttributeDecl(Instance(), ConstDecl(Id("immuAttribute"), IntType(), IntLiteral(0)))
        a3 = AttributeDecl(Instance(), VarDecl(Id("length"), FloatType(), None))
        a4 = AttributeDecl(Instance(), VarDecl(Id("width"), FloatType(), None))
        method_decl = MethodDecl(Static(), Id("getNumOfShape"), [], IntType(), Block([], [Return(Id("numOfShape"))]))
        expect = Program([ClassDecl(Id("Shape"),[a1, a2, a3, a4, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),347))
    
    def test48(self):
        input = """
        class Rectangle extends Shape {
            float getArea(int a; float b){
               return this.length*this.width;
            }
        }
        """
        block = Block([], [Return(BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))])
        method_decl = MethodDecl(Instance(), Id("getArea"), [VarDecl(Id("a"), IntType(), None), VarDecl(Id("b"), FloatType(), None)], FloatType(), block)
        expect = Program([ClassDecl(Id("Rectangle"),[method_decl], Id("Shape"))])
        self.assertTrue(TestAST.test(input,str(expect),348))
    
    def test49(self):
        input = """
        class ID {
            static int[4] total={0,0,0,0};
            string name;
            ID(){
                this.name:=nil;
            }
            ID(string name){
                this.name:=name;
                ID.total[0] := ID.total[0] +1;
            }
        }
        """
        a1 = AttributeDecl(Static(), VarDecl(Id("total"), ArrayType(4, IntType()), ArrayLiteral([IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)])))
        a2 = AttributeDecl(Instance(), VarDecl(Id("name"), StringType(), None))
        block1 = Block([], [Assign(FieldAccess(SelfLiteral(), Id("name")), NullLiteral())])
        method_decl1 = MethodDecl(Instance(),Id("<init>"), [], None, block1)
        ass1 = Assign(FieldAccess(SelfLiteral(), Id("name")), Id("name"))
        ass2 = Assign(ArrayCell(FieldAccess(Id("ID"), Id("total")), IntLiteral(0)), BinaryOp("+", ArrayCell(FieldAccess(Id("ID"), Id("total")), IntLiteral(0)), IntLiteral(1)))
        block2 = Block([], [ass1, ass2])
        method_decl2 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("name"), StringType(), None)], None, block2)
        expect = Program([ClassDecl(Id("ID"),[a1, a2, method_decl1, method_decl2], None)])
        self.assertTrue(TestAST.test(input,str(expect),349))
    

    def test_350(self):
        input = """class ppl extends bbl {
                final static int[5] bbl = 1, ppl;
                void main() {
                    a[3+x.foo(2)] := a[b[2]] +3;
                    x.b[2] := x.m()[3];
                }
            }"""
        expect= """Program([ClassDecl(Id(ppl),Id(bbl),[AttributeDecl(Static,ConstDecl(Id(bbl),ArrayType(5,IntType),IntLit(1))),AttributeDecl(Static,ConstDecl(Id(ppl),ArrayType(5,IntType),None)),MethodDecl(Id(main),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3))),AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test51(self):
        input = """
        class main extends Main {
            string nothing(){
                # really nothing :V
            }

            static string main(){
                (str[0])[0] := "1" + "1";
                return str ^ "= \\"2\\"";
            }
        }
        """
        method_decl1 = MethodDecl(Instance(), Id("nothing"), [], StringType(), Block([], []))
        ass1 = Assign(ArrayCell(ArrayCell(Id("str"), IntLiteral(0)), IntLiteral(0)), BinaryOp("+", StringLiteral('"1"'), StringLiteral('"1"')))
        return1 = Return(BinaryOp("^", Id("str"), StringLiteral('"= \\"2\\""')))
        method_decl2 = MethodDecl(Static(), Id("main"), [], StringType(), Block([], [ass1, return1]))
        expect = Program([ClassDecl(Id("main"),[method_decl1, method_decl2], Id("Main"))])
        self.assertTrue(TestAST.test(input,str(expect),351))
    
    def test52(self):
        input = """
        class Add extends Operator {
            Nil[2] Operator(Nil[2] n, m){
                {
                    {
                        /*3/*2*4/*/
                    }
                    _.__("nil = this = " \ this.acc(this % 2, nil && this || 2e-3));
                }
                {
                    int a = (5 + this.f() * 3 + arr[10])[2] * 5 \ 8;
                    return a;
                }
            }
        }
        """
        call1 = CallStmt(Id("_"), Id("__"), [BinaryOp("\\", StringLiteral('"nil = this = "'), CallExpr(SelfLiteral(), Id("acc"), [BinaryOp("%", SelfLiteral(), IntLiteral(2)), BinaryOp("||", BinaryOp("&&", NullLiteral(), SelfLiteral()), FloatLiteral(2e-3))]))])
        block1 = Block([], [Block([], []), call1])
        v1 = VarDecl(Id("a"), IntType(), BinaryOp("\\", BinaryOp("*", ArrayCell(BinaryOp("+", BinaryOp("+", IntLiteral(5), BinaryOp("*", CallExpr(SelfLiteral(), Id("f"), []), IntLiteral(3))), ArrayCell(Id("arr"), IntLiteral(10))), IntLiteral(2)), IntLiteral(5)), IntLiteral(8)))
        block2 = Block([v1], [Return(Id("a"))])
        method_decl1 = MethodDecl(Instance(), Id("Operator"), [VarDecl(Id("n"),  ArrayType(2, ClassType(Id("Nil")))), VarDecl(Id("m"), ArrayType(2, ClassType(Id("Nil"))))],  ArrayType(2, ClassType(Id("Nil"))), Block([], [block1, block2]))
        expect = Program([ClassDecl(Id("Add"),[method_decl1], Id("Operator"))])
        self.assertTrue(TestAST.test(input,str(expect),352))
    
    def test53(self):
        input = """
        class Main{
            int x;
            float y;

            static string main(float args){
                this.x["zero"] := 7[10] + 32;
                sys.print("Hello" + "I'm NTD");
                return 0;
            }
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("x"), IntType(), None))
        a2 = AttributeDecl(Instance(), VarDecl(Id("y"), FloatType(), None))
        ass1 = Assign(ArrayCell(FieldAccess(SelfLiteral(), Id("x")), StringLiteral('"zero"')), BinaryOp("+", ArrayCell(IntLiteral(7), IntLiteral(10)), IntLiteral(32)))
        call1 = CallStmt(Id("sys"), Id("print"), [BinaryOp("+", StringLiteral('"Hello"'), StringLiteral('''"I'm NTD"'''))])
        method_decl = MethodDecl(Static(), Id("main"), [VarDecl(Id("args"), FloatType(), None)], StringType(), Block([], [ass1, call1, Return(IntLiteral(0))]))
        expect = Program([ClassDecl(Id("Main"),[a1, a2, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),353))
    
    def test54(self):
        input = """
        class Main extends ABC{
            final boolean x, y = true, z;
            static int[5] count = nil;

            static void main(float[5] args){
                final float nill = 2.e-5;
                x := sys.get().randint(1, 100);
                if new Obj(this, 0) then
                    return nill;
                return +nil;
            }
        }
        """
        a1 = AttributeDecl(Instance(), ConstDecl(Id("x"), BoolType(), None))
        a2 = AttributeDecl(Instance(), ConstDecl(Id("y"), BoolType(), BooleanLiteral(True)))
        a3 = AttributeDecl(Instance(), ConstDecl(Id("z"), BoolType(), None))
        a4 = AttributeDecl(Static(), VarDecl(Id("count"), ArrayType(5, IntType()), NullLiteral()))
        v1 = ConstDecl(Id("nill"), FloatType(), FloatLiteral(2.e-5))
        ass1 = Assign(Id("x"), CallExpr(CallExpr(Id("sys"), Id("get"), []), Id("randint"), [IntLiteral(1), IntLiteral(100)]))
        if1 = If(NewExpr(Id("Obj"), [SelfLiteral(), IntLiteral(0)]), Return(Id("nill")))
        return1 = Return(UnaryOp("+", NullLiteral()))
        method_decl = MethodDecl(Static(), Id("main"), [VarDecl(Id("args"), ArrayType(5, FloatType()))], VoidType(), Block([v1], [ass1, if1, return1]))
        expect = Program([ClassDecl(Id("Main"),[a1, a2, a3, a4, method_decl], Id("ABC"))])
        self.assertTrue(TestAST.test(input,str(expect),354))
    
    def test55(self):
        input = """
        class Calculation{
            static boolean findMax(bool[3] arr){
                return arr[sys.get.num().randint(0, 10, False) -- _._()];
            }

            static string main(){
                sys.print(this.findMax({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
                return 0;
            }
        }
        """
        rhs = UnaryOp("-", CallExpr(Id("_"), Id("_"), []))
        lhs = CallExpr(CallExpr(FieldAccess(Id("sys"), Id("get")), Id("num"), []), Id("randint"), [IntLiteral(0), IntLiteral(10), Id("False")])
        return1 = Return(ArrayCell(Id("arr"), BinaryOp("-", lhs, rhs)))
        method_decl1 = MethodDecl(Static(), Id("findMax"), [VarDecl(Id("arr"), ArrayType(3, ClassType(Id("bool"))))], BoolType(), Block([], [return1]))
        call1 = CallStmt(Id("sys"), Id("print"), [CallExpr(SelfLiteral(), Id("findMax"), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5), IntLiteral(6), IntLiteral(7), IntLiteral(8), IntLiteral(9), IntLiteral(10)])])])
        method_decl2 = MethodDecl(Static(), Id("main"), [], StringType(), Block([], [call1, Return(IntLiteral(0))]))
        expect = Program([ClassDecl(Id("Calculation"),[method_decl1, method_decl2], None)])
        self.assertTrue(TestAST.test(input,str(expect),355))
    
    def test56(self):
        input = """
        class Extends{
            HelloWorld(int n){
                this.n := n;
            }

            main(){
                void var = 256;
                for i := 0 to this.n do {
                    string str0 = "Hello" %  "World";
                    (_[1])._(_);
                }
            }
        }
        """
        method_decl1 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("n"), IntType(), None)], None, Block([], [Assign(FieldAccess(SelfLiteral(), Id("n")), Id("n"))]))
        v1 = VarDecl(Id("var"), VoidType(), IntLiteral(256))
        block = Block([VarDecl(Id("str0"), StringType(), BinaryOp("%", StringLiteral('"Hello"'), StringLiteral('"World"')))], [CallStmt(ArrayCell(Id("_"), IntLiteral(1)), Id("_"), [Id("_")])])
        for1 = For(Id("i"), IntLiteral(0), FieldAccess(SelfLiteral(), Id("n")), True, block)
        method_decl2 = MethodDecl(Instance(), Id("<init>"), [], None, Block([v1], [for1]))
        expect = Program([ClassDecl(Id("Extends"),[method_decl1, method_decl2], None)])
        self.assertTrue(TestAST.test(input,str(expect),356))
    
    def test57(self):
        input = """
        class Class extends Extends {
            static int[5] arr = {1, 2, 3,4};

            string concat(string s1; string s2){
                string tmp = "";
                for i := n downto s1.length() do
                    tmp := tmp ^ s1[i];
                for i := n downto s2.length() do
                    tmp[s1.length() + i] := s2[i];
                return tmp;
            }
        }
        """
        a1 = AttributeDecl(Static(), VarDecl(Id("arr"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])))
        v1 = VarDecl(Id("s1"), StringType(), None)
        v2 = VarDecl(Id("s2"), StringType(), None)
        v3 = VarDecl(Id("tmp"), StringType(), StringLiteral('""'))
        for1 = For(Id("i"), Id("n"), CallExpr(Id("s1"), Id("length"), []), False, Assign(Id("tmp"), BinaryOp("^", Id("tmp"), ArrayCell(Id("s1"), Id("i")))))
        for2 = For(Id("i"), Id("n"), CallExpr(Id("s2"), Id("length"), []), False, Assign(ArrayCell(Id("tmp"), BinaryOp("+", CallExpr(Id("s1"), Id("length"), []), Id("i"))), ArrayCell(Id("s2"), Id("i"))))
        method_decl = MethodDecl(Instance(), Id("concat"), [v1, v2], StringType(), Block([v3], [for1, for2, Return(Id("tmp"))]))
        expect = Program([ClassDecl(Id("Class"),[a1, method_decl], Id("Extends"))])
        self.assertTrue(TestAST.test(input,str(expect),357))
    
    def test58(self):
        input = """
        class DEF extends ABC {
            int main(){
                final int r = 10, v, i;
                for i := nil to this do
                    sys.writeln(i);
                return r;
            }
        }
        """
        c1 = ConstDecl(Id("r"), IntType(), IntLiteral(10))
        c2 = ConstDecl(Id("v"), IntType(), None)
        c3 = ConstDecl(Id("i"), IntType(), None)
        for1 = For(Id("i"), NullLiteral(), SelfLiteral(), True, CallStmt(Id("sys"), Id("writeln"), [Id("i")]))
        method_decl = MethodDecl(Instance(), Id("main"), [], IntType(), Block([c1, c2, c3], [for1, Return(Id("r"))]))
        expect = Program([ClassDecl(Id("DEF"),[method_decl], Id("ABC"))])
        self.assertTrue(TestAST.test(input,str(expect),358))
    
    def test59(self):
        input = """
        class BlaBla extends BlaBlas{
            void main(){
                if sys.flag then
                    sys.print_some_thing();
                else if !sys.flag then
                    sys.print_some_thing_else();
            }
        }
        """
        if1 = If(FieldAccess(Id("sys"), Id("flag")), CallStmt(Id("sys"), Id("print_some_thing"), []), If(UnaryOp("!", FieldAccess(Id("sys"), Id("flag"))), CallStmt(Id("sys"), Id("print_some_thing_else"), [])))
        method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [if1]))
        expect = Program([ClassDecl(Id("BlaBla"),[method_decl], Id("BlaBlas"))])
        self.assertTrue(TestAST.test(input,str(expect),359))
    
    def test60(self):
        input = """
        class Luxubu {
            final int main = "main".extract_some_thing("hihi");

            float_(int n; float m){
                if n != -5 <= -5 then
                    return 0 >= 1.;
                else
                    return n / functools.reduce(lambda.blabla);
            }
        }
        """
        a1 = AttributeDecl(Instance(), ConstDecl(Id("main"), IntType(), CallExpr(StringLiteral('"main"'), Id("extract_some_thing"), [StringLiteral('"hihi"')])))
        if1 = If(BinaryOp("<=", BinaryOp("!=", Id("n"), UnaryOp("-", IntLiteral(5))), UnaryOp("-",  IntLiteral(5))), Return(BinaryOp(">=", IntLiteral(0), FloatLiteral(1.))), Return(BinaryOp("/", Id("n"), CallExpr(Id("functools"), Id("reduce"), [FieldAccess(Id("lambda"), Id("blabla"))]))))
        method_decl = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("n"), IntType(), None), VarDecl(Id("m"), FloatType(), None)], None, Block([], [if1]))
        expect = Program([ClassDecl(Id("Luxubu"),[a1, method_decl], None)])
        self.assertTrue(TestAST.test(input,str(expect),360))
    
    def test61(self):
        input = """
        class complex extends simple {
            string str(){

            }

            INT len(){
                return this.len;
            }

            string[7] arr = {1.0e+5, 2e-9, "Song Da", "ab\\tc", false};
            static boolean Final = "string \\"", y = 1e9;
        }
        """
        a1 = AttributeDecl(Instance(), VarDecl(Id("arr"), ArrayType(7, StringType()), ArrayLiteral([FloatLiteral(1.0e+5), FloatLiteral(2e-9), StringLiteral('"Song Da"'), StringLiteral('"ab\\tc"'), BooleanLiteral(False)])))
        a2 = AttributeDecl(Static(), VarDecl(Id("Final"), BoolType(), StringLiteral('"string \\""')))
        a3 = AttributeDecl(Static(), VarDecl(Id("y"), BoolType(), FloatLiteral(1e9)))
        method_decl1 = MethodDecl(Instance(), Id("str"), [], StringType(), Block([], []))
        method_decl2 = MethodDecl(Instance(), Id("len"), [], ClassType(Id("INT")), Block([], [Return(FieldAccess(SelfLiteral(), Id("len")))]))
        expect = Program([ClassDecl(Id("complex"),[method_decl1, method_decl2, a1, a2, a3], Id("simple"))])
        self.assertTrue(TestAST.test(input,str(expect),361))
    
    def test62(self):
        input = """
        class main{
            string foo(){
                for i := this + "123" downto nil do{

                }
            }
        }

        class main extends Main {
            float count = nil - 1;

            void method(){
                x["x"] := a.b.c.d;
                a.a := b.b;
            }
        }
        """
        for1 = For(Id("i"), BinaryOp("+", SelfLiteral(), StringLiteral('"123"')), NullLiteral(), False, Block([], []))
        method_decl1 = MethodDecl(Instance(), Id("foo"), [], StringType(), Block([], [for1]))
        v1 = VarDecl(Id("count"), FloatType(), BinaryOp("-", NullLiteral(), IntLiteral(1)))
        ass1 = Assign(ArrayCell(Id("x"), StringLiteral('"x"')), FieldAccess(FieldAccess(FieldAccess(Id("a"), Id("b")), Id("c")), Id("d")))
        ass2 = Assign(FieldAccess(Id("a"), Id("a")), FieldAccess(Id("b"), Id("b")))
        method_decl2 = MethodDecl(Instance(), Id("method"), [], VoidType(), Block([], [ass1, ass2]))
        expect = Program([ClassDecl(Id("main"),[method_decl1], None), ClassDecl(Id("main"),[AttributeDecl(Instance(), v1), method_decl2], Id("Main"))])
        self.assertTrue(TestAST.test(input,str(expect),362))
    

    def test72(self):
        input = """
        class Ex{
            float a;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    FloatType(),
                                    None
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """
        class Ex extends Ey {
            final float a,b,c;
            static int d,e,f;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("a"),
                                    FloatType(),
                                    None
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("b"),
                                    FloatType(),
                                    None
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("c"),
                                    FloatType(),
                                    None
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("d"),
                                    IntType(),
                                    None
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("e"),
                                    IntType(),
                                    None
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("f"),
                                    IntType(),
                                    None
                                )
                            )
                        ],
                        Id("Ey")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(str(input), expect, 373))

    def test74(self):
        input = """
        class Ex{
            int a = -(10+"3") + 2*10;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    BinaryOp(
                                        "+",
                                        UnaryOp(
                                            "-",
                                            BinaryOp(
                                                "+",
                                                IntLiteral(10),
                                                StringLiteral('"3"')
                                            )
                                        ),
                                        BinaryOp(
                                            "*",
                                            IntLiteral(2),
                                            IntLiteral(10)
                                        )
                                    )
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """
        class Ex{
            int a = this.b;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    FieldAccess(
                                        SelfLiteral(),
                                        Id("b")
                                    )
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """
        class Ex{
            A a = this.b() + new Ex(x+y) - nil;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    ClassType(Id("A")),
                                    BinaryOp(
                                        "-",
                                        BinaryOp(
                                            "+",
                                            CallExpr(
                                                SelfLiteral(),
                                                Id("b"),
                                                []
                                            ),
                                            NewExpr(
                                                Id("Ex"),
                                                [
                                                    BinaryOp(
                                                        "+",
                                                        Id("x"),
                                                        Id("y")
                                                    )
                                                ]
                                            )
                                        ),
                                        NullLiteral()
                                    )
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """
        class Ex{
            A a = new A();
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    ClassType(Id("A")),
                                    NewExpr(
                                        Id("A"),
                                        []
                                    )
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """
        class Ex{
            A[10] a = {10,"10",10,"10",10,"10",10,"10",10,"10"};
            static final int _f = this.a+b.c((this.value()).x);
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    ArrayType(10, ClassType(Id("A"))),
                                    ArrayLiteral(
                                        [
                                            IntLiteral(10),
                                            StringLiteral('"10"'),
                                            IntLiteral(10),
                                            StringLiteral('"10"'),
                                            IntLiteral(10),
                                            StringLiteral('"10"'),
                                            IntLiteral(10),
                                            StringLiteral('"10"'),
                                            IntLiteral(10),
                                            StringLiteral('"10"'),
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("_f"),
                                    IntType(),
                                    BinaryOp(
                                        "+",
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("a")
                                        ),
                                        CallExpr(
                                            Id("b"),
                                            Id("c"),
                                            [
                                                FieldAccess(
                                                    CallExpr(
                                                        SelfLiteral(),
                                                        Id("value"),
                                                        []
                                                    ),
                                                    Id("x")
                                                )
                                            ]
                                        )
                                    )
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """
        class Ex{
            void main() {
            
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    []
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """
        class Ex{
            static int foo(float a,b; string c) {
            
            }
            void main() {
            
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            MethodDecl(
                                Static(),
                                Id("foo"),
                                [
                                    VarDecl(
                                        Id("a"),
                                        FloatType(),
                                        None
                                    ),
                                    VarDecl(
                                        Id("b"),
                                        FloatType(),
                                        None
                                    ),
                                    VarDecl(
                                        Id("c"),
                                        StringType(),
                                        None
                                    )
                                ],
                                IntType(),
                                Block(
                                    [],
                                    []
                                )
                            ),
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    []
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """
        class Ex{
            void main(int a) {
                int a,b;
                float c;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ex"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [
                                    VarDecl(
                                        Id("a"),
                                        IntType(),
                                        None
                                    )
                                ],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            IntType(),
                                            None
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            IntType(),
                                            None
                                        ),
                                        VarDecl(
                                            Id("c"),
                                            FloatType(),
                                            None
                                        )
                                    ],
                                    []
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """
            class duc extends Node {
                void name(){
                    for a:= new A() + 5 to d do {
                        if flag then
                            for b:= 7 to c do {}
                        else if a!=5 then
                           for b:= 8 downto c do {}
                        else
                            for b:= 9 to c do {}
                    } 
                }
            }
        """
        expect = """Program([ClassDecl(Id(duc),Id(Node),[MethodDecl(Id(name),Instance,[],VoidType,Block([],[For(Id(a),BinaryOp(+,NewExpr(Id(A),[]),IntLit(5)),Id(d),True,Block([],[If(Id(flag),For(Id(b),IntLit(7),Id(c),True,Block([],[])]),If(BinaryOp(!=,Id(a),IntLit(5)),For(Id(b),IntLit(8),Id(c),False,Block([],[])]),For(Id(b),IntLit(9),Id(c),True,Block([],[])])))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,382))
    # def test360(self):
    #     input = """
    #     class main extends Main {
    #         void method(){
    #             x.a(x, y, "abc").b(123).c().f.d().e := (a[this]).x.y + this.a().b().x + this.a.b.x();
    #         }

    #         string abc(int x; float[2][2] a){

    #         }
    #     }
    #     """
    #     lhs = FieldAccess(CallExpr(FieldAccess(CallExpr(CallExpr(CallExpr(Id("x"), Id("a"), [Id("x"), Id("y"), StringLiteral("abc")]), Id("b"), [IntLiteral(123)]), Id("c"), []), Id("f")), Id("d"), []), Id("e"))
    #     rhs = BinaryOp("+", BinaryOp("+", FieldAccess(FieldAccess(ArrayCell(Id("a"), SelfLiteral()), Id("x")), Id("y")), FieldAccess(CallExpr(CallExpr(SelfLiteral(), Id("a"), []), Id("b"), []), Id("x"))), CallExpr(FieldAccess(FieldAccess(SelfLiteral(), Id("a")), Id("b")), Id("x"), []))
    #     ass1 = Assign(lhs, rhs)
    #     method_decl1 = MethodDecl(Instance(), Id("method"), [], VoidType(), Block([], [ass1]))
    #     method_decl2 = MethodDecl(Instance(), Id("abc"), [VarDecl(Id("x"), IntType(), None), VarDecl(Id("a"), ArrayType(2, ArrayType(2, FloatType())), None)], StringType(), Block([], []))
    #     expect = Program([ClassDecl(Id("main"),[method_decl1, method_decl2], Id("Main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),360))
    
    # def test361(self):
    #     input = """
    #     class main extends Main {
    #         final int count = 0, x = "abc";

    #         void method(boolean x, y, z){
    #             sys.a.b.c(this).d.e.a.c.b(nil).f(a, b, sys.b).x(1e8);
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Instance(), ConstDecl(Id("count"), IntType(), IntLiteral(0)))
    #     a2 = AttributeDecl(Instance(), ConstDecl(Id("x"), IntType(), StringLiteral("abc")))
    #     obj4 = FieldAccess(FieldAccess(Id("sys"), Id("a")), Id("b"))
    #     obj3 = CallExpr(obj4, Id("c"), [SelfLiteral()])
    #     obj2 = FieldAccess(FieldAccess(FieldAccess(FieldAccess(obj3, Id("d")), Id("e")), Id("a")), Id("c"))
    #     obj1 = CallExpr(obj2, Id("b"), [NullLiteral()])
    #     obj = CallExpr(obj1, Id("f"), [Id("a"), Id("b"), FieldAccess(Id("sys"), Id("b"))])
    #     call1 = CallStmt(obj, Id("x"), [FloatLiteral(1e8)])
    #     method_decl = MethodDecl(Instance(), Id("method"), [VarDecl(Id("x"), BoolType(), None), VarDecl(Id("y"), BoolType(), None), VarDecl(Id("z"), BoolType(), None)], VoidType(), Block([], [call1]))
    #     expect = Program([ClassDecl(Id("main"),[a1, a2, method_decl], Id("Main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),361))
    
    # def test362(self):
    #     input = """
    #     class Main extends ABC{
    #         static int i = x[true] + 5;
    #         ClassType[5] arr = {"Qua Deo Ngang", "Ba Huyen Thanh Quan"};

    #         static type main(type args, kwargs){
    #             (sys.param_x())[nil] := 1234 || False + 22222;
    #             return sys.param_x;
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Static(), VarDecl(Id("i"), IntType(), BinaryOp("+", ArrayCell(Id("x"), BooleanLiteral(True)), IntLiteral(5))))
    #     a2 = AttributeDecl(Instance(), VarDecl(Id("arr"), ArrayType(5, ClassType(Id("ClassType"))), ArrayLiteral([StringLiteral("Qua Deo Ngang"), StringLiteral("Ba Huyen Thanh Quan")])))
    #     ass1 = Assign(ArrayCell(CallExpr(Id("sys"), Id("param_x"), []), NullLiteral()), BinaryOp("||", IntLiteral(1234), BinaryOp("+", Id("False"), IntLiteral(22222))))
    #     method_decl = MethodDecl(Static(), Id("main"), [VarDecl(Id("args"), ClassType(Id("type")), None), VarDecl(Id("kwargs"), ClassType(Id("type")), None)], ClassType(Id("type")), Block([], [ass1, Return(FieldAccess(Id("sys"), Id("param_x")))]))
    #     expect = Program([ClassDecl(Id("Main"),[a1, a2, method_decl], Id("ABC"))])
    #     self.assertTrue(TestAST.test(input,str(expect),362))
    
    # def test363(self):
    #     input = """
    #     class ABC extends DEF{
    #         void method(){
    #             if 1.e-2 then
    #             if 1 then
    #                 inp := f23 + ads[2*10] +  ++++ 2 *f /* "87235jkfgshgsfg $&^# */ ;
    #             else return 0;
    #         }
    #     }
    #     """
    #     ass1 = Assign(Id("inp"), BinaryOp("+", BinaryOp("+", Id("f23"), ArrayCell(Id("ads"), BinaryOp("*", IntLiteral(2), IntLiteral(10)))), BinaryOp("*", UnaryOp("+", UnaryOp("+", UnaryOp("+", UnaryOp("+", IntLiteral(2))))), Id("f"))))
    #     if2 = If(IntLiteral(1), ass1, Return(IntLiteral(0)))
    #     if1 = If(FloatLiteral(1.e-2), if2, None)
    #     method_decl = MethodDecl(Instance(), Id("method"), [], VoidType(), Block([], [if1]))
    #     expect = Program([ClassDecl(Id("ABC"),[method_decl], Id("DEF"))])
    #     self.assertTrue(TestAST.test(input,str(expect),363))
    
    # def test364(self):
    #     input = """
    #     class complex extends simple {
    #         void[0001] _init_(){
    #             x[2e-3 + 1] := -x.y && z % t;     # calc some thing, i dont know
    #             sys.print("nothing_to_return");
    #         }

    #         boolean main(){
    #             inp := ppapa[/**4235 dasfj dd 44 **/ this.g(-/*/*--------------------*/-this.f())];
    #             x := "adf" * {23, 4, "af"}[Return];
    #         }
    #     }
    #     """
    #     ass1 = Assign(ArrayCell(Id("x"), BinaryOp("+", FloatLiteral(2e-3), IntLiteral(1))), BinaryOp("&&", UnaryOp("-", FieldAccess(Id("x"), Id("y"))), BinaryOp("%", Id("z"), Id("t"))))
    #     call1 = CallStmt(Id("sys"), Id("print"), [StringLiteral("nothing_to_return")])
    #     method_decl1 = MethodDecl(Instance(), Id("_init_"), [], ArrayType(1, VoidType()), Block([], [ass1, call1]))
    #     ass2 = Assign(Id("inp"), ArrayCell(Id("ppapa"), CallExpr(SelfLiteral(), Id("g"), [UnaryOp("-", UnaryOp("-", CallExpr(SelfLiteral(), Id("f"), [])))])))
    #     ass3  = Assign(Id("x"), BinaryOp("*", StringLiteral("adf"), ArrayCell(ArrayLiteral([IntLiteral(23), IntLiteral(4), StringLiteral("af")]), Id("Return"))))
    #     method_decl2 = MethodDecl(Instance(), Id("main"), [], BoolType(), Block([], [ass2, ass3]))
    #     expect = Program([ClassDecl(Id("complex"),[method_decl1, method_decl2], Id("simple"))])
    #     self.assertTrue(TestAST.test(input,str(expect),364))
    
    # def test365(self):
    #     input = """
    #     class Main extends ABC{
    #         float a = ----1234 || +++False + -+-+ 22222;

    #         void main(){
    #             b := {{{{"abc"}}}, {123}};
    #         }
    #     }
    #     """
    #     init = BinaryOp("||", UnaryOp("-", UnaryOp("-", UnaryOp("-", UnaryOp("-", IntLiteral(1234))))), BinaryOp("+", UnaryOp("+", UnaryOp("+", UnaryOp("+", Id("False")))), UnaryOp("-", UnaryOp("+", UnaryOp("-", UnaryOp("+", IntLiteral(22222)))))))
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("a"), FloatType(), init))
    #     ass1 = Assign(Id("b"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([StringLiteral("abc")])])]), ArrayLiteral([IntLiteral(123)])]))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [ass1]))
    #     expect = Program([ClassDecl(Id("Main"),[a1, method_decl], Id("ABC"))])
    #     self.assertTrue(TestAST.test(input,str(expect),365))
    
    # def test366(self):
    #     input = """
    #     class Calculation{
    #         static int cal(){
    #             int[10] arr = {0.};
    #             for _ := 0[nil] to y do
    #             {
    #                 {
    #                     # just a comment
    #                     kk := 123;
    #                     123[0] := false[2e-3];
    #                 }
    #                 io.writeln(i);
    #             }
    #         }
    #     }
    #     """
    #     v1 = VarDecl(Id("arr"), ArrayType(10, IntType()), ArrayLiteral([FloatLiteral(0.)]))
    #     ass1 = Assign(Id("kk"), IntLiteral(123))
    #     ass2 = Assign(ArrayCell(IntLiteral(123), IntLiteral(0)), ArrayCell(BooleanLiteral(False), FloatLiteral(2e-3)))
    #     block1 = Block([], [ass1, ass2])
    #     block = Block([], [block1, CallStmt(Id("io"), Id("writeln"), [Id("i")])])
    #     for1 = For(Id("_"), ArrayCell(IntLiteral(0), NullLiteral()), Id("y"), True, block)
    #     method_decl = MethodDecl(Static(), Id("cal"), [], IntType(), Block([v1], [for1]))
    #     expect = Program([ClassDecl(Id("Calculation"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),366))
    
    # def test367(self):
    #     input = """
    #     class Extends {
    #         static int Main(Int args){
    #             {
    #                 final string str = args[0];
    #                 if str then break;
    #             }
    #         }

    #         boolean main(Float args){   
    #             if args[0] == kwargs[0] then
    #             {
    #                 if args[0] != kwargs[0] then 
    #                 {
    #                     if args[0] >= kwargs[0] then 
    #                     {
    #                         if args[0] <= kwargs[0] then 
    #                         {
                            
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     v1 = ConstDecl(Id("str"), StringType(), ArrayCell(Id("args"), IntLiteral(0)))
    #     if1 = If(Id("str"), Break(), None)
    #     method_decl1 = MethodDecl(Static(), Id("Main"), [VarDecl(Id("args"), ClassType(Id("Int")))], IntType(), Block([], [Block([v1], [if1])]))
    #     if5 = If(BinaryOp("<=", ArrayCell(Id("args"), IntLiteral(0)), ArrayCell(Id("kwargs"), IntLiteral(0))), Block([], []), None)
    #     if4 = If(BinaryOp(">=", ArrayCell(Id("args"), IntLiteral(0)), ArrayCell(Id("kwargs"), IntLiteral(0))), Block([], [if5]), None)
    #     if3 = If(BinaryOp("!=", ArrayCell(Id("args"), IntLiteral(0)), ArrayCell(Id("kwargs"), IntLiteral(0))), Block([], [if4]), None)
    #     if2 = If(BinaryOp("==", ArrayCell(Id("args"), IntLiteral(0)), ArrayCell(Id("kwargs"), IntLiteral(0))), Block([], [if3]), None)
    #     method_decl2 = MethodDecl(Instance(), Id("main"), [VarDecl(Id("args"), ClassType(Id("Float")), None)], BoolType(), Block([], [if2]))
    #     expect = Program([ClassDecl(Id("Extends"),[method_decl1, method_decl2], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),367))
    
    # def test368(self):
    #     input = """
    #     class Extends extends _0_ {
    #         static _0_(string _0_; kwargs k){ 
    #             int a = 0; b := false;
    #             return a ^ b || 002.01 % 2;
    #         }
    #     }
    #     """
    #     v1 = VarDecl(Id("a"), IntType(), IntLiteral(0))
    #     ass1 = Assign(Id("b"), BooleanLiteral(False))
    #     return1 = Return(BinaryOp("||", BinaryOp("^", Id("a"), Id("b")), BinaryOp("%", FloatLiteral(2.01), IntLiteral(2))))
    #     method_decl = MethodDecl(Static(), Id("<init>"), [VarDecl(Id("_0_"), StringType(), None), VarDecl(Id("k"), ClassType(Id("kwargs")), None)], None, Block([v1], [ass1, return1]))
    #     expect = Program([ClassDecl(Id("Extends"),[method_decl], Id("_0_"))])
    #     self.assertTrue(TestAST.test(input,str(expect),368))
    
    # def test369(self):
    #     input = """
    #     class Main extends ABC{
    #         static int i = x[123.456] + 5;

    #         static float St(string args){
    #             return Break;
    #         }

    #         int main(){
    #             string Continue = 9, Else = 10;
    #             return Continue / Else;
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Static(), VarDecl(Id("i"), IntType(), BinaryOp("+", ArrayCell(Id("x"), FloatLiteral(123.456)), IntLiteral(5))))
    #     method_decl1 = MethodDecl(Static(), Id("St"), [VarDecl(Id("args"), StringType(), None)], FloatType(), Block([], [Return(Id("Break"))]))
    #     v1 = VarDecl(Id("Continue"), StringType(), IntLiteral(9))
    #     v2 = VarDecl(Id("Else"), StringType(), IntLiteral(10))
    #     method_decl2 = MethodDecl(Instance(), Id("main"), [], IntType(), Block([v1, v2], [Return(BinaryOp("/", Id("Continue"), Id("Else")))]))
    #     expect = Program([ClassDecl(Id("Main"),[a1, method_decl1, method_decl2], Id("ABC"))])
    #     self.assertTrue(TestAST.test(input,str(expect),369))
    
    # def test370(self):
    #     input = """
    #     class Main extends ABC{
    #         final int i = _._.o \ (5).x.y;

    #         static float main(string[999] _____){
    #             for k := 1.e-3.x.y downto 2e-5.x.o() do
    #                 io.print("stupid code, haha");
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Instance(), ConstDecl(Id("i"), IntType(), BinaryOp("\\", FieldAccess(FieldAccess(Id("_"), Id("_")), Id("o")), FieldAccess(FieldAccess(IntLiteral(5), Id("x")), Id("y")))))
    #     call1 = CallStmt(Id("io"), Id("print"), [StringLiteral("stupid code, haha")])
    #     for1 = For(Id("k"), FieldAccess(FieldAccess(FloatLiteral(1.e-3), Id("x")), Id("y")), CallExpr(FieldAccess(FloatLiteral(2e-5), Id("x")), Id("o"), []), False, call1)
    #     method_decl = MethodDecl(Static(), Id("main"), [VarDecl(Id("_____"), ArrayType(999, StringType()), None)], FloatType(), Block([], [for1]))
    #     expect = Program([ClassDecl(Id("Main"),[a1, method_decl], Id("ABC"))])
    #     self.assertTrue(TestAST.test(input,str(expect),370))
    
    # def test371(self):
    #     input = """
    #     class main extends Main {
    #         static main(){
    #             boolean flag = false;
    #             int n = cls.f("1", "194") + a[0000] * "blu bla";
    #             if n % 2 == 00001 then
    #                 flag := +True;
    #             {
    #                 n := 9 > (20 >= 6);
    #                 sys.print(n);
    #             }
    #             return flag;
    #         }
    #     }
    #     """
    #     v1 = VarDecl(Id("flag"), BoolType(), BooleanLiteral(False))
    #     v2 = VarDecl(Id("n"), IntType(), BinaryOp("+", CallExpr(Id("cls"), Id("f"), [StringLiteral("1"), StringLiteral("194")]),BinaryOp("*", ArrayCell(Id("a"), IntLiteral(0)), StringLiteral("blu bla"))))
    #     if1 = If(BinaryOp("==" ,BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(1)), Assign(Id("flag"), UnaryOp("+", Id("True"))))
    #     block = Block([], [Assign(Id("n"), BinaryOp(">", IntLiteral(9), BinaryOp(">=", IntLiteral(20), IntLiteral(6)))), CallStmt(Id("sys"), Id("print"), [Id("n")])])
    #     method_decl = MethodDecl(Static(), Id("<init>"), [], None, Block([v1, v2], [if1, block, Return(Id("flag"))]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], Id("Main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),371))
    
    # def test372(self):
    #     input = """
    #     class Example2 extends Example1{
    #             void[2] main(){
    #                 int[3] s = {1,2,3};
    #                 c := a.b().c[6] + 5.3 - 9*2;
    #             }
    #         }
    #     """
    #     v1 = VarDecl(Id("s"), ArrayType(3, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
    #     lhs = BinaryOp("+", ArrayCell(FieldAccess(CallExpr(Id("a"), Id("b"), []), Id("c")), IntLiteral(6)), FloatLiteral(5.3))
    #     rhs = BinaryOp("*", IntLiteral(9), IntLiteral(2))
    #     ass1 = Assign(Id("c"), BinaryOp("-", lhs, rhs))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], ArrayType(2, VoidType()), Block([v1], [ass1]))
    #     expect = Program([ClassDecl(Id("Example2"),[method_decl], Id("Example1"))])
    #     self.assertTrue(TestAST.test(input,str(expect),372))
    
    # def test373(self):
    #     input = """
    #     class ABC {
    #             void main(){
    #                 if 1+1 then a.b();
    #             }
    #         }
    #     """
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), CallStmt(Id("a"), Id("b"), []))]))
    #     expect = Program([ClassDecl(Id("ABC"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),373))
    
    # def test374(self):
    #     input = """
    #     class main extends main{
    #         FLOAT foo(){
    #                 if nil%this then a := x.c.d();
    #             }
    #     }
    #     """
    #     method_decl = MethodDecl(Instance(), Id("foo"), [], ClassType(Id("FLOAT")), Block([], [If(BinaryOp("%", NullLiteral(), SelfLiteral()), Assign(Id("a"), CallExpr(FieldAccess(Id("x"), Id("c")), Id("d"), [])))]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], Id("main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),374))
    
    # def test375(self):
    #     input = """
    #     class main{
    #         string foo(){
    #             return this;
    #         }
    #     }
    #     class main extends main{
    #         boolean a, b, c, d = true, e;
    #     }
    #     """
    #     method_decl1 = MethodDecl(Instance(), Id("foo"), [], StringType(), Block([], [Return(SelfLiteral())]))
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("a"), BoolType(), None))
    #     a2 = AttributeDecl(Instance(), VarDecl(Id("b"), BoolType(), None))
    #     a3 = AttributeDecl(Instance(), VarDecl(Id("c"), BoolType(), None))
    #     a4 = AttributeDecl(Instance(), VarDecl(Id("d"), BoolType(), BooleanLiteral(True)))
    #     a5 = AttributeDecl(Instance(), VarDecl(Id("e"), BoolType(), None))
    #     expect = Program([ClassDecl(Id("main"),[method_decl1], None), ClassDecl(Id("main"),[a1, a2, a3, a4, a5], Id("main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),375))
    
    # def test376(self):
    #     input = """
    #     class main{
            
    #     }

    #     class Main {
    #             static strinG main(){
    #                 if true then {
    #                     x := {true,false,false};
    #                 }
    #             }
    #         }
    #     """
    #     method_decl = MethodDecl(Static(), Id("main"), [], ClassType(Id("strinG")), Block([], [If(BooleanLiteral(True), Block([], [Assign(Id("x"), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(False)]))]), None)]))
    #     expect = Program([ClassDecl(Id("main"),[], None), ClassDecl(Id("Main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),376))
    
    # def test377(self):
    #     input = """
    #     class main{
    #         con1(int p){

    #         }
    #         con2(float p){

    #         }
    #         con3(string p){

    #         }
    #         con4(boolean p){

    #         }
    #         con5(type p){

    #         }
    #         con6(boolean[3] p){

    #         }
    #         con7(void p){

    #         }
    #     }
    #     """
    #     method_decl1 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), IntType(), None)], None, Block([], []))
    #     method_decl2 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), FloatType(), None)], None, Block([], []))
    #     method_decl3 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), StringType(), None)], None, Block([], []))
    #     method_decl4 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), BoolType(), None)], None, Block([], []))
    #     method_decl5 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), ClassType(Id("type")), None)], None, Block([], []))
    #     method_decl6 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), ArrayType(3, BoolType()), None)], None, Block([], []))
    #     method_decl7 = MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("p"), VoidType(), None)], None, Block([], []))
    #     expect = Program([ClassDecl(Id("main"),[method_decl1, method_decl2, method_decl3, method_decl4, method_decl5, method_decl6, method_decl7], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),377))
    
    # def test378(self):
    #     input = """
    #     class main{
    #         boolean a="str", b=1e9, c=0, d = true, e;
            
    #     }
    #     """
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("a"), BoolType(), StringLiteral("str")))
    #     a2 = AttributeDecl(Instance(), VarDecl(Id("b"), BoolType(), FloatLiteral(1e9)))
    #     a3 = AttributeDecl(Instance(), VarDecl(Id("c"), BoolType(), IntLiteral(0)))
    #     a4 = AttributeDecl(Instance(), VarDecl(Id("d"), BoolType(), BooleanLiteral(True)))
    #     a5 = AttributeDecl(Instance(), VarDecl(Id("e"), BoolType(), None))
    #     expect = Program([ClassDecl(Id("main"),[a1, a2, a3, a4, a5], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),378))
    
    # def test379(self):
    #     input = """
    #     class ABC extends DEF{
    #         void method(){
    #             if 1 then
    #                 inp := f23 + ads[2*10] +  ++++ 2 *f /* "87235jkfgshgsfg $&^# */ ;
    #             else return (1 + "str" - 3.);
    #         }
    #     }
    #     """
    #     ass1 = Assign(Id("inp"), BinaryOp("+", BinaryOp("+", Id("f23"), ArrayCell(Id("ads"), BinaryOp("*", IntLiteral(2), IntLiteral(10)))), BinaryOp("*", UnaryOp("+", UnaryOp("+", UnaryOp("+", UnaryOp("+", IntLiteral(2))))), Id("f"))))
    #     if1 = If(IntLiteral(1), ass1, Return(BinaryOp("-", BinaryOp("+", IntLiteral(1), StringLiteral("str")), FloatLiteral(3.))))
    #     method_decl = MethodDecl(Instance(), Id("method"), [], VoidType(), Block([], [if1]))
    #     expect = Program([ClassDecl(Id("ABC"),[method_decl], Id("DEF"))])
    #     self.assertTrue(TestAST.test(input,str(expect),379))
    
    # def test380(self):
    #     input = """
    #     class Main extends ABC{
    #         void main(){
    #             float a = ----1234 || +++False + -+-+ 22222;
    #             this.print(nil);
    #             b := {{{{"abc"}}}, {123}};
    #         }
    #     }
    #     """
    #     init = BinaryOp("||", UnaryOp("-", UnaryOp("-", UnaryOp("-", UnaryOp("-", IntLiteral(1234))))), BinaryOp("+", UnaryOp("+", UnaryOp("+", UnaryOp("+", Id("False")))), UnaryOp("-", UnaryOp("+", UnaryOp("-", UnaryOp("+", IntLiteral(22222)))))))
    #     v1 = VarDecl(Id("a"), FloatType(), init)
    #     ass1 = Assign(Id("b"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([StringLiteral("abc")])])]), ArrayLiteral([IntLiteral(123)])]))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([v1], [CallStmt(SelfLiteral(), Id("print"), [NullLiteral()]) ,ass1]))
    #     expect = Program([ClassDecl(Id("Main"),[method_decl], Id("ABC"))])
    #     self.assertTrue(TestAST.test(input,str(expect),380))
    
    # def test381(self):
    #     input = """
    #     class Example2 extends Example1{
    #             void[2] main(){
    #                 int[3] s = {this,1.,3};
    #                 c := a.b().c[6] + 5.3 - (this.abc().def);
    #             }
    #         }
    #     """
    #     v1 = VarDecl(Id("s"), ArrayType(3, IntType()), ArrayLiteral([SelfLiteral(), FloatLiteral(1.), IntLiteral(3)]))
    #     lhs = BinaryOp("+", ArrayCell(FieldAccess(CallExpr(Id("a"), Id("b"), []), Id("c")), IntLiteral(6)), FloatLiteral(5.3))
    #     rhs = FieldAccess(CallExpr(SelfLiteral(), Id("abc"), []), Id("def"))
    #     ass1 = Assign(Id("c"), BinaryOp("-", lhs, rhs))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], ArrayType(2, VoidType()), Block([v1], [ass1]))
    #     expect = Program([ClassDecl(Id("Example2"),[method_decl], Id("Example1"))])
    #     self.assertTrue(TestAST.test(input,str(expect),381))
    
    # def test382(self):
    #     input = """
    #     class main extends Main {
    #         static main(){
    #             boolean flag = false;
    #             Int[3] n = cls.f("1", "194") + a[0010] * "blu bla".abc;
    #             if n % 2 == 00001 then
    #                 flag := +True;
    #             {
    #                 n := "Abc" > (20 >= 6 % this);
    #                 sys.print(n);
    #             }
    #             return flag;
    #         }
    #     }
    #     """
    #     v1 = VarDecl(Id("flag"), BoolType(), BooleanLiteral(False))
    #     v2 = VarDecl(Id("n"), ArrayType(3, ClassType(Id("Int"))), BinaryOp("+", CallExpr(Id("cls"), Id("f"), [StringLiteral("1"), StringLiteral("194")]),BinaryOp("*", ArrayCell(Id("a"), IntLiteral(10)), FieldAccess(StringLiteral("blu bla"), Id("abc")))))
    #     if1 = If(BinaryOp("==" ,BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(1)), Assign(Id("flag"), UnaryOp("+", Id("True"))))
    #     block = Block([], [Assign(Id("n"), BinaryOp(">", StringLiteral("Abc"), BinaryOp(">=", IntLiteral(20), BinaryOp("%", IntLiteral(6), SelfLiteral())))), CallStmt(Id("sys"), Id("print"), [Id("n")])])
    #     method_decl = MethodDecl(Static(), Id("<init>"), [], None, Block([v1, v2], [if1, block, Return(Id("flag"))]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], Id("Main"))])
    #     self.assertTrue(TestAST.test(input,str(expect),382))
    
    # def test383(self):
    #     input = """
    #     class _{
    #         False(){

    #         }

    #         static main(){
    #             boolean[5] flag = {false, true};
    #             Int[3] n = cls.f("1", "194") + a[0010] * "blu bla".abc;
    #             if n % 2 == 00001 then
    #                 flag := +True;
    #             {
    #                 n := "Abc" > (20 >= 6 % this);
    #                 sys.print(n);
    #             }
    #             return nil;
    #         }
    #     }
    #     """
    #     v1 = VarDecl(Id("flag"), ArrayType(5, BoolType()), ArrayLiteral([BooleanLiteral(False), BooleanLiteral(True)]))
    #     v2 = VarDecl(Id("n"), ArrayType(3, ClassType(Id("Int"))), BinaryOp("+", CallExpr(Id("cls"), Id("f"), [StringLiteral("1"), StringLiteral("194")]),BinaryOp("*", ArrayCell(Id("a"), IntLiteral(10)), FieldAccess(StringLiteral("blu bla"), Id("abc")))))
    #     if1 = If(BinaryOp("==" ,BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(1)), Assign(Id("flag"), UnaryOp("+", Id("True"))))
    #     block = Block([], [Assign(Id("n"), BinaryOp(">", StringLiteral("Abc"), BinaryOp(">=", IntLiteral(20), BinaryOp("%", IntLiteral(6), SelfLiteral())))), CallStmt(Id("sys"), Id("print"), [Id("n")])])
    #     method_decl = MethodDecl(Static(), Id("<init>"), [], None, Block([v1, v2], [if1, block, Return(NullLiteral())]))
    #     method_decl1 = MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))
    #     expect = Program([ClassDecl(Id("_"),[method_decl1, method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),383))
    
    # def test384(self):
    #     input = """
    #     class BlaBla{
    #         void main(){
    #             if sys.flag then
    #                 sys.print_some_thing();
    #             if !sys.flag then
    #                 sys.print_some_thing_else();
    #         }

    #         init(){

    #         }

    #         int a, b;
    #     }
    #     """
    #     if1 = If(FieldAccess(Id("sys"), Id("flag")), CallStmt(Id("sys"), Id("print_some_thing"), []), None)
    #     if2 = If(UnaryOp("!", FieldAccess(Id("sys"), Id("flag"))), CallStmt(Id("sys"), Id("print_some_thing_else"), []))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [if1, if2]))
    #     method_decl1 = MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), None))
    #     a2 = AttributeDecl(Instance(), VarDecl(Id("b"), IntType(), None))
    #     expect = Program([ClassDecl(Id("BlaBla"),[method_decl, method_decl1, a1, a2], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),384))
    
    # def test385(self):
    #     input = """
    #     class Class{
    #         final boolean flag = true && false;
    #         static boolean main(int[5][10] arr){
    #             if arr[3 - "abc"._ + ABC.foo(2.e-5)] <= sys.a[0] + 4 then
    #                 return flag;
    #             else return !flag;
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Instance(), ConstDecl(Id("flag"), BoolType(), BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False))))
    #     if_exp = BinaryOp("<=", ArrayCell(Id("arr"), BinaryOp("+", BinaryOp("-", IntLiteral(3), FieldAccess(StringLiteral("abc"), Id("_"))), CallExpr(Id("ABC"), Id("foo"), [FloatLiteral(2.e-5)]))), BinaryOp("+", ArrayCell(FieldAccess(Id("sys"), Id("a")), IntLiteral(0)), IntLiteral(4)))
    #     then_stmt = Return(Id("flag"))
    #     else_stmt = Return(UnaryOp("!", Id("flag")))
    #     block = Block([], [If(if_exp, then_stmt, else_stmt)])
    #     method_decl = MethodDecl(Static(), Id("main"), [VarDecl(Id("arr"), ArrayType(10, ArrayType(5, IntType())))], BoolType(), block)
    #     expect = Program([ClassDecl(Id("Class"),[a1, method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),385))
    
    # def test386(self):
    #     input = """
    #     class main{
    #         __init__(){
    #             final int x = sys.call(new Obj());
    #             sys.print("init");
    #         }
    #         static Num a = new Num().x.y;
    #     }
    #     """
    #     c1 = ConstDecl(Id("x"), IntType(), CallExpr(Id("sys"), Id("call"), [NewExpr(Id("Obj"), [])]))
    #     block = Block([c1], [CallStmt(Id("sys"), Id("print"), [StringLiteral("init")])])
    #     method_decl = MethodDecl(Instance(), Id("<init>"), [], None, block)
    #     a1 = AttributeDecl(Static(), VarDecl(Id("a"), ClassType(Id("Num")), FieldAccess(FieldAccess(NewExpr(Id("Num"), []), Id("x")), Id("y"))))
    #     expect = Program([ClassDecl(Id("main"), [method_decl, a1], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),386))
    
    # def test387(self):
    #     input = """
    #     class main{
    #         __init__(){
    #             final int x = sys.call(new Obj());
    #             sys.print("init");
    #         }
    #         string a = new Num().x.y.z(this.x == nil);
    #     }
    #     """
    #     c1 = ConstDecl(Id("x"), IntType(), CallExpr(Id("sys"), Id("call"), [NewExpr(Id("Obj"), [])]))
    #     block = Block([c1], [CallStmt(Id("sys"), Id("print"), [StringLiteral("init")])])
    #     method_decl = MethodDecl(Instance(), Id("<init>"), [], None, block)
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("a"), StringType(), CallExpr(FieldAccess(FieldAccess(NewExpr(Id("Num"), []), Id("x")), Id("y")), Id("z"), [BinaryOp("==", FieldAccess(SelfLiteral(), Id("x")), NullLiteral())])))
    #     expect = Program([ClassDecl(Id("main"), [method_decl, a1], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),387))
    
    # def test388(self):
    #     input = """
    #     class Example2 {
    #             void main(){
    #                 for i := 1 to 100 do {
    #                     io.writeIntLn(i);
    #                     Intarray[i] := i + 1;
    #                 }
    #                 break;
    #                 continue;
    #             }
    #         }
    #     """
    #     call1 = CallStmt(Id("io"), Id("writeIntLn"), [Id("i")])
    #     ass1 = Assign(ArrayCell(Id("Intarray"), Id("i")), BinaryOp("+", Id("i"), IntLiteral(1)))
    #     for1 = For(Id("i"), IntLiteral(1), IntLiteral(100), True, Block([], [call1, ass1]))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [for1, Break(), Continue()]))
    #     expect = Program([ClassDecl(Id("Example2"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),388))
    
    # def test389(self):
    #     input = """
    #     class Example2 {
    #             void main(){
    #                 for i := 1 downto 100 do {
    #                     {
    #                         {
    #                             {
    #                                 io.writeIntLn(i);
    #                                 Intarray[i] := i + 1;
    #                             }
    #                         }
    #                     }
    #                 }
    #                 break;
    #                 continue;
    #             }
    #         }
    #     """
    #     call1 = CallStmt(Id("io"), Id("writeIntLn"), [Id("i")])
    #     ass1 = Assign(ArrayCell(Id("Intarray"), Id("i")), BinaryOp("+", Id("i"), IntLiteral(1)))
    #     for1 = For(Id("i"), IntLiteral(1), IntLiteral(100), False, Block([], [Block([], [Block([], [Block([], [call1, ass1])])])]))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [for1, Break(), Continue()]))
    #     expect = Program([ClassDecl(Id("Example2"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),389))
    
    # def test390(self):
    #     input = """
    #     class main{
    #         string method(){
    #             {
    #                 {
    #                     {
    #                         {
    #                             sys.print_some_thing(nil, {this, nil});
    #                             i := ++i;
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     call1 = CallStmt(Id("sys"), Id("print_some_thing"), [NullLiteral(), ArrayLiteral([SelfLiteral(), NullLiteral()])])
    #     ass1 = Assign(Id("i"), UnaryOp("+", UnaryOp("+", Id("i"))))
    #     method_decl = MethodDecl(Instance(), Id("method"), [], StringType(), Block([], [Block([], [Block([], [Block([], [Block([], [call1, ass1])])])])]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),390))
    
    # def test391(self):
    #     input = """
    #     class main{
    #         void[3] x = 2 - 3[0] - 4.E-5 + 123 + ((f.f(nil) < this) || true) * 24 % (2.0 != 22);
    #     }
    #     """
    #     lhs = BinaryOp("+", BinaryOp("-", BinaryOp("-", IntLiteral(2), ArrayCell(IntLiteral(3), IntLiteral(0))), FloatLiteral(4.E-5)), IntLiteral(123))
    #     rhs = BinaryOp("%", BinaryOp("*", BinaryOp("||", BinaryOp("<", CallExpr(Id("f"), Id("f"), [NullLiteral()]), SelfLiteral()), BooleanLiteral(True)), IntLiteral(24)), BinaryOp("!=", FloatLiteral(2.0), IntLiteral(22)))
    #     init = BinaryOp("+", lhs, rhs)
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("x"), ArrayType(3, VoidType()), init))
    #     expect = Program([ClassDecl(Id("main"),[a1], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),391))
    
    # def test392(self):
    #     input = """
    #     class main{
    #         static void call(){
    #             for i := 0.0 to this.len(row) do
    #             for j := this.len(col) downto 0 do
    #                 result[i + j] := row[i] * col[j];
    #         }
    #     }
    #     """
    #     lhs = ArrayCell(Id("result"), BinaryOp("+", Id("i"), Id("j")))
    #     rhs = BinaryOp("*", ArrayCell(Id("row"), Id("i")), ArrayCell(Id("col"), Id("j")))
    #     ass1 = Assign(lhs, rhs)
    #     for2 = For(Id("j"), CallExpr(SelfLiteral(), Id("len"), [Id("col")]), IntLiteral(0), False, ass1)
    #     for1 = For(Id("i"), FloatLiteral(0.0), CallExpr(SelfLiteral(), Id("len"), [Id("row")]), True, for2)
    #     method_decl = MethodDecl(Static(), Id("call"), [], VoidType(), Block([], [for1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),392))
    
    # def test393(self):
    #     input = """
    #     class main{
    #         boolean func(){
    #             call.sub(n, 1, i + 1);
    #             im := call.coverted(____.read("path", "w"), ____type);
    #             (b[this\\false])[nil] := (im[1]).att;
    #         }
    #     }
    #     """
    #     call1 = CallStmt(Id("call"), Id("sub"), [Id("n"), IntLiteral(1), BinaryOp("+", Id("i"), IntLiteral(1))])
    #     ass1 = Assign(Id("im"), CallExpr(Id("call"), Id("coverted"), [CallExpr(Id("____"), Id("read"), [StringLiteral("path"), StringLiteral("w")]), Id("____type")]))
    #     ass2 = Assign(ArrayCell(ArrayCell(Id("b"), BinaryOp("\\", SelfLiteral(), BooleanLiteral(False))), NullLiteral()), FieldAccess(ArrayCell(Id("im"), IntLiteral(1)), Id("att")))
    #     method_decl = MethodDecl(Instance(), Id("func"), [], BoolType(), Block([], [call1, ass1, ass2]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),393))
    
    # def test394(self):
    #     input = """
    #     class main{
    #         static float calc(){
    #             return "dasd" * asd  - {1,2,3} || 82 == false;
    #         }

    #         int x;
    #     }
    #     """
    #     return1 = Return(BinaryOp('==',BinaryOp('||',BinaryOp('-',BinaryOp('*',StringLiteral("""dasd"""),Id('asd')),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),IntLiteral(82)),BooleanLiteral(False)))
    #     method_decl = MethodDecl(Static(), Id("calc"), [], FloatType(), Block([], [return1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl, AttributeDecl(Instance(), VarDecl(Id("x"), IntType(), None))], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),394))
    
    # def test395(self):
    #     input = """
    #     class main{
    #         Class c = {"abc", {1, 2e3}};
            
    #         Class call(boolean a){
    #             if x && 1 == 0 then
    #             return True;
    #         }
    #     }
    #     """
    #     a1 = AttributeDecl(Instance(), VarDecl(Id("c"), ClassType(Id("Class")), ArrayLiteral([StringLiteral("abc"), ArrayLiteral([IntLiteral(1), FloatLiteral(2e3)])])))
    #     if1 = If(BinaryOp("==", BinaryOp("&&", Id("x"), IntLiteral(1)), IntLiteral(0)), Return(Id("True")), None)
    #     method_decl = MethodDecl(Instance(), Id("call"), [VarDecl(Id("a"), BoolType(), None)], ClassType(Id("Class")), Block([], [if1]))
    #     expect = Program([ClassDecl(Id("main"),[a1, method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),395))
    
    # def test396(self):
    #     input = """
    #     class main{
    #         int call(){
    #             s := io.input();
    #             if s.len() == 0 then
    #                 continue;
    #             arr[arr + i] := str.append(str.split(arr, " "));
    #         }
    #     }
    #     """
    #     ass1 = Assign(Id("s"), CallExpr(Id("io"), Id("input"), []))
    #     if1 = If(BinaryOp("==", CallExpr(Id("s"), Id("len"), []), IntLiteral(0)), Continue(), None)
    #     ass2 = Assign(ArrayCell(Id("arr"), BinaryOp("+", Id("arr"), Id("i"))), CallExpr(Id("str"), Id("append"), [CallExpr(Id("str"), Id("split"), [Id("arr"), StringLiteral(" ")])]))
    #     method_decl = MethodDecl(Instance(), Id("call"), [], IntType(), Block([], [ass1, if1, ass2]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),396))
    
    # def test397(self):
    #     input = """
    #     class main{
    #         int main(){
    #             l := str.split(str, " ");
    #             if !l then io.print("empty string");
    #             return convert2.array(l);
    #         }
    #     }
    #     """
    #     ass1 = Assign(Id("l"), CallExpr(Id("str"), Id("split"), [Id("str"), StringLiteral(" ")]))
    #     if1 = If(UnaryOp("!", Id("l")), CallStmt(Id("io"), Id("print"), [StringLiteral("empty string")]), None)
    #     return1 = Return(CallExpr(Id("convert2"), Id("array"), [Id("l")]))
    #     method_decl = MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [ass1, if1, return1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),397))
    
    # def test398(self):
    #     input = """
    #     class main{
    #         string foo(){
    #             sys.rand();
    #             sys.sleep(num.random(num.randint(max) % 1e10));
    #             return num * num;
    #         }
    #     }

    #     """
    #     call1 = CallStmt(Id("sys"), Id("rand"), [])
    #     call2 = CallStmt(Id("sys"), Id("sleep"), [CallExpr(Id("num"), Id("random"), [BinaryOp("%", CallExpr(Id("num"), Id("randint"), [Id("max")]), FloatLiteral(1e10))])])
    #     return1 = Return(BinaryOp("*", Id("num"), Id("num")))
    #     method_decl = MethodDecl(Instance(), Id("foo"), [], StringType(), Block([], [call1, call2, return1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),398))
    
    # def test399(self):
    #     input = """
    #     class main{
    #         float call(){
    #             if sum <= theta then
    #             return math.mean(math.square(y - call.fn(x)), "mean") \ 2;
    #             else
    #             return theta * math.abs(y - math.fn(x)) - theta * theta \ 2;
    #         }
    #     }
    #     """
    #     call1 = CallExpr(Id("math"), Id("mean"), [CallExpr(Id("math"), Id("square"), [BinaryOp("-", Id("y"), CallExpr(Id("call"), Id("fn"), [Id("x")]))]), StringLiteral("mean")])
    #     return1 = Return(BinaryOp("\\", call1, IntLiteral(2)))
    #     lhs = BinaryOp("*", Id("theta"), CallExpr(Id("math"), Id("abs"), [BinaryOp("-", Id("y"), CallExpr(Id("math"), Id("fn"), [Id("x")]))]))
    #     rhs = BinaryOp("\\", BinaryOp("*", Id("theta"), Id("theta")), IntLiteral(2))
    #     return2 = Return(BinaryOp("-", lhs, rhs))
    #     if1 = If(BinaryOp("<=", Id("sum"), Id("theta")), return1, return2)
    #     method_decl = MethodDecl(Instance(), Id("call"), [], FloatType(), Block([], [if1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),399))
    
    # def test400(self):
    #     input = """
    #     class main{
    #         int doo(){
    #             if a.len() != b.len() then 
    #                 sys.raise(error);
    #             for i := a.len() downto 0 do
    #                 sum := sum + (a[i] - b[i]) * (a[i] - b[i]);
    #         }
    #     }
    #     """
    #     if1 = If(BinaryOp("!=", CallExpr(Id("a"), Id("len"), []), CallExpr(Id("b"), Id("len"), [])), CallStmt(Id("sys"), Id("raise"), [Id("error")]))
    #     rhs = BinaryOp("+", Id("sum"), BinaryOp("*", BinaryOp("-", ArrayCell(Id("a"), Id("i")), ArrayCell(Id("b"), Id("i"))), BinaryOp("-", ArrayCell(Id("a"), Id("i")), ArrayCell(Id("b"), Id("i"))))) 
    #     ass1 = Assign(Id("sum"), rhs)
    #     for1 = For(Id("i"), CallExpr(Id("a"), Id("len"), []), IntLiteral(0), False, ass1)
    #     method_decl = MethodDecl(Instance(), Id("doo"), [], IntType(), Block([], [if1, for1]))
    #     expect = Program([ClassDecl(Id("main"),[method_decl], None)])
    #     self.assertTrue(TestAST.test(input,str(expect),400))
    def test351(self):
        input = """
            class Rectangle extends Node {
                void name(){
                    s := 1+2-(3*4)/5;
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id("Rectangle"),
                [
                    MethodDecl(
                        Instance(),
                        Id("name"),
                        [],
                        VoidType(),
                        Block(
                            [],
                            [
                            Assign(
                                Id("s"),
                                BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),
                                BinaryOp("/",
                                BinaryOp("*",IntLiteral(3),IntLiteral(4)),IntLiteral(5)
                                )))
                            ]
                        )
                    )
                ],
                Id("Node")
            )
        ]))

        self.assertTrue(TestAST.test(input,expect,351))

    def test352(self):
        input = """
        class CALL_STMT{
            void main(){
                this.print(1, {1, "this.b"});  
            }
        }
        """
        expect = str(Program([ClassDecl(Id('CALL_STMT'),[MethodDecl(name=Id('main'),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[CallStmt(obj=SelfLiteral(),method=Id('print'),param=[IntLiteral(1),ArrayLiteral([IntLiteral(1),StringLiteral('"this.b"')])])]))])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_program23(self):
        """program"""
        input = \
            """
class f extends S
{
  boolean[2] n =
    !+L.G () ^ + +A.x / !- - - -+ + +this +
    ! ! !this ^ +this ^ - -+I %
    !-this ^ !this.JK ^ ! !this ^ !this ^ ! !+-this ^ this %
    this ^ ! ! ! !this.XiszVEt ().u.Hr ().K ().O
    && this.L % new eQ ().d () ^ new nA ().q % new FLI () >=
    + +-this ^ -this ^ !+ +nil ^ !this.Y.VOf ().XTnyWWghD
    || -A \\ - -+this ^ ! !nil ^ Q - +- -new V () ^ +-+this ^ !this - !-this
    || this / 9E-81 +
    + +this.oMC () ^ ! !nil ^ ! ! ! ! ! !this \\ !-+- -this %
    this ^ ! ! !+ +-nil || !+-"`2*\ta=".N9 () ^ !-+this % !this ^ K
    && f ^ ! !this, k;
}

        """
        expect = str(Program([ClassDecl(Id("f"),[AttributeDecl(Instance(),VarDecl(Id("n"),ArrayType(2,BoolType()),BinaryOp(">=",BinaryOp("&&",BinaryOp("+",BinaryOp("/",BinaryOp("^",UnaryOp("!",UnaryOp("+",CallExpr(Id("L"),Id("G"),[]))),UnaryOp("+",UnaryOp("+",FieldAccess(Id("A"),Id("x"))))),UnaryOp("!",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("+",UnaryOp("+",UnaryOp("+",SelfLiteral()))))))))),BinaryOp("%",BinaryOp("%",BinaryOp("^",BinaryOp("^",UnaryOp("!",UnaryOp("!",UnaryOp("!",SelfLiteral()))),UnaryOp("+",SelfLiteral())),UnaryOp("-",UnaryOp("-",UnaryOp("+",Id("I"))))),BinaryOp("^",BinaryOp("^",BinaryOp("^",BinaryOp("^",BinaryOp("^",UnaryOp("!",UnaryOp("-",SelfLiteral())),UnaryOp("!",FieldAccess(SelfLiteral(),Id("JK")))),UnaryOp("!",UnaryOp("!",SelfLiteral()))),UnaryOp("!",SelfLiteral())),UnaryOp("!",UnaryOp("!",UnaryOp("+",UnaryOp("-",SelfLiteral()))))),SelfLiteral())),BinaryOp("^",SelfLiteral(),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",FieldAccess(CallExpr(CallExpr(FieldAccess(CallExpr(SelfLiteral(),Id("XiszVEt"),[]),Id("u")),Id("Hr"),[]),Id("K"),[]),Id("O"))))))))),BinaryOp("%",BinaryOp("%",FieldAccess(SelfLiteral(),Id("L")),BinaryOp("^",CallExpr(NewExpr(Id("eQ"),[]),Id("d"),[]),FieldAccess(NewExpr(Id("nA"),[]),Id("q")))),NewExpr(Id("FLI"),[]))),BinaryOp("&&",BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("^",BinaryOp("^",BinaryOp("^",UnaryOp("+",UnaryOp("+",UnaryOp("-",SelfLiteral()))),UnaryOp("-",SelfLiteral())),UnaryOp("!",UnaryOp("+",UnaryOp("+",NullLiteral())))),UnaryOp("!",FieldAccess(CallExpr(FieldAccess(SelfLiteral(),Id("Y")),Id("VOf"),[]),Id("XTnyWWghD")))),BinaryOp("-",BinaryOp("-",BinaryOp("\\",UnaryOp("-",Id("A")),BinaryOp("^",BinaryOp("^",UnaryOp("-",UnaryOp("-",UnaryOp("+",SelfLiteral()))),UnaryOp("!",UnaryOp("!",NullLiteral()))),Id("Q"))),BinaryOp("^",BinaryOp("^",UnaryOp("+",UnaryOp("-",UnaryOp("-",NewExpr(Id("V"),[])))),UnaryOp("+",UnaryOp("-",UnaryOp("+",SelfLiteral())))),UnaryOp("!",SelfLiteral()))),UnaryOp("!",UnaryOp("-",SelfLiteral())))),BinaryOp("+",BinaryOp("/",SelfLiteral(),FloatLiteral(9e-81)),BinaryOp("%",BinaryOp("\\",BinaryOp("^",BinaryOp("^",UnaryOp("+",UnaryOp("+",CallExpr(SelfLiteral(),Id("oMC"),[]))),UnaryOp("!",UnaryOp("!",NullLiteral()))),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",SelfLiteral()))))))),UnaryOp("!",UnaryOp("-",UnaryOp("+",UnaryOp("-",UnaryOp("-",SelfLiteral())))))),BinaryOp("^",SelfLiteral(),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("+",UnaryOp("+",UnaryOp("-",NullLiteral())))))))))),BinaryOp("%",BinaryOp("^",UnaryOp("!",UnaryOp("+",UnaryOp("-",CallExpr(StringLiteral('"`2*\ta="'),Id("N9"),[])))),UnaryOp("!",UnaryOp("-",UnaryOp("+",SelfLiteral())))),BinaryOp("^",UnaryOp("!",SelfLiteral()),Id("K")))),BinaryOp("^",Id("f"),UnaryOp("!",UnaryOp("!",SelfLiteral()))))))),AttributeDecl(Instance(),VarDecl(Id("k"),ArrayType(2,BoolType())))],Id("S"))]))
        self.assertTrue(TestAST.test(input, expect, 323))
    
