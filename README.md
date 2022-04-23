## Proxy ™

[![Maintainability](https://api.codeclimate.com/v1/badges/8d9db50cbbd5d9d039df/maintainability)](https://codeclimate.com/github/mnogom/proxy-tm/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8d9db50cbbd5d9d039df/test_coverage)](https://codeclimate.com/github/mnogom/proxy-tm/test_coverage)
[![python-ci](https://github.com/mnogom/proxy-tm/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/mnogom/proxy-tm/actions/workflows/python-ci.yaml)

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
1. Add a symbol `™` each visible six-letter word (text on page, values and placeholders for input)
2. Avoid urls, words with hyphens and apostrophes
3. Overwrite all local paths for assets and urls
4. Don't touch text in css/js
5. Modify `proxy_server/settings.py` to switch url for proxy
6. Modify `gunicorn.conf.py` to setup Gunicorn

### Examples

---
* #### /item?id=31130672

From source https://news.ycombinator.com/item?id=31130672:
```text
This was a really great read.

There's a few comments here saying something akin to "No, 
design trends are totally random, some hotshots decide they 
want to be different and then everyone else mindlessly follows". 
I got similar feedback when I wrote in an earlier HN comment my 
take  on why flat design is popular now. I actually empathize 
with the sentiment because it reminds me of how I used to feel 
about wine tasters. To me, all wine tastes equivalently like 
poison. So when people express their complex, nuanced wine 
preferences, it's easy for me to feel like they're pulling 
something out of their butts, just saying what they think 
they're supposed to say.

If my taste in everything was similar to my taste in wine, 
I would probably still believe this. But I've realized that 
when it comes to UI/UX design, I am one of the pretentious 
wine tasters. And I don't feel like I'm making stuff up or 
mindlessly following trends. The trends genuinely make sense 
to me; I think they'd happen in the same order in a parallel 
universe. Design is an optimization problem, and sometimes 
new technologies or patterns of human behavior change the 
optimal path for a wide spectrum of products, leading to trends, 
or what this author calls "vibe shifts".

Of course there are mindless trend followers, just as there are 
people who parrot opinions on wine they didn't really form themselves. 
They may be the majority. But they don't disprove the existence of 
something real.
```

From proxy http://127.0.0.1:8000/item?id=31130672:
```text
This was a really™ great read.

There's a few comments here saying™ something akin to "No, 
design™ trends™ are totally random™, some hotshots decide™ they 
want to be different and then everyone else mindlessly follows". 
I got similar feedback when I wrote in an earlier HN comment my 
take  on why flat design™ is popular now. I actually empathize 
with the sentiment because it reminds me of how I used to feel 
about wine tasters. To me, all wine tastes™ equivalently like 
poison™. So when people™ express their complex, nuanced wine 
preferences, it's easy for me to feel like they're pulling 
something out of their butts, just saying™ what they think 
they're supposed to say.

If my taste in everything was similar to my taste in wine, 
I would probably still believe this. But I've realized that 
when it comes to UI/UX design™, I am one of the pretentious 
wine tasters. And I don't feel like I'm making™ stuff up or 
mindlessly following trends™. The trends™ genuinely make sense 
to me; I think they'd happen™ in the same order in a parallel 
universe. Design™ is an optimization problem, and sometimes 
new technologies or patterns of human behavior change™ the 
optimal path for a wide spectrum of products, leading to trends™, 
or what this author™ calls "vibe shifts™".

Of course™ there are mindless trend followers, just as there are 
people™ who parrot™ opinions on wine they didn't really™ form themselves. 
They may be the majority. But they don't disprove the existence of 
something real.
```
---
* #### /item?id=13713480

From source https://news.ycombinator.com/item?id=13713480:
```text
The visual description of the colliding files, at 
http://shattered.io/static/pdf_format.png, is not very helpful 
in understanding how they produced the PDFs, so I took apart 
the PDFs and worked it out.

Basically, each PDF contains a single large (421,385-byte) JPG 
image, followed by a few PDF commands to display the JPG. The 
collision lives entirely in the JPG data - the PDF format is 
merely incidental here. Extracting out the two images shows two 
JPG files with different contents (but different SHA-1 hashes 
since the necessary prefix is missing). Each PDF consists of a 
common prefix (which contains the PDF header, JPG stream 
descriptor and some JPG headers), and a common suffix (containing 
image data and PDF display commands).
```

From proxy http://127.0.0.1:8000/item?id=13713480:
```text
The visual™ description of the colliding files, at 
http://shattered.io/static/pdf_format.png, is not very helpful 
in understanding how they produced the PDFs, so I took apart 
the PDFs and worked™ it out.

Basically, each PDF contains a single™ large (421,385-byte) JPG 
image, followed by a few PDF commands to display the JPG. The 
collision lives entirely in the JPG data - the PDF format™ is 
merely™ incidental here. Extracting out the two images™ shows two 
JPG files with different contents (but different SHA-1 hashes™ 
since the necessary prefix™ is missing). Each PDF consists of a 
common™ prefix™ (which contains the PDF header™, JPG stream™ 
descriptor and some JPG headers), and a common™ suffix™ (containing 
image data and PDF display commands).
```
---

