# irma-probe-tutorial

This tutorial will show you how to create a simple probe for [IRMA](https://github.com/quarkslab/irma).
Our example probe will use [balbuzard](http://www.decalage.info/python/balbuzard) a malware analysis tools to extract patterns from a submitted file.

The probe creation process is splitted in 4 parts, each part is in a specific branch to allow you to easily skip steps and correct yourself.

## Level 0
(Your start point)(branch balbuzard-level0)

to finish level 0 your goal is to copy skeleton files in your new probe directory

## Level 1
(branch balbuzard-level1)

level 1 consists in replacing Skeleton names by your new probe names, and also fill metadata like
Author, Version ...

## Level 2
(branch balbuzard-level2)

level2 consists in handling module dependencies and returning a simple result.

## Level 3
(branch balbuzard-level3)

level3 add a specific method for the analysis.
