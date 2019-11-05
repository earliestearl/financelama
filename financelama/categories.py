# -*- coding: utf-8 -*-

# If one of the keywords is found within the orderer or info column this column is associated with that transaction

categories = {
    'supermarket': ['rewe', 'coop', 'edeka', 'lidl', 'netto', 'norma', 'frukt', 'ica'],
    'rent': ['miete', 'miete', 'wohnung', 'etagenbeitrag'],
    'entertainment': ['netflix', 'spotify', 'ticket', 'konzert', 'museum', 'filmstaden'],
    'restaurant': ['restaurant', 'restaurant', 'bar', 'cafe', 'qstockholm'],
    'traffic': ['db', 'deutschebahn', 'train', 'deutsche bahn'],
    'income': ['gehalt', 'lohn', 'stipendium'],
    'cash': ['bankomat']
}


def get_category(identifier: str) -> str:
    """
    Finds suitable category for given identifier from look up table. If no
    matching category is found, 'other' as fallback will be returned.

    Parameters
    ----------
    identifier : str
        String which is used for finding category

    Returns
    -------
    category : str
    """
    for category, keywords in categories.items():
        # Check for each keyword
        for k in keywords:
            # Check if lower-case keyword is substring of lower-case identifier
            if identifier.lower().find(k.lower()) != -1:
                return category
    # Default value if no category was found
    return 'other'
