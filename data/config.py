from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
BOT2_TOKEN = env.str("BOT2_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")