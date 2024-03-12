from tqdm import tqdm

num = 0
for i in tqdm(range(10000000), desc='processing'):
    num = i
