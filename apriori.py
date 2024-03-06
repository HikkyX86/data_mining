from collections import defaultdict

class Apriori:
    def __init__(self, min_support=0.5, min_confidence=0.5):
        self.min_support = min_support
        self.min_confidence = min_confidence

    def fit(self, transactions):
        self.transactions = transactions
        self.itemsets = self.get_itemsets()
        self.frequent_itemsets = self.get_frequent_itemsets()

    def get_itemsets(self):
        itemsets = set()
        for transaction in self.transactions:
            for item in transaction:
                itemsets.add(frozenset([item]))
        return itemsets

    def get_frequent_itemsets(self):
        frequent_itemsets = defaultdict(int)
        itemsets = self.itemsets
        transactions = self.transactions

        for itemset in itemsets:
            for transaction in transactions:
                if itemset.issubset(transaction):
                    frequent_itemsets[itemset] += 1

        num_transactions = len(transactions)
        frequent_itemsets = {itemset: support / num_transactions for itemset, support in frequent_itemsets.items() if support / num_transactions >= self.min_support}
        return frequent_itemsets

    def generate_rules(self):
        rules = []
        for itemset in self.frequent_itemsets.keys():
            if len(itemset) > 1:
                self.generate_rules_from_itemset(itemset, itemset, rules)
        return rules

    def generate_rules_from_itemset(self, itemset, current_itemset, rules):
        for item in current_itemset:
            antecedent = current_itemset - set([item])
            confidence = self.frequent_itemsets[itemset] / self.frequent_itemsets[antecedent]
            if confidence >= self.min_confidence:
                rules.append((antecedent, itemset - antecedent, confidence))
                if len(antecedent) > 1:
                    self.generate_rules_from_itemset(itemset, antecedent, rules)

# Main
if __name__ == "__main__":
    transactions = [
    {'apple', 'banana', 'orange'},
    {'apple', 'banana'},
    {'banana', 'grape'},
    {'apple', 'orange'},
    {'orange', 'grape'},
    {'banana', 'orange'},
    {'apple', 'banana', 'grape'},
    {'banana', 'orange', 'grape'}
]
    
    apriori = Apriori(min_support=0.4, min_confidence=0.7)
    apriori.fit(transactions)
    print("Frequent Itemsets:")
    for itemset in apriori.get_itemsets():
        print(itemset)