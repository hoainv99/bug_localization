import pandas as pd
df = pd.read_csv('data\BugLocalization-dataset-master\dataset\Eclipse_Platform_UI.txt', sep="\t")
df.to_csv('training_set\Eclipse_Platform_UI.csv', index=False)