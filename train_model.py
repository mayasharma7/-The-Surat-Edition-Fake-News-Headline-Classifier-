import pandas as pd

fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")

print("Fake news:")
print(fake.head())

print("\nReal news:")
print(true.head())

print("\nFake shape:", fake.shape)
print("Real shape:", true.shape)