# Generated from D:/4yrs/ppl/assignment/assignment 1/assignment1/src/main/bkool/parser\BKOOL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_declare.
    def visitClass_declare(self, ctx:BKOOLParser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_declare.
    def visitAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#field.
    def visitField(self, ctx:BKOOLParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_declare.
    def visitMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor_declare.
    def visitConstructor_declare(self, ctx:BKOOLParser.Constructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_declare.
    def visitVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_params.
    def visitList_params(self, ctx:BKOOLParser.List_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter_type.
    def visitParameter_type(self, ctx:BKOOLParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_attribute.
    def visitType_attribute(self, ctx:BKOOLParser.Type_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_statement.
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_var_declare.
    def visitBlock_var_declare(self, ctx:BKOOLParser.Block_var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_satement.
    def visitAssignment_satement(self, ctx:BKOOLParser.Assignment_satementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_statement.
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_statement.
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#loop_block_statement.
    def visitLoop_block_statement(self, ctx:BKOOLParser.Loop_block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_statement.
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_statement.
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo_statement.
    def visitMethod_invo_statement(self, ctx:BKOOLParser.Method_invo_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#prefix_method_invo.
    def visitPrefix_method_invo(self, ctx:BKOOLParser.Prefix_method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_exp.
    def visitBool_exp(self, ctx:BKOOLParser.Bool_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_exp.
    def visitInt_exp(self, ctx:BKOOLParser.Int_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_exp.
    def visitReturn_exp(self, ctx:BKOOLParser.Return_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_represent.
    def visitIndex_represent(self, ctx:BKOOLParser.Index_representContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_create.
    def visitObj_create(self, ctx:BKOOLParser.Obj_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_args_wrapped.
    def visitList_args_wrapped(self, ctx:BKOOLParser.List_args_wrappedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_exps_as_args.
    def visitList_exps_as_args(self, ctx:BKOOLParser.List_exps_as_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#boolean_literal.
    def visitBoolean_literal(self, ctx:BKOOLParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_literal.
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        return self.visitChildren(ctx)



del BKOOLParser