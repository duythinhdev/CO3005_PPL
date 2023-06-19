# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDeclList.
    def visitFuncDeclList(self, ctx:MT22Parser.FuncDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDecl.
    def visitFuncDecl(self, ctx:MT22Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variaFuncList.
    def visitVariaFuncList(self, ctx:MT22Parser.VariaFuncListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variaFuncDeclarator.
    def visitVariaFuncDeclarator(self, ctx:MT22Parser.VariaFuncDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variableDeclList.
    def visitVariableDeclList(self, ctx:MT22Parser.VariableDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varia_no_body.
    def visitVaria_no_body(self, ctx:MT22Parser.Varia_no_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varia_yes_body.
    def visitVaria_yes_body(self, ctx:MT22Parser.Varia_yes_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#args.
    def visitArgs(self, ctx:MT22Parser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expList.
    def visitExpList(self, ctx:MT22Parser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeType.
    def visitTypeType(self, ctx:MT22Parser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcType.
    def visitFuncType(self, ctx:MT22Parser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variType.
    def visitVariType(self, ctx:MT22Parser.VariTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assStmt.
    def visitAssStmt(self, ctx:MT22Parser.AssStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx:MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmtbody.
    def visitBlockStmtbody(self, ctx:MT22Parser.BlockStmtbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso.
    def visitEspresso(self, ctx:MT22Parser.EspressoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso1.
    def visitEspresso1(self, ctx:MT22Parser.Espresso1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso2.
    def visitEspresso2(self, ctx:MT22Parser.Espresso2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso3.
    def visitEspresso3(self, ctx:MT22Parser.Espresso3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso4.
    def visitEspresso4(self, ctx:MT22Parser.Espresso4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso5.
    def visitEspresso5(self, ctx:MT22Parser.Espresso5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso6.
    def visitEspresso6(self, ctx:MT22Parser.Espresso6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso7.
    def visitEspresso7(self, ctx:MT22Parser.Espresso7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso8.
    def visitEspresso8(self, ctx:MT22Parser.Espresso8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso10.
    def visitEspresso10(self, ctx:MT22Parser.Espresso10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso11.
    def visitEspresso11(self, ctx:MT22Parser.Espresso11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#espresso12.
    def visitEspresso12(self, ctx:MT22Parser.Espresso12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhsop.
    def visitLhsop(self, ctx:MT22Parser.LhsopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleanlit.
    def visitBooleanlit(self, ctx:MT22Parser.BooleanlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLit.
    def visitArrayLit(self, ctx:MT22Parser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elemArrays.
    def visitElemArrays(self, ctx:MT22Parser.ElemArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elem.
    def visitElem(self, ctx:MT22Parser.ElemContext):
        return self.visitChildren(ctx)



del MT22Parser