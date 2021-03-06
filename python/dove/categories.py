from collections import defaultdict


# BEGIN static data

# static definitions to create our store's collections from
_categories = {
    "Bedroom": {
        "Beds": {
            "types": ["Bed"],
        },
        "Benches": {
            "types": ["Bench"],
        },
        "Desks": {
            "types": ["Desk", "Hutch"],
        },
        "Chests": {
            "types": ["Chest"],
        },
        "Dressers": {
            "types": ["Dresser"],
        },
        "Headboards": {
            "types": ["Headboard"],
        },
        "Media Chests": {
            "types": ["Media Chest"],
        },
        "Nightstands": {
            "types": ["Nightstand"],
        },
        "Wardrobes & Vanities": {
            "types": ["Wardrobe", "Vanity", "Armoire"],
        },
    },
    "Dining": {
        "Buffets, Hutches, Curios": {
            "types": ["Buffet", "Hutch", "Curio"],
        },
        "Chairs & Stools": {
            "types": ["Stool", "Dining Chair", "Dining Bench"],
        },
        "Counter Height Tables": {
            "types": ["Counter Height Table"],
            "tags": ["Counter Height Table"],
        },
        "Dining Tables": {
            "types": ["Table"],
            "tags": ["Dining Table"],
        },
        "Kitchen Islands": {
            "types": ["Kitchen Island"],
        },
        "Servers & Carts": {
            "types": ["Kitchen Cart", "Server"],
        },
        "Dining Misc": {
            "types": ["Display Cabinet", "Mirror", "Lazy Susan", "Mini Server",
                      "Wine Cabinet", "Wine Rack", "Bench"]
        },
    },
    "Living": {
        "Cabinets": {
            "types": ["Storage Cabinet", "Cabinet"],
        },
        "Accent Chairs": {
            "types": ["Chair"],
        },
        "Chaises & Benches": {
            "types": ["Chaise", "Bench", "Storage Bench"],
        },
        "Coffee Tables":{
            "types": ["Coffee Table", "Coffee Table Set"],
            "tags": ["Coffee Table"],
        },
        "Futons": {
            "types": ["Futon"]
        },
        "Love Seats": {
            "types": ["Love Seat"]
        },
        "Ottomans": {
            "types": ["Ottoman", "Pouf"]
        },
        "Recliners": {
            "types": ["Recliner"]
        },
        "Sectionals": {
            "types": ["Sectional"]
        },
        "Side Tables": {
            "types": ["Side Table", "Sofa Table", "Console Table",
                      "Accent Table", "Nesting Table"]
        },
        "Sofas": {
            "types": ["Sofa"]
        },
        "Entertainment Consoles": {
            "types": [
                "Entertainment Console",
                "TV Console",
                "Pier Cabinet",
                "Bridge",
                "Hutch",
                "Media Cabinet",
            ]
        },
        "Shelves": {
            "types": ["Book Shelf", "Shelf"]
        }
    },
    "Home Office": {
        "Bookshelves": {
            "types": ["Book Shelf"],
        },
        "Desks": {
            "types": ["Desk"]
        },
        "File Cabinets": {
            "types": ["File Cabinet"]
        },
        "Buffets & Hutches": {
            "types": ["Desk Buffet", "Desk Hutch"],
        },
        "Office Chairs": {
            "types": ["Office Chair"]
        },
        "Office Tables": {
            "types": ["Office Table"]
        },
    },
    "Youth": {
        "Youth Beds": {
            "types": ["Bed"],
            "tags": ["Youth"]
        },
        "Bunk Beds": {
            "types": ["Bunk Bed"]
        },
        "Loft Beds": {
            "types": ["Loft Bed"]
        },
        "Trundle Beds": {
            "types": ["Trundle Bed", "Daybed"]
        },
        "Youth Chests": {
            "types": ["Chest"],
            "tags": ["Youth"]
        },
        "Youth Dressers": {
            "types": ["Dresser"],
            "tags": ["Youth"]
        },
        "Youth Nightstands": {
            "types": ["Nightstand"],
            "tags": ["Youth"]
        },
        "Youth Misc.":{
            "types": [
                "Bean Bag",
                "Bench",
                "Book Case",
                "Book Shelf",
                "Coat Rack",
                "Canopy",
                "Chair",
                "Desk",
                "Drawer",
                "Double Door Closet",
                "Futon",
                "Hutch",
                "Media Chest",
                "Mirror",
                "Office Chair",
                "Ottoman",
                "Shelf",
                "Table",
                "Vanity",
            ],
            # need to apply the Youth Misc tag when creating products
            "tags": ["Youth", "Youth Misc"],
        }
    },
    "Outdoor": {
        "Outdoor Seating": {
            "types": [
                "Outdoor Arm Chair",
                "Outdoor Armless Chair",
                "Outdoor Bench",
                "Outdoor Chair",
                "Outdoor Chaise",
                "Outdoor Love Seat",
                "Outdoor Sectional",
                "Outdoor Seating Set",
                "Outdoor Side Chair",
                "Outdoor Sofa",
                "Outdoor Ottoman",
            ]
        },
        "Outdoor Tables": {
            "types": [
                "Outdoor Coffee Table",
                "Outdoor Dining Table",
                "Outdoor Dining Set",
                "Outdoor End Table",
                "Outdoor Side Table",
                "Outdoor Table",
                "Fire Pit Table",
            ]
        },
        "Outdoor Accessories": {
            "types": [
                "Outdoor Fire Place",
                "Outdoor Canopy Daybed",
                "Outdoor Serving Cart",
            ]
        }
    },
    "Accessories": {
        "Accent Chests": {"types": ["Accent Chest"]},
        "Coat Racks": {"types": ["Coat Rack"]},
        "Lamps": {"types": ["Lamp"]},
        "Mirrors": {"types": ["Mirror"]},
        "Rec Room": {
            "types": [
                "Game Table",
                "Pool Table Set",
                "Rec Room Chair",
            ]
        },
        "Rugs": {"types": ["Rug"]},
        "Under Bed Storage": {"types": ["Under Bed Storage"]},
        "Wall Decor": {"types": ["Wall Decor"]},
    },
}

_valid_types = defaultdict(set)
for cat, cat_data in _categories.iteritems():
    for _subcat, subcat_data in cat_data.iteritems():
        for t in subcat_data['types']:
            _valid_types[cat].add(t)

aliases = {
    "bedframe": "Bed",
    "bookshelf": "Book Shelf",
    "endtable": "Sofa Table",
    "entertainmentconsole": "TV Console",
    "nightstand": "Nightstand",
    "pier": "TV Console",
}

# END static data

class InvalidProductTypeError(ValueError):
    pass

def is_valid(subcategory, category):
    """Is the given subcategory a valid value, and is contained in category?"""
    return subcategory in _categories[category]

def subcategories(category):
    return _categories[category]

def resolve(name, category):
    """Turn some bullshit like "Night stands" --> "Nightstand"
    <string> --> <a product type in our store>

    and also validate that it's a valid type for the category
    """
    # check if we have an alias for it
    # create a key that's all lowercase and strips any spaces
    k = name.lower().replace(' ', '')
    if k in aliases:
        name = aliases[k]

    if name not in _valid_types[category]:
        raise InvalidProductTypeError(
            "'%s' couldn't be resolved to a valid category string."
            " Update the types dict in '%s'" % (name, category))

    return name

