class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat0 = Cat('Bernie', 11)
cat1 = Cat('Percy', 2)
cat2 = Cat('Jordan', 5)

def sort_cats_by_age(*args):
    oldest_cat = args[0]
    oldest_age = args[0].age
    for cat in args:
        if cat.age > oldest_age:
            oldest_cat = cat
            oldest_age = cat.age

    return oldest_cat


old_fogey = sort_cats_by_age(cat0, cat1, cat2)

print(old_fogey.name, old_fogey.age)