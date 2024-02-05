# from text.textnormalizer import norm
# from ukrainian_word_stress import Stressifier
# import regex
# import re
# from ipa_uk import ipa
# stressify = Stressifier()


# _whitespace_re = re.compile(r"\s+")
# def collapse_whitespace(text):
#     return re.sub(_whitespace_re, " ", text)


# def ukr_cleaners(text):
#     text = collapse_whitespace(text)
#     text = norm(text).lower()

#     text = regex.sub(r'[^\p{L}\p{N}\?\!\,\.\-\: ]', '', text)
#     return ipa(stressify(text), False)
