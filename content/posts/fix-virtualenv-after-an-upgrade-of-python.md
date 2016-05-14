Title: Fix virtualenv after an upgrade of Python  
Slug: fix-virtualenv-after-an-upgrade-of-python  
Date: 2015-10-07 15:39:41  
Authors: m157q  
Category: Note  
Tags: Python, virtualenv  
Summary: Always forget how to do it after upgrading Python, so just write it down.  
  
## Steps  
  
```terminal  
$ cd ~/.virtualenvs  
$ find ${envname}/ -type l -delete  
$ virtualenv ${envname}  
```  
  
---  
  
## Script  
  
Here's a tiny script from [Fix python virtualenv after python update · GitHub](https://gist.github.com/tevino/1a557a0c200d61d4e4fb) for doing this.  
  
```sh  
fix_virtualenv.sh  
---  
#!/usr/bin/env bash  
ENV_PATH="$(dirname "$(dirname "$(which pip)")")"  
SYSTEM_VIRTUALENV="$(which -a virtualenv|tail -1)"  
  
echo "Ensure the root of current virtualenv:"  
echo "    $ENV_PATH"  
read -p "‼️  Say no if you are not sure (y/N) " -n 1 -r  
echo  
if [[ $REPLY =~ ^[Yy]$ ]]; then  
    echo "♻️  Removing old symbolic links......"  
    find "$ENV_PATH" -type l -delete -print  
    echo "💫  Creating new symbolic links......"  
    $SYSTEM_VIRTUALENV "$ENV_PATH"  
    echo "🎉  Done!"  
fi  
```  
  
### Steps  
  
```terminal  
$ source ~/.virtualenvs/${envname}/bin/activate.sh  
$ chmod u+x ./fix_virtualenv.sh  
$ ./fix_virtualenv.sh  
```  
  
---  
  
## References  
  
+ [Stéphane Wirtel - Read-Eval-Print Loop](http://wirtel.be/posts/en/2014/07/29/fix_virtualenv_python_brew/)  
+ [Fix python virtualenv after python update · GitHub](https://gist.github.com/tevino/1a557a0c200d61d4e4fb)  
  
