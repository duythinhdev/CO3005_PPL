from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import * 
from AST import *



class Utilities:
    @staticmethod
    def isOpForInt(operator):
        return operator in ['+', '-', '*', '/', '\\', '%']
    
    @staticmethod
    def isOpForFloat(operator):
        return operator in ['+', '-', '*', '/']

    @staticmethod
    def isOpForBoolean(operator):
        return operator in ['!=', '==', '!', '&&','||']

    @staticmethod
    def isOpForIntToBoolean(operator):
        return operator in ['<', '==', '>', '!=', '>=', '<=']

    @staticmethod
    def isOpForFloatToBoolean(operator):
        return operator in ['<', '>', '>=', '<=']
    
    @staticmethod
    def isOpForNumber(operator): 
        return operator in ['+', '-', '*', '/', '\\', '%','<', '==', '>', '!=', '>=', '<=']
 
    @staticmethod
    def mergeType(lType, rType):
        if type(lType) == IntType and type(rType) == IntType:
            return IntType(),'both'
        elif type(lType) == FloatType and type(rType) == FloatType:
            return FloatType(),'both'
        elif type(lType) == BoolType:
            return BoolType(),'both'
        elif type(lType) == IntType and type(rType) == FloatType:
            return FloatType(),'left'
        elif type(lType) == FloatType and type(rType) == IntType:
            return FloatType(),'right'
        else:
            return StringType(),'both'



class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

from Emitter import Emitter

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast,path):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl,path)
        gc.visit(ast, None)



class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env,path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i,c)for i in ast.decl]
        return c

    def visitClassDecl(self,ast,c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), c, Frame("<init>", VoidType() ))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl:MethodDecl, o, frame:Frame):
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = consdecl.returnType
        methodName = consdecl.name.name 
        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.typ,consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, type(consdecl.kind) is Static,frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if consdecl.name.name == '<init>':
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0,StringType()), frame.getStartLabel(), frame.getEndLabel(),frame))
        else:
            local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            glenv = local.sym+glenv
        
        body = consdecl.body
        'TODO'
        'visit local var and statement and generate their jasmin code here'
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if consdecl.name.name == '<init>':
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitCallStmt(self, ast, o):
        pass


    def visitIf(self, ast: If, o: SubBody):
        pass
  
    def visitFor(self, ast: For, o: SubBody):
        pass





    def visitBreak(self, ast: Break, o: SubBody):
        ctxt = o
        frame:Frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        ctxt = o
        frame:Frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

# ================   Visit Expression   =================
# Param:    o: Access(frame, sym, isLeft, isFirst)
# Return:   (code, type)

    def visitBinaryOp(self, ast:BinaryOp, o):
        # int op + - * / < <= > >= == != \ %
        # float op + - * / < <= > >=
        # bool op == != ! && ||
        # string op ^
        e1c,e1t = self.visit(ast.left,o)
        e2c,e2t = self.visit(ast.right,o)
        mtype, pos = Utilities.mergeType(e1t, e2t)
        if type(mtype) is IntType:
            if ast.op in ['+','-']:
                return e1c + e2c + self.emit.emitADDOP(ast.op, mtype, o.frame), mtype
            elif ast.op == '*':
                return e1c + e2c + self.emit.emitMULOP(ast.op, mtype, o.frame), mtype
            elif ast.op == '/':
                e1c += self.emit.emitI2F(o.frame)
                e2c += self.emit.emitI2F(o.frame)
                mtype = FloatType()
                return e1c + e2c + self.emit.emitMULOP(ast.op, mtype, o.frame), mtype
            elif ast.op == '\\':
                return e1c + e2c + self.emit.emitDIV(mtype, o.frame), mtype
            elif ast.op == '%':
                return e1c + e2c + self.emit.emitMOD(mtype, o.frame), mtype
            elif ast.op in ['<','<=','>','>=','==','!=']:
                return e1c + e2c + self.emit.emitRELOP(ast.op, mtype, o.frame), BoolType()
        elif type(mtype) is FloatType:
            if pos == 'left':
                e1c += self.emit.emitI2F(o.frame)
            elif pos == 'right':
                e2c += self.emit.emitI2F(o.frame)
            if ast.op in ['+','-']:
                return e1c + e2c + self.emit.emitADDOP(ast.op, mtype, o.frame), mtype
            elif ast.op in ['*','/']:
                return e1c + e2c + self.emit.emitMULOP(ast.op, mtype, o.frame), mtype
            elif ast.op in ['<','<=','>','>=']:
                return e1c + e2c + self.emit.emitRELOP(ast.op, mtype, o.frame), BoolType()
        elif type(mtype) is BoolType:
            return e1c + e2c + self.emit.emitRELOP(ast.op, mtype, o.frame), BoolType()
        elif type(mtype) is StringType:
            'TODO'
            pass
    
    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op).lower()
        bCode, bType = self.visit(ast.body, ctxt)
        if op == '-': return bCode + self.emit.emitNEGOP(bType, frame), bType
        if op == '!': return bCode + self.emit.emitNOT(bType, frame), bType

    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()