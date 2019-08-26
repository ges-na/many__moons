import ipdb
import random
import re

def get_list_from_file(file):
    file_list = file.read()
    file_list = file_list.replace('\n', '')
    file_list = file_list.split(',')
    return file_list

word_lists = {}

with open('aminals.txt') as file:  
    word_lists['animal'] = get_list_from_file(file)


with open('superlative.txt') as file:  
    word_lists['superlative'] = get_list_from_file(file)

with open ('nouns.txt') as file:
    word_lists['nouns'] = get_list_from_file(file)

# superlative = ['super', 'dorky', 'scintillating']
# animal = ['wolf', 'stork', 'chinchilla']
#word_lists['adj'] = ['blood', 'red', 'fight']
template_list = ['{superlative} Moon', '{superlative} {animal} Moon', '{animal} Moon', '{superlative} {animal} {nouns} Moon', '{superlative} {nouns} Moon']
        
#def moonName():
#    name = random.choice(superlative) + ' ' + random.choice(animals) + ' ' + random.choice(adj) + ' Moon'
#    print(name)

#moonName()


class MoonName():
    def __init__(self):
#        self.superlative = random.choice(superlative)
#        self.animal = random.choice(animals) 
#        self.adj = random.choice(adj)
        self.set_template()

    def get_name(self):
        return self.template.format(**self.get_template_context())

    def set_template(self, index=False):
        if index:
            self.template = template_list[index]
        else:
            self.template = random.choice(template_list)
        kwargs = self.get_template_kwargs()
        for kwarg in kwargs:
            if not hasattr(self, kwarg):
                setattr(self, kwarg, self.get_random_word(kwarg)) 

    def get_random_word(self, category):
        category = ''.join([letter for letter in category if not letter.isdigit()])
        return random.choice(word_lists[category])

    def get_template_context(self):
        kwargs = self.get_template_kwargs()
        context = {}
        for kwarg in kwargs:
            context[kwarg] = getattr(self, kwarg)
        return context
        #return {
            #'superlative': self.superlative,
            #'animal': self.animal,
            #'adj': self.adj
        #}

    def get_template_kwargs(self):
        return re.findall('{(\w+)}', self.template)

#        return '{superlative} {animal} {adj} moon'.format(
#            superlative=self.superlative,
#            animal=self.animal,
#            adj=self.adj,
#        )


def start_moon(moon_count):
    affirmative = ['', 'y', 'yes', 'yes thanks', 'yes please']
    if moon_count <= 0:
        print('Would you like to name a moon?')
        print('yes thanks')
        print('\n')
        print('      OR')
        print('\n')
        print('            no please')
        moon_answer = input('-->').lower()
    if moon_count >= 1:
        print('Another moon?')
        moon_answer = input('-->').lower()
    if moon_answer in affirmative:
        moon_count += 1
        moon = MoonName()
        moon.set_template(index=3)
        print(moon.get_name())
        start_moon(moon_count)
    else:
        print('goodbye then')

start_moon(0)

