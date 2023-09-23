import hashlib
import itertools as it
import math
import random
from typing import Iterable, Iterator, Mapping, NamedTuple


# This program was made in response to a challenge from Alikhan Akhmetov
# to write a chapter with the same 19-related "miracles" as the first
# chapter of the Quran. He made a web app to verify each "miracle" for a
# given response:
# https://ahmetovalihan.pythonanywhere.com/english
# He also uploaded his code to GitHub, which is nice:
# https://github.com/AlikhanAkhmetov1991/Site-and-scripts-for-mathematical-miracle-8.3
# NOTE: The web app only allows for 7-verse chapters. For this reason, I
# fix the number of verses in my chapter at 7.


VERSE_BASES = [
    [
        "{there is no} {quran nineteen code}",
        "the {quran} {has no} {nineteen code}",
        "{the quran nineteen code} {is not} {miraculous}",
        "{the quran nineteen code} {is not} {real}",
        "{the quran nineteen code} {is not} {proof of} {allah}",
        "{the quran nineteen code} {is not} {proof of} islam",
        "{the quran nineteen code} {is not} {proof of} god",
        "{the quran nineteen code} {does not} {prove} {allah}",
        "{the quran nineteen code} {does not} {prove} islam",
        "{the quran nineteen code} {does not} {prove} god",
    ],
    [
        "{its} {a coincidence}",
        "all {it} is is {a coincidence}",
        "what {it} is is {a coincidence}",
        "{its} {nothing but} {a coincidence}",
        "all {it} is is {nothing but} {a coincidence}",
        "what {it} is is {nothing but} {a coincidence}",
        "{its} {coincidental}",
        "all {it} is is {coincidental}",
        "what {it} is is {coincidental}",
        "{its} {nothing but} {coincidental}",
        "all {it} is is {nothing but} {coincidental}",
        "what {it} is is {nothing but} {coincidental}",
    ],
    [
        "{its} {cherry picking}",
        "{its} {called} {cherry picking}",
        "{its} {only} {cherry picking}",
        "{it} {cherry picks}",
        "{it} {only} {cherry picks}",
        "{you are} {cherry picking}",
        "{you are} {only} {cherry picking}",
        "you {cherry pick}",
        "you {only} {cherry pick}",
        "what {it} is is {cherry picking}",
        "what {it} is is {only} {cherry picking}",
        "what {you are} doing is {cherry picking}",
        "what {you are} doing is cherry picking your {criteria}",
        "what {you are} doing is {called} {cherry picking}",
        "what {you are} doing is {called} cherry picking your {criteria}",
        "what {you are} doing is {only} {cherry picking}",
        "what {you are} doing is {only} cherry picking your {criteria}",
        "what {it} does is {cherry picks}",
        "what {it} does is {called} {cherry picking}",
        "what {it} does is {only} {cherry picking}",
        "what {it} does is {only} {cherry picks}",
        "what {its} doing is {cherry picking}",
        "what {its} doing is {called} {cherry picking}",
        "what {its} doing is {only} {cherry picking}",
    ],
    [
        "{its} {the texas sharpshooter fallacy}",
        "{its} {called} {the texas sharpshooter fallacy}",
        "{its} {like} {the texas sharpshooter fallacy}",
        "{its} {only} {the texas sharpshooter fallacy}",
        "{its} {an example} of {the texas sharpshooter fallacy}",
        "{its} {only} {an example} of {the texas sharpshooter fallacy}",
    ],
    [
        "{and also} {it} {is nonsense}",
        "{and also} {it} {is nonsense} {to me}",
        "{and also} {its} {nonsense}",
        "{and also} {its} {nonsense} {to me}",
        "{and also} {its} {only} {nonsense}",
        "{and also} {its} {only} {nonsense} {to me}",
        "{and also} the {idea} {is nonsense}",
        "{and also} {this} {idea} {is nonsense}",
        "{and also} the {idea} {is nonsense} {to me}",
        "{and also} {this} {idea} {is nonsense} {to me}",
    ],
    [
        "why is {allah} {so obsessed with} {nineteen}",
        "what makes {allah} {so obsessed with} {nineteen}",
        "what {causes} {allah} to be {so obsessed with} {nineteen}",
        "what is it that makes {allah} {so obsessed with} {nineteen}",
        "what is it which makes {allah} {so obsessed with} {nineteen}",
        "what is it that {causes} {allah} to be {so obsessed with} {nineteen}",
        "what is it which {causes} {allah} to be {so obsessed with} {nineteen}",
    ],
    [
        "is {allah} the {rain man} of {gods}",
        "is {allah} {basically} the {rain man} of {gods}",
        "is {allah} {only} the {rain man} of {gods}",
        "{allah} {seems like} the {rain man} of {gods}",
        "{allah} {seems like} the {rain man} of {gods} {to me}",
        "{to me} {allah} {seems like} the {rain man} of {gods}",
        "{its} {as if} {allah} is the {rain man} of {gods}",
        "{to me} {its} {as if} {allah} is the {rain man} of {gods}",
        "{its} {as if} {allah} is the {rain man} of {gods} {to me}",
    ],
]
SYNONYMS = {
    "a classic": [
        "a {classic_c}", "an {classic_v}",
    ],
    "a coincidence": [
        "a {coincidence_c}", "an {coincidence_v}", "luck", "dumb luck",
        "pure luck", "pure dumb luck", "pure chance",
    ],
    "and also": [
        "and", "{also}", "and {also}",
    ],
    "also": [
        "also", "besides", "for that matter", "not to mention",
        "on top of that", "plus",
    ],
    "an example": [
        "a {example_c}", "an {example_v}", "{a classic} {example}",
    ],
    "allah": [
        "allah", "the god of islam", "the muslim god", "the islamic god",
    ],
    "almost as if": [
        "almost {as if}", "{basically} {as if}",
    ],
    "as if": [
        "as if", "as though", "like",
    ],
    "basically": [
        "basically", "just", "kind of", "really", "sort of",
    ],
    "called": [
        "called", "known as", "referred to as",
    ],
    "causes": [
        "causes", "compels", "drives", "leads",
    ],
    "cherry pick": [
        "cherry pick", "cherry pick {criteria}",
        "cherry pick the {criteria}",
    ],
    "cherry picking": [
        "cherry picking", "cherry picking {criteria}",
        "cherry picking the {criteria}",
    ],
    "cherry picks": [
        "cherry picks", "cherry picks {criteria}",
        "cherry picks the {criteria}",
    ],
    "classic": [
        "{classic_c}", "{classic_v}",
    ],
    "classic_c": [
        "classic", "clear", "common", "perfect", "prime", "signature",
        "standard", "stock", "textbook", "typical",
    ],
    "classic_v": [
        "illustrative", "obvious", "unmistakable",
    ],
    "coincidence_v": [
        "accident", "{coincidental_v} event", "{coincidental_v} occurrence",
        "{coincidental_v} outcome", "{coincidental_v} result",
    ],
    "coincidence_c": [
        "coincidence", "fluke", "{coincidental_c} event",
        "{coincidental_c} occurrence", "{coincidental_c} outcome",
        "{coincidental_c} result",
    ],
    "coincidental": [
        "{coincidental_c}", "{coincidental_v}",
    ],
    "coincidental_c": [
        "chance", "coincidental", "lucky", "random",
    ],
    "coincidental_v": [
        "accidental", "unintended", "unintentional",
    ],
    "criteria": [
        "conditions", "criteria", "data", "facts", "figures", "info",
        "information", "miracles", "numbers", "requirements", "statistics",
    ],
    "does not": [
        "does not", "doesnt",
    ],
    "drawn": [
        "addicted", "attached", "drawn",
    ],
    "example": [
        "{example_c}", "{example_v}",
    ],
    "example_c": [
        "case",
    ],
    "example_v": [
        "example", "instance", "occurrence",
    ],
    "gods": [
        "deities", "divine beings", "gods", "higher beings",
        "supernatural beings", "supreme beings",
    ],
    "good_c": [
        "coherent", "decent", "good", "great", "reasonable", "sensible",
        "solid", "valid",
    ],
    "good_v": [
        "adequate", "amazing",
    ],
    "has no": [
        "does not have a", "doesnt have a", "has no",
    ],
    "idea": [
        "argument", "belief", "concept", "idea", "logic", "reasoning",
        "thinking", "thought", "view", "viewpoint",
    ],
    "intrigued": [
        "captivated", "enticed", "intrigued",
    ],
    "is nonsense": [
        "makes no sense", "is {nonsense}", "is {only} {nonsense}",
    ],
    "is not": [
        "is not", "isnt",
    ],
    "it": [
        "it", "{this}",
    ],
    "its": [
        "its", "{it} is",
    ],
    "like": [
        "a lot like", "much like", "like", "very much like",
        "{basically} like",
    ],
    "miraculous": [
        "a miracle", "extraordinary", "miraculous", "rare", "unusual",
    ],
    "nineteen": [
        "nineteen", "the {number} nineteen",
    ],
    "nineteen code": [
        "math miracle", "mathematical miracle", "nineteen code",
        "nineteen miracle",
    ],
    "nonsense": [
        "absurd", "confusing", "drivel", "foolish", "inane", "nonsense",
        "nonsensical", "ridiculous", "silly", "stupid", "weird",
        "utter nonsense", "inane drivel",
    ],
    "nothing but": [
        "completely", "entirely", "nothing but", "solely", "totally", "{only}",
    ],
    "number": [
        "integer", "number", "value", "value of",
    ],
    "obsessed": [
        "concerned", "fascinated", "obsessed", "preoccupied",
    ],
    "obsessed with": [
        "interested in", "into", "{intrigued} by", "{drawn} to",
        "{obsessed} about", "{obsessed} with",
    ],
    "only": [
        "just", "merely", "only", "purely", "simply",
    ],
    "proof": [
        "attestation", "evidence", "proof",
    ],
    "proof of": [
        "a case for", "a {good_c} case for", "an {good_v} case for",
        "confirmation of", "support for", "{proof} of", "{proof} for",
    ],
    "prove": [
        "authenticate", "back up", "confirm", "demonstrate", "establish",
        "point to", "point toward", "prove", "support", "validate",
    ],
    "quran": [
        "koran",
        "quran",
    ],
    "quranic": [
        "koranic",
        "quranic",
    ],
    "quran nineteen code": [
        "{quran} {nineteen code}", "{nineteen code} in the {quran}",
        "{quranic} {nineteen code}",
        "{nineteen code}", "{quran} code",
    ],
    "rain man": [
        "dustin hoffman", "rain man",
    ],
    "real": [
        "legitimate", "real", "true", "valid",
    ],
    "seems like": [
        "is", "is {basically}", "is like", "is {basically} like", "seems like",
        "{basically} seems like", "seems to be", "{basically} seems to be",
    ],
    "so": [
        "extra", "so", "so very", "super", "that", "this", "very",
    ],
    "so obsessed with": [
        "{obsessed with}", "{so} {obsessed with}",
    ],
    "the quran nineteen code": [
        "the {quran nineteen code}", "{this} {quran nineteen code}",
    ],
    "the texas sharpshooter fallacy": [
        "a texas sharpshooter fallacy", "the texas sharpshooter fallacy",
        "a sharpshooter fallacy", "the sharpshooter fallacy",
        "a clustering illusion", "the clustering illusion",
        "a clustering fallacy", "the clustering fallacy", "cognitive bias",
        "a cognitive bias",
    ],
    "there is no": [
        "there is no", "there is no such thing as the", "there is not a",
        "there is not any such thing as the", "there isnt a", "there isnt any",
        "there isnt any such thing as the", "theres no",
        "theres no such thing as the", "theres not a",
        "theres not any such thing as the",
    ],
    "this": [
        "that", "this",
    ],
    "to me": [
        "in my eyes", "in my opinion", "in my view", "the way i look at it",
        "the way i look at this", "the way i see it", "the way i see this",
        "to me",
    ],
    "you are": [
        "you are", "youre",
    ],
}


def cumsum(iterable: Iterable[int]) -> list[int]:
    """
    Return the cumulative sum of an iterable.

    Parameters
    ----------
    iterable : iterable of int
        Input iterable.

    Returns
    -------
    list of int
        Cumulative sum of `iterable`.
    """
    csum, carr = 0, []
    for val in iterable:
        csum += val
        carr.append(csum)
    return carr


def sum_of_products(*iterables: Iterable[int]) -> int:
    """
    Return the sum of the products of each group of items in parallel
    iterables.

    Parameters
    ----------
    *args
        These arguments should be iterables of integers. The items of
        each iterable will be multiplied together until the shortest
        iterable is exhausted, then the products will be summed
        together.

    Returns
    -------
    int
        Calculated sum of products.
    """
    return sum(math.prod(values) for values in zip(*iterables))


def count_letters(st: str) -> int:
    """
    Return number of letters in string.

    Parameters
    ----------
    st : str
        Input string.

    Returns
    -------
    int
        Number of letters in `st`.
    """
    return len([c for c in st if c.isalpha()])


STANDARD_GEMATRIA = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
    "j": 10, "k": 20, "l": 30, "m": 40, "n": 50, "o": 60, "p": 70, "q": 80,
    "r": 90, "s": 100, "t": 200, "u": 300, "v": 400, "w": 500, "x": 600,
    "y": 700, "z": 800,
}


def calculate_gematria(st: str, mapping: Mapping[str, int]) -> int:
    """
    Calculate the gematria value of a string, according to a certain
    mapping of letters to numbers.

    The calculated gematria value is case-insensitive; the string is
    converted to lowercase before the value is calculated.

    Parameters
    ----------
    st : str
        Input string.
    mapping : mapping of {str : int}
        Mapping of letters to gematria values. Letters in the mapping
        should be lowercase.

    Returns
    -------
    int
        Calculated gematria value of `st`.
    """
    return sum(mapping.get(c, 0) for c in st.lower())


def compile_synonyms(synonyms: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    Prepare a collection of synonyms for use with the `generate_phrases`
    function.

    Synonyms for some words may contain other words which are to be
    replaced with synonyms. This function replaces those words in each
    synonym with every combination of their synonyms, and places them
    back into the collection of synonyms.

    Using circular synonym references is advised against, as it will
    likely result in an infinite loop or exception.

    Parameters
    ----------
    synonyms : dict of {str : list of str}
        Input synonyms collection.

    Returns
    -------
    dict of {str : list of str}
        Compiled synonyms collection.
    """
    while True:
        replace_synonyms = any(
            "{" in syn
            for synset in synonyms.values()
            for syn in synset
        )
        if not replace_synonyms:
            break

        for entry, synset in synonyms.items():
            synonyms[entry] = list(
                generate_phrases(synset, synonyms, False)
            )

    return synonyms


def generate_phrases(
        bases: list[str],
        synonyms: dict[str, list[str]],
        replace_synonyms: bool = True,
) -> Iterator[str]:
    """
    Generate a collection of phrases by taking a list of base phrases
    and replacing certain words with each combination of their synonyms.

    In each base phrase, the words to replace with synonyms will be in
    braces `{like this}`. For each corresponding synonym, the
    brace-enclosed string in the base will be replaced with that
    synonym, and the result will be yielded.

    Parameters
    ----------
    bases : list of str
        List of base strings to replace synonyms in.
    synonyms : dict of {str: list of str}
        Input synonyms collection.
    replace_synonyms : bool, default True
        If true, compile synonyms before starting.

    Yields
    ------
    str
        Phrase generated.

    Examples
    --------
    >>> bases = ["{language} is {flexible}",
    ...         "{language} is a {flexible} thing"]
    >>> synonyms = {"language": ["language", "speech", "vocabulary"],
    ...            "flexible": ["flexible", "fluid"]}
    >>> print([phrase for phrase in generate_phrases(bases, synonyms)])
    ['language is flexible', 'language is fluid', 'speech is flexible',
    'speech is fluid', 'vocabulary is flexible', 'vocabulary is fluid',
    'language is a flexible thing', 'language is a fluid thing',
    'speech is a flexible thing', 'speech is a fluid thing',
    'vocabulary is a flexible thing', 'vocabulary is a fluid thing']
    """
    phrases = set()

    if replace_synonyms:
        synonyms = compile_synonyms(synonyms)

    for base in bases:
        if "{" not in base:
            phrases.add(base)
            yield base
            continue

        keys, values = zip(*[
            (key, value)
            for key, value in synonyms.items()
            if f"{{{key}}}" in base
        ])

        for v in it.product(*values):
            phrase = base.format(**dict(zip(keys, v)))
            if phrase not in phrases:
                phrases.add(phrase)
                yield phrase


# NOTE: Precalculating the gematria/word count/letter count/etc. of a
# verse will speed up the calculations of the miracle numbers.
class VerseProps(NamedTuple):
    phrase: str
    gematria: int
    word_count: int
    letter_count: int
    letter_gematria_string: str


def get_verse_props(verse: str) -> VerseProps:
    """
    Create a `VerseProps` namedtuple from a single verse.

    Parameters
    ----------
    verse : str
        Input verse.

    Returns
    -------
    VerseProps
        Properties of verse.
    """
    # Keep only
    words = [
        "".join(c for c in w if c.isalpha())
        for w in verse.strip().split()
        if w.strip()
    ]
    verse = " ".join(words)

    return VerseProps(
        phrase=verse,
        gematria=calculate_gematria(verse, STANDARD_GEMATRIA),
        word_count=len(words),
        letter_count=len("".join(words)),
        letter_gematria_string="".join(
            str(calculate_gematria(c, STANDARD_GEMATRIA))
            for word in words
            for c in word
        ),
    )


# NOTE: For a 7-verse chapter, the only chapter numbers that make
# Miracle 1 work are those that are congruent to 1 mod 19. I decided to
# fix the chapter at 1, because who the hell cares?
def miracle_01(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 1. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Verse index

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    indices = "".join(f"{i}" for i in range(1, len(surah) + 1))
    return int(f"{chapter}{indices}")


# NOTE: For a Chapter 1, and a 7-verse chapter, and assuming a 2-digit
# number of words, Miracle 2 only works if the number of words is
# congruent to 10 mod 19 (10, 29, 48, 67, or 86).
def miracle_02(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 1. The following parts are concatenated in
    order:
    * Chapter number
    * Number of verses in chapter
    * Number of words in chapter

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    word_count = sum(verse.word_count for verse in surah)
    return int(f"{chapter}{verse_count}{word_count}")


def miracle_03(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 3. The following parts are concatenated in
    order:
    * Sum of indices of verses
    * Number of words in chapter
    * Number of letters in chapter
    * Gematria value of chapter

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    word_count = sum(verse.word_count for verse in surah)
    letter_count = sum(verse.letter_count for verse in surah)
    gematria = sum(verse.gematria for verse in surah)
    # Triangular numbers FTW
    verse_sum = verse_count * (verse_count + 1) // 2
    return int(f"{verse_sum}{word_count}{letter_count}{gematria}")


def miracle_04(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 4. The following parts are concatenated in
    order:
    * Chapter number
    * Number of verses in chapter
    * For each verse:
       * Number of words in verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    word_counts = "".join(f"{verse.word_count}" for verse in surah)
    return int(f"{chapter}{verse_count}{word_counts}")


def miracle_05(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 5. The following parts are concatenated in
    order:
    * Chapter number
    * Number of verses in chapter
    * Number of letters in chapter
    * Gematria value of chapter

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    letter_count = sum(verse.letter_count for verse in surah)
    gematria = sum(verse.gematria for verse in surah)
    return int(f"{chapter}{verse_count}{letter_count}{gematria}")


def miracle_06(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 6. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Number of letters in verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_letters = "".join(f"{verse.letter_count}" for verse in surah)
    return int(f"{chapter}{verse_letters}")


def miracle_07(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 7. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Verse index
       * Number of letters in verse
    * Number of letters in chapter

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_stats = "".join(
        f"{index}{verse.letter_count}"
        for index, verse in enumerate(surah, 1)
    )
    letter_count = sum(verse.letter_count for verse in surah)
    return int(f"{chapter}{verse_stats}{letter_count}")


def miracle_08(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 8. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Verse index
       * Number of letters up to and including this verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    letter_counts = cumsum([verse.letter_count for verse in surah])
    verse_stats = "".join(
        f"{index}{letter_count}"
        for index, letter_count in enumerate(letter_counts, 1)
    )
    return int(f"{chapter}{verse_stats}")


def miracle_09(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 9. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Number of letters in verse
       * Gematria value of verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_stats = "".join(
        f"{verse.letter_count}{verse.gematria}"
        for verse in surah
    )
    return int(f"{chapter}{verse_stats}")


def miracle_10(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 10. The following parts are concatenated in
    order:
    * For each verse in reverse order:
       * Gematria value of verse
       * Number of letters in verse
    * Chapter number

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_stats = "".join(
        f"{verse.gematria}{verse.letter_count}"
        for verse in reversed(surah)
    )
    return int(f"{verse_stats}{chapter}")


def miracle_11(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 11. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Number of letters up to and including this verse
       * Gematria value up to and including this verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    letter_counts = cumsum([verse.letter_count for verse in surah])
    gematrias = cumsum([verse.gematria for verse in surah])
    verse_stats = "".join(
        f"{letter_count}{gematria}"
        for letter_count, gematria in zip(letter_counts, gematrias)
    )
    return int(f"{chapter}{verse_stats}")


def miracle_12(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 12. The following parts are concatenated in
    order:
    * Number of letters in chapter
    * For each verse:
       * Number of words in verse
       * Number of letters in verse
       * Gematria value of verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    letter_count = sum(verse.letter_count for verse in surah)
    verse_stats = "".join(
        f"{verse.word_count}{verse.letter_count}{verse.gematria}"
        for verse in surah
    )
    return int(f"{letter_count}{verse_stats}")


def miracle_13(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 13. The following parts are concatenated in
    order:
    * Chapter number
    * For each verse:
       * Verse index
       * Number of letters in verse
       * Gematria value of verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_stats = "".join(
        f"{index}{verse.letter_count}{verse.gematria}"
        for index, verse in enumerate(surah, 1)
    )
    return int(f"{chapter}{verse_stats}")


def miracle_14(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 14. The following parts are concatenated in
    order:
    * Chapter number
    * Number of verses in chapter
    * Gematria value of chapter
    * For each verse:
       * Verse index
       * Number of words in verse
       * Number of letters in verse
       * Gematria value of verse

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    gematria = sum(verse.gematria for verse in surah)
    verse_stats = "".join(
        f"{index}{verse.word_count}{verse.letter_count}{verse.gematria}"
        for index, verse in enumerate(surah, 1)
    )
    return int(f"{chapter}{verse_count}{gematria}{verse_stats}")


def miracle_15(surah: list[VerseProps], chapter: int = 1) -> int:
    """
    Calculate miracle number 15. The following parts are concatenated in
    order:
    * Chapter number
    * Number of verses in chapter
    * For each verse:
       * Verse index
       * Number of letters in verse
       * For each letter in this verse:
              * Gematria value of letter

    Parameters
    ----------
    surah : list of VerseProps
        Chapter to calculate the miracle number of.
    chapter : int, default 1
        Chapter number of chapter.

    Returns
    -------
    int
        Calculated miracle number.
    """
    verse_count = len(surah)
    verse_stats = "".join(
        f"{index}{verse.letter_count}{verse.letter_gematria_string}"
        for index, verse in enumerate(surah, 1)
    )
    return int(f"{chapter}{verse_count}{verse_stats}")


MIRACLES = [
    miracle_01, miracle_02, miracle_03, miracle_04, miracle_05, miracle_06,
    miracle_07, miracle_08, miracle_09, miracle_10, miracle_11, miracle_12,
    miracle_13, miracle_14, miracle_15,
]


print("Compiling synonyms...")
SYNONYMS_COMPILED = compile_synonyms(SYNONYMS)
print("Generating phrases...")
VERSE_GROUPS = [
    [
        get_verse_props(phrase)
        for phrase in generate_phrases(bases, SYNONYMS_COMPILED, False)
        # NOTE: This enforces Assumptions 3 and 4, which I describe
        # later.
        if 10 <= count_letters(phrase) < 100
        and 1000 <= calculate_gematria(phrase, STANDARD_GEMATRIA) < 10000
    ]
    for bases in VERSE_BASES
]


verse_group_lengths = [len(verse_group) for verse_group in VERSE_GROUPS]
verse_groups_count = math.prod(verse_group_lengths)
print(f"# of verses per verse group: {verse_group_lengths}")
print(f"# of verse groups: {verse_groups_count:_}")
print(
    "Expected # of miraculous chapters:",
    f"~{verse_groups_count // 19 ** 15:_}"
)


# NOTE: Up to this point, I've enforced a few assumptions:
# 1. The chapter number is 1
# 2. The number of verses in the chapter is 7
# 3. The number of letters in each verse is a 2-digit number
# 4. The gematria of each verse in a 4-digit number

# I've also made a few other assumptions that are not enforced:
# 5. The number of words in the chapter is a 2-digit number
# 6. The number of letters in the chapter is a 3-digit number
# 7. The gematria of the chapter is a 5-digit number
# 8. The number of letters in the first 4 verses is a 3-digit number
# 9. The gematria of the first 4 verses is a 5-digit number

# Assumptions 1 and 4 helped me derive that the number of words in the
# chapter must be congruent to 10 (mod 19), which guarantees Miracle 2.
# The rest of the assumptions helped me write a few modular equations
# that are true iff certain miracles are replicated. Here they are, with
# a..g = number of letters in each verse, and h..n = gematria of each
# verse:

# MIRACLES 3 AND 5
# 3a + 3b + 3c + 3d + 3e + 3f + 3g + h + i + j + k + l + m + n = 15
# MIRACLE 6
# 7a + 9b + 17c + 11d + 6e + 5f + g = 3
# MIRACLE 7
# 13a + 2b + 9c + 8d + 12f + 13g = 17
# MIRACLE 8
# if number of letters in the first 3 verses is a 3-digit number:
#     5a + 2b + 16c + 12d + 5e + 7f + g = 11
# if number of letters in the first 3 verses is a 2-digit number:
#     13a + 7b + 16c + 12d + 5e + 7f + g = 13
# MIRACLE 9
# 6a + 4b + 9c + 6d + 4e + 9f + 6g + h + 7i + 11j + k + 7l + 11m + n = 8
# MIRACLE 10
# 10a + 15b + 13c + 10d + 15e + 13f + 10g + 12h + 18i + 8j + 12k + 18l
# + 8m + 12n = 18
# MIRACLE 11
# if number of letters in the first 3 verses is a 3-digit number
# and gematria in the first 3 verses is a 5-digit number:
#     9a + 12b + 14c + 4d + 9e + 16f + 3g + 7h + 17i + 11j + 14k + 3l
#     + 18m + n = 15
# if number of letters in the first 3 verses is a 3-digit number:
# and gematria in the first 3 verses is a 4-digit number:
#     14a + b + 5c + 4d + 9e + 16f + 3g + 3h + 4i + 11j + 14k + 3l + 18m
#     + n = 11
# if number of letters in the first 3 verses is a 2-digit number:
# and gematria in the first 3 verses is a 5-digit number:
#     4a + 10b + 14c + 4d + 9e + 16f + 3g + 3h + 4i + 11j + 14k + 3l
#     + 18m + n = 11
# if number of letters in the first 3 verses is a 2-digit number:
# and gematria in the first 3 verses is a 4-digit number:
#     4a + 16b + 5c + 4d + 9e + 16f + 3g + 14h + 16i + 11j + 14k + 3l
#     + 18m + n = 3
# MIRACLE 13
# 9a + 12b + 16c + 15d + e + 14f + 6g + 11h + 2i + 9j + 12k + 16l + 15m
# + n = 14

# (These equations may look complicated, but they're just simplified
# versions of straightforward equations for each miracle number.)

# Once I had these equations, I solved them, so I could derive which
# values for each verse's letter count/gematria (mod 19) would work for
# at least these miracles. This way, I could guarantee that I only
# search through chapters that are at least mostly miraculous. These
# equations are hardcoded at a few points in the program.

# TODO: Generalize this program, such that it derives and solves these
# modular equations on its own (which could, in theory, let one generate
# an entire book where these miracles work with each chapter!)


def main():
    first_verses = [
        random.choice(verse_group) for verse_group in VERSE_GROUPS[:3]
    ]
    verse_1, verse_2, verse_3 = first_verses

    # NOTE: We use slightly different modular equations depending on the
    # cumulative values of these properties.
    letter_count_is_big = cumsum(
        verse.letter_count for verse in first_verses
    )[2] >= 100
    gematria_is_big = cumsum(
        verse.gematria for verse in first_verses
    )[2] >= 10000

    # Choose a random verse 4 with the right letter count
    v4_letter_count_m19 = sum_of_products(
        [
            verse_1.letter_count,
            verse_2.letter_count,
            verse_3.letter_count,
            1,
        ],
        [10, 8, 14, 0]
        if letter_count_is_big else
        [6, 15, 14, 1]
    ) % 19
    verse_4 = random.choice([
        verse for verse in VERSE_GROUPS[3]
        if verse.letter_count % 19 == v4_letter_count_m19
        and (
            # NOTE: This enforces Assumption 9.
            sum(verse.gematria for verse in first_verses)
            + verse.gematria >= 10000
        )
    ])
    first_verses.append(verse_4)

    # Shuffle the rest of the verse groups
    for verse_group in VERSE_GROUPS[4:]:
        random.shuffle(verse_group)

    miraculous_chapters = []
    # For each choice of verse 5
    for i, verse_5 in enumerate(VERSE_GROUPS[4]):
        print(
            f"{i}/{len(VERSE_GROUPS[4])}",
            " " * 20,
            end="\r"
        )

        # HACK: Throughout my testing, when I've found a group of
        # miraculous chapters, there's usually at least one early in the
        # group. So if I've searched through 5,000 choices of verse 5
        # and haven't found any miraculous chapters, I assume there are
        # none with these first 4 verses. (I don't know if this leads to
        # a faster search, but it certainly *feels* faster.)
        if not miraculous_chapters and i >= 5000:
            print("Retrying...", " " * 20, end="\r")
            return

        constraint_items =  [
            verse_1.letter_count,
            verse_2.letter_count,
            verse_3.letter_count,
            verse_5.letter_count,
            verse_1.gematria,
            verse_2.gematria,
            1,
        ]

        # NOTE: Depending on our choice of verse 5, our choice of verses
        # 3, 4, and 5 could be invalidated. If this happens, we must
        # skip this choice of verse 5.
        v3_gematria_m19 = sum_of_products(
            constraint_items,
            [14, 0, 11, 16, 7, 6, 9]
            if letter_count_is_big and gematria_is_big else
            [16, 7, 15, 16, 13, 16, 3]
            if letter_count_is_big and not gematria_is_big else
            [8, 10, 11, 16, 13, 16, 4]
            if not letter_count_is_big and gematria_is_big else
            [8, 1, 15, 16, 6, 17, 11]
        ) % 19
        if verse_3.gematria % 19 != v3_gematria_m19:
            continue

        v4_gematria_m19 = sum_of_products(
            constraint_items,
            [14, 3, 4, 4, 15, 8, 13]
            if letter_count_is_big and gematria_is_big else
            [3, 12, 1, 4, 1, 10, 8]
            if letter_count_is_big and not gematria_is_big else
            [14, 1, 4, 4, 1, 10, 6]
            if not letter_count_is_big and gematria_is_big else
            [14, 3, 1, 4, 11, 14, 15]
        ) % 19
        if verse_4.gematria % 19 != v4_gematria_m19:
            continue

        v5_gematria_m19 = sum_of_products(
            constraint_items,
            [5, 8, 15, 15, 0, 18, 16]
            if letter_count_is_big else
            [12, 10, 15, 15, 0, 18, 0]
        ) % 19
        if verse_5.gematria % 19 != v5_gematria_m19:
            continue

        # Narrow down our options for verse 6
        v6_letter_count_m19 = sum_of_products(
            constraint_items,
            [15, 9, 3, 10, 0, 0, 4]
            if letter_count_is_big else
            [13, 3, 3, 10, 0, 0, 14]
        ) % 19
        v6_gematria_m19 = sum_of_products(
            constraint_items,
            [15, 9, 14, 18, 12, 13, 10]
            if letter_count_is_big and gematria_is_big else
            [13, 2, 10, 18, 6, 3, 16]
            if letter_count_is_big and not gematria_is_big else
            [3, 2, 14, 18, 6, 3, 10]
            if not letter_count_is_big and gematria_is_big else
            [3, 11, 10, 18, 13, 2, 3]
        ) % 19
        v6_candidates = [
            verse for verse in VERSE_GROUPS[5]
            if verse.letter_count % 19 == v6_letter_count_m19
            and verse.gematria % 19 == v6_gematria_m19
        ]

        # Narrow down our options for verse 7
        v7_letter_count_m19 = sum_of_products(
            constraint_items,
            [17, 10, 4, 1, 0, 0, 2]
            if letter_count_is_big else
            [14, 1, 4, 1, 0, 0, 17]
        ) % 19
        v7_gematria_m19 = sum_of_products(
            constraint_items,
            [13, 10, 4, 6, 3, 11, 6]
            if letter_count_is_big and gematria_is_big else
            [5, 1, 7, 6, 17, 9, 11]
            if letter_count_is_big and not gematria_is_big else
            [13, 12, 4, 6, 17, 9, 13]
            if not letter_count_is_big and gematria_is_big else
            [13, 10, 7, 6, 7, 5, 4]
        ) % 19
        v7_candidates = [
            verse for verse in VERSE_GROUPS[6]
            if verse.letter_count % 19 == v7_letter_count_m19
            and verse.gematria % 19 == v7_gematria_m19
        ]

        for verse_6 in v6_candidates:
            partial_chapter = first_verses + [verse_5, verse_6]
            # NOTE: Some of our ways for narrowing down our options for
            # verse 7 depend on our choice of verse 6. Therefore, we
            # take the original list of options for verse 7 and filter
            # them again here.
            v7_candidates_filtered = v7_candidates.copy()

            # This ensures Miracle 2 will work
            word_count = sum(verse.word_count for verse in partial_chapter)
            v7_candidates_filtered = [
                verse for verse in v7_candidates_filtered
                if (word_count + verse.word_count) % 19 == 10
            ]
            if not v7_candidates_filtered:
                continue

            # Miracles that are guaranteed to work here:
            # 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13
            # This ensures the rest of the miracles will work
            # NOTE: I couldn't come up with a neat equation that works
            # for these miracles as well as the others.
            for miracle in (miracle_04, miracle_12, miracle_14, miracle_15):
                v7_candidates_filtered = [
                    verse for verse in v7_candidates_filtered
                    if miracle(partial_chapter + [verse]) % 19 == 0
                ]
                if not v7_candidates_filtered:
                    break
            if not v7_candidates_filtered:
                continue

            # Now our choices of verse 7 should work for every miracle
            for verse_7 in v7_candidates_filtered:
                chapter: list[VerseProps] = partial_chapter + [verse_7]
                chapter_text = "/".join(verse.phrase for verse in chapter)
                print(chapter_text)

                # Verify that all miracles indeed work for this chapter
                miracle_numbers = [miracle(chapter) for miracle in MIRACLES]
                replications = sum(n % 19 == 0 for n in miracle_numbers)
                assert replications == len(MIRACLES)

                # This is a miraculous chapter!
                miraculous_chapters.append(chapter_text)

    if miraculous_chapters:
        print(
            f"Found {len(miraculous_chapters)} miraculous chapters "
            "with these first 4 verses:"
        )
        chapters_id = "/".join(verse.phrase for verse in first_verses)
        print(chapters_id)

        # Output chapters to specially-named text file
        chapters_hash = hashlib.shake_128(
            chapters_id.encode("utf-8"),
            usedforsecurity=False
        ).hexdigest(19)  # Get it?
        print(f"Writing {chapters_hash}.txt...")
        with open(f"{chapters_hash}.txt", "w", encoding="utf-8") as f:
            f.writelines(chapter + "\n" for chapter in miraculous_chapters)
        print("Done.")
    else:
        print("Starting over...", " " * 20, end="\r")


if __name__ == "__main__":
    # We can keep this running as long as we like, and it'll keep
    # finding miraculous chapters!
    while True:
        main()
