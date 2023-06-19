import unittest
from TestUtils import *
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_SC401(self):
        input = Program([
            VarDecl("x", AutoType()),
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_SC402(self):
        input = Program([
            VarDecl("x", IntegerType(), IntegerLit(1)),
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_SC403(self):
        input = Program([
            VarDecl("x", IntegerType(), IntegerLit(1))
        ])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_SC404(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
            f[4.3] = 1;
        }"""
        expect = "Type mismatch in expression: ArrayCell(f, [FloatLit(4.3)])"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_SC405(self):
        input = Program([VarDecl("a", IntegerType()),
                        VarDecl("c", FloatType())])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_SC406(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_SC407(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function float(){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_SC408(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function void(x: auto){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_SC409(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_SC410(self):
        input = """
        foo: function void() inherit ain{
            super(14,1);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function auto(){        
        }"""
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_SC411(self):
        input = """
        foo: function void() inherit ain{
            super(1);        
        }
        ain:function void ( y: integer) {
            f: array[3] of float;
        }
        main: function auto(){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_SC412(self):
        input = """
        foo: function void(){
            super(1);        
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(super, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_SC413(self):
        input = """
        foo: function void(){
            in(1.2, 1);        
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Undeclared Function: in"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_SC414(self):
        input = """
        foo: function void(){
            ain(1.2, 1, "");        
        }
        ain:function void (inherit x: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(ain, FloatLit(1.2), IntegerLit(1), StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_SC415(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4};        
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_SC416(self):
        input = """
        foo: function void() inherit ain{
            super(1);
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){
        }"""
        expect = "Redeclared Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_SC417(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,3},{4,5,6}}};
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_SC418(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_SC419(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,"34"},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(34)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_SC420(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6","7"}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([StringLit(1), StringLit(2), StringLit(34)]), ArrayLit([StringLit(4), StringLit(5), StringLit(6), StringLit(7)])])])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_SC421(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[1,2,2] = "1";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_SC422(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,e,r] = "1";
        }"""
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_SC423(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,f,r] = "1";
        }"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), Id(f), Id(r)])"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_SC424(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1] = "1";
        }"""
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(g, [Id(x), IntegerLit(1)]), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_SC425(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            super(10);
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), IntegerLit(1), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_SC426(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_SC427(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            //preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_SC428(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            //preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_SC429(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            super("!");
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
        }
        foo: function float(inherit x: float){}"""
        expect = "Type mismatch in expression: StringLit(!)"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_SC430(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x == "1") x = 1;            
        }
        foo: function float(){}"""
        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_SC431(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{"1","2","34"},{"4","5","6"}}};            
        }
        foo: function float(){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(g, ArrayType([1, 2, 3], IntegerType), ArrayLit([ArrayLit([ArrayLit([StringLit(1), StringLit(2), StringLit(34)]), ArrayLit([StringLit(4), StringLit(5), StringLit(6)])])]))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_SC432(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,3},{4,3,2}}};
            if (x >= 1) x = 1;            
        }
        foo: function float(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_SC432(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x :: "1") x = 1;            
        }
        foo: function float(){}"""
        expect = "Type mismatch in statement: IfStmt(BinExpr(::, Id(x), StringLit(1)), AssignStmt(Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_SC433(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            preventDefault(1);
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x :: "1") x = 1;
        }
        foo: function float(){}"""
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_SC434(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        foo: function float(x: integer){
            main(1);
        }"""
        expect = "Type mismatch in statement: CallStmt(main, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_SC435(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        foo: function float(x: integer){
            main();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_SC436(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                printInteger(x);
            } while (bar() > 0);
        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_SC437(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                printInteger(x);
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_SC438(self):
        input = """
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                x = printInteger();
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = "Type mismatch in expression: FuncCall(printInteger, [])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_SC439(self):
        input = """
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                x = boo();
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_SC440(self):
        input = """
        pool: function void() inherit foo{}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            for (i = 0, i < 10, i + 1){
                pool();
                i = pool();
            }
        }"""
        expect = "Invalid statement in function: pool"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_SC441(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i < 10, i + 1){
                pool(1);
            }
        }"""
        expect = "Type mismatch in statement: CallStmt(pool, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_SC442(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i < 10, i + 1){
                i = pool();
            }
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(i), FuncCall(pool, []))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_SC443(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i != -10, i == 1){
                i = pool();
            }
        }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), UnExpr(-, IntegerLit(0))), BinExpr(!=, Id(i), UnExpr(-, IntegerLit(10))), BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), FuncCall(pool, []))]))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_SC444(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            while ( x < 10) return x+1;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_SC445(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            while(boo()>0) continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            while ( x < 10) break;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_SC446(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            while(boo()>0) continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            break;
        }"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_SC447(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            break;
        }"""
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_SC448(self):
        input = """
        pool: function void() inherit foo{
            super(1);
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            return "";
        }"""
        expect = "Type mismatch in statement: ReturnStmt(StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_SC449(self):
        input = """
        pool: function void() inherit foo{
            super(1);
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            if(x == 1) return 1;
            return "";
            return "ashjdgkf";
        }"""
        expect = "Type mismatch in statement: ReturnStmt(StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_SC450(self):
        input = """
        f:array[1,2,3] of float;
        g: array[1,2,3] of integer = f;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(g, ArrayType([1, 2, 3], IntegerType), Id(f))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_SC451(self):
        input = """
        f:array[1,2,3] of integer;
        g: array[1,2,3] of float = f;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_SC452(self):
        input = """
        x: integer = 3;
        foo1: function void( x:float,inherit y: string){}
        foo2: function auto(){return 2.3;}
        main:function void () {
            n: integer;
            x,y,z: float;
            {
                {

                }
                x = n;
            }
            if((x<y) && (y < 9) && (z != 10)) z = 456;
            else z = 34576;
            foo1(2.3,"abc");
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_SC453(self):
        input = """
        main:function void () {}
        poo: function void(n: auto) {
            n = 1;
            if(n>0) n = n + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_SC454(self):
        input = """
        poo: function auto(n: auto) {
            n = 1;
            if(n>0) n = n + 1;
        }
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_SC455(self):
        input = """
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_SC456(self):
        input = """
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        boo: function void(){
            if (poo("1") < 10){
                printInteger(poo(1));
            }
        }
        """
        expect = "Type mismatch in expression: FuncCall(poo, [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_SC457(self):
        input = """
        main:function void () {
            x: integer = 1;
            hehe(poo(""),"");
        }
        hehe: function float(x: integer, y : string){}
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        boo: function void(){
            if (poo("1") < 10){
                printInteger(poo(1));
            }
        }
        """
        expect = "Type mismatch in expression: BinExpr(>, Id(n), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_SC458(self):
        input = """
        main:function void () {
        }
        hehe: function float(x: integer, y : string){
            x = 1;
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_SC459(self):
        input = """
        main:function void () {
        }
        hehe: function float(inherit x: integer, y : string) inherit aaa{
            super(3);
            b = 1;
        }
        aaa: function float(inherit a: integer) inherit bbb{
            super(2,1);
            b = 1;
        }
        bbb: function float(inherit b: integer, inherit c: float){
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_SC460(self):
        input = """
        main:function void () {
        }
        hehe: function float(inherit x: integer, y : string) inherit aaa{
            super(3);
            b = 1;
        }
        aaa: function float(inherit a: integer) inherit bbb{
            super(2,1);
            b = 1;
        }
        bbb: function float(inherit b: integer, inherit b: float){
            
        }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_SC461(self):
        input = """
        main:function void () {
        }
        hehe: function float(inherit x: integer, y : string) inherit aaa{
            super(3);
            b = 1;
        }
        aaa: function float(inherit c: integer) inherit bbb{
            super(2,1);
            b = 1;
        }
        bbb: function float(inherit b: integer, inherit c: float){
            
        }
        """
        expect = "Invalid Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_SC462(self):
        input = """
        main:function void () {
        }
        hehe: function float(inherit c: integer, y : string) inherit aaa{
            super(3);
            b = 1;
        }
        aaa: function float(inherit a: integer) inherit bbb{
            super(2,1);
            b = 1;
        }
        bbb: function float(inherit b: integer, inherit c: float){
            
        }
        """
        expect = "Invalid Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_SC463(self):
        input = """
        g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
        foo: function auto(){return 1;}
        main: function void() {
            g[1,foo(),2] = "1";
            if(foo() > 1) return 1;
            return 2.1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_SC464(self):
        input = """
        g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
        foo: function auto(){}
        main: function void() {
            g[1,foo(),2] = "1";
            if(foo() > 1) return 1;
            return 2.1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_SC465(self):
        input = """
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

        main: function void () {
            printInteger(4);
        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_SC466(self):
        input = """
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
        bar: function void(){}
        main: function void () inherit foo {
            super(1, 1.2);
            printInteger(4);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_SC466(self):
        input = """
        foo: function void (inherit a: auto, inherit out b: auto) inherit bar {}
        bar: function void(){}
        main: function void () inherit foo {
            super(1, 1.2);
            printInteger(4);
            a = 1;
            b = 1.2;
            if (b > a){
                printInteger(4);
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_SC467(self):
        input = """
        foo: function void (inherit a: auto, inherit out b: auto) inherit bar {}
        bar: function void(){}
        main: function void () inherit foo {
            super(1, 1.2);
            printInteger(4);
            a = 1;
            b = 1.2;
            if (a + b){
                printInteger(4);
            }
        }"""
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(a), Id(b)), BlockStmt([CallStmt(printInteger, IntegerLit(4))]))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_SC468(self):
        input = """
        foo: function void (inherit a: auto, inherit out b: auto) inherit bar {}
        bar: function void(){}
        main: function void () inherit foo {
            super(1, 1.2);
            printInteger(4);
            foo(true,false);
            if (a == b){
                printBoolean(a);
            }
        }"""
        expect = "Type mismatch in statement: CallStmt(foo, BooleanLit(True), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_SC469(self):
        input = """
        a : float = 1 ;
        b : float = a + 2 ;
        c : integer = 2.3 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_SC470(self):
        input = """
        a : auto = 10;
        b : auto = " h e l l o " ;
        c : auto = a < 100;
        main: function void(){
            if (c) return 1;
            else return 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_SC471(self):
        input = """
        main: function void(a: auto){
            if (a < 1.2) return 1;
            
            a = 13;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_SC472(self):
        input = """
        main: function integer(a: auto){
            if (a < 1.2){
                return 1.3;
                if (a < 1.2){
                    if (a < 1.2){
                        if (a < 1.2){
                            if (a < 1.2){
                                if (a < 1.2){
                                    if (a < 1.2){
                                        return 1.2;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.3))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_SC473(self):
        input = """
        main: function integer(a: auto){
            if (a < 1.2){
                return 1;
                if (a < 1.2){
                    if (a < 1.2){
                        if (a < 1.2){
                            if (a < 1.2){
                                if (a < 1.2){
                                    if (a < 1.2){
                                        return 1.2;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return 13214.124;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_SC474(self):
        input = """
        main: function integer(a: auto){
            if (a < 1.2){
                return 1;
                if (a < 1.2){
                    if (a < 1.2){
                        if (a < 1.2){
                            if (a < 1.2){
                                if (a < 1.2){
                                    if (a < 1.2){
                                        return 1.2;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return 13214.124;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_SC475(self):
        input = """
            main: function void(){}
            foo: function auto(){}
            c: function integer (x: auto){
                a: integer = 1 + foo();
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_SC476(self):
        input = """
            main: function void(){}
            foo: function auto(){}
            c: function integer (x: auto){
                a: integer = 1.3 + foo();
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(1.3), FuncCall(foo, [])))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_SC477(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            //preventDefault();
            x = 1;
        }
        """
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_SC478(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            preventDefault();
            x = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_SC479(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(1.2);
            x = 1;
        }
        """
        expect = "Type mismatch in expression: FloatLit(1.2)"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_SC480(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = "1";
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_SC481(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: integer;
            x: float = x;
        }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_SC482(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: float = x;
        }
        foo2: function void() {}
        """
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_SC483(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        g: array[5] of float = {1,2,3,4,5}; 
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: float = x;
            g[x] = 1;
        }
        foo2: function void() {}
        """
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_SC484(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        g: array[5] of float = {1,2,3,4,5}; 
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: float = x;
            g[f[3,1,1]] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_SC485(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        g: array[5] of float = {1,2,3,4,5}; 
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: float = x;
            g[f[3,1,foo2(1)]] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_SC486(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        g: array[5] of integer = {1,2,3,4,5}; 
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x = 1;
            x: float = x;
            g[f[g[g[1]],1,foo2(1)]] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_SC487(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
        g: array[5] of integer = {1,2,3,4,5}; 
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2);
        foo2: function integer(b:auto){}
        foo3: function auto(){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            g[f[g[g[1+foo2(foo3()+x)]],1,foo2(1)]] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_SC488(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4.5}, {5}}};
        g: array[5] of integer = {1,2,3,4,5};
        h: array[2] of float;
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2.1);
        foo2: function integer(b:auto){}
        foo3: function auto(){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x,r,t: auto = 1, {3,12}, 1-2.e13;
            g[f[g[g[1+foo2(foo3()+x)]],1,foo2(1)]] = 1;
            //r = h;
        }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(1)])]), ArrayLit([ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(1)])]), ArrayLit([ArrayLit([FloatLit(4.5)]), ArrayLit([IntegerLit(5)])])])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_SC489(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{45}, {5}}};
        g: array[5] of integer = {1,2,3,4,5};
        h: array[2] of float;
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2.1);
        foo2: function integer(b:auto){}
        foo3: function auto(){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x,r,t: auto = 1, {3,12}, 1-2.e13;
            h[1,1] = r[1,1];
            r[3,4] = h[5,6];
        }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(h, [IntegerLit(1), IntegerLit(1)]), ArrayCell(r, [IntegerLit(1), IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_SC490(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{45}, {5}}};
        g: array[5] of integer = {1,2,3,4,5};
        h: array[2] of float;
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2.1);
        foo2: function integer(b:auto){}
        foo3: function auto(){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x,r,t: auto = 1, {3,12}, 1-2.e13;
            h[1] = r[11];
            r[3] = h[5];
        }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(r, [IntegerLit(3)]), ArrayCell(h, [IntegerLit(5)]))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_SC491(self):
        input = """
        f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{45}, {5}}};
        g: array[5] of integer = {1,2,3,4,5};
        h: array[2] of float;
        foo1: function void( x:float,inherit y: string){}
        x: auto = foo2(2.1);
        foo2: function integer(b:auto){}
        foo3: function auto(){}
        main: function void() inherit foo2{
            super(f[1,2,1]);
            x,r,t: auto = 1, {30,12}, 1-2.e13;
            h[1] = r[11];
            r[3] = h[5];
        }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(r, [IntegerLit(3)]), ArrayCell(h, [IntegerLit(5)]))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_SC492(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                cse = cse + 1;
                continue;
            } while (x <= 10);
        }
        """
        expect = "Type mismatch in expression: BinExpr(+, Id(cse), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_SC493(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        str: function void (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                cse = cse + 1;
                continue;
            } while (x <= 10);
        }
        """
        expect = "Type mismatch in expression: BinExpr(::, StringLit(CSE = ), FuncCall(str, [Id(cse)]))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_SC493(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        str: function void (s: string){}
        main2: function void() {
            continue;
            do {
                printString("CSE = " :: str(cse));
                cse = cse + 1;
                continue;
            } while (x <= 10);
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_SC494(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = 1, 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                cse = cse :: "1";
                continue;
            } while (x <= 10);
        }
        main: function boolean(){
            return (a + b) < (c + d); 
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_SC495(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = "1", 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                cse = cse :: "1";
                continue;
            } while (x <= 10);
        }
        main: function boolean(){
            return (a + b) < (c + d); 
        }
        """
        expect = "Type mismatch in expression: BinExpr(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_SC495(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = 1, 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                cse =  a + b ;
                continue;
            } while (x <= 10);
        }
        main: function boolean(){
            return (a + b) < (c + d); 
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(cse), BinExpr(+, Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_SC496(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = 1, 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                b =  a / c ;
                d = a % b;
                break;
            } while (x <= 10);
        }
        main: function void(){
            return (a + b) < (c + d); 
        }
        """
        expect = "Type mismatch in expression: BinExpr(%, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_SC497(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = 1, 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                b =  a / c ;
                d = a % d;
                break;
            } while (x <= 10);
        }
        main: function void(){
            return (a + b) < (c + d); 
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_SC497(self):
        input = """
        x,r,t, cse: auto = 1, {3,12}, 1-2.e13, "";
        a,b,c,d: auto = 1, 2.0, 3.0, 4;
        str: function string (s: string){}
        main2: function void() {
            do {
                printString("CSE = " :: str(cse));
                b =  a / c ;
                d = a % d;
                break;
            } while (x <= 10);
        }
        main: function integer(){
            return -a; 
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_SC498(self):
        input = Program([
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_SC499(self):
        input = """
        x: auto = foo2(2);
        //foo1: function void( x:float,inherit y: string){}
        foo2: function integer(b:auto){}
        foo:function void(t: integer, q : float){
            //super(1.2 , "12");
            r: float = 3.2;
            //r = foo2(r);
            r = readFloat();
            f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
            //y = "1";

            //x = readInteger();
        }
        main:function void () {
            foo(1,1.2);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_SC500(self):
        input = """
        x: auto = foo2(2);
        foo1: function void( x:float,inherit y: string){}
        foo2: function integer(b:auto){}
        foo:function void(t: integer, q : float) inherit foo1{
            super(1.2 , "12");
            r: float = 3.2;
            r = readFloat();
            f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
            y = "1";
            x = readInteger();
        }
        main:function void () {
            foo(1,1.2);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
