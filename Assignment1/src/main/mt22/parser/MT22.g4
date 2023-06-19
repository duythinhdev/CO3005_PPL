grammar MT22;

// 2052612 MAI HUU NGHIA
@lexer::header {
from lexererr import *
# 2052612 MAI HUU NGHIA
}

@parser::members {
}

options {
	language = Python3;
}

program: (funcDeclList | variableDeclList)+ EOF;

funcDeclList: funcDecl funcDeclList | funcDecl;
funcDecl:
	ID COLON FUNCTION funcType LB (variaFuncList)? RB (
		INHERIT ID
	)? blockStmt;

variaFuncList:
	variaFuncDeclarator COMMA variaFuncList
	| variaFuncDeclarator;
variaFuncDeclarator: INHERIT? OUT? ID COLON typeType;

variableDeclList: (varia_yes_body | varia_no_body) SM;

varia_no_body:
	ID COMMA varia_no_body
	| ID COLON (variType | arrayType);

varia_yes_body:
	ID COMMA varia_yes_body COMMA espresso
	| ID COLON (variType | arrayType) ASS espresso;

args: LB expList? RB;
expList: espresso COMMA expList | espresso;

typeType: funcType | arrayType | variType;
arrayType:
	ARRAY LSB INTEGERLIT (COMMA INTEGERLIT)* RSB OF variType;
funcType: INTEGER | FLOAT | BOOLEAN | STRING | VOID | AUTO | arrayType;
variType: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;

statement:
	assStmt SM
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt SM
	| breakStmt SM
	| continueStmt SM
	| returnStmt SM
	| callStmt SM
	| blockStmt;

assStmt: lhs ASS espresso;
ifStmt: IF LB espresso RB statement (ELSE statement)?;
forStmt:
	FOR LB ID ASS espresso COMMA espresso COMMA espresso RB statement;
whileStmt: WHILE LB espresso RB statement;
doWhileStmt: DO statement WHILE LB espresso RB;
breakStmt: BREAK;
continueStmt: CONTINUE;
returnStmt: RETURN espresso?;
callStmt: ID LB (espresso (COMMA espresso)*)? RB;
blockStmt: LCB blockStmtbody? RCB;
blockStmtbody: (variableDeclList | statement) blockStmtbody
	| (variableDeclList | statement);

espresso: espresso (AND | OR) espresso1 | espresso1;
espresso1:
	espresso1 (GT | LT | GTE | LTE) espresso2
	| espresso2;
espresso2: espresso2 (EQUAL | NEQUAL) espresso3 | espresso3;
espresso3: espresso3 (ADD | SUB) espresso4 | espresso4;
espresso4: espresso4 (MUL | DIV | MOD) espresso5 | espresso5;
espresso5: espresso5 CONCAT espresso6 | espresso6;
espresso6: NOT espresso6 | espresso7;
espresso7: (ADD | SUB) espresso7 | espresso8;
espresso8: espresso10 LSB espresso (COMMA espresso)* RSB | espresso10;
espresso10: ID args | espresso11;
espresso11: elem | arrayLit | LB espresso RB | ID;
espresso12: elem COMMA espresso12 | elem;
lhs: ID | lhsop;
lhsop: ID LSB (espresso12 | lhsop) RSB;

// 3.4 Keywords
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

// 3.5 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '::';

// 3.6 Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SM: ';';
COLON: ':';
LCB: '{';
RCB: '}';
ASS: '=';

// 3.2 Comment
LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

// 3.7 Literals 12_12345
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
INTEGERLIT: ('0' | [1-9][0-9]* ('_' [0-9] | [0-9])*) {self.text = self.text.replace("_","")};
FLOATLIT: (INTEGERLIT (Deci | Deci? Expo) | Deci Expo) {self.text = self.text.replace("_","")};
//INTEGERLIT: ([1-9][0-9_]* | '0')+ {self.text = self.text.replace("_","")}; FLOATLIT: ('0' |
// [1-9][0-9_]*)+ (Deci | Deci? Expo) {self.text = self.text.replace("_","")};
booleanlit: TRUE | FALSE;

STRINGLIT: ('"' StrCha? '"') {self.text = self.text[1:-1]};
arrayLit: LCB elemArrays? RCB;
elemArrays: espresso COMMA elemArrays | espresso;
// elemArray: INTEGERLIT | FLOATLIT | booleanlit | STRINGLIT;
elem: INTEGERLIT | FLOATLIT | booleanlit | STRINGLIT;
fragment StrCha: (~["\\\r\n] | Esc)+;
fragment Esc: '\\' [btnfr"'\\];
fragment Deci: '.' [0-9]*;
fragment Expo: ('e' | 'E') ('+' | '-')? [0-9]+;

// 3.3 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

UNCLOSE_STRING:
	'"' StrCha* EOF? {
y = str(self.text)
raise UncloseString(y[1:])
};
ILLEGAL_ESCAPE:
	'"' StrCha* ('\\' ~[bfrnt"'\\]) {
y = str(self.text)
raise IllegalEscape(y[1:])
};
ERROR_CHAR:
	.{
raise ErrorToken(self.text)
};
// UNTERMINATED_COMMENT: '/*' .*? { y = str(self.text) raise UnterminatedComment(y[0:]) };