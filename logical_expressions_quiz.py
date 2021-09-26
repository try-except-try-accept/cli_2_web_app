import random

from datetime import datetime
from atexit import register
from os.path import abspath
from hashlib import md5
from urllib.request import Request, urlopen
import sys


POINTS_NEEDED = 100

score = 0



def probability(chance):
    """???% chance of something happening..."""
    if random.randint(1, 100) > chance:
        return True
    else:
        return False


def random_cap(s):
    """RAnDOm CaSE a word"""
    new = ""
    mode = random.randint(0, 2)
    if mode == 0:
        return s[0].upper() + s[1:]
    elif mode == 1:
        return s[0].lower() + s[1:]
    else:
        for c in s:
            if random.randint(0, 1):
                new += c.upper()
            else:
                new += c
        return new


def add_random_index(string):
    """Add random indexing syntax"""
    return string + "[{}]".format(random.randrange(0, len(string)-2))

def create_question(points):
    """Construct a logical expression"""
    c = ""
    compound = False
    complete = False
    while not complete:

        logic_operators = [">", ">=", "<=", "<", "==", "==", "!="]
        math_operators = ["*", "-", "/", "+", "//", "%", "**"]
        strings = ['help', 'common', 'morale', 'predict', 'illusion', 'chop', 'award', 'graze', 'separate', 'work out', 'presentation', 'dynamic', 'script', 'grudge', 'dome', 'matter', 'animal', 'lump', 'tourist', 'tube', 'gossip', 'dividend', 'accurate', 'miracle', 'drown', 'wonder', 'creation', 'discovery', 'canvas', 'relief', 'broccoli', 'guilt', 'observer', 'invasion', 'philosophy', 'egg white', 'lunch', 'fax', 'cafe', 'curriculum', 'ferry', 'single', 'move', 'positive', 'parking', 'ditch', 'exact', 'round', 'mutation', 'lamp', 'exile', 'solo', 'casualty', 'resign', 'gravity', 'perforate', 'scenario', 'privilege', 'pier', 'spare', 'decay', 'pit', 'good', 'healthy', 'employ', 'tank', 'delete', 'depression', 'invite', 'band', 'ambiguous', 'corruption', 'theater', 'distance', 'knee', 'belly', 'reign', 'die', 'avant-garde', 'manual', 'established', 'expansion', 'risk', 'deep', 'accessible', 'integrity', 'transition', 'childish', 'division', 'arrogant', 'abnormal', 'retirement', 'criminal', 'litigation', 'sensation', 'consideration', 'law', 'height', 'mail', 'crevice', 'visit', 'belong', 'society', 'cream', 'system', 'cereal', 'sheet', 'fluctuation', 'tradition', 'king', 'filter', 'harass', 'sport', 'whole', 'curve', 'garage', 'ostracize', 'twin', 'thick', 'first-hand', 'thigh', 'continental', 'grace', 'wrap', 'articulate', 'accompany', 'crack', 'multiply', 'auditor', 'bee', 'teach', 'finger', 'way', 'give', 'enthusiasm', 'rich', 'tasty', 'complication', 'vote', 'unpleasant', 'harm', 'tolerant', 'exempt', 'percent', 'medium', 'arrest', 'evening', 'mud', 'cancel', 'aviation', 'audience', 'conspiracy', 'distant', 'finished', 'immune', 'elect', 'literature', 'club', 'market', 'onion', 'name', 'secretion', 'contradiction', 'photocopy', 'conscious', 'old', 'flesh', 'carrot', 'legislature', 'row', 'nursery', 'tip', 'bike', 'mouse', 'drag', 'teenager', 'correspond', 'appetite', 'cinema', 'tick', 'franchise', 'courtship', 'rate', 'sex', 'crossing', 'curl', 'stem', 'achievement', 'storage', 'sentiment', 'interactive', 'context', 'confuse', 'crime', 'behave', 'break in', 'genetic', 'pass', 'brain', 'warn', 'sticky', 'concert', 'ground', 'rhetoric', 'perfume', 'master', 'annual', 'reduction', 'provision', 'quote', 'maid', 'permanent', 'remind', 'tooth', 'husband', 'indirect', 'energy', 'deprivation', 'find', 'refuse', 'ready', 'wave', 'nature', 'forget', 'dilemma', 'director', 'anticipation', 'prince', 'campaign', 'dough', 'terrify', 'safari', 'rare', 'responsibility', 'amber', 'dollar', 'estimate', 'sign', 'deport', 'favor', 'trail', 'represent', 'merchant', 'number', 'falsify', 'despair', 'television', 'property', 'crown', 'jewel', 'fireplace', 'rehearsal', 'banner', 'brilliance', 'trace', 'monkey', 'blow', 'continuous', 'mile', 'promise', 'table', 'insert', 'gain', 'letter', 'voice', 'duck', 'collection', 'bar', 'staff', 'explode', 'shame', 'cup', 'packet', 'friend', 'bucket', 'practical', 'flock', 'short', 'fleet', 'threaten', 'vehicle', 'worm', 'hostility', 'sweet', 'manufacture', 'concentrate', 'qualified', 'flight', 'far', 'exit', 'feminine', 'stretch', 'sodium', 'carry', 'formal', 'seller', 'section', 'variety', 'overlook', 'tray', 'sheep', 'consciousness', 'budget', 'break down', 'decisive', 'tempt', 'argument', 'sea', 'weigh', 'operation', 'candle', 'timetable', 'approach', 'tiptoe', 'gem', 'party', 'pile', 'symbol', 'consumer', 'road', 'kit', 'soil', 'aquarium', 'muggy', 'climb', 'depressed', 'memorandum', 'sound', 'tap', 'increase', 'virgin', 'twilight', 'register', 'revive', 'cheat', 'aisle', 'sustain', 'guess', 'war', 'record', 'remark', 'drink', 'nut', 'bulb', 'slam', 'minute', 'debut', 'bench', 'competition', 'interest', 'narrow', 'robot', 'food', 'disorder', 'leash', 'background', 'challenge', 'printer', 'calendar', 'economy', 'volcano', 'stage', 'siege', 'family', 'load', 'mystery', 'fraction', 'wardrobe', 'concept', 'producer', 'long', 'career', 'lonely', 'rehabilitation', 'excess', 'financial', 'thesis', 'dish', 'speaker', 'folk', 'machinery', 'publication', 'sigh', 'color', 'hope', 'notice', 'rabbit', 'innocent', 'chase', 'embark', 'album', 'credibility', 'hemisphere', 'instrument', 'reliance', 'water', 'pack', 'confession', 'leaflet', 'drawing', 'heavy', 'accident', 'contrary', 'main', 'trench', 'breeze', 'south', 'rule', 'notion', 'shoot', 'secretary', 'discourage', 'referral', 'future', 'bean', 'tone', 'craft', 'green', 'claim', 'endure', 'dive', 'site', 'accent', 'exploration', 'extent', 'hotdog', 'buy', 'substitute', 'transform', 'seminar', 'march', 'wisecrack', 'opinion', 'digress', 'snub', 'army', 'profound', 'rebellion', 'tired', 'drum', 'abbey', 'confine', 'surround', 'management', 'loud', 'reactor', 'perceive', 'subject', 'add', 'thin', 'pupil', 'inhibition', 'sword', 'liver', 'necklace', 'incapable', 'ballot', 'relaxation', 'recommend', 'indication', 'talkative', 'deprive', 'wear', 'weapon', 'fastidious', 'exhibition', 'wording', 'chocolate', 'quest', 'dramatic', 'worker', 'wait', 'fade', 'faint', 'extend', 'production', 'frozen', 'court', 'sacrifice', 'interface', 'suffer', 'route', 'dull', 'bargain', 'excavation', 'branch', 'tile', 'palace', 'bundle', 'restrict', 'pitch', 'fuel', 'funny', 'critical', 'build', 'tear', 'anniversary', 'mutter', 'cousin', 'pick']

        strings = ["'"+random_cap(s)+"'" for s in strings] * 10

        q_type = random.randint(1,3)

        a = str(random.randint(1, 10))
        b = str(random.randint(1, 10))

        functions = ["len"]     

        if q_type == 2:

            many_string = random.randint(1, 3)

            if many_string == 1:

                logic_operators = logic_operators[4:]

                a = random.choice(strings)
                b = random.choice(strings + [a] * 10)
                if probability(50):
                    b = random_cap(a)

                if probability(50) and points > 25:

                    a = add_random_index(a)

                    if probability(50):
                        if probability(50):
                            b = "'" + chr(random.randint(97, 122)) + "'"
                            if random.randint(0, 1):
                                b = b.upper()
                        else:
                            b = "'" + eval(a) + "'"

                    else:
                        try:
                            b += "[{}]".format(b.index(eval(a)))
                        except ValueError:
                            if probability(50):
                                b = add_random_index(b)


                else:
                    logic_operators += ["in"]                       

            elif many_string == 2:
                a = random.choice(functions) + "(" + random.choice(strings) + ")"

            else:
                b = random.choice(functions) + "(" + random.choice(strings) + ")"

        op = random.choice(logic_operators)

        if op == "in":
            if probability(25):
                a = chr(random.randint(97, 122))
                a = "'" + random_cap(a) + "'"

        # when passed 20 pts
        # 50% chance of the q being compound

        if probability(50) and points > 20 and not compound:
            # store first half of expression
            save_a = a + " " + op + " " + b
            compound = True            
        else:
            if compound:
                # finish second half of expression
                save_b = a + " " + op + " " + b
                boolean_operators = ["or", "and"]
                if points > 35:
                    boolean_operators += ["or not", "and not"]
                a = save_a + " " + random.choice(boolean_operators)
                b = save_b                            
            complete = True
            

            
    if compound:
        op = ""
    question = a + " " + op + " " + b    
    
    return question


def capitalise(a):
    """Capitalise a word"""

    return a[0].upper() + a[1:]

def get_answer():
    """Get user to answer True or False"""
    answer = input().lower().strip()
    while answer not in ["true", "false", "t", "f", "q"]:
        answer = input("True or False? ").lower().strip()        

    if answer == "t":
        answer = "true"
    elif answer == "f":
        answer = "false"
    
    return capitalise(answer)


def check_answer(question, answer, score):
    """Check if user's answer is correct evaluation"""
    if str(eval(question)) == answer:
        print("Correct!")
        return 1

    else:
        print("Incorrect!")
        if score > 20:
            print("You lose a point!")
            return -1
            
        else:
            return 0



def main():

    print("""\nWelcome to............\n
******************************
LOGICAL EXPRESSIONS QUIZ!!!!!!
******************************\n\n
how much of a logical thinker are you?
""")

    print()
    print("Press CTRL+C to stop playing at any time - don't press X or else your score will not be saved!")
    print()

    print("Score {} points to win!".format(POINTS_NEEDED))
    array = None

    score = 0
    q_count = 0
    end = False
    try:
        while not end:
            q_count += 1
            q = create_question(score)
            print("\nQ{}:\t{}?".format(q_count, q))
            a = get_answer()
            #testing
            #a = random.choice([True, False])
            if a != "Q":

                score += check_answer(q, a, score)

                if q_count % 10 == 0:

                    string = "\n**** YOUR SCORE IS: {} *****".format(score)
                    print("*" * len(string))
                    print(string)
                    print("*" * len(string))

            else:
                print("\nYour correct answers: {}/{}\n".format(score, q_count))
                end = True


    except KeyboardInterrupt:
        pass

    print()
    if score >= POINTS_NEEDED:
        score = ((POINTS_NEEDED / q_count)) * 100
        print("You are a logical mastermind!... WELL DONE!")
        print("You won with a final score of {:.2f} ({} attempts)".format(score, q_count))
    else:
        score = ((score / POINTS_NEEDED) * 100) * 0.75
        print("You scored {:.2f} ({} attempts)".format(score, q_count))
    print()



from helpers import Mocker

m = Mocker()

print = m.print_wrapper
input = m.input_wrapper