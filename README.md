# python-1st-grade
書籍「Python 1年生 (森 巧尚)」を読みながら書いたコードです。

Python1年生 第2版 体験してわかる！会話でまなべる！プログラミングのしくみ

https://amzn.asia/d/fb4ksOh

<img src="https://github.com/Tatsurou-Yajima/python-1st-grade/assets/44424270/e74dcfb6-5ec1-4653-aa7a-96863e73cbe0" width="500px">

## `__pycache__`ディレクトリを生成させない方法

Pythonのコードを実行すると、`__pycache__`ディレクトリが自動生成されることがあります。

`__pycache__`ディレクトリが存在すると、Pythonコードの実行時にbytecodeへのコンパイルを省略することができます。

`__pycache__`ディレクトリはあってもなくてもプログラムの実行には関係ありません。

（個人的にはない方がスッキリすると思います）

もしこの`__pycache__`が不要な場合は、以下の通り環境変数を指定してください。

```bash:ターミナル
echo PYTHONDONTWRITEBYTECODE=1
```
