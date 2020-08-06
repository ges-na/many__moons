from datetime import date
import random
import re
import os
from moon_phases import special_moons, moon_phases

abs_path = os.path.dirname(os.path.abspath(__file__))

def get_list_from_file(file):
    file_list = file.read()
    file_list = file_list.replace('\n', '')
    file_list = file_list.split(',')
    return file_list

word_lists = {}

with open(f'{abs_path}/aminals.txt') as file:  
    word_lists['animal'] = get_list_from_file(file)

with open(f'{abs_path}/superlative.txt') as file:  
    word_lists['superlative'] = get_list_from_file(file)

with open (f'{abs_path}/nouns.txt') as file:
    word_lists['nouns'] = get_list_from_file(file)


template_list = ['{superlative} {animal} Moon', '{superlative} {animal} {nouns} Moon', '{superlative} {nouns} Moon']
        

class MoonName():
    def __init__(self):
        self.set_many_moons_template()
        self.check_date()

    def get_name(self):
        if self.special_moon:
            return f'Tonight\'s moon is a {self.special_moon}! Make sure to go look!'
        elif self.todays_moon_phase:
            todays_moon_phase_template = self.template.format(**self.get_template_context())
            return f'{self.todays_moon_phase} {todays_moon_phase_template}'
        else:
            return self.template.format(**self.get_template_context())

    def set_many_moons_template(self, index=False):
        if index:
            self.template = template_list[index]
        else:
            self.template = random.choice(template_list)
        kwargs = self.get_template_kwargs()
        for kwarg in kwargs:
            if not hasattr(self, kwarg):
                setattr(self, kwarg, self.get_random_word(kwarg)) 

    def check_date(self):
        today = date.today()
        today_string = today.strftime('%Y-%-m-%-d')
        self.special_moon = special_moons.get(today)            
        #self.special_moon = 'test moon'
        self.todays_moon_phase = moon_phases.get(today)
        #self.todays_moon_phase = 'test'

    def get_random_word(self, category):
        category = ''.join([letter for letter in category if not letter.isdigit()])
        return random.choice(word_lists[category])

    def get_template_context(self):
        kwargs = self.get_template_kwargs()
        context = {}
        for kwarg in kwargs:
            context[kwarg] = getattr(self, kwarg)
        return context

    def get_template_kwargs(self):
        return re.findall('{(\w+)}', self.template)


def generate_moon():
    moon = MoonName()
    return moon.get_name()
