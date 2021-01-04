from fxparser import ActionParser,PriceParser,SLParser,TPParser,UrgencyParser,ParserHelper, SymbolParser
from pathlib import Path

import emoji
def give_emoji_free_text(text):
    return emoji.get_emoji_regexp().sub(r'', text)

examples = [
    "samples/sample1.txt",
    "samples/sample2.txt",
    "samples/sample3.txt",
    "samples/sample4.txt",
    "samples/sample5.txt"
]

actionParser = ActionParser()
priceParser = PriceParser()
slParser = SLParser()
tpParser = TPParser()
urgencyParser = UrgencyParser()
helper = ParserHelper()

for item in examples:
    file_data = Path(__file__).parent.joinpath(item).read_text()
    print(item)
    # action = actionParser.parse_text(file_data)
    # sl = slParser.parse_text(file_data)
    # tp = tpParser.parse_text(file_data)
    # urgency = urgencyParser.parse_text(file_data)
    # price = priceParser.parse_text(file_data, tp, sl)
    # print(action)
    # print(price)
    # print(sl)
    # print(tp)
    # print(urgency)
    data = helper.parse_text(give_emoji_free_text(file_data))
    print(data)
    print("\n\n")
