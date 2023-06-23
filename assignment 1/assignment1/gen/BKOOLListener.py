# Generated from D:/4yrs/ppl/assignment/assignment 1/assignment1/src/main/bkool/parser\BKOOL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete listener for a parse tree produced by BKOOLParser.
class BKOOLListener(ParseTreeListener):

    # Enter a parse tree produced by BKOOLParser#program.
    def enterProgram(self, ctx:BKOOLParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKOOLParser#program.
    def exitProgram(self, ctx:BKOOLParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKOOLParser#class_declare.
    def enterClass_declare(self, ctx:BKOOLParser.Class_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#class_declare.
    def exitClass_declare(self, ctx:BKOOLParser.Class_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#members.
    def enterMembers(self, ctx:BKOOLParser.MembersContext):
        pass

    # Exit a parse tree produced by BKOOLParser#members.
    def exitMembers(self, ctx:BKOOLParser.MembersContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attribute_declare.
    def enterAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attribute_declare.
    def exitAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#field.
    def enterField(self, ctx:BKOOLParser.FieldContext):
        pass

    # Exit a parse tree produced by BKOOLParser#field.
    def exitField(self, ctx:BKOOLParser.FieldContext):
        pass


    # Enter a parse tree produced by BKOOLParser#method_declare.
    def enterMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#method_declare.
    def exitMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#constructor_declare.
    def enterConstructor_declare(self, ctx:BKOOLParser.Constructor_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#constructor_declare.
    def exitConstructor_declare(self, ctx:BKOOLParser.Constructor_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#var_declare.
    def enterVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#var_declare.
    def exitVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#list_params.
    def enterList_params(self, ctx:BKOOLParser.List_paramsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#list_params.
    def exitList_params(self, ctx:BKOOLParser.List_paramsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#parameter.
    def enterParameter(self, ctx:BKOOLParser.ParameterContext):
        pass

    # Exit a parse tree produced by BKOOLParser#parameter.
    def exitParameter(self, ctx:BKOOLParser.ParameterContext):
        pass


    # Enter a parse tree produced by BKOOLParser#parameter_type.
    def enterParameter_type(self, ctx:BKOOLParser.Parameter_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#parameter_type.
    def exitParameter_type(self, ctx:BKOOLParser.Parameter_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#return_type.
    def enterReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#return_type.
    def exitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#type_attribute.
    def enterType_attribute(self, ctx:BKOOLParser.Type_attributeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#type_attribute.
    def exitType_attribute(self, ctx:BKOOLParser.Type_attributeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#array_type.
    def enterArray_type(self, ctx:BKOOLParser.Array_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#array_type.
    def exitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#class_type.
    def enterClass_type(self, ctx:BKOOLParser.Class_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#class_type.
    def exitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#primitive_type.
    def enterPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#primitive_type.
    def exitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#block_statement.
    def enterBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#block_statement.
    def exitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#block_var_declare.
    def enterBlock_var_declare(self, ctx:BKOOLParser.Block_var_declareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#block_var_declare.
    def exitBlock_var_declare(self, ctx:BKOOLParser.Block_var_declareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#statement.
    def enterStatement(self, ctx:BKOOLParser.StatementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#statement.
    def exitStatement(self, ctx:BKOOLParser.StatementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#assignment_satement.
    def enterAssignment_satement(self, ctx:BKOOLParser.Assignment_satementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#assignment_satement.
    def exitAssignment_satement(self, ctx:BKOOLParser.Assignment_satementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#lhs.
    def enterLhs(self, ctx:BKOOLParser.LhsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#lhs.
    def exitLhs(self, ctx:BKOOLParser.LhsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#if_statement.
    def enterIf_statement(self, ctx:BKOOLParser.If_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#if_statement.
    def exitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#for_statement.
    def enterFor_statement(self, ctx:BKOOLParser.For_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#for_statement.
    def exitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#loop_block_statement.
    def enterLoop_block_statement(self, ctx:BKOOLParser.Loop_block_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#loop_block_statement.
    def exitLoop_block_statement(self, ctx:BKOOLParser.Loop_block_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#break_statement.
    def enterBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#break_statement.
    def exitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#continue_statement.
    def enterContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#continue_statement.
    def exitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#return_statement.
    def enterReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#return_statement.
    def exitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#method_invo_statement.
    def enterMethod_invo_statement(self, ctx:BKOOLParser.Method_invo_statementContext):
        pass

    # Exit a parse tree produced by BKOOLParser#method_invo_statement.
    def exitMethod_invo_statement(self, ctx:BKOOLParser.Method_invo_statementContext):
        pass


    # Enter a parse tree produced by BKOOLParser#prefix_method_invo.
    def enterPrefix_method_invo(self, ctx:BKOOLParser.Prefix_method_invoContext):
        pass

    # Exit a parse tree produced by BKOOLParser#prefix_method_invo.
    def exitPrefix_method_invo(self, ctx:BKOOLParser.Prefix_method_invoContext):
        pass


    # Enter a parse tree produced by BKOOLParser#bool_exp.
    def enterBool_exp(self, ctx:BKOOLParser.Bool_expContext):
        pass

    # Exit a parse tree produced by BKOOLParser#bool_exp.
    def exitBool_exp(self, ctx:BKOOLParser.Bool_expContext):
        pass


    # Enter a parse tree produced by BKOOLParser#int_exp.
    def enterInt_exp(self, ctx:BKOOLParser.Int_expContext):
        pass

    # Exit a parse tree produced by BKOOLParser#int_exp.
    def exitInt_exp(self, ctx:BKOOLParser.Int_expContext):
        pass


    # Enter a parse tree produced by BKOOLParser#return_exp.
    def enterReturn_exp(self, ctx:BKOOLParser.Return_expContext):
        pass

    # Exit a parse tree produced by BKOOLParser#return_exp.
    def exitReturn_exp(self, ctx:BKOOLParser.Return_expContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp.
    def enterExp(self, ctx:BKOOLParser.ExpContext):
        pass

    # Exit a parse tree produced by BKOOLParser#exp.
    def exitExp(self, ctx:BKOOLParser.ExpContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp1.
    def enterExp1(self, ctx:BKOOLParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp1.
    def exitExp1(self, ctx:BKOOLParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp2.
    def enterExp2(self, ctx:BKOOLParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp2.
    def exitExp2(self, ctx:BKOOLParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp3.
    def enterExp3(self, ctx:BKOOLParser.Exp3Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp3.
    def exitExp3(self, ctx:BKOOLParser.Exp3Context):
        pass


    # Enter a parse tree produced by BKOOLParser#operands.
    def enterOperands(self, ctx:BKOOLParser.OperandsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#operands.
    def exitOperands(self, ctx:BKOOLParser.OperandsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#index_represent.
    def enterIndex_represent(self, ctx:BKOOLParser.Index_representContext):
        pass

    # Exit a parse tree produced by BKOOLParser#index_represent.
    def exitIndex_represent(self, ctx:BKOOLParser.Index_representContext):
        pass


    # Enter a parse tree produced by BKOOLParser#obj_create.
    def enterObj_create(self, ctx:BKOOLParser.Obj_createContext):
        pass

    # Exit a parse tree produced by BKOOLParser#obj_create.
    def exitObj_create(self, ctx:BKOOLParser.Obj_createContext):
        pass


    # Enter a parse tree produced by BKOOLParser#list_args_wrapped.
    def enterList_args_wrapped(self, ctx:BKOOLParser.List_args_wrappedContext):
        pass

    # Exit a parse tree produced by BKOOLParser#list_args_wrapped.
    def exitList_args_wrapped(self, ctx:BKOOLParser.List_args_wrappedContext):
        pass


    # Enter a parse tree produced by BKOOLParser#list_exps_as_args.
    def enterList_exps_as_args(self, ctx:BKOOLParser.List_exps_as_argsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#list_exps_as_args.
    def exitList_exps_as_args(self, ctx:BKOOLParser.List_exps_as_argsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#literals.
    def enterLiterals(self, ctx:BKOOLParser.LiteralsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#literals.
    def exitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#boolean_literal.
    def enterBoolean_literal(self, ctx:BKOOLParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by BKOOLParser#boolean_literal.
    def exitBoolean_literal(self, ctx:BKOOLParser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by BKOOLParser#array_literal.
    def enterArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        pass

    # Exit a parse tree produced by BKOOLParser#array_literal.
    def exitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        pass



del BKOOLParser