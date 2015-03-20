Title: GitHub Talk - Advanced Git and CI in NCTU
Slug: github-talk-advanced-git-and-ci-in-nctu
Date: 2015-03-20 14:30:29
Authors: m157q
Category: Git
Tags: Git, GitHub
Summary: GitHub X CCCA X SITCON Talk in NCTU

## Look into .git directory

```
$ git init foo
$ cd foo
$ tree
```

```
.
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags
```

+ refs
    + HEAD, tag, branch
+ objects
    + blob, tree, commit
        + blob
            + type, bytes, content of blog`
            + `blob 13hello,world`
        + tree
            + main file directory for the project
            + tree: point to the next tree object
            + blob: ref name for blob object (one for every related object files for this tree)
        + commit
            + parent: point to the last commit
            + message: commit message
    + store files for git
    + SHA1 hash
    + Compressed
    + commit action will add a commit object and tree object into the objects
    + tree objects have filenames for blob objects
    + blob files which have exactly same content will be stored as the same hash not only in the same project but also among all users.

### Branch
+ branch just store the hash of the newest commit for that branch

### Tag
+ regular tags do not have hash value
+ be stored in refs/tags
+ just a text file contain the commit object hash
+ annotated tag
    + `git tag -a $tag_name`
    + tagger, annotation
    + has a hash value

## Webhook
+ use <http://requestb.in/> as payload url in github, so every time there's a event github will send event message to the payload url.
+ Travis CI
+ <https://github.com/muan/emoji>


## Misc
+ if you delete tree objects manually, `git fsck` will tell you what happened.
+ Git does not support empty directory
+ .gitkeep
+ Every files in Git are treated as binary, so the blob file is not just a plaintext file
+ git clone won't clone unreferenced files in default, but you can specify that.
+ git push/pull won't do anything about unreferenced files

```
$ watch -n .1 tree
```

## Git commands

```
git ls-tree
git ls-tree HEAD

git fsck

git show $tag_name --pretty=raw`

git rebase $branch

git reflog
// use reflog to get the hash or alias and use git reset to undo your actions

git gc
// delete useless files (unreferenced files) after 90 days when someone do the action
```

## Reference
+ [Example at NCTU by johndbritton · Pull Request #132 · muan/emoji · GitHub](https://github.com/muan/emoji/pull/132)
