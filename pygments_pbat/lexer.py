from pygments.lexer import RegexLexer
from pygments.token import Comment, Keyword, String, Text, Literal, Name, Number


class PBatLexer(RegexLexer):
    name = 'PBAT'
    aliases = ['pbat']
    filenames = ['*.pbt']

    tokens = {
        'root': [
            (r'SET|UNSET|SAVEVARS|ECHO|MESSAGE|ADDWIDGET|CLEARWIDGETS|SETTITLE|EVAL|GOTO|IF|ELSE|ELSEIF|ENDIF|COPY|RM|RRM|FORMAT|MKDIR|REDIRFILE|UNMOUNT|FPRINT|LOADEXEC|KEEP|RETURN|EXIT|KILLSESS|SKIPBACK|LOADIMG|UNLOADIMG|PARSEPATH|SETAUTH|SETBIOS|SHUTDOWN|PEEKB|PEEKH|PEEKW|POKEB|POKEH|POKEW|GETDISKTYPE|PARSECNF|CYCLETRAY|LOADSRAM|REBOOTIOP', Keyword),
            (r'EQU|NEQ|GTE|GT|LTE|LT|EXISTS|MATCHES|FAIL|MODLOADED|ISIN|NOT', Keyword.Pseudo),
            (r'\$[a-zA-Z0-9_.]+\$', Name.Variable),
            (r'-?[0-9]+', Number.Integer),
            (r':[a0zA-Z0-9_]+', Name.Function),
            (r'"', String.Double, 'string'),
            (r'#.*$', Comment),
            (r'\s+', Text),
        ],
        'string': [
            (r'\^"', Literal.String.Escape),
            (r'\$[a-zA-Z0-9_.]+\$', Name.Variable),
            (r'[^\^"$]+', String.Double),
            (r'"', String.Double, '#pop')
        ]
    }
