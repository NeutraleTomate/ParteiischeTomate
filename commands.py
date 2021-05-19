from functionsUtility import help, send, clear
from functionsMemes import wahrheit, nein, xxtime, write
from functionsDestiny import throne, pit, vog, dsc, gos, wish, vault, wp, wpx

commands = { # Diese Commands werden auch erkannt, wenn die Nachricht noch etwas anderes außer dem Wort enthält(z.B. "!wish 4", "!dsc loot",...)
    # utility
    "help": help,
    "send": send,
    "clear": clear,

    # memes
    "wahrheit": wahrheit,
    "nein": nein,
    "xxtime": xxtime,
    "write": write,

    # Destiny commands

    "throne": throne,
    "pit": pit,
    "heresy": pit,
    "vog":vog,
    "dsc": dsc,
    "gos": gos,
    "wish": wish,
    "vault": vault,

}

exactCommands = { # Diese Commands müssen exakt erkannt werden
    "wp": wp,
    "wpx": wpx,

}
