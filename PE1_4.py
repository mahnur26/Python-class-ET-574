#a) Create a variable price and assign it the value 99.99.
price=99.99
#b)Create a variable discountPercent and assign it the value 25.
discountPrice=25
#c)Create the variable markdown and assign it the value of discountPercent divided by 100 times the value of price
markdown=(discountPrice/100)*price
#d)Decrease the value of price by markdown.
newPrice=price-markdown
#e)Display the value of price (round to two decimal places).
print("new Price=$",round(newPrice,4))