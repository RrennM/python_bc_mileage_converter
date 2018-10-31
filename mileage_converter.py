print("How many kilometers did you cycle today?")
kms = input()
mile = float(kms) * 0.621371
# kms = str(kms)
# mile = str(mile)

# print("Okay, you said " + kms + " kilometers. That's about " + mile + " miles!")

round_mile = round(mile, 2)
print(f"Okay, you said {kms} kilometers. That's about {round_mile} miles!")