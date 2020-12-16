#### What is sitemgr ?
sitemgr stands for site manager. sitemgr offers very simple command
line bookmark functionalities. It offers the following features:

+ add a site to a bookmark list.
+ remove site from a bookmark list.
+ update a site.
+ list all site. 
+ tag renaming.

#### Installation
To install sitemgr follow above instructions
```jsunicoderegexp
git clone https://github.com/Godmind-BM/sitemgr.git
pip install virtualenv
virtualenv venv -p python3.6
source venv/bin/activate
pip install -r requirements.txt
``` 

#### Usage
##### Help feature
sitemgr  --help        show help message.<br/>
sitemgr &lt; command &gt; --help   show help message for a command

##### commands 
sitemgr add [options] url <br/>
sitemgr rm [options] site-tag <br/> 
sitemgr update [options] site-tg <br/>
sitemgr rename source-tag dest-tag <br/> 

