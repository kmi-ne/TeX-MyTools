# unicode-math-snippets

## 対象

VS Code のスニペットファイルの扱い方と記法，およびスニペットを利用した編集について既に知っている方が対象です．

## 背景

$\text{Lua}\LaTeX$ や $\text{Xe}\LaTeX$ では，[`unicode-math`パッケージ](https://ctan.org/pkg/unicode-math)によって数学記号の Unicode文字入力が可能となります．例えば，
$$\int_{\omega} \partial\Omega = \int_{\Omega} H(\phi) dx$$
という数式を出力したい場合，
```latex
\[\int_{\omega} \partial\Omega = \int_{\Omega} H(\phi) dx\]
```
と書く代わりに，直接
```latex
\[∫_𝜔 𝜕𝛺 = ∫_𝛺 H(𝜙) dx\]
```
と書くことが許容されます．これはファイルの可読性を高める上で非常に魅力的な機能です．

一方で，このような Unicode文字入力は極めて手間のかかる作業であり，このことが上記機能の活用を妨げる要因となっていました．

## 用途

`unicode-math-snippets` は，上記の課題を解消するために制作された VS Code用スニペットファイル群です．具体的には，[`unicode-math` の記号表](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unimath-symbols.pdf)に掲載されている全ての Unicode文字を，対応するマクロ名によって直接入力できるようにしたものです．

例えば，上記の記号表によると，Unicode符号位置 U+0222B（`∫`, integral operator）と U+1D482（`𝒂`, mathematical bold italic small a）に対応するマクロ名は，それぞれ `\int` と `\mbfita` となっています．これに対応して，本スニペットファイルには， `∫` と `𝒂` を入力するためのスニペットが以下のように登録されています．

```json
{
    (略)
    "0222B": {
        "scope": "latex",
        "prefix": "/int",
        "body": "∫",
        "description": [
            "∫",
            "integral operator",
            "\r"
        ]
    },
    (略)
    "1D482": {
        "scope": "latex",
        "prefix": "/mbfita",
        "body": "𝒂",
        "description": [
            "𝒂",
            "mathematical bold italic small a",
            "\r"
        ]
    },
    (略)
}
```

なお，IntelliSence上でマクロ（`\int`, `\mbfita`）と prefix との表記上の区別が付かなくなることを防ぐため，各 prefix の先頭には `\` ではなく `/` を付しています．

同様に，他の記号についても，記号表に掲載されているマクロ `\foo` に対応して，Unicode文字を入力するための prefix `/foo` が登録されています．記号とマクロ名の一覧は [`unicode-math` の記号表](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unimath-symbols.pdf)をご覧ください．

## ファイル
以下のスニペットファイルが含まれています．
- [`unicode-math-snippets.code-snippets`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/unicode-math-snippets.code-snippets)：全てのスニペットを scope指定付で登録したもの．
- [`unicode-math-snippets_no-scope.code-snippets`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/unicode-math-snippets_no-scope.code-snippets)：全てのスニペットを scope指定なしで登録したもの．`latex.json` での使用を想定．
- [`01_mathopen.code-snippets`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/01_mathopen.code-snippets) ～ [`13_mathalpha.code-snippets`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/13_mathalpha.code-snippets)（全13個）：`unicode-math-snippets.code-snippets` を数式クラス別に分割したもの．
- `additional.code-snippets`（**未追加**）：上記のスニペットファイルには登録されていないが，個人的にあった方が便利と思われる prefix とスニペットを追加登録したもの．例えば，
  - 小文字斜体アルファ `𝛼` を入力するための `/alpha`（上記スニペットファイルでは `/mitalpha` のみ登録されている）．
  - `/langle`（`⟨`）と `/rangle`（`⟩`）を一つにまとめた `/lrangle`（`⟨⟩`）．

その他，以下のファイルが含まれています．
- [`macro_extract.py`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/macro_extract.py)：スニペットファイル生成用プログラム．「その他」の節を参照．
- [`unicode-math-table.tex`](https://github.com/kmi-ne/TeX-MyTools/blob/main/unicode-math-snippets/unicode-math-table.tex)：https://github.com/latex3/unicode-math/blob/master/unicode-math-table.tex のコピー．「その他」の節を参照．

## 使い方

設置は通常のスニペットファイルと同様です．グローバルに使う場合は，`unicode-math-snippets_no-scope.code-snippets` の中身を `latex.json`内にコピペしてください．特定プロジェクト等でローカルに使う場合は，`unicode-math-snippets.code-snippets` を `.vscode` ディレクトリ内に設置するなどしてください．

`additional.code-snippets` はお好みで追加してください．

## その他

`01_mathopen.code-snippets` ～ `13_mathalpha.code-snippets` は，`macro_extract.py`によって `unicode-math-table.tex` から抽出されています．`unicode-math-snippets.code-snippets` および `unicode-math-snippets_no-scope.code-snippets` は，それらを手動で結合させたものです．
