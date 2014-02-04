formatieur = "%r %r %r %r"

print formatieur % (1, 2, 3, 4)
print formatieur % ("one", "two", "three", "four")
print formatieur % (True, False, False, True)
print formatieur % (formatieur, formatieur, formatieur, formatieur)
print formatieur % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)