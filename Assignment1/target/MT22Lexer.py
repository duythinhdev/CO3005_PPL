# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# 2052612 MAI HUU NGHIA



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01b9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\61\7\61\u0138\n\61\f\61\16\61\u013b\13\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\7\62\u0143\n\62\f\62\16\62\u0146")
        buf.write("\13\62\3\62\3\62\3\62\3\62\3\62\3\63\6\63\u014e\n\63\r")
        buf.write("\63\16\63\u014f\3\63\3\63\3\64\3\64\3\64\7\64\u0157\n")
        buf.write("\64\f\64\16\64\u015a\13\64\3\64\3\64\3\64\7\64\u015f\n")
        buf.write("\64\f\64\16\64\u0162\13\64\5\64\u0164\n\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\5\65\u016b\n\65\3\65\5\65\u016e\n\65\3\65")
        buf.write("\3\65\3\65\5\65\u0173\n\65\3\65\3\65\3\66\3\66\5\66\u0179")
        buf.write("\n\66\3\66\3\66\3\66\3\66\3\67\3\67\6\67\u0181\n\67\r")
        buf.write("\67\16\67\u0182\38\38\38\39\39\79\u018a\n9\f9\169\u018d")
        buf.write("\139\3:\3:\5:\u0191\n:\3:\6:\u0194\n:\r:\16:\u0195\3;")
        buf.write("\3;\7;\u019a\n;\f;\16;\u019d\13;\3<\3<\7<\u01a1\n<\f<")
        buf.write("\16<\u01a4\13<\3<\5<\u01a7\n<\3<\3<\3=\3=\7=\u01ad\n=")
        buf.write("\f=\16=\u01b0\13=\3=\3=\3=\3=\3=\3>\3>\3>\3\u0144\2?\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2")
        buf.write("u8w9y:{;\3\2\f\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3\2\63")
        buf.write(";\3\2\62;\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\4\2GG")
        buf.write("gg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\2\u01c8\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\3}\3\2\2\2\5\u0082\3\2\2\2\7\u0088\3\2\2\2\t")
        buf.write("\u0090\3\2\2\2\13\u0093\3\2\2\2\r\u0098\3\2\2\2\17\u009e")
        buf.write("\3\2\2\2\21\u00a4\3\2\2\2\23\u00a8\3\2\2\2\25\u00b1\3")
        buf.write("\2\2\2\27\u00b4\3\2\2\2\31\u00bc\3\2\2\2\33\u00c3\3\2")
        buf.write("\2\2\35\u00ca\3\2\2\2\37\u00cf\3\2\2\2!\u00d5\3\2\2\2")
        buf.write("#\u00da\3\2\2\2%\u00de\3\2\2\2\'\u00e7\3\2\2\2)\u00ea")
        buf.write("\3\2\2\2+\u00f2\3\2\2\2-\u00f8\3\2\2\2/\u00fa\3\2\2\2")
        buf.write("\61\u00fc\3\2\2\2\63\u00fe\3\2\2\2\65\u0100\3\2\2\2\67")
        buf.write("\u0102\3\2\2\29\u0104\3\2\2\2;\u0107\3\2\2\2=\u010a\3")
        buf.write("\2\2\2?\u010d\3\2\2\2A\u0110\3\2\2\2C\u0112\3\2\2\2E\u0115")
        buf.write("\3\2\2\2G\u0117\3\2\2\2I\u011a\3\2\2\2K\u011d\3\2\2\2")
        buf.write("M\u011f\3\2\2\2O\u0121\3\2\2\2Q\u0123\3\2\2\2S\u0125\3")
        buf.write("\2\2\2U\u0127\3\2\2\2W\u0129\3\2\2\2Y\u012b\3\2\2\2[\u012d")
        buf.write("\3\2\2\2]\u012f\3\2\2\2_\u0131\3\2\2\2a\u0133\3\2\2\2")
        buf.write("c\u013e\3\2\2\2e\u014d\3\2\2\2g\u0163\3\2\2\2i\u0172\3")
        buf.write("\2\2\2k\u0176\3\2\2\2m\u0180\3\2\2\2o\u0184\3\2\2\2q\u0187")
        buf.write("\3\2\2\2s\u018e\3\2\2\2u\u0197\3\2\2\2w\u019e\3\2\2\2")
        buf.write("y\u01aa\3\2\2\2{\u01b6\3\2\2\2}~\7c\2\2~\177\7w\2\2\177")
        buf.write("\u0080\7v\2\2\u0080\u0081\7q\2\2\u0081\4\3\2\2\2\u0082")
        buf.write("\u0083\7d\2\2\u0083\u0084\7t\2\2\u0084\u0085\7g\2\2\u0085")
        buf.write("\u0086\7c\2\2\u0086\u0087\7m\2\2\u0087\6\3\2\2\2\u0088")
        buf.write("\u0089\7d\2\2\u0089\u008a\7q\2\2\u008a\u008b\7q\2\2\u008b")
        buf.write("\u008c\7n\2\2\u008c\u008d\7g\2\2\u008d\u008e\7c\2\2\u008e")
        buf.write("\u008f\7p\2\2\u008f\b\3\2\2\2\u0090\u0091\7f\2\2\u0091")
        buf.write("\u0092\7q\2\2\u0092\n\3\2\2\2\u0093\u0094\7g\2\2\u0094")
        buf.write("\u0095\7n\2\2\u0095\u0096\7u\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\f\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7c\2\2\u009a")
        buf.write("\u009b\7n\2\2\u009b\u009c\7u\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\16\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7n\2\2\u00a0")
        buf.write("\u00a1\7q\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7v\2\2\u00a3")
        buf.write("\20\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7q\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9")
        buf.write("\u00aa\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac")
        buf.write("\u00ad\7v\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7q\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7h\2\2\u00b3\26\3\2\2\2\u00b4\u00b5\7k\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7i\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\30\3\2\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7v\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7t\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\32\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write("\u00c8\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\34\3\2\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7w\2\2\u00cd")
        buf.write("\u00ce\7g\2\2\u00ce\36\3\2\2\2\u00cf\u00d0\7y\2\2\u00d0")
        buf.write("\u00d1\7j\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7n\2\2\u00d3")
        buf.write("\u00d4\7g\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7x\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7f\2\2\u00d9")
        buf.write("\"\3\2\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7w\2\2\u00dc")
        buf.write("\u00dd\7v\2\2\u00dd$\3\2\2\2\u00de\u00df\7e\2\2\u00df")
        buf.write("\u00e0\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7w\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6&\3\2\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7h\2\2\u00e9(\3\2\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee\7g\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7v\2\2\u00f1")
        buf.write("*\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7{\2\2\u00f7")
        buf.write(",\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9.\3\2\2\2\u00fa\u00fb")
        buf.write("\7/\2\2\u00fb\60\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd\62\3")
        buf.write("\2\2\2\u00fe\u00ff\7\61\2\2\u00ff\64\3\2\2\2\u0100\u0101")
        buf.write("\7\'\2\2\u0101\66\3\2\2\2\u0102\u0103\7#\2\2\u01038\3")
        buf.write("\2\2\2\u0104\u0105\7(\2\2\u0105\u0106\7(\2\2\u0106:\3")
        buf.write("\2\2\2\u0107\u0108\7~\2\2\u0108\u0109\7~\2\2\u0109<\3")
        buf.write("\2\2\2\u010a\u010b\7?\2\2\u010b\u010c\7?\2\2\u010c>\3")
        buf.write("\2\2\2\u010d\u010e\7#\2\2\u010e\u010f\7?\2\2\u010f@\3")
        buf.write("\2\2\2\u0110\u0111\7>\2\2\u0111B\3\2\2\2\u0112\u0113\7")
        buf.write(">\2\2\u0113\u0114\7?\2\2\u0114D\3\2\2\2\u0115\u0116\7")
        buf.write("@\2\2\u0116F\3\2\2\2\u0117\u0118\7@\2\2\u0118\u0119\7")
        buf.write("?\2\2\u0119H\3\2\2\2\u011a\u011b\7<\2\2\u011b\u011c\7")
        buf.write("<\2\2\u011cJ\3\2\2\2\u011d\u011e\7*\2\2\u011eL\3\2\2\2")
        buf.write("\u011f\u0120\7+\2\2\u0120N\3\2\2\2\u0121\u0122\7]\2\2")
        buf.write("\u0122P\3\2\2\2\u0123\u0124\7_\2\2\u0124R\3\2\2\2\u0125")
        buf.write("\u0126\7\60\2\2\u0126T\3\2\2\2\u0127\u0128\7.\2\2\u0128")
        buf.write("V\3\2\2\2\u0129\u012a\7=\2\2\u012aX\3\2\2\2\u012b\u012c")
        buf.write("\7<\2\2\u012cZ\3\2\2\2\u012d\u012e\7}\2\2\u012e\\\3\2")
        buf.write("\2\2\u012f\u0130\7\177\2\2\u0130^\3\2\2\2\u0131\u0132")
        buf.write("\7?\2\2\u0132`\3\2\2\2\u0133\u0134\7\61\2\2\u0134\u0135")
        buf.write("\7\61\2\2\u0135\u0139\3\2\2\2\u0136\u0138\n\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013c\u013d\b\61\2\2\u013db\3\2\2\2\u013e\u013f")
        buf.write("\7\61\2\2\u013f\u0140\7,\2\2\u0140\u0144\3\2\2\2\u0141")
        buf.write("\u0143\13\2\2\2\u0142\u0141\3\2\2\2\u0143\u0146\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0147")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7,\2\2\u0148")
        buf.write("\u0149\7\61\2\2\u0149\u014a\3\2\2\2\u014a\u014b\b\62\2")
        buf.write("\2\u014bd\3\2\2\2\u014c\u014e\t\3\2\2\u014d\u014c\3\2")
        buf.write("\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\b\63\2\2\u0152")
        buf.write("f\3\2\2\2\u0153\u0164\7\62\2\2\u0154\u0158\t\4\2\2\u0155")
        buf.write("\u0157\t\5\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u0160\3")
        buf.write("\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\7a\2\2\u015c\u015f")
        buf.write("\t\5\2\2\u015d\u015f\t\5\2\2\u015e\u015b\3\2\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3")
        buf.write("\2\2\2\u0163\u0153\3\2\2\2\u0163\u0154\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0166\b\64\3\2\u0166h\3\2\2\2\u0167\u016d")
        buf.write("\5g\64\2\u0168\u016e\5q9\2\u0169\u016b\5q9\2\u016a\u0169")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016e\5s:\2\u016d\u0168\3\2\2\2\u016d\u016a\3\2\2\2\u016e")
        buf.write("\u0173\3\2\2\2\u016f\u0170\5q9\2\u0170\u0171\5s:\2\u0171")
        buf.write("\u0173\3\2\2\2\u0172\u0167\3\2\2\2\u0172\u016f\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0175\b\65\4\2\u0175j\3\2\2")
        buf.write("\2\u0176\u0178\7$\2\2\u0177\u0179\5m\67\2\u0178\u0177")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017b\7$\2\2\u017b\u017c\3\2\2\2\u017c\u017d\b\66\5\2")
        buf.write("\u017dl\3\2\2\2\u017e\u0181\n\6\2\2\u017f\u0181\5o8\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183n")
        buf.write("\3\2\2\2\u0184\u0185\7^\2\2\u0185\u0186\t\7\2\2\u0186")
        buf.write("p\3\2\2\2\u0187\u018b\7\60\2\2\u0188\u018a\t\5\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018cr\3\2\2\2\u018d\u018b\3\2\2")
        buf.write("\2\u018e\u0190\t\b\2\2\u018f\u0191\t\t\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192")
        buf.write("\u0194\t\5\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196t\3\2\2")
        buf.write("\2\u0197\u019b\t\n\2\2\u0198\u019a\t\13\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019cv\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u01a2\7$\2\2\u019f\u01a1\5m\67\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7")
        buf.write("\7\2\2\3\u01a6\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a9\b<\6\2\u01a9x\3\2\2\2\u01aa")
        buf.write("\u01ae\7$\2\2\u01ab\u01ad\5m\67\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2")
        buf.write("\7^\2\2\u01b2\u01b3\n\7\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\b=\7\2\u01b5z\3\2\2\2\u01b6\u01b7\13\2\2\2\u01b7")
        buf.write("\u01b8\b>\b\2\u01b8|\3\2\2\2\27\2\u0139\u0144\u014f\u0158")
        buf.write("\u015e\u0160\u0163\u016a\u016d\u0172\u0178\u0180\u0182")
        buf.write("\u018b\u0190\u0195\u019b\u01a2\u01a6\u01ae\t\b\2\2\3\64")
        buf.write("\2\3\65\3\3\66\4\3<\5\3=\6\3>\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    NEQUAL = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    CONCAT = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    DOT = 41
    COMMA = 42
    SM = 43
    COLON = 44
    LCB = 45
    RCB = 46
    ASS = 47
    LINE_CMT = 48
    BLOCK_CMT = 49
    WS = 50
    INTEGERLIT = 51
    FLOATLIT = 52
    STRINGLIT = 53
    ID = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "NEQUAL", "LT", "LTE", "GT", "GTE", "CONCAT", "LB", "RB", "LSB", 
            "RSB", "DOT", "COMMA", "SM", "COLON", "LCB", "RCB", "ASS", "LINE_CMT", 
            "BLOCK_CMT", "WS", "INTEGERLIT", "FLOATLIT", "STRINGLIT", "ID", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SM", "COLON", 
                  "LCB", "RCB", "ASS", "LINE_CMT", "BLOCK_CMT", "WS", "INTEGERLIT", 
                  "FLOATLIT", "STRINGLIT", "StrCha", "Esc", "Deci", "Expo", 
                  "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INTEGERLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[52] = self.STRINGLIT_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGERLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            y = str(self.text)
            raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            y = str(self.text)
            raise IllegalEscape(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            raise ErrorToken(self.text)

     


