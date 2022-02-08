text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
key_words = ["average", "temperature", "distance"]
# Ciclo for para recorrer la cadena
for sentence in text:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break