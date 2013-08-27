#!/usr/bin/env python
import re
import unittest


# To run the code in this file, run this command:
# > python pytut.py

# You will need to replace all of the places wher you see a "FIXME" to get this
# code working. You should look over the documentation on data structures before
# staring on this:
# http://docs.python.org/tutorial/datastructures.html


class TestSimpleEnv(unittest.TestCase):

    def test_a_list(self):
        print '\n\tlist'
        # A list works like an ArrayList in Java or std:vector in C++. The items
        # in the list do not have to have the same type, but they generally do.

        primes = [2,3,5,7,11]
        self.assertEqual( primes[0], 2 )
        self.assertEqual( len(primes), 5 )
        self.assertEqual( sum(primes), "FIXME" )

        # Let's print out a few of them:
        for prime in primes:
            if prime<6:
                print prime

        # Let's add something to the end of the list.
        primes.append(13)
        self.assertEqual( primes[-1], 13)

        # Now you can make a list of names. Make sure the third one is
        # 'Charlie'.
        names = "FIXME"
        self.assertEqual( names[2], 'charlie' )


    def test_dict(self):
        print '\n\tdict'
        # A dict works like HashMap in Java or std:map in C++. It maps
        # keys to values.
        fav_foods = {
            'vegetable': 'spinach',
            'fruit': 'apple',
            'meat': 'steak',
            'ice cream': 'mint chocolate chip',
            "FIXME": "FIXME",
        }
        for kind,label in fav_foods.iteritems():
            print "favorite %s : %s"%(kind,label)

        self.assertEqual( fav_foods['fruit'], 'apple' )
        # you need to add your favorite type of nut to fav_foods:
        self.assertTrue( 'nut' in fav_foods )

    def test_dict_of_lists(self):
        print '\n\tdicts of lists'
        # Here's some things I want to get at the grocery store. It is a dict
        # that maps department names to lists of items I want to buy in that
        # department:
        groceries = {
            'fruits': ['apple','banana'],
            'vegetables': ['avocado','onion','tomato','okra'],
            'cereal': ['granola','raisin bran','musli'],
            'dairy': ['skim milk','buttermilk'],
            'bulk foods': ['peanuts','black beans'],
            'meats':[],
        }

        self.assertEqual( groceries.get('fruits'), ['apple','banana'] )
        self.assertEqual( groceries.get('baking'), None )
        self.assertEqual( groceries['fruits'], ['apple','banana'] )
        # What happens when you uncomment the next line?
        # self.assertEqual( groceries['baking'], None )

        # iterating over a dictionary returns the keys
        for dept in groceries:
            print "%s: %r"%(dept,groceries[dept])

        # Let's sort the list of departements by the number of items we are
        # buying in each section. The department with the smallest nuber of
        # foods (meat) should be first, and the department with the most foods
        # (vegetables) should be last.
        # http://docs.python.org/library/functions.html#sorted may help you
        # decode this.
        sorted_keys = sorted(
                        groceries,
                        key=lambda label:len(groceries[label])
                        )
        self.assertEqual( sorted_keys[-1], 'vegetables' )
        self.assertEqual( sorted_keys[0], 'meats' )
        self.assertEqual( groceries[sorted_keys[0]], "FIXME" )

        # Now try counting how many leters are in each department's list.
        counts = {
                dept:sum(len(word) for word in items)
                for dept,items in groceries.iteritems()
                }
        self.assertEqual( counts['meats'], 0 )
        self.assertEqual( counts['fruits'], "FIXME" )

    def _vowel_ending(self, word):
        # A method whose name begins with an underscore is treated like it is
        # private by convention.

        # This method should return True if word ends with a vowel, and false
        # otherwise.
        # Big hint: http://docs.python.org/library/re.html
        # The functions search, match, split, findall, and sub could be useful
        # in this course.
        return "FIXME"

    def test_regexes(self):
        print '\n\tregular expressions'
        self.assertFalse( self._vowel_ending('book') )
        self.assertTrue( self._vowel_ending('movie') )
        self.assertFalse( self._vowel_ending('song') )
        self.assertTrue( self._vowel_ending('YMCA') )


if __name__ == '__main__':
    unittest.main()
