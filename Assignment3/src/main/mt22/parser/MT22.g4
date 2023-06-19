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

program: declares EOF;

declares: declare declares | declare;

declare: funcDecl | variableDeclList;
funcDecl:
	ID COLON FUNCTION funcType LB (variaFuncList)? RB (
		INHERIT ID
	)? blockStmt;

variaFuncList:
	variaFuncDeclarator COMMA variaFuncList
	| variaFuncDeclarator;
variaFuncDeclarator: INHERIT? OUT? ID COLON typeType;

variableDeclList: (
		varia_yes_body
		| (varia_no_body COLON (variType | arrayType))
	) SM;

varia_no_body: ID COMMA varia_no_body | ID;

varia_yes_body:
	ID COMMA varia_yes_body COMMA espresso
	| ID COLON (variType | arrayType) ASS espresso;

args: LB expList? RB;
expList: espresso COMMA expList | espresso;

typeType: funcType | arrayType | variType;
arrayType: ARRAY LSB arraySize RSB OF variNoAuto;
arraySize: INTEGERLIT COMMA arraySize | INTEGERLIT;
variNoAuto: INTEGER | FLOAT | BOOLEAN | STRING;
variType: variNoAuto | AUTO;
funcType: variType | VOID | arrayType;

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
	FOR LB assStmt COMMA espresso COMMA espresso RB statement;
whileStmt: WHILE LB espresso RB statement;
doWhileStmt: DO blockStmt WHILE LB espresso RB;
breakStmt: BREAK;
continueStmt: CONTINUE;
returnStmt: RETURN espresso?;
callStmt: ID LB callEsp? RB;
callEsp: espresso COMMA callEsp | espresso;
blockStmt: LCB blockStmtbody? RCB;
blockStmtbody: (variableDeclList | statement) blockStmtbody
	| (variableDeclList | statement);

espresso: espresso CONCAT espresso1 | espresso1;
espresso1:
	espresso1 (EQUAL | NEQUAL | GT | LT | GTE | LTE) espresso2
	| espresso2;
espresso2: espresso2 (AND | OR) espresso3 | espresso3;
espresso3: espresso3 (ADD | SUB) espresso4 | espresso4;
espresso4: espresso4 (MUL | DIV | MOD) espresso5 | espresso5;
espresso5: NOT espresso5 | espresso6;
espresso6: SUB (espresso5 | espresso6) | espresso7;
espresso7: ID LSB expList RSB | espresso10a;
espresso10a: ID args | espresso11a;
espresso11a: elem | arrayLit | LB espresso RB | ID;
lhs: ID | lhsop;
lhsop: ID LSB (expList | lhsop) RSB;

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

// 3.7 Literals 
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
INTEGERLIT: ('0' | [1-9][0-9]* ('_' [0-9] | [0-9])*) {self.text = self.text.replace("_","")};
FLOATLIT: (INTEGERLIT (Deci | Deci? Expo) | Deci Expo) {self.text = self.text.replace("_","")};
booleanlit: TRUE | FALSE;

STRINGLIT: ('"' StrCha? '"') {self.text = self.text[1:-1]};
arrayLit: LCB elemArrays? RCB;
elemArrays: (espresso | arrayLit) COMMA elemArrays
	| (espresso | arrayLit);
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