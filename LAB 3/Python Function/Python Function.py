def grams_to_ounces(grams):
  
    ounces = 28.3495231 * grams
    return ounces


gram_value = float(input("Enter weight in grams: "))
ounce_value = grams_to_ounces(gram_value)
print(f"{gram_value} grams is equal to {ounce_value:.2f} ounces")
