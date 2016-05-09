"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

#   >>> Brand.query.get(8).name

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

#   >>> Model.query.filter_by(name = 'Corvette', brand_name = 'Chevrolet').all()

# Get all models that are older than 1960.

#   >>> Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

#   >>> Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

#   >>> Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

#   >>> Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

#   >>> Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

#   >>> Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = Model.query.filter(Model.year == year).all()

#     print [(m.name, m.brand_name, m.brand.headquarters) for m in model_info]

    for m in model_info:
        if m.brand:
            print "Model: {}; brand: {}; headquarters in: {}.".format(m.name, m.brand_name, m.brand.headquarters)
        else:
            print "Model: {}; brand: {}.".format(m.name, m.brand_name)

get_model_info(1960)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand.name, Model.name).outerjoin(Model).all()

    for brand, model in brands:
        if model:
            print "Brand: {}; model: {}.".format(brand, model)
        else:
            print "Brand: {}.".format(brand)

get_brands_summary()

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

"""This returns a query object; to query the brand table, would have to add .all(),
.first() or .one()."""

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

"""An association table is used to manage many to many relationships, with columns that
act as foreign keys relating back to the other tables' primary keys. Often the relationship
for association tables is defined in the db.relationship as the 'secondary' table."""

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    return Brand.query.filter(Brand.name.like('%mystr%')).all()


def get_models_between(start_year, end_year):
    
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all
