# nineteen-code
A Python program made to debunk the idea of the "Quran 19 code".

# Background Information

In 2021, I made a TikTok account called [@KingYoshiyahu](https://www.tiktok.com/@kingyoshiyahu) where I discuss various religious topics (and sometimes math and coding) from the perspective of an atheist. [One of my videos](https://www.tiktok.com/@kingyoshiyahu/video/7051101222459444527) was on the topic of the ["Quran 19 code"](https://en.wikipedia.org/wiki/Quran_code), a supposed mathematical structure in the Quran based on multiples of 19. I argued that such patterns can be easily found in any text, if you look hard enough for them.

But on September 11, 2023, Alikhan Akhmetov DMed me with a link to [a web app](https://ahmetovalihan.pythonanywhere.com/english) he made to demonstrate the Quran 19 code, and challenged me to replicate 15 specific 19-based patterns that he found in the first chapter of the Quran. Composing a text that fits a specific pattern is, of course, much harder than finding patterns in a specific text, but I accepted his challenge.

(He also thankfully uploaded the code of his web app to [a GitHub repo](https://github.com/AlikhanAkhmetov1991/Site-and-scripts-for-mathematical-miracle-8.3/). It's apparently written in Flask. Neat.)

# Usage

To use, simply run `quran-miracle-finder.py` (preferably with [PyPy](https://www.pypy.org/), for speed).

The program generates random variants of the same 7-verse chapter (which talks about the 19 code in a meta way), and when it finds variants that replicate all 15 defined "miracles", it outputs them to a text file (grouped by first 4 verses).

# Example of a Miraculous Chapter

This is my favorite result from the program (formatted, and curated from many thousands of other options):

> **CHAPTER 1: THE RAIN MAN**
> 1. The "nineteen code" in the Quran does not point toward the Islamic god.
> 2. It's solely dumb luck.
> 3. What that does is referred to as "cherry picking" data.
> 4. It is purely an occurrence of a sharpshooter fallacy.
> 5. And for that matter, this thinking is silly.
> 6. Why is Allah super enticed by nineteen?
> 7. The way I see it, the god of Islam is really the Dustin Hoffman of deities!

This chapter replicates all 15 miracles presented on Alikhan Akhmetov's web app.

## Miracle 1

Write the following next to each other: the chapter number (1); then the index of each verse (1, 2, 3, 4, 5, 6, 7).

**11234567**

The result is a multiple of 19.

## Miracle 2

Write the following next to each other: the chapter number (1); then the number of verses (7); then the number of words (67).

**1767**

The result is a multiple of 19.

## Miracle 3

Write the following next to each other: the sum of the verse indices (1 + 2 + 3 + 4 + 5 + 6 + 7 = 28); then the number of words (67); then the number of letters (285); then the gematria value (23499).

**286728523499**

The result is a multiple of 19.

(NOTE: For the "gematria" value, each letter is substituted for the corresponding number in this table, and then added.)

| Letter | Gematria | Letter | Gematria | Letter | Gematria |
|:------:|:--------:|:------:|:--------:|:------:|:--------:|
|    A   |     1    |    J   |    10    |    S   |    100   |
|    B   |     2    |    K   |    20    |    T   |    200   |
|    C   |     3    |    L   |    30    |    U   |    300   |
|    D   |     4    |    M   |    40    |    V   |    400   |
|    E   |     5    |    N   |    50    |    W   |    500   |
|    F   |     6    |    O   |    60    |    X   |    600   |
|    G   |     7    |    P   |    70    |    Y   |    700   |
|    H   |     8    |    Q   |    80    |    Z   |    800   |
|    I   |     9    |    R   |    90    |        |          |

## Miracle 4

Write the following next to each other: the chapter number (1); then the number of verses (7); then the number of words in each verse (13, 4, 10, 9, 8, 7, 16).

**171341098716**

The result is a multiple of 19.

## Miracle 5

Write the following next to each other: the chapter number (1); then the number of verses (7); then the number of letters (285); then the gematria value (23499).

**1728523499**

The result is a multiple of 19.

## Miracle 6

Write the following next to each other: the chapter number (1); then the number of letters in each verse (56, 17, 43, 44, 35, 32, 58).

**156174344353258**

The result is a multiple of 19.

## Miracle 7

Write the following next to each other: the chapter number (1); then for each verse, the verse index, and the number of letters (1 56, 2 17, 3 43, 4 44, 5 35, 6 32, 7 58); then the number of letters (285).

**1156217343444535632758285**

The result is a multiple of 19.

## Miracle 8

Write the following next to each other: the chapter number (1); then for each verse, the verse index, and the number of letters *up to and including this verse* (1 56, 2 73, 3 116, 4 160, 5 195, 6 227, 7 285).

**115627331164160519562277285**

The result is a multiple of 19.

## Miracle 9

Write the following next to each other: the chapter number (1); then for each verse, the number of letters, and the gematria value (56 3651, 17 1933, 43 3322, 44 3803, 35 2804, 32 3304, 58 4682).

**1563651171933433322443803352804323304584682**

The result is a multiple of 19.

## Miracle 10

Write each part of Miracle 9 next to each other, but in a backwards order.

**4682583304322804353803443322431933173651561**

The result is a multiple of 19.

## Miracle 11

Write the following next to each other: the chapter number (1); then for each verse, the number of letters *up to and including this verse*, and the gematria *up to and including this verse* (56 3651, 73 5584, 116 8906, 160 12709, 195 15513, 227 18817, 285 23499).

**1563651735584116890616012709195155132271881728523499**

The result is a multiple of 19.

## Miracle 12

Write the following next to each other: the number of letters (285); then for each verse, the number of words, the number of letters, and the gematria value (13 56 3651, 4 17 1933, 10 43 3322, 9 44 3803, 8 35 2804, 7 32 3304, 16 58 4682).

**2851356365141719331043332294438038352804732330416584682**

The result is a multiple of 19.

## Miracle 13

Write the following next to each other: the chapter number (1); then for each verse, the verse index, the number of letters, and the gematria value (1 56 3651, 2 17 1933, 3 43 3322, 4 44 3803, 5 35 2804, 6 32 3304, 7 58 4682).

**11563651217193334333224443803535280463233047584682**

The result is a multiple of 19.

## Miracle 14

Write the following next to each other: the chapter number (1); then the number of verses (7); then the gematria value (23499); then for each verse, the verse index, the number of words, the number of letters, and the gematria value (1 13 56 3651, 2 4 17 1933, 3 10 43 3322, 4 9 44 3803, 5 8 35 2804, 6 7 32 3304, 7 16 58 4682).

**172349911356365124171933310433322494438035835280467323304716584682**

The result is a multiple of 19.

## Miracle 15

Write the following next to each other: the chapter number (1); then the number of verses (7); then for each verse, the verse index, the number of letters, and the gematria value of every letter written next to each other (take my word for this).

**17156200855095052005550360459502008580300901504605100506020070609502002006050019042008591003014093760421792001001006030530700430040230300320343500812002008120046051009100905659090542006011003859090700709320950741200144492009100703009053070015060333009090550356061100819070100860602005906130301370053515046609020081200401200200590200891002008950209507910010093030700632500870091001303018100300705905502009354270050950520055507582008550017009100559200200857604606910030140910090513030700200854300100200950860664015060645920095100**

The result is a multiple of 19.

# What Does This Prove?

Not much on its own, really. It proves you can create a piece of constrained writing using math and coding knowledge.

But Akhmetov's claim is that the composer of the Quran (be it Allah, Muhammad, or some secret third thing) intentionally placed these specific constraints on the text of the Quran (or at least the first chapter). Which seems highly unlikely, in my opinion. After all, who would intentionally use *these* specific constraints, and not others?

He also indirectly claimed on his website that I wouldn't be able to write a chapter that's just like the Quran, citing Surah 2:23-24. And yet, for this 19-based definition of "just like the Quran", it seems like I have.

# Future Ideas

* At the moment, this program is tailor-made to work with these specific verses and their variants, including hard-coding the solutions to many different modular equations. Perhaps in the future, I can modify this to work with any set of verses and their variants.
