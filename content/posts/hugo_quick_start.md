---
title: "Hugo_quick_start"
date: 2021-10-10T19:20:35+08:00
author: "Max"
draft: false
---

## Install Hugo

### Mac - install with homebrew
```
$ brew install hugo
```

### Windows - install with [Scoop](https://scoop.sh/)

```
$ scoop install hugo
```


## Quick start
### Step 1: Create a New Site
```
$ hugo new site {name}
```



### Step 2: Add a Theme

We will use the [Loveit theme](https://hugoloveit.com/) here.
```
$ cd {name}
$ git submodule add https://github.com/dillonzq/LoveIt.git themes/LoveIt
```


### Step 3: Change the configuration

Copy below code to the config.toml.

```
baseURL = "http://example.org/"
# [en, zh-cn, fr, ...] determines default content language
defaultContentLanguage = "en"
# language code
languageCode = "en"
title = "My New Hugo Site"

# Change the default theme to be use when building the site with Hugo
theme = "LoveIt"

[params]
  # LoveIt theme version
  version = "0.2.X"

[menu]
  [[menu.main]]
    identifier = "posts"
    # you can add extra information before the name (HTML format is supported), such as icons
    pre = ""
    # you can add extra information after the name (HTML format is supported), such as icons
    post = ""
    name = "Posts"
    url = "/posts/"
    # title will be shown when you hover on this menu link
    title = ""
    weight = 1
  [[menu.main]]
    identifier = "tags"
    pre = ""
    post = ""
    name = "Tags"
    url = "/tags/"
    title = ""
    weight = 2
  [[menu.main]]
    identifier = "categories"
    pre = ""
    post = ""
    name = "Categories"
    url = "/categories/"
    title = ""
    weight = 3

# Markup related configuration in Hugo
[markup]
  # Syntax Highlighting (https://gohugo.io/content-management/syntax-highlighting)
  [markup.highlight]
    # false is a necessary configuration (https://github.com/dillonzq/LoveIt/issues/158)
    noClasses = false

```

### Step 4: Create your first post

```
$ hugo new posts/first_post.md
```

```
$ hugo serve
```

```
$ hugo
```
```
$ hugo --minify
```


```
$ git checkout -b gh-pages
$ git rm -rf .
$ echo "gh-pages" > "README.md"


```
