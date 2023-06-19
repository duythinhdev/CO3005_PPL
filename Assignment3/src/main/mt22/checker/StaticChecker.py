from Visitor import Visitor
from AST import *
from StaticError import *
from functools import *
from abc import ABC


class MT22SupFunc:
    @staticmethod
    def insert_glo_func(scope):
        scope["readInteger"] = Glo_func([], IntegerType())
        scope["printInteger"] = Glo_func([IntegerType()], VoidType())
        scope["readFloat"] = Glo_func([], FloatType())
        scope["writeFloat"] = Glo_func([FloatType()], VoidType())
        scope["readBoolean"] = Glo_func([], BooleanType())
        scope["printBoolean"] = Glo_func([BooleanType()], VoidType())
        scope["readString"] = Glo_func([], StringType())
        scope["printString"] = Glo_func([StringType()], VoidType())
        scope["super"] = Glo_func([], VoidType())
        scope["preventDefault"] = Glo_func([], VoidType())

    @staticmethod
    def compare(typ1, typ2):
        if type(typ1) == ArrayType and type(typ2) == ArrayType:
            return typ1.dimensions == typ2.dimensions and MT22SupFunc.compare(typ1.typ, typ2.typ)
        elif type(typ1) == FloatType and type(typ2) == IntegerType:
            return True
        elif (type(typ2) in [IntegerType, FloatType, StringType, ArrayType, BooleanType]) and type(typ1) == AutoType:
            typ1 = typ2
            return True
        elif (type(typ1) in [IntegerType, FloatType, StringType, ArrayType, BooleanType]) and type(typ2) == AutoType:
            typ2 = typ1
            return True
        return type(typ1) == type(typ2)

    @staticmethod
    def return_type(type_util):
        if type(type_util) == Variable_op or type(type_util) == Function_op or type(type_util) == Params_op or type(type_util) == Glo_func:
            return type_util.type
        else:
            return type_util


class Function_op:
    def __init__(self, ftype: Type, inherit: str or None):
        self.type = ftype
        self.inherit = inherit
        self.parameter = {}
        self.inheram = []


class Variable_op:
    def __init__(self, var_type: Type, var_init: Expr or None):
        self.type = var_type
        self.init = var_init


class Params_op:
    def __init__(self, typ: Type, out: bool = False, inherit: bool = False):
        self.type = typ
        self.out = out
        self.inherit = inherit


class Glo_func:
    def __init__(self, input_typ: List, return_typ: Type or None):
        self.parameter = input_typ
        self.type = return_typ


class StaticChecker(Visitor):

    def enter_loop(self):
        self.in_loop += 1

    def exit_loop(self):
        self.in_loop -= 1

    def enter_scope(self):
        self.local_index += 1

    def exit_scope(self):
        self.local_index -= 1

    def hierarchical_recur(self, grandma):
        if grandma.inherit != None:
            temp = {}
            return_temp = {}
            return_temp = self.hierarchical_recur(
                self.funclist[grandma.inherit])
            for i in grandma.parameter:
                if grandma.parameter[i].inherit == True:
                    if i in temp:
                        raise Redeclared(Parameter(), i)
                    else:
                        temp[i] = grandma.parameter[i]

            for key, value in return_temp.items():
                try:
                    temp.update({key: value})
                except ValueError:
                    raise Invalid(Parameter(), key)

            return temp
        else:
            temp = {}
            for i in grandma.parameter:
                if grandma.parameter[i].inherit == True:
                    temp[i] = grandma.parameter[i]
            return temp

    def retrieve_inherit(self, parent, child):
        temp = {}
        temp = self.hierarchical_recur(parent)
        child.parameter.update(temp)

        # for i in parent:
        #     if parent[i].inherit == True:
        #         child[i] = parent[i]

    def check_dup_inherit_params(self, parent):
        for i in range(len(parent)):
            for j in range(i+1, len(parent)):
                if parent[i].name == parent[j].name:
                    if parent[i].inherit == parent[j].inherit:
                        if parent[i].inherit == True:
                            raise Redeclared(Parameter(), parent[j].name)

    def convert_func_glo(self, funclist, globalo):
        for key in funclist.keys():
            if globalo[key].type != funclist[key].type:
                globalo[key].type = funclist[key].type

    def check(self):
        return self.visitProgram(self.ast, [])

    def __init__(self, ast):
        self.ast = ast
        self.funclist = {}
        self.varilist = {}
        self.glo_envi = {}
        self.hierarchical = {}
        self.func_flag = False
        self.for_flag = False
        self.array_flag = False
        self.return_flag = False
        self.current = None
        self.array_return = None
        self.array_scope = None
        self.in_loop = 0
        self.local_index = 0

########################## EXPRESSO ##########################

    def visitBinExpr(self, ast: BinExpr, o):
        lhs = MT22SupFunc.return_type(self.visit(ast.left, o))
        rhs = MT22SupFunc.return_type(self.visit(ast.right, o))
        # print(lhs)
        # print(rhs)
        if ast.op in ["+", "-", "*", "/"]:
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType):
                return FloatType() if ast.op == "/" else IntegerType()
            elif ((type(lhs), type(rhs)) == (FloatType, IntegerType)
                  or (type(lhs), type(rhs)) == (IntegerType, FloatType)
                  or (type(lhs), type(rhs)) == (FloatType, FloatType)):
                return FloatType()
            elif type(lhs) == AutoType or type(rhs) == AutoType:
                if type(lhs) == AutoType and type(rhs) in [IntegerType, FloatType]:
                    temp = self.visit(ast.left, o)
                    temp = rhs  # FloatType()
                elif type(rhs) == AutoType and type(lhs) in [IntegerType, FloatType]:
                    temp = self.visit(ast.right, o)
                    temp = lhs  # FloatType()
                return temp
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "%":
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType):
                return IntegerType()
            elif type(lhs) == AutoType or type(rhs) == AutoType:
                if type(lhs) == AutoType and type(rhs) == IntegerType:
                    temp = self.visit(ast.left, o)
                    temp = rhs  # IntegerType()
                elif type(rhs) == AutoType and type(lhs) == IntegerType:
                    temp = self.visit(ast.right, o)
                    temp = lhs  # IntegerType()
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ["&&", "||"]:
            if (type(lhs), type(rhs)) == (BooleanType, BooleanType):
                return BooleanType()
            elif type(lhs) == AutoType or type(rhs) == AutoType:
                if type(lhs) == AutoType and type(rhs) == BooleanType:
                    temp = self.visit(ast.left, o)
                    temp = BooleanType()
                elif type(rhs) == AutoType and type(lhs) == BooleanType:
                    temp = self.visit(ast.right, o)
                    temp = BooleanType()
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "::":
            if (type(lhs), type(rhs)) == (StringType, StringType):
                return StringType()
            elif type(lhs) == AutoType or type(rhs) == AutoType:
                if type(lhs) == AutoType and type(rhs) == StringType:
                    temp = self.visit(ast.left, o)
                    temp = StringType()
                elif type(rhs) == AutoType and type(lhs) == StringType:
                    temp = self.visit(ast.right, o)
                    temp = StringType()
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if ((type(lhs), type(rhs)) == (IntegerType, IntegerType)
                or (type(lhs), type(rhs)) == (FloatType, IntegerType)
                or (type(lhs), type(rhs)) == (IntegerType, FloatType)
                or (type(lhs), type(rhs)) == (FloatType, FloatType)
                or ((type(lhs), type(rhs)) == (BooleanType, BooleanType)
                    and (ast.op in ["==", "!="]))):
                return BooleanType()
            elif type(lhs) == AutoType or type(rhs) == AutoType:
                if type(lhs) == AutoType and type(rhs) in [IntegerType, FloatType, BooleanType]:
                    temp = self.visit(ast.left, o)
                    temp = rhs
                elif type(rhs) == AutoType and type(lhs) in [IntegerType, FloatType, BooleanType]:
                    temp = self.visit(ast.right, o)
                    temp = lhs
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnExpr(self, ast: UnExpr, o):
        val = MT22SupFunc.return_type(self.visit(ast.val, o))
        if ast.op == "-" and type(val) not in [IntegerType, FloatType]:
            if type(val) == AutoType:
                # temp = self.visit(ast.val, o)
                # temp.type = FloatType()
                return self.visit(ast.val, o)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "!" and type(val) != BooleanType:
            if type(val) == AutoType:
                temp = self.visit(ast.val, o)
                temp.type = BooleanType()
                return temp
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return self.visit(ast.val, o)

    def visitId(self, ast: Id, o):
        index = self.local_index
        # if self.for_flag == False:
        if "local" not in o:
            if ast.name not in o["global"]:
                raise Undeclared(Identifier(), ast.name)
            else:
                return o["global"][ast.name]
        else:
            for i in range(index, -1, -1):
                if ast.name in o["local"][i]:
                    return o["local"][i][ast.name]

            if ast.name in o["global"]:
                return o["global"][ast.name]

            raise Undeclared(Identifier(), ast.name)
        # else:
        #     self.visit(VarDecl(ast.name, IntegerType(), None), o)
        #     return o["local"][self.local_index][ast.name]

    def visitArrayCell(self, ast: ArrayCell, o):
        if "local" not in o:
            if ast.name not in o["global"]:
                raise Undeclared(Identifier(), ast.name)
            else:
                return o["global"][ast.name]
        else:
            temp = None
            for i in range(self.local_index, -1, -1):
                if ast.name in o["local"][i]:
                    temp = o["local"][i][ast.name]

            if temp is None:
                if ast.name in o["global"]:
                    temp = o["global"][ast.name]
                else:
                    raise Undeclared(Identifier(), ast.name)

            if type(temp.type) != ArrayType:
                raise TypeMismatchInExpression(ast)

            first_cafe = MT22SupFunc.return_type(self.visit(ast.cell[0], o))

            for cell in ast.cell:
                espresso = self.visit(cell, o)
                if type(MT22SupFunc.return_type(espresso)) != type(first_cafe) or type(first_cafe) != IntegerType or type(MT22SupFunc.return_type(espresso)) != IntegerType:
                    if type(MT22SupFunc.return_type(espresso)) == AutoType:
                        hehe = self.visit(cell, o)
                        hehe.type = IntegerType()
                    else:
                        raise TypeMismatchInExpression(ast)

            if (len(temp.type.dimensions) == len(ast.cell)):
                return temp.type.typ

            return temp

    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def visitArrayLit(self, ast: ArrayLit, o):
        if self.array_flag == False:
            self.array_scope = ast
            array_list = ast.explist
            for i in array_list:
                if not MT22SupFunc.compare(i, array_list[0]):
                    raise IllegalArrayLiteral(ast)

            size = [len(array_list)]

            if type(array_list[0]) == ArrayLit:
                self.array_flag = True
                sub_size, sub_type = self.visit(array_list[0], o)
                for i in array_list:
                    sub_size_1, sub_type_1 = self.visit(i, o)
                    if sub_size != sub_size_1 or type(sub_type) != type(sub_type_1):
                        # if (type(sub_type) == FloatType and type(sub_type_1) == IntegerType) or (type(sub_type) == IntegerType and type(sub_type_1) == FloatType):
                        #     self.array_return = FloatType()
                        # else:
                        raise IllegalArrayLiteral(ast)

                self.array_flag = False
                size += sub_size
            else:
                self.array_return = self.visit(array_list[0], o)

            return ArrayType(size, self.array_return)
        else:
            array_list = ast.explist

            for i in array_list:
                if not MT22SupFunc.compare(i, array_list[0]):
                    raise IllegalArrayLiteral(self.array_scope)

            size = [len(array_list)]
            if type(array_list[0]) == ArrayLit:
                sub_size, sub_type = self.visit(array_list[0], o)

                for i in array_list:
                    sub_size_1, sub_type_1 = self.visit(i, o)

                    if sub_size != sub_size_1 or type(sub_type) != type(sub_type_1):
                        # if (type(sub_type) == FloatType and type(sub_type_1) == IntegerType) or (type(sub_type) == IntegerType and type(sub_type_1) == FloatType):
                        #     self.array_return = FloatType()
                        # else:
                        raise IllegalArrayLiteral(self.array_scope)
                size += sub_size

            else:
                self.array_return = self.visit(array_list[0], o)

            return (size, self.array_return)

    def visitFuncCall(self, ast: FuncCall, o):
        if ast.name != "super":
            glo_envi_call = False
            if ast.name not in self.funclist:
                if ast.name not in self.glo_envi:
                    raise Undeclared(Function(), ast.name)
                else:
                    glo_envi_call = True
                    call_temp = self.glo_envi[ast.name].parameter
            else:
                call_temp = self.funclist[ast.name].parameter

            if len(call_temp) != len(ast.args):
                raise TypeMismatchInExpression(ast)

            param_typ_list = []
            if glo_envi_call == False:
                for key in call_temp:
                    param_typ_list.append(call_temp[key])
            else:
                param_typ_list = call_temp

            for i in range(len(param_typ_list)):
                if glo_envi_call == False:
                    if type(param_typ_list[i].type) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                        if type(param_typ_list[i].type) == FloatType and type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == IntegerType:
                            pass
                        elif type(param_typ_list[i].type) == AutoType:
                            param_typ_list[i].type = MT22SupFunc.return_type(
                                self.visit(ast.args[i], o))
                        elif type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == AutoType:
                            temp = MT22SupFunc.return_type(
                                self.visit(ast.args[i], o))
                            temp = param_typ_list[i].type
                        else:
                            raise TypeMismatchInExpression(ast)
                elif glo_envi_call == True:
                    if type(param_typ_list[i]) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                        raise TypeMismatchInExpression(ast)
            if glo_envi_call == True:
                return self.glo_envi[ast.name]
            else:
                if ast.name in o["global"]:
                    self.convert_func_glo(
                        self.funclist[ast.name].parameter, o["global"][ast.name].parameter)
                    return o["global"][ast.name]
                return self.funclist[ast.name]
        else:
            if o["global"][self.current].inherit != None:
                call_temp = self.funclist[o["global"]
                                          [self.current].inherit].parameter

                param_typ_list = []
                for key in call_temp:
                    param_typ_list.append(call_temp[key].type)

                if len(param_typ_list) == len(ast.args):
                    for i in range(len(param_typ_list)):
                        if type(param_typ_list[i]) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                            raise TypeMismatchInExpression(ast.args[i])
                elif len(param_typ_list) > len(ast.args):
                    raise TypeMismatchInExpression("")
                elif len(param_typ_list) < len(ast.args):
                    raise TypeMismatchInExpression(
                        ast.args[len(param_typ_list)])

                return self.funclist[o["global"][self.current].inherit]
            else:
                raise TypeMismatchInExpression(ast)


########################## STATEMENT ##########################


    def visitAssignStmt(self, ast: AssignStmt, o):
        lhs = MT22SupFunc.return_type(self.visit(ast.lhs, o))
        rhs = MT22SupFunc.return_type(self.visit(ast.rhs, o))
        # if self.for_flag == True:
        #     if type(lhs) == type(rhs):
        #         return lhs
        #     else:
        #         return None
        # print(ast.lhs)
        # print(ast.rhs)
        # print("\n")
        # print(lhs)
        # print(rhs)
        # print("\n")
        # print(type(lhs))
        # print(type(rhs))
        if type(lhs) == ArrayType or type(lhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif (type(lhs) == AutoType) and (type(rhs) != AutoType):
            temp = self.visit(ast.lhs, o)
            temp.type = rhs
        elif (type(lhs) != AutoType) and (type(rhs) == AutoType):
            temp = self.visit(ast.rhs, o)
            temp.type = lhs
        elif not MT22SupFunc.compare(lhs, rhs):
            raise TypeMismatchInStatement(ast)
        elif self.for_flag == True:
            if type(lhs) == type(rhs):
                return lhs
            else:
                return None

    def visitBlockStmt(self, ast: BlockStmt, o):
        self.enter_scope()
        new_o_block = o.copy()
        new_o_block["local"][self.local_index] = {}
        for body in ast.body:
            self.visit(body, new_o_block)

        del new_o_block
        self.exit_scope()

    def visitIfStmt(self, ast: IfStmt, o):
        self.enter_scope()
        new_o_if = o.copy()
        new_o_if["local"][self.local_index] = {}
        condition = MT22SupFunc.return_type(self.visit(ast.cond, new_o_if))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.tstmt, new_o_if)
        if ast.fstmt:
            self.visit(ast.fstmt, new_o_if)

        del new_o_if
        self.exit_scope()

    def visitForStmt(self, ast: ForStmt, o):
        self.enter_loop()
        self.enter_scope()
        self.for_flag = True
        new_o_for = o.copy()
        new_o_for["local"][self.local_index] = {}
        init = self.visit(ast.init, new_o_for)
        self.for_flag = False

        cond = self.visit(ast.cond, new_o_for)
        updt = self.visit(ast.upd, new_o_for)
        if type(updt) != IntegerType or type(init) != IntegerType or type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_for)

        del new_o_for
        self.enter_scope()
        self.exit_loop()

    def visitWhileStmt(self, ast: WhileStmt, o):
        self.enter_loop()
        self.enter_scope()
        new_o_while = o.copy()
        new_o_while["local"][self.local_index] = {}
        condition = MT22SupFunc.return_type(self.visit(ast.cond, new_o_while))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_while)
        del new_o_while
        self.exit_scope()
        self.exit_loop()

    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        self.enter_loop()
        new_o_do_while = o.copy()
        condition = MT22SupFunc.return_type(
            self.visit(ast.cond, new_o_do_while))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_do_while)
        del new_o_do_while
        self.exit_loop()

    def visitBreakStmt(self, ast: BreakStmt, o):
        if self.in_loop == 0:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast: ContinueStmt, o):
        if self.in_loop == 0:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast: ReturnStmt, o):
        if self.local_index == 0:
            if self.return_flag == False:
                new_o_return = o.copy()
                return_type = MT22SupFunc.return_type(self.visit(
                    ast.expr, new_o_return)) if ast.expr else None

                if return_type is not None:
                    if type(o["global"][self.current].type) == FloatType and type(return_type) == IntegerType:
                        pass
                    elif type(o["global"][self.current].type) == VoidType:
                        pass
                    elif type(o["global"][self.current].type) == AutoType:
                        o["global"][self.current].type = return_type
                    elif not MT22SupFunc.compare(o["global"][self.current].type, return_type):
                        raise TypeMismatchInStatement(ast)
                self.return_flag = True
                del new_o_return
            else:
                pass
        else:
            new_o_return = o.copy()
            return_type = MT22SupFunc.return_type(self.visit(
                ast.expr, new_o_return)) if ast.expr else None
            if return_type is not None:
                if type(o["global"][self.current].type) == FloatType and type(return_type) == IntegerType:
                    pass
                elif type(o["global"][self.current].type) == VoidType:
                    pass
                elif type(o["global"][self.current].type) == AutoType:
                    o["global"][self.current].type = return_type
                elif not MT22SupFunc.compare(o["global"][self.current].type, return_type):
                    raise TypeMismatchInStatement(ast)
            del new_o_return

    def visitCallStmt(self, ast: CallStmt, o):
        if ast.name == "super":
            if o["global"][self.current].inherit != None:
                call_temp = self.funclist[o["global"]
                                          [self.current].inherit].parameter

                param_typ_list = []
                for key in call_temp:
                    param_typ_list.append(call_temp[key])

                if len(param_typ_list) == len(ast.args):
                    for i in range(len(param_typ_list)):
                        # print(param_typ_list[i])
                        # print(MT22SupFunc.return_type(self.visit(ast.args[i], o)))
                        if type(param_typ_list[i].type) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                            if type(param_typ_list[i].type) == FloatType and type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == IntegerType:
                                pass
                            elif type(param_typ_list[i].type) == AutoType:
                                param_typ_list[i].type = MT22SupFunc.return_type(
                                    self.visit(ast.args[i], o))
                            elif type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == AutoType:
                                temp = MT22SupFunc.return_type(
                                    self.visit(ast.args[i], o))
                                temp = param_typ_list[i].type
                            else:

                                raise TypeMismatchInExpression(ast.args[i])
                        else:
                            pass
                elif len(param_typ_list) > len(ast.args):
                    raise TypeMismatchInExpression("")
                elif len(param_typ_list) < len(ast.args):
                    raise TypeMismatchInExpression(
                        ast.args[len(param_typ_list)])
            else:
                raise TypeMismatchInStatement(ast)
        elif ast.name == "preventDefault":
            if len(ast.args) > 0:
                raise TypeMismatchInExpression(ast.args[0])
        else:
            if ast.name not in self.funclist:
                if ast.name not in self.glo_envi:
                    raise Undeclared(Function(), ast.name)
                else:
                    glo_envi_call = True
                    call_temp = self.glo_envi[ast.name].parameter
            else:
                glo_envi_call = False
                call_temp = self.funclist[ast.name].parameter

            if len(call_temp) != len(ast.args):
                raise TypeMismatchInStatement(ast)

            param_typ_list = []
            if glo_envi_call == False:
                for key in call_temp:
                    param_typ_list.append(call_temp[key])
            else:
                param_typ_list = call_temp

            for i in range(len(param_typ_list)):
                if glo_envi_call == False:
                    if type(param_typ_list[i].type) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                        if type(param_typ_list[i].type) == FloatType and type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == IntegerType:
                            pass
                        elif type(param_typ_list[i].type) == AutoType:
                            param_typ_list[i].type = MT22SupFunc.return_type(
                                self.visit(ast.args[i], o))
                        elif type(MT22SupFunc.return_type(self.visit(ast.args[i], o))) == AutoType:
                            temp = MT22SupFunc.return_type(
                                self.visit(ast.args[i], o))
                            temp = param_typ_list[i].type
                        else:
                            raise TypeMismatchInStatement(ast)
                    else:
                        pass
                else:
                    if type(param_typ_list[i]) != type(MT22SupFunc.return_type(self.visit(ast.args[i], o))):
                        raise TypeMismatchInStatement(ast)

########################## DECL ##########################

    def visitVarDecl(self, ast: VarDecl, o):
        var_type = ast.typ
        if self.func_flag == False:
            index = self.local_index
            var_init = MT22SupFunc.return_type(
                self.visit(ast.init, o)) if ast.init else None
            if "local" not in o:
                if ast.name in o["global"]:
                    raise Redeclared(Variable(), ast.name)
                if var_init is None and type(var_type) == AutoType:
                    raise Invalid(Variable(), ast.name)
                else:
                    if type(var_type) == AutoType:
                        var_type = var_init
                    o["global"][ast.name] = Variable_op(var_type, var_init)
                    initial_init = o["global"][ast.name]
            else:
                if ast.name in o["local"][index]:
                    raise Redeclared(Variable(), ast.name)

                if var_init is None and type(var_type) == AutoType:
                    raise Invalid(Variable(), ast.name)
                else:
                    if type(var_type) == AutoType:
                        var_type = var_init
                    o["local"][index][ast.name] = Variable_op(
                        var_type, var_init)
                    initial_init = o["local"][index][ast.name]

            if ast.init is not None:
                if not MT22SupFunc.compare(initial_init.type, var_init) and (type(ast.typ) != AutoType or type(var_init) != AutoType):
                    raise TypeMismatchInVarDecl(ast)
                elif type(ast.typ) == AutoType and type(var_init) in [IntegerType, FloatType, StringType, ArrayType, BooleanType]:
                    initial_init.type = var_init
                elif type(var_init) == AutoType and type(ast.typ) in [IntegerType, FloatType, StringType, ArrayType, BooleanType]:
                    temp = self.visit(ast.init, o)
                    temp.type = ast.typ

        else:
            if ast.name not in o:
                o[ast.name] = Variable_op(var_type, None)

    def visitParamDecl(self, ast: ParamDecl, o):
        if self.func_flag == False:
            o_child, o_parent = o

            if ast.name in o_parent:
                raise Invalid(Parameter(), ast.name)

            if ast.name in o_child:
                raise Redeclared(Parameter(), ast.name)

            if type(self.funclist[self.current].parameter[ast.name].type) != type(ast.typ):
                var_type = self.funclist[self.current].parameter[ast.name].type
            else:
                var_type = ast.typ

            o_child[ast.name] = Params_op(var_type, ast.out, ast.inherit)

        else:
            if ast.name not in o:
                o[ast.name] = Params_op(ast.typ, ast.out, ast.inherit)

    def visitFuncDecl(self, ast: FuncDecl, o):

        if self.func_flag == False:
            self.return_flag = False
            if type(self.funclist[ast.name].type) != type(ast.return_type):
                var_type = self.funclist[ast.name].type
            else:
                var_type = ast.return_type

            if ast.name in o["global"]:
                raise Redeclared(Function(), ast.name)

            o["global"][ast.name] = Function_op(var_type, ast.inherit)
            if ast.inherit is not None:
                if ast.inherit not in self.funclist:
                    raise Undeclared(Function(), ast.inherit)
                else:
                    if len(self.funclist[ast.inherit].parameter) == 0:
                        if ast.body.body == []:
                            pass
                        # else:
                            # if ast.body.body[0].name != "preventDefault":
                            #     self.retrieve_inherit(
                            #         self.funclist[ast.inherit].parameter, o["global"][ast.name].parameter)

                    else:
                        if ast.body.body == []:
                            raise InvalidStatementInFunction(ast.name)
                        else:
                            if type(ast.body.body[0]) != CallStmt:
                                raise InvalidStatementInFunction(ast.name)
                            else:
                                if ast.body.body[0].name == "super":
                                    self.check_dup_inherit_params(
                                        self.funclist[ast.inherit].inheram)
                                    self.retrieve_inherit(
                                        self.funclist[ast.inherit], o["global"][ast.name])
                                elif ast.body.body[0].name != "preventDefault":
                                    raise InvalidStatementInFunction(ast.name)

            self.current = ast.name
            new_o_param = {}
            if ast.params != []:
                for params in ast.params:
                    self.visit(
                        params, (new_o_param, o["global"][ast.name].parameter))

            # o["global"][ast.name].parameter.update(new_o_param)
            # print(o["global"][ast.name].parameter)
            # print("\n")

            self.local_index = 0
            self.return_flag = False
            new_o = o.copy()
            new_o["local"] = {}
            new_o["local"][0] = {}
            # new_o["local"][0].update(o["global"][ast.name].parameter)
            new_o["local"][0].update(new_o_param)

            if ast.body.body != []:
                for body in ast.body.body:
                    self.visit(body, new_o)
                    if body == ast.body.body[0]:
                        if ast.inherit != None and body.name == "super":
                            new_o["local"][0].update(
                                o["global"][ast.name].parameter)
                            o["global"][ast.name].parameter.update(new_o_param)
                        else:
                            o["global"][ast.name].parameter.update(new_o_param)
            else:
                o["global"][ast.name].parameter.update(new_o_param)

            del new_o
            del new_o_param

        else:
            if ast.name not in o:
                o[ast.name] = Function_op(ast.return_type, ast.inherit)
                if ast.params != []:
                    fake_params = []
                    for i in ast.params:
                        fake_params += [i]

                    o[ast.name].inheram = fake_params

                    for params in ast.params:
                        self.visit(params, o[ast.name].parameter)


########################## WHERE ITS START ##########################


    def visitProgram(self, ast: Program, o):
        o = {}
        o["global"] = {}
        MT22SupFunc.insert_glo_func(self.glo_envi)
        # print(self.glo_envi)
        has_main = False

        self.func_flag = True
        for i in ast.decls:
            # # print((o))
            if type(i) == FuncDecl:
                self.visit(i, self.funclist)
            elif type(i) == VarDecl:
                self.visit(i, self.varilist)

        self.func_flag = False
        for i in ast.decls:
            self.visit(i, o)
            if type(i) is FuncDecl and i.name == "main" and type(i.return_type) == VoidType and i.params == []:
                has_main = True

        # print("\ndictionary cua program sau khi nhập xong hết: ")
        # print(o["global"]["poo"].type)
        if has_main == False:
            raise NoEntryPoint()
