Title: [CLI] manage /etc/group and /etc/gshadow
Date: 2014-08-12 20:45
Author: m157q
Category: Cli
Tags: unix, cli, GroupManagement, vigr, grpck, grpconv, gshadow
Slug: cli-manage-etcgroup-and-etcgshadow

+ `# vigr`  
    + edit `/etc/group` file  
+ `# grpconv`  
    + generate new `/etc/gshadow` file based on `/etc/group`  
+ `# grpck`  
    + cross-comparison the members in groups of `/etc/group` and `/etc/gshadow`, it will also detect wrong or useless syntax.  
    + (For me, it's a little bit like tell you the result of `vimdiff /etc/group /etc/gshadow` directly)  