from fxparser import FlagParser
from fxparser import FlagParserV2
from pathlib import Path
import tensorflow as tf

# flagParser = FlagParser()
flagParser2 = FlagParserV2()

# print(flagParser.detect_image(str(Path(__file__).parent.joinpath("samples/test.jpg"))))
data = flagParser2.detect_image(str(Path(__file__).parent.joinpath("samples/test.jpg")))
print(data)
# data["key"].print()

