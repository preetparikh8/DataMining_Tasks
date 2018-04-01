import matplotlib.pyplot as plt
from wordcloud import WordCloud

#WordCloud
text = open('crimenyctweets.txt').read()
wordcloud = WordCloud(stopwords='grand').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()