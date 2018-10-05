class MorseDecoder:
    # TODO: Добавить остальные буквы
    codes = {
        "._": "A",
        "_...": "B",
        "_._.": "C",
        "_..": "D",
        ".": "E",
        ".._.": "F",
        "__.": "G",
        "....": "H",
        "..": "I",
        ".___": "J",
        "_._": "K",
        "._..": "L",
        "__": "M",
        "_.": "N",
        "___": "O",
        ".__.": "P",
        "__._": "Q",
        "._.": "R",
        "...": "S",
        "_": "T",
        ".._": "U",
        "..._": "V",
        ".__": "W",
        "_.._": "X",
        "_.__": "Y",
        "__..": "Z",
        ".____": "1",
        "..___": "2",
        "...__": "3",
        "...._": "4",
        ".....": "5",
        "_....": "6",
        "__...": "7",
        "___..": "8",
        "____.": "9",
        "_____": "0",
    }

    def decode(self, cipher):
        a = cipher.split(" ")
        new_word = ""
        for k in a:
            new_symbol = self.codes[k]
            new_word += new_symbol
        return new_word
# Данная конструкция нужна для правильного импортировании модуля morse_code
if __name__ == "__main__":
    # создаем экземпляр класса
    decoder = MorseDecoder()
    # расшифрованные буквы
    decoded_word = decoder.decode("._ ..._ ...__")
    print(decoded_word)
