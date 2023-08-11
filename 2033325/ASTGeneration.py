from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

class ASTGeneration(BKOOLVisitor):
    
    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.class_declare()])


    # Visit a parse tree produced by BKOOLParser#class_declare.
    def visitClass_declare(self, ctx:BKOOLParser.Class_declareContext):
        class_name = Id(ctx.ID(0).getText())
        mem_list = []
        if(ctx.members().__len__()> 0):
            mem_list = reduce(lambda acc,ele:acc + self.visit(ele),ctx.members(),[])
        if ctx.EXTENDS():
            parent_name = Id(ctx.ID(1).getText())
            return ClassDecl(class_name,mem_list,parent_name)
        return ClassDecl(class_name, mem_list)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        if ctx.getChildCount() == 0: return
        a = self.visit(ctx.getChild(0))
        return a


    # Visit a parse tree produced by BKOOLParser#attribute_declare.
    def visitAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by BKOOLParser#mutable_declare.
    def visitMutable_declare(self, ctx:BKOOLParser.Mutable_declareContext):
        type_attribute = self.visit(ctx.type_attribute())
        list_var = [self.visit(i) for i in ctx.var_declare()]
        if ctx.STATIC():
            return [AttributeDecl(Static(),VarDecl(i[0], type_attribute, i[1])) for i in list_var]
        return [AttributeDecl(Instance(),VarDecl(i[0], type_attribute, i[1])) for i in list_var]


    # Visit a parse tree produced by BKOOLParser#immutable_declare.
    def visitImmutable_declare(self, ctx:BKOOLParser.Immutable_declareContext):
        type_attribute = self.visit(ctx.type_attribute())
        list_var = [self.visit(i) for i in ctx.var_declare()]
        if ctx.STATIC():
            return [AttributeDecl(Static(),ConstDecl(i[0], type_attribute, i[1])) for i in list_var]
        return [AttributeDecl(Instance(),ConstDecl(i[0], type_attribute, i[1])) for i in list_var]


    # Visit a parse tree produced by BKOOLParser#method_declare.
    def visitMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        return_type = self.visit(ctx.return_type())
        list_param = self.visit(ctx.list_params())
        block_stmt = self.visit(ctx.block_statement())
        if ctx.STATIC():
            return [MethodDecl(Static(),Id(ctx.ID().getText()),list_param,return_type,block_stmt)]
        return [MethodDecl(Instance(), Id(ctx.ID().getText()), list_param, return_type, block_stmt)]

    # Visit a parse tree produced by BKOOLParser#constructor_declare.
    def visitConstructor_declare(self, ctx:BKOOLParser.Constructor_declareContext):
        if ctx.STATIC():
            return [MethodDecl(Static(),Id("<init>"),self.visit(ctx.list_params()),None,self.visit(ctx.block_statement()))]
        return [MethodDecl(Instance(),Id("<init>"),self.visit(ctx.list_params()),None,self.visit(ctx.block_statement()))]


    # Visit a parse tree produced by BKOOLParser#var_declare.
    def visitVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        if ctx.exp():
            return Id(ctx.ID().getText()), self.visit(ctx.exp())
        return Id(ctx.ID().getText()), None


    # Visit a parse tree produced by BKOOLParser#list_params.
    def visitList_params(self, ctx:BKOOLParser.List_paramsContext):
        if ctx.getChildCount() == 0:
            return []
        list_params = []
        for i in ctx.parameter():
            list_params += self.visit(i)
        return list_params


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        type_of_params = self.visit(ctx.parameter_type())
        return [VarDecl(Id(i.getText()),type_of_params) for i in ctx.ID()]


    # Visit a parse tree produced by BKOOLParser#parameter_type.
    def visitParameter_type(self, ctx:BKOOLParser.Parameter_typeContext):
        return self.visit(ctx.type_attribute())


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by BKOOLParser#type_attribute.
    def visitType_attribute(self, ctx:BKOOLParser.Type_attributeContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        type_arr = self.visit(ctx.primitive_type()) if ctx.primitive_type() else self.visit(ctx.class_type())
        return ArrayType(size=int(ctx.INTEGER_LIT().getText()),eleType=type_arr)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        return VoidType()


    # Visit a parse tree produced by BKOOLParser#block_statement.
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        if len(ctx.local_attribute()) > 0:
            local_att = reduce(lambda acc,ele: acc + self.visit(ele),ctx.local_attribute(),[])
            return Block(local_att,[self.visit(i) for i in ctx.statement()])
        return Block([],[self.visit(i) for i in ctx.statement()])


    # Visit a parse tree produced by BKOOLParser#local_attribute.
    def visitLocal_attribute(self, ctx:BKOOLParser.Local_attributeContext):
        type_of_var = self.visit(ctx.type_attribute())
        # visit list of var declare immu/not immu should return list of tuple of (id, value)
        if ctx.FINAL():
            list_var = [self.visit(i) for i in ctx.var_declare()]
            return [ConstDecl(i[0],type_of_var,i[1]) for i in list_var]
        list_var = [self.visit(i) for i in ctx.var_declare()]
        return [VarDecl(i[0], type_of_var, i[1]) for i in list_var]

    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by BKOOLParser#assignment_satement.
    def visitAssignment_statement(self, ctx:BKOOLParser.Assignment_statementContext):
        return Assign(self.visit(ctx.lhs()),self.visit(ctx.exp()))


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.operands()),self.visit(ctx.index_represent()))
        return FieldAccess(self.visit(ctx.prefix_attribute_invo()),Id(ctx.ID().getText()))


    # Visit a parse tree produced by BKOOLParser#prefix_attribute_invo.
    def visitPrefix_attribute_invo(self, ctx:BKOOLParser.Prefix_attribute_invoContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            return SelfLiteral()
        if ctx.ROUND_OPEN():
            return self.visit(ctx.exp())
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.prefix_attribute_invo()),self.visit(ctx.index_represent()))
        if ctx.getChildCount() == 3:
            return FieldAccess(obj=self.visit(ctx.prefix_attribute_invo()),fieldname=Id(ctx.ID().getText()))
        obj_invo = self.visit(ctx.prefix_attribute_invo())
        method = Id(ctx.ID().getText())
        return CallExpr(obj=obj_invo,method=method,param=self.visit(ctx.list_args_wrapped()))



    # Visit a parse tree produced by BKOOLParser#if_statement.
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        exp = self.visit(ctx.bool_exp())
        stm1 = self.visit(ctx.statement(0))
        if not ctx.ELSE():
            return If(expr=exp,thenStmt=stm1)
        stm2 = self.visit(ctx.statement(1))
        return If(expr=exp, thenStmt=stm1,elseStmt=stm2)

    # Visit a parse tree produced by BKOOLParser#for_statement.
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        scala_var = Id(ctx.ID().getText())
        loop = self.visit(ctx.statement())
        up = True if ctx.TO() else False
        expr1 = self.visit(ctx.int_exp()[0])
        expr2 = self.visit(ctx.int_exp()[1])
        return For(scala_var,expr1,expr2,up,loop)

    # Visit a parse tree produced by BKOOLParser#break_statement.
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by BKOOLParser#continue_statement.
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return Return(self.visit(ctx.return_exp()))

    # Visit a parse tree produced by BKOOLParser#method_invo_statement.
    def visitMethod_invo_statement(self, ctx:BKOOLParser.Method_invo_statementContext):
        obj = self.visit(ctx.obj_methodInvo())
        name = Id(ctx.ID().getText())
        arguments = self.visit(ctx.list_args_wrapped())
        return CallStmt(obj,name,arguments)

    def visitObj_methodInvo(self, ctx:BKOOLParser.Obj_methodInvoContext):
        if ctx.getChildCount() == 1:
            if ctx.literals():
                return self.visit(ctx.literals())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.THIS():
                return SelfLiteral()
            elif ctx.NIL():
                return NullLiteral()
        elif ctx.ROUND_OPEN():
            return self.visit(ctx.exp())
        elif ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.operands()), self.visit(ctx.index_represent()))
        obj = self.visit(ctx.operands())
        name_f_i = Id(ctx.ID().getText())  # field or id
        if not ctx.list_args_wrapped():
            # if field access
            return FieldAccess(obj, name_f_i)
        return CallExpr(obj, name_f_i, self.visit(ctx.list_args_wrapped()))

    # Visit a parse tree produced by BKOOLParser#bool_exp.
    def visitBool_exp(self, ctx:BKOOLParser.Bool_expContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by BKOOLParser#int_exp.
    def visitInt_exp(self, ctx:BKOOLParser.Int_expContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by BKOOLParser#return_exp.
    def visitReturn_exp(self, ctx:BKOOLParser.Return_expContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        if ctx.LT():
            return BinaryOp(ctx.LT().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LTE():
            return BinaryOp(ctx.LTE().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        return BinaryOp(ctx.GTE().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))

    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx: BKOOLParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        return BinaryOp(ctx.NEQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp2(self, ctx: BKOOLParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))

    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.FLOAT_DIV():
            return BinaryOp(ctx.FLOAT_DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.INT_DIV():
            return BinaryOp(ctx.INT_DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))

    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))

    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        exp_of_unary = self.visit(ctx.exp6())
        return UnaryOp('!', exp_of_unary)

    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        exp_of_unary = self.visit(ctx.exp7())
        if ctx.ADD():
            return UnaryOp('+', exp_of_unary)
        return UnaryOp('-', exp_of_unary)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        if ctx.getChildCount() == 1:
            if ctx.literals():
                return self.visit(ctx.literals())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.THIS():
                return SelfLiteral()
            elif ctx.NIL():
                return NullLiteral()
            return self.visit(ctx.obj_create())
        elif ctx.ROUND_OPEN():
            return self.visit(ctx.exp())
        elif ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.operands()),self.visit(ctx.index_represent()))
        obj = self.visit(ctx.operands())
        name_f_i = Id(ctx.ID().getText())  # field or id
        if not ctx.list_args_wrapped():
            # if field access
            return FieldAccess(obj,name_f_i)
        return CallExpr(obj,name_f_i,self.visit(ctx.list_args_wrapped()))



    # Visit a parse tree produced by BKOOLParser#index_represent.
    def visitIndex_represent(self, ctx:BKOOLParser.Index_representContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by BKOOLParser#obj_create.
    def visitObj_create(self, ctx:BKOOLParser.Obj_createContext):
        return NewExpr(Id(ctx.ID().getText()),self.visit(ctx.list_args_wrapped()))


    # Visit a parse tree produced by BKOOLParser#list_args_wrapped.
    def visitList_args_wrapped(self, ctx:BKOOLParser.List_args_wrappedContext):
        return self.visit(ctx.list_exps_as_args())


    # Visit a parse tree produced by BKOOLParser#list_exps_as_args.
    def visitList_exps_as_args(self, ctx:BKOOLParser.List_exps_as_argsContext):
        # return list of expr in parameter
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(i) for i in ctx.exp()]


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visit(ctx.getChild(0))


    def visitBoolean_literal(self, ctx:BKOOLParser.Boolean_literalContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        return BooleanLiteral(False)


    # Visit a parse tree produced by BKOOLParser#array_literal.
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        list_replica = [self.visit(i) for i in ctx.literal_replica()]
        return ArrayLiteral(list_replica)


    # Visit a parse tree produced by BKOOLParser#literal_replica.
    def visitLiteral_replica(self, ctx:BKOOLParser.Literal_replicaContext):
        if ctx.INTEGER_LIT():
            return IntLiteral(int(ctx.INTEGER_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        return self.visitBoolean_literal(ctx.boolean_literal())
