from coc.cthulhu_messenger import CthulhuMessenger
from coc.charactors import load_charactors as coc_lc
from nanjamonja.nanja_messenger import NanjaMessenger
from freechat.free_messenger import FreeChatMessenger


class MessageManager():

    def __init__(self, input_mode, conf):
        if input_mode == 'coc':
            self.messenger = CthulhuMessenger(coc_lc(conf))
        elif input_mode == 'nanjamonja':
            self.messenger = NanjaMessenger()
        elif input_mode == 'free':
            self.messenger = FreeChatMessenger()
        else:
            raise ValueError('invalid mode value.')

        self.mode = str(self.messenger)


    def __call__(self, input_msg, player):
        msg = self.messenger(input_msg, player)
        if self.mode == 'coc':
            indicate = 'PL:' + player + '\n'
            msg = indicate + msg
            
        return msg


    def help(self, help_at, sound_map):
        if help_at == 'coc':
            msg = CthulhuMessenger.show_help()
        elif help_at == 'nanjamonja':
            msg = NanjaMessenger.show_help()
        elif help_at == 'free':
            msg = FreeChatMessenger.show_help()
        elif help_at == 'main':
            msg = '**yasumi: Main-commands**\n'\
                    '`/yasumi init [hoge]`: システムを_hoge_でイニシャライズ(省略時: free)\n'\
                    '`/[fuga]`: システムに応じたコマンドを実行\n'\
                    '`#[piyo]`: 対応したサウンドを再生\n'\
                    '`/yasumi help [heke]`: システム_heke_のヘルプを表示(省略時: main)\n'\
                    '`/bye`: yasumiを終了'
        elif help_at == 'sound':
            msg = '**yasumi: Sound-commands**\n'
            for idx, item in enumerate(sound_map.items()):
                command, sound_file = item[0], item[1]
                msg_head = '`' + command + '`: '
                msg_tail = sound_file + '\n' if idx + 1 < len(sound_map) else sound_file
                msg += msg_head + msg_tail
        else:
            raise ValueError('invalid mode value.')

        return msg

