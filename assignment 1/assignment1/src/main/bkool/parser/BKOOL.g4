/* 1811984 */
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : class_declare+ EOF ;


// declarations

class_declare: CLASS ID (EXTENDS ID)? CURLY_OPEN members* CURLY_CLOSE;

members: attribute_declare | method_declare | constructor_declare;

attribute_declare: mutable_declare | immutable_declare;

mutable_declare: (STATIC|) type_attribute var_declare ( COMMA var_declare )* SEMI;

immutable_declare: (FINAL | STATIC FINAL | FINAL STATIC) type_attribute var_declare_immu ( COMMA var_declare_immu )* SEMI;


method_declare: STATIC ? return_type ID ROUND_OPEN list_params ROUND_CLOSE block_statement;

constructor_declare: ID ROUND_OPEN list_params ROUND_CLOSE  block_statement;

var_declare: ID ( ASSIGN exp) ? ;

var_declare_immu: ID  ASSIGN exp;




// list parameter of method and constructor

list_params: | parameter (SEMI parameter)* ;

parameter: parameter_type ID (COMMA ID)*;

parameter_type: type_attribute;





//type

return_type: primitive_type | class_type | array_type ;

type_attribute: class_type | primitive_type |  array_type;

array_type: (primitive_type|class_type) SQUARE_OPEN INTEGER_LIT SQUARE_CLOSE;

class_type: ID;

primitive_type: INTEGER | FLOAT | BOOLEAN | STRING | VOID ;






// statements

block_statement: CURLY_OPEN (local_attribute*) (statement*) CURLY_CLOSE;

local_attribute: type_attribute var_declare ( COMMA var_declare )* SEMI
               | FINAL type_attribute var_declare_immu ( COMMA var_declare_immu )* SEMI;

//------------------------------------------------

statement:  if_statement
         |  for_statement
         |  break_statement SEMI
         |  continue_statement SEMI
         |  return_statement SEMI
         |  method_invo_statement SEMI
         |  assignment_statement SEMI
         |  block_statement;  // end with semicolon

// ------- assignment -------------

assignment_statement: lhs ASSIGN_EQ exp;

lhs: ID | operands index_represent | prefix_attribute_invo DOT ID ;

prefix_attribute_invo: | ID
                       | prefix_attribute_invo DOT ID list_args_wrapped
                       | ROUND_OPEN exp ROUND_CLOSE
                       | prefix_attribute_invo index_represent
                       | THIS
                       ;

if_statement: IF bool_exp THEN statement (ELSE statement)? ;

for_statement: FOR ID ASSIGN_EQ int_exp (TO | DOWNTO) int_exp DO statement;


break_statement: BREAK ;
continue_statement: CONTINUE;
return_statement: RETURN return_exp ;

method_invo_statement: obj_methodInvo DOT ID list_args_wrapped ;

obj_methodInvo:  literals | ID  | operands DOT ID  | operands DOT ID list_args_wrapped  | ROUND_OPEN exp ROUND_CLOSE  | operands index_represent  | THIS | NIL;

// expressions

bool_exp: exp;

int_exp: exp;

return_exp: exp;

exp: exp1 (LT | GT | LTE | GTE ) exp1 | exp1;

exp1: exp1 (EQ | NEQ) exp1 | exp2;

exp2: exp3 (AND | OR) exp2 | exp3;

exp3: exp4 (ADD | SUB) exp3 | exp4;

exp4: exp5 ( MUL | FLOAT_DIV | INT_DIV | MOD ) exp4 | exp5;

exp5: exp6 CONCAT exp5 | exp6;

exp6: NOT exp6 | exp7;

exp7: (ADD | SUB) exp7 | operands;


operands: literals
        | ID
        | operands index_represent
        | operands DOT ID
        | operands DOT ID list_args_wrapped
        | ROUND_OPEN exp ROUND_CLOSE
        | THIS
        | obj_create
        | NIL
        ;

index_represent: SQUARE_OPEN exp SQUARE_CLOSE;

obj_create: NEW ID list_args_wrapped;

list_args_wrapped:  ROUND_OPEN list_exps_as_args  ROUND_CLOSE;

list_exps_as_args:<assoc=right> exp ( COMMA exp )* | ;







// keywords tokens
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INTEGER: 'int';
STRING: 'string';
THEN: 'then' ;
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// operator

ADD: '+';
SUB: '-';
MUL: '*';
FLOAT_DIV: '/';
INT_DIV: '\\';
MOD: '%';
ASSIGN: '=';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
EQ : '==' ;
LT : '<' ;
GT : '>' ;
NOT: '!';
AND: '&&';
OR: '||';
CONCAT: '^';
DOT: '.';
NEW: 'new';
COLON: ':';
ASSIGN_EQ: ':=';

// separator and parenthesis
CURLY_OPEN: '{';
CURLY_CLOSE: '}';
ROUND_OPEN: '(';
ROUND_CLOSE: ')';
SQUARE_OPEN:'[';
SQUARE_CLOSE: ']';
SEMI: ';';
COMMA: ',';


// another skip-error tokens and literals
literals: literal_replica | array_literal  ;

boolean_literal: TRUE | FALSE ;

array_literal: CURLY_OPEN literal_replica (COMMA literal_replica )* CURLY_CLOSE;

literal_replica: INTEGER_LIT | FLOAT_LIT | STRING_LIT | THIS | NIL | boolean_literal;
FLOAT_LIT : [0-9]+(('.'[0-9]*)|(('.'[0-9]*)?(('E'|'e')('+'|'-')?[0-9]+)));
INTEGER_LIT: [0-9]+;

STRING_LIT: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y
	}
	;

ID: [_a-zA-Z][_a-zA-Z0-9]* ;




COMMENT: (MUL_COMMENT|ONE_COMMENT) -> skip;
WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: '"' STR_CHAR*
	{
		y = str(self.text)
		raise UncloseString(y)
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y)
	}
	;


//Fragment

fragment STR_CHAR: ( '\\' [btnfr"\\] | ~[\n\r"\\] ) ;
fragment ESC_ILLEGAL
    : '\\'~[bfrnt"\\]
    | '\''~'"'
    ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;


fragment MUL_COMMENT: '/*' (.)*? '*/';
fragment ONE_COMMENT: '#' ~[\r\n]*;
fragment UNDERSCORE: '_';


ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;