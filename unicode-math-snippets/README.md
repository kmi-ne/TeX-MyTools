# unicode-math-snippets：`unicode-math` ユーザーのための Unicode 文字入力補助

この記事（ `README.md` ）は，[TeX ＆ LaTeX Advent Calendar 2024](https://adventar.org/calendars/10647) の5日目の記事です．大層な見出しですが，羊頭狗肉だと思ってください．

（4日目は [ut さん](http://texuttex.g2.xrea.com/AdventCal2024.html)です．）


## 予備知識

以下の2つを既知とします．

- VS Code のスニペットファイルの基本的な使い方
- `unicode-math` の基本的な使い方．特に，文字種指定コマンド（例：`\symbfit`）と，立体・イタリック体関連のパッケージオプション（例：`math-style`）についての知識

> [!TIP]
> なお，`unicode-math` の名前を初めて聞いた方は，
> 
> - [unicode-mathとかdiffcoeffとか](https://qiita.com/Niccori250km/items/af798fe64419adfc3877)（ Niccori250km ）
> - [徹底解説！ unicode-mathパッケージでココが変わる](https://qiita.com/zr_tex8r/items/648b024e55126f3ba077)（ zr_tex8r ）
> - [unicode-math におけるラテン文字・ギリシャ文字とパッケージオプションを理解する](https://qiita.com/Yarakashi_Kikohshi/items/ac3a31420ad6f754db99)（ Yarakashi_Kikohshi ）
> - [unicode-math の注意するべき落とし穴](https://qiita.com/Yarakashi_Kikohshi/items/5404d1b67144de5be51f)（ Yarakashi_Kikohshi ）
> - [unicode-math を完全に理解したい話(1)](https://zrbabbler.hatenablog.com/entry/20180915/1537031499)（ zr_tex8r ）
> 
> などの記事を参照してみてください（もちろん[公式ドキュメント](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unicode-math.pdf)も）．

> [!TIP]
> 文字種コマンドと立体・イタリック体関連のパッケージオプションについては，「[unicode-math におけるラテン文字・ギリシャ文字とパッケージオプションを理解する](https://qiita.com/Yarakashi_Kikohshi/items/ac3a31420ad6f754db99)」や，[公式ドキュメント](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unicode-math.pdf)の §4 "Unicode maths font setup" などを参照してください．

## 要約

困難に対しては，パワー系ソリューションが求められる時もあります．

- [`unicode-math`](https://ctan.org/pkg/unicode-math) がサポートする Unicode 文字全てを入力できる，VS Code 用の巨大なスニペットファイルを作った．また，利便性を高めるための追加スニペットも作った．
- [`unicode-math-snippets.code-snippets`](/unicode-math-snippets.code-snippets)（本体）と [`additional.code-snippets`](/additional.code-snippets)（追加スニペット）の中身を `latex.json` にコピペすることで使用できる．
- 例えば，$\forall$ を出力するために `∀` を Unicode 文字入力したければ， `forall` とタイプし，サジェストから `/forall` を選択すればよい（`\` ではなく `/` であることに注意）．実際にはタイプ数はもっと短く済む．
- 他の Unicode 文字についても，[`unicode-math` の記号表](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unimath-symbols.pdf)に掲載されているマクロ名をタイプすることで，該当文字を入力できる．
- 追加スニペットについては「[追加スニペット](#追加スニペット)」の節を参照．

<div align="center">
    <img src="assets/sample.gif" style="max-width: 650px; min-width: 350px; width: 100%">
</div>


## ファイル
以下のスニペットファイルが含まれています．
- [`unicode-math-snippets.code-snippets`](/unicode-math-snippets.code-snippets)：全てのスニペット．`latex.json` での使用を想定．
- [`unicode-math-snippets_with-scope.code-snippets`](/unicode-math-snippets_with-scope.code-snippets)：上記ファイルに scope 指定を付けたもの．
- [`additional.code-snippets`](/additional.code-snippets)：上記のスニペットファイルには登録されていないが，個人的にあった方が便利と思われる prefix・スニペットを登録したもの．`latex.json` での使用を想定．
- [`additional_with-scope.code-snippets`](/additional_with-scope.code-snippets)：上記ファイルに scope 指定を付けたもの．

その他，以下のファイルが含まれています．
- [`01_mathopen.code-snippets`](/01_mathopen.code-snippets) ～ [`13_mathalpha.code-snippets`](/13_mathalpha.code-snippets)（全13個）：`unicode-math-snippets.code-snippets` を数式クラス別に分割したもの．
- [`macro_extract.py`](/macro_extract.py)：スニペットファイル生成に用いたスクリプト．「[その他](#その他)」の節を参照．



## 背景

よく知られているように，$\text{Lua}\LaTeX$ や $\text{Xe}\LaTeX$ では，[`unicode-math`](https://ctan.org/pkg/unicode-math) によって数学記号の Unicode 文字入力が可能となります．

例えば，
$$\forall \varepsilon > 0 \ \exists N \in \mathbb{N} \ \forall n \in \mathbb{N} \ (n > N \Rightarrow |a_n - b| < \varepsilon)$$
という式を出力したい場合，
```latex
\[
  \forall \varepsilon > 0 \ \exists N \in \mathbb{N} \ \forall n \in \mathbb{N} \ (n > N \Rightarrow |a_n - b| < \varepsilon)
\]
```
と書く代わりに，直接
```latex
\[
  ∀ 𝜀 > 0 \ ∃ N ∈ ℕ \ ∀ n ∈ ℕ \ (n > N ⇒ |a_n - b| < 𝜀)
\]
```
と書くことが許容されます．これはファイルの可読性を高める上で非常に魅力的な機能です．

一方で，このような Unicode 文字を入力するのは極めて手間のかかる作業であり，このことが上記機能の活用を妨げる要因となっていました．

---

[`unicode-math-snippets`](.) は，上記の課題を解消するために制作された VS Code 用スニペットファイル群です．具体的には，[`unicode-math` の記号表](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unimath-symbols.pdf)に掲載されている全ての Unicode 文字を，対応するマクロ名によって直接入力できるようにしたものです．

[`unicode-math-snippets`](.) は「本体」と「追加スニペット」からなります．

## 本体

> 以下のファイルからなります．ファイルの使用方法は「[ファイルの設置](#ファイルの設置)」の節を見てください．
> - [`unicode-math-snippets.code-snippets`](/unicode-math-snippets.code-snippets)：全てのスニペット．`latex.json` での使用を想定．
> - [`unicode-math-snippets_with-scope.code-snippets`](/unicode-math-snippets_with-scope.code-snippets)：上記ファイルに scope 指定を付けたもの．

`unicode-math` の記号表によると，U+0222B（`∫`, integral operator）に対応するマクロは `\int` となっています．これに対応して，本スニペットファイルには， `∫` を入力するためのスニペットが以下のように登録されています．

```json
{
    (略)
    "0222B": {
        "prefix": "/int",
        "body": "∫",
        "description": [
            "∫",
            "integral operator",
            "\r"
        ]
    },
    (略)
}
```

従って，`int` とタイプして，サジェストから `/int` を選択すれば，`∫` を入力することができます．

同様に，他の記号についても，記号表に掲載されているマクロ `\foo` に対応して，Unicode 文字を入力するための prefix `/foo` が登録されています．記号とマクロ名の一覧は [`unicode-math` の記号表](http://mirrors.ctan.org/macros/unicodetex/latex/unicode-math/unimath-symbols.pdf)をご覧ください．


## 追加スニペット

> 以下のファイルからなります．ファイルの使用方法は「[ファイルの設置](#ファイルの設置)」の節を見てください．
> - [`additional.code-snippets`](/additional.code-snippets)：本体のスニペットファイルには登録されていないが，個人的にあった方が便利と思われる prefix・スニペットを登録したもの．`latex.json` での使用を想定．
> - [`additional_with-scope.code-snippets`](/additional_with-scope.code-snippets)：上記ファイルに scope 指定を付けたもの．

追加スニペットには，以下の「括弧ペア」・「数字」・「ラテン文字」・「ギリシャ文字」・「ナブラと偏微分記号」の各号に掲げるものが追加登録されています．

### 括弧ペア

次の2通りのスニペットが登録されています．

- `\l<括弧名>` と `\r<括弧名>` を組み合わせた **`/lr<括弧名>`**．例えば，`\lparen`（ `(` ）と `\rparen` （ `)` ）を組み合わせた `()` が `/lrparen` として登録されています．
- `\left\l<括弧名>` と `\right\r<括弧名>` を組み合わせた **`\LR-<括弧名>`**．例えば，`\left\lparen`（ `\left(` ）と `\right\rparen` （ `)` ）を組み合わせた `\left( \right)` が `/LR-paren` として登録されています．  
ただし，`\left ~ \right` によって実際に伸縮するものしか登録していません．例えば，`\left\lVvert ~ \right\rVvert` はその中身の大きさにかかわらず伸縮しないため，`/LR-Vvert` は登録されていません．

### 数字

数字をより速く入力するために，全ての数字に対して，本体ファイルとは異なる prefix を登録しています．

例えば，サンセリフ・太字・立体の 2（ `𝟮` ＝ `\symbfsf{2}` ）は，本体ファイルでは `/mbfsanstwo` として登録されていましたが，この追加スニペットには `/bs-2` として登録されています．

なお，この「`bs`」は sym**b**f**s**fup に由来します．逆に言えば，`\symbfsfup` 相当の文字種の文字を入力したいと思ったら，それを圧縮した文字列である `bs` から始まる prefix をタイプすればよいと分かるわけです．

> [!IMPORTANT]
> **規則 1**  
> **一般に，文字種指定コマンドからの文字列の圧縮は，以下の変換に従って行います．**
> - sym は削除
> - **中字・太字情報：** bf → b
> - **セリフ・サンセリフ情報：** sf → s
> - **立体・イタリック体情報：** up → u，it → i
> - **その他の情報：** tt → tt，bb → bb，scr → sc，frak → fr

ただし，数字に限っては立体・イタリック体の区別がないため，立体・イタリック体情報である **`u`・`i` は省略します**．

本体ファイルの prefix 名と，追加スニペットにおける prefix 名の対応は，以下の通りです．

| 本体ファイルにおける prefix 名（* = zero, one, two, ...） | 追加スニペットに追加登録された prefix名（@ = 0, 1, 2, ...） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mbf* | /b-@ | \sym**b**fup | セリフ・太字 |
| /msans* | /s-@ | \sym**s**fup | サンセリフ・中字 |
| /mbfsans* | /bs-@ | \sym**b**f**s**fup | サンセリフ・太字 |
| /mtt* | /tt-@ | \sym**tt** | タイプライター体 |
| /Bbb* | /bb-@ | \sym**bb** | 黒板太字 |

> 例：`/b-1`（ `𝟏` ），`/s-1`（ `𝟣` ），`/bs-1`（ `𝟭` ），`/tt-1`（ `𝟷` ），`/bb-1`（ `𝟙` ）

### ラテン文字

数字と同様に，全てのラテン文字に対して，本体ファイルとは異なる prefix を登録しています．大枠は上記とほぼ同様です．

ただし数字とは対照的に，ラテン文字には立体・イタリック体の区別があるため，prefix 名には立体・イタリック体情報である `u`・`i` も含まれます．これは，以降のギリシャ文字・ナブラ・偏微分記号も同様です．

> [!IMPORTANT]
> **規則 2**  
> ところで，数式中の文字は，立体よりも常にイタリック体が優先されるのが[一般的でしょう](https://qiita.com/zr_tex8r/items/05dd9958169cd844975d)．言い換えれば，イタリック体は「標準的な」書体とみなすことができます．すると，イタリック体文字の prefix 中に，わざわざイタリック体である旨の `i` を明示するのは，煩わしいだけともいえるでしょう．  
> そこで，**`u`・`i`のうち標準的な方は省略してもよい**という規則を設けます．つまり，イタリック体を標準とするラテン文字では，`i` を省略することができます．


#### 立体

| 本体ファイルにおける prefix 名（* = A, a, B, b, ...） | 追加スニペットに追加登録された prefix名（* = A, a, B, b, ...） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mbf* | /bu-* | \sym**b**f**u**p | セリフ・太字 |
| /msans* | /su-* | \sym**s**fup | サンセリフ・中字 |
| /mbfsans* | /bsu-* | \sym**b**f**s**f**u**p | サンセリフ・太字 |
| /mtt* | /tt-* | \sym**tt** | タイプライター体 |
| /Bbb* | /bb-* | \sym**bb** | 黒板太字 |
| /mscr* | /sc-* | \sym**sc**r | 中字・スクリプト体 |
| /mbfscr* | /bsc-* | \sym**b**f**sc**r | 太字・スクリプト体 |
| /mfrak* | /fr-* | \sym**fr**ak | 中字・フラクトゥール |
| /mbffrak* | /bfr-* | \sym**b**f**fr**ak | 太字・フラクトゥール |

> 例：`/bu-R`（ `𝐑` ），`/su-R`（ `𝖱` ），`/bsu-R`（ `𝗥` ），`/tt-R`（ `𝚁` ），`/bb-R`（ `ℝ` ），`/sc-R`（ `ℛ` ），`/bsc-R`（ `𝓡` ），`/fr-R`（ `ℜ` ），`/bfr-R`（ `𝕽` ）

#### イタリック体

規則 2 に従い，`i` を含んだ prefix と，省略した prefix の2つを登録しています．ただし，`/bbi-*` は例外的に `/bbi-*` のみとします（立体・黒板太字の `/bb-*` とバッティングするため）．

| 本体ファイルにおける prefix 名（* = A, a, B, b, ...） | 追加スニペットに追加登録された prefix名（* = A, a, B, b, ...） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mit* | /i-*, /\* | \sym**i**t | セリフ・中字 |
| /mbfit* | /bi-*, /b-\* | \sym**b**f**i**t | セリフ・太字 |
| /mitsans* | /si-*, /s-\* | \sym**b**f**s**f**i**t | サンセリフ・中字 |
| /mbfitsans* | /bsi-*, /bs-\* | \sym**b**f**s**f**i**t | サンセリフ・太字 |
| /mitBbb* | /bbi-* | \sym**bbi**t | 黒板太字 |

> 例：`/d` （ `𝑑` ），`/b-d` （ `𝒅` ），`/s-d` （ `𝘥` ），`/bs-d` （ `𝙙` ），`/bbi-d` （ `ⅆ` ）

> [!TIP]
> `\symbbit` が有効なラテン文字は，D, d, e, i, j の5文字のみです．

### ギリシャ文字

ラテン文字と同様です．

#### 立体

| 本体ファイルにおける prefix 名（* = Alpha, alpha, Beta, beta, ...） | 追加スニペットに追加登録された prefix名（* = Alpha, alpha, Beta, beta, ...） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mup*, /up* | /u-* | \sym**u**p | セリフ・中字 |
| /mbf* | /bu-* | \sym**b**f**u**p | セリフ・太字 |
| /mbfsans* | /bsu-* | \sym**b**f**s**f**u**p | サンセリフ・太字 |
| /Bbb* | /bb-* | \sym**bb** | 黒板太字 |

> 例：`u-pi`（ `π` ），`bu-pi`（ `𝛑` ），`bsu-pi`（ `𝝿` ），`bb-pi`（ `ℼ` ），

> [!TIP]
> `\symbb` が有効なギリシャ文字は，γ, π, Γ, Π の4文字のみです．
> 

#### イタリック体

| 本体ファイルにおける prefix 名（* = Alpha, alpha, Beta, beta, ...） | 追加スニペットに追加登録された prefix名（* = Alpha, alpha, Beta, beta, ...） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mit* | /i-*, /\* | \sym**i**t | セリフ・中字 |
| /mbfit* | /bi-*, /b-\* | \sym**b**f**i**t | セリフ・太字 |
| /mbfitsans* | /bsi-*, /bs-\* | \sym**b**f**s**f**i**t | サンセリフ・太字 |

> 例：`pi`（ `𝜋` ），`b-pi`（ `𝝅` ），`bs-pi`（ `𝞹` ），

### ナブラと偏微分記号

> [!IMPORTANT]
> `unicode-math` では，`\nabla` と `\partial` は，それぞれ立体のナブラ（ `∇` ）と立体の偏微分記号（ `∂` ）に割り当てられています．そのため，**ナブラと偏微分記号については，例外的に立体を標準とみなします．**

#### 立体

立体が標準なので，ここでは `i` ではなく `u` の方を省略します．

| 本体ファイルにおける prefix 名（* = nabla, partial） | 追加スニペットに追加登録された prefix名（* = nabla, partial） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /* | /u-* | \sym**u**p | セリフ・中字 |
| /mbf* | /bu-*, /b-\* | \sym**b**f**u**p | セリフ・太字 |
| /mbfsans* | /bsu-*, /bs-\* | \sym**b**f**s**f**u**p | サンセリフ・太字 |

> 例：`/u-partial`（ `∂` ），`/b-partial`（ `𝛛` ），`/bs-partial`（ `𝞉` ）

#### イタリック体

| 本体ファイルにおける prefix 名（* = nabla, partial） | 追加スニペットに追加登録された prefix名（* = nabla, partial） | 対応する文字種指定コマンド | 文字種 |
|-|-|-|-|
| /mit* | /i-* | \sym**i**t | セリフ・中字 |
| /mbfit* | /bi-* | \sym**b**f**i**t | セリフ・太字 |
| /mbfitsans* | /bsi-* | \sym**b**f**s**f**i**t | サンセリフ・太字 |

> 例：`/i-partial`（ `𝜕` ），`/bi-partial`（ `𝝏` ），`/bsi-partial`（ `𝟃` ）


## ファイルの設置

全て単なるスニペットファイルですので，いつもの要領で設置すれば使用できます．

グローバルに使う場合は，`unicode-math-snippets.code-snippets`（+ 必要なら `additional.code-snippets` も）の中身を `latex.json` 内にコピペしてください．

特定プロジェクト等で使う場合は，`unicode-math-snippets_with-scope.code-snippets`（+ 必要なら`additional_with-scope.code-snippets` も）を `.vscode` ディレクトリ内に設置するなどしてください．

## その他

`01_mathopen.code-snippets` ～ `13_mathalpha.code-snippets` は，まず `macro_extract.py` によって https://github.com/latex3/unicode-math/blob/master/unicode-math-table.tex から抽出され，それらを手作業で手直ししたものです．

`unicode-math-snippets.code-snippets` および `unicode-math-snippets_with-scope.code-snippets` は，それらを結合したものです．

## ライセンス

MIT
