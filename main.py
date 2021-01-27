import requests
import random

def run():

    # ファイルオープン
    file_name = 'the path of your file'
    f = open(file_name, 'r')

    # ファイルの中身全てを1つの文字列にする
    whole_str = f.read()

    # 改行で区切ってリスト化
    list_str = whole_str.split('\n\n')

    # リストの中からランダムで1つ選ぶ
    index = random.randint(0, len(list_str) - 1)
    actual_str = list_str[index]

    # LINE NotifyのWebページで作成した独自のTOKENを入れる
    TOKEN = 'your own token of LINE Notify'

    # 送信するメッセージの形式に変換
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': '\n' + actual_str}

    # LINE Notifyに送信
    requests.post('https://notify-api.line.me/api/notify', headers=TOKEN_dic, data=send_dic)

if __name__ == '__main__':
    run()
