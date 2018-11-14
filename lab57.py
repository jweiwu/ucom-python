# pip install wikipedia
import wikipedia

print wikipedia.summary('Pythonidae')
# print wikipedia.summary('eeeeeexxxxxx')
print wikipedia.summary('Cython')
print wikipedia.search('C++')

taipeiPage = wikipedia.page("Taipei")
print taipeiPage.title, taipeiPage.url
print taipeiPage.content
print taipeiPage.links[0]

wikipedia.set_lang('zh')
print wikipedia.summary('Taipei', sentences=4)
