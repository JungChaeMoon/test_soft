from django.shortcuts import render
from django.views.generic.base import TemplateView
import models.research.textsum.seq2seq_attention
import models.research.textsum.data
def getsummary(article):

    mad = models.research.textsum.seq2seq_attention.main(article)
    return 'summary of ' + str(mad)


def view(request):

    article = 'The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet.'
    summary1 = getsummary(article)

    return render(request,'base.html', {'summary': summary1})
