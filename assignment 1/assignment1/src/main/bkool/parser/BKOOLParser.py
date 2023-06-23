# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0207\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\5\3t\n")
        buf.write("\3\3\3\3\3\7\3x\n\3\f\3\16\3{\13\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\5\4\u0082\n\4\3\5\3\5\5\5\u0086\n\5\3\6\3\6\5\6\u008a")
        buf.write("\n\6\3\6\3\6\3\6\3\6\7\6\u0090\n\6\f\6\16\6\u0093\13\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u009c\n\7\3\7\3\7\3\7")
        buf.write("\3\7\7\7\u00a2\n\7\f\7\16\7\u00a5\13\7\3\7\3\7\3\b\5\b")
        buf.write("\u00aa\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\5\n\u00bc\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00c6\n\f\f\f\16\f\u00c9\13\f\5\f")
        buf.write("\u00cb\n\f\3\r\3\r\3\r\3\r\7\r\u00d1\n\r\f\r\16\r\u00d4")
        buf.write("\13\r\3\16\3\16\3\17\3\17\3\17\5\17\u00db\n\17\3\20\3")
        buf.write("\20\3\20\5\20\u00e0\n\20\3\21\3\21\5\21\u00e4\n\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\7\24\u00f0")
        buf.write("\n\24\f\24\16\24\u00f3\13\24\3\24\7\24\u00f6\n\24\f\24")
        buf.write("\16\24\u00f9\13\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u0101\n\25\f\25\16\25\u0104\13\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\7\25\u010d\n\25\f\25\16\25\u0110\13\25")
        buf.write("\3\25\3\25\5\25\u0114\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0128\n\26\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0136\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u013f\n\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\7\31\u0147\n\31\f\31\16\31\u014a")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0152\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \5 \u017d\n \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3$\5")
        buf.write("$\u018a\n$\3%\3%\3%\3%\3%\3%\7%\u0192\n%\f%\16%\u0195")
        buf.write("\13%\3&\3&\3&\3&\3&\5&\u019c\n&\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u01a3\n\'\3(\3(\3(\3(\3(\5(\u01aa\n(\3)\3)\3)\3)\3")
        buf.write(")\5)\u01b1\n)\3*\3*\3*\5*\u01b6\n*\3+\3+\3+\5+\u01bb\n")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01c7\n,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u01d2\n,\f,\16,\u01d5\13,\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\7\60\u01e6")
        buf.write("\n\60\f\60\16\60\u01e9\13\60\3\60\5\60\u01ec\n\60\3\61")
        buf.write("\3\61\5\61\u01f0\n\61\3\62\3\62\3\63\3\63\3\63\3\63\7")
        buf.write("\63\u01f8\n\63\f\63\16\63\u01fb\13\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\5\64\u0205\n\64\3\64\2\5\60HV")
        buf.write("\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\n\6\2\3\3\n\n\f\r")
        buf.write("\23\23\3\2\30\31\4\2!\"%&\3\2#$\3\2()\3\2\32\33\3\2\34")
        buf.write("\37\3\2\21\22\2\u021c\2i\3\2\2\2\4o\3\2\2\2\6\u0081\3")
        buf.write("\2\2\2\b\u0085\3\2\2\2\n\u0089\3\2\2\2\f\u009b\3\2\2\2")
        buf.write("\16\u00a9\3\2\2\2\20\u00b2\3\2\2\2\22\u00b8\3\2\2\2\24")
        buf.write("\u00bd\3\2\2\2\26\u00ca\3\2\2\2\30\u00cc\3\2\2\2\32\u00d5")
        buf.write("\3\2\2\2\34\u00da\3\2\2\2\36\u00df\3\2\2\2 \u00e3\3\2")
        buf.write("\2\2\"\u00e9\3\2\2\2$\u00eb\3\2\2\2&\u00ed\3\2\2\2(\u0113")
        buf.write("\3\2\2\2*\u0127\3\2\2\2,\u0129\3\2\2\2.\u0135\3\2\2\2")
        buf.write("\60\u013e\3\2\2\2\62\u014b\3\2\2\2\64\u0153\3\2\2\2\66")
        buf.write("\u015c\3\2\2\28\u015e\3\2\2\2:\u0160\3\2\2\2<\u0163\3")
        buf.write("\2\2\2>\u017c\3\2\2\2@\u017e\3\2\2\2B\u0180\3\2\2\2D\u0182")
        buf.write("\3\2\2\2F\u0189\3\2\2\2H\u018b\3\2\2\2J\u019b\3\2\2\2")
        buf.write("L\u01a2\3\2\2\2N\u01a9\3\2\2\2P\u01b0\3\2\2\2R\u01b5\3")
        buf.write("\2\2\2T\u01ba\3\2\2\2V\u01c6\3\2\2\2X\u01d6\3\2\2\2Z\u01da")
        buf.write("\3\2\2\2\\\u01de\3\2\2\2^\u01eb\3\2\2\2`\u01ef\3\2\2\2")
        buf.write("b\u01f1\3\2\2\2d\u01f3\3\2\2\2f\u0204\3\2\2\2hj\5\4\3")
        buf.write("\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2m")
        buf.write("n\7\2\2\3n\3\3\2\2\2op\7\5\2\2ps\7:\2\2qr\7\t\2\2rt\7")
        buf.write(":\2\2sq\3\2\2\2st\3\2\2\2tu\3\2\2\2uy\7/\2\2vx\5\6\4\2")
        buf.write("wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3")
        buf.write("\2\2\2|}\7\60\2\2}\5\3\2\2\2~\u0082\5\b\5\2\177\u0082")
        buf.write("\5\16\b\2\u0080\u0082\5\20\t\2\u0081~\3\2\2\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2\2\u0083\u0086")
        buf.write("\5\n\6\2\u0084\u0086\5\f\7\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\t\3\2\2\2\u0087\u008a\7\27\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u008c\5\36\20\2\u008c\u0091")
        buf.write("\5\22\n\2\u008d\u008e\7\66\2\2\u008e\u0090\5\22\n\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0094\u0095\7\65\2\2\u0095\13\3\2\2\2\u0096\u009c")
        buf.write("\7\26\2\2\u0097\u0098\7\27\2\2\u0098\u009c\7\26\2\2\u0099")
        buf.write("\u009a\7\26\2\2\u009a\u009c\7\27\2\2\u009b\u0096\3\2\2")
        buf.write("\2\u009b\u0097\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009e\5\36\20\2\u009e\u00a3\5\24\13\2\u009f")
        buf.write("\u00a0\7\66\2\2\u00a0\u00a2\5\24\13\2\u00a1\u009f\3\2")
        buf.write("\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6")
        buf.write("\u00a7\7\65\2\2\u00a7\r\3\2\2\2\u00a8\u00aa\7\27\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\5\34\17\2\u00ac\u00ad\7:\2\2\u00ad\u00ae")
        buf.write("\7\61\2\2\u00ae\u00af\5\26\f\2\u00af\u00b0\7\62\2\2\u00b0")
        buf.write("\u00b1\5&\24\2\u00b1\17\3\2\2\2\u00b2\u00b3\7:\2\2\u00b3")
        buf.write("\u00b4\7\61\2\2\u00b4\u00b5\5\26\f\2\u00b5\u00b6\7\62")
        buf.write("\2\2\u00b6\u00b7\5&\24\2\u00b7\21\3\2\2\2\u00b8\u00bb")
        buf.write("\7:\2\2\u00b9\u00ba\7 \2\2\u00ba\u00bc\5F$\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\23\3\2\2\2\u00bd\u00be")
        buf.write("\7:\2\2\u00be\u00bf\7 \2\2\u00bf\u00c0\5F$\2\u00c0\25")
        buf.write("\3\2\2\2\u00c1\u00cb\3\2\2\2\u00c2\u00c7\5\30\r\2\u00c3")
        buf.write("\u00c4\7\65\2\2\u00c4\u00c6\5\30\r\2\u00c5\u00c3\3\2\2")
        buf.write("\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00c1\3\2\2\2\u00ca\u00c2\3\2\2\2\u00cb\27\3\2\2\2\u00cc")
        buf.write("\u00cd\5\32\16\2\u00cd\u00d2\7:\2\2\u00ce\u00cf\7\66\2")
        buf.write("\2\u00cf\u00d1\7:\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d4")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\31\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\5\36\20\2")
        buf.write("\u00d6\33\3\2\2\2\u00d7\u00db\5$\23\2\u00d8\u00db\5\"")
        buf.write("\22\2\u00d9\u00db\5 \21\2\u00da\u00d7\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\35\3\2\2\2\u00dc\u00e0")
        buf.write("\5\"\22\2\u00dd\u00e0\5$\23\2\u00de\u00e0\5 \21\2\u00df")
        buf.write("\u00dc\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2")
        buf.write("\u00e0\37\3\2\2\2\u00e1\u00e4\5$\23\2\u00e2\u00e4\5\"")
        buf.write("\22\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e6\7\63\2\2\u00e6\u00e7\78\2\2\u00e7")
        buf.write("\u00e8\7\64\2\2\u00e8!\3\2\2\2\u00e9\u00ea\7:\2\2\u00ea")
        buf.write("#\3\2\2\2\u00eb\u00ec\t\2\2\2\u00ec%\3\2\2\2\u00ed\u00f1")
        buf.write("\7/\2\2\u00ee\u00f0\5(\25\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f7\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f6\5")
        buf.write("*\26\2\u00f5\u00f4\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00fa\u00fb\7\60\2\2\u00fb\'\3\2\2\2\u00fc")
        buf.write("\u00fd\5\36\20\2\u00fd\u0102\5\22\n\2\u00fe\u00ff\7\66")
        buf.write("\2\2\u00ff\u0101\5\22\n\2\u0100\u00fe\3\2\2\2\u0101\u0104")
        buf.write("\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\7\65\2")
        buf.write("\2\u0106\u0114\3\2\2\2\u0107\u0108\7\26\2\2\u0108\u0109")
        buf.write("\5\36\20\2\u0109\u010e\5\24\13\2\u010a\u010b\7\66\2\2")
        buf.write("\u010b\u010d\5\24\13\2\u010c\u010a\3\2\2\2\u010d\u0110")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7\65\2")
        buf.write("\2\u0112\u0114\3\2\2\2\u0113\u00fc\3\2\2\2\u0113\u0107")
        buf.write("\3\2\2\2\u0114)\3\2\2\2\u0115\u0128\5\62\32\2\u0116\u0128")
        buf.write("\5\64\33\2\u0117\u0118\5\66\34\2\u0118\u0119\7\65\2\2")
        buf.write("\u0119\u0128\3\2\2\2\u011a\u011b\58\35\2\u011b\u011c\7")
        buf.write("\65\2\2\u011c\u0128\3\2\2\2\u011d\u011e\5:\36\2\u011e")
        buf.write("\u011f\7\65\2\2\u011f\u0128\3\2\2\2\u0120\u0121\5<\37")
        buf.write("\2\u0121\u0122\7\65\2\2\u0122\u0128\3\2\2\2\u0123\u0124")
        buf.write("\5,\27\2\u0124\u0125\7\65\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0128\5&\24\2\u0127\u0115\3\2\2\2\u0127\u0116\3\2\2\2")
        buf.write("\u0127\u0117\3\2\2\2\u0127\u011a\3\2\2\2\u0127\u011d\3")
        buf.write("\2\2\2\u0127\u0120\3\2\2\2\u0127\u0123\3\2\2\2\u0127\u0126")
        buf.write("\3\2\2\2\u0128+\3\2\2\2\u0129\u012a\5.\30\2\u012a\u012b")
        buf.write("\7.\2\2\u012b\u012c\5F$\2\u012c-\3\2\2\2\u012d\u0136\7")
        buf.write(":\2\2\u012e\u012f\5V,\2\u012f\u0130\5X-\2\u0130\u0136")
        buf.write("\3\2\2\2\u0131\u0132\5\60\31\2\u0132\u0133\7+\2\2\u0133")
        buf.write("\u0134\7:\2\2\u0134\u0136\3\2\2\2\u0135\u012d\3\2\2\2")
        buf.write("\u0135\u012e\3\2\2\2\u0135\u0131\3\2\2\2\u0136/\3\2\2")
        buf.write("\2\u0137\u013f\b\31\1\2\u0138\u013f\7:\2\2\u0139\u013a")
        buf.write("\7\61\2\2\u013a\u013b\5F$\2\u013b\u013c\7\62\2\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013f\7\25\2\2\u013e\u0137\3\2\2")
        buf.write("\2\u013e\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013f\u0148\3\2\2\2\u0140\u0141\f\6\2\2\u0141")
        buf.write("\u0142\7+\2\2\u0142\u0143\7:\2\2\u0143\u0147\5\\/\2\u0144")
        buf.write("\u0145\f\4\2\2\u0145\u0147\5X-\2\u0146\u0140\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\61\3\2\2\2\u014a\u0148\3\2")
        buf.write("\2\2\u014b\u014c\7\13\2\2\u014c\u014d\5@!\2\u014d\u014e")
        buf.write("\7\16\2\2\u014e\u0151\5*\26\2\u014f\u0150\7\b\2\2\u0150")
        buf.write("\u0152\5*\26\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\63\3\2\2\2\u0153\u0154\7\17\2\2\u0154\u0155\7:")
        buf.write("\2\2\u0155\u0156\7.\2\2\u0156\u0157\5B\"\2\u0157\u0158")
        buf.write("\t\3\2\2\u0158\u0159\5B\"\2\u0159\u015a\7\7\2\2\u015a")
        buf.write("\u015b\5*\26\2\u015b\65\3\2\2\2\u015c\u015d\7\4\2\2\u015d")
        buf.write("\67\3\2\2\2\u015e\u015f\7\6\2\2\u015f9\3\2\2\2\u0160\u0161")
        buf.write("\7\20\2\2\u0161\u0162\5D#\2\u0162;\3\2\2\2\u0163\u0164")
        buf.write("\5> \2\u0164\u0165\7+\2\2\u0165\u0166\7:\2\2\u0166\u0167")
        buf.write("\5\\/\2\u0167=\3\2\2\2\u0168\u017d\5`\61\2\u0169\u017d")
        buf.write("\7:\2\2\u016a\u016b\5V,\2\u016b\u016c\7+\2\2\u016c\u016d")
        buf.write("\7:\2\2\u016d\u017d\3\2\2\2\u016e\u016f\5V,\2\u016f\u0170")
        buf.write("\7+\2\2\u0170\u0171\7:\2\2\u0171\u0172\5\\/\2\u0172\u017d")
        buf.write("\3\2\2\2\u0173\u0174\7\61\2\2\u0174\u0175\5F$\2\u0175")
        buf.write("\u0176\7\62\2\2\u0176\u017d\3\2\2\2\u0177\u0178\5V,\2")
        buf.write("\u0178\u0179\5X-\2\u0179\u017d\3\2\2\2\u017a\u017d\7\25")
        buf.write("\2\2\u017b\u017d\7\24\2\2\u017c\u0168\3\2\2\2\u017c\u0169")
        buf.write("\3\2\2\2\u017c\u016a\3\2\2\2\u017c\u016e\3\2\2\2\u017c")
        buf.write("\u0173\3\2\2\2\u017c\u0177\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017b\3\2\2\2\u017d?\3\2\2\2\u017e\u017f\5F$\2")
        buf.write("\u017fA\3\2\2\2\u0180\u0181\5F$\2\u0181C\3\2\2\2\u0182")
        buf.write("\u0183\5F$\2\u0183E\3\2\2\2\u0184\u0185\5H%\2\u0185\u0186")
        buf.write("\t\4\2\2\u0186\u0187\5H%\2\u0187\u018a\3\2\2\2\u0188\u018a")
        buf.write("\5H%\2\u0189\u0184\3\2\2\2\u0189\u0188\3\2\2\2\u018aG")
        buf.write("\3\2\2\2\u018b\u018c\b%\1\2\u018c\u018d\5J&\2\u018d\u0193")
        buf.write("\3\2\2\2\u018e\u018f\f\4\2\2\u018f\u0190\t\5\2\2\u0190")
        buf.write("\u0192\5H%\5\u0191\u018e\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194I\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\5L\'\2\u0197\u0198\t\6\2\2")
        buf.write("\u0198\u0199\5J&\2\u0199\u019c\3\2\2\2\u019a\u019c\5L")
        buf.write("\'\2\u019b\u0196\3\2\2\2\u019b\u019a\3\2\2\2\u019cK\3")
        buf.write("\2\2\2\u019d\u019e\5N(\2\u019e\u019f\t\7\2\2\u019f\u01a0")
        buf.write("\5L\'\2\u01a0\u01a3\3\2\2\2\u01a1\u01a3\5N(\2\u01a2\u019d")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3M\3\2\2\2\u01a4\u01a5")
        buf.write("\5P)\2\u01a5\u01a6\t\b\2\2\u01a6\u01a7\5N(\2\u01a7\u01aa")
        buf.write("\3\2\2\2\u01a8\u01aa\5P)\2\u01a9\u01a4\3\2\2\2\u01a9\u01a8")
        buf.write("\3\2\2\2\u01aaO\3\2\2\2\u01ab\u01ac\5R*\2\u01ac\u01ad")
        buf.write("\7*\2\2\u01ad\u01ae\5P)\2\u01ae\u01b1\3\2\2\2\u01af\u01b1")
        buf.write("\5R*\2\u01b0\u01ab\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1Q")
        buf.write("\3\2\2\2\u01b2\u01b3\7\'\2\2\u01b3\u01b6\5R*\2\u01b4\u01b6")
        buf.write("\5T+\2\u01b5\u01b2\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6S")
        buf.write("\3\2\2\2\u01b7\u01b8\t\7\2\2\u01b8\u01bb\5T+\2\u01b9\u01bb")
        buf.write("\5V,\2\u01ba\u01b7\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbU")
        buf.write("\3\2\2\2\u01bc\u01bd\b,\1\2\u01bd\u01c7\5`\61\2\u01be")
        buf.write("\u01c7\7:\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1\5F$\2\u01c1")
        buf.write("\u01c2\7\62\2\2\u01c2\u01c7\3\2\2\2\u01c3\u01c7\7\25\2")
        buf.write("\2\u01c4\u01c7\5Z.\2\u01c5\u01c7\7\24\2\2\u01c6\u01bc")
        buf.write("\3\2\2\2\u01c6\u01be\3\2\2\2\u01c6\u01bf\3\2\2\2\u01c6")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7\u01d3\3\2\2\2\u01c8\u01c9\f\t\2\2\u01c9\u01d2\5")
        buf.write("X-\2\u01ca\u01cb\f\b\2\2\u01cb\u01cc\7+\2\2\u01cc\u01d2")
        buf.write("\7:\2\2\u01cd\u01ce\f\7\2\2\u01ce\u01cf\7+\2\2\u01cf\u01d0")
        buf.write("\7:\2\2\u01d0\u01d2\5\\/\2\u01d1\u01c8\3\2\2\2\u01d1\u01ca")
        buf.write("\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4W\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d7\7\63\2\2\u01d7\u01d8\5F$\2")
        buf.write("\u01d8\u01d9\7\64\2\2\u01d9Y\3\2\2\2\u01da\u01db\7,\2")
        buf.write("\2\u01db\u01dc\7:\2\2\u01dc\u01dd\5\\/\2\u01dd[\3\2\2")
        buf.write("\2\u01de\u01df\7\61\2\2\u01df\u01e0\5^\60\2\u01e0\u01e1")
        buf.write("\7\62\2\2\u01e1]\3\2\2\2\u01e2\u01e7\5F$\2\u01e3\u01e4")
        buf.write("\7\66\2\2\u01e4\u01e6\5F$\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01ec\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01ec\3")
        buf.write("\2\2\2\u01eb\u01e2\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec_")
        buf.write("\3\2\2\2\u01ed\u01f0\5f\64\2\u01ee\u01f0\5d\63\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0a\3\2\2\2\u01f1")
        buf.write("\u01f2\t\t\2\2\u01f2c\3\2\2\2\u01f3\u01f4\7/\2\2\u01f4")
        buf.write("\u01f9\5f\64\2\u01f5\u01f6\7\66\2\2\u01f6\u01f8\5f\64")
        buf.write("\2\u01f7\u01f5\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u01fd\7\60\2\2\u01fde\3\2\2\2\u01fe")
        buf.write("\u0205\78\2\2\u01ff\u0205\7\67\2\2\u0200\u0205\79\2\2")
        buf.write("\u0201\u0205\7\25\2\2\u0202\u0205\7\24\2\2\u0203\u0205")
        buf.write("\5b\62\2\u0204\u01fe\3\2\2\2\u0204\u01ff\3\2\2\2\u0204")
        buf.write("\u0200\3\2\2\2\u0204\u0201\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0204\u0203\3\2\2\2\u0205g\3\2\2\2/ksy\u0081\u0085\u0089")
        buf.write("\u0091\u009b\u00a3\u00a9\u00bb\u00c7\u00ca\u00d2\u00da")
        buf.write("\u00df\u00e3\u00f1\u00f7\u0102\u010e\u0113\u0127\u0135")
        buf.write("\u013e\u0146\u0148\u0151\u017c\u0189\u0193\u019b\u01a2")
        buf.write("\u01a9\u01b0\u01b5\u01ba\u01c6\u01d1\u01d3\u01e7\u01eb")
        buf.write("\u01ef\u01f9\u0204")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'string'", "'then'", "'for'", "'return'", "'true'", 
                     "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'='", "'<='", "'>='", "'!='", 
                     "'=='", "'<'", "'>'", "'!'", "'&&'", "'||'", "'^'", 
                     "'.'", "'new'", "':'", "':='", "'{'", "'}'", "'('", 
                     "')'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INTEGER", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
                      "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "NOT", 
                      "AND", "OR", "CONCAT", "DOT", "NEW", "COLON", "ASSIGN_EQ", 
                      "CURLY_OPEN", "CURLY_CLOSE", "ROUND_OPEN", "ROUND_CLOSE", 
                      "SQUARE_OPEN", "SQUARE_CLOSE", "SEMI", "COMMA", "FLOAT_LIT", 
                      "INTEGER_LIT", "STRING_LIT", "ID", "COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_members = 2
    RULE_attribute_declare = 3
    RULE_mutable_declare = 4
    RULE_immutable_declare = 5
    RULE_method_declare = 6
    RULE_constructor_declare = 7
    RULE_var_declare = 8
    RULE_var_declare_immu = 9
    RULE_list_params = 10
    RULE_parameter = 11
    RULE_parameter_type = 12
    RULE_return_type = 13
    RULE_type_attribute = 14
    RULE_array_type = 15
    RULE_class_type = 16
    RULE_primitive_type = 17
    RULE_block_statement = 18
    RULE_local_attribute = 19
    RULE_statement = 20
    RULE_assignment_statement = 21
    RULE_lhs = 22
    RULE_prefix_attribute_invo = 23
    RULE_if_statement = 24
    RULE_for_statement = 25
    RULE_break_statement = 26
    RULE_continue_statement = 27
    RULE_return_statement = 28
    RULE_method_invo_statement = 29
    RULE_obj_methodInvo = 30
    RULE_bool_exp = 31
    RULE_int_exp = 32
    RULE_return_exp = 33
    RULE_exp = 34
    RULE_exp1 = 35
    RULE_exp2 = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_exp7 = 41
    RULE_operands = 42
    RULE_index_represent = 43
    RULE_obj_create = 44
    RULE_list_args_wrapped = 45
    RULE_list_exps_as_args = 46
    RULE_literals = 47
    RULE_boolean_literal = 48
    RULE_array_literal = 49
    RULE_literal_replica = 50

    ruleNames =  [ "program", "class_declare", "members", "attribute_declare", 
                   "mutable_declare", "immutable_declare", "method_declare", 
                   "constructor_declare", "var_declare", "var_declare_immu", 
                   "list_params", "parameter", "parameter_type", "return_type", 
                   "type_attribute", "array_type", "class_type", "primitive_type", 
                   "block_statement", "local_attribute", "statement", "assignment_statement", 
                   "lhs", "prefix_attribute_invo", "if_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "method_invo_statement", "obj_methodInvo", "bool_exp", 
                   "int_exp", "return_exp", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "operands", "index_represent", 
                   "obj_create", "list_args_wrapped", "list_exps_as_args", 
                   "literals", "boolean_literal", "array_literal", "literal_replica" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INTEGER=10
    STRING=11
    THEN=12
    FOR=13
    RETURN=14
    TRUE=15
    FALSE=16
    VOID=17
    NIL=18
    THIS=19
    FINAL=20
    STATIC=21
    TO=22
    DOWNTO=23
    ADD=24
    SUB=25
    MUL=26
    FLOAT_DIV=27
    INT_DIV=28
    MOD=29
    ASSIGN=30
    LTE=31
    GTE=32
    NEQ=33
    EQ=34
    LT=35
    GT=36
    NOT=37
    AND=38
    OR=39
    CONCAT=40
    DOT=41
    NEW=42
    COLON=43
    ASSIGN_EQ=44
    CURLY_OPEN=45
    CURLY_CLOSE=46
    ROUND_OPEN=47
    ROUND_CLOSE=48
    SQUARE_OPEN=49
    SQUARE_CLOSE=50
    SEMI=51
    COMMA=52
    FLOAT_LIT=53
    INTEGER_LIT=54
    STRING_LIT=55
    ID=56
    COMMENT=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.class_declare()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 107
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def members(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MembersContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MembersContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = BKOOLParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKOOLParser.CLASS)
            self.state = 110
            self.match(BKOOLParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 111
                self.match(BKOOLParser.EXTENDS)
                self.state = 112
                self.match(BKOOLParser.ID)


            self.state = 115
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 116
                self.members()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declareContext,0)


        def constructor_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.attribute_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.method_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.constructor_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutable_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Mutable_declareContext,0)


        def immutable_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Immutable_declareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = BKOOLParser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declare)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.mutable_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.immutable_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_declare" ):
                return visitor.visitMutable_declare(self)
            else:
                return visitor.visitChildren(self)




    def mutable_declare(self):

        localctx = BKOOLParser.Mutable_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mutable_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.state = 133
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self.type_attribute()
            self.state = 138
            self.var_declare()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 139
                self.match(BKOOLParser.COMMA)
                self.state = 140
                self.var_declare()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Immutable_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare_immu(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declare_immuContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declare_immuContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutable_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_declare" ):
                return visitor.visitImmutable_declare(self)
            else:
                return visitor.visitChildren(self)




    def immutable_declare(self):

        localctx = BKOOLParser.Immutable_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 149
                self.match(BKOOLParser.STATIC)
                self.state = 150
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 151
                self.match(BKOOLParser.FINAL)
                self.state = 152
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 155
            self.type_attribute()
            self.state = 156
            self.var_declare_immu()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 157
                self.match(BKOOLParser.COMMA)
                self.state = 158
                self.var_declare_immu()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(BKOOLParser.Return_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def list_params(self):
            return self.getTypedRuleContext(BKOOLParser.List_paramsContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = BKOOLParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 166
                self.match(BKOOLParser.STATIC)


            self.state = 169
            self.return_type()
            self.state = 170
            self.match(BKOOLParser.ID)
            self.state = 171
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 172
            self.list_params()
            self.state = 173
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 174
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def list_params(self):
            return self.getTypedRuleContext(BKOOLParser.List_paramsContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declare" ):
                return visitor.visitConstructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declare(self):

        localctx = BKOOLParser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BKOOLParser.ID)
            self.state = 177
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 178
            self.list_params()
            self.state = 179
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 180
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKOOLParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BKOOLParser.ID)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ASSIGN:
                self.state = 183
                self.match(BKOOLParser.ASSIGN)
                self.state = 184
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_immuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_declare_immu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_immu" ):
                return visitor.visitVar_declare_immu(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_immu(self):

        localctx = BKOOLParser.Var_declare_immuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_declare_immu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKOOLParser.ID)
            self.state = 188
            self.match(BKOOLParser.ASSIGN)
            self.state = 189
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParameterContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_params" ):
                return visitor.visitList_params(self)
            else:
                return visitor.visitChildren(self)




    def list_params(self):

        localctx = BKOOLParser.List_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ROUND_CLOSE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.parameter()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SEMI:
                    self.state = 193
                    self.match(BKOOLParser.SEMI)
                    self.state = 194
                    self.parameter()
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_type(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKOOLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.parameter_type()
            self.state = 203
            self.match(BKOOLParser.ID)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 204
                self.match(BKOOLParser.COMMA)
                self.state = 205
                self.match(BKOOLParser.ID)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_type" ):
                return visitor.visitParameter_type(self)
            else:
                return visitor.visitChildren(self)




    def parameter_type(self):

        localctx = BKOOLParser.Parameter_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.type_attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = BKOOLParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return_type)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.class_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_type_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_attribute" ):
                return visitor.visitType_attribute(self)
            else:
                return visitor.visitChildren(self)




    def type_attribute(self):

        localctx = BKOOLParser.Type_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_attribute)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.class_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.primitive_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_OPEN(self):
            return self.getToken(BKOOLParser.SQUARE_OPEN, 0)

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def SQUARE_CLOSE(self):
            return self.getToken(BKOOLParser.SQUARE_CLOSE, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 223
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 224
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 227
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 228
            self.match(BKOOLParser.INTEGER_LIT)
            self.state = 229
            self.match(BKOOLParser.SQUARE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def local_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Local_attributeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Local_attributeContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = BKOOLParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BKOOLParser.CURLY_OPEN)

            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 236
                    self.local_attribute() 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)


            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 242
                    self.statement() 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 248
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def var_declare_immu(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declare_immuContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declare_immuContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_attribute" ):
                return visitor.visitLocal_attribute(self)
            else:
                return visitor.visitChildren(self)




    def local_attribute(self):

        localctx = BKOOLParser.Local_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_local_attribute)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.type_attribute()
                self.state = 251
                self.var_declare()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 252
                    self.match(BKOOLParser.COMMA)
                    self.state = 253
                    self.var_declare()
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 259
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(BKOOLParser.FINAL)
                self.state = 262
                self.type_attribute()
                self.state = 263
                self.var_declare_immu()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 264
                    self.match(BKOOLParser.COMMA)
                    self.state = 265
                    self.var_declare_immu()
                    self.state = 270
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 271
                self.match(BKOOLParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def method_invo_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invo_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.for_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.break_statement()
                self.state = 278
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.continue_statement()
                self.state = 281
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.return_statement()
                self.state = 284
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 286
                self.method_invo_statement()
                self.state = 287
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 289
                self.assignment_statement()
                self.state = 290
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 292
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN_EQ(self):
            return self.getToken(BKOOLParser.ASSIGN_EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = BKOOLParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.lhs()
            self.state = 296
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 297
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def prefix_attribute_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Prefix_attribute_invoContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.operands(0)
                self.state = 301
                self.index_represent()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.prefix_attribute_invo(0)
                self.state = 304
                self.match(BKOOLParser.DOT)
                self.state = 305
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_attribute_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def prefix_attribute_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Prefix_attribute_invoContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_prefix_attribute_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_attribute_invo" ):
                return visitor.visitPrefix_attribute_invo(self)
            else:
                return visitor.visitChildren(self)



    def prefix_attribute_invo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Prefix_attribute_invoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_prefix_attribute_invo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 310
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 311
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 312
                self.exp()
                self.state = 313
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 4:
                self.state = 315
                self.match(BKOOLParser.THIS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 324
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 318
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 319
                        self.match(BKOOLParser.DOT)
                        self.state = 320
                        self.match(BKOOLParser.ID)
                        self.state = 321
                        self.list_args_wrapped()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 322
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 323
                        self.index_represent()
                        pass

             
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def bool_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_expContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKOOLParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(BKOOLParser.IF)
            self.state = 330
            self.bool_exp()
            self.state = 331
            self.match(BKOOLParser.THEN)
            self.state = 332
            self.statement()
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 333
                self.match(BKOOLParser.ELSE)
                self.state = 334
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_EQ(self):
            return self.getToken(BKOOLParser.ASSIGN_EQ, 0)

        def int_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Int_expContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Int_expContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKOOLParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKOOLParser.FOR)
            self.state = 338
            self.match(BKOOLParser.ID)
            self.state = 339
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 340
            self.int_exp()
            self.state = 341
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 342
            self.int_exp()
            self.state = 343
            self.match(BKOOLParser.DO)
            self.state = 344
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKOOLParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(BKOOLParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKOOLParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKOOLParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def return_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Return_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKOOLParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BKOOLParser.RETURN)
            self.state = 351
            self.return_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj_methodInvo(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_methodInvoContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_statement" ):
                return visitor.visitMethod_invo_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_statement(self):

        localctx = BKOOLParser.Method_invo_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method_invo_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.obj_methodInvo()
            self.state = 354
            self.match(BKOOLParser.DOT)
            self.state = 355
            self.match(BKOOLParser.ID)
            self.state = 356
            self.list_args_wrapped()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_methodInvoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_methodInvo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_methodInvo" ):
                return visitor.visitObj_methodInvo(self)
            else:
                return visitor.visitChildren(self)




    def obj_methodInvo(self):

        localctx = BKOOLParser.Obj_methodInvoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_obj_methodInvo)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.operands(0)
                self.state = 361
                self.match(BKOOLParser.DOT)
                self.state = 362
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.operands(0)
                self.state = 365
                self.match(BKOOLParser.DOT)
                self.state = 366
                self.match(BKOOLParser.ID)
                self.state = 367
                self.list_args_wrapped()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 369
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 370
                self.exp()
                self.state = 371
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 373
                self.operands(0)
                self.state = 374
                self.index_represent()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 376
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 377
                self.match(BKOOLParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_exp" ):
                return visitor.visitBool_exp(self)
            else:
                return visitor.visitChildren(self)




    def bool_exp(self):

        localctx = BKOOLParser.Bool_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_bool_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_int_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_exp" ):
                return visitor.visitInt_exp(self)
            else:
                return visitor.visitChildren(self)




    def int_exp(self):

        localctx = BKOOLParser.Int_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_int_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_exp" ):
                return visitor.visitReturn_exp(self)
            else:
                return visitor.visitChildren(self)




    def return_exp(self):

        localctx = BKOOLParser.Return_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.exp1(0)
                self.state = 387
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 388
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.exp2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.exp1(3) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.exp3()
                self.state = 405
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.AND or _la==BKOOLParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 406
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.exp3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKOOLParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.exp4()
                self.state = 412
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 413
                self.exp3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKOOLParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.exp5()
                self.state = 419
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 420
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.exp5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKOOLParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp5)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.exp6()
                self.state = 426
                self.match(BKOOLParser.CONCAT)
                self.state = 427
                self.exp5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.exp6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(BKOOLParser.NOT)
                self.state = 433
                self.exp6()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 438
                self.exp7()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.operands(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def obj_create(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_createContext,0)


        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)



    def operands(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.OperandsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_operands, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 443
                self.literals()
                pass

            elif la_ == 2:
                self.state = 444
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 445
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 446
                self.exp()
                self.state = 447
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 4:
                self.state = 449
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 5:
                self.state = 450
                self.obj_create()
                pass

            elif la_ == 6:
                self.state = 451
                self.match(BKOOLParser.NIL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 463
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 454
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 455
                        self.index_represent()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 456
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 457
                        self.match(BKOOLParser.DOT)
                        self.state = 458
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 459
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 460
                        self.match(BKOOLParser.DOT)
                        self.state = 461
                        self.match(BKOOLParser.ID)
                        self.state = 462
                        self.list_args_wrapped()
                        pass

             
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_representContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_OPEN(self):
            return self.getToken(BKOOLParser.SQUARE_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SQUARE_CLOSE(self):
            return self.getToken(BKOOLParser.SQUARE_CLOSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_represent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_represent" ):
                return visitor.visitIndex_represent(self)
            else:
                return visitor.visitChildren(self)




    def index_represent(self):

        localctx = BKOOLParser.Index_representContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_represent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 469
            self.exp()
            self.state = 470
            self.match(BKOOLParser.SQUARE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_create" ):
                return visitor.visitObj_create(self)
            else:
                return visitor.visitChildren(self)




    def obj_create(self):

        localctx = BKOOLParser.Obj_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_obj_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(BKOOLParser.NEW)
            self.state = 473
            self.match(BKOOLParser.ID)
            self.state = 474
            self.list_args_wrapped()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_args_wrappedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def list_exps_as_args(self):
            return self.getTypedRuleContext(BKOOLParser.List_exps_as_argsContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_args_wrapped

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_args_wrapped" ):
                return visitor.visitList_args_wrapped(self)
            else:
                return visitor.visitChildren(self)




    def list_args_wrapped(self):

        localctx = BKOOLParser.List_args_wrappedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_args_wrapped)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 477
            self.list_exps_as_args()
            self.state = 478
            self.match(BKOOLParser.ROUND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exps_as_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_exps_as_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exps_as_args" ):
                return visitor.visitList_exps_as_args(self)
            else:
                return visitor.visitChildren(self)




    def list_exps_as_args(self):

        localctx = BKOOLParser.List_exps_as_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_exps_as_args)
        self._la = 0 # Token type
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.exp()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 481
                    self.match(BKOOLParser.COMMA)
                    self.state = 482
                    self.exp()
                    self.state = 487
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKOOLParser.ROUND_CLOSE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_replica(self):
            return self.getTypedRuleContext(BKOOLParser.Literal_replicaContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKOOLParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_literals)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.literal_replica()
                pass
            elif token in [BKOOLParser.CURLY_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = BKOOLParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def literal_replica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Literal_replicaContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Literal_replicaContext,i)


        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BKOOLParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 498
            self.literal_replica()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 499
                self.match(BKOOLParser.COMMA)
                self.state = 500
                self.literal_replica()
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 506
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_replicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal_replica

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_replica" ):
                return visitor.visitLiteral_replica(self)
            else:
                return visitor.visitChildren(self)




    def literal_replica(self):

        localctx = BKOOLParser.Literal_replicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal_replica)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(BKOOLParser.INTEGER_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 511
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 512
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 513
                self.boolean_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.prefix_attribute_invo_sempred
        self._predicates[35] = self.exp1_sempred
        self._predicates[42] = self.operands_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prefix_attribute_invo_sempred(self, localctx:Prefix_attribute_invoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def operands_sempred(self, localctx:OperandsContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




