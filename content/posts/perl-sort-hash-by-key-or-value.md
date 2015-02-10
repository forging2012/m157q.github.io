Title: [Perl] Sort hash by key or value
Date: 2013-05-10 16:38
Author: m157q
Category: Perl
Tags: perl, Sort
Slug: perl-sort-hash-by-key-or-value

#In Perl5.16    
<!--more-->  
  
`%h = hash, $key = keys in %h`    
    
---  
  
##Sort by key    
  
```perl  
    #if key is int    
    
        # ascending    
        for $key (sort keys %hash) {say "$key: $hash{$key}";}    
    
        # descending    
        for $key (reverse sort keys %hash) {say "$key: $hash{$key}";}    
    
     #if key is str (represent number)    
    
        # ascending    
        for $key (sort {$a <=> $b;} keys %h) {say "$key: $h{$key}";}    
    
        # descending    
        for $key (sort {$b <=> $a;} keys %h) {say "$key: $h{$key}";}   
```  
    
---    
  
##Sort by value (int)  
  
```perl  
    #value of %h is int ($h{$key})  
    # ascending order  
    for $key (sort {$hash{$a} <=> $hash{$b};} keys %h) {say "$key: $h{$key}";}  
    
    # descending order  
    for $key (sort {$hash{$b} <=> $hash{$a};} keys %h) {say "$key: $h{$key}";}   
```  
  