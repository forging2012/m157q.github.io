Title: Compiler Design Week 3
Slug: compiler-design-week-3
Date: 2015-03-10 15:47:17
Authors: m157q
Category: Course
Tags: Cousre, Compiler
Summary: Note for Compiler Design Course in NTHU - Week 3

## 2015/03/10

### Left-Recursion Grammar & Right-Recursion Grammar
+ 兩者可以互轉
+ Left-Recursion => Left Associate, Right-Recursion => Right Associate.

#### Left-Recursion Conversion
```
S -> Sα | β

to

S  -> βS'
S' -> αS' | ɛ
```

### Parser for a Grammar
+ Top-down Parser / LL(1) Parser
+ Bottom-up Parser / LR(1) Parser

---

## Chapter 3 - Regular Expression

Regular Expresssion aka Regular Grammar, Regular Language, Regular, Regex

---
