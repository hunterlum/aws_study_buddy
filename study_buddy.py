import pandas as pd
from random import shuffle

class card():
    def __init__(self,service,category,question,answer):
        self.service = service
        self.category = category
        self.question = question
        self.answer = answer
        return None
    def get_service(self):
        return self.service
    def get_category(self):
        return self.category
    def get_question(self):
        return self.question
    def get_answer(self):
        return self.answer
class deck():
    def __init__(self,cards):
        self.new_cards = cards
        self.used_cards = list()
        self.drawn_card = None
        self.shuffle_deck()
        return None
    def draw_card(self):
        if not self.drawn_card:
            try:
                self.drawn_card = self.new_cards.pop()
                service = self.drawn_card.get_service()
                category = self.drawn_card.get_category()
                question = self.drawn_card.get_question()
                print(f'{service} --{category}\n{question}')
            except:
                print('Deck is empty, please shuffle or exit.')
        else:
            assert(False,"Logic Error -- Drawn card should be empty here")
        return None
    def flip_card(self):
        if self.drawn_card:
            print(self.drawn_card.get_answer())
            self.used_cards.append(self.drawn_card)
            self.drawn_card = None
        else:
            assert(False,"Logic Error -- Drawn card should NOT be empty here")
        return None
    def shuffle_deck(self):
        assert(self.drawn_card == None)
        shuffled_deck = self.new_cards+self.used_cards
        shuffle(shuffled_deck)
        self.new_cards = shuffled_deck
        self.used_cards = list()
        return None
class study_buddy():
    def __init__(self,faqs):
        self.question_bank = faqs
        self.deck = None
        return None
    def choose_deck(self):
        services = set(self.question_bank['Service'])
        services_mapping = {}
        for ct,service in enumerate(services):
            services_mapping[str(ct)] = service
            print(f'{str(ct)}: {service}')
        service_index = input('Select Service: ')
        print(f'\n{"-"*100}')
        
        try:
            cards = []
            for ct,row in self.question_bank[self.question_bank['Service']==services_mapping[service_index]].iterrows():
                cards.append(card(row['Service'],row['Category'],row['Question'],row['Answer']))
        except:
            print(f'\n{"-"*100}')
            print(f'\"{service_index}\" is not a valid value. Please try again.')
            self.choose_deck()

        self.deck = deck(cards)
        return None
    def study_deck(self):
        usr_input = None
        while not usr_input == 'exit':
            if usr_input == 'shuffle':
                self.deck.shuffle_deck()
                
            self.deck.draw_card()
            input('\n')
            self.deck.flip_card()
            prompt = [
                '',
                'Allowed Actions -- (exit|shuffle|continue)',
                'Next Action (continue): '
            ]
            usr_input = input('\n'.join(prompt))
            print(f'\n{"-"*100}')
        return None
    def study(self):
        usr_input = None
        while not usr_input == 'exit':
            self.choose_deck()
            self.study_deck()
            prompt = [
                '',
                'You have exited the current deck. Would you like to study more?',
                'Allowed Actions -- (exit|new_deck)',
                'Next Action (new_deck): '
            ]
            usr_input = input('\n'.join(prompt))
            print(f'\n{"-"*100}')
        return None

if __name__=='__main__':
    data = pd.read_csv('faqs.csv')

    #Initiates Study Buddy
    buddy = study_buddy(data)
    buddy.study()
