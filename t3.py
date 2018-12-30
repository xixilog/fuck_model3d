import shelve




with shelve.open('shelve.db') as db:
    db['eggs'] = 'eggs'
