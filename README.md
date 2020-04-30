# mikochiku_alarm

さくらみこチャンネルの配信が開始されると音でお知らせします  
ゲリラ、配信開始の遅れ、枠BANによる次枠取り直しなど配信を見逃してしまいそうな時に重宝します  

* 枠バグでもアラームが鳴るようになっています
* 自動でブラウザで配信を開いてくれる機能付き
* 自分の好きなアラームの音を設定することもできます

アラームの音の設定は`mikochiku_alarm.exe`と同じフォルダーに`alarm.mp3`と名付けた好きな音源を置いてみこ畜アラームを起動してください  
アラームは５回繰り返します  
みこ畜アラームは**1つだけ**起動するようにしてください  
動かない、機能追加の要望などありましたらお知らせください  

みこちゃんのバイオで枠BAN＋枠バグで配信してるのに気づかなかった人がいたのをみて早急にこちらを作りました  
フォルダーの中にエリート工場の曲を勝手ながら入れてあるのでそちらをalarm.mp3にしてもいいです  
元からあるalarm.mp3は同じものをexeに入れ込んであるので消してもらって構いません  

なおメンバー限定配信ではアラームは作動しません。ログインが必要な情報は集めることができません。

## 言語選択

右下の`language`より言語を選択してから再起動すると反映されます。  


## リポジトリーの運用方法

* developではなくmasterへmergeする（初めての人でも参加しやすいようにしました）
* コラボレータは自分が出したPRを自分で承認してマージしてはならない(コードの品質を守るため)
