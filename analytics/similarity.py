text_1 = 'tag1 ' * 10 + 'tag2 ' * 10 + 'tag3 ' * 10
text_2 = 'tag1 ' * 1 + 'tag2 ' * 1

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform((text_1, text_2))
result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
print(result_cos[0][1])


from collections import Counter

list_of_dicts = ([{'dari_ln_tattoo': 0.039689157475414384}, {'captain_partak': 0.004196760745207708}, {'prtck.sketch': 0.043875867537141115}, {'bst_tatts': 0.39542088425685956}, {'bst_tatts': 0.39542088425685956}, {'goran.serb.tattoo': 0.20781620851707877}, {'divotattoo8767': 0.09895367918218712}, {'saint_le': 0.050125113456619866}, {'one.two.tattoo': 0.2947989069878814}, {'tattoo_nhamon': 0.39542088425685956}, {'phoenix_tattooer': 0.13331861125572014}, {'alvol_tattooer': 0.1410849873821999}, {'marinadqtattoo': 0.06268901113765202}, {'marmi_tattoo': 0.16400176808152425}, {'kolshica101': 0.013466644627465987}, {'alexborum': 0.30887602753155774}, {'kolshica101': 0.013466644627465987}, {'tattoo_andrey_': 0.0847029677789122}, {'kolshica101': 0.013466644627465987}, {'hurtlandtattoo': 0.09865114910781725}, {'trendybum_luxtut': 0.02096594924650461}, {'kate_ger_tattoo': 0.22697795150796896}, {'tarasow13tattoo': 0.032514443129057366}, {'kom_tattoo': 0.16972909510027204}, {'morrganttattoo': 0.024693791718287}, {'alexborum': 0.30887602753155774}, {'ilina.tattoo': 0.11262851484258037}, {'mrtsh.tattoo': 0.14568024545487612}, {'annytattoomoscow': 0.053610618817659064}, {'one.two.tattoo': 0.2947989069878814}])

print({key: val for key, val in list_of_dicts})

print(a)