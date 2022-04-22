## Proxy ™

[![Maintainability](https://api.codeclimate.com/v1/badges/8d9db50cbbd5d9d039df/maintainability)](https://codeclimate.com/github/mnogom/proxy-tm/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8d9db50cbbd5d9d039df/test_coverage)](https://codeclimate.com/github/mnogom/proxy-tm/test_coverage)

### Description
Custom local http-proxy-server, that shows site [Hacker News](https://news.ycombinator.com/). This proxy modified text 
on html page. A symbol `™` is added to each six-letter word.

### How to install
```shell
$ git clone https://github.com/mnogom/proxy-tm
$ cd proxy-tm
$ make install
$ make test
```

### How to run
```console
$ make run
```

### Features
1. Add a symbol `™` each visible six-letter word
2. Overwrite all local paths for assets and urls
3. Don't touch text in css/js in page

### Examples
From source
```text
In the article they use the example of "Motherboard" and "Landlord" and seem to suggest that these are areas where the Google AI is making mistakes or being overly strict.
As a Google employee expressing my own opinion and observations of company culture, I can say that these are 100% not mistakes. Many Google employees are just so out of touch with the real world that they believe it is the duty of Google Docs to change the English language to exclude the words "landlord", "motherboard", and even "mother" in most contexts (sub with birthing person).
This may seem unbelievable, but the word "motherboard" is literally banned within Google and you are required to use "mainboard" instead. You are not allowed to use this word in documentation or code, and you're also not allowed to say it privately in chats or emails.
```
From proxy:
```text
In the article they use the example of "Motherboard" and "Landlord" and seem to suggest that these are areas where the Google™ AI is making™ mistakes or being overly™ strict™.
As a Google™ employee expressing my own opinion and observations of company culture, I can say that these are 100% not mistakes. Many Google™ employees are just so out of touch with the real world that they believe it is the duty of Google™ Docs to change™ the English language to exclude the words "landlord", "motherboard", and even "mother™" in most contexts (sub with birthing person™).
This may seem unbelievable, but the word "motherboard" is literally banned™ within™ Google™ and you are required to use "mainboard" instead. You are not allowed to use this word in documentation or code, and you're also not allowed to say it privately in chats or emails™.
```
