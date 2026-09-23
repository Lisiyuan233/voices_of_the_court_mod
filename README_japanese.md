# よくある質問

## 1. ダイアログボックスが表示されない
このModを実行するには、追加のバックエンドプログラムが必要です。ローカライズされたバックエンドプログラムをこちらからダウンロードしてください：[https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest)。ダウンロードした.exeファイルを開くと、自動的にインストールされます。

## 2. API設定の問題
公式のDeepSeek APIの使用を推奨します。対話モデル接続のドロップダウンメニューで、`custom(openai-compatible)` ページを選択し、以下のように設定してください：
- サーバーURL: `https://api.deepseek.com/beta`
- APIキー: [https://platform.deepseek.com](https://platform.deepseek.com) で申請した自身のAPIキーを入力してください。

OpenAIやOpenRouterも互換性があるはずです。

## 3. インストール後、バックエンドプログラムが実行されているのにダイアログボックスが表示されない
**解決策**: ローカライズModを使用する必要があります。

インストール方法（いずれかを選択）：
1. ダウンロードしたローカライズModファイルを解凍後、Steam Workshopディレクトリ内の元のModファイルを直接上書きします。
2. 解凍したModフォルダ `voices_of_the_court_mod-1.2.1-beta` をゲームのModフォルダに配置します。次に、メモ帳を使用して `Documents\Paradox Interactive\Crusader Kings III\mod` フォルダに `voices_of_the_court_mod-1.2.1-beta.mod` という名前の新しいファイルを作成し、以下の内容を記述します：
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [あなたのPCユーザー名] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

ローカライズModをインストールして有効にしてもダイアログボックスが表示されない場合は、CK3のユーザーフォルダパスが正しく設定されていないか、ゲームがアイアンマンモードになっている可能性があります。このModはアイアンマンモードでは動作しません。

## 4. チャットウィンドウを開くと赤文字で "TypeError: Cannot read properties of undefined (reading 'playerID')" というエラーが出る
**解決策**: `Documents\Paradox Interactive\Crusader Kings III` 内に `run` という名前のフォルダを作成します。そのフォルダに入り、 `votc.txt` という名前のテキストファイルを作成します。

## 5. キャラクターと話す際、最近の記憶が読み込まれない
**解決策**:
1. これは原作者のバックエンドプログラムにある小さなバグです。ローカライズされたバックエンドをダウンロードすることで解決します。
2. メモリトークンの制限が原因である可能性もあります。バックエンドプログラムの設定ページで `max memory tokens` のサイズを調整してください。メモリトークンを調整した後は、 `max new tokens` も増やす必要があります。 `max new tokens` は `max memory tokens` よりも大きく設定するのが最適です。

## 6. バックエンドプログラムを再起動するとプロンプト生成スクリプトが元に戻ってしまう
**解決策**:
`custom` フォルダに別のファイルとして保存してください。

## ライセンスと帰属

### Mod情報
- **Mod名**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **ライセンス**: GNU General Public License v3.0 (GPLv3)
- **対応CK3バージョン**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### GPLv3通知
このプログラムはフリーソフトウェアです：Free Software Foundationによって公開されたGNU General Public Licenseの条項に従って、このプログラムを再配布および/または変更することができます。ライセンスのバージョン3、または（あなたの選択により）それ以降のバージョンのいずれかです。

このプログラムは有用であることを期待して配布されていますが、商品性や特定目的への適合性の黙示的保証を含め、いかなる保証もありません。詳細についてはGNU General Public Licenseを参照してください。

あなたはこのプログラムと一緒にGNU General Public Licenseのコピーを受け取っているはずです。そうでない場合は、<https://www.gnu.org/licenses/>を参照してください。
