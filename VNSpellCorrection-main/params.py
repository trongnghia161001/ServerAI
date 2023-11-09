PERCENT_NOISE = 0.3 # 0 - 2 word in 5-grams
NUM_CPUS = 12
NUM_PROCESSES = 12
RANDOM_SEED = 1301
MAXIMUM_TOKENS_PER_BATCH = 1024
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 32
DEVICE = "cpu"
BUCKET_SAMPLING = True
CHECKPOINT_FREQ = 50
PRINT_PER_ITER = 10
EPOCHS = 5
LOG = "./log"
PATIENCE = 5
MAX_LR = 5e-5
WARMUP_PERCENT = 0.05